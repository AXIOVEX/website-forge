# MCP Server — website-forge

<!-- SPDX-License-Identifier: MIT -->

A small, deterministic MCP server (FastMCP, stdio, **no API keys**) that gives
your AI the audit + generator tools described in `../skill/SKILL.md`.

## Install & smoke test
```bash
cd mcp-server
python3 -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python server.py --selftest https://your-site.example/
# expect: a JSON fact dump + an estimate + "SELFTEST OK"
# (the self-test also runs with NO packages installed — it only needs the stdlib)
```

## Connect it
### Muse (recommended for doing the file work)
From your website repo root:
```bash
Muse mcp add website-forge -- python /ABSOLUTE/PATH/TO/website-forge/mcp-server/server.py
```
Or commit an `.mcp.json` in the site repo (see `.mcp.json.example`).
### Claude Desktop
Add the same server block to `claude_desktop_config.json` (Settings → Developer
→ Edit Config), restart, and confirm the tools appear.
### ChatGPT
ChatGPT's consumer UI does not run local stdio MCP servers the way Muse
does. Either pair ChatGPT (planning/copy) with a coding agent that runs this
server, or — on plans with developer-mode MCP connectors — host this server
behind an HTTPS MCP endpoint and add it as a connector; tool names and
schemas are identical. Never paste API keys, passwords, or subscriber data
into any AI chat.

## Tools (9)
| Tool | What it does |
|---|---|
| `audit_site(url)` | Full fact audit: status, byte weight, title/meta/OG/canonical, JSON-LD count+validity, H1/H2/H3, images, `<time>` tags, links, `data:` URI count/kinds, discovery-file status |
| `check_discovery(base_url)` | HTTP status + bytes for `/robots.txt`, `/sitemap.xml`, `/llms.txt`, `/llms-full.txt`, `/favicon.ico` |
| `check_headers(url)` | Security/cache headers present vs. missing (HSTS, CSP, frame, content-type, referrer, permissions), encoding, and whether a staging `X-Robots-Tag` guard is set |
| `check_page(url)` | One page's health: title/description lengths, canonical, OG count, JSON-LD, exactly-one-H1, `<time>` tags, `healthy` boolean |
| `estimate_score(url)` | Heuristic AEO estimate + a gap list. Labeled an estimate — the official scanners are the record |
| `generate_robots(site_url)` | robots.txt allowing the major AI crawlers + a Sitemap line |
| `generate_sitemap(urls)` | sitemap.xml from `[{loc, lastmod}]` |
| `generate_llms(...)` | llms.txt from a site summary + a page/edition list |
| `validate_html(html)` | Offline checks on an HTML string before you deploy it |

All tools are read-only against the public web; generators only return text.
Nothing in this server deploys, writes, or sends anything.
