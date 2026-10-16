---
title: "PayPal iOS SDK"
type: concept
category: technology
tags: [paypal, ios, mobile, swift, card-payments, web-payments, fraud-protection, payment-buttons, swiftui, uikit, spm, cocoapods, orders-api, 3d-secure, vault]
---

## PayPal iOS SDK

The PayPal iOS SDK provides native Swift modules for cards, PayPal checkout, PayPal-branded buttons, vault approval, and device data collection. The latest ingested package is `paypal-ios@3.1.1`; this is wiki ingest status, not a claim about the latest upstream release. Version 1/2 guidance below remains historical.

Repository: <https://github.com/paypal/paypal-ios>

## Version 3 Session-First Integration

At `3.1.1`, optional `CoreConfig.bnCode` is forwarded into `ShopperSessionExperimentationContext` and encoded as `bnCode` (explicit null when nil). The demo adds trimmed BN input and UserDefaults persistence, then passes it through CoreConfigManager. This is attribution-context wiring, not a new payment method, eligibility guarantee or proof of attribution credit. Its Clear action does not reset the separately stored BN code.

> [!warning] Version support and history
> The cumulative CHANGELOG retained at `3.1.1` marks `3.0.0` unsupported and directs users to `3.1.0`; it also moves earlier v3 release descriptions under `3.1.0`. Original `3.0.0`/`3.1.0` notes and exact source snapshots remain separate historical evidence. Do not use the later changelog rearrangement to change when code first appeared. See [[source-github-paypal-ios]], [[changelog-github-paypal-ios]].

The subsequent full `3.1.0` baseline requires **iOS 16+**, retaining Swift 5.9+/Xcode 15+ in the README. It fixes session payment-type forwarding: `.continue` -> `CONTINUE`, `.payNow` -> `PAY`, `.setupNow` -> `COMMIT`. This resolves the hardcoded-PAY defect below, not the still-unimplemented invalid-action error documented in `PayPalUserAction`.

At `3.1.0`, local installed-app detection is removed: the eligibility request optimistically sends `paypalNativeAppInstalled: true`, while analytics sets installed-state to nil. The SDK still requires server eligibility/redirect/session data before attempting a Universal Link, with browser fallback if opening fails. This is not proof the app is installed. FraudProtection now depends on external `paypal/paypal-risk-ios` exactly `5.6.0` (SPM product/pod `PayPalRisk`) instead of a vendored binary; dependency internals remain uncollected. The full source recheck retains the session-per-attempt, callback-only PayPal and separate server-finalization boundaries. Source/history: [[source-github-paypal-ios]], [[changelog-github-paypal-ios]].

The full `paypal-ios@3.0.0` baseline renames `PayPalWebPayments` to `PayPalPayments`, `PayPalWebCheckoutClient` to `PayPalClient`, and `Environment` to `CoreEnvironment`. `CoreConfig(clientID:environment:merchantID:bnCode:)` requires the merchant ID; BN code is optional. Its README/SPM/podspec retain iOS 14+, Swift 5.9+ and Xcode 15+.

Call `createPayPalSession(sessionType:userIdentity:urlConfig:userAction:)` with `.checkout` or `.vaultWithoutPurchase`, then `start(orderID:completion:)` or `vault(setupTokenID:completion:)` using a merchant-server-created identifier. These PayPal APIs expose completion handlers, not the removed v2 request/async overloads. Card APIs retain Result and async/await. Prewarming is consumed per launch attempt; it is not durable process-restoration state.

In `3.0.0`, app switching requires installed-app detection, server eligibility and valid redirect/session data. Failure to open the eligible Universal Link falls back to browser authentication. Session creation failure instead returns an error. Forward validated app-return URLs to `handleReturnURL`; the browser path completes through its authentication callback. Merchant-server capture/authorization or payment-token exchange remains separate. Email/structured-phone hints or an existing shopper-session ID are not saved-payment credentials.

> [!warning] Contradiction - version 3.0.0 action intent
> The public API accepts `userAction` and its comments describe action-specific behavior, but the retained session request does not forward that argument and defaults to `PAY`. The documented `invalidUserActionError` is absent from the retained error/API implementation. Do not infer enforced `.setupNow` validation. See [[source-github-paypal-ios]] and [[changelog-github-paypal-ios]].

The renamed funding enum still contains only `.paypal`, `.paylater` and `.paypalCredit`; the public `start` no longer accepts the old request's funding-source argument. Native Venmo support is not added. See [[source-github-paypal-ios]] for exact-SHA evidence and demo limitations.

## Version 2 Requirements and Modules

