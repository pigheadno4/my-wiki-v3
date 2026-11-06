---
title: "Adyen Management API: List company shipping locations"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/shippingLocations"
raw_files:
  - "adyen/api-explorer/Management/latest/get/companies/(companyId)/shippingLocations/2026-11-05.md"
tags: [adyen, management-api, terminal-orders, shipping-locations]
---

## Overview

The captured Management API `GET /companies/{companyId}/shippingLocations` lists shipping locations for the specified company and its merchant accounts. A location includes an address for deliveries and an ID used as `shippingLocationId` when ordering terminal products. The required path `companyId` is the company account identifier. The pinned reference lists `https://management-test.adyen.com/v3`; it also states that live requests are subject to rate limits without giving figures here. See [[adyen]] and [[adyen-terminal-management]].

## Key takeaways

- The API credential needs either Management API—Terminal ordering read or Management API—Terminal ordering read and write. Optional query parameters are `limit` (locations returned), `offset` (locations skipped), and `name` (location name); this reference specifies no defaults or numeric limit.
- The 200 response has an optional `data` array of physical shipping locations. Each entry's `id`, unique `name`, `address`, and `contact` are marked optional in the response table. The `id` is the reference to supply as `shippingLocationId` when creating an order; address and contact subfields are detailed in the raw schema.
- Listing a shipping location identifies a configured delivery destination; it does not create a terminal order, prove delivery, device assignment or boarding, or establish payment readiness. Example IDs and addresses are illustrative.
- Listed failures are 400, 401, 403, 422 and 500. This GET documents no request body, idempotency key, mutation, asynchronous approval or financial outcome.

## Detail locators

- Purpose, credential roles, live rate-limit qualification and TEST server: raw lines 5–20.
- Required path and optional query parameters: raw lines 21–35. Response fields, including `shippingLocationId` purpose: raw lines 36–60.
- Error schemas: raw lines 63–160. Illustrative 200 response: raw lines 162–204.

## Related

- [[adyen-terminal-management]]
- [[adyen-api-access]]

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/shippingLocations/2026-11-05|Adyen Management API company shipping locations list, captured 2026-11-05]]
