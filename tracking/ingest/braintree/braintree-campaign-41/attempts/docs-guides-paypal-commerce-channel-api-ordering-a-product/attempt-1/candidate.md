---
title: "Braintree PayPal Commerce Channel API — Ordering a Product"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/paypal-commerce-channel-api/ordering-a-product"
raw_files:
  - "braintree/docs/guides/paypal-commerce-channel-api/ordering-a-product-2026-09-16.md"
tags: [braintree, paypal-commerce-channel-api, product-ordering, retailer, checkout]
---

## Overview

This collected, unversioned Braintree website guide describes how a channel initiates a purchase of a retailer's product variant for a user through the PayPal Commerce Channel API. The captured page uses sandbox endpoints in its examples and does not establish current API availability, merchant or channel eligibility, production enablement, or an exact SDK or API version. See [[braintree]] and the provider-level route [[braintree-payment-platform]].

## Key takeaways

- The documented flow obtains a Braintree SDK `payment_method_token`, a shipping address, and the full cost before creating the order with a customer access token and initiating the purchase. The shipping address supports retailer delivery plus tax and shipping calculation; exact fields and requiredness are routed to the raw locator.
- Before order creation, the guide strongly recommends querying the single-variant endpoint with destination data and presenting the full cost, warning that omission can cause confusion, chargebacks, and a poor user experience. That response can indicate shippability, taxes, shipping costs, and promotion results; the snapshot documents 404 responses for unsupported promo codes and unknown SKUs.
- Order creation first requires a customer access token for the particular user. The guide says that token is specific to the channel and retailer, is obtained using a unique customer ID, and has a returned validity duration; its sample request targets the sandbox Channel API.
- To initiate the purchase, the request body contains an `order` with a partner order ID, variant, shipping address, vaulted payment-method token, and optional promo codes. The captured success path returns HTTP 201 with order cost data, then says the system transmits the order to the retailer's ecommerce system to be marked ready to fulfill. An order request, HTTP 201 response, transmission, or `ready to fulfill` state is not evidence here of separate merchant approval, completed fulfillment, payment settlement, or funding.
- The page states that purchasing-process failures return a 400–499 code and routes readers to separate error-handling guidance; this snapshot does not enumerate those error semantics.

## Detail locators

- **Flow and payment token:** `Ordering a Product` and `Obtaining and storing payment information` (raw lines 14–27).
- **Shipping schema:** `Obtaining a shipping address` (raw lines 28–42) lists optional and required address components.
- **Cost preview and response conditions:** `Obtaining the full cost` (raw lines 45–65); sandbox request and response examples plus unknown-SKU example (raw lines 66–147).
- **Customer-scoped authorization:** `Creating an order` and `Obtaining a customer access token` (raw lines 149–182), including channel-and-retailer scope, `customer_id`, sandbox token request, expiry, and caching guidance.
- **Order request schema:** `Initiating the purchase` (raw lines 183–223), including the sandbox `/channel/orders` example.
- **Documented response and handoff state:** raw lines 224–248, including HTTP 201 cost data, the 400–499 warning, retailer-system transmission, and `ready to fulfill` wording.

## Related

- [[braintree]]
- [[braintree-payment-platform]]

## Raw Sources

- [[raw/braintree/docs/guides/paypal-commerce-channel-api/ordering-a-product-2026-09-16|Braintree PayPal Commerce Channel API — Ordering a Product (2026-09-16 snapshot)]]
