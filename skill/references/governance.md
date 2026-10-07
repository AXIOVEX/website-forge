# Governance — spec-first, wireframes-gated change

## The flow (every change, in order)
1. **Specify.** Create or extend `specs/NNN-name/` (`NNN` = next free number):
   `spec.md` (what + why + requirements + claims with provenance), `plan.md`
   (steps), `tasks.md` (checkboxes; gates are tasks).
2. **Wireframes — if the change is visible.** Update `docs/wireframes/`
   (drawings + an index/revision log). Content-only changes on an existing
   template (e.g. a new blog article) skip the drawing and say so in the spec.
3. **Owner gate.** Approval is a blocking task. Prepare a recommendation —
   when one option is clearly right, recommend that one; do not present false
   choices. Nothing visible is built before approval.
4. **Implement on staging.** Edit sources/templates, never generated output.
   New CSS/JS versions get new versioned filenames.
5. **Verify on staging** (see visual-verification.md).
6. **Promote** by merging `staging` → `main` under the guard-proof checklist
   (staging-and-promotion.md), then verify production the same way.
7. **Close out.** Update the spec/tasks with what actually happened and the
   evidence (scores, screenshots, commit hashes). If what shipped differs
   from the wireframes, update the wireframes in the same change.

## Claims and copy rules
- Every factual claim in copy needs provenance recorded in the spec (vendor
  page, primary source, internal record, dated scan). Modeled or projected
  numbers are labeled modeled/projected wherever they appear.
- A checker, an AI suggestion, or a style preference never edits a claim.
  Findings about wording are owner decisions.
- Legal pages (privacy, disclaimer, terms): state only what is true of the
  actual stack (host, processors, forms, list handling), cross-reference
  rather than duplicate, and never let one page quietly re-broaden a promise
  another page narrowed.

## Repo hygiene
- Generated output is committed by the build (or a CI sync action) and never
  hand-edited; edit the generator's inputs (templates, Markdown, data).
- Expect automation commits (content sync, data refresh). Rebase; never
  force-push a shared branch.
- One logical change per commit where practical; messages name the spec.
