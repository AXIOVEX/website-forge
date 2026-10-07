# MASTER PROMPT — paste once, after AGENT-INSTRUCTIONS.md


# AGENT INSTRUCTIONS — website-forge standing orders
# Save as AGENTS.md AND CLAUDE.md in the site repo root. Read in full before acting.

You are working on a website run the website-forge way. The package that
accompanies this file contains: skill/SKILL.md (your workflow + forced
requirements), skill/references/ (governance, staging & promotion, SEO/AEO,
visual verification, analytics reporting, costs, newsletter), mcp-server/
(your tools), templates/ (starting files), docs/CHECKLISTS.md.

## Standing orders
1. Read skill/SKILL.md completely before changing anything. Its FORCED
   REQUIREMENTS bind you: spec first; wireframes + owner approval before
   any visible change; staging before production; screenshot verification;
   claims discipline; versioned assets; secrets never travel; owner-only
   decisions (claims, branding, prices, legal copy, billing, sending as the
   owner) are surfaced, never decided by you.
2. Work in phases, in order. After each phase: commit, deploy to staging,
   verify, record scores, STOP and report before the next phase or any
   production promotion — unless the owner has told you to continue.
3. Never invent claims, statistics, dates, authors, addresses, prices, or
   links. Unknown = a `REPLACE_` token + a line in your report listing it
   as an owner decision. Grep for `REPLACE_` before every deploy; zero
   tokens may ship.
4. Never report a score you did not just run. Name the scanner, the URL,
   and the date with every score. Label MCP `estimate_score` output as an
   estimate; the official scanners are the record.
5. Never call a visual change verified without rendered screenshots at
   desktop (1440px) and mobile (390px), compared to the approved
   wireframes or the intended design. Source checks are not verification.
6. Promotion guard-proof, every time: the promotion diff must not contain
   staging's `robots.txt` or the staging `_headers` noindex line, and the
   file list must be exactly the spec's set. If a guard file appears, stop
   and restore the production version before pushing.
7. Prefer this package's templates and generators over writing replacements
   from scratch. Edit sources/templates — never generated output.
8. Never paste secrets, API keys, or subscriber data into files, commits,
   issues, or chat. Refer to secrets by name and location only.

## Report format (end of every phase)
- Scores: before → after (scanner, URL, date) for AEO and SEO, where relevant
- Files changed (list) + commit hashes
- Verification: live status of robots/sitemap/llms, JSON-LD validation,
  page weight where relevant, screenshot locations, guard-proof results
- Owner decisions / `REPLACE_` tokens still open (list, or "none")
- Next phase: one-line plan

Begin now with a baseline audit (MCP `audit_site` + the official AEO and SEO scanners), save the scores, write the spec for Phase 1 (discoverability files, head, structured data), and stop for my review before implementing.

---

*Copyright (c) 2026 Axiovex Systems, LLC — MIT License (see [LICENSE](../../LICENSE)).*
