---
title: "GitHub: Adyen/adyen-android"
type: source
date_ingested: 2026-08-01
original_format: github-repo
raw_files:
  - "github/adyen/adyen-android/snapshots/2026-08-01-5314fad/manifest.json"
tags: [adyen, android, kotlin, mobile-sdk, drop-in, components, sessions, jetpack-compose, github-repository]
---

## Overview

`Adyen/adyen-android` contains Adyen's modular native Android checkout SDK. It provides a prebuilt Drop-in, individual payment Components, Session orchestration, follow-up actions, card encryption, Jetpack Compose adapters, and integrations for local payment methods and delegated wallet or authentication SDKs. This cumulative page begins with package-qualified release `adyen-android@5.20.0` at exact SHA `5314fad1389a8def9d8e3377f27f7405e303faba`.

Repository: <https://github.com/Adyen/adyen-android>

## Evidence boundary

- The snapshot proves retained implementation at `adyen-android@5.20.0`, released on 2026-07-30. It does not establish current product eligibility, merchant enablement, regional availability, or device support.
- Payment-method models and Components are client integration surfaces. The merchant backend or Session response remains authoritative for available methods and transaction results.
- The capsule retains the complete selected source set, including example and story-equivalent integration material, while excluding tests and generated or binary artifacts by policy.
- Adyen 3DS2, Google Pay, Cash App Pay, Twint, and WeChat Pay behavior is partly delegated to separately versioned dependencies. This page records the Android SDK's adapter boundary, not each dependency's complete runtime.

## Grounding excerpts

> "Adyen Android allows you to accept in-app payments by providing you with the building blocks you need to create a checkout experience."
>
> `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/files/README.md:9`

> "Drop-in is our pre-built checkout UI for accepting payments. You only need to integrate through your backend with the /sessions API endpoint"
>
> `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/files/drop-in/src/main/java/com/adyen/checkout/dropin/DropIn.kt:31-36`

> "The rest of the /payments call request data should be filled in, on your server, according to your needs."
>
> `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/files/components-core/src/main/java/com/adyen/checkout/components/core/PaymentComponentData.kt:21-25`

> "You only need to integrate with the /sessions endpoint to create a session and the component will automatically handle the rest of the payment flow."
>
> `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/files/components-compose/src/main/java/com/adyen/checkout/components/compose/ComposeExtensions.kt:124-126`

> "Supported API levels" with Compile SDK Version 36 and Target SDK Version 36.
>
> `raw/github/adyen/adyen-android/releases/adyen-android/5.20.0/2026-08-01/release-notes.md:1-6`

## Platform, distribution, and lifecycle

The retained README marks 5.x active, 4.x inactive with deprecation in June 2026 and end-of-life in June 2027, and 3.x end-of-life. Version `5.20.0` uses minimum Android API 21, compile and target SDK 36, Java toolchain 11, and Kotlin 1.9.25.

Artifacts are distributed through Maven Central. Merchants can import View-based `drop-in` and payment-method modules or Compose-oriented `drop-in-compose` and `components-compose` adapters. ProGuard and R8 rules are embedded in the published artifacts.

## Integration modes and server boundary

Drop-in is the prebuilt checkout route. With Sessions, the merchant backend creates a Session and the SDK handles the remaining client flow. The advanced route begins with `/paymentMethods` and delegates `/payments` and `/payments/details` to merchant callbacks. Drop-in must be registered through the Activity Result API before starting a payment.

Individual Components expose typed state and shopper input. `PaymentComponentData` includes payment-method details, amount, order, storage choice, shopper reference, installments, and billing data that the SDK can infer; the merchant server must complete and submit the rest of the payment request in an advanced integration.

## Sessions

`CheckoutSessionProvider` initializes a checkout Session from a server-created session ID and session data. The internal Session service supports setup, payments, payment details, balance checks, order creation and cancellation, payment-method refresh, and stored-token disabling.

A merchant can take over Session payments or details calls. Once a call is taken over, the corresponding callbacks become the merchant's responsibility; missing callback implementations fail rather than silently returning to SDK ownership. This allows selective server control but requires a consistent ownership boundary.

## Drop-in, storage, and partial payments

