# Fixed retrieval checks — older 3D Secure Authentication report

Q1. Which authentication population and report scope does this Adyen page document, and what must not be inferred?
- Expected: The older 3D Secure Authentication report contains information about authentication attempts, has one entry per line, CET page-level report time zone, selected Customer Area date range, and stated company/merchant account availability. It does not define the newer report's filtering population, a user role, a completed retirement date, or successful authentication or payment outcomes.
- Raw locators: `raw/adyen/docs/reporting/3d-secure/authentication-report/2026-09-15.md:15-37`, `:46-55`, `:107-110`. Newer filtering and non-reconciliation qualification: `raw/adyen/docs/reporting/3d-secure/3ds-authentication-report/2026-09-15.md:17-23`.
- Canonical route: `wiki/sources/adyen/source-adyen-docs-reporting-3d-secure-authentication-report.md` → `[[adyen-reporting]]`; compare `[[source-adyen-docs-reporting-3d-secure-3ds-authentication-report]]`.

Q2. Which legacy fields distinguish 3DS flow evidence from authorisation and outcomes?
- Expected: Transaction currency/amount and creation time are fields, while 3DS version, exemption, retry, data-only, redirect and protocol response fields describe authentication flows. Directory versus authentication response fields vary by Redirect versus 3DS2 frictionless/challenge context. Acquirer response describes authorisation separately. Fallback directory response is for the initial failed 3DS2 attempt. A report row or liability-shift field does not prove capture, settlement or payout; newer report filtering means counts cannot be fully reconciled.
- Raw locators: `raw/adyen/docs/reporting/3d-secure/authentication-report/2026-09-15.md:49-70`, `:83-105`; newer boundary `raw/adyen/docs/reporting/3d-secure/3ds-authentication-report/2026-09-15.md:17-23`.
- Canonical route: `wiki/sources/adyen/source-adyen-docs-reporting-3d-secure-authentication-report.md` → `[[adyen-reporting]]`.
