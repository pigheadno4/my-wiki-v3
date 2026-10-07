---
title: "Braintree PayPal Commerce Channel API — Receiving Order Updates"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/paypal-commerce-channel-api/receiving-order-updates"
raw_files:
  - "braintree/docs/guides/paypal-commerce-channel-api/receiving-order-updates-2026-09-16.md"
tags: [braintree, paypal-commerce-channel-api, order-updates, retailer, webhooks]
---

## Overview

This collected, unversioned Braintree website guide describes a PayPal Commerce Channel API webhook sent after Braintree receives a retailer ecommerce-system update that a channel-initiated purchase was fulfilled. The message goes to the same destination URL used for Channel API retailer onboarding and offboarding messages and is intended to let the channel show updated order information to users. The 2026-09-16 snapshot does not establish current API availability, channel or retailer eligibility, endpoint setup, webhook delivery, fulfillment of a particular order, or payment authorization, capture, settlement, or funding. See [[braintree]], the provider route [[braintree-payment-platform]], and the dedicated notification route [[braintree-webhooks]].

## Key takeaways

- The documented trigger is Braintree receiving an order update from the retailer's ecommerce system; the material example condition is the retailer fulfilling a channel-initiated purchase. Braintree then sends an order-update webhook to the Channel API destination also used for retailer onboarding and offboarding messages.
- The example HTTP message uses `topic: order`, `action: update`, and an `order` object containing `partner_order_id` and `status: fulfilled`. It is an illustrative payload, not an exhaustive schema or a guarantee that those are the only fields or statuses.
- The page says delivery is attempted immediately after Braintree receives retailer confirmation that the order was fulfilled. That timing statement is an attempt condition, not a delivery-time guarantee or evidence that a webhook was received.
- For retry and failure handling, this page expressly delegates to the Channel API retailer-message guide. That fully read guide requires HTTP 200 in under 10 seconds to avoid redelivery and otherwise describes several redelivery attempts over the next 12 hours with increasing delay. These product-specific rules do not import the generic Braintree Node webhook guide's signature, parsing, acknowledgement, environment, cadence, ordering, or duplicate-delivery semantics. [[source-braintree-docs-guides-paypal-commerce-channel-api-keeping-track-of-retailers]]
- This order-update webhook reports retailer fulfillment state to the channel; it does not by itself prove payment approval, capture, settlement, funding, shipment, delivery, or successful user display.

## Detail locators

- **Purpose, retailer ecommerce-system update, destination reuse, and user-information purpose:** `Receiving Order Updates` (raw lines 14–18).
- **Channel-initiated fulfillment condition:** raw lines 18–19.
- **Illustrative HTTP request and order-update payload:** raw lines 20–34.
- **Immediate-attempt condition after retailer fulfillment confirmation:** raw lines 35–36.
- **Delegation of retry and failure handling to the retailer-message guide:** raw lines 36–37; exact Channel API acknowledgement and redelivery conditions are in [[source-braintree-docs-guides-paypal-commerce-channel-api-keeping-track-of-retailers]].

## Related

- [[braintree]]
- [[braintree-payment-platform]]
- [[braintree-webhooks]] — dedicated notification route; keep this Channel API order-update contract distinct from generic gateway webhook guidance
- [[source-braintree-docs-guides-paypal-commerce-channel-api-keeping-track-of-retailers]] — fully read authority for the acknowledgement and redelivery behavior incorporated by this page's explicit retry/failure reference

## Raw Sources

- [[raw/braintree/docs/guides/paypal-commerce-channel-api/receiving-order-updates-2026-09-16|Braintree PayPal Commerce Channel API — Receiving Order Updates (2026-09-16 snapshot)]]
