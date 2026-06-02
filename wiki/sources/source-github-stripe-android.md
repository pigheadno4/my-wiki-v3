---
title: "GitHub: stripe/stripe-android"
type: source
date_ingested: 2026-05-13
original_format: github-repo
raw_files:
  - "github-stripe-android.md"
tags: [stripe, android, kotlin, mobile, sdk, payments, google-pay, payment-sheet, jetpack-compose]
---

## Summary

Official Stripe Android SDK (`stripe-android`, v23.8.0). A modular Kotlin SDK for building native payment UIs on Android. Provides prebuilt payment sheets, low-level Stripe API bindings, Google Pay integration, 3DS2 handling, and saved payment method management. Built with Jetpack Compose internally.

## Requirements

- Android 6.0 (API level 23) and above
- `compileSdkVersion` 36+
- Android Gradle Plugin 8.13.2
- Gradle 9.3.1
- Kotlin 2.3.10
- Jetpack Compose (version-pinned — SDK updates Compose monthly; check CHANGELOG for compat table)

## Installation

```gradle
dependencies {
    implementation 'com.stripe:stripe-android:23.8.0'
}
```

## Key modules

| Module | Purpose |
|---|---|
| `paymentsheet` | PaymentSheet, FlowController, CustomerSheet, EmbeddedPaymentElement |
| `payments-core` | `Stripe` API client, PaymentMethod model, Google Pay launcher, 3DS2 config |
| `payments-model` | Shared data models (PaymentIntent, SetupIntent, etc.) |
| `payments-ui-core` | Shared UI components |
| `stripe-core` | Core utilities, networking, error handling |
| `financial-connections` | Bank account linking |
| `identity` | Identity verification |
| `connect` | Connect embedded components |
| `stripecardscan` | Camera-based card scanning |
| `crypto-onramp` | Crypto onramp UI |

## Initialization

```kotlin
PaymentConfiguration.init(context, publishableKey = "pk_...")
// Optional: set Stripe account for Connect
PaymentConfiguration.init(context, publishableKey = "pk_...", stripeAccountId = "acct_...")
```

## Payment UI options

### PaymentSheet

Full-screen bottom sheet — collect + confirm in one flow.

```kotlin
// Activity/Fragment
val paymentSheet = PaymentSheet(this) { result ->
    when (result) {
        is PaymentSheetResult.Completed -> { /* success */ }
        is PaymentSheetResult.Canceled -> { }
        is PaymentSheetResult.Failed -> { result.error }
    }
}

// Present with client secret (server creates PaymentIntent upfront)
paymentSheet.presentWithPaymentIntent(clientSecret, configuration)

// Or with IntentConfiguration (deferred confirm)
val intentConfig = PaymentSheet.IntentConfiguration(
    mode = PaymentSheet.IntentConfiguration.Mode.Payment(amount = 1099, currency = "usd"),
    confirmHandler = { paymentMethod, _, intentCreationCallback ->
        // create PaymentIntent server-side → call intentCreationCallback
    }
)
paymentSheet.presentWithIntentConfiguration(intentConfig, configuration)
```

Compose: `PaymentSheet.rememberPaymentSheet()`

### FlowController

Two-step: collect payment method separately, then confirm. Allows custom "Pay" button.

### CustomerSheet

Saved payment methods management UI. Configure via `CustomerSheet.Configuration` and `CustomerAdapter`.

## Google Pay

```kotlin
val googlePayLauncher = GooglePayLauncher(
    activity = this,
    config = GooglePayLauncher.Config(
        environment = GooglePayEnvironment.Test,
        merchantCountryCode = "US",
        merchantName = "My Shop"
    ),
    readyCallback = { isReady -> /* show/hide Google Pay button */ },
    resultCallback = { result -> /* handle GooglePayLauncherResult */ }
)
googlePayLauncher.presentForPaymentIntent(clientSecret)
```

Also: `GooglePayPaymentMethodLauncher` for creating a PaymentMethod without immediately charging.

## Low-level API (`Stripe` client)

```kotlin
val stripe = Stripe(context, publishableKey = "pk_...")
stripe.createPaymentMethod(params, callback)
stripe.confirmPaymentIntent(confirmParams, activity, REQUEST_CODE)
stripe.handleNextActionForPayment(activity, clientSecret)
```

Key methods: `createPaymentMethod`, `createToken`, `confirmPaymentIntent`, `confirmSetupIntent`, `retrievePaymentIntent`, `retrieveSetupIntent`, `handleNextActionForPayment`, `handleNextActionForSetupIntent`.

## 3DS2 customization

`PaymentAuthConfig.Stripe3ds2Config` — customize the 3DS2 challenge UI: button style, label, navigation bar, text fields, footer, selection indicators. Set globally via `PaymentAuthConfig.init()`.

## Localization

40+ languages — same set as iOS SDK (Bulgarian, Catalan, Chinese variants, Croatian, Czech, Danish, Dutch, Finnish, French, German, Greek, Hungarian, Indonesian, Italian, Japanese, Korean, Norwegian, Polish, Portuguese, Romanian, Russian, Slovak, Slovenian, Spanish, Swedish, Thai, Turkish, Vietnamese).

## Notable vs iOS differences

- Android uses `PaymentConfiguration.init()` for SDK init (vs `StripeProvider` / `initStripe()` on iOS)
- Google Pay via `GooglePayLauncher` (vs `usePlatformPay` hook in React Native)
- Jetpack Compose integration built-in (Compose-based `rememberPaymentSheet()`, `rememberGooglePayLauncher()`)
- **No IAP restriction note** in Android README (unlike iOS/React Native which explicitly warn about App Store rules)

## Related pages

- [[stripe-android-sdk]] — concept page
- [[stripe-ios-sdk]] — iOS counterpart
- [[stripe-react-native-sdk]] — React Native counterpart
- [[stripe]] — company page

## Raw Sources

- [[github-stripe-android]] — stub file with key file index
