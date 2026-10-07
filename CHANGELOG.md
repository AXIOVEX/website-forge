# Changelog
All notable changes to website-forge. Format loosely follows Keep a Changelog;
versions are SemVer.

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
