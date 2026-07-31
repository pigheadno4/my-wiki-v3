---
title: "GitHub: paypal/paypal-android"
type: source
date_ingested: 2026-04-13
date_updated: 2026-07-31
original_format: github-repo
raw_files:
  - "github/paypal/paypal-android/snapshots/2026-07-31-d69a2fa/manifest.json"
  - "github-paypal-android.md"
tags: [paypal, android, kotlin, mobile, sdk, card-payments, web-payments, vault, fraud-protection, payment-buttons, venmo, github-repository]
---

## Overview

`paypal/paypal-android` publishes PayPal's modular native Android SDK. This cumulative page preserves the April 2026 review at commit `2685f88374fa09c17e5af6f3ea88ba622d940901` and adds the approved full baseline for `paypal-android@2.3.0` at commit `d69a2fad7a96155e71f2681dc7cbfa9957fff544`.

Repository: <https://github.com/paypal/paypal-android>

## Evidence Boundary

- The `2.3.0` capsule contains 242 documentation, API-signature, build, implementation, demo, GraphQL, and resource files totaling 567,836 bytes. Tests, fixtures, CI, binaries, and tooling were excluded by collection policy.
- This is a bounded public-source capsule, not a complete repository mirror. A query requiring excluded implementation needs an immutable supplement tied to the exact SHA.
- There is no automated comparison from the earlier manually reviewed SHA to `2.3.0`; version 1 findings are preserved as historical context, while the cumulative changelog and migration guide establish the intervening major-version changes.
- Public classes and modules prove code contracts, not merchant eligibility, country availability, account enablement, or production behavior.

## Grounding Excerpts

> "The PayPal Android SDK is available for Android SDK 23+."
>
> `raw/github/paypal/paypal-android/snapshots/2026-07-31-d69a2fa/files/README.md:10-11`

> "Capture instance state for later restoration. This can be useful for recovery during a process kill."
>
> `raw/github/paypal/paypal-android/snapshots/2026-07-31-d69a2fa/files/CardPayments/src/main/java/com/paypal/android/cardpayments/CardClient.kt:50-55`

> "callback for receiving result asynchronously"
>
> `raw/github/paypal/paypal-android/snapshots/2026-07-31-d69a2fa/files/CardPayments/src/main/java/com/paypal/android/cardpayments/CardClient.kt:66-72`

> "Use start(activity, request, callback) instead."
>
> `raw/github/paypal/paypal-android/snapshots/2026-07-31-d69a2fa/files/PayPalWebPayments/src/main/java/com/paypal/android/paypalwebpayments/PayPalWebCheckoutClient.kt:69-81`

> "PAYPAL will launch the web checkout for a one-time PayPal Checkout flow"
>
> `raw/github/paypal/paypal-android/snapshots/2026-07-31-d69a2fa/files/PayPalWebPayments/src/main/java/com/paypal/android/paypalwebpayments/PayPalWebCheckoutFundingSource.kt:20-23`

## Package Status

| Package | Latest ingested release | Exact SHA | Evidence status |
| --- | --- | --- | --- |
| `paypal-android` | `2.3.0` | `d69a2fad7a96155e71f2681dc7cbfa9957fff544` | Approved full baseline; earlier reviewed SHA retained |

This table reports wiki ingest progress, not the latest release currently published upstream.

## Modules and Requirements

| Module | Purpose and current boundary |
| --- | --- |
| `CorePayments` | Shared configuration, networking, GraphQL, analytics, errors, browser-switch request codes, and session storage |
| `CardPayments` | Card order confirmation and card vault-without-purchase, including explicit 3DS challenge presentation and completion |
| `PayPalWebPayments` | Browser-based PayPal checkout and PayPal vault approval |
| `PaymentButtons` | Android views for PayPal, Pay Later, and PayPal Credit buttons |
| `FraudProtection` | Device-data collection through the bundled Magnes 5.5.1 binary |
| `Venmo` | Build marker only in the retained `2.3.0` capsule; no public integration API |

