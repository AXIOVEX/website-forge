#!/usr/bin/env python3
"""
website-forge MCP server (FastMCP, stdio, no API keys required).
SPDX-License-Identifier: MIT
Copyright (c) 2026 Axiovex Systems, LLC

Tools are deterministic and (except for fetching the public site) offline.
Generators produce starting files — a human/AI must replace REPLACE_ tokens
with real owner-approved values before deploying.

Run:
  pip install -r requirements.txt
  python server.py            # stdio MCP server

Smoke test (no MCP client needed):
  python server.py --selftest https://example.com/
"""
import json, re, sys, urllib.request, urllib.error
from html.parser import HTMLParser

try:
    from mcp.server.fastmcp import FastMCP
except ImportError:  # allow --selftest without the package installed
    FastMCP = None

BASE_DEFAULT = "https://example.com"

AI_CRAWLERS = ["GPTBot","ChatGPT-User","OAI-SearchBot","ClaudeBot","Claude-User",
 "Claude-SearchBot","PerplexityBot","Perplexity-User","Google-Extended","Applebot",
 "Applebot-Extended","CCBot","cohere-ai","Meta-ExternalAgent","Meta-ExternalFetcher",
 "Amazonbot","YouBot","DuckAssistBot","MistralAI-User","Bytespider"]

