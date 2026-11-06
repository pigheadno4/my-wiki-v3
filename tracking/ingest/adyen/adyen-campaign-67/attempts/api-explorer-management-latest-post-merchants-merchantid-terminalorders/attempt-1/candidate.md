---
title: "Create a merchant terminal order | Adyen Management API v3"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/terminalOrders"
raw_files:
  - "adyen/api-explorer/Management/latest/post/merchants/(merchantId)/terminalOrders/2026-11-05.md"
tags: [adyen, management-api, terminal-orders, merchant-account]
---

## Overview

`POST /merchants/{merchantId}/terminalOrders` creates an order for payment-terminal products for the merchant account identified by required `merchantId`. The captured Management API server is `https://management-test.adyen.com/v3`; the credential needs **Management API—Terminal ordering read and write**. This merchant-scoped order is distinct from a company-scoped order and from Terminal API payment processing. See [[adyen]] and [[adyen-terminal-management]].

> [!warning] Test and live boundary
> Management API test requests **do not create actual orders for test terminals**; the page directs test-terminal sales orders to Customer Area. Live calls to this endpoint are subject to rate limits, but the pinned page supplies no live server or rate figure. A test response is not proof of an actual order.

## Key takeaways

- The request-body table marks `billingEntityId`, `customerOrderReference`, `items`, `orderType`, `shippingLocationId`, and `taxId` optional; nested item `id`, `installments`, `name`, and `quantity` are also table-optional. For Brazil product orders, `billingEntityId` need not be included. The request example's merchant billing-entity ID and two accessory lines do not make those fields mandatory.
- HTTP 200 reports request success and can return optional order `id`, processing `status`, `orderDate`, item details, billing and shipping entities, customer reference and carrier `trackingUrl`. HTTP 204 is separately documented as successful processing without additional content. No response property is schema-required.
- The example's `status: "Placed"` is a sample value, not a general guarantee. Order creation or status does not establish shipment, delivery, device assignment, boarding or payment readiness.
- 400, 401, 403, 422 and 500 error routes separate request problems, authentication, permission, validation and server processing.

## Detail locators

- Raw lines 5–40: purpose, role, test/live warning, test v3 server, merchant ID and optional request-body schema.
- Raw lines 42–63: illustrative accessory order with merchant-account billing entity.
- Raw lines 66–115: optional 200 order fields and distinct 204 no-content success.
- Raw lines 118–215: 400, 401, 403, 422 and 500 errors and generic response fields.
- Raw lines 217–269: illustrative 200 order with `Placed` status; not shipment or delivery proof.

## Related

- [[adyen-terminal-management]] — terminal fleet and ordering context.
- [[source-adyen-docs-point-of-sale-automating-terminal-management-order-terminals-api]] — separate ordering guide.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/merchants/(merchantId)/terminalOrders/2026-11-05|Create merchant terminal order, captured 2026-11-05]]