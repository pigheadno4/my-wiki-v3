---
title: "Charge for Shipping"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/advanced/charge-shipping"
raw_files:
  - "stripe-charge-shipping-2025.md"
tags: [stripe, shipping, shipping-rates, checkout-sessions, payment-intents, stripe-tax, elements]
---

## Summary

The 2026-04-21 guide covers two distinct API paths. Its Checkout Sessions embedded-components variant uses the `ShippingRate` API and Session `shipping_options`; its Payment Intents elements variant has no built-in shipping-rate calculation or definition, so it describes calculating the shipping-inclusive total yourself or using Checkout. The 2026-11-07 capture at this URL is a variant index only.

> See also [[source-stripe-checkout-shipping]] for deeper Checkout Sessions shipping coverage.

## Payment Intents: No Built-In Shipping-Rate Calculation

The older Payment Intents variant says the API does not calculate or define shipping rates out of the box. Stripe presents two options:

1. Build it yourself: add shipping cost to the product total, display in checkout UI, process as a single amount
2. Use Checkout Sessions for its built-in shipping-rate features

## Checkout Sessions: Key Facts

- **Fixed-rate example** — the older guide's ShippingRate values are fixed for the entire order and do not scale with item count; its separate dynamic shipping-update route was explicitly a preview feature
- **`shipping_options` in the dated guide** — supported on Checkout Sessions in payment mode, not subscription or setup modes
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

## 2026-11-07 Variant Index

The later base-URL capture links Checkout Sessions (`payment-ui=embedded-components`) and Payment Intents (`payment-ui=elements`) variants. It does not include either body; their current detailed behavior and eligibility are unverified here. The difference from the older combined capture is a navigation change, not evidence that either path was removed.

## Related raw API references

- [[raw/stripe-payments-advanced-charge-shipping-2026-11-07|2026-11-07 variant index]] — navigation to the two API-specific pages only.

## Related Pages

- [[source-stripe-checkout-shipping]] — deeper shipping coverage for Checkout Sessions
- [[source-stripe-checkout-dynamic-shipping]] — dynamic server-side shipping (beta): address validation, region-based options, runServerUpdate pattern
- [[stripe-checkout]] — Checkout concept page
- [[stripe-payment-intents]] — Payment Intents (no built-in shipping-rate calculation or definition)

## Raw Sources

- [[raw/stripe-charge-shipping-2025|2026-04-21 combined guide]] — verbatim Checkout Sessions and Payment Intents variants
