#!/usr/bin/env python3
"""
Static site generator for Knowledge Engine.

Reads Markdown posts with YAML frontmatter from posts/ and writes a complete
static site to site/. No framework, no npm — just `markdown` and `PyYAML`.

Usage:
    python3 build.py                 # build with config.json
    BASE_PATH= python3 build.py      # build for local preview (no path prefix)

Read counts come from the GoatCounter API when both env vars are set:
    GOATCOUNTER_CODE        your site code, e.g. "knowledge-engine"
    GOATCOUNTER_API_TOKEN   an API token with "read statistics" permission
Without them the build still succeeds; counts render as "—".
"""

import datetime as dt
import html
import json
import os
import re
import shutil
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

import markdown
import yaml

ROOT = Path(__file__).resolve().parent
POSTS_DIR = ROOT / "posts"
OUT_DIR = ROOT / "site"
THEME = ROOT / "theme.css"

MD_EXTENSIONS = ["extra", "sane_lists", "smarty", "toc"]
FILENAME_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-(.+)\.md$")


# --------------------------------------------------------------------------
# config
# --------------------------------------------------------------------------

def load_config():
    cfg = json.loads((ROOT / "config.json").read_text(encoding="utf-8"))
    # Env overrides, so CI and local preview can differ without editing config.
    if "BASE_PATH" in os.environ:
        cfg["base_path"] = os.environ["BASE_PATH"]
    if os.environ.get("GOATCOUNTER_CODE"):
        cfg["goatcounter_code"] = os.environ["GOATCOUNTER_CODE"]
    cfg["base_path"] = cfg.get("base_path", "").rstrip("/")
    cfg["base_url"] = cfg.get("base_url", "").rstrip("/")
    return cfg


# --------------------------------------------------------------------------
# posts
# --------------------------------------------------------------------------

def slugify(value):
    value = re.sub(r"[^a-z0-9]+", "-", str(value).strip().lower())
    return value.strip("-") or "untitled"


def parse_post(path):
    """Parse one Markdown file. Returns a dict, or raises ValueError."""
    raw = path.read_text(encoding="utf-8")
    if not raw.startswith("---"):
        raise ValueError(f"{path.name}: missing YAML frontmatter block")
    parts = raw.split("---", 2)
    if len(parts) < 3:
        raise ValueError(f"{path.name}: frontmatter block is not closed")

    try:
        front = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError as exc:
        raise ValueError(f"{path.name}: frontmatter is not valid YAML — {exc}")
    if not isinstance(front, dict):
        raise ValueError(f"{path.name}: frontmatter must be a mapping")

    body = parts[2].lstrip("\n")

    m = FILENAME_RE.match(path.name)
    if not m:
        raise ValueError(f"{path.name}: filename must be YYYY-MM-DD-slug.md")
    file_date, file_slug = m.group(1), m.group(2)

    title = front.get("title")
    if not title:
        raise ValueError(f"{path.name}: frontmatter needs a title")

    date_value = front.get("date", file_date)
    if isinstance(date_value, dt.datetime):
        date = date_value.date()
    elif isinstance(date_value, dt.date):
        date = date_value
    else:
        try:
            date = dt.date.fromisoformat(str(date_value)[:10])
        except ValueError:
            raise ValueError(f"{path.name}: date must be YYYY-MM-DD")

    topics = front.get("topics") or []
    if isinstance(topics, str):
        topics = [t.strip() for t in topics.split(",")]
    topics = [str(t).strip() for t in topics if str(t).strip()]

    md = markdown.Markdown(extensions=MD_EXTENSIONS)
    return {
        "title": str(title),
        "date": date,
        "slug": front.get("slug") or file_slug,
        "topics": topics,
        "summary": str(front.get("summary", "")).strip(),
        "status": str(front.get("status", "published")).strip().lower(),
        "html": md.convert(body),
        "source_file": path.name,
    }