The README requires Android SDK 23+ and supports Kotlin and Java integrations. The build targets and compiles against API 35. Modules are independently added from Maven Central, including `com.paypal.android:card-payments` and `com.paypal.android:paypal-web-payments`.

`PayPalNativePayments` was deprecated in version 1 and removed in version 2. It is historical migration context, not a current module.

## Version 2 Lifecycle Model

Version 2 removes the old `ApproveOrderListener`, `CardVaultListener`, `PayPalWebCheckoutListener`, and vault-listener state from the clients. Current flows return sealed results through callbacks or explicit finish methods:

```kotlin
cardClient.approveOrder(cardRequest) { result -> ... }
cardClient.vault(cardVaultRequest) { result -> ... }

paypalClient.start(activity, checkoutRequest) { result -> ... }
val checkoutResult = paypalClient.finishStart(intent)
val vaultResult = paypalClient.finishVault(intent)
```

Both `CardClient` and `PayPalWebCheckoutClient` expose `instanceState` plus `restore(instanceState)` for process-death recovery. A successful browser presentation stores auth state internally; the no-auth-state overloads of the finish methods use and then clear that state after a terminal result.

## Card Payments and 3DS

`CardClient(context, CoreConfig)` confirms a card payment source for a server-created order. `approveOrder(request, callback)` yields:

- `CardApproveOrderResult.Success(orderId, status)` when no payer action is needed;
- `AuthorizationRequired(CardAuthChallenge)` when the API supplies a payer-action link; or
- `Failure(PayPalSDKError)`.

For authorization-required results, call `presentAuthChallenge(activity, challenge)`, wait for the deep link, then call `finishApproveOrder(intent)`. Its final result distinguishes `Success`, `Failure`, `Canceled`, and `NoResult`. The same explicit present/finish model applies to card vaulting through `finishVault(intent)`.

`CardRequest` carries the order ID, card, return URL, and `SCA_WHEN_REQUIRED` or `SCA_ALWAYS`. After client-side confirmation, the merchant server still captures or authorizes the order. The demo passes the PayPal client metadata ID on that server completion call.

## Card Vault Without Purchase

`CardClient.vault(CardVaultRequest, CardVaultCallback)` attaches card details to a server-created setup token. A direct success returns setup-token status and whether 3DS was attempted; an authorization-required result follows the browser challenge path. The demo then upgrades the setup token to a payment token through the merchant server.

The SDK sends the card and setup-token variables through its retained `UpdateVaultSetupToken` GraphQL operation. That implementation detail does not remove the merchant's responsibility to create setup and payment tokens server-side.

## PayPal Web Checkout and `2.3.0`

`PayPalWebCheckoutClient(context, CoreConfig, urlScheme)` launches browser checkout for a `PayPalWebCheckoutRequest(orderId, fundingSource)`. The public funding-source enum contains only `PAYPAL`, `PAY_LATER`, and `PAYPAL_CREDIT`.

Release `2.3.0` adds `start(activity, request, PayPalWebStartCallback)`. This overload first updates client configuration asynchronously, launches the browser switch, and returns its presentation result on the main dispatcher. The synchronous two-argument overload is deprecated. After the deep link returns, `finishStart(intent)` distinguishes success, cancellation, failure, and no matching result; the merchant server then captures or authorizes the order.

The cumulative history also records `2.0.1` cancellation parsing fixes, `2.1.2` internal auth-state storage and finish overloads, and `2.2.0` migration from `ComponentActivity` to plain `Activity` parameters.

## PayPal Vault Without Purchase

`vault(activity, PayPalWebVaultRequest(setupTokenId))` opens PayPal's approval page. `finishVault(intent)` returns the approval-session ID on success and separately reports failure, cancellation, or no result. The demo creates a PayPal setup token on its server, performs browser approval, and then upgrades the setup token to a payment token.

The deprecated two-argument `PayPalWebVaultRequest(setupTokenId, approveVaultHref)` remains in the public API; current code builds the approval URL from the setup-token ID.

## Native Venmo Boundary

