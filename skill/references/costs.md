# Costs — why this stack, in numbers

Full table with sources: `docs/COSTS.md`. The short version:

- **Cloudflare Pages (free):** unlimited unmetered bandwidth for static
  assets, 500 builds/month, 100 custom domains per project, SSL + CDN + a
  firewall included, Pages Functions 100k requests/day on the free plan.
- **Domain:** ~$10/year at registrar cost.
- **Azure Static Web Apps:** free tier exists; Standard is **$9 per app per
  month**, 100 GB bandwidth included per subscription, then **$0.20/GB**.
  A modeled 1 TB month ≈ $9 + ~$180 ≈ **$189 (modeled, not a bill)**.
- **AWS, assembled:** storage + CDN + certificates + DNS + CI are separate
  metered services (~$1–3/month at small scale for the basics), and the
  firewall alone (AWS WAF) is **$5 per Web ACL + $1 per rule + $0.60 per
  million requests** — before hosting anything.
- **The hidden line item is time:** on AWS/Azure-for-a-static-site you are
  assembling and remembering a small platform. On this stack there are two
  places to look: the repo, and one Cloudflare account.

## The boundary (say it in every cost conversation)
Real application backends, named-cloud compliance, committed enterprise
spend, and library-scale video belong on AWS/Azure or purpose-built media
services. Host *that project* there; keep the marketing/content website on
this stack. Portability is the insurance: the site is plain files in a repo.

---

*Copyright (c) 2026 Axiovex Systems, LLC — MIT License (see [LICENSE](../../LICENSE)).*