def load_posts():
    if not POSTS_DIR.is_dir():
        return [], []
    posts, problems = [], []
    for path in sorted(POSTS_DIR.glob("*.md")):
        try:
            post = parse_post(path)
        except ValueError as exc:
            problems.append(str(exc))
            continue
        if post["status"] != "published":
            continue
        post["url_path"] = f"/posts/{post['slug']}/"
        posts.append(post)
    posts.sort(key=lambda p: (p["date"], p["slug"]), reverse=True)
    return posts, problems


# --------------------------------------------------------------------------
# read counts (GoatCounter)
# --------------------------------------------------------------------------

def fetch_views(cfg, since):
    """
    Return {url_path: visitor_count}. Empty dict when unconfigured or on any
    failure — analytics must never break a build.
    """
    code = cfg.get("goatcounter_code") or os.environ.get("GOATCOUNTER_CODE", "")
    token = os.environ.get("GOATCOUNTER_API_TOKEN", "")
    if not code or not token:
        return {}

    base = f"https://{code}.goatcounter.com/api/v0/stats/hits"
    start = f"{since.isoformat()}T00:00:00Z"
    counts, exclude, pages = {}, [], 0

    try:
        while pages < 20:  # hard cap: 20 * 100 paths is plenty, and bounds the loop
            params = [("start", start), ("limit", "100")]
            params += [("exclude_paths", p) for p in exclude]
            params.append(("path_by_name", "true"))
            req = urllib.request.Request(
                base + "?" + urllib.parse.urlencode(params, doseq=True),
                headers={
                    "Authorization": f"Bearer {token}",
                    "Content-Type": "application/json",
                },
            )
            with urllib.request.urlopen(req, timeout=20) as resp:
                payload = json.loads(resp.read().decode("utf-8"))

            hits = payload.get("hits") or []
            if not hits:
                break
            for hit in hits:
                path = hit.get("path")
                if path:
                    counts[path] = int(hit.get("count") or 0)
                    exclude.append(path)
            pages += 1
            if not payload.get("more"):
                break
    except (urllib.error.URLError, urllib.error.HTTPError, ValueError, OSError, TimeoutError) as exc:
        print(f"  ! read counts unavailable ({type(exc).__name__}: {exc}) — rendering as unknown",
              file=sys.stderr)
        return {}

    return counts


def lookup_views(counts, url_path):
    """GoatCounter may record the path with or without a trailing slash."""
    if not counts:
        return None
    for candidate in (url_path, url_path.rstrip("/"), url_path.rstrip("/") + "/"):
        if candidate in counts:
            return counts[candidate]
    return None


# --------------------------------------------------------------------------
# html helpers
# --------------------------------------------------------------------------

def e(text):
    return html.escape(str(text), quote=True)


def page(cfg, *, title, body, nav_key="", description="", wide=False, canonical=""):
    css = THEME.read_text(encoding="utf-8")
    bp = cfg["base_path"]
    full_title = title if title == cfg["title"] else f"{title} · {cfg['title']}"

    tracker = ""
    if cfg.get("goatcounter_code"):
        tracker = (
            f'<script data-goatcounter="https://{e(cfg["goatcounter_code"])}.goatcounter.com/count"\n'
            f'        async src="//gc.zgo.at/count.js"></script>'
        )

    def nav_link(key, href, label):
        current = ' aria-current="page"' if key == nav_key else ""
        return f'<a href="{bp}{href}"{current}>{label}</a>'

    wrap = "wrap-wide" if wide else "wrap"
    year = dt.date.today().year

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(full_title)}</title>
<meta name="description" content="{e(description or cfg.get('tagline', ''))}">
{f'<link rel="canonical" href="{e(canonical)}">' if canonical else ''}
<link rel="alternate" type="application/rss+xml" title="{e(cfg['title'])}" href="{bp}/feed.xml">
<style>{css}</style>
</head>
<body>
<header class="site-head">
  <div class="{wrap} site-head-inner">
    <a class="brand" href="{bp}/">{e(cfg['title'])}</a>
    <nav class="nav">
      {nav_link('home', '/', 'Latest')}
      {nav_link('archive', '/archive/', 'Archive')}
      {nav_link('topics', '/topics/', 'Topics')}
      <a href="{bp}/feed.xml">RSS</a>
    </nav>
  </div>
