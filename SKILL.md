---
name: website-forge
description: "Build and run a small-business website on GitHub (source of truth) + Cloudflare Pages (hosting): spec-first governance with a wireframes approval gate, a staging branch + staging site with a guarded staging→production promotion, SEO + AEO to near 100 (robots/sitemap/llms.txt, meta/OG, JSON-LD, citability), rendered-screenshot visual verification, scheduled analytics + SEO/AEO reporting with a safe-fix policy, and an optional double-opt-in newsletter. Use whenever a task touches a website run this way — publishing content, changing pages, auditing SEO/AEO, promoting staging, or checking traffic."
version: 1.0.0
license: MIT
---

# website-forge — the website operating skill

## Orientation
A website run this way is **static files in a GitHub repository**, delivered by
**Cloudflare Pages** through its Git integration: push to `main` deploys
production; push to the long-lived `staging` branch deploys a separate staging
Pages project at `staging.<your-domain>`. There is no CMS, no database (except
an optional newsletter list store), and no server to administer. Dynamic needs
are small and specific: a contact-form endpoint (Pages Function), analytics
(Cloudflare's API), and optionally a newsletter (a list store + a mail sender).

## FORCED REQUIREMENTS (non-negotiable)
1. **Spec first.** Every change is specified in `specs/NNN-name/` in the site
   repo (`spec.md` requirements, `plan.md`, `tasks.md`, claims with provenance
   where facts are asserted) before it is built. Small fixes ride under an
   existing spec's scope or the monitoring safe-fix policy — never unspecified.
2. **Wireframes before UI.** Any change a visitor can see starts in
   `docs/wireframes/`, and the **owner approves it** — approval is a blocking
   task in `tasks.md` — before implementation. Shipped wireframes must match
   the shipped site; drift is a process defect.
3. **Staging before production.** Build and verify on `staging` first.
   Promotion is a merge `staging` → `main`, never hand-copying files, and the
   staging guard files (`robots.txt` disallow-all, the `_headers` noindex
   line) must **never** appear in a promotion diff — if they do, STOP.
   See references/staging-and-promotion.md.
4. **Visual verification is mandatory.** "Verified" = live fetch + a fresh
   scanner/checker run where relevant + **rendered screenshots at desktop
   AND mobile widths compared against the approved wireframes**, on staging
   and again after promotion. Source checks alone never verify a visual
   change. See references/visual-verification.md.
5. **Claims discipline.** Never invent or strengthen claims (certifications,
   compliance status, partnerships, statistics, prices, addresses). Where
   evidence is incomplete, copy gets narrower, never padded. Unknown values
   become clearly marked `REPLACE_` tokens, listed to the owner — never guesses.
6. **Versioned assets.** Stylesheets/scripts ship under versioned filenames
   (`styles.v12.css`). CDNs cache same-name files for hours; a "fix" behind a
   stale filename looks un-fixed and wastes everyone's time.
7. **Secrets never travel.** Tokens and keys live only in the host's secret
   store or a mode-600 `.env` outside git. Refer to them by name and location,
   never by value — not in chat, commits, reports, or issues.
8. **Owner-only decisions.** Marketing claims, founder/brand wording, prices,
   legal copy, billing, and sending anything as the owner (posts, mail) happen
   only under the owner's direction for that item. Checker tools never edit
   claims: findings about copy are surfaced, not auto-fixed.

## Task index
| To do this | Follow |
|---|---|
| Publish a blog article / content page | references/governance.md + the blog authoring flow in docs/GETTING-STARTED.md §Blog; worked example: examples/spec-add-blog-article/ |
| Change layout, styling, navigation | references/governance.md (spec + wireframes + owner gate), then references/staging-and-promotion.md |
| Run an SEO/AEO audit or fix findings | references/seo-aeo.md, tools in mcp-server/, starters in templates/ |
| Promote staging to production | references/staging-and-promotion.md + docs/CHECKLISTS.md (promotion guard-proof) |
| Check traffic / produce a report | references/analytics-reporting.md |
| Estimate or compare hosting costs | references/costs.md (full table: docs/COSTS.md) |
| Add a newsletter | references/newsletter.md |
| Verify a change visually | references/visual-verification.md |

## Scores to hold (targets, restated honestly)
- AEO (e.g. check.aeojs.org): **95–100**. Achievable in full with this method.
- SEO checkers (e.g. Seobility): **~90 with zero errors**. The "external
  factors / backlinks" sub-score sits near zero on a young site and improves
  only as real sites link to you. Never buy links, never manufacture them,
  and never report the composite without naming that ceiling.
- Performance: homepage HTML under ~250 KB; PDFs, audio, and video are real
  files at real URLs — never base64 `data:` URIs embedded in a page.

## Working agreements for agents
- Work phase by phase; after each phase, commit, verify, record scores, and
  report before starting the next. Report every score with its scanner, the
  URL checked, and the date.
- When the right path is clear, take it and report; reserve owner questions
  for genuine trade-offs and the owner-only decisions above. Ask once, with
  the full list, rather than dribbling questions.
- Prefer deterministic generators and templates in this package over writing
  replacements from scratch. Grep for `REPLACE_` before every deploy; zero
  tokens may ship.

---

*Copyright (c) 2026 Axiovex Systems, LLC — MIT License (see [LICENSE](LICENSE)).*
