---
title: "Adyen Management API: list company accounts"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/companies"
raw_files:
  - "adyen/api-explorer/Management/latest/get/companies/2026-09-15.md"
tags: [adyen, management-api, company-accounts, api-access]
---

## Overview

This 2026-09-15 Management API reference for `GET /companies` returns a paginated list of **company accounts accessible to the calling API credential**. It is a scoped read, not an operation to create or enable a company account or merchant payment capabilities. The credential needs the `Management API—Account read` role. [[adyen]] [[adyen-account-structure]] [[adyen-api-access]]

## Key takeaways

- The listed server is `https://management-test.adyen.com/v3`. Optional `pageSize` defaults to 10 and has maximum 100; `pageNumber` is optional (raw lines 13–22).
- A 200 response has required `itemsTotal` and `pagesTotal`; `data` and top-level `_links` are marked optional. Nested first/last/self links are marked required **within** `_links`, while next/prev are conditional on page existence (lines 24–58). Each listed company's `id`, `name`, `status`, `dataCenters` and connected-resource links are optional schema properties.
- Company `Active` permits user login, but processing and payouts still depend on merchant-account status. `Inactive` permits login while disabling payment processing/payouts; `Closed` is irreversible and disallows login/processing/payouts. These are company-status descriptions, not an observed transition in this GET response (line 56).
- `dataCenters.livePrefix` is empty in TEST; the page recommends a shopper-proximate live prefix for live requests (lines 49–51). The success sample uses `/v1` links despite the declared `/v3` server, so do not derive the captured endpoint version from sample hrefs (lines 13–14, 160–208).

## Detail locators

- Resource scope, role and pagination inputs: raw lines 5–22.
- Success response shape and optionality: 24–58; example: 160–208.
- 400 request, 401 authentication, 403 permission, 422 validation and 500 server error schemas: 61–158. No error examples are present.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/companies/2026-09-15|Management API GET companies, captured 2026-09-15]]
