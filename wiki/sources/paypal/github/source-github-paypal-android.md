---
title: "GitHub: paypal/paypal-android"
type: source
date_ingested: 2026-04-13
date_updated: 2026-10-16
original_format: github-repo
raw_files:
  - "github/paypal/paypal-android/snapshots/2026-10-16-d100313/manifest.json"
  - "github/paypal/paypal-android/snapshots/2026-10-16-3540adf/manifest.json"
  - "github/paypal/paypal-android/snapshots/2026-07-31-d69a2fa/manifest.json"
  - "github-paypal-android.md"
tags: [paypal, android, kotlin, mobile, sdk, card-payments, web-payments, vault, fraud-protection, payment-buttons, venmo, github-repository]
---

## Overview

`paypal/paypal-android` publishes PayPal's modular native Android SDK. This cumulative page preserves the April 2026 review at commit `2685f88374fa09c17e5af6f3ea88ba622d940901` and adds the approved full baseline for `paypal-android@2.3.0` at commit `d69a2fad7a96155e71f2681dc7cbfa9957fff544`.

The additive full `paypal-android@3.0.0` baseline at `3540adff974abdc20371d66fe47748e4c5174592` introduces a session-first PayPal client, app-switch routing and breaking API/module changes. The earlier baselines below remain available for version-specific queries.

Repository: <https://github.com/paypal/paypal-android>

## Evidence Boundary

- The `3.1.0` delta read all 17 changed retained files, release evidence and the affected `3.0.0` source already fully read in the preceding serial cycle. Its 277-file snapshot totals 683,872 bytes, with 260 unchanged files and one removed demo enum. Generated inventories/diff were mechanically verified under separate explicit approval; unchanged history was preserved.
- The `3.0.0` full ingest read all 278 retained files (682,258 bytes), assigned removed/prior source and release notes. User-approved mechanical checks cover generated inventories and the duplicated comparison diff; both snapshots' hashes/sizes and packet/comparison hashes passed. This is not a full upstream-repository read or build/payment execution.
- The v3 capsule omits variant-specific `CoreEnvironment` and fraud environment-mapping implementations under `src/debug` / `src/release`, the shopper-session GraphQL resource, and the embedded Magnes binary. Public API/source establish contracts, not those omitted implementation details. Exact-SHA supplements are needed for deeper claims.
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
| `paypal-android` | `3.1.0` | `d100313f2247b512cedf6080bb7b6ecaada26d42` | Approved delta after full 3.0 baseline; v2/v1 retained |

This table reports wiki ingest progress, not the latest release currently published upstream.

## Version 3.1.0 Delta

Published 2026-10-06; the upstream changelog labels 2026-10-05. Collected and ingested 2026-10-16, after completing the full `3.0.0` cycle.

- **Required enum made public-facing:** `TokenType.kt` removes `@RestrictTo(LIBRARY_GROUP)` and its import; `CorePayments.api` adds `ORDER_ID`, `VAULT_ID` and `BILLING_TOKEN`. This resolves the specific `3.0.0` API-accessibility issue without replacing the session-first lifecycle.
- **Partner attribution reaches session eligibility:** `PayPalClient` passes `coreConfig.bnCode` through session params into the serializable experimentation context. The field already existed in CoreConfig/analytics at `3.0.0`; the new fact is forwarding into this session request, not first-ever BN-code support. Demo settings add a BN-code field, but excluded repository/variant wiring prevents proving persistence or consumption of that UI field end to end.
- **Card-vault demo fixed:** it now assigns `cardClient = CardClient(applicationContext, buildCoreConfig())` immediately before `vault`, retaining the instance for challenge completion. This fixes the null-client wiring identified above; it does not establish process-death recovery or sandbox success.
- **User-action ownership simplified in the demo:** `UserActionSelected` and its order-model/property/mapping are removed. The merchant-order sample still sends funding selection but no longer user action; `createPayPalSession(..., userAction)` remains. This is a sample change, not removal of the public Orders REST field.
- **Magnes collision fix boundary:** notes report replacing the embedded JAR to avoid symbol collisions, and `PayPalDataCollector` imports move from `lib.android.paypal.com.magnessdk` to `lib.android.com.paypal.magnessdk`. The JAR and variant environment mapping are not retained, so exact binary behavior, version upgrade and coexistence success are not verified. The unchanged Gradle filename alone cannot prove an unchanged binary.

The return-URL validation discrepancy and LSAT-header construction caution remain in the collected code: relevant helpers are hash-unchanged. No new native Venmo surface, automatic returning-buyer payment, capture method or merchant enablement is established.

