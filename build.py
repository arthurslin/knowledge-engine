#!/usr/bin/env python3
"""
Static site generator for Knowledge Engine.

Reads Markdown posts with YAML frontmatter from posts/ and writes a complete
static site to site/. No framework, no npm, just `markdown` and `PyYAML`.

Usage:
    python3 build.py                 # build with config.json
    BASE_PATH= python3 build.py      # build for local preview (no path prefix)

Read counts come from the GoatCounter API when both env vars are set:
    GOATCOUNTER_CODE        your site code, e.g. "knowledge-engine"
    GOATCOUNTER_API_TOKEN   an API token with "read statistics" permission
Without them the build still succeeds; counts render as "no read data".
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
# Smart quotes yes, smart dashes no: house style forbids em dashes, and smarty
# would silently turn "---" in a body into one.
MD_EXTENSION_CONFIGS = {"smarty": {"smart_dashes": False}}
FILENAME_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-(.+)\.md$")
EM_DASH = "\u2014"


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
        raise ValueError(f"{path.name}: frontmatter is not valid YAML, {exc}")
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

    quiz = parse_quiz(path.name, front.get("quiz") or [])
    reflect = [str(r).strip() for r in (front.get("reflect") or []) if str(r).strip()]

    md = markdown.Markdown(extensions=MD_EXTENSIONS,
                           extension_configs=MD_EXTENSION_CONFIGS)
    return {
        "title": str(title),
        "date": date,
        "slug": front.get("slug") or file_slug,
        "topics": topics,
        "summary": str(front.get("summary", "")).strip(),
        "status": str(front.get("status", "published")).strip().lower(),
        "quiz": quiz,
        "reflect": reflect,
        "html": md.convert(body),
        "source_file": path.name,
        "raw": raw,
    }


def parse_quiz(filename, raw_quiz):
    """Validate the frontmatter quiz block. Raises ValueError on a bad one."""
    if not isinstance(raw_quiz, list):
        raise ValueError(f"{filename}: quiz must be a list of questions")

    questions = []
    for i, item in enumerate(raw_quiz, start=1):
        if not isinstance(item, dict):
            raise ValueError(f"{filename}: quiz question {i} must be a mapping")
        prompt = str(item.get("q", "")).strip()
        options = item.get("options") or []
        if not prompt:
            raise ValueError(f"{filename}: quiz question {i} has no 'q'")
        if not isinstance(options, list) or len(options) < 2:
            raise ValueError(f"{filename}: quiz question {i} needs at least 2 options")
        try:
            answer = int(item.get("answer"))
        except (TypeError, ValueError):
            raise ValueError(f"{filename}: quiz question {i} needs an integer 'answer'")
        if not 0 <= answer < len(options):
            raise ValueError(
                f"{filename}: quiz question {i} 'answer' is {answer}, "
                f"but there are {len(options)} options (indexes are 0-based)"
            )
        questions.append({
            "q": prompt,
            "options": [str(o) for o in options],
            "answer": answer,
            "explain": str(item.get("explain", "")).strip(),
        })
    return questions


def find_em_dashes(post):
    """House style bans em dashes. Returns a list of 'file:line  context' hits."""
    hits = []
    for lineno, line in enumerate(post["raw"].splitlines(), start=1):
        if EM_DASH in line:
            snippet = line.strip()
            if len(snippet) > 90:
                col = snippet.index(EM_DASH)
                snippet = "..." + snippet[max(0, col - 40):col + 45] + "..."
            hits.append(f"{post['source_file']}:{lineno}  {snippet}")
    return hits


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
    failure, analytics must never break a build.
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
        print(f"  ! read counts unavailable ({type(exc).__name__}: {exc}), rendering as unknown",
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

THEME_SCRIPT = """<script>
(function () {
  var btn = document.getElementById("theme-toggle");
  if (!btn) return;
  var ICONS = {
    auto: '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M12 3a9 9 0 0 1 0 18z" fill="currentColor" stroke="none"/></svg>',
    light: '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>',
    dark: '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>'
  };
  var LABELS = { auto: "Theme: follow system", light: "Theme: light", dark: "Theme: dark" };
  var ORDER = ["auto", "light", "dark"];

  function current() {
    try {
      var t = localStorage.getItem("ke-theme");
      return (t === "light" || t === "dark") ? t : "auto";
    } catch (e) { return "auto"; }
  }
  function apply(mode) {
    if (mode === "auto") document.documentElement.removeAttribute("data-theme");
    else document.documentElement.setAttribute("data-theme", mode);
    btn.innerHTML = ICONS[mode];
    btn.title = LABELS[mode];
    btn.setAttribute("aria-label", LABELS[mode] + ". Click to change.");
  }
  function store(mode) {
    try {
      if (mode === "auto") localStorage.removeItem("ke-theme");
      else localStorage.setItem("ke-theme", mode);
    } catch (e) { /* private mode: the choice just won't persist */ }
    apply(mode);
  }
  apply(current());
  btn.addEventListener("click", function () {
    store(ORDER[(ORDER.indexOf(current()) + 1) % ORDER.length]);
  });
})();
</script>"""


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

    # Applied before first paint so a remembered theme never flashes.
    theme_boot = (
        '<script>(function(){try{var t=localStorage.getItem("ke-theme");'
        'if(t==="light"||t==="dark")document.documentElement.setAttribute("data-theme",t);}'
        'catch(e){}})();</script>'
    )

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
{theme_boot}
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
      <button id="theme-toggle" class="theme-toggle" type="button"
              aria-label="Switch colour theme" title="Switch colour theme"></button>
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
{THEME_SCRIPT}
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
        return '<span class="views" data-unknown="1">no read data</span>'
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


QUIZ_SCRIPT = """<script>
(function () {
  var root = document.getElementById("quiz");
  if (!root) return;
  var questions = Array.prototype.slice.call(root.querySelectorAll(".q"));
  var scoreBox = root.querySelector(".quiz-score");
  var resetBtn = root.querySelector(".quiz-reset");
  var answered = 0, correct = 0;

  function finish() {
    scoreBox.textContent = correct + " of " + questions.length + " correct.";
    scoreBox.hidden = false;
    resetBtn.hidden = false;
  }

  function reset() {
    answered = 0; correct = 0;
    scoreBox.hidden = true; resetBtn.hidden = true;
    questions.forEach(function (q) {
      q.classList.remove("done");
      q.querySelector(".explain").hidden = true;
      Array.prototype.forEach.call(q.querySelectorAll(".opt"), function (b) {
        b.classList.remove("chosen", "correct", "wrong");
        b.disabled = false;
        b.removeAttribute("aria-describedby");
      });
    });
    questions[0].scrollIntoView({ behavior: "smooth", block: "center" });
  }

  questions.forEach(function (q) {
    var right = parseInt(q.dataset.answer, 10);
    var opts = Array.prototype.slice.call(q.querySelectorAll(".opt"));
    var explain = q.querySelector(".explain");
    var verdict = q.querySelector(".verdict");

    opts.forEach(function (btn, i) {
      btn.addEventListener("click", function () {
        if (q.classList.contains("done")) return;
        q.classList.add("done");
        var hit = i === right;
        if (hit) correct++;
        answered++;

        btn.classList.add("chosen", hit ? "correct" : "wrong");
        if (!hit) opts[right].classList.add("correct");
        opts.forEach(function (b) { b.disabled = true; });

        verdict.textContent = hit ? "Correct." : "Not that one.";
        verdict.className = "verdict " + (hit ? "ok" : "no");
        explain.hidden = false;

        if (answered === questions.length) finish();
      });
    });
  });

  resetBtn.addEventListener("click", reset);
})();
</script>"""


def render_quiz(post):
    """Interactive self-test rendered from the post's frontmatter."""
    if not post["quiz"] and not post["reflect"]:
        return ""

    items = []
    for question in post["quiz"]:
        opts = "".join(
            f'<button class="opt" type="button">{e(option)}</button>'
            for option in question["options"]
        )
        explain = e(question["explain"]) if question["explain"] else ""
        items.append(f"""<li class="q" data-answer="{question['answer']}">
  <p class="q-text">{e(question['q'])}</p>
  <div class="opts">{opts}</div>
  <p class="explain" hidden><strong class="verdict"></strong> {explain}</p>
</li>""")

    quiz_block = ""
    if items:
        quiz_block = f"""<ol class="quiz-list">{''.join(items)}</ol>
<p class="quiz-score" hidden></p>
<button class="quiz-reset" type="button" hidden>Start over</button>"""

    reflect_block = ""
    if post["reflect"]:
        lis = "".join(f"<li>{e(r)}</li>" for r in post["reflect"])
        reflect_block = f"""<h3 class="quiz-subhead">Questions without answers</h3>
<ol class="reflect">{lis}</ol>"""

    note = "Answers are checked in your browser. Nothing is recorded or sent anywhere."
    return f"""<section class="quiz" id="quiz">
  <h2 class="quiz-head">Check yourself</h2>
  <p class="quiz-note">{note}</p>
  {quiz_block}
  {reflect_block}
</section>
{QUIZ_SCRIPT if items else ''}"""


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
{render_quiz(post)}
<p style="margin-top:40px"><a href="{cfg['base_path']}/archive/">Back to the archive</a></p>"""

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
            cells.append(f'<div class="cell{level}" title="{day.isoformat()}, {label}"></div>')
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
      return '<span class="views" data-unknown="1">no read data</span>';
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
    """Machine-readable index, useful for the daily agent's topic rotation."""
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

