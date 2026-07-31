---
title: "GitHub: paypal/paypal-ios"
type: source
date_ingested: 2026-04-13
date_updated: 2026-07-31
original_format: github-repo
raw_files:
  - "github/paypal/paypal-ios/snapshots/2026-07-31-2008a6d/manifest.json"
  - "github-paypal-ios.md"
tags: [paypal, ios, swift, mobile, sdk, card-payments, web-payments, vault, fraud-protection, payment-buttons, swiftui, uikit, spm, cocoapods, github-repository]
---

## Overview

`paypal/paypal-ios` publishes PayPal's modular native iOS SDK. This cumulative page preserves the April 2026 review at commit `600a97a5f69ea6f44db3cf2f8b631276fd0152d8` and adds the approved full baseline for `paypal-ios@2.0.1` at commit `2008a6de7c00a2ae53c669932d5fb19674c35b1e`.

Repository: <https://github.com/paypal/paypal-ios>

## Evidence Boundary

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
| `paypal-ios` | `2.0.1` | `2008a6de7c00a2ae53c669932d5fb19674c35b1e` | Approved full baseline; earlier reviewed SHA retained |

This reports wiki ingest progress, not the latest release published upstream.

## Modules and Requirements

| Module | Purpose |
| --- | --- |
| `CorePayments` | Shared configuration, networking, analytics, errors, and web authentication |
| `CardPayments` | Card order approval and card vault-without-purchase, including 3DS |
| `PayPalWebPayments` | Browser-based PayPal checkout and PayPal vault approval |
| `PaymentButtons` | UIKit buttons and SwiftUI wrappers for PayPal, Pay Later, and PayPal Credit |
| `FraudProtection` | Device data collection through the bundled Magnes binary |

The package supports Swift Package Manager and CocoaPods. The `2.0.1` README requires iOS 14+, Swift 5.9+, Xcode 15+, and macOS Ventura 13.

## Version 2 API Model

Version 2 removes the payment and vault delegate protocols used by version 1. Current operations expose `Result<Success, CoreSDKError>` completion handlers plus Swift concurrency overloads:

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