### Delta Grounding

> "enum class TokenType {"
>
> `raw/github/paypal/paypal-android/snapshots/2026-10-16-d100313/files/CorePayments/src/main/java/com/paypal/android/corepayments/model/TokenType.kt:3`

> "bnCode = coreConfig.bnCode,"
>
> `raw/github/paypal/paypal-android/snapshots/2026-10-16-d100313/files/PayPalPayments/src/main/java/com/paypal/android/paypalpayments/PayPalClient.kt:444`

> "cardClient = CardClient(applicationContext, buildCoreConfig())"
>
> `raw/github/paypal/paypal-android/snapshots/2026-10-16-d100313/files/Demo/src/main/java/com/paypal/android/ui/vaultcard/VaultCardViewModel.kt:136`

> "import lib.android.com.paypal.magnessdk.MagnesSDK"
>
> `raw/github/paypal/paypal-android/snapshots/2026-10-16-d100313/files/FraudProtection/src/main/java/com/paypal/android/fraudprotection/PayPalDataCollector.kt:7`

## Version 3.0.0 Integration Contract

The artifact changes from `com.paypal.android:paypal-web-payments` to `com.paypal.android:paypal-payments`; imports move from `paypalwebpayments` to `paypalpayments`. Construct `PayPalClient(context, CoreConfig(...))` without a URL-scheme argument. `Environment` becomes `CoreEnvironment`, configured with `CoreConfig.coreEnvironment`. Android minimum 23, compile/target 35, Kotlin 1.9.24 and Java toolchain 17 remain declared in the retained build files.

The final public flow is:

```kotlin
val config = CoreConfig("CLIENT_ID", "MERCHANT_ID", coreEnvironment = CoreEnvironment.SANDBOX)
val client = PayPalClient(context, config)
val urls = ReturnToAppUrlConfig(
    returnAppUrl = "https://merchant.example/paypal/success",
    cancelAppUrl = "https://merchant.example/paypal/cancel",
    fallbackSchemeUrl = "com.example.merchant"
)
client.createPayPalSession(TokenType.ORDER_ID, null, urls, PayPalUserAction.CONTINUE)
// After the merchant server creates the order:
client.start(activity, orderId) { presentation -> /* handle launch failure */ }
// On the browser/app return, handle finishStart(intent), then finalize server-side.
```

This illustrates the retained signatures, not a runnable complete Activity or a tested integration. Handle success, failure, cancellation and unrelated intents, configure verified links/intent filters, persist browser state, and keep secrets/order creation/capture on the server. `3.0.0` restricts the required `TokenType` as described below.

V3 `CoreConfig` requires both `clientId` and `merchantId`; optional `bnCode` carries partner attribution. The one-ID v2 constructor example is not a v3 configuration.

### Prewarm, Launch and Return

- `createPayPalSession(tokenType, userIdentity, urlConfig, userAction)` returns immediately and starts a background shopper-session fetch with context token `ppcp_android`; it does not require the order ID yet. `start()` / `vault()` await that fetch.
- Each launch consumes the deferred session, including the failure path. Prewarm again for a subsequent attempt. Missing prewarm produces `SESSION_NOT_CREATED`; fetch failure produces `SESSION_CREATION_FAILED`, not an automatic legacy-checkout fallback.
- `PayPalResultCallback.onPayPalResult` replaces the web-specific callback; its success means presentation, not buyer approval or capture. Call `finishStart(intent)` / `finishVault(intent)` on return and then complete the order or token exchange server-side.
- No stored auth state yields `null`; a nonmatching intent with state may yield `NoResult`. Terminal results clear state. `instanceState` / `restore` preserve auth state only, not the prewarm Deferred.
- `PayPalUserIdentity` accepts an existing shopper-session ID, email or structured `PayPalPhoneNumber(countryCode, nationalNumber)`. This is not a stored payment token or a returning-buyer charge authorization.
- `ORDER_ID` launches with `token`; `VAULT_ID` uses `approval_session_id`; `BILLING_TOKEN` uses `ba_token`. User action maps `CONTINUE` to `CONTINUE`, `PAY_NOW` to `PAY`, and `SETUP_NOW` to `COMMIT` in the session request.

### App Switch and Return Routing

