# Analytics & health reporting — the weekly loop that holds the scores

## What to measure (and where it comes from)
- **Traffic:** Cloudflare's analytics API (GraphQL) for the zone — requests,
  unique visitors (sum of daily uniques, always labeled as such), top pages,
  status-code mix, cached-bytes ratio. Zone API data is the source of truth,
  not a dashboard tab. Fail closed: if the API errors, the report says so and
  shows no invented numbers.
- **Visibility:** fresh AEO + SEO scanner runs (see seo-aeo.md), recorded in
  a score history so drift is visible over time.
- **Incidents in plain English:** every HTTP status code named in a report
  carries its meaning at first use (e.g. "500 — the server failed to handle
  a valid request"). A bare code number is a format defect. Scanner probes
  (e.g. requests for `/wp-admin/...` on a site with no WordPress) are
  reported as probes, not as lost visitors.

## Cadence that works
- **Daily (light):** yesterday vs. trailing 7-day average; one to four lines
  unless something is actually wrong.
- **Weekly (the real one):** 7 days vs. prior 7, fresh AEO/SEO scans, safe
  fixes applied under the policy below, score history updated.
- **Monthly:** month vs. month, what the trends mean in plain English, and
  next month's recommendations.
- **Push-triggered:** after any deploy, a re-check that the change landed
  and nothing regressed.

## Report format (non-negotiable structure)
Headline numbers → **"What this means"** in plain English (required) →
traffic detail → SEO/AEO → insights → suggestions. Facts, insights, and
suggestions are kept separate. Every suggestion is labeled **[auto-fixable]**
(safe technical fix: meta, headings, alt, schema, robots, sitemap, llms,
canonical, broken internal links, a new versioned stylesheet) or
**[owner decision]** (claims, branding, content, spend, new infrastructure).
Anything a data source couldn't serve is marked **Unavailable** with the
reason — never estimated or back-filled. At most two charts, only when a
pattern is easier to see than to read.

## Delivery
Reports are rendered documents (styled HTML email with a plain-text
fallback reads correctly everywhere; raw Markdown pasted into an email
client does not). Recipients and cadence are the owner's choice; the report
file is also saved with the project records either way.
