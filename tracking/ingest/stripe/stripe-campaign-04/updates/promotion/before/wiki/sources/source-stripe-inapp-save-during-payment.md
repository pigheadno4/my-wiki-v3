---
title: "Save Payment Details During an In-App Payment"
type: source
date_ingested: 2026-04-22
original_format: webpage
raw_files:
  - "stripe-inapp-save-during-payment-2025.md"
tags: [stripe, mobile, ios, android, react-native, save-payment-method, setup-future-usage, off-session, customer-session, mobile-payment-element]
---

## Summary

Mobile-specific guide for saving payment methods during payment across iOS, Android, and React Native. Uses `setup_future_usage` on PaymentIntent + `mobile_payment_element` CustomerSession component.

## Key Mobile Limitation

> `setup_future_usage` on mobile only supports **cards and US bank accounts** — not all payment methods.

## Server Endpoint Pattern

```js
// Create Account/Customer + CustomerSession + PaymentIntent
const customerSession = await stripe.customerSessions.create({
  customer: customer.id, // or customer_account
  components: {
    mobile_payment_element: {  // NOTE: mobile_payment_element, not payment_element
      enabled: true,
      features: {
        payment_method_save: 'enabled',
        payment_method_redisplay: 'enabled',
        payment_method_remove: 'enabled',
      },
    },
  },
});

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099, currency: 'eur',
  customer: customer.id,
  setup_future_usage: 'off_session',
  automatic_payment_methods: { enabled: true },
});

// Return: paymentIntent.client_secret, customerSession.client_secret, customer.id, publishableKey
```

## iOS Client Setup

```swift
@_spi(CustomerSessionBetaAccess) import StripePaymentSheet

var configuration = PaymentSheet.Configuration()
configuration.merchantDisplayName = "Example, Inc."
configuration.customer = .init(id: customerId, customerSessionClientSecret: customerSessionClientSecret)
configuration.allowsDelayedPaymentMethods = true  // opt in for ACH, SEPA, etc.
configuration.returnURL = "your-app://stripe-redirect"

self.paymentSheet = PaymentSheet(paymentIntentClientSecret: paymentIntentClientSecret, configuration: configuration)
```

**SwiftUI**: use `PaymentSheet.PaymentButton` component with `onCompletion` handler.

## Off-Session Charging (After Save)

```js
// List saved PMs
const paymentMethods = await stripe.paymentMethods.list({
  customer: customerId, type: 'card'
});

// Charge off-session
await stripe.paymentIntents.create({
  customer: customerId,
  payment_method: pmId,
  off_session: true, confirm: true,
  return_url: 'https://example.com/complete',
});
```

## `allowsDelayedPaymentMethods`

Opt in to delayed notification PMs (ACH, SEPA, OXXO, Konbini):
- PaymentSheet returns `.completed` immediately when customer selects these
- Final status arrives later via `payment_intent.succeeded` webhook
- Don't fulfill order until webhook fires — only show "order confirmed" message

## Related Pages

- [[stripe-saved-payment-methods]] — saved PM concept page
- [[stripe-inapp-payments]] — in-app payments concept page
- [[source-stripe-inapp-finalize-payments-server]] — full server confirmation guide

## Raw Sources

- [[stripe-inapp-save-during-payment-2025]] — verbatim mobile save-during-payment guide (2918 lines, iOS+Android+RN)