Drop-in separates stored, regular, gift-card, and already-paid methods, filters unavailable Components, and routes follow-up actions. It can remove supported stored methods and preserve partial-payment state.

Sessions can check gift-card balances, create or cancel orders, refresh payment methods against a remaining amount, and continue an order after partial payment. These client capabilities do not replace server-side order reconciliation or final transaction verification.

## Components and Compose

The repository separates shared Component models and lifecycle from method-specific modules. Compose adapters retain lifecycle and saved-state owners, create one Component per lifecycle by default, and accept a key when multiple instances are needed. `AdyenComponent` hosts the existing Component view in Compose. Drop-in Compose wraps the same Activity Result contracts as View-based Drop-in instead of introducing a separate checkout engine.

Payment-method modules include cards, ACH, Bacs, Blik, Boleto, issuer-list banking, Pay by Bank, PayTo, SEPA, UPI, gift cards, Google Pay, Cash App Pay, Twint, WeChat Pay, and other local methods. A module's presence proves an adapter exists, not that the method is enabled for a particular merchant.

## Cards and encryption

The Card Component supports six- and eight-digit BIN callbacks, card-brand lookup, dual-brand selection, card scanning, holder name, billing address and address lookup, storage choice, installments, country-specific fields, and stored-card security-code policies. The selected co-badged brand is submitted with the payment data, while debit funding sources suppress installments in the retained implementation.

Card fields and generic sensitive fields are encrypted with an Adyen public key before submission. Client-side encryption narrows raw-detail exposure but does not replace server-side payment creation, result verification, compliance controls, or fulfillment logic.

## Actions and delegated SDKs

The action layer dispatches redirect, 3DS2 fingerprint and challenge, generic SDK, await, QR-code, and voucher actions. The 3DS2 adapter coordinates token validation, fingerprint submission, challenge results, and app-return handling while delegating its underlying runtime to `com.adyen.threeds:adyen-3ds2@2.2.27`.

Google Pay delegates to Google Play Services Wallet `19.4.0`, Cash App Pay to Pay Kit `2.5.0`, Twint to its Android SDK `8.0.0`, and WeChat Pay to Tencent's SDK `6.8.0`. Claims about those runtimes require their own evidence histories.

## Analytics

Drop-in and Component analytics are enabled by default from the 5.x line. `AnalyticsLevel.NONE` suppresses event analytics, while the implementation retains an initial setup request used to obtain a checkout-attempt identifier. Merchants should evaluate this behavior against their telemetry, consent, and privacy requirements.

## `5.20.0` release finding

The exact release documents one change: compile and target SDK support moved to API 36. Android consumers should verify their build toolchain and application compatibility when adopting the release. No API migration or breaking behavioral change is documented in the retained release note.

Broader Drop-in, Session, Component, card, action, wallet, analytics, and payment-method findings above describe accumulated behavior present at the exact SHA, not changes introduced solely by `5.20.0`.

## Related

- [[changelog-github-adyen-android]] - package-qualified release ledger
- [[adyen-android-sdk]] - native Android SDK concept
- [[source-github-adyen-ios]] - independently versioned native iOS SDK
- [[source-github-adyen-web]] - independently versioned browser SDK
- [[co-badged-cards]] - cross-provider network-choice concept
- [[adyen]] - company and knowledge-status page

## Raw sources

- Snapshot manifest: `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/manifest.json`
- Release manifest: `raw/github/adyen/adyen-android/releases/adyen-android/5.20.0/2026-08-01/manifest.json`
- Release notes: `raw/github/adyen/adyen-android/releases/adyen-android/5.20.0/2026-08-01/release-notes.md`
- README: `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/files/README.md`
- Build metadata: `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/files/build.gradle` and `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/files/gradle/libs.versions.toml`
- Session: `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/files/sessions-core/`
- Drop-in: `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/files/drop-in/` and `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/files/drop-in-compose/`
- Components: `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/files/components-core/` and `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/files/components-compose/`
- Cards and encryption: `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/files/card/` and `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/files/cse/`
- Actions: `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/files/action-core/`, `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/files/3ds2/`, and method-specific action modules
- Example integration: `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/files/example-app/`