| Module | Purpose |
| --- | --- |
| `CorePayments` | Configuration, networking, analytics, errors, and web authentication |
| `CardPayments` | Card order approval, 3DS, and card vault without purchase |
| `PayPalWebPayments` | Browser-based PayPal checkout and PayPal vault approval |
| `PaymentButtons` | PayPal, Pay Later, and PayPal Credit buttons for UIKit and SwiftUI |
| `FraudProtection` | Device data collection through Magnes |

The package supports Swift Package Manager and CocoaPods. The `2.0.1` source requires iOS 14+, Swift 5.9+, Xcode 15+, and macOS Ventura 13.

## Version 2 Shared Configuration

```swift
let config = CoreConfig(clientID: "CLIENT_ID", environment: .sandbox)
let cardClient = CardClient(config: config)
let payPalClient = PayPalWebCheckoutClient(config: config)
let dataCollector = PayPalDataCollector(config: config)
```

Unlike Android, the iOS `CardClient` does not take an Android-style context or activity.

## Version 2 Result Model

Version 2 replaces the version 1 delegate APIs with `Result<Success, CoreSDKError>` completion handlers and async/await overloads.

```swift
cardClient.approveOrder(request: request) { result in
    switch result {
    case .success(let cardResult):
        // Capture or authorize on the merchant server.
    case .failure(let error):
        // Handle CoreSDKError, including cancellation.
    }
}

let checkoutResult = try await payPalClient.start(request: request)
```

Cancellation is an error in v2, not a separate delegate callback:

- card 3DS: `CardError.threeDSecureCanceledError`
- PayPal checkout: `PayPalError.checkoutCanceledError`
- PayPal vault: `PayPalError.vaultCanceledError`

`CoreSDKError` is equatable. `CardError`, `PayPalError`, and `NetworkingError` are public for domain-specific handling.

## Card Payments

The server creates an order, the app builds `Card` and `CardRequest`, and `CardClient.approveOrder` confirms the card payment source. If PayPal returns `PAYER_ACTION_REQUIRED`, the SDK presents 3DS authentication. The merchant server must still capture or authorize after SDK approval.

```swift
let request = CardRequest(orderID: orderID, card: card, sca: .scaWhenRequired)
let result = try await cardClient.approveOrder(request: request)
```

`CardResult` includes the order ID, optional status, and whether 3DS was attempted. SCA options are `.scaWhenRequired` and `.scaAlways`.

## Version 2 PayPal Web Checkout

```swift
let request = PayPalWebCheckoutRequest(orderID: orderID, fundingSource: .paypal)
let result = try await payPalClient.start(request: request)
```

Release `2.0.1` corrects cancellation recognition in deep-link returns for both checkout and PayPal vault flows.

### Funding-source boundary

At `2.0.1`, `PayPalWebCheckoutFundingSource` exposes only `.paypal`, `.paylater`, and `.paypalCredit`. The lowercase `.paylater` case and its future-rename comment remain; `.payLater` is not the current source case.

The native funding-source and button enums contain no Venmo case. A stale comment mentioning `.venmo` is not an implementation. Therefore the native SDK source does not establish native Venmo support; use separately supported web/JavaScript SDK evidence and verify merchant eligibility when proposing Venmo for a native app.

## Vault Without Purchase

### PayPal wallet

`PayPalWebCheckoutClient.vault(PayPalVaultRequest(setupTokenID:))` approves a server-created setup token and returns `PayPalVaultResult(tokenID, approvalSessionID)` through a completion handler or async/await. The `2.0.1` demo creates its setup token with `usage_type: MERCHANT`.

Older iOS product guidance uses `usage_type: PLATFORM`. Treat this as a context-sensitive or documentation discrepancy until PayPal confirms the correct value for the merchant model.

### Cards

`CardClient.vault(CardVaultRequest)` attaches card data to a server-created setup token, can launch 3DS, and returns `CardVaultResult`. The merchant server upgrades the setup token to a payment token.

## Save During Purchase

For PayPal or card save-during-purchase, the merchant includes `store_in_vault: ON_SUCCESS` in the Orders API payment source. The client still runs the normal checkout or card approval flow, and the merchant stores returned vault/customer identifiers after the server completes the order.

Availability, country support, reference-transaction approval, and card PCI obligations must be verified independently from the SDK source.

## Payment Buttons

The SDK provides `PayPalButton`, `PayPalPayLaterButton`, and `PayPalCreditButton`. They are UIKit controls with SwiftUI `Representable` wrappers. Configuration covers color, edges, size, label, and funding source. There is no native Venmo button in the `2.0.1` source.

## Fraud Protection

`PayPalDataCollector.collectDeviceData()` returns JSON containing a correlation ID. It uses Magnes and a Keychain-stored device identifier. The FraudProtection privacy manifest declares device-ID collection for app functionality and marks it as not linked to the user and not used for tracking.

