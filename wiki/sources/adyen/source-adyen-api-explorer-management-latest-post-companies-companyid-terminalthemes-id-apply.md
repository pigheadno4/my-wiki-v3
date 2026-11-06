---
title: "Adyen Management API: apply a company terminal theme"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/companies/(companyId)/terminalThemes/(id)/apply"
raw_files:
  - "adyen/api-explorer/Management/latest/post/companies/(companyId)/terminalThemes/(id)/apply/2026-11-07.md"
tags: [adyen, management-api, android-terminals, terminal-themes]
---

## Overview

This 2026-11-07 Management API `latest` reference describes `POST /companies/{companyId}/terminalThemes/{id}/apply` on the listed TEST `/v3` server. It applies the identified theme to Android terminals under the company unless a different theme is applied at merchant, store, or individual-terminal level. The `200` response is only documented as `OK`, with no response body or on-device confirmation. See [[adyen]] and [[adyen-android-terminals]].

## Key takeaways

- Both path parameters are required: `companyId` identifies the company account and `id` the terminal theme. The API credential needs `Management API - Terminal themes read and write`. No query parameter or request body is listed.
- This is a company-level theme-application operation, subject to lower-level overrides. A `403` example says only company-owned themes can be applied at company level; that example illustrates a possible failure and does not describe all ownership checks.
- Documented responses are `200` OK, `401` unauthorized, `403` forbidden, `404` not found, and `500` internal server error. The reference gives no propagation time, terminal acknowledgement, theme image/video payload, idempotency rule, or installation state. `200` does not establish that every device currently displays the theme or that a payment can be processed.

## Detail locators

- Apply scope, role, TEST server and required path IDs: pinned raw lines 5–22.
- Response headings and absence of success body: pinned raw lines 24–43.
- Illustrative error payloads, including company-owned-theme `403` and account-access `404`: pinned raw lines 45–96.

## Related

- [[adyen-android-terminals]] — Android terminal theming and configuration context.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/companies/(companyId)/terminalThemes/(id)/apply/2026-11-07|2026-11-07 pinned apply company terminal theme reference]]