</header>
<main class="{wrap}">
{body}
</main>
<footer class="{wrap} site-foot">
  <span>© {year} {e(cfg.get('author', ''))}</span>
  <span>Written daily by an automated agent. Sources are verified at publish time; mistakes are mine.</span>
</footer>
{tracker}
</body>
</html>
"""


def tag_links(cfg, topics):
    if not topics:
        return ""
    links = "".join(
        f'<a class="tag" href="{cfg["base_path"]}/topics/{slugify(t)}/">{e(t)}</a>'
        for t in topics
    )
    return f'<div class="tags">{links}</div>'


def fmt_date(date):
    return date.strftime("%-d %B %Y") if os.name != "nt" else date.strftime("%d %B %Y")


def fmt_date_short(date):
    """Compact form for dense archive rows: 26 Oct 2026."""
    return date.strftime("%-d %b %Y") if os.name != "nt" else date.strftime("%d %b %Y")


def fmt_views(count):
    if count is None:
        return '<span class="views" data-unknown="1" title="No read data yet">—</span>'
    label = "read" if count == 1 else "reads"
    return f'<span class="views">{count:,} {label}</span>'


def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


# --------------------------------------------------------------------------
# pages
# --------------------------------------------------------------------------

def render_index(cfg, posts, views):
    limit = int(cfg.get("posts_per_page_index", 10))
    items = []
    for post in posts[:limit]:
        count = lookup_views(views, post["url_path"])
        items.append(f"""<li>
  <h2><a href="{cfg['base_path']}{post['url_path']}">{e(post['title'])}</a></h2>
  <div class="meta">
    <time datetime="{post['date'].isoformat()}">{fmt_date(post['date'])}</time>
    <span class="dot">·</span>{fmt_views(count)}
  </div>
  {f'<p class="summary">{e(post["summary"])}</p>' if post["summary"] else ''}
  {tag_links(cfg, post['topics'])}
</li>""")

    body = f"""<p class="tagline">{e(cfg.get('tagline', ''))}</p>
<ul class="post-list">
{''.join(items) if items else '<li class="empty">No posts yet.</li>'}
</ul>
<p style="margin-top:32px"><a href="{cfg['base_path']}/archive/">See all {len(posts)} posts in the archive →</a></p>"""

    write(OUT_DIR / "index.html",
          page(cfg, title=cfg["title"], body=body, nav_key="home",
               canonical=f"{cfg['base_url']}/"))


def render_post(cfg, post, views):
    count = lookup_views(views, post["url_path"])
    body = f"""<article>
  <div class="article-head">
    <h1>{e(post['title'])}</h1>
    <div class="meta">
      <time datetime="{post['date'].isoformat()}">{fmt_date(post['date'])}</time>
      <span class="dot">·</span>{fmt_views(count)}
    </div>
    {tag_links(cfg, post['topics'])}
  </div>
  <div class="prose">
{post['html']}
  </div>
</article>
<p style="margin-top:40px"><a href="{cfg['base_path']}/archive/">← Archive</a></p>"""

    write(OUT_DIR / "posts" / post["slug"] / "index.html",
          page(cfg, title=post["title"], body=body, description=post["summary"],
               canonical=f"{cfg['base_url']}{post['url_path']}"))


def build_heatmap(posts, weeks=53):
    """GitHub-style grid of posting days for the last `weeks` weeks."""
    today = dt.date.today()
    per_day = {}
    for post in posts:
        per_day[post["date"]] = per_day.get(post["date"], 0) + 1

    # Grid runs Mon..Sun down each column; start on the Monday `weeks` back.
    end = today + dt.timedelta(days=(6 - today.weekday()))
    start = end - dt.timedelta(weeks=weeks) + dt.timedelta(days=1)

    cells = []
    day = start
    while day <= end:
        if day > today:
            cells.append('<div class="cell void"></div>')
        else:
            n = per_day.get(day, 0)
            level = "" if n == 0 else (" l1" if n == 1 else (" l2" if n == 2 else " l3"))
            label = "no post" if n == 0 else (f"{n} post" if n == 1 else f"{n} posts")
            cells.append(f'<div class="cell{level}" title="{day.isoformat()} — {label}"></div>')
        day += dt.timedelta(days=1)

    posted_days = sum(1 for d in per_day if start <= d <= today)
    span_days = (today - start).days + 1
    return f"""<section class="heat-card">
  <p class="heat-title">Posting history · {posted_days} of the last {span_days} days</p>
  <div class="heat">{''.join(cells)}</div>
  <div class="heat-legend">
    <span>none</span>
    <div class="cell"></div><div class="cell l1"></div><div class="cell l2"></div><div class="cell l3"></div>
    <span>more</span>
  </div>
