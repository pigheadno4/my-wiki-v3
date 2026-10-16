---
title: "GitHub: paypal/paypal-ios"
type: source
date_ingested: 2026-04-13
date_updated: 2026-10-16
original_format: github-repo
raw_files:
  - "github/paypal/paypal-ios/snapshots/2026-10-16-de98414/manifest.json"
  - "github/paypal/paypal-ios/snapshots/2026-10-16-67e4a96/manifest.json"
  - "github/paypal/paypal-ios/snapshots/2026-10-16-fc69f40/manifest.json"
  - "github/paypal/paypal-ios/snapshots/2026-07-31-2008a6d/manifest.json"
  - "github-paypal-ios.md"
tags: [paypal, ios, swift, mobile, sdk, card-payments, web-payments, vault, fraud-protection, payment-buttons, swiftui, uikit, spm, cocoapods, github-repository]
---

## Overview

`paypal/paypal-ios` publishes PayPal's modular native iOS SDK. This cumulative page preserves the April 2026 review at commit `600a97a5f69ea6f44db3cf2f8b631276fd0152d8` and the full `paypal-ios@2.0.1` baseline at `2008a6de7c00a2ae53c669932d5fb19674c35b1e`, adding full `paypal-ios@3.0.0` at `fc69f404fa68b2c7336a684296543a67e0e809d5`. Older-version sections remain historical integration evidence.

The subsequent full `paypal-ios@3.1.0` baseline at `67e4a9635f8e3ff829221c6d64573590937d1a2f` adds the iOS 16 and risk-dependency migration, corrected action intent and revised app-switch eligibility behavior.

Delta `paypal-ios@3.1.1` at `de98414f5cf74dc3db2239a4828b4760ef391d20` forwards BN attribution into shopper-session context. Its later changelog marks `3.0.0` unsupported; the original notes and implementation findings remain preserved.

Repository: <https://github.com/paypal/paypal-ios>

## Evidence Boundary

- The `3.1.1` delta fully reads all nine changed retained files, affected prior source already read in the full cycle, release notes and cumulative wiki context; 153 unchanged paths are hash-verified. Its complete snapshot remains retained (162 files, 378,154 bytes). Generated files/diff are mechanically verified under explicit approval.
- The `3.1.0` full ingest reads all 162 retained files (376,418 bytes), release notes and cumulative wiki context, including all 151 unchanged source files. Generated manifests/inventories/duplicated diffs are mechanically verified under the same explicit approval. The external risk dependency is not collected or executed.
- The `3.0.0` full ingest reads all 162 retained files (375,722 bytes), assigned prior source and release evidence. Generated manifests, inventories and duplicated diffs are mechanically verified under explicit user approval. This is not a full upstream repository read; tests, binaries, project files, entitlements and Info.plist are outside the capsule.
- The `2.0.1` capsule contains 145 retained documentation, build, demo, public API, and implementation files totaling 281,036 bytes. Tests and fixtures are excluded by collection policy.
- This is a bounded public-source capsule, not a full repository mirror. Queries requiring excluded code need a supplemental immutable capsule tied to the exact SHA.
- The earlier source was manually selected. There is no automated file comparison from its SHA to `2.0.1`, so old findings are preserved as historical context rather than represented as a complete diff.
- Public enums and components establish SDK contracts, not merchant eligibility, country availability, account enablement, or production behavior.

## Grounding Excerpts

> "Replace delegate pattern with completion handlers and Swift concurrency"
>
> `raw/github/paypal/paypal-ios/snapshots/2026-07-31-2008a6d/files/CHANGELOG.md:15`

> "For 2.0.0 GA, these methods now use Result<SomeResult, CoreSDKError> in their completion blocks."
>
> `raw/github/paypal/paypal-ios/snapshots/2026-07-31-2008a6d/files/v2_MIGRATION_GUIDE.md:5-8`

> "In v2.0, cancellations (e.g., 3DS cancellations, PayPal web flow cancellations) are now returned as errors rather than as separate delegate methods."
>
> `raw/github/paypal/paypal-ios/snapshots/2026-07-31-2008a6d/files/v2_MIGRATION_GUIDE.md:19-20`

> "The PayPal iOS SDK supports a minimum deployment target of iOS 14+ and requires Xcode 15.0+ and macOS Ventura 13."
>
> `raw/github/paypal/paypal-ios/snapshots/2026-07-31-2008a6d/files/README.md:11`

