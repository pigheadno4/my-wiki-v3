---
title: "PayPal Android SDK"
type: concept
category: technology
tags: [paypal, android, mobile, kotlin, card-payments, web-payments, vault, fraud-protection, payment-buttons, maven]
---

## PayPal Android SDK

The PayPal Mobile Android SDK enables merchants to accept PayPal, credit, and debit card payments in Android apps. Available via Maven Central.

Repo: <https://github.com/paypal/paypal-android>

## Version 3 Baseline

Latest ingested is `paypal-android@3.1.0` (`d100313f2247b512cedf6080bb7b6ecaada26d42`, delta 2026-10-16), following the additive `3.0.0` baseline below. It removes `TokenType`'s library-group restriction and includes the enum in the public API inventory. It also forwards optional `CoreConfig.bnCode` into shopper-session eligibility, fixes the card-vault demo's missing client initialization, and changes Magnes imports to the namespace accompanying the release-noted collision fix. The demo now supplies user action only through session creation, not its order payload. No new native Venmo API or live payment proof follows from these changes. Sources: [[source-github-paypal-android]], [[changelog-github-paypal-android]].

The approved full baseline `paypal-android@3.0.0` (`3540adff974abdc20371d66fe47748e4c5174592`, ingested 2026-10-16) adds a shopper-session-first checkout/vault lifecycle. Replace `paypal-web-payments` with `com.paypal.android:paypal-payments`, `PayPalWebCheckoutClient` with `PayPalClient`, and `Environment` / `CoreConfig.environment` with `CoreEnvironment` / `coreEnvironment`. Android SDK 23+ remains the declared minimum.

Call `createPayPalSession(tokenType, userIdentity, urlConfig, userAction)` before each `start(activity, orderId, callback)` or `vault(activity, setupTokenId, callback)` attempt. Prewarming returns immediately; launch awaits it and consumes the session. Missing or failed prewarming reports failure rather than silently opening legacy checkout. `PayPalResultCallback.onPayPalResult` reports presentation, not payment completion: retain `finishStart(intent)` / `finishVault(intent)` and server capture/authorization or setup-token exchange. `instanceState` preserves browser auth state, not the pending prewarm.

App switch requires server eligibility and an enabled, resolvable PayPal app meeting the implementation's version-code threshold; otherwise the returned checkout fallback URL is used. `ReturnToAppUrlConfig` supplies return/cancel App Links and a custom-scheme fallback. These code paths do not prove account enablement, verified return routing, or production checkout success.

> [!warning] Contradiction - version 3 documentation versus final API
> The `3.0.0` notes mention request-object/async migration alternatives that are absent from the final public API, and call `fallbackSchemeUrl` mandatory even though implementation accepts a nonblank return App Link without it. Use exact-version signatures and verify supported merchant return configuration; permissive validation is not an availability promise. Earlier v1/v2 examples below remain historical, not drop-in v3 code.

At `3.0.0`, the required `TokenType` is public Kotlin but marked `LIBRARY_GROUP`-restricted and omitted from the public API inventory. The retained card-vault demo also leaves its nullable `cardClient` uninitialized before `cardClient?.vault(...)`; this is a sample wiring defect, not proof the SDK's card vault API fails. See [[source-github-paypal-android]] and [[changelog-github-paypal-android]] for exact evidence and limitations. The v3 `Venmo.api` still exposes only `BuildConfig`, not a native Venmo integration.

`CoreConfig(clientId, merchantId, coreEnvironment, bnCode)` now requires both client and merchant IDs; `bnCode` remains optional. Do not reuse the one-ID v2 configuration example below for v3.

## Historical Version 2 Baseline

The approved GitHub baseline is `paypal-android@2.3.0` at SHA `d69a2fad7a96155e71f2681dc7cbfa9957fff544`. It supports Android SDK 23+, is written in Kotlin, and supports Kotlin and Java integrations. This version uses callback result types and explicit browser-return completion methods; the listener APIs summarized from older product pages are version 1 history.

## Reference Demo Baseline

