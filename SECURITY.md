# Security policy

## Scope
website-forge is documentation, templates, and a read-only MCP helper.
The MCP server fetches public URLs you give it and returns text; it holds
no credentials, writes nothing, and sends nothing. Templates include a
`_headers` starter — a starting point you must test on staging (especially
any Content-Security-Policy) before production.

## Reporting a vulnerability
Email **start@axiovexsystems.com** with "website-forge security" in the
subject. Include what you found, how to reproduce it, and the impact you
believe it has. Please do not open a public issue for a security report,
and do not include anyone's credentials or subscriber data in a report.
We aim to acknowledge within two business days.

## Good practice this project teaches (and follows)
- Secrets live in host secret stores or mode-600 files outside git — never
  in a repo, an issue, or a chat transcript.
- Least privilege everywhere: one GitHub App installation per site repo,
  one scoped API token per system, one mailbox-scoped sender per feature.
- Staging never holds production mail/data secrets.
