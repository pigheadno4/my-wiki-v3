---
title: "Adyen Management API: List merchant shipping locations"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/shippingLocations"
raw_files:
  - "adyen/api-explorer/Management/latest/get/merchants/(merchantId)/shippingLocations/2026-11-05.md"
tags: [adyen, management-api, terminal-orders, shipping-locations]
---

## Overview

The captured Management API `GET /merchants/{merchantId}/shippingLocations` lists shipping locations for the merchant account identified by the required path `merchantId`. A location has a delivery address and an ID to specify when ordering terminal products. The pinned reference lists `https://management-test.adyen.com/v3`; it separately says live requests are rate-limited without stating figures here. See [[adyen]] and [[adyen-terminal-management]].

## Key takeaways

- The API credential needs Management API—Terminal ordering read or Management API—Terminal ordering read and write. Optional query fields are `limit` (locations returned), `offset` (locations skipped) and `name` (location name). No default or numeric limit is specified here.
- The 200 response's `data` array is marked optional. Each location's unique `id`, unique `name`, `address` and `contact` are also marked optional in the response schema. The `id` is for use as `shippingLocationId` when creating an order; the raw schema lists address and contact subfields.
- The reference lists 204 success with no additional content and 400, 401, 403, 422 and 500 errors. The GET readback does not place an order, prove delivery or terminal boarding, or establish payment readiness. Sample response values are illustrative.

## Detail locators

- Purpose, roles, live rate-limit caveat and TEST server: raw lines 5–20.
- Required merchant path ID, query parameters and response fields: raw lines 21–60.
- 204 and error response schemas: raw lines 63–164. Illustrative 200 response: raw lines 166–192.
- This read operation documents no request body, idempotency key, lifecycle mutation, asynchronous approval/activation or financial result.

## Related

- [[adyen-terminal-management]]
- [[adyen-api-access]]

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/shippingLocations/2026-11-05|Adyen Management API merchant shipping locations list, captured 2026-11-05]]
