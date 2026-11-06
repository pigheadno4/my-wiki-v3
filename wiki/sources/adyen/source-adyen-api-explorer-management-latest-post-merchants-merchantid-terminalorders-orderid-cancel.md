---
title: "Cancel a merchant terminal products order | Adyen Management API v3"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/terminalOrders/(orderId)/cancel"
raw_files:
  - "adyen/api-explorer/Management/latest/post/merchants/(merchantId)/terminalOrders/(orderId)/cancel/2026-11-05.md"
tags: [adyen, management-api, terminal-orders, merchant-accounts, point-of-sale]
---

## Overview

This [[adyen]] Management API `latest` reference, captured 2026-11-05, describes `POST /merchants/{merchantId}/terminalOrders/{orderId}/cancel`: cancel the specified terminal products order under a merchant-account path. Cancellation is possible only while its status is `Placed`, and the POST has no request body. The introduction describes a successful response with full order details and status `Cancelled`; the response section also lists a `204` success with no additional content. The listed server is TEST `https://management-test.adyen.com/v3`. The caller's API credential needs `Management API—Terminal ordering read and write`. Live requests are rate limited, with no numeric limit given here. See [[adyen-terminal-management]] and [[adyen-api-access]].

## Key takeaways

- Both path parameters are required strings: `merchantId` identifies the merchant account and `orderId` the terminal products order. The reference specifies no query parameters, request body, defaults or numeric rate limit. The `Placed` status is a cancellation precondition, not a request field. [Raw: lines 5–26]
- `200` is a documented success response with an order-detail schema. The introduction says the returned order has `Cancelled` status, but the schema marks all top-level fields, including `status`, optional. Optional details include order `id`, customer order reference, items, order date, billing entity, shipping location and carrier tracking URL. Nested address/contact properties are optional within optional parents. The example is illustrative, not a guarantee that each field appears. [Raw: lines 7–9, 28–75, 181–233]
- `204` is separately documented as successful processing without additional content; it supplies no order state readback. Do not infer a `Cancelled` response body from a `204`. [Raw: lines 78–79]
- This is terminal-products-order cancellation, not payment cancellation or a terminal action. Neither success shape proves shipment interception, inventory restoration, refund, device boarding or payment readiness. The capture gives no idempotency, undo/reversal, downstream propagation timing or fulfillment guarantee. [Raw: lines 5–9, 28–79]
- Failures listed are `400` request interpretation, `401` authentication, `403` insufficient permission, `422` validation and `500` server processing, with problem-detail response schemas. [Raw: lines 82–179]

## Detail locators

- Purpose, `Placed` restriction, bodyless POST, role, Live rate-limit notice, TEST server and path IDs: pinned raw lines 5–26.
- `200` optional-field order schema and `204` no-content result: pinned raw lines 28–79.
- Error categories and exact schema requiredness: pinned raw lines 82–179.
- Illustrative `Cancelled` order example: pinned raw lines 181–233.
- This dated `latest` capture does not establish current account eligibility, Live route details, shipment outcome, compliance or financial results.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/merchants/(merchantId)/terminalOrders/(orderId)/cancel/2026-11-05|Management API merchant terminal order cancellation — captured 2026-11-05]]