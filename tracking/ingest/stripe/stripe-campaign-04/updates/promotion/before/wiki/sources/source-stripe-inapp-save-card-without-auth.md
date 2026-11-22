---
title: "Save a Card Without Bank Authentication — Mobile"
type: source
date_ingested: 2026-04-23
original_format: webpage
raw_files:
  - "stripe-inapp-save-card-without-auth-2025.md"
tags: [stripe, mobile, ios, android, react-native, save-card, error-on-requires-action, legacy, us-canada, setup-future-usage, cvc-recollection]
---

## Summary

Legacy/simple mobile integration for saving cards and charging later without handling bank authentication. US/Canada only. **Non-compliant in India** and other countries requiring authentication for saving cards. Extends `source-stripe-inapp-without-card-auth` with save-for-later and CVC re-collection patterns.

> See also [[source-stripe-inapp-without-card-auth]] for the simpler one-time charge variant (same `error_on_requires_action` approach).

## Flow

1. Collect PM via `STPPaymentCardTextField` / `CardInputWidget` / `CardField` → send PM ID to server
2. Server: `stripe.customers.create({ payment_method })` or `paymentMethods.attach(pmId, { customer })`
3. Store Customer ID + PaymentMethod ID mapping in your DB
4. Later: `paymentIntents.create({ customer, payment_method, error_on_requires_action: true, confirm: true })`

## Combined Charge + Save

```javascript
// Save and charge in one call
stripe.paymentIntents.create({
    amount: 1099, currency: 'usd',
    customer: customerId, payment_method: paymentMethodId,
    error_on_requires_action: true, confirm: true,
    setup_future_usage: 'on_session',  // saves without triggering unnecessary auth
})
```

## Compliance Requirements

Must disclose and obtain written consent for:
- Agreement to initiate payments on customer's behalf
- Timing and frequency of charges
- How the payment amount is determined
- Cancellation policy (for subscriptions)

**Non-compliant in**: India and countries requiring authentication for saving cards.

## CVC Re-collection (Optional, All Platforms)

### iOS
```swift
let cardOptions = STPConfirmCardOptions()
cardOptions.cvc = cvc
let paymentMethodOptions = STPConfirmPaymentMethodOptions()
paymentMethodOptions.cardOptions = cardOptions
paymentIntentParams.paymentMethodOptions = paymentMethodOptions
STPPaymentHandler.shared().confirmPayment(paymentIntentParams, with: self)
```

### Android
```kotlin
ConfirmPaymentIntentParams.createWithPaymentMethodId(
    paymentMethodId = pmId,
    paymentMethodOptions = PaymentMethodOptionsParams.Card(cvc = cvc),
    clientSecret = clientSecret
)
stripe.confirmPayment(this, params)
```

### React Native
```javascript
await confirmPayment(clientSecret, {
    paymentMethodType: 'Card',
    paymentMethodData: { cvc, paymentMethodId },
})
```

**CVC warning**: payment can succeed even with failed CVC check. Configure Radar rules to block when CVC verification fails.

## Accounts v2 Note

Use `customer_account` instead of `customer` when listing PaymentMethods with Accounts v2.

## Related Pages

- [[stripe-inapp-payments]] — in-app payments concept page
- [[stripe-saved-payment-methods]] — saved payment methods concept page
- [[source-stripe-inapp-without-card-auth]] — one-time charge variant (same error_on_requires_action pattern)

## Raw Sources

- [[stripe-inapp-save-card-without-auth-2025]] — verbatim guide (~929 lines, iOS + Android + React Native, 2 video assets reused)