## Reference Demo Baseline

The independent `paypal-examples/paypal-ios-sdk-demo-app` baseline at `047a50e` provides a SwiftUI reference for direct PayPal and card checkout. It accepts PayPal iOS SDK `>=2.0.0,<3.0.0`, but no retained lockfile establishes the exact patch version. Both paths create and complete orders through a merchant server and pass collected device data during completion. The PayPal request uses only `.paypal`; it adds no native Venmo evidence.

The card path uses `.scaWhenRequired` and awaits SDK approval rather than rejecting a 3DS-required branch. The sample still has a miswired CVV change handler, embedded sandbox card values, and no production payment-state validation. Its separate Payment Link path is hosted checkout, not an iOS SDK payment method. See [[source-github-paypal-ios-sdk-demo-app]].

## Version 1 Historical API

Existing 1.x integrations may still use `CardDelegate`, `CardVaultDelegate`, `PayPalWebCheckoutDelegate`, and `PayPalVaultDelegate`. These delegate signatures remain important maintenance knowledge but are not current version 2 APIs. Follow the repository migration guide before moving a 1.x integration to 2.x.

## Messages Module

Pay Later messaging is a separate package, [paypal/paypal-messages-ios](https://github.com/paypal/paypal-messages-ios). The latest ingested package is `paypal-messages-ios@2.0.0` at SHA `e3ee08c`; the `1.2.0` baseline at `432d6b8` remains retained. It is independently versioned from `paypal-ios`.

The untagged `develop` commit `fdd1868` changed the Messages README policy without changing source code: it requires a Braintree account and Braintree SDK integration, and says PPCP SDK integrations are unsupported. Release `2.0.0` now carries this policy in its README; `fdd1868` remains a separate documentation-history boundary, not a package version. No new runtime account-validation mechanism is established by this update.

Messages `2.0.0` requires iOS 15+, while `1.2.0` supports iOS 14+. Its README retains Swift 5.8+ and Xcode 14.3+. These requirements belong to Messages and must not be substituted for the independently versioned checkout SDK requirements above. The rendering/configuration implementations are unchanged, including incomplete environment/partner-identity replacement through `setConfig`; see [[changelog-github-paypal-messages-ios]].

`PayPalMessageView` is a UIKit control with a SwiftUI `UIViewRepresentable` wrapper. Configuration covers merchant identity, transaction context, preferred offer, placement, localization, cache behavior, and branding. The SDK reports loading/success/error plus click/application events and opens a web-backed learn-more modal after successful rendering.

This is promotional messaging, not native payment checkout: it does not create, approve, authorize, or capture an order. Offer enums and rendering support also do not establish merchant or buyer eligibility.

See [[source-github-paypal-messages-ios]] for its versioned API evidence.

## iOS vs Android

| Aspect | iOS 2.x | Android |
| --- | --- | --- |
| Distribution | Swift Package Manager / CocoaPods | Maven Central / Gradle |
| `CardClient` construction | `CardClient(config:)` | Requires Android context/activity in the reviewed API |
| Result handling | Completion `Result` and async/await | Listener/callback APIs in the reviewed Android source |
| 3DS SCA | `.scaWhenRequired` / `.scaAlways` | `SCA_WHEN_REQUIRED` / `SCA_ALWAYS` |
| Buttons | UIKit plus SwiftUI wrappers | Views/Compose surfaces vary by module version |

## Sources

- [[source-github-paypal-ios]] - cumulative package-qualified source through `3.1.1` delta, retaining full `3.0.0`/`3.1.0` and v1/v2 history
- [[changelog-github-paypal-ios]] - major-version and patch release ledger
- [[source-paypal-ios-card-payments]] - older official iOS integration guide
- [[source-paypal-save-paypal-purchase-later-ios-sdk]] - older PayPal vault-without-purchase delegate guidance
- [[source-paypal-save-cards-purchase-later-ios-sdk]] - older card vault delegate guidance
- [[source-paypal-save-paypal-ios-sdk]] - PayPal save-during-purchase guidance
- [[source-paypal-save-cards-ios-sdk]] - card save-during-purchase guidance
- [[source-paypal-ios-in-app-purchases]] - iOS policy-sensitive browser payment patterns
- [[source-github-paypal-messages-ios]] - separate Pay Later messaging package
- [[source-github-paypal-ios-sdk-demo-app]] - SwiftUI direct checkout and hosted Payment Link reference baseline

## Related

- [[paypal]] - PayPal company overview
- [[paypal-vault]] - setup tokens, payment tokens, and stored-credential flows
- [[source-github-paypal-android]] - independently versioned Android SDK evidence