The launcher uses the shopper response's `redirectUrl` only when server app-switch eligibility and local PayPal-app checks both pass; otherwise it uses `checkoutFallbackUrl`. Local checks require the enabled PayPal package, a resolvable PayPal App Link and strict `versionCode > 1_160_090_132L`. A nearby comment's build threshold differs, so use the literal condition for exact code analysis. These are routing checks, not account or country eligibility proof.

With a fallback scheme, App Link return is selected only when the merchant app handles its return URL by default and either PayPal app switch or a listed compatible browser is available. Otherwise a custom scheme is chosen. Without a fallback, a nonblank return App Link is accepted without that handler probe. Custom-scheme success/cancel routes use `://x-callback-url/paypal-sdk/paypal-checkout/success` or `/cancel`, carrying original return/cancel query parameters. The neutral browser probe avoids treating PayPal's verified domain as a browser check.

> [!warning] Contradiction - release notes versus final v3 implementation
> Notes call `fallbackSchemeUrl` mandatory, but `PayPalClient.isValid()` accepts a nonblank return App Link OR fallback scheme. Notes also suggest request-object and `startAsync()` / `vaultAsync()` alternatives absent from the final retained public API. Follow exact release signatures; permissive code validation does not establish supported production configuration. Historical migration guides retained in this tree still describe older native/v2 clients, not a v3 integration recipe. The same warning is recorded in [[paypal-android-sdk]].

### Checkout, Vault, Cards and Fraud

`PayPalCheckoutFundingSource` remains PayPal, Pay Later and PayPal Credit, with no Venmo case. Unlike the removed checkout request's funding argument, the v3 demo passes its choice into the merchant-created order's experience context. The demo also supplies user action there; keep it aligned with session configuration. Sample camelCase server DTOs are not the direct REST wire schema.

For save-without-purchase, prewarm `VAULT_ID`, call `vault(activity, setupTokenId, callback)`, then `finishVault(intent)` and server-side setup-token exchange. The demo's setup token uses `MERCHANT`; older `PLATFORM` documentation remains separately qualified in [[paypal-vault]]. Purchase-with-vault uses server-owned order `ON_SUCCESS` attributes and normal order approval/finalization.

Card approval/vault retain callback results and explicit 3DS present/finish handling. V3 removes deprecated finish overloads taking explicit auth state and removes public presentation `authState`. A return or `didAttemptThreeDSecureAuthentication` flag alone is not payment completion or liability-shift proof. Fraud collection retains `PayPalDataCollectorRequest`, removes deprecated overloads and `setLogging`, uses application context and per-install GUID, and returns an empty string on Magnes invalid input. The build still names Magnes 5.5.1 at this release.

### Version 3.0.0 Source Cautions

- **Public API restriction:** required `TokenType` is a public Kotlin enum annotated `@RestrictTo(LIBRARY_GROUP)`, omitted from `CorePayments.api`. Do not describe it as Kotlin `internal` or claim a reproduced compiler failure.
- **Demo wiring defect:** `VaultCardViewModel` declares a nullable `cardClient` but never assigns it before `cardClient?.vault(...)`. Its state changes to Loading without that call or callback. Other methods' temporary fallback clients do not initialize it. This is a sample defect, not evidence the SDK card-vault implementation is broken.
- **Request-construction discrepancy:** `AuthenticationSecureTokenServiceAPI` supplies form content type and Basic credentials on `APIRequest`; `RestClient` instead rebuilds headers using its default Basic client-ID encoding and JSON POST content type, without merging those request headers. This is a code-level inconsistency, not a verified provider rejection. The separate GraphQL client does merge additional headers.
- **No native Venmo API:** the retained v3 `Venmo.api` still contains only `BuildConfig`; no Venmo button/checkout flow is established by that directory.

### Version 3 Grounding Excerpts

> "Pre-warms the shopper session in the background. Must be called before [start] or [vault]."
>
> `raw/github/paypal/paypal-android/snapshots/2026-10-16-3540adf/files/PayPalPayments/src/main/java/com/paypal/android/paypalpayments/PayPalClient.kt:102`

> "@RestrictTo(RestrictTo.Scope.LIBRARY_GROUP)"
>
> `raw/github/paypal/paypal-android/snapshots/2026-10-16-3540adf/files/CorePayments/src/main/java/com/paypal/android/corepayments/model/TokenType.kt:5`

> "val returnToAppStrategy = if (fallbackSchemeUrl.isBlank()) {"
>
> `raw/github/paypal/paypal-android/snapshots/2026-10-16-3540adf/files/CorePayments/src/main/java/com/paypal/android/corepayments/usecase/GetReturnToAppStrategyUseCase.kt:67`

