---
title: "Finalize Payments on the Server — Mobile"
type: source
date_ingested: 2026-04-22
original_format: webpage
raw_files:
  - "stripe-inapp-finalize-payments-server-2025.md"
tags: [stripe, mobile, ios, android, react-native, payment-sheet, flow-controller, confirmation-token, server-confirmation, apple-pay, saved-cards, customer-session]
---

## Summary

Full integration guide for the server-side confirmation pattern across iOS, Android, and React Native. Client renders PaymentSheet → collects payment details → sends ConfirmationToken ID to server → server creates+confirms PaymentIntent → returns client_secret. Also covers Apple Pay, saved cards, card scanning, delayed PMs.

## Core Pattern: ConfirmationToken Flow

```
Client: PaymentSheet collects payment details
  ↓
Client sends confirmationToken.stripeId to server
  ↓
Server: stripe.paymentIntents.create({
  confirm: true,
  confirmation_token: req.body.confirmation_token_id,
  amount: 1099, currency: 'usd',
  automatic_payment_methods: { enabled: true },
})
  ↓
Server returns client_secret → PaymentSheet handles next actions
```

Verify IntentConfiguration properties match PaymentIntent (amount, currency, setup_future_usage).

## PaymentSheet vs FlowController

| | PaymentSheet | FlowController |
| --- | --- | --- |
| Who controls confirm | Stripe (user taps Pay) | You (call confirm() on your own button) |
| Use when | Standard checkout | Custom buy flow |

## FlowController `update()` — Important

When cart changes (items, discounts), call `update()` with new IntentConfiguration:

```swift
// iOS — disable UI during update
paymentSheetFlowController.update(intentConfiguration: newConfig) { error in
  if error != nil { /* Must retry — customer can't pay until update succeeds */ }
  else { /* Re-enable UI */ }
}
```

**Must retry on failure** — until update succeeds, customer can't pay or select PM. Don't call `present` or `confirm` during update.

## Apple Pay Setup

1. Register Apple Merchant ID at developer.apple.com
2. Create certificate: Dashboard → iOS Certificate Settings → Add new application
3. Xcode: add Apple Pay capability, select merchant ID

```swift
configuration.applePay = .init(
  merchantId: "merchant.com.your_app_name",
  merchantCountryCode: "US"
)
```

**Recurring payments**: set `PKRecurringPaymentRequest` on `PKPaymentRequest` in `paymentRequestHandler`.

**Order tracking**: implement `authorizationResultHandler` to attach `PKPaymentOrderDetails` after payment.

## Saved Cards (CustomerSession)

```js
// Server: use mobile_payment_element component (NOT payment_element)
const customerSession = await stripe.customerSessions.create({
  customer: customer.id,
  components: {
    mobile_payment_element: {
      enabled: true,
      features: {
        payment_method_save: 'enabled',
        payment_method_redisplay: 'enabled',
        payment_method_remove: 'enabled',
      },
    },
  },
});
```

```swift
// iOS client: requires beta import
@_spi(CustomerSessionBetaAccess) import StripePaymentSheet
configuration.customer = .init(id: customerId, customerSessionClientSecret: csSecret)
```

Note: `mobile_payment_element` component (NOT `payment_element`) — different from web integration.

## Configuration Options

| Option | Description |
| --- | --- |
| `returnURL` | Custom URL scheme for redirect-based PMs |
| `allowsDelayedPaymentMethods` | Opt in to ACH, SEPA, OXXO, etc. (defaults false) |
| `paymentMethodLayout` | `.automatic`, `.vertical`, `.horizontal` |
| `style` | `.alwaysLight`, `.alwaysDark`, or auto |
| `merchantDisplayName` | Shown in payment UI (defaults to app name) |
| `defaultBillingDetails` | Pre-populate billing fields |
| `billingDetailsCollectionConfiguration` | Control which fields are collected |

## Card Scanning (iOS)

Add `NSCameraUsageDescription` to Info.plist.

## SDK Installation (iOS)

Swift Package Manager → `https://github.com/stripe/stripe-ios-spm`, add **StripePaymentSheet** product. Also supports CocoaPods, Carthage, and Manual Framework.

## Related Pages

- [[stripe-inapp-payments]] — concept page
- [[source-stripe-inapp-payment-sheet]] — Payment Sheet UI detail
- [[stripe-saved-payment-methods]] — saved PM patterns

## Raw Sources

- [[stripe-inapp-finalize-payments-server-2025]] — verbatim server confirmation guide (6106 lines, iOS+Android+RN; 7 images reused)
