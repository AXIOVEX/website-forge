# Newsletter — a list you own, built carefully

A checker score brings a visitor once; a list brings them back every
edition, and returning readers who share are how real backlinks accrue.
A newsletter is also the most legally sensitive feature on a small site —
build it like it matters.

## Non-negotiables
- **Double opt-in:** subscribe → confirmation email → confirmed. Keep
  per-subscriber consent proof (timestamp, source, confirmation) in the
  list store.
- **Suppression is forever:** unsubscribed/suppressed addresses are kept
  **as hashes only** (so they can never be re-mailed), never as plaintext,
  and never deleted from the suppression set. Importing an old list means
  importing its unsubscribes too.
- **No subscriber data in git,** in the site repo, in analytics, or in chat
  with an AI. The list lives in its store (e.g. Cloudflare D1) and nowhere else.
- **Privacy policy covers the list:** what is collected, the lawful basis,
  retention, and how to withdraw — written before the first send.
- **CAN-SPAM (US):** a publishable postal address in every send's footer
  (a PO Box or registered-agent address is fine), a truthful subject, and
  one-click unsubscribe (`List-Unsubscribe` header + landing page).
  **Sending is blocked until the owner supplies that address.**
- **GDPR/UK:** explicit consent, no pre-checked boxes, withdrawal as easy
  as signup, export/delete on request.

## Sending architecture that works at this scale
- A **dedicated shared mailbox** in the organization's Microsoft 365 tenant
  (e.g. `newsletter@<domain>`, display name = the publication/site name).
- A mail app granted send permission **scoped to that one mailbox only** —
  never a tenant-wide credential for a website feature.
- SPF, DKIM, and DMARC pass on a test send before any real campaign.
- Content sends link back to the edition's own crawlable web page; the
  email is the notification, never the only copy of the content.

## Endpoints to build
subscribe · confirm · unsubscribe (GET landing + one-click POST) ·
privacy page · confirm/unsubscribe landing pages that match the site's
design system (they are pages like any other: spec, staging, screenshots).
Until the list store exists and is bound, subscribe endpoints should fail
closed (a clear "not yet" response), never silently accept addresses into
a void.
