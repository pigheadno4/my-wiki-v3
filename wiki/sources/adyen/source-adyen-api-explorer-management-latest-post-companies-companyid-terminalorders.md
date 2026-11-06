---
title: "Create a company terminal order | Adyen Management API v3"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/companies/(companyId)/terminalOrders"
raw_files:
  - "adyen/api-explorer/Management/latest/post/companies/(companyId)/terminalOrders/2026-11-05.md"
tags: [adyen, management-api, terminal-orders, company-account]
---

## Overview

`POST /companies/{companyId}/terminalOrders` creates an order for payment-terminal products for the company identified by required path `companyId`. The captured Management API server is `https://management-test.adyen.com/v3`; the caller's credential needs **Management API—Terminal ordering read and write**. This concerns product ordering and logistics, not a Terminal API payment. See [[adyen]] and [[adyen-terminal-management]].

> [!warning] Test and live boundary
> Requests to the Management API test endpoint **do not create actual orders for test terminals**; the page directs test-terminal sales orders to Customer Area. In live, this endpoint is subject to rate limits. The pinned page lists only the test server and does not establish live account eligibility or an actual order from a test response.

## Key takeaways

- The request table marks all body properties optional: `billingEntityId`, merchant-defined `customerOrderReference`, `items` with optional product `id`, `name`, `quantity`, and `installments`, plus `orderType`, `shippingLocationId`, and `taxId`. The page says a Brazil product order need not include `billingEntityId`. The illustrated request is one example, not a schema-required field set.
- HTTP 200 reports request success and can return optional order `id`, `status`, `orderDate`, `items`, billing entity, shipping location, customer reference and carrier `trackingUrl`. The schema does not mark any response property required.
- The example's `status: "Placed"` is sample data. Neither it nor optional `trackingUrl` establishes shipment, delivery, device assignment, boarding or payment readiness.
- Error routes are 400, 401, 403, 422 and 500. Authentication and role permission are separate from request validation and server processing.

## Detail locators

- Raw lines 5–40: purpose, credential role, test/live qualification, server, company identifier and complete request schema.
- Raw lines 42–63: illustrative product-order request.
- Raw lines 66–111: 200 response schema, including optional order identity, status, billing/shipping details and tracking URL.
- Raw lines 114–211: 400, 401, 403, 422 and 500 errors and their generic response fields.
- Raw lines 213–264: illustrative 200 order with `Placed` status; values are examples, not delivery proof.

## Related

- [[adyen-terminal-management]] — fleet management and ordering context.
- [[source-adyen-docs-point-of-sale-automating-terminal-management-order-terminals-api]] — separate ordering guide.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/companies/(companyId)/terminalOrders/2026-11-05|Create company terminal order, captured 2026-11-05]]