</section>"""


def render_archive(cfg, posts, views):
    bp = cfg["base_path"]

    data = []
    for post in posts:
        count = lookup_views(views, post["url_path"])
        data.append({
            "title": post["title"],
            "url": bp + post["url_path"],
            "date": post["date"].isoformat(),
            "dateLabel": fmt_date_short(post["date"]),
            "month": post["date"].strftime("%B %Y"),
            "topics": post["topics"],
            "topicSlugs": [slugify(t) for t in post["topics"]],
            "views": count,
            "summary": post["summary"],
        })

    all_topics = sorted({t for p in posts for t in p["topics"]}, key=str.lower)
    chips = "".join(
        f'<button class="chip" type="button" aria-pressed="false" data-topic="{slugify(t)}">{e(t)}</button>'
        for t in all_topics
    )

    # Server-rendered default view (date descending, grouped by month) so the
    # page is complete without JavaScript. JS re-renders on interaction.
    static_rows, current_month = [], None
    for item in data:
        if item["month"] != current_month:
            current_month = item["month"]
            static_rows.append(f'<h2 class="month-head">{e(current_month)}</h2>')
        tags = "".join(
            f'<a class="tag" href="{bp}/topics/{s}/">{e(t)}</a>'
            for t, s in zip(item["topics"], item["topicSlugs"])
        )
        static_rows.append(f"""<div class="row">
  <div class="d">{e(item['dateLabel'])}</div>
  <div class="t"><a href="{e(item['url'])}">{e(item['title'])}</a>
    {f'<div class="tags">{tags}</div>' if tags else ''}</div>
  <div class="v">{fmt_views(item['views'])}</div>
</div>""")

    has_views = any(item["views"] is not None for item in data)
    views_note = "" if has_views else (
        '<p class="page-sub">Read counts appear here once GoatCounter is connected '
        'and has collected traffic.</p>'
    )

    script = """
