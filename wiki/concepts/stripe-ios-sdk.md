---
title: "Stripe iOS SDK"
type: concept
category: framework
tags: [stripe, ios, swift, mobile, sdk, payments, apple-pay, payment-sheet, embedded-payments]
---

## Overview

`stripe-ios` (v25.14.0) is Stripe's official native iOS SDK. A modular Swift SDK requiring iOS 13+. Provides prebuilt payment sheets, low-level Stripe API bindings, Apple Pay integration, 3DS handling, identity verification, and Financial Connections. PCI-compliant — sensitive data goes directly to Stripe.

## Module architecture

| Module | Install footprint | Purpose |
|---|---|---|
| `StripePaymentSheet` | Largest | Prebuilt UI: PaymentSheet, EmbeddedPaymentElement, CustomerSheet |
| `StripePayments` | Medium | Low-level API: STPAPIClient, STPPaymentHandler |
| `StripeApplePay` | Lightweight | Apple Pay only — designed for App Clips |
| `StripeConnect` | Medium | Embedded Connect dashboard components |
| `StripeIdentity` | Medium | ID document + selfie capture |
| `StripeFinancialConnections` | Medium | Bank account linking |
| `StripeCardScan` | Medium | Camera-based card scanning |
| `StripeCryptoOnramp` | Small | Crypto onramp UI |
| `Stripe` | Umbrella | All modules + Issuing support |

**Integration**: SPM (Package.swift), CocoaPods (individual `.podspec` per module), or Carthage.

## Important limitation

In-app purchases (subscriptions, in-game currency, premium content, full-version upgrades) **must use Apple's IAP APIs**. Stripe SDK for all other payment scenarios.

## Payment UI options

### PaymentSheet (recommended)

Full-screen sheet — collect + confirm in one flow. Two init patterns:

```swift
// 1. Client-secret pattern (server creates PaymentIntent upfront)
let ps = PaymentSheet(paymentIntentClientSecret: secret, configuration: config)
ps.present(from: vc) { result in ... }

// 2. IntentConfiguration pattern (deferred — server confirms after collection)
let intentConfig = PaymentSheet.IntentConfiguration(
    mode: .payment(amount: 1099, currency: "usd")
) { paymentMethod, _, intentCreationCallback in
    // Create PaymentIntent server-side → call intentCreationCallback(clientSecret, nil)
}
```

`PaymentSheetResult`: `.completed`, `.canceled`, `.failed(error:)`

### EmbeddedPaymentElement

Inline (non-sheet) payment UI embedded in your own view hierarchy. Delegate-based; calls `confirm()` when customer taps your own button.

### CustomerSheet

Saved payment methods management UI. Uses `CustomerAdapter` protocol to sync with a Stripe Customer or custom backend.

## Apple Pay (StripeApplePay module)

Standalone, lightweight — suitable for App Clips.

```swift
let context = STPApplePayContext(paymentRequest: pkRequest, delegate: self)
context?.presentApplePay(on: vc)
```

Delegate:
- `didCreatePaymentMethod(_:paymentInformation:completion:)` — confirm PaymentIntent server-side, return clientSecret
- `didCompleteWith(status:error:)` — `.success`, `.error`, `.userCancellation`

## Low-level API (StripePayments module)

`STPAPIClient.shared` — direct Stripe API:
- `createPaymentMethod(with:completion:)`
- `confirmPaymentIntent(with:completion:)`
- `confirmSetupIntent(with:completion:)`
- `retrievePaymentIntent(withClientSecret:completion:)`

`STPPaymentHandler.shared()` — handles next actions (3DS, redirects):
- `confirmPayment(_:with:completion:)` — confirm + handle next action in one call
- `handleNextAction(forPayment:with:returnURL:completion:)`
- Requires `STPAuthenticationContext` — typically a `UIViewController` conformance

## Configuration

`PaymentSheet.Configuration` / `PaymentElementConfiguration`:
- `merchantDisplayName` — shown in Apple Pay sheet and payment UI
- `customer` — `Customer(id:ephemeralKeySecret:)` for saved payment methods
- `applePay` — `ApplePayConfiguration(merchantId:merchantCountryCode:)`
- `returnURL` — for redirect-based payment methods
- `appearance` — colors, fonts, corner radius (full `PaymentSheet.Appearance` API)
- `defaultBillingDetails` — pre-fill billing fields
- `allowsDelayedPaymentMethods` — enable bank debits, vouchers, etc.

## Localization

40+ languages: Bulgarian, Catalan, Chinese (HK/Simplified/Traditional), Croatian, Czech, Danish, Dutch, English (US/UK), Estonian, Filipino, Finnish, French (FR/CA), German, Greek, Hungarian, Indonesian, Italian, Japanese, Korean, Latvian, Lithuanian, Malay, Maltese, Norwegian (Bokmål/Nynorsk), Polish, Portuguese (PT/BR), Romanian, Russian, Slovak, Slovenian, Spanish (ES/LATAM), Swedish, Thai, Turkish, Vietnamese.

## Sources

- [[source-github-stripe-ios]] — GitHub repo: stripe/stripe-ios (v25.14.0, 13 key files)
- [[source-stripe-billing-ios-sdk]] — BillingSDK for iOS (private preview): higher-level SDK with buy buttons, entitlements, customer portal via Customer Sessions
