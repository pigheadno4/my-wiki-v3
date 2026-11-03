---
title: "Adyen Management API v3: List merchant accounts under a company"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/merchants"
raw_files:
  - "adyen/api-explorer/Management/latest/get/companies/(companyId)/merchants/2026-11-03.md"
tags: [adyen, management-api, merchant-accounts, account-structure]
---

## Overview

This captured Management API reference describes `GET /companies/{companyId}/merchants`: a paginated read of merchant accounts under the path's company account, limited to accounts accessible to the calling API credential. The documented server is `https://management-test.adyen.com/v3`; the credential needs the **Management API—Account read** role. See [[adyen]], [[adyen-account-structure]], and [[adyen-api-access]].

## Key takeaways

- `companyId` is the required path identifier of the company account. Optional integer query parameters are `pageSize` (default 10, maximum 100) and `pageNumber`; this reference gives no default for `pageNumber`. No request body is described.
- A 200 means the list request succeeded. The response schema has optional `data` merchant objects and optional pagination `_links`, plus required `itemsTotal` and `pagesTotal`. Where present, a merchant's `id` identifies the merchant account, `companyId` its parent, and `reference` its merchant reference; these are distinct fields. Merchant links can point to its own resource, API credentials, users and webhooks.
- Merchant fields include optional `status`, `captureDelay`, `defaultShopperInteraction`, legal-entity name/city, settlement currency, website, pricing plan, and data-center information. In test, `livePrefix` is empty and `default` is the returned data-center name. Read the raw schema for field-level optionality and allowed values.
- `PreActive` cannot process payments. For `Active`, the reference conditions enabled payment processing and payouts on the **company account also being Active**. `InactiveWithModifications` disallows new payments while allowing changes such as refunds and still allowing payouts; `Inactive` disables processing and payouts; `Closed` is irreversible. A listed account or a 200 response does not itself establish a completed payment, payout, bank receipt, or current live eligibility.
- The documented error responses are 400, 401, 403, 422 and 500. This GET reference states no idempotency, account creation/change/deletion, review/approval, activation, propagation, or reversal operation.

> [!warning] Version conflict
> The Servers section lists the test `/v3` base URL, while the 200 response example embeds `/v1` links. Treat the example as illustrative; this captured page does not resolve which version those returned links would use in a current response.

## Detail locators

- Purpose, credential role and test server: raw lines 5–14.
- Path and pagination parameters: raw lines 16–28.
- 200 response, pagination, merchant fields and status meanings: raw lines 30–71.
- Error response schemas: raw lines 74–171.
- Illustrative 200 payload and its older-version links: raw lines 173–433.

## Related

- [[adyen-account-structure]] — company and merchant account hierarchy.
- [[adyen-api-access]] — credential scope and permissions.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/merchants/2026-11-03|Adyen Management API merchant list reference, captured 2026-11-03]]
