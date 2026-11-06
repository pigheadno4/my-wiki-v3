---
title: "Adyen Management API v3: list company terminal orders"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/terminalOrders"
raw_files:
  - "adyen/api-explorer/Management/latest/get/companies/(companyId)/terminalOrders/2026-11-05.md"
tags: [adyen, management-api, terminal-orders, company-accounts]
---

## Overview

This 2026-11-05-captured Management API reference documents `GET /companies/{companyId}/terminalOrders`, a filtered list of terminal-product orders for the path-identified company account. The caller needs either `Management API—Terminal ordering read` or `Management API—Terminal ordering read and write`. The only listed server is TEST `https://management-test.adyen.com/v3`; the page notes Live rate limits without giving a numeric value. An order-list readback is not proof of delivery, terminal boarding, payment readiness, or a financial outcome. [[adyen]] [[adyen-terminal-management]]

## Key takeaways

- Required string `companyId` identifies the company account. Optional query filters are integer `limit` (orders to return), integer `offset` (orders to skip), case-insensitive `status` with Placed, Confirmed, Cancelled, Shipped, or Delivered values, and `customerOrderReference` (merchant purchase-order number). No bounds or defaults are specified for limit/offset (raw lines 21–35).
- HTTP 200 returns an optional `data` array of terminal-package and part orders. Each order can include `id`, `customerOrderReference`, `orderDate`, processing `status`, carrier `trackingUrl`, product `items`, `billingEntity`, and `shippingLocation`; all are schema-marked optional. Billing entity, shipping location, product and order IDs are distinct references (raw lines 39–66).
- The example contains one Placed and one Cancelled order with illustrative addresses, products and quantities; it does not establish shipping or billing status for a real order (raw lines 168–260).
- The reference lists 400, 401, 403, 422 and 500 error schemas. It does not document an idempotency, mutation, reversal, or delivery-confirmation contract for this GET (raw lines 69–166).

## Detail locators

- Purpose, caller roles, Live rate-limit qualification and TEST server: raw lines 5–19.
- Path and query fields: raw lines 21–35; complete 200 order schema: lines 39–66.
- Error schemas: raw lines 69–166; illustrative 200 response: lines 168–260.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/terminalOrders/2026-11-05|Management API company terminal-order list, captured 2026-11-05]]
