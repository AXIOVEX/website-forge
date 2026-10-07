# Costs — the verified comparison

*Vendor figures checked against the vendors' own pricing/limits pages on
2026-10-07. Prices change — re-check before budgeting. The modeled example
is labeled as modeled wherever it appears; it is arithmetic on published
rates, not a bill anyone received.*

## The table

| What you pay for | GitHub + Cloudflare Pages | Azure Static Web Apps | AWS (assembled) |
|---|---|---|---|
| Hosting | **$0** (free plan) | $0 free tier; Standard **$9/app/month** | Parts-based; ~$1–3/month for storage+delivery basics at small scale |
| Bandwidth | **Unlimited, unmetered** for static assets (free plan) | 100 GB/month included per subscription, then **$0.20/GB** | Metered per GB (CDN egress) |
| Builds | **500 builds/month** (free) | Via GitHub Actions (your minutes) | Amplify: 1,000 free build minutes, then usage |
| Edge functions | Pages Functions/Workers: 100k requests/day (free) | Functions within plan limits (Free: 0.25 GB/app max, 2 custom domains) | Lambda + API Gateway, each metered, each configured separately |
| Custom domains | 100 per project (free), SSL free | 2 (Free) / 5 (Standard), SSL free | ACM certificates free; you wire them |
| Firewall | Included (managed rules on free/paid tiers) | Front Door (its CDN+WAF tier) starts ~$35/month base + usage | AWS WAF: **$5 per Web ACL + $1 per rule + $0.60 per million requests** |
| Domain | ~**$10/year** at registrar cost (e.g. Cloudflare Registrar) | Same, wherever bought | Same (Route 53 registration is comparable) |
| Analytics | Built-in web analytics + API reporting, free | Application Insights (metered) | CloudWatch etc. (metered) |

## The worked example (modeled)
A site serves **1 TB** in a month — a genuinely popular month.
- **Cloudflare Pages free:** hosting bill **$0**. Bandwidth is not metered.
- **Azure Static Web Apps Standard:** $9 + (1,024 − 100) GB × $0.20 ≈ **$189
  (modeled)**.
- **AWS:** the same terabyte is a sum of per-GB line items across the CDN
  and storage services, plus the WAF arithmetic above — tens of dollars at
  minimum, and a bill that needs reading either way.

## The second cost nobody tables: assembly
AWS/Azure for a static site means assembling storage + CDN + certificates +
DNS + CI + WAF across several consoles, and *remembering* that assembly
forever. This stack has two places to look: the GitHub repo and one
Cloudflare account. For a small business, the operator-hours difference
routinely exceeds the hosting difference.

## Sources (vendor pages, checked 2026-10-07)
- Cloudflare Pages limits & pricing — developers.cloudflare.com/pages/platform/limits/ and /pages/functions/pricing/
- Cloudflare Workers pricing — developers.cloudflare.com/workers/platform/pricing/
- Azure Static Web Apps pricing — azure.microsoft.com/en-us/pricing/details/app-service/static/
- AWS WAF pricing — aws.amazon.com/waf/pricing/
- AWS Amplify pricing — aws.amazon.com/amplify/pricing/

## The boundary
Real application backends, named-cloud compliance regimes, committed
enterprise spend, and library-scale video belong on AWS/Azure or
purpose-built media services. Host that project there; keep the website
here. The website is portable by construction — plain files in a repo.