At `2.3.0`, `PayPalWebCheckoutFundingSource` has no Venmo case, PaymentButtons contains no Venmo button, the demo exposes no Venmo flow, and `Venmo.api` contains only `BuildConfig`. Therefore this repository does not establish a native PayPal Android Venmo integration.

> [!warning] Contradiction - Venmo funding source
> Older PayPal Android guidance referenced Venmo as a PayPalWebPayments funding source. The collected `2.3.0` public API and implementation expose only PayPal, Pay Later, and PayPal Credit, while the separate `Venmo` directory has no callable API. Do not infer Venmo support from the directory name; verify a separately supported product path and merchant eligibility.

## Payment Buttons

The module exposes `PayPalButton`, `PayLaterButton`, and `PayPalCreditButton`. Configuration includes size, shape, corner radius, labels, and supported brand colors. These are static Android views whose click listeners start merchant-defined flows; button presence does not prove funding eligibility.

## Fraud Protection

`PayPalDataCollector(CoreConfig)` returns device data through `collectDeviceData(context, request)`. `PayPalDataCollectorRequest` controls location-consent and additional-data inputs. The demo collects this value before capture or authorization and sends it as `PayPal-Client-Metadata-Id`. The retained module bundles Magnes 5.5.1.

## Historical Version 1 Context

The April 2026 review documented the version 1 `ApproveOrderListener` and PayPal web listener patterns, automatic observer completion, and the deprecated native-payments migration. Those findings remain useful for maintaining older integrations but are not current `2.3.0` signatures. The earlier findings that `CardClient` takes an Android `Context`, clients preserve instance state, and merchant-server order/token endpoints are required remain valid.

## Evidence Discrepancies

- The retained `v2_MIGRATION_GUIDE.md` illustrates the v2 architecture using immediate result expressions for card operations, while the current `2.3.0` source and API signatures require `CardApproveOrderCallback` and `CardVaultCallback`. Use the release's API signatures for exact current method calls.
- Older product source pages still show version 1 listeners. Treat them as historical documentation unless separately recollected for version 2.
- Public APIs and demo routes do not establish merchant availability or regional eligibility.

## Related

- Company: [[paypal]]
- Concept: [[paypal-android-sdk]]
- Vault: [[paypal-vault]]
- iOS counterpart: [[source-github-paypal-ios]]
- Release history: [[changelog-github-paypal-android]]

## Raw Sources

- `raw/github/paypal/paypal-android/snapshots/2026-07-31-d69a2fa/manifest.json` - exact-SHA bounded source capsule
- `raw/github/paypal/paypal-android/releases/paypal-android/2.3.0/2026-07-31/manifest.json` - package-qualified release record
- `raw/github/paypal/paypal-android/releases/paypal-android/2.3.0/2026-07-31/release-notes.md` - exact `2.3.0` release notes
- `raw/github/paypal/paypal-android/snapshots/2026-07-31-d69a2fa/files/CHANGELOG.md` - cumulative upstream history
- `raw/github/paypal/paypal-android/snapshots/2026-07-31-d69a2fa/files/v2_MIGRATION_GUIDE.md` - version 1 to version 2 migration
- `raw/github/paypal/paypal-android/snapshots/2026-07-31-d69a2fa/files/CardPayments/src/main/java/com/paypal/android/cardpayments/CardClient.kt` - card approval, vault, 3DS, and state APIs
- `raw/github/paypal/paypal-android/snapshots/2026-07-31-d69a2fa/files/PayPalWebPayments/src/main/java/com/paypal/android/paypalwebpayments/PayPalWebCheckoutClient.kt` - checkout, vault, callback, finish, and state APIs
- `raw/github/paypal/paypal-android/snapshots/2026-07-31-d69a2fa/files/PayPalWebPayments/src/main/java/com/paypal/android/paypalwebpayments/PayPalWebCheckoutFundingSource.kt` - current native funding-source enum
- `raw/github/paypal/paypal-android/snapshots/2026-07-31-d69a2fa/files/Venmo/api/Venmo.api` - empty public Venmo surface boundary
- `raw/github-paypal-android.md` - legacy manually selected capsule pointer