> "Update `PayPalWebCheckoutClient.vault()` to recognize `cancel` path in deep link urls"
>
> `raw/github/paypal/paypal-ios/releases/paypal-ios/2.0.1/2026-07-31/release-notes.md:4`

## Package Status

| Package | Latest ingested release | Exact SHA | Evidence status |
| --- | --- | --- | --- |
| `paypal-ios` | `3.1.1` | `de98414f5cf74dc3db2239a4828b4760ef391d20` | Approved delta after full 3.0.0/3.1.0; earlier releases retained |

This reports wiki ingest progress, not the latest release published upstream.

## Version 3.1.1 Delta

### Grounding excerpts

- `bnCode: coreConfig.bnCode` - `raw/github/paypal/paypal-ios/snapshots/2026-10-16-de98414/files/Sources/PayPalPayments/APIRequests/CreateShopperSessionAPI.swift:94`
- `try container.encode(bnCode, forKey: .bnCode)` - `raw/github/paypal/paypal-ios/snapshots/2026-10-16-de98414/files/Sources/PayPalPayments/APIRequests/CreateShopperSessionVariables.swift:77`
- `DemoSettings.bnCode = trimmedBNCode.isEmpty ? nil : trimmedBNCode` - `raw/github/paypal/paypal-ios/snapshots/2026-10-16-de98414/files/Demo/Demo/DemoSettings/CustomEnvironmentView.swift:200`
- "This version is no longer supported. Please use version 3.1.0 instead." - `raw/github/paypal/paypal-ios/snapshots/2026-10-16-de98414/files/CHANGELOG.md:40`, referring to `3.0.0`.

### BN attribution and demo wiring

`CoreConfig.bnCode` existed before this patch; `3.1.1` specifically forwards it to the shopper-session API's experimentation context. The context gains optional `bnCode`, includes it in CodingKeys, and encodes explicit JSON null if nil rather than omitting it. This is additional request attribution context, not proof of server crediting, eligibility or a new checkout/vault method.

The DEBUG custom-environment screen adds BN input, trims whitespace on Save, and stores empty input as nil. `DemoSettings` persists the value separately in UserDefaults; CoreConfigManager forwards it into every constructed config. The Clear action only clears the environment fields/config: it does not clear `bnCode`, and its empty-state test ignores that field. Existing client instances are not shown being rebuilt just by changing settings. Do not describe the demo as production attribution management or complete reset behavior.

`PayPal.podspec` and SDK analytics constant advance to `3.1.1`. `CardClient` changes only whitespace (verified by whitespace-stripped equality), not approval/vault logic. iOS 16 minimum, exact risk dependency, session/action/routing and prior cautions remain unchanged; there is no new native Venmo API.

### Later support notice versus original release history

> [!warning] Version support and retrospective changelog attribution
> The cumulative changelog at `3.1.1` strikes out `3.0.0`, says it is unsupported and directs users to `3.1.0`. It also relocates the original v3 API/configuration descriptions under `3.1.0`. The immutable original `3.0.0` release record and source already contain those APIs; retain their original first-observed version and add this later support notice, rather than rewriting history. See [[paypal-ios-sdk]] and [[changelog-github-paypal-ios]].

This notice is evidence as of the collected `3.1.1` SHA, not a live upstream support-policy audit. No payment/dependency build or runtime execution was performed.

## Version 3.1.0 Full Baseline

### Grounding excerpts

- `platforms: [.iOS(.v16)],` - `raw/github/paypal/paypal-ios/snapshots/2026-10-16-67e4a96/files/Package.swift:8`
- `.package(url: "https://github.com/paypal/paypal-risk-ios", exact: "5.6.0")` - same Package.swift, line 33.
- `paymentType: userAction.externalPaymentType,` - `raw/github/paypal/paypal-ios/snapshots/2026-10-16-67e4a96/files/Sources/PayPalPayments/APIRequests/CreateShopperSessionAPI.swift:92`
- `paypalNativeAppInstalled: true,` - same raw session API, line 102.
- `return "COMMIT"` - `raw/github/paypal/paypal-ios/snapshots/2026-10-16-67e4a96/files/Sources/PayPalPayments/Models/PayPalUserAction.swift:33`

