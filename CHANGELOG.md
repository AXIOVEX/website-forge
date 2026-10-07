# Changelog
All notable changes to website-forge. Format loosely follows Keep a Changelog;
versions are SemVer.

## [Unreleased]
Cold-run validation of the whole package (see `VALIDATION.md`) plus a
templates/notices uplift.
- **Fixed:** the MCP score estimator counted JSON-LD `<script>` blocks, so a
  site built with this package's own `@graph` homepage template scored 82
  with a false "JSON-LD partial" gap. It now counts JSON-LD entities
  (`jsonld_entities` in `audit_site` output); the same site estimates at
  the 90 maximum, and a naive baseline page is unchanged.
- **Fixed:** `generate_sitemap` defaulted a missing `lastmod` to a
  hardcoded date; it now defaults to today's date.
- **Fixed:** duplicated header comment lines in `templates/robots.txt`.
- **Added:** `templates/privacy-page.md` — a plain-language privacy-page
  starter (the launch checklist required a privacy page; the package
  shipped nothing to start from), linked from the getting-started guide.
- **Changed:** `templates/head-snippet.html` now instructs per-page title /
  description / canonical / `og:url` instead of shipping the homepage's
  values on every page.
- **Changed:** issue templates converted from Markdown to GitHub issue
  forms (`bug.yml`, `feature.yml`, new `question.yml`) with an
  `ISSUE_TEMPLATE/config.yml` that routes security reports to
  `SECURITY.md` and disables blank issues.
- **Added:** a Disclaimer section in the README; copyright lines at the
  foot of the docs and skill files; SPDX identifiers in the workflow and
  HTML/JSON-LD templates. User-site templates assert no ownership by the
  package's author — names there are the site owner's own.
- **Added:** `VALIDATION.md` — the full cold-run report: method, scores,
  checklist results, and the friction log behind every fix above.

## [1.0.0] — 2026-10-07
Initial public release.
- The Skill (`skill/SKILL.md`) with forced requirements and seven references:
  governance, staging & promotion, SEO/AEO, visual verification, analytics
  reporting, costs, newsletter.
- The MCP server (9 tools: audit, discovery, headers, page check, score
  estimate, robots/sitemap/llms generators, HTML validation) with a
  dependency-free `--selftest` mode.
- Templates: robots/sitemap/llms starters, `_headers`, `_redirects`,
  a complete `<head>` snippet, JSON-LD (Organization/WebSite/WebPage,
  NewsArticle, FAQPage), a blog-post template, `.gitignore`, and a
  GitHub Actions generated-site sync workflow.
- Docs: getting started, agent instructions, master + per-phase prompts,
  launch/promotion/weekly checklists, and the verified cost comparison.
- Examples: a filled llms.txt and a complete worked spec for adding a
  blog article.
