---
title: "PayPal Android SDK"
type: concept
category: technology
tags: [paypal, android, mobile, kotlin, card-payments, web-payments, vault, fraud-protection, payment-buttons, maven]
---

## PayPal Android SDK

The PayPal Mobile Android SDK enables merchants to accept PayPal, credit, and debit card payments in Android apps. Available via Maven Central.

Repo: <https://github.com/paypal/paypal-android>

## Current Baseline

The approved GitHub baseline is `paypal-android@2.3.0` at SHA `d69a2fad7a96155e71f2681dc7cbfa9957fff544`. It supports Android SDK 23+, is written in Kotlin, and supports Kotlin and Java integrations. This version uses callback result types and explicit browser-return completion methods; the listener APIs summarized from older product pages are version 1 history.

## Available Modules

| Module | Gradle artifact | Purpose |
| ------ | --------------- | ------- |
| `card-payments` | `com.paypal.android:card-payments` | Inline card fields in merchant UI |
| `paypal-web-payments` | `com.paypal.android:paypal-web-payments` | Browser-based PayPal checkout inside app |
| `payment-buttons` | `com.paypal.android:payment-buttons` | PayPal-branded buttons (PayPalButton, PayPalPayLater, PayPalCredit) |
| `fraud-protection` | `com.paypal.android:fraud-protection` | Device fingerprinting via PayPalDataCollector |

`PayPalNativePayments` was deprecated in version 1 and removed from version 2. The retained `Venmo` directory at `2.3.0` contains build metadata but no public integration API.

## Core Pattern

All modules share a `CoreConfig`:

```kotlin
val config = CoreConfig("CLIENT_ID", environment = Environment.SANDBOX)
```

Each module creates its own client from `CoreConfig` (e.g. `CardClient`, `PayPalWebCheckoutClient`).

## Card Payments

Server creates order -> client builds `Card` + `CardRequest` -> `cardClient.approveOrder(request, callback)` -> handle `Success`, `Failure`, or `AuthorizationRequired` -> present and finish any 3DS challenge -> server captures or authorizes.

SCA controlled via `sca` param: `SCA_WHEN_REQUIRED` (default) or `SCA_ALWAYS`.

Version 2 manually balances a successful `presentAuthChallenge(activity, challenge)` with `finishApproveOrder(intent)` or `finishVault(intent)` after the deep link returns. `instanceState` and `restore()` preserve the internal auth state across process death.

## Web Payments

Browser-based checkout supports `PAYPAL`, `PAY_LATER`, and `PAYPAL_CREDIT`. In `2.3.0`, use `start(activity, request, callback)`; the synchronous two-argument overload is deprecated. After the browser returns, pass the intent to `finishStart(intent)` and handle `Success`, `Canceled`, `Failure`, or `NoResult`.

PayPal vault without purchase remains a separate `vault(activity, PayPalWebVaultRequest)` path, completed with `finishVault(intent)`.

## Historical Native Payments

`PayPalNativePayments` was deprecated in July 2024 and removed in version 2. Existing integrations should migrate to `paypal-web-payments`.

## Fraud Protection

`PayPalDataCollector.collectDeviceData()` — collect `clientMetadataId` before each payment. Pass to server for inclusion in payment request. Requires user consent for location data.

## iOS Equivalent

See [[source-github-paypal-ios]] for the current iOS SDK baseline. iOS version 2 uses completion `Result` values and async/await rather than the older `CardDelegate`; it also supports SwiftUI button wrappers and does not require Android `Context` objects.

## Relevant Companies

- [[paypal]] — PayPal company overview

> [!warning] Contradiction - Venmo funding source
> Older product guidance references Venmo as a `PayPalWebPayments` funding source, but `PayPalWebCheckoutFundingSource` at `paypal-android@2.3.0` only defines `PAYPAL`, `PAY_LATER`, and `PAYPAL_CREDIT`. The retained `Venmo` module exposes only `BuildConfig`, so this repository does not establish a native Venmo integration. Verify a separately supported Venmo product path and merchant eligibility before offering it.

## Messages Module (Pay Later Messaging)

