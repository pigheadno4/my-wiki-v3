---
title: "GitHub: stripe/stripe-ios"
type: source
date_ingested: 2026-05-13
original_format: github-repo
raw_files:
  - "github-stripe-ios.md"
tags: [stripe, ios, swift, mobile, sdk, payments, apple-pay, payment-sheet, embedded-payments]
---

## Summary

Official Stripe iOS SDK (`stripe-ios`, v25.14.0). A modular Swift SDK for building native payment UIs on iOS. Provides prebuilt payment sheets, low-level API bindings, Apple Pay context, 3DS handling, and embedded payment elements.

## Modules

| Module | Purpose | Min iOS |
|---|---|---|
| `StripePaymentSheet` | Prebuilt full-screen payment UI (PaymentSheet, CustomerSheet, EmbeddedPaymentElement) | 13.0 |
| `StripePayments` | Low-level API bindings (STPAPIClient, STPPaymentHandler) | 13.0 |
| `StripeApplePay` | Lightweight Apple Pay for App Clips | 13.0 |
| `StripeConnect` | Embedded Connect dashboard components | 13.0 |
| `StripeIdentity` | Identity verification (ID + selfie capture) | 13.0 |
| `StripeFinancialConnections` | Bank account linking | 13.0 |
| `StripeCardScan` | Camera-based card scanning | 13.0 |
| `StripeCryptoOnramp` | Crypto onramp UI | 13.0 |
| `Stripe` | All-in-one umbrella (includes Issuing) | 13.0 |

## Important limitation

In-app purchases (subscriptions, in-game currency, premium content unlocks, full-version upgrades) must use Apple's IAP APIs. Stripe SDK for all other payment scenarios.

## Payment UI options

### PaymentSheet

Full-screen sheet covering collect → confirm in one flow.

```swift
// Server creates PaymentIntent, returns clientSecret
var config = PaymentSheet.Configuration()
config.merchantDisplayName = "My Shop"
let paymentSheet = PaymentSheet(paymentIntentClientSecret: clientSecret, configuration: config)
paymentSheet.present(from: viewController) { result in
    switch result {
    case .completed: // success
    case .canceled: break
    case .failed(let error): break
    }
}
```

Also supports `IntentConfiguration` (deferred confirm — server confirms after PaymentSheet collects):
```swift
let intentConfig = PaymentSheet.IntentConfiguration(mode: .payment(amount: 1000, currency: "usd")) { paymentMethod, _, intentCreationCallback in
    // Create PaymentIntent server-side, call intentCreationCallback with clientSecret
}
```

### EmbeddedPaymentElement

Inline (non-sheet) payment UI embedded directly in your view hierarchy. Delegate-based.

### CustomerSheet

Saved payment methods management UI. Uses `CustomerAdapter` protocol to sync with Stripe Customer or your own backend.

## Apple Pay (StripeApplePay)

```swift
let context = STPApplePayContext(paymentRequest: request, delegate: self)
context?.presentApplePay()

// Delegate
func applePayContext(_ context: STPApplePayContext, didCreatePaymentMethod paymentMethod: STPPaymentMethod, paymentInformation: PKPayment, completion: @escaping STPIntentClientSecretCompletionBlock)
func applePayContext(_ context: STPApplePayContext, didCompleteWith status: STPPaymentStatus, error: Error?)
```

## Low-level API (StripePayments)

`STPAPIClient` — direct Stripe API calls:
- `createPaymentMethod(with:completion:)` — tokenize card / bank details
- `confirmPaymentIntent(with:completion:)` — confirm a PaymentIntent
- `confirmSetupIntent(with:completion:)` — confirm a SetupIntent
- `retrievePaymentIntent(withClientSecret:completion:)`

`STPPaymentHandler` — handles next actions (3DS, redirect):
- `confirmPayment(_:with:completion:)` — confirm + handle next action
- `handleNextAction(forPayment:with:returnURL:completion:)` — handle 3DS challenge
- Requires `STPAuthenticationContext` (a `UIViewController` conformance)

## Localization

40+ languages including: Bulgarian, Chinese (Simplified/Traditional/HK), Croatian, Czech, Danish, Dutch, Finnish, French, German, Greek, Hungarian, Indonesian, Italian, Japanese, Korean, Norwegian, Polish, Portuguese, Romanian, Russian, Slovak, Spanish, Swedish, Thai, Turkish, Vietnamese.

## Key configuration types

- `PaymentSheet.Configuration` / `PaymentElementConfiguration` — appearance, billing details, shipping, customer info, merchant display name, Apple Pay config, return URL, allowed payment methods
- `PaymentSheet.Appearance` — colors, fonts, corner radius customization
- `STPAuthenticationContext` — protocol for providing a `UIViewController` for 3DS presentation

## Related pages

- [[stripe-ios-sdk]] — concept page
- [[stripe-react-native-sdk]] — React Native counterpart
- [[stripe]] — company page

## Raw Sources

- [[github-stripe-ios]] — stub file with key file index
