---
title: "Stripe Checkout Elements: Build a Checkout Page (Quickstart)"
type: source
date_ingested: 2026-04-21
original_format: notes
raw_files:
  - "stripe-checkout-elements-quickstart-2025.md"
tags: [stripe, checkout, elements, checkout-elements, react, useCheckout, CheckoutElementsProvider, adaptive-pricing, payment-element]
---

## Summary

Complete quickstart guide for building a checkout page using Stripe's Checkout Elements integration (`ui_mode: 'elements'`): Checkout Sessions API on the server + React Elements client. Covers full server setup, client wiring, payment confirmation, return page handling, and optional features (Stripe Tax, Adaptive Pricing, address collection).

## Key Takeaways

- **`ui_mode: 'elements'`** on session create — activates Checkout Elements path
- **Client package**: `@stripe/react-stripe-js/checkout` (separate from `@stripe/react-stripe-js`)
- **`CheckoutElementsProvider`**: wraps routes; receives `clientSecret`, `elementsOptions`, `adaptivePricing`
- **`useCheckout()` hook**: central hook; returns `checkoutState.type` (`loading`/`error`/ready) + `checkout` object
- **`checkout.confirm()`**: completes payment; `checkout.canConfirm`: boolean for gating submit button
- **`checkout.total.total.amount`**: live total for display (handles Adaptive Pricing conversions)
- **Return page**: poll `/session-status` → `session.status` = `complete` (success) or `open` (remount)
- **Adaptive Pricing**: `adaptivePricing: { allowed: true }` in provider + `CurrencySelectorElement`

## Integration Architecture

```
Server                           Client
──────                           ──────
POST /create-checkout-session    CheckoutElementsProvider
  → stripe.checkout.sessions       clientSecret (Promise)
    .create({                       adaptivePricing.allowed: true
      ui_mode: 'elements',        
      return_url: '...{CHECKOUT_SESSION_ID}',
      automatic_tax: {enabled:true},
    })                           useCheckout() hook
  ← { clientSecret }               checkout.confirm()
                                   checkout.canConfirm
GET /session-status              Complete.jsx
  → sessions.retrieve(id,          fetch /session-status
      {expand:['payment_intent']})  status: complete → success
  ← { status, payment_status,       status: open → remount
      payment_intent_id,
      payment_intent_status }
```

## Elements Used

| Element | Purpose |
| --- | --- |
| `PaymentElement` | Main payment form (40+ methods) |
| `BillingAddressElement` | Billing address collection |
| `ShippingAddressElement` | Shipping address collection |
| `CurrencySelectorElement` | Adaptive Pricing currency chooser |

## Key Imports

```js
// All from @stripe/react-stripe-js/checkout (NOT @stripe/react-stripe-js)
import { CheckoutElementsProvider } from "@stripe/react-stripe-js/checkout";
import {
  PaymentElement,
  BillingAddressElement,
  ShippingAddressElement,
  CurrencySelectorElement,
  useCheckout,
} from "@stripe/react-stripe-js/checkout";
```

## Session Status Handling

`/session-status` returns `payment_intent_id` and `payment_intent_status` (via `expand: ['payment_intent']`) in addition to `session.status` and `session.payment_status`.

## Optional Features

| Feature | Server param | Client |
| --- | --- | --- |
| Tax | `automatic_tax: { enabled: true }` | `BillingAddressElement` |
| Billing address | `billing_address_collection: 'auto'` | `BillingAddressElement` |
| Shipping address | `shipping_address_collection.allowed_countries` | `ShippingAddressElement` |
| Adaptive Pricing | Dashboard setting | `adaptivePricing: { allowed: true }` + `CurrencySelectorElement` |
| Prefill email | `customer_email` or `customer` | Remove `updateEmail` if using `customer` |

## Test Cards

| Scenario | Card |
| --- | --- |
| Success | `4242 4242 4242 4242` |
| 3DS required | `4000 0025 0000 3155` |
| Declined | `4000 0000 0000 9995` |

## Related Pages

- [[stripe-checkout]] — Stripe Checkout concept page (Checkout Elements = ui_mode: 'elements')
- [[source-stripe-elements-advanced-payments]] — Checkout Sessions vs Payment Intents comparison for Elements
- [[source-stripe-checkout-sessions]] — Checkout Sessions API deep dive

## Raw Sources

- [[stripe-checkout-elements-quickstart-2025]] — Full Checkout Elements quickstart: server setup, CheckoutElementsProvider, useCheckout hook, all 4 elements, return page, Adaptive Pricing, Stripe Tax, address collection, test cards