The Messages Module is a separate standalone library: [paypal/paypal-messages-android](https://github.com/paypal/paypal-messages-android) v1.3.0. Available via Maven Central.

Key API: `PayPalMessageView` (FrameLayout) for XML layouts; `PayPalComposableMessage` for Jetpack Compose. Config via `PayPalMessageConfig(data, style, viewStateCallbacks, eventsCallbacks)`.

> [!info] Availability
> Still in active development — README recommends sandbox use only until GA.

Offer types: `PAY_LATER_SHORT_TERM`, `PAY_LATER_LONG_TERM`, `PAY_LATER_PAY_IN_1`, `PAYPAL_CREDIT_NO_INTEREST`.

See [[source-github-paypal-messages-android]] for full API reference.

## PayPal Wallet Vault (Save During Purchase)

Uses `PayPalWebCheckoutClient` - the same client as non-vault web payments, with vault payload added:

- Create Order with `payment_source.paypal.attributes.vault.store_in_vault: ON_SUCCESS`
- `start(activity, request, callback)` launches the browser; payer approves; returns through the configured URL scheme
- `finishStart(intent)` resolves the returned deep link before server capture or authorization
- Capture response contains `vault.id` + `customer.id` — store both
- Returning payer: pass `vault.id` as payment source in next Create Order

See [[source-paypal-save-paypal-android-sdk]] for full detail.

## PayPal Wallet Vault Without Purchase (Save for Later)

Uses `PayPalWebCheckoutClient.vault()` - the same client as web payments, with a vault-specific request:

- Module: `paypal-web-payments`
- `PayPalWebVaultRequest(setupTokenId)` — not `PayPalWebRequest(orderId)`
- `vault(activity, request)` returns browser-presentation success or failure
- `finishVault(intent)` returns `Success`, `Failure`, `Canceled`, or `NoResult`
- Setup token uses `usage_type: PLATFORM` (vs `MERCHANT` for during-purchase)
- Setup token response: `PAYER_ACTION_REQUIRED`

See [[source-paypal-save-paypal-purchase-later-android-sdk]] for full detail.

## Card Vault Without Purchase (Save for Later)

Uses `CardClient.vault()` - separate from `approveOrder()`:

- `CardVaultRequest(setupTokenID, card)` — setup token from server, card from payer input
- `CardVaultCallback` receives `Success`, `Failure`, or `AuthorizationRequired`
- after a challenge, `finishVault(intent)` returns the final setup-token result
- Returning customer: `customer.id` passed in setup token request body (not in Create Order)
- Setup token response status: `CREATED` (no payer action required for cards)

See [[source-paypal-save-cards-purchase-later-android-sdk]] for full detail.

## Card Vault (Save During Purchase)

Extends the base card payments integration. Key additions:

- Compose `Checkbox` grouped with card fields for save-card opt-in
- Create Order with `payment_source.card.attributes.vault.store_in_vault: ON_SUCCESS`
- Returning payer: pass `customer.id` in `payment_source.card.attributes.customer.id` (not via token request)
- `CardClient.approveOrder(request, callback)` confirms the card source; vault-on-success happens server-side after capture
- RTAU (real-time account updater) available to keep saved cards current

See [[source-paypal-save-cards-android-sdk]] for full detail.

## Sources

- [[source-paypal-android-card-payments]] — Full Android SDK integration guide
- [[source-paypal-save-paypal-purchase-later-android-sdk]] — PayPal Wallet vault without purchase: `PayPalWebCheckoutClient.vault()`, `usage_type: PLATFORM`, `PAYER_ACTION_REQUIRED` setup token
- [[source-paypal-save-cards-purchase-later-android-sdk]] — historical version 1 card-vault guide; current callback and finish behavior is recorded here
- [[source-paypal-save-paypal-android-sdk]] — PayPal Wallet vault during purchase: `PayPalWebCheckoutClient`, deep link, `vault.id` for returning payers
- [[source-paypal-save-cards-android-sdk]] — Card vault during purchase: Compose checkbox, returning payer pattern, APPROVED/VAULTED, RTAU
- [[source-github-paypal-android]] — GitHub source: CardClient constructor, instance state, Demo ViewModels, server API contract
- [[changelog-github-paypal-android]] — package-qualified Android SDK release history through `2.3.0`
- [[source-github-paypal-messages-android]] — GitHub paypal-messages-android: PayPalMessageConfig API, callbacks, Compose support, Android vs iOS differences