<script>
(function () {
  var data = JSON.parse(document.getElementById("post-data").textContent);
  var list = document.getElementById("rows");
  var sortSel = document.getElementById("sort");
  var search = document.getElementById("q");
  var chips = Array.prototype.slice.call(document.querySelectorAll(".chip"));
  var active = new Set();

  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  function viewsHtml(v) {
    if (v === null || v === undefined) {
      return '<span class="views" data-unknown="1" title="No read data yet">\\u2014</span>';
    }
    return '<span class="views">' + v.toLocaleString() + (v === 1 ? " read" : " reads") + "</span>";
  }

  function render() {
    var q = search.value.trim().toLowerCase();
    var rows = data.filter(function (p) {
      if (active.size) {
        var hit = p.topicSlugs.some(function (s) { return active.has(s); });
        if (!hit) return false;
      }
      if (q) {
        var hay = (p.title + " " + p.summary + " " + p.topics.join(" ")).toLowerCase();
        if (hay.indexOf(q) === -1) return false;
      }
      return true;
    });

    var sort = sortSel.value;
    rows.sort(function (a, b) {
      if (sort === "oldest") return a.date.localeCompare(b.date);
      if (sort === "views") return (b.views || 0) - (a.views || 0) || b.date.localeCompare(a.date);
      if (sort === "title") return a.title.localeCompare(b.title);
      return b.date.localeCompare(a.date);
    });

    if (!rows.length) {
      list.innerHTML = '<p class="empty">Nothing matches that filter.</p>';
      return;
    }

    var html = "";
    var month = null;
    var grouped = sort === "newest" || sort === "oldest";
    rows.forEach(function (p) {
      if (grouped && p.month !== month) {
        month = p.month;
        html += '<h2 class="month-head">' + esc(month) + "</h2>";
      }
      var tags = p.topics.map(function (t, i) {
        return '<a class="tag" href="' + TOPIC_BASE + p.topicSlugs[i] + '/">' + esc(t) + "</a>";
      }).join("");
      html += '<div class="row"><div class="d">' + esc(p.dateLabel) + "</div>" +
        '<div class="t"><a href="' + esc(p.url) + '">' + esc(p.title) + "</a>" +
        (tags ? '<div class="tags">' + tags + "</div>" : "") + "</div>" +
        '<div class="v">' + viewsHtml(p.views) + "</div></div>";
    });
    list.innerHTML = html;
  }

  chips.forEach(function (chip) {
    chip.addEventListener("click", function () {
      var slug = chip.dataset.topic;
      if (active.has(slug)) { active.delete(slug); chip.setAttribute("aria-pressed", "false"); }
      else { active.add(slug); chip.setAttribute("aria-pressed", "true"); }
      render();
    });
  });
  sortSel.addEventListener("change", render);
  search.addEventListener("input", render);
  render();
})();
</script>"""
    script = script.replace("TOPIC_BASE", json.dumps(bp + "/topics/"))

    body = f"""<h1 class="page-title">Archive</h1>
<p class="page-sub">{len(posts)} post{'' if len(posts) == 1 else 's'}, every one dated and tagged.</p>
{build_heatmap(posts)}
{views_note}
<div class="controls">
  <label for="sort">Sort</label>
  <select id="sort">
    <option value="newest">Newest first</option>
    <option value="oldest">Oldest first</option>
    <option value="views">Most read</option>
    <option value="title">Title A–Z</option>
  </select>
  <input id="q" type="search" placeholder="Search titles and topics" aria-label="Search posts">
</div>
<div class="chip-row">{chips}</div>
<div id="rows">
{''.join(static_rows) if static_rows else '<p class="empty">No posts yet.</p>'}
</div>
<script type="application/json" id="post-data">{json.dumps(data)}</script>
{script}"""

    write(OUT_DIR / "archive" / "index.html",
          page(cfg, title="Archive", body=body, nav_key="archive", wide=True,
               canonical=f"{cfg['base_url']}/archive/"))


def render_topics(cfg, posts, views):
    bp = cfg["base_path"]
    by_topic = {}
    for post in posts:
        for topic in post["topics"]:
            by_topic.setdefault(topic, []).append(post)

    ordered = sorted(by_topic.items(), key=lambda kv: (-len(kv[1]), kv[0].lower()))
    cards = "".join(
        f'<li><a class="topic-card" href="{bp}/topics/{slugify(t)}/">'
        f'<span>{e(t)}</span><span class="n">{len(ps)}</span></a></li>'
        for t, ps in ordered
    )
    body = f"""<h1 class="page-title">Topics</h1>
<p class="page-sub">{len(ordered)} topic{'' if len(ordered) == 1 else 's'} across {len(posts)} post{'' if len(posts) == 1 else 's'}.</p>
<ul class="topic-grid">{cards or '<li class="empty">No topics yet.</li>'}</ul>"""

    write(OUT_DIR / "topics" / "index.html",
          page(cfg, title="Topics", body=body, nav_key="topics", wide=True,
               canonical=f"{cfg['base_url']}/topics/"))

    for topic, topic_posts in ordered:
        items = []
        for post in topic_posts:
            count = lookup_views(views, post["url_path"])
            items.append(f"""<li>
  <h2><a href="{bp}{post['url_path']}">{e(post['title'])}</a></h2>
  <div class="meta">
    <time datetime="{post['date'].isoformat()}">{fmt_date(post['date'])}</time>
    <span class="dot">·</span>{fmt_views(count)}
  </div>
  {f'<p class="summary">{e(post["summary"])}</p>' if post["summary"] else ''}
  {tag_links(cfg, [t for t in post['topics'] if t != topic])}