> "private var cardClient: CardClient? = null"
>
> `raw/github/paypal/paypal-android/snapshots/2026-10-16-3540adf/files/Demo/src/main/java/com/paypal/android/ui/vaultcard/VaultCardViewModel.kt:49`

## Version 2 Modules and Requirements

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

- `raw/github/paypal/paypal-android/snapshots/2026-10-16-d100313/manifest.json` - exact 3.1.0 source capsule
- `raw/github/paypal/paypal-android/releases/paypal-android/3.1.0/2026-10-16/manifest.json` - package-qualified release identity
- `raw/github/paypal/paypal-android/releases/paypal-android/3.1.0/2026-10-16/release-notes.md` - enum accessibility and Magnes collision-fix intent
- `tracking/github/repos/paypal/paypal-android/comparisons/paypal-android/3.0.0--3.1.0/comparison.json` - bounded comparison
- `raw/github/paypal/paypal-android/snapshots/2026-10-16-d100313/files/CorePayments/src/main/java/com/paypal/android/corepayments/model/TokenType.kt` - unrestricted enum
- `raw/github/paypal/paypal-android/snapshots/2026-10-16-d100313/files/CorePayments/api/CorePayments.api` - public enum signature
- `raw/github/paypal/paypal-android/snapshots/2026-10-16-d100313/files/PayPalPayments/src/main/java/com/paypal/android/paypalpayments/PayPalClient.kt` - BN-code input forwarding and retained session lifecycle
- `raw/github/paypal/paypal-android/snapshots/2026-10-16-d100313/files/CorePayments/src/main/java/com/paypal/android/corepayments/api/CreateShopperSessionWithAppSwitchEligibilityAPI.kt` - BN-code eligibility variables
- `raw/github/paypal/paypal-android/snapshots/2026-10-16-d100313/files/Demo/src/main/java/com/paypal/android/ui/vaultcard/VaultCardViewModel.kt` - initialized vault client
- `raw/github/paypal/paypal-android/snapshots/2026-10-16-d100313/files/Demo/src/main/java/com/paypal/android/usecase/CreateOrderUseCase.kt` - order payload without user action
- `raw/github/paypal/paypal-android/snapshots/2026-10-16-d100313/files/FraudProtection/src/main/java/com/paypal/android/fraudprotection/PayPalDataCollector.kt` - relocated imports
- `raw/github/paypal/paypal-android/snapshots/2026-10-16-3540adf/manifest.json` - complete retained v3.0 source capsule
- `raw/github/paypal/paypal-android/releases/paypal-android/3.0.0/2026-10-16/manifest.json` - exact release identity, published 2026-08-19 (upstream changelog labels 2026-08-18)
- `raw/github/paypal/paypal-android/releases/paypal-android/3.0.0/2026-10-16/release-notes.md` - breaking changes and migration wording
- `tracking/github/repos/paypal/paypal-android/comparisons/paypal-android/2.3.0--3.0.0/comparison.json` - classified retained/upstream comparison inventory
- `raw/github/paypal/paypal-android/snapshots/2026-10-16-3540adf/files/PayPalPayments/src/main/java/com/paypal/android/paypalpayments/PayPalClient.kt` - session, checkout, vault and completion lifecycle
- `raw/github/paypal/paypal-android/snapshots/2026-10-16-3540adf/files/CorePayments/src/main/java/com/paypal/android/corepayments/model/TokenType.kt` - restricted required enum
- `raw/github/paypal/paypal-android/snapshots/2026-10-16-3540adf/files/CorePayments/src/main/java/com/paypal/android/corepayments/common/DeviceInspector.kt` - local app-switch eligibility
- `raw/github/paypal/paypal-android/snapshots/2026-10-16-3540adf/files/CorePayments/src/main/java/com/paypal/android/corepayments/usecase/GetReturnToAppStrategyUseCase.kt` - return strategy
- `raw/github/paypal/paypal-android/snapshots/2026-10-16-3540adf/files/CorePayments/src/main/java/com/paypal/android/corepayments/RestClient.kt` - request-header construction
- `raw/github/paypal/paypal-android/snapshots/2026-10-16-3540adf/files/CorePayments/src/main/java/com/paypal/android/corepayments/api/AuthenticationSecureTokenServiceAPI.kt` - token-request input headers
- `raw/github/paypal/paypal-android/snapshots/2026-10-16-3540adf/files/Demo/src/main/java/com/paypal/android/ui/vaultcard/VaultCardViewModel.kt` - card-vault demo wiring caution
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