### Compatibility and dependency boundary

README, Package.swift and podspec consistently raise the minimum from iOS 14 to **iOS 16**. Swift 5.9+, Xcode 15+ and macOS Ventura 13 remain the README requirements; its Xcode 14.3+ demo sentence is still stale. This breaking minimum and dependency migration justify the user's full-ingest override despite the collector's contained-delta recommendation.

SPM now declares `https://github.com/paypal/paypal-risk-ios` **exactly `5.6.0`**, with product `PayPalRisk`; CocoaPods uses `PayPalRisk`, `5.6.0`. The vendored `PPRiskMagnes.xcframework` reference/binary target is removed. Wrapper source still imports `PPRiskMagnes` and preserves its collection calls. This proves dependency wiring, not dependency internals, successful resolution, binary contents or a runtime fraud-behavior change.

### Action intent and routing

`PayPalClient` now passes `userAction` to the session API, which requires `paymentType` and maps `.continue` -> `CONTINUE`, `.payNow` -> `PAY`, `.setupNow` -> `COMMIT`. This resolves the `3.0.0` hardcoded-PAY finding without rewriting that version's history.

> [!warning] Contradiction - action validation remains undocumented in implementation
> The `3.1.0` `PayPalUserAction` comment still promises `PayPalError.invalidUserActionError` for checkout with `.setupNow`; neither that error nor validation exists in the retained client. Correct intent forwarding does not prove enforced action compatibility. The same distinction is recorded in [[paypal-ios-sdk]].

`URLOpener`/UIApplication no longer expose `isPayPalAppInstalled()`. Session eligibility optimistically sends `paypalNativeAppInstalled: true`; installed-state analytics is nil. The client drops the local installed-app gate, but still requires server eligibility, redirect URL, shopper-session ID and constructed URL before attempting an OS Universal Link. Failure to open clears the pending app callback and falls back to browser auth. No server eligibility response or actual installed-app state was exercised.

### Reconfirmed integration baseline

The full read reconfirms all retained current modules and demo code, not only these eleven changes. Required merchant ID, public `PayPalSessionType`, structured identity hints, prewarm-per-attempt and callback-only PayPal ID APIs remain; CardClient retains callbacks/async APIs and 3DS. App returns use `handleReturnURL`; browser returns use SDK authentication callbacks. Capture/authorization and setup-token-to-payment-token exchange remain merchant-server responsibilities. The retained demo still uses `MERCHANT` and `ON_SUCCESS`, with no native Venmo or newly exposed funding selector.

Return binding, absent invalid-action error, optional-query browser URL construction, license metadata mismatch, stale demo toolchain statement and the card UpdateClientConfig log/continue behavior remain cautions. There is no upstream build, external dependency inspection or successful payment proof. Earlier version-specific knowledge below remains valid historical evidence.

## Version 3.0.0 Full Baseline

Historical baseline only: the later `3.1.1` changelog marks this release unsupported and points to `3.1.0`; its original API and implementation evidence below is retained.

### Grounding excerpts

- "`CoreConfig.init` now requires a `merchantID` parameter." - `raw/github/paypal/paypal-ios/snapshots/2026-10-16-fc69f40/files/v3_MIGRATION_GUIDE.md:9`
- "Whether this session is for a checkout or a vault-without-purchase flow." - `raw/github/paypal/paypal-ios/snapshots/2026-10-16-fc69f40/files/Sources/PayPalPayments/PayPalClient.swift:118`
- "Return and cancel deep-link URLs registered with PayPal." - same raw client, line 120.
- "A completion block invoked on the main thread with a `Result`:" - same raw client, line 164.
- `completion: @escaping (Result<PayPalCheckoutResult, CoreSDKError>) -> Void` - same raw client, line 169.

### Migration and requirements

| Version 2 | Version 3.0.0 |
| --- | --- |
| `PayPalWebPayments` | `PayPalPayments` |
| `PayPalWebCheckoutClient` | `PayPalClient` |
| `PayPalWebCheckoutResult` | `PayPalCheckoutResult` |
| `PayPalWebCheckoutFundingSource` | `PayPalCheckoutFundingSource` |
| `Environment` | `CoreEnvironment`; configuration label remains `environment:` |
| `CoreConfig(clientID:environment:)` | Requires `merchantID:`; optional `bnCode:` |
| `start(request:)` / `vault(PayPalVaultRequest)` | Session prewarm followed by `start(orderID:completion:)` / `vault(setupTokenID:completion:)` |

