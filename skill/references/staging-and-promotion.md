# Staging & promotion — the two-environment flow

## Topology
- Repo branches: `main` = production, `staging` = long-lived staging branch.
- Cloudflare Pages: **two projects** on the same repo — production project
  builds `main`; staging project builds `staging` and serves
  `staging.<domain>` (plus its `*.pages.dev` URL).
- No build command for plain static sites; output = repo root (or your
  publish directory). Generated sites commit their output and also deploy
  with no build command — the generator runs locally or in CI.

## Staging guards (staging branch ONLY)
- `robots.txt` on staging is exactly: `User-agent: *` / `Disallow: /`
  (staging must never be indexed).
- `_headers` on staging = the production file **plus exactly one line**:
  `X-Robots-Tag: noindex, nofollow` under the `/*` rule.
- Staging form endpoints use test keys and have **no mail-delivery secrets**,
  so a staging submission can never reach a real inbox; it ends at a
  graceful, visible fallback.

## The promotion rule (guard-proof — the heart of this reference)
Merging `staging` → `main` will try to carry the guard files with it. Before
pushing any promotion merge:
1. `git diff <old-main>..HEAD -- robots.txt` must be **empty**.
2. `git diff <old-main>..HEAD -- _headers` must be **empty** (or exactly the
   intended production change, if the spec changes production headers).
3. The promotion file list must be **exactly the spec's file set** — nothing
   else rode along.
If a guard file appears in the diff: restore the production version inside
the (unpushed) merge, or as a clearly named guard-restoration commit, and
re-run the proofs. Never push first and fix later.

## Sync-back
After promotion, staging is behind. Sync by merging `main` → `staging`, then
re-apply the two guard files in one commit before pushing. Verify staging
still serves `noindex` and the disallow robots afterwards.

## Verification at each step
- Staging: page returns 200 with the new content, guards intact
  (`x-robots-tag: noindex` header, disallow robots), screenshots taken.
- Production after promotion: 200, production robots = `Allow: /` + sitemap
  line, **no** `x-robots-tag`, sitemap includes any new URL, headers intact.

---

*Copyright (c) 2026 Axiovex Systems, LLC — MIT License (see [LICENSE](../../LICENSE)).*
