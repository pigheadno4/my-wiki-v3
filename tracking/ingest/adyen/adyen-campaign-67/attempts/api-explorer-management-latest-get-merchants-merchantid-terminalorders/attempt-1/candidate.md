---
title: "Adyen Management API v3: list merchant terminal orders"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/terminalOrders"
raw_files:
  - "adyen/api-explorer/Management/latest/get/merchants/(merchantId)/terminalOrders/2026-11-05.md"
tags: [adyen, management-api, terminal-orders, merchant-accounts]
---

## Overview

This 2026-11-05-captured Management API reference documents `GET /merchants/{merchantId}/terminalOrders`, a list of terminal-product orders for the path-identified merchant account. The caller needs either `Management API—Terminal ordering read` or `Management API—Terminal ordering read and write`. The listed server is TEST `https://management-test.adyen.com/v3`; Live requests are subject to rate limits, without a numeric value here. Order readback is not shipment delivery, terminal boarding, payment readiness, or financial-outcome proof. [[adyen]] [[adyen-terminal-management]]

## Key takeaways

- Required string `merchantId` identifies the merchant account, as stated by the endpoint purpose; its path table leaves the description blank. Optional query parameters are integer `limit` and `offset`, case-insensitive `status` (Placed, Confirmed, Cancelled, Shipped, Delivered), and `customerOrderReference`. No limit/offset bounds or defaults are given (raw lines 5–7, 20–34).
- HTTP 200 has an optional `data` array of terminal-package and part orders. Each order's `id`, purchase-order reference, UTC `orderDate`, processing `status`, carrier `trackingUrl`, `items`, `billingEntity`, and `shippingLocation` are schema-marked optional; product, billing, shipping and order IDs are distinct references (raw lines 38–65).
- The reference also lists HTTP 204 with no additional content; that response provides no order readback. The illustrative 200 example has Placed and Cancelled rows with example billing and shipping identities, not evidence for an actual merchant (raw lines 68–69, 171–270).
- The reference lists 400, 401, 403, 422, and 500 error schemas; it gives no order mutation, idempotency, reversal, or delivery-confirmation contract for this GET (raw lines 72–169).

## Detail locators

- Purpose, required caller role, Live rate-limit qualification, and TEST server: raw lines 5–18.
- Path and query parameters: raw lines 20–34; complete 200 order schema: lines 38–65.
- 204 and error schemas: raw lines 68–169; illustrative 200 response: lines 171–270.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/terminalOrders/2026-11-05|Management API merchant terminal-order list, captured 2026-11-05]]
