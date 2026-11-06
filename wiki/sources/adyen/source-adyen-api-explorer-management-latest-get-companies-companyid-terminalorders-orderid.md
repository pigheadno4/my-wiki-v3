---
title: "Adyen Management API: Get a company terminal order"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/terminalOrders/(orderId)"
raw_files:
  - "adyen/api-explorer/Management/latest/get/companies/(companyId)/terminalOrders/(orderId)/2026-11-05.md"
tags: [adyen, management-api, terminal-orders, point-of-sale]
---

## Overview

This [[adyen]] Management API `latest` reference, captured 2026-11-05, documents `GET /companies/{companyId}/terminalOrders/{orderId}` to read details of one terminal-products order. It lists `https://management-test.adyen.com/v3` as its server and notes Live rate limits without stating a numeric value.

## Key takeaways

- The caller's API credential needs either **Management API—Terminal ordering read** or **Management API—Terminal ordering read and write**. Both path parameters are required: `companyId` identifies the company account and `orderId` identifies the order. No query/body fields, defaults, or idempotency behavior are specified for this read operation.
- A 200 means the read request succeeded. Its response schema marks all listed top-level fields optional: `id`, `customerOrderReference`, `orderDate`, `status`, `trackingUrl`, `items`, `billingEntity`, and `shippingLocation`. `billingEntity.id` and `shippingLocation.id`, when present, are the IDs used as `billingEntityId` and `shippingLocationId` when creating an order. Item rows can include product ID, name, quantity, and installments; shipping contact and address fields are in the raw table.
- The response describes `status` only as the order's processing status and `trackingUrl` only as a carrier-provided shipment-tracking URL. The example shows `Placed` and no tracking URL; it does not define the full status enum or prove shipment, delivery, terminal boarding, activation, or payment capability.
- Error responses cover 400, 401, 403, 422, and 500. This readback neither creates an order nor establishes stock, order fulfillment, device state, merchant eligibility, or financial settlement.

## Detail locators

- Purpose, credential roles, Live rate-limit qualification and captured Test server: opening text and `## Servers`, lines 5-18.
- Required company and order path IDs: `## Parameters`, lines 20-26.
- 200 response and optional billing, item, shipping, status and tracking fields: `### 200 Success`, lines 28-75.
- Error meanings and problem-body fields: `### 400 Client Error` (lines 78-95), `### 401 Client Error` (98-115), `### 403 Client Error` (118-135), `### 422 Client Error` (138-155), and `### 500 Server Error` (158-175).
- Illustrative placed-order response: `## Response examples`, lines 177-229.

## Related

- Company: [[adyen]]
- Concept: [[adyen-terminal-management]]

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/terminalOrders/(orderId)/2026-11-05|Adyen Management API — Get terminal order (2026-11-05)]]
