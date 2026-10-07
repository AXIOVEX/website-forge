# SEO / AEO — getting to (and holding) near 100

AEO = Answer Engine Optimization: being findable, understandable, and
**citable** by AI answer engines (ChatGPT, Claude, Perplexity, Google AI
Overviews), not just ranked by classic search. The same work serves both.

## The layers, in payoff order
1. **Discoverability files** (all must return HTTP 200 with correct content):
   `robots.txt` allowing search *and* AI crawlers explicitly (GPTBot,
   ChatGPT-User, OAI-SearchBot, ClaudeBot/-User/-SearchBot, PerplexityBot/
   -User, Google-Extended, Applebot/-Extended, CCBot, and peers) + a Sitemap
   line; `sitemap.xml` with one entry per real page and honest `<lastmod>`;
   `llms.txt` + `llms-full.txt` — the Markdown brief an AI reads first
   (what this is, how to cite it, links to every key page with one-line
   summaries; full text in the `-full` file).
2. **Head completeness, per page:** unique keyword title (~50–60 chars), meta
   description 150–160 chars, self-referencing canonical, full Open Graph +
   Twitter Card with a real 1200×630 image, a real favicon set (never an
   empty `data:,` href), author/robots/theme-color where they apply.
3. **Structured data (JSON-LD), validated:** Organization (with logo) +
   WebSite + WebPage on the home page; an Article/NewsArticle per article
   (headline/date/author must match the visible page); FAQPage only where
   the identical Q&A is visible on the page; BreadcrumbList on sub-pages.
   Zero validation errors (schema.org validator + Rich Results Test).
4. **Architecture:** real URLs per piece of content (`/blog/<slug>/`,
   one URL per report/edition). Downloads and media are real files
   (`/files/*.pdf`, `/audio/*.mp3`) — a base64 blob in a page is invisible
   to crawlers and murders page weight. Homepage target < 250 KB.
5. **Citability:** each article opens with a 40–60 word self-contained
   summary an AI can quote whole; statistics live in body text, not only in
   charts; lists and tables are real `<ul>/<ol>/<table>`; every date uses
   `<time datetime>`; byline + published/modified dates are visible and in
   schema; one idea per paragraph.
6. **Performance & headers:** versioned, minified CSS/JS, deferred
   non-critical scripts, long cache lifetimes for versioned assets and
   revalidation for HTML, and a real security-header set (HSTS, CSP tested
   on staging first, X-Content-Type-Options, Referrer-Policy,
   Permissions-Policy, frame protection).

## The audit loop
Baseline with the MCP tools (`audit_site`, `check_discovery`,
`check_headers`, `check_page`) or the manual checklist in docs/CHECKLISTS.md,
then run the official scanners in a real browser (they are JavaScript apps;
a text fetch doesn't run them): an AEO scanner (e.g. check.aeojs.org) and an
SEO checker (e.g. Seobility). Record every run — scanner, URL, date, score —
in a `SCORES.md`. Disposition every finding as **safe fix** (technical:
meta, headings, alt, schema, robots, sitemap, llms, canonical, internal
links), **by design** (with the reason written down), or **owner decision**
(anything touching claims or branding). Apply safe fixes, deploy, re-scan.

## Known ceilings (state them, don't chase them)
- SEO "external factors" ≈ backlinks. A new site scores near zero there no
  matter how perfect the site is; it accrues with real links over months.
- A perfect AEO score is attainable and holdable; a composite SEO 100
  generally is not, on any honest site. Report sub-scores, not just totals.

---

*Copyright (c) 2026 Axiovex Systems, LLC — MIT License (see [LICENSE](../../LICENSE)).*
