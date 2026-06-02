---
title: "Migrate to Confirmation Tokens — Mobile"
type: source
date_ingested: 2026-04-23
original_format: webpage
raw_files:
  - "stripe-inapp-migrate-confirmation-tokens-2025.md"
tags: [stripe, mobile, ios, android, react-native, confirmation-token, payment-method, migration, payment-intents]
---

## Summary

Migration guide from legacy `PaymentMethod` to `ConfirmationToken` in mobile integrations (iOS, Android, React Native). ConfirmationToken auto-handles shipping, mandate data, return URL, and setup_future_usage — and uniquely enables server-side CVC recollection.

## PaymentMethod vs ConfirmationToken

| Feature | PaymentMethod (Legacy) | ConfirmationToken |
| --- | --- | --- |
| Payment confirmation | ✓ | ✓ |
| Setup future usage | Manual | Automatic |
| Shipping information | Manual | Automatic |
| Mandate data | Manual | Automatic |
| Return URL | Manual | Automatic |
| Server-side CVC recollection | ✗ | ✓ |

## Client-Side Changes

### iOS
Callback param changes from `paymentMethod` to `confirmationToken`:
```swift
PaymentSheet.IntentConfiguration(mode: ...) { confirmationToken in
    // Send confirmationToken.stripeId instead of paymentMethod.stripeId
}
```

### Android
`createIntentCallback` now receives `confirmationToken`:
```kotlin
PaymentSheet.Builder(::onPaymentSheetResult)
    .createIntentCallback { confirmationToken ->
        // Pass confirmationToken.id to server if doing server-side confirmation
    }
```

### React Native
Rename `confirmHandler` → `confirmationTokenConfirmHandler`:
```javascript
intentConfiguration: {
    confirmationTokenConfirmHandler: async (confirmationToken, intentCreationCallback) => {
        // Pass confirmationToken.id to server
    }
}
```

## Server-Side Changes (Two Modes, Same for All Platforms)

### Client-side confirmation
Exclude `payment_method`, `return_url`, `mandate_data`, `shipping` — SDK fills these from ConfirmationToken:
```javascript
const intent = await stripe.paymentIntents.create({
    amount: 1099, currency: 'usd',
    automatic_payment_methods: { enabled: true },
    // NO payment_method, return_url, mandate_data, shipping
});
res.json({ client_secret: intent.client_secret });
```

### Server-side confirmation
Create + confirm in one call:
```javascript
const intent = await stripe.paymentIntents.create({
    amount: 1099, currency: 'usd',
    automatic_payment_methods: { enabled: true },
    confirm: true,
    confirmation_token: req.body.confirmationTokenId, // KEY
});
```

**Override rule**: params passed directly to PaymentIntent at confirmation override ConfirmationToken properties.

## Accessing PM Details

Use `confirmationToken.paymentMethodPreview` instead of inspecting the PaymentMethod object directly.

## Related Pages

- [[stripe-inapp-payments]] — in-app payments concept page
- [[source-stripe-inapp-finalize-payments-server]] — full server-side confirmation guide with ConfirmationToken

## Raw Sources

- [[stripe-inapp-migrate-confirmation-tokens-2025]] — verbatim migration guide (~280 lines, iOS + Android + React Native)
