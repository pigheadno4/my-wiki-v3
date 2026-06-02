---
title: "PayPal Android SDK"
type: concept
category: technology
tags: [paypal, android, mobile, kotlin, card-payments, web-payments, native-payments, fraud-protection, payment-buttons, maven]
---

## PayPal Android SDK

The PayPal Mobile Android SDK enables merchants to accept PayPal, credit, and debit card payments in Android apps. Available via Maven Central.

Repo: <https://github.com/paypal/paypal-android>

## Available Modules

| Module | Gradle artifact | Purpose |
| ------ | --------------- | ------- |
| `card-payments` | `com.paypal.android:card-payments` | Inline card fields in merchant UI |
| `paypal-web-payments` | `com.paypal.android:paypal-web-payments` | Browser-based PayPal checkout inside app |
| `paypal-native-payments` | `com.paypal.android:paypal-native-payments` | **DEPRECATED** — in-app PayPal paysheet |
| `payment-buttons` | `com.paypal.android:payment-buttons` | PayPal-branded buttons (PayPalButton, PayPalPayLater, PayPalCredit) |
| `fraud-protection` | `com.paypal.android:fraud-protection` | Device fingerprinting via PayPalDataCollector |

## Core Pattern

All modules share a `CoreConfig`:

```kotlin
val config = CoreConfig("CLIENT_ID", environment = Environment.SANDBOX)
```

Each module creates its own client from `CoreConfig` (e.g. `CardClient`, `PayPalWebCheckoutClient`).

## Card Payments

Server creates order → client builds `Card` + `CardRequest` → `cardClient.approveOrder()` → `ApproveOrderListener` → server captures/authorizes.

SCA controlled via `sca` param: `SCA_WHEN_REQUIRED` (default) or `SCA_ALWAYS`.

Requires `myapp://` custom URL scheme in `AndroidManifest.xml` for 3DS browser switch.

## Web Payments (Recommended over Native)

Browser-based checkout. Supports `PAYPAL`, `PAY_LATER`, `PAYPAL_CREDIT` funding sources. Same AndroidManifest setup required.

## Native Payments (Deprecated)

`PayPalNativePayments` deprecated July 2024, EOL July 2025. Migrate to `paypal-web-payments`.

## Fraud Protection

`PayPalDataCollector.collectDeviceData()` — collect `clientMetadataId` before each payment. Pass to server for inclusion in payment request. Requires user consent for location data.

## iOS Equivalent

See [[source-paypal-ios-card-payments]] for the iOS SDK integration guide. Key differences: iOS `CardClient` takes no `Context`; uses `CardDelegate` protocol instead of `ApproveOrderListener`; SwiftUI support via `PayPalButton.Representable()`; fraud protection requires no location consent flag.

## Relevant Companies

- [[paypal]] — PayPal company overview

> [!warning] Contradiction — Venmo funding source
> The official docs reference Venmo as a `PayPalWebPayments` funding source, but `PayPalWebCheckoutFundingSource` in the source code (see [[source-github-paypal-android]]) only defines `PAYPAL`, `PAY_LATER`, and `PAYPAL_CREDIT` — no `VENMO`. Venmo may be handled via the separate `Venmo` module.

## Messages Module (Pay Later Messaging)

The Messages Module is a separate standalone library: [paypal/paypal-messages-android](https://github.com/paypal/paypal-messages-android) v1.3.0. Available via Maven Central.

Key API: `PayPalMessageView` (FrameLayout) for XML layouts; `PayPalComposableMessage` for Jetpack Compose. Config via `PayPalMessageConfig(data, style, viewStateCallbacks, eventsCallbacks)`.

> [!info] Availability
> Still in active development — README recommends sandbox use only until GA.

Offer types: `PAY_LATER_SHORT_TERM`, `PAY_LATER_LONG_TERM`, `PAY_LATER_PAY_IN_1`, `PAYPAL_CREDIT_NO_INTEREST`.

See [[source-github-paypal-messages-android]] for full API reference.

## PayPal Wallet Vault (Save During Purchase)

Uses `PayPalWebCheckoutClient` — same client as non-vault web payments, with vault payload added:

- Create Order with `payment_source.paypal.attributes.vault.store_in_vault: ON_SUCCESS`
- `PayPalWebCheckoutClient` launches browser; payer approves; returns via `deepLinkUrlScheme`
- Capture response contains `vault.id` + `customer.id` — store both
- Returning payer: pass `vault.id` as payment source in next Create Order

See [[source-paypal-save-paypal-android-sdk]] for full detail.

## PayPal Wallet Vault Without Purchase (Save for Later)

Uses `PayPalWebCheckoutClient.vault()` — same client as web payments, vault-specific method:

- Module: `paypal-web-payments`
- `PayPalWebVaultRequest(setupTokenId)` — not `PayPalWebRequest(orderId)`
- `vaultListener` with `onPayPalWebVaultSuccess/Failure/Canceled`
- Setup token uses `usage_type: PLATFORM` (vs `MERCHANT` for during-purchase)
- Setup token response: `PAYER_ACTION_REQUIRED`

See [[source-paypal-save-paypal-purchase-later-android-sdk]] for full detail.

## Card Vault Without Purchase (Save for Later)

Uses `CardClient.vault()` — not `approveOrder()`:

- `CardVaultRequest(setupTokenID, card)` — setup token from server, card from payer input
- `CardVaultListener.onVaultSuccess(result: CardVaultResult)` → `result.setupTokenID` → server upgrades to payment token
- Returning customer: `customer.id` passed in setup token request body (not in Create Order)
- Setup token response status: `CREATED` (no payer action required for cards)

See [[source-paypal-save-cards-purchase-later-android-sdk]] for full detail.

## Card Vault (Save During Purchase)

Extends the base card payments integration. Key additions:

- Compose `Checkbox` grouped with card fields for save-card opt-in
- Create Order with `payment_source.card.attributes.vault.store_in_vault: ON_SUCCESS`
- Returning payer: pass `customer.id` in `payment_source.card.attributes.customer.id` (not via token request)
- `CardClient.approveOrder()` unchanged — vault happens server-side after capture
- RTAU (real-time account updater) available to keep saved cards current

See [[source-paypal-save-cards-android-sdk]] for full detail.

## Sources

- [[source-paypal-android-card-payments]] — Full Android SDK integration guide
- [[source-paypal-save-paypal-purchase-later-android-sdk]] — PayPal Wallet vault without purchase: `PayPalWebCheckoutClient.vault()`, `usage_type: PLATFORM`, `PAYER_ACTION_REQUIRED` setup token
- [[source-paypal-save-cards-purchase-later-android-sdk]] — Card vault without purchase: `CardClient.vault()`, `CardVaultListener`, `CREATED` setup token status
- [[source-paypal-save-paypal-android-sdk]] — PayPal Wallet vault during purchase: `PayPalWebCheckoutClient`, deep link, `vault.id` for returning payers
- [[source-paypal-save-cards-android-sdk]] — Card vault during purchase: Compose checkbox, returning payer pattern, APPROVED/VAULTED, RTAU
- [[source-github-paypal-android]] — GitHub source: CardClient constructor, instance state, Demo ViewModels, server API contract
- [[source-github-paypal-messages-android]] — GitHub paypal-messages-android: PayPalMessageConfig API, callbacks, Compose support, Android vs iOS differences
