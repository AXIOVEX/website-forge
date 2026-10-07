# Validation — a cold run of this package, end to end

**Date:** 2026-10-07
**Method:** A fresh operator (an AI agent) built a website for a fictional
business using **only this package's own instructions** — the README
quickstart, `docs/AGENT-INSTRUCTIONS.md` as `AGENTS.md`/`CLAUDE.md`, a spec
modeled on `examples/spec-add-blog-article/`, and the `templates/` starters.
No internal knowledge, no outside templates. The run was local (a plain
static file server stands in for Cloudflare Pages), so hosting/account
steps are marked "not testable locally" rather than passed on faith.

**The example:** Harbor & Pine Bakery (fictional, `harborandpine.example`) —
home, about, contact, a journal index stub, and a privacy page, built from
`templates/head-snippet.html`, `templates/jsonld/homepage.jsonld.html`,
`templates/robots.txt`, the sitemap/llms starters, and (after fix F4 below)
the new `templates/privacy-page.md`. Zero `REPLACE_` tokens shipped.

## Tool outputs (the package's own MCP server)

| Run | URL | AEO estimate* | Gaps |
|---|---|---|---|
| Naive baseline page (title + two paragraphs) | local | **8** / 90 | robots, sitemap, llms, description, canonical, OG, JSON-LD, `<time>` |
| Template-built site, first self-test | local | **82** / 90 | "JSON-LD partial (-8)" — see F1 |
| Template-built site, after fix F1 | local | **90** / 90 | none |

\* MCP `estimate_score` output, labeled an estimate per the standing orders;
the estimator caps at 90 because the last ~10 points are official-scanner
citability. `check_page` reported `healthy: true` for all four content
pages; discovery files (robots, sitemap, llms, llms-full, favicon) all 200.

## Launch checklist results (`docs/CHECKLISTS.md`)

- ✅ robots.txt, sitemap.xml, llms.txt, llms-full.txt all 200
- ✅ Every page: unique title, meta description, canonical, OG/Twitter with
  a real 1200×630 image, favicon set
- ✅ JSON-LD validates (parser-verified on every page; homepage `@graph`
  carries Organization + WebSite + WebPage = 3 entities)
- ✅ Screenshots filed for every page type, desktop (1440px) + mobile (390px)
- ⚠️ SCORES.md opened with the MCP estimate (labeled) — the official AEO/SEO
  scanners need a public URL, so they are **partial** by construction here
- ⚠️ Privacy page: **failed on the first pass** (checklist requires one; the
  package shipped no template — F4), passed on re-run using the new starter.
  Contact route is email-only (mailto); an inbox delivery test is not
  possible against a fictional domain
- ⏸️ Not testable locally (hosting/account items, neither passed nor
  failed): domain/DNS/HTTPS + www redirect, email-record separation,
  Pages production/staging projects, staging guards live, Search Console
  + Bing submission

## Friction log — every rough edge found, and the fix made

- **F1 — the estimator docked sites built with the package's own JSON-LD
  template.** The homepage template ships Organization+WebSite+WebPage as
  one `@graph` in a single `<script>` block; `estimate_score` counted
  *blocks*, so a by-the-book site scored 82 with a "JSON-LD partial" gap.
  **Fix:** `mcp-server/server.py` now counts JSON-LD *entities*
  (`jsonld_entities`, expanding `@graph` and arrays) and the estimator
  scores on entities. By-the-book site: 82 → 90; the naive baseline is
  unchanged at 8, so the fix discriminates rather than inflates.
- **F2 — `generate_sitemap` defaulted a missing `lastmod` to a hardcoded
  date** (`2026-10-07`), which would silently go stale and teach exactly
  the dishonest-lastmod habit the sitemap template warns against.
  **Fix:** the default is now today's date.
- **F3 — `templates/robots.txt` carried two overlapping header comment
  lines** saying the same thing two different ways. **Fix:** one clear
  instruction line.
- **F4 — the launch checklist requires a privacy page, but the package
  shipped no privacy template or guidance** — a first-time user hits a
  checklist item with nothing to start from. **Fix:** added
  `templates/privacy-page.md` (a state-only-what's-true starter) and a
  pointer in `docs/GETTING-STARTED.md` §6; the cold run then built the
  example's privacy page from it.
- **F5 — `templates/head-snippet.html` is homepage-shaped** (canonical and
  `og:url` point at the site root) and nothing said how to adapt it for
  other pages; a literal copy would give every page the homepage's
  canonical. **Fix:** the template's header comment now instructs per-page
  title/description/canonical/`og:url`.
- **F6 (observation, no fix) — the package ships no visual design system.**
  Templates cover head structure, discovery files, and schema, not CSS or
  layout; a template-built site renders unstyled until the owner adds a
  design (by wireframe, per the method). That is consistent with what the
  README promises, so it is recorded as a scope boundary, not a defect.
- **F7 (observation, no fix) — `check_headers` against a plain local
  server reports every security header missing**, because a local file
  server does not process `_headers` (a host-platform file). The tool
  faithfully reports what the server sends; on Cloudflare Pages/Netlify
  the same file takes effect. Local validation of headers is therefore
  limited to reviewing the `_headers` file itself.

## Verdict

The package works cold. Following only its own instructions produced a
site that passes every locally testable launch-checklist item and reaches
the MCP estimator's maximum (90) with zero gaps — and the one real defect
the run exposed (F1) was in the package's measuring tool, not in what a
user builds. Remaining limitations are environmental, stated above:
hosting/account steps, official scanner scores, and contact-delivery can
only be verified on a real deployment, and visual design is the owner's
to add.