The new PayPal entry points are callback-only; the removed v2 request/async overloads are not retained under the new signatures. Card approval/vault keep Result callbacks and async/await. The public session enum is `PayPalSessionType.checkout` / `.vaultWithoutPurchase`; `TokenType` is internal, unlike Android's required public-facing token type. Legacy PatchCCO eligibility types are removed. The short v3 migration guide documents configuration only, so source reading is needed for the wider migration.

The `3.0.0` README, Package.swift and podspec retain iOS 14+, Swift 5.9+, Xcode 15+ (README also names macOS Ventura 13). README demo instructions still say Xcode 14.3+, a stale inconsistency. FraudProtection still uses vendored `PPRiskMagnes`; the binary itself is not retained. UIKit/SwiftUI buttons and the other modules remain.

### Checkout and vault lifecycle

1. Retain a `PayPalClient` initialized with client ID, merchant ID and environment.
2. Call `createPayPalSession(sessionType:userIdentity:urlConfig:userAction:)`. It starts an asynchronous shopper-session task, without needing an order ID yet. Optional identity is an existing shopper-session ID or email/structured `PayPalPhoneNumber(countryCode:nationalNumber:)` hints.
3. Create the order or setup token on the merchant server. The demo overlaps this with prewarming, then calls `start(orderID:completion:)` or `vault(setupTokenID:completion:)`; those methods await the session task.
4. Missing prewarm returns `sessionNotStartedError`. Failed session creation returns `sessionNotCreatedError`; this is not the browser-fallback branch. The task is cleared after scheduling launch, so a new attempt needs a new prewarm. No durable process-restoration API is established.
5. For app switching, `3.0.0` checks installed PayPal app, server `appSwitchEligible`, redirect URL and shopper-session ID, then opens a Universal Link with `universalLinksOnly`. Ineligibility or failure to open routes to browser authentication. PayPal browser checkout/vault surfaces `updateClientConfig` failures instead of continuing.
6. Route validated app returns to `handleReturnURL`. Checkout needs nonempty `token` and `PayerID`; vault needs `approval_token_id` and `approval_session_id`; a path containing `/cancel` is cancellation. Browser return is handled by `ASWebAuthenticationSession` and its callback. Do not copy Android's separate `finishStart` / `finishVault` API into this iOS flow.
7. A checkout result is buyer approval, not capture. Authorize/capture on the merchant server; after vault approval exchange the setup token for a payment token and verify its customer association. Identity hints do not authorize charging a saved credential.

The demo routes `.onOpenURL` to its retained client; it does not establish production Universal Link/AASA configuration because entitlements/Info.plist are excluded. Its order request supplies return/cancel URLs and `nativeApp`; vault setup uses `appSwitchContext.nativeApp`, `usageType: MERCHANT`, and the same return host. Save-during-purchase adds `ON_SUCCESS`. Its API client distinguishes sandbox shorthand routes/camelCase bodies from a live REST proxy/snake_case body contract; those sample endpoints are not merchant production infrastructure.

### Version-specific cautions and boundaries

> [!warning] Contradiction - user-action contract at 3.0.0
> `createPayPalSession` accepts `userAction` but only records it in analytics; the session request uses its default `PAY`. `PayPalUserAction` documentation describes an `invalidUserActionError` for `.setupNow` in checkout, but that error and enforcement are absent from the retained implementation. Do not present the documented validation as implemented. See [[paypal-ios-sdk]].

