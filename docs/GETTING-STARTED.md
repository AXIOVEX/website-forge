# Getting started — your website, the website-forge way

Budget about an hour for the accounts-and-connections pass. Everything after
that is git pushes.

## 1. Accounts you need
- **GitHub** — holds the site repo (free). This repo is the source of truth:
  if the live site and the repo ever disagree, fix from the repo.
- **Cloudflare** — one account holds the domain registration, DNS, hosting
  (Pages), security, and analytics. Sign up free.
- **A registrar** — simplest is Cloudflare Registrar itself (domains at
  cost, DNS already in the right place). ~$10/year for a typical `.com`.
- **Microsoft 365 or Google Workspace** — only when you want professional
  email on the domain and/or a newsletter sender mailbox. Add it when you
  need it; the website does not wait on it.
- Optional for distribution: accounts on the search consoles
  (Google Search Console, Bing Webmaster Tools).

## 2. The repo
- One repo per site. Static files at the publish root, or a generated site:
  sources (Markdown, templates, data) in the repo, a deterministic build
  script that renders the pages, generated output committed (see
  `templates/github-workflows/site-sync.yml.example`).
- Branches: `main` (production) and a long-lived `staging` branch. Create
  `staging` from `main` on day one, before your first real change.
- Put `docs/AGENT-INSTRUCTIONS.md` (from this package) in the repo as
  `AGENTS.md` and `CLAUDE.md`, and the skill at `.muse/skills/website-forge/`.

## 3. Connect GitHub → Cloudflare Pages (twice: production + staging)
1. In Cloudflare: Workers & Pages → Create → Pages → Connect to Git →
   authorize the Cloudflare GitHub app for **your site repo only**
   (least privilege: one app, named repos).
2. **Production project:** production branch `main`, no build command
   (plain static / pre-generated), output = your publish directory.
3. Attach your custom domain to the production project; let Cloudflare
   create the DNS record; confirm HTTPS and that `www` redirects to the
   apex (or your chosen canonical) with path + query preserved.
4. **Staging project:** a second Pages project on the same repo,
   production branch `staging`, domain `staging.<your-domain>`.
5. On the `staging` branch only, install the guards
   (`skill/references/staging-and-promotion.md`): disallow-all
   `robots.txt`, and `_headers` = production's file + the one noindex line.
   Staging form endpoints get test keys and **no** mail secrets.

## 4. The daily flow (this is the whole operating system)
spec → (wireframes + owner approval if visible) → implement on `staging` →
verify on staging (screenshots!) → owner review → merge `staging` → `main`
→ verify production → sync `main` back into `staging` with guards re-applied.
Promotion guard-proofs: `docs/CHECKLISTS.md`.

## 5. Blog (generated pattern)
Write Markdown with front matter (`templates/blog-post-template.md`) in
`blog/posts/YYYY-MM-DD-slug.md`; the build renders `/blog/` and
`/blog/<slug>/` (with BlogPosting JSON-LD, canonical/OG, breadcrumbs),
updates the sitemap and the feed, and the sync action commits the output.
Edit templates, never generated pages. A legacy `/blog/post?p=<slug>`
redirect shim keeps old shared links working if you migrate formats.

## 6. First-week extras that pay off for years
- `robots.txt`, `sitemap.xml`, `llms.txt` from `templates/`, live and 200.
- Organization/WebSite/WebPage JSON-LD from `templates/jsonld/`, validated.
- A privacy page at `/privacy/` — start from `templates/privacy-page.md`
  and state only what your real stack does.
- Search Console + Bing: verify the property, submit the sitemap.
- Turn on the weekly loop (`skill/references/analytics-reporting.md`) —
  even a 20-minute manual version beats discovering a problem in month six.

---

*Copyright (c) 2026 Axiovex Systems, LLC — MIT License (see [LICENSE](../LICENSE)).*
