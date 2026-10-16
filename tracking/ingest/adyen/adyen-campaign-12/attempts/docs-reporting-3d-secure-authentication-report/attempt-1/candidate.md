---
title: "Adyen 3D Secure Authentication report"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/reporting/3d-secure/authentication-report"
raw_files:
  - "adyen/docs/reporting/3d-secure/authentication-report/2026-09-15.md"
tags: [adyen, reporting, 3d-secure, authentication]
---

## Overview

This Adyen page describes the older **3D Secure Authentication report**, which contains information about 3D Secure authentication attempts. The report can be obtained manually or automatically, uses a page-level **CET** report time zone, lets the user select a Customer Area date range, and is described for company and merchant accounts. This captured page does not state a particular user's access role or current availability. See [[adyen]], [[adyen-reporting]], and [[adyen-3d-secure]].

## Key takeaways

- Each line under the report header is a separate entry. The table identifies company, merchant, acquirer, payment method, PSP and merchant references, transaction currency and amount, transaction creation date and its `time_zone` field. This is authentication-attempt reporting; a row does not by itself prove authentication success, payment authorisation, capture, settlement or payout.
- The column table distinguishes 3D Secure version, device channel, message category, authentication-only flag, soft-decline SCA retry, requested SCA exemption, data-only and redirect indicators. Directory/authentication response columns have **different definitions for 3D Secure Redirect and 3D Secure 2 frictionless/challenge flows**; use the specific field definition rather than a shared result interpretation.
- `acquirer_response` and `raw_acquirer_response` describe the authorisation response separately from 3D Secure response fields. The table also includes liability-shift, error, challenge-cancel and fallback indicators. For `threeds2_fallback_directory_response`, the page says it belongs to the initial failed 3DS2 attempt, so do not treat it as the final fallback result.
- The separate [[source-adyen-docs-reporting-3d-secure-3ds-authentication-report|3DS Authentication report]] says it **will replace** this older report and has updated filtering, so the two reports' numbers cannot be fully reconciled. The newer report's population is Adyen 3DS attempts or exemptions, excluding cases without applicable 3DS or authenticated by another provider. The older page does not establish equivalent filtering or a completed retirement date.

## Detail locators

- Report purpose, generation, CET, date range and account-type availability: pinned raw lines 15–27.
- Entry grain and identity, amount, timestamp and 3DS-flow fields: pinned raw lines 29–66.
- Redirect versus 3DS2 response meanings and identifiers: pinned raw lines 67–82.
- Authorisation-response, error, liability-shift and fallback fields: pinned raw lines 83–105.
- Successor-report and conversion-report navigation: pinned raw lines 107–110; successor's own filtering warning is in [[source-adyen-docs-reporting-3d-secure-3ds-authentication-report]].

## Related

- [[adyen-reporting]] — provider reporting and evidence boundary.
- [[adyen-3d-secure]] — 3D Secure integration context.
- [[source-adyen-docs-reporting-3d-secure-3ds-authentication-report]] — newer report with changed filtering; do not merge its row population with this report.

## Raw Sources

- [[raw/adyen/docs/reporting/3d-secure/authentication-report/2026-09-15|Adyen older 3D Secure Authentication report, captured 2026-09-15]]
