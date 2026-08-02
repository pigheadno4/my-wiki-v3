---
title: "Adyen Android SDK"
type: concept
category: technology
tags: [adyen, android, kotlin, mobile, sdk, drop-in, components, sessions, jetpack-compose, google-pay, 3d-secure]
---

## Adyen Android SDK

Adyen Android is a modular native checkout SDK. Its main integration choices are Drop-in, which supplies a prebuilt payment-method selection and action flow, and individual Components, which let the merchant own the surrounding interface and orchestration. Both traditional Android Views and Jetpack Compose entry points are retained in the `adyen-android@5.20.0` baseline.

## Current baseline

| Field | Value |
| --- | --- |
| Package | `adyen-android@5.20.0` |
| Release tag | `5.20.0` |
| Exact commit | `5314fad1389a8def9d8e3377f27f7405e303faba` |
| Minimum Android API | 21 |
| Compile SDK | 36 |
| Target SDK | 36 |
| Java toolchain | 11 |
| Kotlin | 1.9.25 |

The README marks the 5.x line active. This table reports retained repository evidence, not current merchant eligibility or payment-method availability.

## Integration and server boundary

The Sessions flow starts from a Session created by the merchant backend. `CheckoutSessionProvider` performs the SDK setup call, and Drop-in or an individual Component can then handle payments, additional details, balance checks, partial-payment orders, and stored-method removal through the Session endpoints. A merchant can take over a Session call, but after takeover the remaining required callbacks must be implemented consistently.

The advanced flow starts from `/paymentMethods` and delegates `/payments` and `/payments/details` to the merchant's `DropInService` or Component callbacks. `PaymentComponentData` contains SDK-derived and shopper-entered fields, but the source explicitly assigns completion of the rest of the payment request to the merchant server.

## Module architecture

| Surface | Responsibility |
| --- | --- |
| `drop-in` / `drop-in-compose` | Prebuilt payment-method list, Activity Result launchers, stored methods, actions, and partial-payment flow |
| `components-core` / `components-compose` | Shared models, configuration, callbacks, provider lifecycle, analytics, and Compose adapters |
| `sessions-core` | Session setup, payments, payment details, balance, order, cancellation, and token-disable calls |
| `card` / `cse` | Card UI, BIN and brand detection, dual-brand selection, installments, address fields, and client-side encryption |
| `action-core`, `redirect`, `3ds2`, `await`, `qr-code`, `voucher` | Follow-up action dispatch and method-specific action handling |
| Payment-method modules | ACH, Bacs, Blik, Boleto, issuer-list banking, Pay by Bank, PayTo, SEPA, UPI, gift cards, and other local methods |
| External SDK adapters | Google Pay, Cash App Pay, Twint, WeChat Pay, and Adyen 3DS2 |

Compose Components retain lifecycle and saved-state owners, create one Component per lifecycle by default, and allow a key when multiple instances are needed. `AdyenComponent` bridges the existing Component view into Compose; Drop-in Compose wraps the same Activity Result contracts rather than implementing a separate payment engine.

## Cards, storage, and partial payments

The Card Component supports six- or eight-digit BIN callbacks, brand lookup, dual-brand selection, card scanning, holder name, billing address and address lookup, storage choice, installments, country-specific fields, and stored-card CVC policy. Debit funding sources suppress installments in the retained implementation.

Card and generic fields are encrypted with an Adyen public key before submission. Encryption narrows exposure of sensitive fields but does not replace server-side payment creation, result verification, compliance controls, or fulfillment logic.

Drop-in separates stored and regular methods, checks method availability, can remove supported stored methods, and represents gift-card and remaining-amount state during partial payments. Sessions can check balances, create or cancel orders, refresh payment methods, and continue from a partially paid order.

## Actions and delegated runtimes

The SDK handles redirect, 3DS2 fingerprint and challenge, SDK, await, QR-code, and voucher actions. The 3DS2 adapter validates required tokens, coordinates fingerprint and challenge results, and can configure an out-of-band app-return URL, but the underlying runtime comes from `com.adyen.threeds:adyen-3ds2@2.2.27`.

Google Pay delegates to Google Play Services Wallet, Cash App Pay to Pay Kit, Twint to its Android SDK, and WeChat Pay to Tencent's SDK. Their adapters and configuration are evidence for the Adyen integration boundary only; source presence does not prove merchant enablement, regional eligibility, device availability, or complete delegated behavior.

## Analytics and release boundary

Drop-in and Component analytics are enabled by default from the 5.x line. `AnalyticsLevel.NONE` suppresses Drop-in/Component events, while the implementation retains an initial setup level used to obtain a checkout-attempt identifier. Release `5.20.0` documents one change: compile and target SDK support moved to API 36. Broader SDK behavior on this page is accumulated baseline evidence and must not be attributed solely to that release.

## Related

- [[source-github-adyen-android]] - cumulative exact-SHA repository evidence
- [[changelog-github-adyen-android]] - package-qualified release ledger
- [[adyen-ios-sdk]] - independently versioned native iOS SDK
- [[adyen-react-native-sdk]] - wrapper baseline that pins Adyen Android `5.19.0`, not this page's newer `5.20.0`
- [[source-github-adyen-web]] - independently versioned browser SDK
- [[co-badged-cards]] - version-qualified dual-brand implementation evidence
- [[adyen]] - company and knowledge-status page

## Sources

- `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/manifest.json` - exact-SHA source capsule
- `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/files/README.md` - purpose, lifecycle, installation, and analytics defaults
- `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/files/drop-in/src/main/java/com/adyen/checkout/dropin/DropIn.kt` - Sessions and advanced Drop-in contracts
- `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/files/sessions-core/src/main/java/com/adyen/checkout/sessions/core/internal/data/api/SessionService.kt` - client Session operations
- `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/files/components-core/src/main/java/com/adyen/checkout/components/core/PaymentComponentData.kt` - payment request and server boundary
- `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/files/card/src/main/java/com/adyen/checkout/card/internal/ui/DefaultCardDelegate.kt` - card, encryption, installments, and dual-brand behavior
- `raw/github/adyen/adyen-android/releases/adyen-android/5.20.0/2026-08-01/release-notes.md` - API-level change
