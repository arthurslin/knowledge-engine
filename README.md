# Knowledge Engine

A daily newsletter: one unfamiliar idea, with the evidence behind it stated
honestly. Posts are written by a scheduled agent and published automatically.

Live at **https://arthurslin.github.io/knowledge-engine**

## How it works

```
posts/*.md  ──►  build.py  ──►  site/  ──►  GitHub Pages
                     ▲
                     └── read counts from the GoatCounter API
```

A scheduled agent writes a Markdown file into `posts/` and pushes to `main`.
GitHub Actions rebuilds and deploys. The prompt it runs is in
[AUTOMATION.md](AUTOMATION.md).

## Writing a post

Create `posts/YYYY-MM-DD-slug.md`:

```markdown
---
title: "The third kind of good life"
date: 2026-10-26
topics: [psychology, well-being]
summary: "One or two sentences for the index page and the RSS feed."
status: published
quiz:
  - q: "What distinguishes psychological richness from happiness?"
    options:
      - "First option"
      - "Second option"
      - "Third option"
    answer: 1          # zero-based index into options
    explain: "Why that answer is right. Shown after the reader picks."
reflect:
  - "An open question with no scored answer."
---

Body in Markdown.
```

`status: draft` keeps a file out of the build. The slug comes from the filename
unless you override it with a `slug:` field. `quiz` and `reflect` are both
optional; a post with neither simply has no self-test at the bottom.

### House style

**No em dashes.** `build.py --check` fails on them. Smart dashes are disabled in
the Markdown renderer, so writing `---` in a body will not silently produce one
either. En dashes in number ranges and compound names (`800–804`,
`hippocampal–striatal`) are fine and are not flagged.

## Building and checking locally

```bash
pip install -r requirements.txt

python3 build.py --check           # validate posts: frontmatter, quiz, style
BASE_PATH= python3 build.py        # empty BASE_PATH for local file:// preview
open site/index.html
```

`--check` validates without building and is what the daily agent runs before it
commits. It fails on unparseable frontmatter, a quiz `answer` that is out of
range, and em dashes.

A normal build treats style problems as warnings rather than errors. One stray
dash should not take the site offline; the strict gate lives in `--check`,
before anything is committed.

Leave `BASE_PATH` unset in CI. It comes from `config.json`, where it is
`/knowledge-engine` because this is a GitHub project page rather than a user
page. If you later move to a custom domain, set `base_path` to `""` and
`base_url` to the new origin.

## What gets generated

| Path | What it is |
| --- | --- |
| `/` | The ten most recent posts |
| `/archive/` | Every post, grouped by month, with a posting heatmap, topic filter, search, and sort by date / reads / title |
| `/topics/` | All topics with post counts |
| `/topics/<topic>/` | Posts in one topic |
| `/posts/<slug>/` | A single post, with glossary tooltips and its interactive quiz |
| `/glossary/` | Every defined term and which posts use it |
| `/feed.xml` | RSS, 30 most recent |
| `/data/posts.json` | Machine-readable index. The daily agent reads this to avoid repeating topics |

The archive renders fully without JavaScript; filtering and sorting are
progressive enhancement on top of the server-rendered list. The quiz does need
JavaScript, since grading happens in the browser.

## Glossary tooltips

`glossary.yml` maps jargon to one-sentence definitions. The build wraps the
**first** occurrence of each term in each post, so a reader gets the definition
once rather than a page speckled with dotted underlines. Hover, tap, or focus
the word with a keyboard to see it; Escape closes it. Every term also gets a
row on `/glossary/` showing which posts use it.

```yaml
hedonic:
  definition: "Concerned with pleasure and feeling good, as opposed to purpose."
  aliases: [hedonia, hedonic well-being]
  source: https://example.com/optional-link
```

A bare `term: "definition"` works too. Matching is case-insensitive and
respects word boundaries, and terms are tried longest-first so "openness to
experience" wins over "openness". Headings, links, and code are skipped: a
tooltip nested inside a link would break the link, and one inside a heading
looks broken.

Definitions are shared across posts deliberately. A term defined once stays
defined the same way, instead of each post inventing its own wording.

## Themes

Every page has a theme button in the header that cycles **follow system →
light → dark**. The choice is stored in `localStorage` and applied by a tiny
inline script in `<head>`, before first paint, so a remembered theme never
flashes the wrong colours. With JavaScript off or storage blocked, pages
follow the operating system setting.

## Read counts

Counts come from [GoatCounter](https://www.goatcounter.com), fetched at build
time from `/api/v0/stats/hits` and baked into the pages.

**Setup:**

1. Create a site at goatcounter.com and note your code (the `MYCODE` in
   `MYCODE.goatcounter.com`).
2. Set `goatcounter_code` in `config.json`. This adds the tracking script to
   every page.
3. Create an API token under *Username → API* with permission to read
   statistics.
4. In the repo: **Settings → Secrets and variables → Actions**
   - Secret `GOATCOUNTER_API_TOKEN`
   - Variable `GOATCOUNTER_CODE`

Until that is done, counts render as "no read data" and the build still
succeeds. Analytics failures never fail a build; the error goes to stderr and
the site deploys without counts.

**What the numbers do and do not mean.** GoatCounter reports visitors per path.
That is not readers. Ad blockers and privacy modes drop an unknown share of
hits, usually estimated in the tens of percent, and the direction of that bias
is not random: a technical audience undercounts harder. Treat the figures as a
floor and a relative signal between posts, not a headcount.

## Deployment

`.github/workflows/deploy.yml` builds on every push to `main`, on a daily cron
at 06:17 UTC (so counts refresh even with no new post), and on manual dispatch.

GitHub Pages must be set to deploy from GitHub Actions:
**Settings → Pages → Source → GitHub Actions**.
