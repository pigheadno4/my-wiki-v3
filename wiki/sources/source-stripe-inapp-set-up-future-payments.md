---
title: "Set Up Future Payments — Mobile"
type: source
date_ingested: 2026-04-22
original_format: webpage
raw_files:
  - "stripe-inapp-set-up-future-payments-2025.md"
tags: [stripe, mobile, ios, android, react-native, setup-intents, save-payment-method, off-session, ephemeral-key, payment-sheet]
---

## Summary

Mobile guide for saving payment details WITHOUT an initial charge (SetupIntent-based). Covers iOS, Android, and React Native. Key mobile limitation: only specific payment methods are supported.

## Mobile SetupIntent Supported Payment Methods

> Cards, Bancontact, iDEAL, Link, SEPA Direct Debit, Sofort, and US bank accounts only. NOT all payment methods.

## Server Endpoint Pattern

```js
// Create Customer/Account + EphemeralKey (legacy) OR CustomerSession + SetupIntent
const setupIntent = await stripe.setupIntents.create({
  customer: customer.id,
  automatic_payment_methods: { enabled: true },
});

// Return: setupIntent.client_secret, ephemeralKey.secret (OR customerSessionClientSecret), customer.id, publishableKey
```

## Client Init — PaymentSheet with SetupIntent

```swift
// iOS — key difference: setupIntentClientSecret (not paymentIntentClientSecret)
self.paymentSheet = PaymentSheet(
  setupIntentClientSecret: setupIntentClientSecret,
  configuration: configuration
)
```

Same `configuration` object: `merchantDisplayName`, `customer`, `allowsDelayedPaymentMethods`, `returnURL`.

## Off-Session Charging After Setup

```js
// List saved PMs
const pms = await stripe.paymentMethods.list({ customer: id, type: 'card' });

// Charge off-session
await stripe.paymentIntents.create({
  customer: id, payment_method: pm.id,
  off_session: true, confirm: true,
  return_url: 'https://example.com/complete',
});
```

## FlowController Pattern Available

Same FlowController (custom buy button) pattern available for setup flows — initialize with `setupIntentClientSecret` instead of `paymentIntentClientSecret`.

## Ephemeral Key (Legacy) vs CustomerSession

Older iOS examples use `EphemeralKey.secret` instead of `customerSessionClientSecret`. Both work but CustomerSession is preferred for new integrations.

## Related Pages

- [[stripe-saved-payment-methods]] — saved PM concept page
- [[stripe-inapp-payments]] — in-app payments concept page
- [[source-stripe-inapp-save-during-payment]] — save WITH initial payment (mobile)

## Raw Sources

- [[stripe-inapp-set-up-future-payments-2025]] — verbatim mobile setup guide (2521 lines, iOS+Android+RN; 8 images reused)
