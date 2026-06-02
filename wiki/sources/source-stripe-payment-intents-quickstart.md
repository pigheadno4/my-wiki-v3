---
title: "Stripe: Build a Checkout Page with Payment Intents API (Quickstart)"
type: source
date_ingested: 2026-04-21
original_format: notes
raw_files:
  - "stripe-payment-intents-quickstart-2025.md"
tags: [stripe, payment-intents, elements, react, useStripe, useElements, confirmPayment, stripe-tax, off-session]
---

## Summary

Complete quickstart guide for building a checkout page using the Payment Intents API + React Elements. Covers server-side PaymentIntent creation (with Stripe Tax integration), client-side Elements wiring, payment confirmation, return page status handling, email receipts, and saving payment methods for future use.

## Key Takeaways

- **Payment Intents API** — `stripe.paymentIntents.create()` server-side; returns `client_secret`
- **Client package**: `@stripe/react-stripe-js` (NOT the `/checkout` subpackage)
- **`Elements` provider**: wraps routes; receives `clientSecret`, `appearance`, `loader: 'auto'`
- **`useStripe()` + `useElements()` hooks**: access Stripe and Elements in form components
- **`stripe.confirmPayment()`**: confirms payment; redirects for bank auth; immediate error for card declines
- **Return page**: `payment_intent_client_secret` URL param → `stripe.retrievePaymentIntent()` → status map
- **Webhook events**: `payment_intent.succeeded`, `payment_intent.processing`, `payment_intent.payment_failed`

## Integration Architecture

```
Server                           Client
──────                           ──────
POST /create-payment-intent      Elements provider
  stripe.paymentIntents.create()   clientSecret, appearance, loader
  → client_secret                
                                 useStripe() + useElements()
                                 stripe.confirmPayment({
                                   elements,
                                   confirmParams: {
                                     return_url,
                                     receipt_email
                                   }
                                 })

Return page                      
  payment_intent_client_secret   stripe.retrievePaymentIntent(cs)
  → paymentIntent.status           succeeded / processing /
                                   requires_payment_method
```

## Status Map (return page)

| Status | Message |
| --- | --- |
| `succeeded` | Payment succeeded |
| `processing` | Your payment is processing |
| `requires_payment_method` | Payment not successful, please try again |
| default | Something went wrong, please try again |

## Stripe Tax Integration

```js
// 1. Calculate tax
const taxCalculation = await stripe.tax.calculations.create({
  currency: 'usd',
  customer_details: { address: {...}, address_source: 'shipping' },
  line_items: [{ amount, reference }],
});

// 2. Use tax total as PaymentIntent amount
const amount = taxCalculation.amount_total;

// 3. Link to PaymentIntent
stripe.paymentIntents.create({
  amount,
  hooks: { inputs: { tax: { calculation: taxCalculation.id } } },
})
```

## Save Payment Method for Future Use

```js
// On PaymentIntent create
setup_future_usage: 'off_session'

// To charge later
stripe.paymentIntents.create({
  customer: customerId,
  payment_method: paymentMethods.data[0].id,
  off_session: true,
  confirm: true,
})
```

## Vs Checkout Elements (Sessions API)

| | Payment Intents API | Checkout Elements |
| --- | --- | --- |
| Server creates | `PaymentIntent` | `Checkout Session` |
| Client provider | `Elements` (`@stripe/react-stripe-js`) | `CheckoutElementsProvider` (`@stripe/react-stripe-js/checkout`) |
| Client hooks | `useStripe()` + `useElements()` | `useCheckout()` |
| Confirm method | `stripe.confirmPayment()` | `checkout.confirm()` |
| Return page param | `payment_intent_client_secret` | `session_id` |
| Built-in tax/shipping | Manual (Tax API) | Automatic (`automatic_tax`) |
| Effort | Most coding | Low coding |

## Related Pages

- [[source-stripe-elements-advanced-payments]] — Checkout Sessions vs Payment Intents comparison
- [[source-stripe-checkout-elements-quickstart]] — Checkout Elements (Sessions API) quickstart
- [[stripe-checkout]] — Stripe Checkout concept page

## Raw Sources

- [[stripe-payment-intents-quickstart-2025]] — Full Payment Intents quickstart: server setup (Tax API, save future usage), client Elements wiring, confirmPayment, return page status, email receipts, off-session charging
