---
title: "Create a company shipping location | Adyen Management API v3"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/companies/(companyId)/shippingLocations"
raw_files:
  - "adyen/api-explorer/Management/latest/post/companies/(companyId)/shippingLocations/2026-11-05.md"
tags: [adyen, management-api, shipping-locations, terminal-ordering]
---

## Overview

This 2026-11-05-captured Management API reference describes `POST /companies/{companyId}/shippingLocations`, which creates a delivery-address record for the company identified by the required `companyId` path parameter. A shipping location can later be referenced as `shippingLocationId` when creating an order; this POST does not itself place or deliver an order. The listed server is TEST `https://management-test.adyen.com/v3`. The caller's API credential needs **Management API—Terminal ordering read and write**. The page says Live requests are rate-limited without stating a numerical limit. See [[adyen]] and [[adyen-terminal-management]].

## Key takeaways

- The request-body table marks `address`, `contact`, `id` and `name` optional; all listed children of those optional objects are also marked optional. It does not independently declare whole-body requiredness or an idempotency rule. `name` is described as unique, `country` as an ISO 3166-1 alpha-2 code and `stateOrProvince` as ISO 3166-2 for the specified countries. The `contact.phoneNumber` table says 10–14 digits with an optional `+` prefix.
- `200` says the request succeeded. Its response table offers `id`, `name`, `address` and `contact`, all marked optional, and describes `id` as the later order's `shippingLocationId`. The example includes an ID, but the schema does not guarantee one in every shown body. Creation does not prove order creation, stock allocation, shipment or receipt.
- Listed errors are `400`, `401`, `403`, `422` and `500`. The generic error `requestId` description invokes `pspReference`, but this is a shipping-location configuration request, not a payment. The snapshot does not state later propagation, deletion/reversal or order-approval behavior.

> [!warning] Contradiction
> The request and response tables describe `contact.phoneNumber` as 10–14 digits with only an optional `+` prefix, but both examples use `+31 020 1234567` with spaces. The examples do not resolve whether spaces are accepted by validation.

## Detail locators

- Raw lines 5–44: purpose, credential role, Live rate-limit caveat, TEST server, company path and request-property table.
- Raw lines 46–91: illustrative request, `200` result and response schema.
- Raw lines 94–191: error cases and bodies; lines 193–215: illustrative `200` response.

## Related

- [[adyen-terminal-management]] — terminal-ordering and fleet administration context.
- [[source-adyen-docs-point-of-sale-automating-terminal-management-order-terminals-api]] — separate order-creation guide.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/companies/(companyId)/shippingLocations/2026-11-05|2026-11-05 company shipping-location creation reference]]