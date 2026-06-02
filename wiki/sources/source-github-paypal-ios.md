---
title: "GitHub: paypal/paypal-ios"
type: source
date_ingested: 2026-04-13
original_format: github-repo
raw_files:
  - "github-paypal-ios.md"
tags: [paypal, ios, mobile, swift, card-payments, web-payments, fraud-protection, payment-buttons, swiftui, uikit, spm, cocoapods, orders-api, 3d-secure]
---

## GitHub: paypal/paypal-ios

Source code for the PayPal Mobile iOS SDK — Swift modules for card, PayPal web, fraud protection, and payment button integrations.

Repo URL: <https://github.com/paypal/paypal-ios>

Commit SHA: `600a97a5f69ea6f44db3cf2f8b631276fd0152d8` | Reviewed: 2026-04-13

## Key Takeaways from Source

### `CardClient` — no `Context`, only `CoreConfig`

Confirmed: iOS `CardClient` constructor takes only config:

```swift
public init(config: CoreConfig)
```

No Android-style `Context` dependency. Simpler initialisation.

### `PayPalWebCheckoutFundingSource` — case names differ from docs

The actual enum values in source:

```swift
public enum PayPalWebCheckoutFundingSource: String {
    case paypalCredit = "credit"
    case paylater = "paylater"   // NOTE: NEXT_MAJOR_VERSION will rename to `payLater`
    case paypal = "paypal"
}
```

Note: `paylater` (lowercase L) has a `// NEXT_MAJOR_VERSION: rename to 'payLater'` comment — will be a breaking change in the next major version. Use `.paylater` now, not `.payLater`.

### `CardClient` supports vaulting too

Beyond `approveOrder()`, `CardClient` also exposes:

```swift
public func vault(_ vaultRequest: CardVaultRequest, completion: @escaping (Result<CardVaultResult, CoreSDKError>) -> Void)
```

For saving cards without a purchase (vault-without-purchase flow). Returns `CardVaultResult` with `setupTokenID`, `status`, and `didAttemptThreeDSecureAuthentication`.

### Demo ViewModels — complete Swift integration patterns

`CardPaymentViewModel.swift` (165 lines) shows:
1. Create order via `DemoMerchantAPI`
2. Build `Card` + `CardRequest(orderID:, card:, sca:)`
3. `cardClient.approveOrder(request:)` with `delegate = self`
4. Handle `CardDelegate` callbacks
5. On `didFinishWithResult` → capture/authorize via `DemoMerchantAPI`

`PayPalWebViewModel.swift` (189 lines) shows:
1. Create order
2. `PayPalWebCheckoutRequest(orderID:, fundingSource:)`
3. `payPalWebCheckoutClient.start(request:)` with `delegate = self`
4. Handle `PayPalWebCheckoutDelegate` callbacks

`DemoMerchantAPI.swift` (216 lines) — all server calls:
- Create order, capture, authorize
- Create/get setup tokens and payment tokens (vault flows)

### `PaymentButton` — full customisation surface

`PaymentButton.swift` (340 lines) defines all button properties: `color` (`PaymentButtonColor`), `edges` (`PaymentButtonEdges`), `size` (`PaymentButtonSize`), `label` (`PaymentButtonLabel`), `fundingSource` (`PaymentButtonFundingSource`). Both UIKit and SwiftUI via `Representable`.

## Files Saved

See stub file for full path list and per-file descriptions: [[github-paypal-ios]]

## Raw Sources

- [[github-paypal-ios]] — stub file with repo metadata and file navigation table
- Detail directory: `raw/github-paypal-ios/`

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[source-paypal-ios-card-payments]] — official integration guide (docs layer above this source)
- [[source-github-paypal-android]] — Android counterpart (compare iOS vs Android SDK patterns)
