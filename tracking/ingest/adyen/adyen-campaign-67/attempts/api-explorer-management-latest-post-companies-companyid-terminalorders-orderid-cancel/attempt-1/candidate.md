---
title: "Cancel a terminal products order | Adyen Management API v3"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/companies/(companyId)/terminalOrders/(orderId)/cancel"
raw_files:
  - "adyen/api-explorer/Management/latest/post/companies/(companyId)/terminalOrders/(orderId)/cancel/2026-11-05.md"
tags: [adyen, management-api, terminal-orders, point-of-sale]
---

## Overview

This [[adyen]] Management API `latest` reference, captured 2026-11-05, describes `POST /companies/{companyId}/terminalOrders/{orderId}/cancel`: cancel the specified terminal products order. Cancellation is possible only while its status is `Placed`; make the POST without a request body. On success, the response returns the order details with status `Cancelled`. The listed server is TEST `https://management-test.adyen.com/v3`. The caller's API credential needs `Management API—Terminal ordering read and write`. Live requests to this endpoint are subject to rate limits, but this capture gives no numeric limit. See [[adyen-terminal-management]] for fleet administration and [[adyen-api-access]] for credential scope.

## Key takeaways

- Both path parameters are required strings: `companyId` identifies the company account and `orderId` the terminal products order. The reference specifies no query parameters, request body, defaults or numeric limits. The `Placed` status is a precondition, not a request field. [Raw: lines 5–26]
- `200` is the documented success status. The introduction says the full order details return with `Cancelled` status, while the response table marks every top-level field, including `status`, optional. Read the actual response rather than assuming every illustrative field is always present. Optional details include order `id`, customer order reference, items, order date, billing entity, shipping location and carrier tracking URL. Optional nested objects contain optional fields such as billing/shipping IDs, addresses and contact information. [Raw: lines 7–9, 28–75]
- This cancels a terminal-products order, not a payment or device action. The returned `Cancelled` order state does not prove shipment interception, inventory restoration, refund, reversal of a payment, device boarding or payment readiness. The capture does not state cancellation timing beyond the `Placed` precondition, idempotency, a reversal path, or downstream propagation. [Raw: lines 5–9, 30–75]
- The reference lists `400` request interpretation, `401` authentication, `403` permission, `422` validation and `500` server failures. Error response schemas use problem-detail fields; see raw for requiredness. [Raw: lines 78–175]

> [!warning] Contradiction
> The response schema describes both billing and shipping address `country` as a two-letter ISO 3166-1 alpha-2 code, but the `200` example uses `"Netherlands"` in both addresses. Treat those country values as illustrative sample data, not a validated code format. [Raw: lines 40, 61, 200, 212]

## Detail locators

- Purpose, `Placed` restriction, bodyless POST, role, Live rate-limit notice, TEST server and path IDs: pinned raw lines 5–26.
- `200` order response and optional-field schema: pinned raw lines 28–75.
- Failure categories and schemas: pinned raw lines 78–175.
- Illustrative `Cancelled` order example and country-format conflict: pinned raw lines 177–228.
- The `latest` label and dated TEST capture do not establish current account eligibility, Live route details, actual fulfillment outcome, compliance or payment execution.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/companies/(companyId)/terminalOrders/(orderId)/cancel/2026-11-05|Management API terminal order cancellation — captured 2026-11-05]]