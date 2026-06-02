---
title: "Stripe Android SDK"
type: concept
category: framework
tags: [stripe, android, kotlin, mobile, sdk, payments, google-pay, payment-sheet, jetpack-compose]
---

## Overview

`stripe-android` (v23.8.0) is Stripe's official native Android SDK. Written in Kotlin, built with Jetpack Compose internally. Requires Android 6.0+ (API 23), `compileSdkVersion` 36, Kotlin 2.x. PCI-compliant — sensitive card data goes directly to Stripe.

## Requirements

| Requirement | Value |
|---|---|
| Android API | 23+ (Android 6.0) |
| `compileSdkVersion` | 36+ |
| Android Gradle Plugin | 8.13.2 |
| Gradle | 9.3.1 |
| Kotlin | 2.3.10 |
| Jetpack Compose | Version-pinned (SDK updates monthly; check CHANGELOG) |

## Installation

```gradle
dependencies {
    implementation 'com.stripe:stripe-android:23.8.0'
}
```

## Initialization

```kotlin
// Call once at app startup (e.g. Application.onCreate)
PaymentConfiguration.init(context, publishableKey = "pk_...")

// For Connect (on behalf of connected accounts)
PaymentConfiguration.init(context, publishableKey = "pk_...", stripeAccountId = "acct_...")
```

## Payment UI options

### PaymentSheet (recommended)

Full-screen bottom sheet — collect + confirm in one flow.

```kotlin
val paymentSheet = PaymentSheet(activity) { result ->
    when (result) {
        is PaymentSheetResult.Completed -> { /* success */ }
        is PaymentSheetResult.Canceled -> { }
        is PaymentSheetResult.Failed -> { result.error }
    }
}

// Client-secret pattern (server creates PaymentIntent upfront)
paymentSheet.presentWithPaymentIntent(clientSecret, configuration)

// IntentConfiguration pattern (deferred — server confirms after collection)
val intentConfig = PaymentSheet.IntentConfiguration(
    mode = PaymentSheet.IntentConfiguration.Mode.Payment(amount = 1099, currency = "usd"),
    confirmHandler = { paymentMethod, _, intentCreationCallback ->
        // create PaymentIntent server-side → call intentCreationCallback(clientSecret, null)
    }
)
paymentSheet.presentWithIntentConfiguration(intentConfig, configuration)
```

Jetpack Compose: `PaymentSheet.rememberPaymentSheet()`

### FlowController

Two-step flow: present payment method selector separately, then confirm when customer taps your own Pay button. Use `PaymentSheet.FlowController`.

### CustomerSheet

Saved payment methods management UI. Configure via `CustomerSheet.Configuration` and `CustomerAdapter` protocol.

### EmbeddedPaymentElement

Inline (non-sheet) payment UI embedded directly in your layout.

## Google Pay

```kotlin
val launcher = GooglePayLauncher(
    activity = this,
    config = GooglePayLauncher.Config(
        environment = GooglePayEnvironment.Test,
        merchantCountryCode = "US",
        merchantName = "My Shop"
    ),
    readyCallback = { isReady -> /* toggle Google Pay button visibility */ },
    resultCallback = { result ->
        when (result) {
            is GooglePayLauncherResult.Completed -> { result.paymentIntent }
            is GooglePayLauncherResult.Canceled -> { }
            is GooglePayLauncherResult.Failed -> { result.error }
        }
    }
)
launcher.presentForPaymentIntent(clientSecret)
```

`GooglePayPaymentMethodLauncher` — creates a PaymentMethod without immediately confirming a PaymentIntent (for custom flows).

Compose: `rememberGooglePayLauncher()`

## Low-level API (`Stripe` client)

```kotlin
val stripe = Stripe(context, publishableKey = "pk_...")
```

Key methods:
- `createPaymentMethod(params, callback)` — tokenize card/bank details
- `createToken(params, callback)` — legacy token creation
- `confirmPaymentIntent(confirmParams, activity, requestCode)` — confirm + handle 3DS
- `confirmSetupIntent(confirmParams, activity, requestCode)` — confirm SetupIntent
- `handleNextActionForPayment(activity, clientSecret)` — resume 3DS from `onActivityResult`
- `retrievePaymentIntent(clientSecret, callback)`
- `retrieveSetupIntent(clientSecret, callback)`

## 3DS2 customization

`PaymentAuthConfig.Stripe3ds2Config` — customize 3DS2 challenge screen appearance: button style, label, navigation bar, text fields, footer, selection indicators. Set globally:

```kotlin
PaymentAuthConfig.init(
    PaymentAuthConfig.Builder()
        .set3ds2Config(PaymentAuthConfig.Stripe3ds2Config.Builder()
            .setTimeout(5)
            .build())
        .build()
)
```

## Key configuration (`PaymentSheet.Configuration`)

- `merchantDisplayName` — shown in payment sheet header
- `customer` — `PaymentSheet.CustomerConfiguration(id, ephemeralKeySecret)` for saved PMs
- `googlePay` — `PaymentSheet.GooglePayConfiguration(environment, countryCode, currencyCode)`
- `appearance` — `PaymentSheet.Appearance` (colors, shapes, typography)
- `defaultBillingDetails` — pre-fill billing fields
- `allowsDelayedPaymentMethods` — enable bank debits, vouchers, etc.
- `returnUrl` — for redirect-based payment methods

## Localization

40+ languages — same set as iOS SDK: Bulgarian, Catalan, Chinese (HK/Simplified/Traditional), Croatian, Czech, Danish, Dutch, Finnish, French, German, Greek, Hungarian, Indonesian, Italian, Japanese, Korean, Norwegian, Polish, Portuguese, Romanian, Russian, Slovak, Slovenian, Spanish, Swedish, Thai, Turkish, Vietnamese.

## Key differences vs iOS SDK

| Aspect | Android | iOS |
|---|---|---|
| Init pattern | `PaymentConfiguration.init(context, pk)` | `StripeProvider` / `initStripe()` |
| Platform Pay | `GooglePayLauncher` | `STPApplePayContext` |
| UI framework | Jetpack Compose (internal) | SwiftUI / UIKit |
| IAP restriction | Not mentioned | Explicitly noted (Apple App Store rules) |

## Sources

- [[source-github-stripe-android]] — GitHub repo: stripe/stripe-android (v23.8.0, 10 key files)