def _fetch(url, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent":"website-forge-mcp/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, dict(r.headers), r.read()
    except urllib.error.HTTPError as e:
        return e.code, dict(e.headers or {}), e.read() if hasattr(e,"read") else b""
    except Exception as e:
        return 0, {}, str(e).encode()

class _Facts(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title=""; self._in_title=False; self.meta={}; self.canonical=None
        self.jsonld=0; self.jsonld_ok=0; self._in_ld=False; self._ld=""
        self.h1=0; self.h2=0; self.h3=0; self.img=0; self.time=0; self.links=0
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if tag=="title": self._in_title=True
        elif tag=="meta":
            k=(a.get("name") or a.get("property") or "").lower()
            if k: self.meta[k]=a.get("content","")
        elif tag=="link" and a.get("rel")=="canonical": self.canonical=a.get("href")
        elif tag=="script" and a.get("type")=="application/ld+json":
            self.jsonld+=1; self._in_ld=True; self._ld=""
        elif tag=="h1": self.h1+=1
        elif tag=="h2": self.h2+=1
        elif tag=="h3": self.h3+=1
        elif tag=="img": self.img+=1
        elif tag=="time": self.time+=1
        elif tag=="a": self.links+=1
    def handle_endtag(self, tag):
        if tag=="title": self._in_title=False
        if tag=="script" and self._in_ld:
            self._in_ld=False
            try: json.loads(self._ld); self.jsonld_ok+=1
            except Exception: pass
    def handle_data(self, d):
        if self._in_title: self.title+=d
        if self._in_ld: self._ld+=d

def audit_facts(base_url: str) -> dict:
    base_url = base_url.rstrip("/")
    status, headers, body = _fetch(base_url + "/")
    html = body.decode("utf-8", "ignore")
    f=_Facts(); f.feed(html)
    data_uris = re.findall(r'data:([a-z/+.-]+);base64,', html)
    disc={}
    for path in ["/robots.txt","/sitemap.xml","/llms.txt","/llms-full.txt","/favicon.ico"]:
        s,_,b = _fetch(base_url+path); disc[path]={"status":s,"bytes":len(b)}
    return {
        "url": base_url+"/", "http_status": status, "html_bytes": len(body),
        "content_encoding": headers.get("Content-Encoding"), "cache_control": headers.get("Cache-Control"),
        "hsts": bool(headers.get("Strict-Transport-Security")),
        "title": f.title.strip(), "title_chars": len(f.title.strip()),
        "meta_description": f.meta.get("description"), "canonical": f.canonical,
        "og": {k:v for k,v in f.meta.items() if k.startswith("og:")},
        "twitter_card": f.meta.get("twitter:card"),
        "jsonld_blocks": f.jsonld, "jsonld_valid": f.jsonld_ok,
        "h1": f.h1, "h2": f.h2, "h3": f.h3, "img": f.img, "time_tags": f.time, "links": f.links,
        "data_uri_count": len(data_uris), "data_uri_kinds": sorted(set(data_uris)),
        "discovery": disc,
    }


def headers_facts(url: str) -> dict:
    status, headers, _ = _fetch(url)
    wanted = ["Strict-Transport-Security","Content-Security-Policy","X-Frame-Options",
              "X-Content-Type-Options","Referrer-Policy","Permissions-Policy",
              "Cache-Control","Content-Encoding","X-Robots-Tag"]
    present = {k: headers.get(k) for k in wanted}
    return {"url": url, "http_status": status,
            "headers": present,
            "missing_security_headers": [k for k in wanted[:6] if not headers.get(k)],
            "is_staging_guarded": bool(headers.get("X-Robots-Tag"))}

def page_facts(url: str) -> dict:
    status, headers, body = _fetch(url)
    html = body.decode("utf-8", "ignore")
    f = _Facts(); f.feed(html)
    return {"url": url, "http_status": status, "html_bytes": len(body),
            "title": f.title.strip(), "title_chars": len(f.title.strip()),
            "meta_description": f.meta.get("description"),
            "description_chars": len(f.meta.get("description","")),
            "canonical": f.canonical, "og_count": len([k for k in f.meta if k.startswith("og:")]),
            "twitter_card": f.meta.get("twitter:card"),
            "jsonld_blocks": f.jsonld, "jsonld_valid": f.jsonld_ok,
            "h1": f.h1, "h2": f.h2, "time_tags": f.time,
            "healthy": status == 200 and f.h1 == 1 and bool(f.meta.get("description")) and f.jsonld == f.jsonld_ok}

def estimate(f: dict) -> dict:
    aeo=0; notes=[]
    d=f["discovery"]
    if d["/robots.txt"]["status"]==200: aeo+=10
    else: notes.append("robots.txt missing (-10)")
    if d["/sitemap.xml"]["status"]==200: aeo+=8
    else: notes.append("sitemap.xml missing (-8)")
    if d["/llms.txt"]["status"]==200: aeo+=10
    else: notes.append("llms.txt missing (-10)")
    if d["/llms-full.txt"]["status"]==200: aeo+=4
    if f["meta_description"]: aeo+=8
    else: notes.append("meta description missing (-8)")
    if f["canonical"]: aeo+=6
    else: notes.append("canonical missing (-6)")
    if f["og"]: aeo+=6
    else: notes.append("Open Graph missing (-6)")
    if f["jsonld_blocks"]>=3: aeo+=16
    elif f["jsonld_blocks"]>=1: aeo+=8; notes.append("JSON-LD partial — need Organization+WebSite+WebPage/Article (-8)")
    else: notes.append("no JSON-LD (-16)")
    if f["h1"]==1: aeo+=8
    if f["time_tags"]>=1: aeo+=4
    else: notes.append("no <time> tags (-4)")
    # citability proxy: content exists (links/headings) — full citability needs the official scanner
    if f["h2"]>=5: aeo+=10
    if f["html_bytes"]>1_000_000: notes.append(f"page weight {f['html_bytes']} bytes — performance risk, split data: URIs out")
    if f["data_uri_count"]: notes.append(f"{f['data_uri_count']} data: URIs — editions not crawlable")
    aeo=min(aeo,90)  # remaining ~10 pts are official-scanner citability, only it can award them
    return {"aeo_estimate_max": aeo, "note": "Estimate only. Official record = check.aeojs.org + Seobility fresh scans, with date/URL.", "gaps": notes}

def gen_robots(site_url: str) -> str:
    lines=["# Website — robots.txt (website-forge)","User-agent: *","Allow: /",""]
    for c in AI_CRAWLERS: lines += [f"User-agent: {c}","Allow: /",""]
    lines += [f"Sitemap: {site_url.rstrip('/')}/sitemap.xml"]
    return "\n".join(lines)

def gen_sitemap(urls: list) -> str:
    out=['<?xml version="1.0" encoding="UTF-8"?>','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls: out.append(f"  <url><loc>{u['loc']}</loc><lastmod>{u.get('lastmod','2026-10-07')}</lastmod></url>")
    out.append("</urlset>"); return "\n".join(out)

if FastMCP:
    mcp = FastMCP("website-forge")
    @mcp.tool()
    def audit_site(url: str = BASE_DEFAULT) -> dict:
        """Full SEO/AEO fact audit of the live site (meta, OG, JSON-LD, headings, data: URIs, discovery files)."""
        return audit_facts(url)
    @mcp.tool()
    def check_discovery(base_url: str = BASE_DEFAULT) -> dict:
        """Status/bytes for /robots.txt /sitemap.xml /llms.txt /llms-full.txt /favicon.ico only."""
        return audit_facts(base_url)["discovery"]
    @mcp.tool()
    def estimate_score(url: str = BASE_DEFAULT) -> dict:
        """Heuristic AEO estimate + gap list from a live audit. Label as estimate; official scanners are the record."""
        return estimate(audit_facts(url))
    @mcp.tool()
    def generate_robots(site_url: str = BASE_DEFAULT) -> str:
        """robots.txt allowing all AI crawlers in AI_CRAWLERS plus a Sitemap line."""
        return gen_robots(site_url)
    @mcp.tool()
    def generate_sitemap(urls: list) -> str:
        """sitemap.xml from [{loc, lastmod}] entries."""
        return gen_sitemap(urls)
    @mcp.tool()
    def generate_llms(site_name: str, site_url: str, summary: str, editions: list) -> str:
        """llms.txt from a summary + [{title, url, description}] editions list."""
        lines=[f"# {site_name}","",f"> {summary}","","## Editions"]
        for e in editions: lines.append(f"- [{e['title']}]({e['url']}): {e.get('description','')}")
        lines += ["", f"Site: {site_url}"]; return "\n".join(lines)

    @mcp.tool()
    def check_headers(url: str = BASE_DEFAULT) -> dict:
        """Security/cache header audit for one URL: which of HSTS/CSP/frame/content-type/referrer/permissions headers are present, cache + encoding, and whether a staging noindex guard (X-Robots-Tag) is set."""
        return headers_facts(url if url.startswith("http") else "https://" + url)
    @mcp.tool()
    def check_page(url: str = BASE_DEFAULT) -> dict:
        """Single-page health check: status, weight, title/meta lengths, canonical, OG count, JSON-LD validity, exactly-one-H1, <time> tags, and a boolean healthy flag."""
        return page_facts(url if url.startswith("http") else "https://" + url)
    @mcp.tool()
    def validate_html(html: str) -> dict:
        """Offline checks on an HTML string: title/meta lengths, JSON-LD parses, exactly 1 H1, no document data: URIs."""
        f=_Facts(); f.feed(html)
        return {"title_chars": len(f.title.strip()), "has_description": bool(f.meta.get("description")),
                "description_chars": len(f.meta.get("description","")), "canonical": f.canonical,
                "jsonld_blocks": f.jsonld, "jsonld_valid": f.jsonld_ok, "h1": f.h1,
                "document_data_uris": len(re.findall(r'data:(application|audio|text/css)', html)),
                "pass": bool(f.meta.get("description")) and f.h1==1 and f.jsonld==f.jsonld_ok and not re.findall(r'data:(application|audio)', html)}

if __name__ == "__main__":
    if len(sys.argv)>1 and sys.argv[1]=="--selftest":
        f=audit_facts(sys.argv[2] if len(sys.argv)>2 else BASE_DEFAULT)
        print(json.dumps(f, indent=2)); print(json.dumps(estimate(f), indent=2))
        assert f["http_status"]==200, "site did not return 200"
        print("SELFTEST OK")
    elif FastMCP is None:
        print("Install dependencies first: pip install -r requirements.txt", file=sys.stderr); sys.exit(1)
    else:
        mcp.run()
