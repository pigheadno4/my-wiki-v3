---
title: "3D Secure Conversion report | Adyen Docs"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/reporting/3d-secure/conversion-report"
raw_files:
  - "adyen/docs/reporting/3d-secure/conversion-report/2026-09-15.md"
tags: [adyen, reporting, 3d-secure, authentication, conversion]
---

## Overview

This 2026-09-15 [[adyen]] Docs snapshot is a column reference for the **3D Secure Conversion report**, which includes transactions that used 3D Secure. It says the report is based on CET and describes each line below its header as a separate entry. Despite the title, the page provides no conversion-rate formula or denominator, filtering rule, generation schedule, or access-role requirement. [[adyen-reporting]] [[adyen-3d-secure]]

## Key takeaways

- The column table identifies company and merchant, payment PSP reference and merchant reference, acquirer, method, transaction creation date and time-zone field, currency and transaction amount. The report-level CET basis should not be confused with a promise that every transaction time-zone field has a fixed value.
- Shopper-interaction, BIN, shopper name/IP/country/email, CVC-supplied and CVC-response fields appear in the column reference. Their presence is a schema description, not a statement that each value is populated for every entry; treat potentially personal fields with the appropriate access boundary.
- `threed_directory_response` describes whether 3D Secure was offered for the transaction; `threed_authentication_response` is described as explaining the outcome of the authorisation attempt. The table gives **C** and **Y** only as examples, not a complete status map. The separate acquirer-response fields are responses to authorisation. Do not infer payment approval, capture, settlement, a 3DS challenge, or a computed conversion rate from the field names or examples alone.
- The raw page does not specify inclusion/exclusion filters beyond transactions that used 3D Secure, report-generation or download method, user permissions, aggregation or rate calculation. Consult the specific report-generation and 3DS lifecycle guides for those separate questions.

## Detail locators

- **CET and report population:** raw lines 19–23.
- **Entry grain and identity/amount/date/shopper columns:** raw lines 25–56.
- **3DS directory/authentication-response example columns:** raw lines 57–58.

## Related

- [[adyen]]
- [[adyen-reporting]]
- [[adyen-3d-secure]]
- [[source-adyen-docs-reporting-3d-secure-authentication-report]] — separately documented authentication report

## Raw Sources

- [[raw/adyen/docs/reporting/3d-secure/conversion-report/2026-09-15|Adyen 3D Secure Conversion report — collected 2026-09-15]]