- The return handler does not bind host/scheme/order to an expected transaction internally, and even an unrelated forwarded URL clears session/analytics state. Merchant URL routing and server-side result checks remain necessary; no exploit or live failure was tested.
- The renamed funding enum still contains only `.paypal`, `.paylater`, `.paypalCredit`; the public `start(orderID:completion:)` has no funding selector. The demo's legacy funding-button method accepts `funding` but does not pass it to the client. A retained enum or button is not proof this new call can force Pay Later/Credit, and no native Venmo case is added.
- Card approval still logs an UpdateClientConfig error and continues, unlike the fail-closed PayPal browser path. A 3DS-attempt flag is not authentication/liability-shift proof: the result comments require server retrieval of order/setup-token details. SDK approval still requires server completion.
- LSAT OAuth requests use form encoding and Basic client authentication; GraphQL requests merge the resulting bearer token. Android's separately recorded header discrepancy must not be copied into this iOS finding.
- Non-JSON error messages now include status, URL and response body; analytics explicitly uses the live tracking endpoint even for sandbox payment configuration. These are retained-code facts, not evidence of successful telemetry delivery.
- `PayPalClient.makeCheckoutURL` / `makeVaultCheckoutURL` append query items through an optional existing query array. A queryless fallback base may therefore omit expected items; this is a static code concern, not reproduced checkout behavior. The separate `PayPalCheckoutURLBuilder` for app switching initializes its query array explicitly.
- LICENSE/podspec mismatch and `MERCHANT` versus older `PLATFORM` vault guidance persist. The new API does not resolve merchant eligibility, geography, licensing or policy questions.

## Version 2 Modules and Requirements

| Module | Purpose |
| --- | --- |
| `CorePayments` | Shared configuration, networking, analytics, errors, and web authentication |
| `CardPayments` | Card order approval and card vault-without-purchase, including 3DS |
| `PayPalWebPayments` | Browser-based PayPal checkout and PayPal vault approval |
| `PaymentButtons` | UIKit buttons and SwiftUI wrappers for PayPal, Pay Later, and PayPal Credit |
| `FraudProtection` | Device data collection through the bundled Magnes binary |

The package supports Swift Package Manager and CocoaPods. The `2.0.1` README requires iOS 14+, Swift 5.9+, Xcode 15+, and macOS Ventura 13.

## Version 2 API Model

Version 2 removes the payment and vault delegate protocols used by version 1. Version 2 operations expose `Result<Success, CoreSDKError>` completion handlers plus Swift concurrency overloads:

```swift
cardClient.approveOrder(request: request) { result in ... }
let cardResult = try await cardClient.approveOrder(request: request)

cardClient.vault(vaultRequest) { result in ... }
let vaultResult = try await cardClient.vault(vaultRequest)

payPalClient.start(request: request) { result in ... }
let checkoutResult = try await payPalClient.start(request: request)

payPalClient.vault(vaultRequest) { result in ... }
let vaultResult = try await payPalClient.vault(vaultRequest)
```

`CoreSDKError` is equatable, and domain errors such as `CardError`, `PayPalError`, and `NetworkingError` are public. Cancellation is represented by errors such as `CardError.threeDSecureCanceledError`, `PayPalError.checkoutCanceledError`, and `PayPalError.vaultCanceledError`.

## Card Payments and 3DS

`CardClient.approveOrder` confirms the card payment source against `/v2/checkout/orders/{id}/confirm-payment-source`. A `PAYER_ACTION_REQUIRED` response launches web authentication for 3DS, after which the merchant server must still capture or authorize the order.

`CardResult` contains the order ID, optional status, and whether 3DS authentication was attempted. SCA preferences remain `.scaWhenRequired` and `.scaAlways`. The demo shows the complete server-create, client-approve, and server-capture-or-authorize sequence.

## Vault Without Purchase

### Cards

`CardClient.vault(CardVaultRequest)` updates a server-created setup token with card data. It can launch 3DS and returns `CardVaultResult` with the setup token ID, status, and 3DS-attempted flag. The demo then upgrades the setup token to a payment token on the merchant server.

### PayPal

`PayPalWebCheckoutClient.vault(PayPalVaultRequest(setupTokenID:))` launches browser approval and returns `PayPalVaultResult(tokenID, approvalSessionID)`. The retained demo creates the PayPal setup token with `usage_type: MERCHANT`, then creates a payment token after approval.

This demo evidence conflicts with older iOS purchase-later documentation that uses `usage_type: PLATFORM`. The correct value may depend on merchant/platform context; do not silently normalize the two examples.

## PayPal Checkout and the `2.0.1` Fix

`PayPalWebCheckoutClient.start` runs an order-based PayPal web checkout. Release `2.0.1` fixes deep-link cancellation recognition in both checkout and vault flows: checkout recognizes `opType=cancel`, while vault recognizes the cancellation path. These are cancellation-result fixes, not new payment methods.

