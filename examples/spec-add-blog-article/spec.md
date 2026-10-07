# Example spec — Add a blog article (worked example, fictional site)

**Spec:** `specs/014-harbor-outlook-article/` · **Status:** approved, in staging
**Owner direction:** "Write up the quarterly harbor outlook as a blog article,
stage it, and show me before it goes live."

## What this adds
One article at `/blog/harbor-outlook-q4/` from
`blog/posts/2026-10-15-harbor-outlook-q4.md` (front matter per
templates/blog-post-template.md), rendered by the existing build.
**Content only — no UI change, so no wireframe update** (governance:
content on an existing template skips the drawing; this line is how the
spec records that).

## Claims (each with provenance — the discipline matters more than the format)
- C-1: Q3 container throughput figure — port authority's published Q3
  release (primary source, linked in the article).
- C-2: "Rates rose for a third week" — the index cited in the article,
  values as of the stated cutoff date.
- C-3: Any outlook probabilities are the editors' view, labeled as such.

## Requirements
- FR-001: Article opens with a 40–60 word self-contained summary.
- FR-002: Every statistic appears in body text with its source linked.
- FR-003: Article carries Article JSON-LD via the existing template
  (generated — not hand-written in the post).
- FR-004: Staging verification includes desktop + mobile screenshots and
  a fresh AEO scan of the staging article URL, recorded in tasks.md.
- FR-005: Promotion only after the owner's approval task is checked.
