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

## Writing a post by hand

Create `posts/YYYY-MM-DD-slug.md`:

```markdown
---
title: "The third kind of good life"
date: 2026-10-26
topics: [psychology, well-being]
summary: "One or two sentences for the index page and the RSS feed."
status: published
---

Body in Markdown.
```

`status: draft` keeps a file out of the build. The slug comes from the
filename unless you override it with a `slug:` field.

## Building locally

```bash
pip install -r requirements.txt
BASE_PATH= python3 build.py        # empty BASE_PATH for local file:// preview
open site/index.html
```

Leave `BASE_PATH` unset in CI — it comes from `config.json`, where it is
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
| `/posts/<slug>/` | A single post |
| `/feed.xml` | RSS, 30 most recent |
| `/data/posts.json` | Machine-readable index — the daily agent reads this to avoid repeating topics |

The archive renders fully without JavaScript; filtering and sorting are
progressive enhancement on top of the server-rendered list.

## Read counts

Counts come from [GoatCounter](https://www.goatcounter.com), fetched at build
time from `/api/v0/stats/hits` and baked into the pages.

**Setup:**

1. Create a site at goatcounter.com and note your code (the `MYCODE` in
   `MYCODE.goatcounter.com`).
2. Set `goatcounter_code` in `config.json` — this adds the tracking script to
   every page.
3. Create an API token under *Username → API* with permission to read
   statistics.
4. In the repo: **Settings → Secrets and variables → Actions**
   - Secret `GOATCOUNTER_API_TOKEN` — the token
   - Variable `GOATCOUNTER_CODE` — your site code

Until that's done, counts render as `—` and the build still succeeds. Analytics
failures never fail a build; the error goes to stderr and the site deploys
without counts.

**What the numbers do and don't mean.** GoatCounter reports visitors per path.
That is not readers. Ad blockers and privacy modes drop an unknown share of
hits, usually estimated in the tens of percent, and the direction of that bias
is not random — a technical audience undercounts harder. Treat the figures as a
floor and a relative signal between posts, not a headcount.

## Deployment

`.github/workflows/deploy.yml` builds on every push to `main`, on a daily cron
at 06:17 UTC (so counts refresh even with no new post), and on manual dispatch.

GitHub Pages needs to be set to deploy from GitHub Actions:
**Settings → Pages → Source → GitHub Actions**.
