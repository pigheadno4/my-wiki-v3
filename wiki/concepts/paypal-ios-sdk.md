---
title: "PayPal iOS SDK"
type: concept
category: technology
tags: [paypal, ios, mobile, swift, card-payments, web-payments, fraud-protection, payment-buttons, swiftui, uikit, spm, cocoapods, orders-api, 3d-secure, vault]
---

## PayPal iOS SDK

The PayPal iOS SDK provides native Swift modules for cards, browser-based PayPal checkout, PayPal-branded buttons, vault approval, and device data collection. The latest ingested package is `paypal-ios@2.0.1`; this is wiki ingest status, not a claim about the latest upstream release.

Repository: <https://github.com/paypal/paypal-ios>

## Requirements and Modules

| Module | Purpose |
| --- | --- |
| `CorePayments` | Configuration, networking, analytics, errors, and web authentication |
| `CardPayments` | Card order approval, 3DS, and card vault without purchase |
| `PayPalWebPayments` | Browser-based PayPal checkout and PayPal vault approval |
| `PaymentButtons` | PayPal, Pay Later, and PayPal Credit buttons for UIKit and SwiftUI |
| `FraudProtection` | Device data collection through Magnes |

The package supports Swift Package Manager and CocoaPods. The `2.0.1` source requires iOS 14+, Swift 5.9+, Xcode 15+, and macOS Ventura 13.

## Shared Configuration

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

## PayPal Web Checkout

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

## Version 1 Historical API

Existing 1.x integrations may still use `CardDelegate`, `CardVaultDelegate`, `PayPalWebCheckoutDelegate`, and `PayPalVaultDelegate`. These delegate signatures remain important maintenance knowledge but are not current version 2 APIs. Follow the repository migration guide before moving a 1.x integration to 2.x.

## Messages Module

Pay Later messaging is a separate package, [paypal/paypal-messages-ios](https://github.com/paypal/paypal-messages-ios). Its `PayPalMessageView` supports UIKit and SwiftUI and is not the same module as native payment checkout.

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

- [[source-github-paypal-ios]] - cumulative package-qualified source through `paypal-ios@2.0.1`
- [[changelog-github-paypal-ios]] - major-version and patch release ledger
- [[source-paypal-ios-card-payments]] - older official iOS integration guide
- [[source-paypal-save-paypal-purchase-later-ios-sdk]] - older PayPal vault-without-purchase delegate guidance
- [[source-paypal-save-cards-purchase-later-ios-sdk]] - older card vault delegate guidance
- [[source-paypal-save-paypal-ios-sdk]] - PayPal save-during-purchase guidance
- [[source-paypal-save-cards-ios-sdk]] - card save-during-purchase guidance
- [[source-paypal-ios-in-app-purchases]] - iOS policy-sensitive browser payment patterns
- [[source-github-paypal-messages-ios]] - separate Pay Later messaging package

## Related

- [[paypal]] - PayPal company overview
- [[paypal-vault]] - setup tokens, payment tokens, and stored-credential flows
- [[source-github-paypal-android]] - independently versioned Android SDK evidence
