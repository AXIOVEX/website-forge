# Contributing to website-forge

Thanks for helping make small-business websites cheaper to run and easier
to verify. Contributions are welcome — especially corrections to vendor
pricing/limits (with the vendor page and the date you checked it), new
checker findings, and anonymized field reports ("we ran the loop on a site
like X and learned Y").

## Ground rules (the same ones the skill enforces)
- **Claims need provenance.** Pricing, limits, and capability claims cite a
  vendor page or a dated primary record. Modeled numbers are labeled modeled.
- **No site-specific material.** No client names, domains (other than the
  publisher's own, used as the worked example), emails, account details, or
  screenshots containing them. Anonymize case studies ("a two-site client
  rebuild").
- **No secrets, ever** — not in code, docs, issues, or screenshots.
- Docs must be usable standalone: a reader with only this repo and their own
  AI should be able to execute what a document describes.

## How to contribute
1. Open an issue first for anything larger than a typo (templates in
   `.github/ISSUE_TEMPLATE/`).
2. Fork, branch (`docs/...`, `fix/...`, `feat/...`), keep one logical change
   per PR, and fill in the PR template — including the verification section.
3. If you change the MCP server: run `python mcp-server/server.py --selftest
   https://axiovexsystems.com/` and at least one other live URL, and paste
   the results in the PR.
4. By contributing you agree your work is licensed under this repo's MIT
   license.
