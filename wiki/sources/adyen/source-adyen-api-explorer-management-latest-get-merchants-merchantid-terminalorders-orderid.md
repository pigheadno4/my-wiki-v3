---
title: "Adyen Management API: Get a merchant terminal order"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/terminalOrders/(orderId)"
raw_files:
  - "adyen/api-explorer/Management/latest/get/merchants/(merchantId)/terminalOrders/(orderId)/2026-11-05.md"
tags: [adyen, management-api, terminal-orders, point-of-sale]
---

## Overview

This [[adyen]] Management API `latest` reference, captured 2026-11-05, documents `GET /merchants/{merchantId}/terminalOrders/{orderId}` to read a terminal-products order under a merchant account. It lists `https://management-test.adyen.com/v3` as its server and says Live requests are rate-limited without stating the numeric limit.

## Key takeaways

- The API credential needs either **Management API—Terminal ordering read** or **Management API—Terminal ordering read and write**. Required path IDs are `merchantId`, the merchant-account identifier, and `orderId`, the order identifier. This read reference lists no query/body parameters, defaults, or idempotency behavior.
- A 200 means the request succeeded and can return an order body. Its top-level schema marks `billingEntity`, `customerOrderReference`, `id`, `items`, `orderDate`, `shippingLocation`, `status`, and `trackingUrl` optional. Billing and shipping IDs, when present, are reusable as `billingEntityId` and `shippingLocationId` when creating an order; item details and nested address/contact fields are in the raw table.
- A 204 is also documented as successful processing but **has no additional content**; do not infer a returned order body for that response. The 200 example's `Placed` value does not define the status enum. The schema describes `status` only as order processing status, and `trackingUrl` as an optional carrier-provided URL.
- This GET readback does not place an order or prove shipment, delivery, device boarding, activation, payment capability, or financial outcome. Documented errors are 400, 401, 403, 422 and 500.

## Detail locators

- Purpose, roles, Live rate-limit statement and captured Test server: opening text and `## Servers`, lines 5-18.
- Merchant-account and order path identities: `## Parameters`, lines 20-26.
- 200 response schema, nested billing/shipping/item data, processing status and tracking URL: `### 200 Success`, lines 28-75.
- No-content success: `### 204 Success`, lines 78-79.
- Error meanings and problem bodies: `### 400 Client Error` (82-99), `### 401 Client Error` (102-119), `### 403 Client Error` (122-139), `### 422 Client Error` (142-159), `### 500 Server Error` (162-179).
- Illustrative `Placed` order: `## Response examples`, lines 181-234.

## Related

- Company: [[adyen]]
- Concept: [[adyen-terminal-management]]

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/terminalOrders/(orderId)/2026-11-05|Adyen Management API — Get merchant terminal order (2026-11-05)]]
