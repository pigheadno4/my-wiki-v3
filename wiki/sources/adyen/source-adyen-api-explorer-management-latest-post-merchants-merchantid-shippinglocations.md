---
title: "Create a merchant shipping location | Adyen Management API v3"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/shippingLocations"
raw_files:
  - "adyen/api-explorer/Management/latest/post/merchants/(merchantId)/shippingLocations/2026-11-05.md"
tags: [adyen, management-api, shipping-locations, terminal-ordering]
---

## Overview

This 2026-11-05-captured Management API reference describes `POST /merchants/{merchantId}/shippingLocations`, which creates a shipping-location address under the merchant account identified by required `merchantId`. The location's ID can later serve as `shippingLocationId` when creating an order; this POST is not an order. The listed server is TEST `https://management-test.adyen.com/v3`. The caller's API credential needs **Management API—Terminal ordering read and write**. The page says Live requests are rate-limited without giving a number. See [[adyen]] and [[adyen-terminal-management]].

## Key takeaways

- The request table marks `address`, `contact`, `id` and unique `name` optional, along with their listed nested fields. It does not separately declare whole-body requiredness, defaults or idempotency behavior. `country` is an ISO 3166-1 alpha-2 code; `stateOrProvince` uses ISO 3166-2 for the listed countries. The `contact.phoneNumber` table specifies 10–14 digits and an optional `+` prefix.
- `200` says the request succeeded. Its response table marks `id`, `name`, `address` and `contact` optional; the example has a location ID but does not establish an always-present response field. `204` says successfully processed with no additional content. Neither result demonstrates creation of a later order, stock allocation, shipment or receipt.
- The page lists `400`, `401`, `403`, `422` and `500` errors. Its generic error `requestId` description mentions `pspReference`, but the operation is location configuration rather than a payment. The snapshot states no propagation, deletion/reversal or order-approval contract.

> [!warning] Contradiction
> The request table describes `contact.phoneNumber` as 10–14 digits with an optional `+` prefix, but its request example uses `+34 93 1234567` with spaces. The response example instead uses `+34931234567`. The examples do not establish whether spaced input is accepted or normalized.

## Detail locators

- Raw lines 5–44: purpose, role, Live rate-limit caveat, TEST server, merchant path and request fields.
- Raw lines 46–95: illustrative request, `200` response schema and `204` no-content result.
- Raw lines 98–195: documented errors and schemas; lines 197–220: illustrative `200` response.

## Related

- [[adyen-terminal-management]] — terminal ordering and fleet administration.
- [[source-adyen-docs-point-of-sale-automating-terminal-management-order-terminals-api]] — separate order-creation guide.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/merchants/(merchantId)/shippingLocations/2026-11-05|2026-11-05 merchant shipping-location creation reference]]