The independent `paypal-examples/paypal-android-sdk-demo-app` baseline at `d1137d5` demonstrates a Jetpack Compose cart using SDK `2.3.0`. Its direct PayPal path creates an order on a merchant server, starts `PayPalWebCheckoutClient` with `PAYPAL`, persists `instanceState`, finishes the browser return, and then captures server-side. Its card path uses `SCA_WHEN_REQUIRED` but rejects `AuthorizationRequired`, so it is not a complete 3DS example.

The same app presents Payment Links as a separate hosted-browser option. It handles warm and cold App Link returns, but it trusts the return URI for UI completion and does not verify settlement. See [[source-github-paypal-android-sdk-demo-app]] and [[changelog-github-paypal-android-sdk-demo-app]].

## Version 2 Modules

| Module | Gradle artifact | Purpose |
| ------ | --------------- | ------- |
| `card-payments` | `com.paypal.android:card-payments` | Inline card fields in merchant UI |
| `paypal-web-payments` | `com.paypal.android:paypal-web-payments` | Browser-based PayPal checkout inside app |
| `payment-buttons` | `com.paypal.android:payment-buttons` | PayPal-branded buttons (PayPalButton, PayPalPayLater, PayPalCredit) |
| `fraud-protection` | `com.paypal.android:fraud-protection` | Device fingerprinting via PayPalDataCollector |

`PayPalNativePayments` was deprecated in version 1 and removed from version 2. The retained `Venmo` directory at `2.3.0` contains build metadata but no public integration API.

## Version 2 Core Pattern

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

The Messages Module is a separate standalone library: [paypal/paypal-messages-android](https://github.com/paypal/paypal-messages-android), with approved baseline `paypal-messages-android@1.3.0` at SHA `f1aa138cc6822cc11d68ac4bfdee3cf183aedbc2`. It promotes Pay Later and PayPal Credit but does not execute checkout payments.

On a separate untagged `develop` line, README commit `0424354` requires a Braintree account and Braintree SDK integration and says PPCP SDK integrations are unsupported. The direct comparison starts at historical SHA `1d2238c`, not the `1.3.0` release tree, and changes no implementation file.

Key API: `PayPalMessageView` (FrameLayout) for XML layouts; `PayPalComposableMessage` for Jetpack Compose. Config via `PayPalMessageConfig(data, style, viewStateCallbacks, eventsCallbacks)`.

> [!info] Availability
> Still in active development — the README recommends sandbox use until an official release. The development guide also says the Jetpack view does not currently work, so Compose demo/source presence is not readiness evidence.

Offer types: `PAY_LATER_SHORT_TERM`, `PAY_LATER_LONG_TERM`, `PAY_LATER_PAY_IN_1`, `PAYPAL_CREDIT_NO_INTEREST`.

The retained release/build metadata conflicts: GitHub identifies `1.3.0`, Gradle says `1.1.14`, and the checked-in POM says `1.1.10`; MIT and Apache-2.0 license evidence also conflict. Verify the live Maven coordinate before installation. At this exact SHA, the AppCompat modal maps Apply to the close callback, `setConfig()` omits environment, and activity callbacks are registered after launch.

See [[source-github-paypal-messages-android]] for the full evidence boundary and [[changelog-github-paypal-messages-android]] for release history.

The later untagged Messages demo commit `develop@aede075` changes Compose message containers from 40dp to 100dp and the XML wrapper from 80dp to 100dp to accommodate CCD2 disclaimers. It is a direct descendant of the retained `0424354` policy ref, not a new package release. The library and its Compose compatibility warnings are unchanged; larger demo containers do not establish a readiness fix or a universal sizing requirement. See [[source-github-paypal-messages-android]].

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
- [[changelog-github-paypal-android]] — package-qualified Android history through `3.1.0`, retaining v1/v2 and the full `3.0.0` baseline
- [[source-github-paypal-android-sdk-demo-app]] — Jetpack Compose PayPal, card, and hosted Payment Link checkout sample at `d1137d5`
- [[changelog-github-paypal-android-sdk-demo-app]] — commit-qualified demo baseline and retained limitations
- [[source-github-paypal-messages-android]] — GitHub paypal-messages-android: PayPalMessageConfig API, callbacks, Compose support, Android vs iOS differences
- [[changelog-github-paypal-messages-android]] — managed `1.3.0` release, cumulative stable history, and retained metadata conflicts