</li>""")
        tbody = f"""<h1 class="page-title">{e(topic)}</h1>
<p class="page-sub">{len(topic_posts)} post{'' if len(topic_posts) == 1 else 's'} · <a href="{bp}/topics/">all topics</a></p>
<ul class="post-list">{''.join(items)}</ul>"""
        write(OUT_DIR / "topics" / slugify(topic) / "index.html",
              page(cfg, title=topic, body=tbody, nav_key="topics",
                   canonical=f"{cfg['base_url']}/topics/{slugify(topic)}/"))


def render_feed(cfg, posts):
    base = cfg["base_url"]
    items = []
    for post in posts[:30]:
        stamp = dt.datetime.combine(post["date"], dt.time(12, 0), dt.timezone.utc)
        items.append(f"""  <item>
    <title>{e(post['title'])}</title>
    <link>{e(base + post['url_path'])}</link>
    <guid isPermaLink="true">{e(base + post['url_path'])}</guid>
    <pubDate>{stamp.strftime('%a, %d %b %Y %H:%M:%S +0000')}</pubDate>
    <description>{e(post['summary'] or post['title'])}</description>
{''.join(f'    <category>{e(t)}</category>{chr(10)}' for t in post['topics'])}  </item>""")

    now = dt.datetime.now(dt.timezone.utc).strftime("%a, %d %b %Y %H:%M:%S +0000")
    feed = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
  <title>{e(cfg['title'])}</title>
  <link>{e(base)}/</link>
  <description>{e(cfg.get('tagline', ''))}</description>
  <language>en</language>
  <lastBuildDate>{now}</lastBuildDate>
  <atom:link href="{e(base)}/feed.xml" rel="self" type="application/rss+xml"/>
{chr(10).join(items)}
</channel>
</rss>
"""
    write(OUT_DIR / "feed.xml", feed)


def render_data(cfg, posts, views):
    """Machine-readable index — useful for the daily agent's topic rotation."""
    payload = {
        "generated": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "count": len(posts),
        "posts": [
            {
                "title": p["title"],
                "slug": p["slug"],
                "date": p["date"].isoformat(),
                "topics": p["topics"],
                "summary": p["summary"],
                "url": cfg["base_url"] + p["url_path"],
                "views": lookup_views(views, p["url_path"]),
            }
            for p in posts
        ],
    }
    write(OUT_DIR / "data" / "posts.json", json.dumps(payload, indent=2))


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------

def main():
    cfg = load_config()
    posts, problems = load_posts()

    for problem in problems:
        print(f"  ! skipped — {problem}", file=sys.stderr)

    since = min((p["date"] for p in posts), default=dt.date.today()) - dt.timedelta(days=1)
    views = fetch_views(cfg, since)

    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
    OUT_DIR.mkdir(parents=True)

    render_index(cfg, posts, views)
    for post in posts:
        render_post(cfg, post, views)
    render_archive(cfg, posts, views)
    render_topics(cfg, posts, views)
    render_feed(cfg, posts)
    render_data(cfg, posts, views)
    (OUT_DIR / ".nojekyll").write_text("", encoding="utf-8")

    topics = {t for p in posts for t in p["topics"]}
    counted = sum(1 for p in posts if lookup_views(views, p["url_path"]) is not None)
    print(f"Built {len(posts)} post(s), {len(topics)} topic(s) into {OUT_DIR}")
    print(f"Read counts: {counted}/{len(posts)} posts have data"
          if views else "Read counts: not configured")

    if problems:
        print(f"\n{len(problems)} file(s) were skipped — see warnings above.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
