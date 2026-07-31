---
title: "Stripe Android SDK"
type: concept
category: framework
tags: [stripe, android, kotlin, mobile, sdk, payments, google-pay, payment-sheet, embedded-payment-element, jetpack-compose]
---

## Overview

`stripe-android` is Stripe's official native Android SDK. The approved `23.13.1` baseline provides prebuilt payment UI, lower-level PaymentIntent and SetupIntent APIs, Google Pay, automatic 3DS/SCA handling, and separate modules for Connect, Identity, Financial Connections, Crypto Onramp, BNPL messaging, and card scanning.

The SDK collects sensitive payment details directly for Stripe rather than routing them through the merchant server. Merchant backends still own creation of PaymentIntents, SetupIntents, customer/session credentials, fulfillment decisions, and webhook processing.

## Current Ingested Baseline

| Field | Value |
| --- | --- |
| Package | `com.stripe:stripe-android:23.13.1` |
| Release tag | `v23.13.1` |
| Exact commit | `dc874ce7c62dd433664ec4e312efeb9300c21795` |
| Android minimum | Android 6.0 / API 23 |
| Compile SDK | 36+ |
| Android Gradle Plugin | 8.13.2 |
| Gradle | 9.3.1 |
| Kotlin | 2.3.10 |
| Compose compatibility | Compose UI 1.10.x for SDK 23.x |

This table reports the latest wiki-ingested release, not necessarily the latest release available upstream.

## Installation

```gradle
dependencies {
    implementation 'com.stripe:stripe-android:23.13.1'
}
```

Initialize publishable configuration at application startup. A connected-account ID can be included for Connect API requests.

```kotlin
PaymentConfiguration.init(context, publishableKey = "pk_...")
PaymentConfiguration.init(context, publishableKey = "pk_...", stripeAccountId = "acct_...")
```

## Payment UI

### PaymentSheet

PaymentSheet is the maintained prebuilt checkout surface. `PaymentSheet.Builder` is the preferred Activity, Fragment, and Compose construction path; direct constructors are deprecated. It supports:

- PaymentIntent and SetupIntent client-secret flows;
- deferred Intent creation through a merchant callback;
- saved methods through customer configuration;
- Google Pay, Link, delayed methods, custom methods, and external methods subject to account and platform eligibility;
- appearance, billing, shipping, payment-method ordering, and wallet-button configuration; and
- automatic next-action and 3DS handling.

`PaymentSheetResult.Completed` means the customer completed the SDK flow. The payment can still be processing, so fulfillment must wait for a successful server-side payment event.

### FlowController

`PaymentSheet.FlowController` separates method selection from confirmation. The merchant presents payment options, displays the returned `PaymentOption`, and calls `confirm()` from its own pay button.

### Embedded Payment Element

`EmbeddedPaymentElement` places payment-method UI inside a merchant-owned Compose layout. It has explicit configure, selection-state, clear, and confirm operations and returns `Completed`, `Canceled`, or `Failed`. The retained example demonstrates one-step and state-preserving two-step Activity contracts.

## Google Pay

`GooglePayLauncher` confirms PaymentIntents or SetupIntents after an asynchronous readiness callback. `presentForPaymentIntent` and `presentForSetupIntent` are invalid until the device is reported ready. SetupIntent presentation additionally requires an ISO currency code, even though the SetupIntent API itself does not.

`GooglePayPaymentMethodLauncher` is the lower-level option when an integration needs a PaymentMethod without immediately confirming an Intent. Compose integrations use `rememberGooglePayLauncher`.

Wallet API availability does not prove that a specific merchant, country, currency, card network, or payment method is enabled.

## Low-Level APIs

The `Stripe` entry point supports asynchronous and synchronous access to:

- PaymentIntent confirmation, retrieval, and next-action handling;
- SetupIntent confirmation, retrieval, and next-action handling;
- PaymentMethod creation;
- Source creation and retrieval; and
- token creation for supported card, bank, identity, and account parameter types.