## Native Funding Sources and Venmo Boundary

At `2.0.1`, `PayPalWebCheckoutFundingSource` contains only `.paypalCredit`, `.paylater`, and `.paypal`. `PaymentButtonFundingSource` contains only PayPal, Pay Later, and PayPal Credit. Neither public enum exposes Venmo.

Therefore this repository does not establish a native PayPal iOS Venmo integration. A stale `PaymentButtonSize.mini` comment mentions `.venmo`, but there is no corresponding enum case or button implementation, so the comment is not capability evidence. A merchant requiring Venmo in a native app needs a separately supported web/JavaScript SDK flow or another eligible SDK, with current product and account eligibility verified independently.

The earlier source predicted that `.paylater` would be renamed in the next major version. The same `NEXT_MAJOR_VERSION` comment and lowercase `.paylater` case remain in `2.0.1`; the rename has not occurred.

## Payment Buttons

The module exposes `PayPalButton`, `PayPalCreditButton`, and `PayPalPayLaterButton`, with UIKit implementations and SwiftUI `Representable` wrappers. Configuration covers color, edges, size, label, and funding source. Button availability does not prove buyer or merchant eligibility.

## Fraud Protection and Privacy

`PayPalDataCollector.collectDeviceData()` uses Magnes and returns JSON containing a correlation ID. Its implementation maintains a device identifier in Keychain. The FraudProtection privacy manifest declares device-ID collection for app functionality and marks it as not linked to the user and not used for tracking.

CardPayments declares payment information and physical address collection for app functionality. The SDK also sends analytics containing app, device, package, environment, order, and setup-token context.

## Historical Version 1 Context

The April 2026 review documented the older delegate APIs: `CardDelegate`, `CardVaultDelegate`, `PayPalWebCheckoutDelegate`, and `PayPalVaultDelegate`. It also established `CardClient(config:)`, card vault support, demo merchant-server orchestration, UIKit/SwiftUI buttons, and the lowercase `.paylater` case. These remain useful for maintaining 1.x integrations but are not current 2.x signatures.

## Evidence Discrepancies

- The repository `LICENSE` contains Apache License 2.0 text, while `PayPal.podspec` declares `MIT`. Treat the package license metadata as inconsistent and obtain authoritative licensing guidance before relying on either field.
- The current demo uses `usage_type: MERCHANT` for PayPal vault without purchase; older iOS product guidance uses `PLATFORM`.
- Public API presence is not production eligibility evidence.

## Related

- Company: [[paypal]]
- Concept: [[paypal-ios-sdk]]
- Vault: [[paypal-vault]]
- Android counterpart: [[source-github-paypal-android]]
- Release history: [[changelog-github-paypal-ios]]

## Raw Sources

