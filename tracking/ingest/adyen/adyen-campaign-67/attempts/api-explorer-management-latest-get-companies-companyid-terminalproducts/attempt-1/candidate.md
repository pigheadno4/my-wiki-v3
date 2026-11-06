---
title: "Adyen Management API v3: list company terminal products"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/terminalProducts"
raw_files:
  - "adyen/api-explorer/Management/latest/get/companies/(companyId)/terminalProducts/2026-11-05.md"
tags: [adyen, management-api, terminal-products, point-of-sale]
---

## Overview

This 2026-11-05-captured Management API v3 TEST reference defines `GET /companies/{companyId}/terminalProducts` to list country-specific payment-terminal packages and parts accessible to the company account in the path. This is a catalog read for [[adyen-terminal-management]], not a terminal order, delivery, boarding, or payment.

## Key takeaways

- `companyId` is a required company-account path string; `country` is a required ISO 3166-1 alpha-2 query string. Optional query fields are `limit`, `offset`, and `terminalModelId` (a model ID from `GET /terminalModels`). The page states no defaults or numeric bounds for pagination.
- The API credential needs either `Management API—Terminal ordering read` or `Management API—Terminal ordering read and write`. The listed server is TEST `https://management-test.adyen.com/v3`; the page says live requests are rate limited without giving a rate here.
- A 200 response has an optional `data` array of orderable terminal products. Each product may include `id`, `name`, `description`, `itemsIncluded`, and `price` with `currency` and `value`. The example's zero prices and EU product identifiers are illustrative; they do not establish a price or stock for another request or time.
- Errors listed are 400, 401, 403, 422, and 500. A successful catalog read does not prove the caller can place an order, that products are presently available in live, that a device is deployed, or that payments can be processed.

## Detail locators

- Purpose, roles, live rate-limit note, TEST server: raw lines 5–18.
- Required path/query and optional filters: raw lines 20–34.
- 200 response fields and errors: raw lines 36–151.
- Illustrative product and price response: raw lines 153–216.

## Related

- [[adyen-terminal-management]] — ordering and fleet-management context.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/terminalProducts/2026-11-05|GET company terminalProducts, captured 2026-11-05]]