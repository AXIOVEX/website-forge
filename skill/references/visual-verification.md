# Visual verification — screenshots or it didn't happen

## The rule
Never report a visual change as verified from source checks (curl, HTML
greps, schema parsing). A page can pass every source check and still render
broken — unstyled navigation, invisible card text, wrong link colors — when
a stylesheet is stale, a class is renamed, or a template diverges. Rendered
evidence is the only evidence.

## Procedure (staging, then again on production after promotion)
1. Render the changed pages with a real browser engine (Playwright or
   equivalent) at **desktop 1440px** and **mobile 390px** (add tablet 834px
   for layout-sensitive changes).
2. Capture top-of-page and full-page screenshots; keep them with the spec's
   work records.
3. Compare against the **approved wireframes**: layout, spacing rhythm,
   colors from the actual design palette (sample pixels when a color claim
   matters), text visibility, link styling, no horizontal overflow at any
   width.
4. Check interactive states the change touches (nav, menus, forms, share
   rows) — a static screenshot of a broken menu is a pass only if you opened it.
5. Accessibility quick pass: heading order with no skips, one H1 per page,
   alt text present, an automated axe-core (or equivalent) run with no *new*
   violations vs. baseline.

## Two traps that cause false "verified" claims
- **Stale stylesheet cache:** CDNs may serve a same-name CSS file for hours.
  If a screenshot looks unchanged, check the versioned filename in the page
  source before debugging anything else; visual changes ship under a *new*
  versioned filename precisely to defeat this.
- **Repeat-visitor browser profiles:** a browser that has visited the site
  before can render an old cached build. Verify in a clean profile/context.

## Reporting
A verification report names: the URLs, the widths, where the screenshots are
filed, what was compared, and any residual findings — with the same honesty
rules as scores (a screenshot you didn't take is not a screenshot you took).