def run_checks(posts, problems):
    """
    Validate posts without building. Used by the daily agent before it commits:
        python3 build.py --check
    Returns a process exit code.
    """
    style = []
    for post in posts:
        style.extend(find_em_dashes(post))

    for problem in problems:
        print(f"ERROR  {problem}", file=sys.stderr)
    for hit in style:
        print(f"ERROR  em dash (house style forbids it) {hit}", file=sys.stderr)

    if problems or style:
        print(f"\n{len(problems)} parse error(s), {len(style)} em dash(es). "
              f"Fix these before committing.", file=sys.stderr)
        return 1

    print(f"OK  {len(posts)} post(s) parse cleanly, no em dashes, "
          f"{sum(len(p['quiz']) for p in posts)} quiz question(s) valid")
    return 0


def main():
    cfg = load_config()
    posts, problems = load_posts()

    if "--check" in sys.argv:
        return run_checks(posts, problems)

    for problem in problems:
        print(f"  ! skipped: {problem}", file=sys.stderr)

    # Style issues warn but never block a deploy: one stray dash should not
    # take the whole site offline. --check is where they are fatal.
    style = [hit for post in posts for hit in find_em_dashes(post)]
    for hit in style:
        print(f"  ! em dash in {hit}", file=sys.stderr)

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
    if style:
        print(f"Style: {len(style)} em dash(es) found, see warnings above")

    if problems:
        print(f"\n{len(problems)} file(s) were skipped, see warnings above.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