- [3.1.1 snapshot](raw/github/paypal/paypal-ios/snapshots/2026-10-16-de98414/manifest.json), [release record](raw/github/paypal/paypal-ios/releases/paypal-ios/3.1.1/2026-10-16/manifest.json), [notes](raw/github/paypal/paypal-ios/releases/paypal-ios/3.1.1/2026-10-16/release-notes.md), [3.1.0 to 3.1.1 comparison](tracking/github/repos/paypal/paypal-ios/comparisons/paypal-ios/3.1.0--3.1.1/comparison.md)
- [3.1.1 session API](raw/github/paypal/paypal-ios/snapshots/2026-10-16-de98414/files/Sources/PayPalPayments/APIRequests/CreateShopperSessionAPI.swift), [encoded context](raw/github/paypal/paypal-ios/snapshots/2026-10-16-de98414/files/Sources/PayPalPayments/APIRequests/CreateShopperSessionVariables.swift), [demo settings](raw/github/paypal/paypal-ios/snapshots/2026-10-16-de98414/files/Demo/Demo/DemoSettings/CustomEnvironmentView.swift), [cumulative changelog/support notice](raw/github/paypal/paypal-ios/snapshots/2026-10-16-de98414/files/CHANGELOG.md)
- [3.1.0 snapshot](raw/github/paypal/paypal-ios/snapshots/2026-10-16-67e4a96/manifest.json), [release record](raw/github/paypal/paypal-ios/releases/paypal-ios/3.1.0/2026-10-16/manifest.json), [release notes](raw/github/paypal/paypal-ios/releases/paypal-ios/3.1.0/2026-10-16/release-notes.md), [3.0.0 to 3.1.0 comparison](tracking/github/repos/paypal/paypal-ios/comparisons/paypal-ios/3.0.0--3.1.0/comparison.md)
- [3.1.0 package](raw/github/paypal/paypal-ios/snapshots/2026-10-16-67e4a96/files/Package.swift), [client](raw/github/paypal/paypal-ios/snapshots/2026-10-16-67e4a96/files/Sources/PayPalPayments/PayPalClient.swift), [session API](raw/github/paypal/paypal-ios/snapshots/2026-10-16-67e4a96/files/Sources/PayPalPayments/APIRequests/CreateShopperSessionAPI.swift), [action mapping](raw/github/paypal/paypal-ios/snapshots/2026-10-16-67e4a96/files/Sources/PayPalPayments/Models/PayPalUserAction.swift)
- [3.0.0 snapshot manifest](raw/github/paypal/paypal-ios/snapshots/2026-10-16-fc69f40/manifest.json) - full retained capsule, exact SHA `fc69f40`
- [3.0.0 release record](raw/github/paypal/paypal-ios/releases/paypal-ios/3.0.0/2026-10-16/manifest.json) and [release notes](raw/github/paypal/paypal-ios/releases/paypal-ios/3.0.0/2026-10-16/release-notes.md)
- [2.0.1 to 3.0.0 comparison](tracking/github/repos/paypal/paypal-ios/comparisons/paypal-ios/2.0.1--3.0.0/comparison.md) - generated, mechanically verified
- [3.0.0 PayPalClient](raw/github/paypal/paypal-ios/snapshots/2026-10-16-fc69f40/files/Sources/PayPalPayments/PayPalClient.swift), [session API](raw/github/paypal/paypal-ios/snapshots/2026-10-16-fc69f40/files/Sources/PayPalPayments/APIRequests/CreateShopperSessionAPI.swift), and [v3 migration](raw/github/paypal/paypal-ios/snapshots/2026-10-16-fc69f40/files/v3_MIGRATION_GUIDE.md)
- [3.0.0 demo checkout](raw/github/paypal/paypal-ios/snapshots/2026-10-16-fc69f40/files/Demo/Demo/PayPalPayments/PayPalWebViewModel/PayPalWebViewModel.swift) and [vault](raw/github/paypal/paypal-ios/snapshots/2026-10-16-fc69f40/files/Demo/Demo/PayPalVault/PayPalVaultViewModel/PayPalVaultViewModel.swift)
- `raw/github/paypal/paypal-ios/snapshots/2026-07-31-2008a6d/manifest.json` - exact-SHA bounded source capsule
- `raw/github/paypal/paypal-ios/releases/paypal-ios/2.0.1/2026-07-31/manifest.json` - package-qualified release record
- `raw/github/paypal/paypal-ios/releases/paypal-ios/2.0.1/2026-07-31/release-notes.md` - exact `2.0.1` release notes
- `raw/github/paypal/paypal-ios/snapshots/2026-07-31-2008a6d/files/CHANGELOG.md` - cumulative upstream history
- `raw/github/paypal/paypal-ios/snapshots/2026-07-31-2008a6d/files/v2_MIGRATION_GUIDE.md` - version 1 to version 2 migration
- `raw/github/paypal/paypal-ios/snapshots/2026-07-31-2008a6d/files/Package.swift` - products, dependencies, and platform metadata
- `raw/github/paypal/paypal-ios/snapshots/2026-07-31-2008a6d/files/Sources/CardPayments/CardClient.swift` - card approval and vault APIs
- `raw/github/paypal/paypal-ios/snapshots/2026-07-31-2008a6d/files/Sources/PayPalWebPayments/PayPalWebCheckoutClient.swift` - PayPal checkout and vault APIs
- `raw/github/paypal/paypal-ios/snapshots/2026-07-31-2008a6d/files/Sources/PayPalWebPayments/PayPalWebCheckoutFundingSource.swift` - native web-checkout funding-source enum
- `raw/github/paypal/paypal-ios/snapshots/2026-07-31-2008a6d/files/Sources/PaymentButtons/PaymentButtonFundingSource.swift` - native button funding-source enum
- `raw/github-paypal-ios.md` - legacy manually selected capsule pointer
