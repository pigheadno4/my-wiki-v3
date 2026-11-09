---
title: "Charge for Shipping"
type: source
date_ingested: 2026-04-21
original_format: webpage
raw_files:
  - "stripe-charge-shipping-2025.md"
tags: [stripe, shipping, shipping-rates, checkout-sessions, payment-intents, stripe-tax, elements]
---

## Summary

Shipping rate integration guide for both API paths. Checkout Sessions has full built-in support via the `ShippingRate` API. Payment Intents has **no native shipping rate support** — must be built manually or by switching to Checkout.

> See also [[source-stripe-checkout-shipping]] for deeper Checkout Sessions shipping coverage.

## Payment Intents: No Native Shipping Support

The Payment Intents API does not support shipping rates. Options:

1. Build it yourself: add shipping cost to the product total, display in checkout UI, process as a single amount
2. Switch to Checkout Sessions (recommended)

## Checkout Sessions: Key Facts

- **Fixed amount only** — cannot vary by item count
- **payment mode only** — not supported in subscription or setup modes
- **Shipping rate IDs**: `shr_...`; created via API or Dashboard
- **Cannot update amount** of a set currency — must archive + create new rate
- Pass rates via `shipping_options[].shipping_rate` (pre-created ID) or `shipping_options[].shipping_rate_data` (inline)

## Client-Side Shipping Option Selection (Elements Path)

```js
// Get shipping options from session
const options = actions.getSession().shippingOptions;

// When customer selects
actions.updateShippingOption(option.id);
```

React: use `useCheckout()` → `{ shippingOptions, updateShippingOption, shipping }` from `checkoutState.checkout`.

## Post-Payment: Retrieve Shipping Cost

```js
// In checkout.session.completed webhook handler
const selectedRate = await stripe.shippingRates.retrieve(session.shipping_cost.shipping_rate);
const shippingTotal = session.shipping_cost.amount_total;
```

## Delivery Estimate Units

`hour`, `day`, `business_day` — can mix min/max of different units. Set `maximum: null` for "at least N" open-ended estimates.

## Shipping Tax

```js
shipping_rate_data: {
  tax_behavior: 'exclusive',
  tax_code: 'txcd_92010001', // Shipping tax code
}
// With automatic_tax: { enabled: true } on the session
```

Use `txcd_00000000` (Nontaxable) to explicitly exclude shipping from tax.

## Related Pages

- [[source-stripe-checkout-shipping]] — deeper shipping coverage for Checkout Sessions
- [[source-stripe-checkout-dynamic-shipping]] — dynamic server-side shipping (beta): address validation, region-based options, runServerUpdate pattern
- [[stripe-checkout]] — Checkout concept page
- [[stripe-payment-intents]] — Payment Intents (no shipping support)

## Raw Sources

- [[stripe-charge-shipping-2025]] — verbatim guide (both API paths)
