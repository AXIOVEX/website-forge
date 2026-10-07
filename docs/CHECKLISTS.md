# Checklists

## Launch checklist (a new site going public)
- [ ] Domain registered; DNS in Cloudflare; HTTPS works; www → canonical redirect preserves path + query
- [ ] Email records (MX/SPF/DKIM/DMARC) verified **separately** from web DNS — web work never edits mail records
- [ ] Production Pages project builds `main`; staging project builds `staging` at `staging.<domain>`
- [ ] Staging guards live: disallow robots + `x-robots-tag: noindex` on staging only
- [ ] robots.txt (Allow + AI crawlers + Sitemap line), sitemap.xml, llms.txt, llms-full.txt all HTTP 200
- [ ] Every page: unique title, meta description, canonical, OG/Twitter with a real 1200×630 image, favicon set
- [ ] JSON-LD validates with zero errors (Organization/WebSite/WebPage; Article per article)
- [ ] Privacy page states only what the real stack does; contact route works end-to-end (a test reaches the inbox)
- [ ] Search Console + Bing verified; sitemap submitted
- [ ] Desktop + mobile screenshots of every page type filed with the launch spec
- [ ] SCORES.md opened with the first AEO + SEO scanner runs (scanner, URL, date)

## Promotion guard-proof (every staging → production promotion)
- [ ] Owner approval recorded in the spec's tasks (gate task checked, with who/when)
- [ ] `git diff <old-main>..HEAD -- robots.txt` is EMPTY
- [ ] `git diff <old-main>..HEAD -- _headers` is EMPTY (or exactly the spec'd production change)
- [ ] Promotion file list = exactly the spec's file set
- [ ] Production after deploy: article/pages 200, robots = Allow, NO `x-robots-tag`, sitemap includes new URLs, headers intact
- [ ] Production screenshots (desktop + mobile) match the staging-approved render
- [ ] Sync-back done: `main` merged into `staging`, both guard files re-applied, staging still noindexed

## Weekly health checklist (~20–40 min, or automated)
- [ ] Pull traffic (Cloudflare API): requests, uniques (labeled), top pages, status mix in plain English
- [ ] Fresh AEO scan + fresh SEO scan; append to SCORES.md with date/URL/scanner
- [ ] Disposition findings: safe fix / by design (reason recorded) / owner decision
- [ ] Apply safe fixes only; version-bump any stylesheet; deploy via staging if the fix is visible
- [ ] Re-fetch robots/sitemap/llms live (all 200); confirm no `REPLACE_` tokens anywhere in the tree
- [ ] Write the report (headline → what this means → detail → scores → labeled suggestions); file it
- [ ] Anything marked [owner decision] is actually sent to the owner, not just written down

---

*Copyright (c) 2026 Axiovex Systems, LLC — MIT License (see [LICENSE](../LICENSE)).*
