---
title: "Adyen Management API v3: update a merchant terminal products order"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/patch/merchants/(merchantId)/terminalOrders/(orderId)"
raw_files:
  - "adyen/api-explorer/Management/latest/patch/merchants/(merchantId)/terminalOrders/(orderId)/2026-11-05.md"
tags: [adyen, management-api, terminal-management, terminal-orders]
---

## Overview

This 2026-11-05-captured Management API reference describes `PATCH /merchants/{merchantId}/terminalOrders/{orderId}` to update a terminal products order under a **merchant account**. The listed server is `https://management-test.adyen.com/v3`; the credential needs **Management API—Terminal ordering read and write**. The page separately notes rate limits for live requests. See [[adyen]] and [[adyen-terminal-management]].

## Key takeaways

- Updating is possible only while the order status is **`Placed`**. Both `merchantId` (merchant account) and `orderId` (order) are required string path IDs.
- The request body need contain only fields to change, **except `items` must be sent as the entire replacement array** when products change. The schema marks `billingEntityId`, `customerOrderReference`, `items` and its product subfields, `orderType`, `shippingLocationId`, and `taxId` optional. It says Brazil product orders do not need `billingEntityId`; it does not mark that field required for all other PATCH requests.
- The reference documents both HTTP `200` with order details and HTTP `204` processed with no additional content. The `200` schema marks order ID, status, items, order date, billing and shipping objects, customer reference and carrier `trackingUrl` optional. The example's `Placed` order does not prove shipment, inventory, billing, arrival or terminal boarding.
- No idempotency or propagation timing is specified.

## Detail locators

- Purpose, `Placed` gate, whole-`items` replacement, role, live rate-limit notice, TEST server, and path identities: raw lines 5–29.
- Optional request fields, Brazil `billingEntityId` note, and illustrative item request: raw lines 32–69.
- `200` order response schema and `204` no-content result: raw lines 70–121; illustrative `200` response: raw lines 223–281.
- `400`, `401`, `403`, `422`, and `500` problem response schemas: raw lines 124–221. `401` means authentication required and `403` insufficient permission.

## Related

- [[adyen-terminal-management]] — terminal-ordering and fleet administration routes.
- [[adyen-api-access]] — API credential context.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/patch/merchants/(merchantId)/terminalOrders/(orderId)/2026-11-05|Adyen Management API update merchant terminal order, captured 2026-11-05]]