`PaymentLauncher` is a lifecycle-aware confirmation and next-action abstraction for Activity, Fragment, and Compose integrations. Both surfaces use publishable keys and client secrets; they do not replace server-side secret-key operations.

## Specialized Modules

| Module | Primary contract | Lifecycle or access note |
| --- | --- | --- |
| `connect` | `EmbeddedComponentManager` creates account-onboarding, Payments, and Payouts components | Requires publishable key plus a callback that fetches a server-created client secret; Payments and Payouts became GA in `23.12.0` |
| `financial-connections` | `FinancialConnectionsSheet` returns linked-account session data or token results | Register the launcher unconditionally during Activity/Fragment initialization |
| `identity` | `IdentityVerificationSheet` presents a verification session | Requires a verification-session ID and ephemeral-key secret created on the server |
| `crypto-onramp` | `OnrampCoordinator` handles Link authentication, KYC, wallet ownership, payment collection, token creation, and checkout | Marked experimental/private-preview evidence; availability is not implied by the public source |
| `payment-method-messaging` | Compose BNPL promotional messaging for Affirm, Afterpay/Clearpay, and Klarna | Public preview; amount and currency are required, and configuration can return `NoContent` |
| `stripecardscan` | Card scan implementation used by Stripe UI surfaces | Direct retained classes are library-group restricted; v23.6 restored card scanning in public preview through Stripe UI |

## Migration Landmarks

- `23.0.0` raises the minimum Android API level to 23 and the compile/target SDK to 36. It also updates Kotlin, Compose, Gradle, and Android dependencies.
- v22 removes legacy token-oriented `CardParams` paths, deprecated Google Pay launchers, 3DS1, and accidentally exposed APIs; builder APIs replace data-class copying for public configuration objects.
- v21 removes Basic Integration in favor of Mobile Payment Element and changes PaymentSheet's default method layout to automatic.
- Current code favors builder and lifecycle-aware launcher APIs over deprecated constructors and launcher factories.

## `23.13.1` Release Note

The exact `23.13.1` release fixes an Alipay test-mode issue where the SDK could fail to reconcile and close out a payment. The broader architecture on this page is baseline evidence from the complete retained capsule and must not be attributed solely to that patch.

## Related

- Source: [[source-github-stripe-android]]
- Changelog: [[changelog-github-stripe-android]]
- Company: [[stripe]]
- Native counterpart: [[stripe-ios-sdk]]
- Cross-platform bridge: [[stripe-react-native-sdk]]
- Supporting concepts: [[stripe-inapp-payments]], [[stripe-payment-intents]], [[stripe-3d-secure]], [[stripe-payment-method-messaging-element]], [[stripe-crypto-onramp]]

## Sources

- `raw/github/stripe/stripe-android/snapshots/2026-07-31-dc874ce/manifest.json` - exact-SHA `23.13.1` source capsule
- `raw/github/stripe/stripe-android/snapshots/2026-07-31-dc874ce/files/README.md` - purpose, capabilities, requirements, installation, and security boundary
- `raw/github/stripe/stripe-android/snapshots/2026-07-31-dc874ce/files/MIGRATING.md` - major-version migration requirements
- `raw/github/stripe/stripe-android/snapshots/2026-07-31-dc874ce/files/paymentsheet/src/main/java/com/stripe/android/paymentsheet/PaymentSheet.kt` - PaymentSheet and FlowController contract
- `raw/github/stripe/stripe-android/snapshots/2026-07-31-dc874ce/files/paymentsheet/src/main/java/com/stripe/android/paymentsheet/PaymentSheetResult.kt` - result and fulfillment semantics
- `raw/github/stripe/stripe-android/snapshots/2026-07-31-dc874ce/files/payments-core/src/main/java/com/stripe/android/Stripe.kt` - low-level client API
- `raw/github/stripe/stripe-android/snapshots/2026-07-31-dc874ce/files/payments-core/src/main/java/com/stripe/android/googlepaylauncher/GooglePayLauncher.kt` - Google Pay lifecycle and result contract
- `raw/github-stripe-android.md` - legacy v23.8.0 capsule pointer
