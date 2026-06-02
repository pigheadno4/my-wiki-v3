---
title: "Stripe: Migrate to the Payment Element with Checkout Sessions API"
type: source
date_ingested: 2026-04-21
original_format: webpage
raw_files:
  - "stripe-payment-element-migration-ewcs-2025.md"
tags: [stripe, payment-element, checkout-sessions, migration, card-element, payment-intents, setup-intents, initCheckoutElementsSdk, actions-confirm]
---

## Summary

Migration guide from Card Element + Payment Intents to Payment Element + Checkout Sessions — the recommended path that adds tax, shipping, discounts, and currency conversion. Covers both one-time payment (PaymentIntent → Checkout Session) and future payment (SetupIntent → Checkout Session with `mode: 'setup'`) paths.

## Key Takeaways

- **Recommended migration path**: Payment Intents + Card Element → Checkout Sessions + Payment Element
- **Gains vs staying on Payment Intents**: tax, shipping, discounts, Adaptive Pricing, subscriptions, currency conversion — all built-in with Checkout Sessions
- **Two migration paths**: One-time (`mode: 'payment'`) and Future payments (`mode: 'setup'`)
- **New required step**: collect customer email (`updateEmail` or `customer_email` at session create)
- **Save PM**: `saved_payment_method_options.payment_method_save: 'enabled'` + `savePaymentMethod: true` on confirm

## Server Migration

### One-time payments (PaymentIntent → Checkout Session)

```javascript
// Before
stripe.paymentIntents.create({ amount: 1099, currency: 'usd' })

// After
stripe.checkout.sessions.create({
  line_items: [{ price_data: { currency: 'usd', product_data: { name: 'T-shirt' }, unit_amount: 1099 }, quantity: 1 }],
  mode: 'payment',
  ui_mode: 'elements',
  return_url: '{{RETURN_URL}}',
})
// → return session.client_secret
```

### Future payments (SetupIntent → Checkout Session)

```javascript
// Before
stripe.setupIntents.create()

// After
stripe.checkout.sessions.create({
  mode: 'setup',
  ui_mode: 'elements',
  return_url: '{{RETURN_URL}}',
  currency: 'usd',  // required when payment_method_types not set
})
```

## Client Migration

### HTML (vanilla)

```javascript
// Before: stripe.elements()
// After:
const checkout = stripe.initCheckoutElementsSdk({ clientSecret });
const loadActionsResult = await checkout.loadActions();
const { actions } = loadActionsResult;

// Display totals from session
const session = actions.getSession();
// session.total, session.lineItems

// Mount Payment Element
const paymentElement = checkout.createPaymentElement();
paymentElement.mount("#payment-element");

// Collect email
actions.updateEmail(email);

// Confirm
const { error } = await actions.confirm();
```

### React

```jsx
// Before: import { Elements } from "@stripe/react-stripe-js"
// After:
import { CheckoutElementsProvider, useCheckout } from "@stripe/react-stripe-js/checkout";

// Provider
<CheckoutElementsProvider stripe={stripe} options={{ clientSecret }}>
  <CheckoutForm />
</CheckoutElementsProvider>

// In component
const checkoutState = useCheckout();
// checkoutState.type: 'loading' | 'error' | ready
const { checkout } = checkoutState;
// checkout.total, checkout.lineItems
checkout.updateEmail(email);
const { error } = await checkout.confirm({ savePaymentMethod: true });
```

## Key Method Changes

| Before | After |
| --- | --- |
| `stripe.elements()` | `stripe.initCheckoutElementsSdk({ clientSecret })` |
| `Elements` provider | `CheckoutElementsProvider` (`@stripe/react-stripe-js/checkout`) |
| `stripe.confirmCardPayment()` | `actions.confirm()` |
| `stripe.confirmCardSetup()` | `actions.confirm()` |
| `elements.submit()` + `stripe.confirmPayment()` | `actions.confirm()` |

## 12 Checkout Session Options (server)

`mode`, `line_items`, `automatic_tax`, `allow_promotion_codes`, `billing_address_collection`, `payment_method_types`, `phone_number_collection`, `shipping_address_collection`, `shipping_options`, `customer_creation`, `payment_intent_data`, `setup_intent_data`

## Webhook Events

| Event | Action |
| --- | --- |
| `checkout.session.completed` | Fulfill order |
| `checkout.session.async_payment_succeeded` | Fulfill order (delayed PMs) |
| `checkout.session.async_payment_failed` | Offer retry |
| `checkout.session.expired` | Offer new session |

## Related Pages

- [[stripe-elements]] — Stripe Elements concept page
- [[source-stripe-payment-element-migration]] — Migration to Payment Intents path (not recommended)
- [[source-stripe-checkout-elements-quickstart]] — Checkout Elements quickstart

## Raw Sources

- [[stripe-payment-element-migration-ewcs-2025]] — Full migration: one-time + future payment paths, 12 Checkout Session options, email collection, save PM, webhook events, comprehensive test tables
