---
title: "Card Payments Without Bank Authentication — Mobile"
type: source
date_ingested: 2026-04-23
original_format: webpage
raw_files:
  - "stripe-inapp-without-card-auth-2025.md"
tags: [stripe, mobile, ios, android, react-native, card-payments, error-on-requires-action, legacy, us-canada, payment-intents]
---

## Summary

Legacy/simple mobile card integration for US and Canadian cards only. Uses `error_on_requires_action: true` to synchronously decline instead of handling 2FA. No webhooks needed. Stripe recommends upgrading to the global integration for global businesses.

## When to Use

- Business primarily accepts US/Canada cards
- Want synchronous confirmation (no webhook for post-payment logic)
- Willing to sacrifice global card support for simplicity

**Not suitable for**: global businesses, European/Indian cards (frequently require 2FA).

## Key Param: `error_on_requires_action`

```javascript
const intent = await stripe.paymentIntents.create({
    amount: 1099, currency: 'usd',
    payment_method: req.body.payment_method_id,
    confirm: true,
    error_on_requires_action: true,  // KEY: auto-decline if 2FA required
});
```

Response: `status: 'succeeded'` or error with `code: 'authentication_required'` / `decline_code: 'authentication_not_handled'`.

## Platform UI Components

| Platform | Component | SDK Product |
| --- | --- | --- |
| iOS | `STPPaymentCardTextField` | `StripePaymentsUI` (not StripePaymentSheet) |
| Android | `CardInputWidget` | `stripe-android` |
| React Native | `CardField` | `@stripe/stripe-react-native` |

## Flow

1. Client collects card → `createPaymentMethod()` → sends `paymentMethod.id` to server
2. Server: `paymentIntents.create({ payment_method, confirm: true, error_on_requires_action: true })`
3. Response synchronous: `succeeded` or card error — no async webhook needed

## Comparison: This vs Global Integration

| Feature | This | Global |
| --- | --- | --- |
| US/Canada cards | ✔ | ✔ |
| Global cards | ✗ | ✔ |
| Handles 2FA | ✗ (declines) | ✔ |
| Webhooks needed | No | Recommended |
| Scales to other PMs | ✗ | ✔ |

## Test Cards

| Number | Description |
| --- | --- |
| 4242 4242 4242 4242 | Success |
| 4000 0000 0000 9995 | Decline (insufficient funds) |
| 4000 0025 0000 3155 | Auth required → fails here (`authentication_not_handled`) |

## Upgrade Path

When Dashboard shows `Failed` payments → upgrade to global integration (handles `requires_action` instead of declining).

## Related Pages

- [[stripe-inapp-payments]] — in-app payments concept page

## Raw Sources

- [[stripe-inapp-without-card-auth-2025]] — verbatim guide (~930 lines, iOS + Android + React Native, 2 video assets)
