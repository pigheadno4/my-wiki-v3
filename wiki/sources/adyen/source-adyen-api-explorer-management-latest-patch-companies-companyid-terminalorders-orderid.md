---
title: "Adyen Management API v3: update a company terminal products order"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/patch/companies/(companyId)/terminalOrders/(orderId)"
raw_files:
  - "adyen/api-explorer/Management/latest/patch/companies/(companyId)/terminalOrders/(orderId)/2026-11-05.md"
tags: [adyen, management-api, terminal-management, terminal-orders]
---

## Overview

This 2026-11-05-captured Management API reference describes `PATCH /companies/{companyId}/terminalOrders/{orderId}` to update a terminal products order. The listed server is `https://management-test.adyen.com/v3`; the credential needs **Management API—Terminal ordering read and write**. The page separately notes rate limits for live requests. See [[adyen]] and [[adyen-terminal-management]].

## Key takeaways

- Updating is possible only while the order status is **`Placed`**. Both `companyId` (company account) and `orderId` (order) are required string path IDs.
- The body need contain only fields to change, **except `items` must be sent as the complete replacement array** when products change. Omitting an existing item from that submitted array removes it. The schema marks all listed body fields optional: `billingEntityId`, `customerOrderReference`, `items` with optional product subfields, `orderType`, `shippingLocationId`, and `taxId`. It says Brazil product orders do not need `billingEntityId`; this does not make that field schema-required for all other PATCH requests.
- HTTP `200` returns order details, with schema-optional order ID, status, items, order date, billing entity, shipping location, customer reference and carrier `trackingUrl`. The example returns `status: "Placed"`; it does not prove shipment, inventory, billing, arrival or terminal boarding. No idempotency or propagation timing is specified.

## Detail locators

- Purpose, `Placed` gate, whole-`items` replacement, role, live rate-limit notice, TEST server, and path identities: raw lines 5–29.
- Optional request fields, Brazil `billingEntityId` note, and illustrative item request: raw lines 32–69.
- `200` response schema, nested billing/shipping identities, order status and tracking URL: raw lines 70–117. Illustrative response: raw lines 219–277.
- `400`, `401`, `403`, `422`, and `500` problem response schemas: raw lines 120–217; `401` means authentication required and `403` insufficient permission.

## Related

- [[adyen-terminal-management]] — terminal-ordering and fleet administration routes.
- [[adyen-api-access]] — API credential context.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/patch/companies/(companyId)/terminalOrders/(orderId)/2026-11-05|Adyen Management API update company terminal order, captured 2026-11-05]]
