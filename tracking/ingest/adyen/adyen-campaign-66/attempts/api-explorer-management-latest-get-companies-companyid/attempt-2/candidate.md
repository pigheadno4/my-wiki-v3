---
title: "Adyen Management API: get a company account"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)"
raw_files:
  - "adyen/api-explorer/Management/latest/get/companies/(companyId)/2026-11-03.md"
tags: [adyen, management-api, company-accounts, api-access]
---

## Overview

This 2026-11-03 Management API reference describes `GET /companies/{companyId}`, a read of the company account identified by the path value. The calling API credential must have access to that company account and the `Management API—Account read` role. The listed server is `https://management-test.adyen.com/v3`. This read does not create or activate an account or establish merchant processing, payout, or payment outcomes. [[adyen]] [[adyen-account-structure]] [[adyen-api-access]]

## Key takeaways

- `companyId` is a required string path parameter; no query parameter or body is listed (raw lines 16–22).
- The 200 response is a company-account representation. Its top-level `_links` object is optional, while its nested `self` object is marked required only when `_links` is present. Top-level `dataCenters`, `description`, `id`, `name`, `reference`, and `status` are optional. `description` has a 300-character maximum. The connected-resource links for API credentials, users, and webhooks are optional (raw lines 23–47).
- `Active` permits login, while processing and payouts depend on merchant-account status. `Inactive` permits login but disables payment processing and payouts. `Closed` is irreversible and disables login, processing, and payouts. These are status definitions, not changes made by this GET request (raw line 47).
- `dataCenters.livePrefix` is empty in TEST. The page recommends a live URL prefix from a data center close to shoppers for live requests; the shown server alone does not prove live access (raw lines 13–14, 40–42).

> [!warning] Contradiction
> The declared TEST server uses `/v3`, but response-example resource hrefs use `/v1`. The sample hrefs do not establish this operation's version or resolve which version of those linked resources is applicable (raw lines 13–14, 149–179).

## Detail locators

- Purpose, credential access, role, server, and path input: raw lines 5–22.
- 200 schema, including optionality and account status: raw lines 23–47; example: 149–179.
- 400 request, 401 authentication, 403 permission, 422 validation, and 500 server errors and their response fields: raw lines 50–147. No error example is supplied.

## Related

- [[source-adyen-api-explorer-management-latest-get-companies]] — credential-scoped company-account list from a separate September 2026 snapshot.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/2026-11-03|Management API GET company account, captured 2026-11-03]]
