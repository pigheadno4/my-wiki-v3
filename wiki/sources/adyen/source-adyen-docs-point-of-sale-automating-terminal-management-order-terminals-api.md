---
title: "Adyen Docs: Order terminals with Management API"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/automating-terminal-management/order-terminals-api"
raw_files:
  - "adyen/docs/point-of-sale/automating-terminal-management/order-terminals-api/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-management, management-api, terminal-orders]
---

## Overview

This 2026-09-15 Adyen guide explains how a POS integration uses the Management API to order payment terminals, accessories, and enabled hardware kits for a company or merchant account. It covers product discovery, billing and shipping IDs, order creation, order status, updates, and cancellation. This is terminal procurement and logistics, distinct from Terminal API payment messages and payment refunds. See [[adyen-terminal-management]] and [[adyen]].

## Key takeaways

- The ordering credential needs an API key with the Management API Terminal ordering read or read-and-write role, as appropriate to the operation. Management API order creation is for **live terminals**; a test endpoint request does not create a physical test-terminal order. Test terminals require a sales order in the test Customer Area. Live terminal-order endpoints have rate limits.
- Orders are scoped to a company or merchant account. Discover the account ID, available terminal models, and country-filtered terminal products before using product IDs. Each order identifies a shipping location and normally a billing entity, the legal entity charged for the hardware; Brazil orders do not need `billingEntityId`. A shipping location belongs to the company or merchant account and can be created or retrieved through that scope. Wait a few seconds after creating a new shipping location before using it in an order.
- Terminal hardware is region-specific and will not work outside the country or region for which it was ordered, even with a different power cord. Hardware kits need Adyen enablement and custom packaging setup; return the onboarding form at least three months before go-live. A kit appears with a `KIT-` product ID and cannot share an order with non-kit products.
- Create uses `POST /companies/{companyId}/terminalOrders` or `POST /merchants/{merchantId}/terminalOrders`, with product `items` (`id`, `quantity`), `shippingLocationId`, and `billingEntityId` except for the Brazil case. The guide says to supply `taxId` when shipping and billing entities are in different countries or regions. The response includes order ID and status; examples are illustrative and do not establish current stock, price, or eligibility.
- List or retrieve orders to inspect their status. Only a `Placed` order can be updated or cancelled; an update can change items, shipping location, or billing entity, and changing `items` replaces the entire array. Cancellation uses a separate order endpoint without a body. Order-update platform webhooks, email, and Customer Area provide logistics updates; webhook subscription is optional.

## Detail locators

- Prerequisites, roles, live/test boundary, rate limits, and kit setup: [[raw/adyen/docs/point-of-sale/automating-terminal-management/order-terminals-api/2026-09-15#Requirements|Requirements]].
- Product and account scope, regional compatibility, and kit mixing: [[raw/adyen/docs/point-of-sale/automating-terminal-management/order-terminals-api/2026-09-15#Products and orders|Products and orders]] and [[raw/adyen/docs/point-of-sale/automating-terminal-management/order-terminals-api/2026-09-15#Order hardware kits|Order hardware kits]].
- Account/model/product IDs and country filter: [[raw/adyen/docs/point-of-sale/automating-terminal-management/order-terminals-api/2026-09-15#Get the product ID|Get the product ID]]. Billing entity, Brazil exception, and shipping location creation or lookup: [[raw/adyen/docs/point-of-sale/automating-terminal-management/order-terminals-api/2026-09-15#Get the billing entity ID|Get the billing entity ID]] and [[raw/adyen/docs/point-of-sale/automating-terminal-management/order-terminals-api/2026-09-15#Get the shipping location ID|Get the shipping location ID]].
- Order body, company and merchant endpoints, Brazil exception, cross-border tax ID, and example response: [[raw/adyen/docs/point-of-sale/automating-terminal-management/order-terminals-api/2026-09-15#Create a terminal order|Create a terminal order]].
- Logistics updates and order list or individual retrieval: [[raw/adyen/docs/point-of-sale/automating-terminal-management/order-terminals-api/2026-09-15#Terminal order updates|Terminal order updates]] and [[raw/adyen/docs/point-of-sale/automating-terminal-management/order-terminals-api/2026-09-15#View orders|View orders]]. State-gated mutation and entire-array replacement: [[raw/adyen/docs/point-of-sale/automating-terminal-management/order-terminals-api/2026-09-15#Update an order|Update an order]] and [[raw/adyen/docs/point-of-sale/automating-terminal-management/order-terminals-api/2026-09-15#Cancel an order|Cancel an order]].

## Related

- [[adyen-terminal-management]] — broader terminal administration route.
- [[adyen-terminal-api]] — payment messaging boundary.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/automating-terminal-management/order-terminals-api/2026-09-15|Adyen Order terminals, 2026-09-15 snapshot]]
