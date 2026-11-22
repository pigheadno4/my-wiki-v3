---
title: "Card Payments Without Bank Authentication — Mobile"
type: source
date_ingested: 2026-04-23
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/mobile/without-card-authentication"
raw_files:
  - "stripe-inapp-without-card-auth-2025.md"
tags: [stripe, mobile, ios, android, react-native, card-payments, error-on-requires-action, basic-card-integration, us-canada, payment-intents]
---

## Summary

The April 23, 2026 guide describes Stripe's basic mobile integration for businesses accepting only US and Canadian cards. An issuer authentication request causes the payment to fail immediately. The April snapshot includes iOS, Android and React Native examples (raw lines 8–334, 335–629 and 630–930).

## When to Use

- The business accepts only US and Canadian cards.
- The integration attempts confirmation immediately on the server and declines cards that require issuer authentication.

For growing or global businesses, the April guide points to Stripe's [global integration](https://docs.stripe.com/payments/accept-a-payment.md), which supports issuer authentication and recommends webhooks for post-payment tasks (raw lines 12–34).

## April Server Example

```javascript
const intent = await stripe.paymentIntents.create({
    amount: 1099, currency: 'usd', // Example amount selected by the server
    payment_method: req.body.payment_method_id,
    confirm: true,
    error_on_requires_action: true, // Fail confirmation if customer action is required
});
```

The April Node.js example fulfills only when the server observes a `PaymentIntent` status of `succeeded`. It returns the `StripeCardError` message to the client and handles unexpected statuses and other exceptions as separate error paths. The authentication-required API example shows `error.code: authentication_required`, `decline_code: authentication_not_handled` and an embedded `PaymentIntent` with status `requires_payment_method` (raw lines 216–265 and 290–316).

## April Platform UI Components

| Platform | Component | SDK Product |
| --- | --- | --- |
| iOS | `STPPaymentCardTextField` | `StripePaymentsUI` |
| Android | `CardInputWidget` | `stripe-android` |
| React Native | `CardField` | `@stripe/stripe-react-native` |

The April SDK guidance lists iOS 13 or later and shows Stripe Android SDK `23.5.0` in the Gradle sample. The examples use publishable keys on the client and distinguish test keys from live keys (raw lines 38–123, 369–415 and 682–722).

## Flow

1. The client SDK collects sensitive card details and creates a `PaymentMethod` with `createPaymentMethod`. The app sends its ID to the merchant server.
2. The trusted server determines the amount and creates a distinct `PaymentIntent` using the supplied payment method ID. It attempts confirmation immediately with `confirm: true` and `error_on_requires_action: true`.
3. For this synchronous example, the server can run immediate post-payment actions from its `succeeded` response without waiting for a webhook.

## April Comparison with the Global Integration

| Feature | Basic example | Global integration |
| --- | --- | --- |
| US and Canadian cards | Supported | Supported |
| Global cards | Outside scope | Supported |
| Issuer authentication requests | Declines the payment | Handles authentication |
| Post-payment handling | Immediate actions use the server's `succeeded` result | Webhooks recommended |
| Other payment methods | Card-only guide | Can scale to other methods |

## April Sandbox Test Cards

The April test guide uses any CVC and postal code with a future expiration date (raw lines 317–327).

| Number | Test-environment result |
| --- | --- |
| 4242 4242 4242 4242 | Payment succeeds immediately |
| 4000 0000 0000 9995 | Decline with `insufficient_funds` |
| 4000 0025 0000 3155 | Authentication required. This flow fails with `authentication_not_handled` |

## Upgrade Path

The [April 23, 2026 mobile migration guide](https://docs.stripe.com/payments/mobile/upgrade-to-handle-actions) recommends upgrading if you see many Dashboard failures like its issuer-authentication example or the API diagnostic `requires_action_not_handled`. The [November 7, 2026 Payment Intents migration guide](https://docs.stripe.com/payments/payment-intents/upgrade-to-handle-actions) repeats that diagnostic. The basic acceptance example above has its own authentication error fields, and the `insufficient_funds` card illustrates a separate decline. See [[source-stripe-inapp-upgrade-to-handle-actions]] for the mobile authentication flow.

## Related Pages

- [[stripe]]
- [[stripe-inapp-payments]] — in-app payments concept page

## Raw Sources

- [[raw/stripe-inapp-without-card-auth-2025|April 23, 2026 basic mobile card guide]] — iOS, Android and React Native, with two video assets.

## Related raw API references

- [[raw/stripe-payments-mobile-without-card-authentication-2026-11-07|November 7, 2026 platform selector]] — navigation for iOS, Android and React Native. The linked variant bodies were outside the capture.
