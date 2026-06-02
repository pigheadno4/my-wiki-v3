---
title: "Stripe Checkout: Charge for Shipping"
type: source
date_ingested: 2026-04-20
original_format: webpage
raw_files:
  - "stripe-checkout-charge-shipping-2025.md"
tags: [stripe, checkout, shipping, shipping-rates, delivery-estimate, tax, checkout-sessions]
---

## Summary

How to create shipping rates and charge customers for shipping in Stripe Checkout. Covers the ShippingRate API, inline `shipping_rate_data`, delivery estimates, shipping tax, and post-payment fulfillment — for both hosted and embedded Checkout modes.

## Key Takeaways

- **ShippingRate API**: `stripe.shippingRates.create()` with `type: 'fixed_amount'`, `display_name`, `fixed_amount`, and optional `delivery_estimate`
- **Fixed amount only**: shipping rates apply to the entire order — cannot adjust per item count
- **Immutable amounts**: once a currency+amount is set on a shipping rate, it cannot be updated — must archive and create a new one
- **2 ways to attach**: pre-created shipping rate ID, or inline `shipping_rate_data` within `shipping_options` on the Checkout Session
- **Payment mode only**: `shipping_options` only supported in `mode: 'payment'` Checkout Sessions
- **Pre-selection**: first option in `shipping_options` array is pre-selected for the customer
- **Dynamic shipping rates** (preview): can update rates based on customer address or order value via `custom-shipping-options`

## Delivery Estimate

Configurable via `delivery_estimate.minimum` and `delivery_estimate.maximum` with `unit` (`hour`, `day`, `business_day`) and `value`. Examples:
- "1 business day" → min & max both `{ unit: 'business_day', value: 1 }`
- "At least 2 business days" → min `{ unit: 'business_day', value: 2 }`, max `null`
- "3 to 7 days" → min `{ unit: 'day', value: 3 }`, max `{ unit: 'day', value: 7 }`
- Mixed units supported: "4 hours to 2 business days"

## Shipping Tax

- Set `tax_code` and `tax_behavior` on the shipping rate to enable Stripe Tax for shipping
- Recommended: `tax_code: 'txcd_92010001'` (Shipping) — Stripe determines taxability per state/country
- Use `txcd_00000000` (Nontaxable) to explicitly skip shipping tax
- `tax_behavior: 'exclusive'` is common in the US
- Requires `automatic_tax: { enabled: true }` on the Checkout Session

## Post-Payment Fulfillment

- Shipping amount available at `shipping_cost.amount_total` on the Checkout Session
- Selected shipping rate ID at `shipping_cost.shipping_rate`
- Access via `checkout.session.completed` webhook handler

## Related Pages

- [[stripe-checkout]] — Stripe Checkout concept page
- [[source-stripe-checkout-collect-addresses-2025]] — Collect billing and shipping addresses (prerequisite)
- [[source-stripe-how-checkout-works]] — How Checkout works: features, lifecycle, address collection
- [[source-stripe-checkout-custom-shipping-options]] — Dynamic shipping: address-based rate calculation, onShippingDetailsChange callback, embedded only

## Raw Sources

- [[stripe-checkout-charge-shipping-2025]] — Charge for shipping: ShippingRate API, shipping_options, delivery estimates, shipping tax (txcd_92010001), post-payment fulfillment, hosted + embedded modes (3 CDN images)
