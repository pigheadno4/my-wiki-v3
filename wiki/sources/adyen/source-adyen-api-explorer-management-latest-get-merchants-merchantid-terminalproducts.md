---
title: "Adyen Management API v3: list merchant terminal products"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/terminalProducts"
raw_files:
  - "adyen/api-explorer/Management/latest/get/merchants/(merchantId)/terminalProducts/2026-11-05.md"
tags: [adyen, management-api, terminal-products, point-of-sale]
---

## Overview

This 2026-11-05-captured Management API v3 TEST reference defines `GET /merchants/{merchantId}/terminalProducts` to list country-specific payment-terminal packages and parts accessible to the merchant account named in the path. It is a product-catalog read within [[adyen-terminal-management]], not an order or device-state read.

## Key takeaways

- `merchantId` is a required merchant-account path string and `country` is a required ISO 3166-1 alpha-2 query string. Optional query parameters are `limit`, `offset`, and `terminalModelId` (a model ID from the merchant `GET /terminalModels` route). No pagination defaults or bounds are stated.
- The API credential needs `Management API—Terminal ordering read` or `Management API—Terminal ordering read and write`. The listed server is `https://management-test.adyen.com/v3`; the page notes live-environment rate limits without specifying their numbers here.
- A 200 response may include a `data` array of products that can be ordered. Entries may include `id`, `name`, `description`, `itemsIncluded`, and `price` with `currency` and `value`. The endpoint also lists 204 success with no content. The EU example's zero prices are illustrative, not a current or general price guarantee.
- Listed failures are 400, 401, 403, 422, and 500. A catalog response does not establish order placement, stock, delivery, boarding, terminal readiness, or payment execution.

## Detail locators

- Purpose, roles, rate-limit note and TEST server: raw lines 5–18.
- Merchant path and country/filter queries: raw lines 20–34.
- 200 fields, 204 and errors: raw lines 36–155.
- Illustrative product/price response: raw lines 157–220.

## Related

- [[adyen-terminal-management]] — ordering and fleet administration.
- [[source-adyen-api-explorer-management-latest-get-companies-companyid-terminalproducts]] — analogous company-account catalog path.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/terminalProducts/2026-11-05|GET merchant terminalProducts, captured 2026-11-05]]