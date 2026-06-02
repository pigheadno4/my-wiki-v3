---
title: "PayPal iOS SDK"
type: concept
category: technology
tags: [paypal, ios, mobile, swift, card-payments, web-payments, fraud-protection, payment-buttons, swiftui, uikit, spm, cocoapods, orders-api, 3d-secure, vault]
---

## PayPal iOS SDK

The PayPal Mobile iOS SDK enables merchants to accept PayPal, credit, and debit card payments in iOS apps. Written in Swift; distributed via Swift Package Manager and CocoaPods.

Repo: <https://github.com/paypal/paypal-ios>

## Available Modules

| Module | SPM product | CocoaPods pod | Purpose |
| ------ | ----------- | ------------- | ------- |
| `CardPayments` | `CardPayments` | `PayPal/CardPayments` | Inline card fields in merchant UI |
| `PayPalWebPayments` | `PayPalWebPayments` | `PayPal/PayPalWebPayments` | Browser-based PayPal checkout inside app |
| `PaymentButtons` | `PaymentButtons` | `PayPal/PaymentButtons` | PayPal-branded buttons (UIKit + SwiftUI) |
| `FraudProtection` | `FraudProtection` | `PayPal/FraudProtection` | Device fingerprinting via `PayPalDataCollector` |

## Core Pattern

All modules share a `CoreConfig`:

```swift
let config = CoreConfig(clientID: "CLIENT_ID", environment: .sandbox)
```

Each module creates its own client from `CoreConfig`:

```swift
let cardClient = CardClient(config: config)           // no Context needed — unlike Android
let webClient = PayPalWebCheckoutClient(config: config)
let dataCollector = PayPalDataCollector(config: config)
```

## Card Payments

Server creates order → client builds `Card` + `CardRequest` → `cardClient.approveOrder(request:)` → `CardDelegate` callbacks → server captures/authorizes.

```swift
let card = Card(number: "4111...", expirationMonth: "01", expirationYear: "2027",
                securityCode: "123", cardholderName: "Jane Doe", billingAddress: address)
let request = CardRequest(orderID: orderID, card: card, sca: .scaAlways)
cardClient.approveOrder(request: request)
```

SCA controlled via `sca` param: `.scaWhenRequired` (default) or `.scaAlways`.

`CardDelegate` protocol methods:

- `didFinishWithResult(_ result: CardResult)` → capture/authorize on server
- `didFinishWithError(_ error: CoreSDKError)`
- `cardDidCancel()`
- `cardThreeDSecureWillLaunch()` / `cardThreeDSecureDidFinish()`

## Vault (Card Without Purchase)

`CardClient` also supports vault-without-purchase — saving a card to a setup token without an immediate charge:

```swift
cardClient.vault(vaultRequest) { result in
    // CardVaultResult: setupTokenID, status, didAttemptThreeDSecureAuthentication
}
```

## Web Payments

Browser-based checkout. Funding sources: `.paypal`, `.payLater`, `.paypalCredit`.

> [!warning] Case name gotcha
> The source code uses `paylater` (lowercase L), not `.payLater`. A `// NEXT_MAJOR_VERSION: rename to 'payLater'` comment indicates this will be a breaking change in the next major version. Use `.paylater` now.

```swift
let request = PayPalWebCheckoutRequest(orderID: orderID, fundingSource: .paypal)
payPalWebCheckoutClient.start(request: request)
```

Implement `PayPalWebCheckoutDelegate` for result callbacks.

## Payment Buttons

`PaymentButton` supports full customisation: `color`, `edges`, `size`, `label`, `fundingSource`. Works in both UIKit and SwiftUI:

```swift
// SwiftUI
PayPalButton.Representable(...)   // wraps UIKit button for SwiftUI
```

SwiftUI support via `Representable` — not available on Android (Android uses XML layout or Compose).

## Fraud Protection

```swift
let clientMetadataID = await dataCollector.collectDeviceData()
```

No location consent flag required (unlike Android's `PayPalDataCollectorRequest(hasUserLocationConsent:)`).

## iOS vs Android — key differences

| Aspect | iOS | Android |
| ------ | --- | ------- |
| Package manager | Swift Package Manager / CocoaPods | Maven Central / Gradle |
| `CardClient` constructor | `CardClient(config:)` — no Context | `CardClient(context, config)` |
| Result handling | `CardDelegate` protocol | `ApproveOrderListener` interface |
| 3DS SCA enum | `.scaWhenRequired` / `.scaAlways` | `SCA.SCA_WHEN_REQUIRED` / `SCA.SCA_ALWAYS` |
| SwiftUI buttons | `PayPalButton.Representable()` | Not available (XML/Compose) |
| Fraud protection | No location consent flag | `hasUserLocationConsent` required |
| Deprecated module | None | `paypal-native-payments` (EOL July 2025) |

## Messages Module (Pay Later Messaging)

The Messages Module is a separate standalone package: [paypal/paypal-messages-ios](https://github.com/paypal/paypal-messages-ios) v1.2.0. Recommended to integrate via the umbrella SDK but usable standalone.

Key API: `PayPalMessageView` (UIControl) + `PayPalMessageView.Representable` (SwiftUI). Config via `PayPalMessageConfig(data:style:)`.

Offer types: `payLaterShortTerm` (Pay in 4), `payLaterLongTerm` (Pay Monthly), `payLaterPayIn1` (deferred), `payPalCreditNoInterest`.

See [[source-github-paypal-messages-ios]] for full API reference.

## Relevant Companies

- [[paypal]] — PayPal company overview

## PayPal Wallet Vault (Save During Purchase)

Uses `PayPalWebCheckoutClient` — same client as non-vault web payments, with vault payload added:

- Create Order with `payment_source.paypal.attributes.vault.store_in_vault: ON_SUCCESS`
- `PayPalButton.Representable()` triggers order creation; `PayPalWebCheckoutClient.start(request:)` launches browser checkout
- Capture response contains `vault.id` + `customer.id` — store both
- Returning payer: pass `vault.id` as payment source in next Create Order
- **35 countries** (unlike iOS card vault: US only)

See [[source-paypal-save-paypal-ios-sdk]] for full detail.

## PayPal Wallet Vault Without Purchase (Save for Later)

Uses `PayPalWebCheckoutClient.vault()` — same client as web payments, vault-specific method:

- Module: `PayPalWebPayments`
- `PayPalVaultRequest(setupTokenID:)` — not `PayPalWebCheckoutRequest(orderID:fundingSource:)`
- `paypalClient.vaultDelegate = self` → `PayPalVaultDelegate` protocol
- `usage_type: PLATFORM` (vs `MERCHANT` for during-purchase)
- Setup token: `PAYER_ACTION_REQUIRED`

See [[source-paypal-save-paypal-purchase-later-ios-sdk]] for full detail.

## Card Vault Without Purchase (Save for Later)

Uses `CardClient.vault()` — not `approveOrder(request:)`:

- `CardVaultRequest(setupTokenID:card:)` — setup token from server, card from payer input
- `cardClient.vaultDelegate = self` → `CardVaultDelegate` protocol
- Callbacks: `didFinishWithVaultResult`, `didFinishWithVaultError`, `cardVaultDidCancel`, `cardThreeDSecureWillLaunch/DidFinish`
- Returning customer: `customer.id` in setup token request body
- Setup token response status: `CREATED`

See [[source-paypal-save-cards-purchase-later-ios-sdk]] for full detail.

## Card Vault (Save During Purchase)

Extends the base card payments integration. Key additions:

- SwiftUI `Toggle` for save-card opt-in
- Create Order with `payment_source.card.attributes.vault.store_in_vault: ON_SUCCESS`
- Returning payer: `customer.id` in `payment_source.card.attributes.customer` (same as Android)
- `CardClient.approveOrder(request:)` unchanged — vault happens server-side after capture
- RTAU available for keeping saved cards current

> [!warning] Availability
> Docs state US only — contradicts Android SDK (35 countries). Verify before deploying globally.

See [[source-paypal-save-cards-ios-sdk]] for full detail.

## Sources

- [[source-paypal-ios-card-payments]] — official iOS integration guide (docs layer)
- [[source-paypal-save-paypal-purchase-later-ios-sdk]] — PayPal Wallet vault without purchase: `PayPalVaultDelegate`, `PayPalVaultRequest`, `usage_type: PLATFORM`
- [[source-paypal-save-cards-purchase-later-ios-sdk]] — Card vault without purchase: `CardVaultDelegate`, `cardVaultDidCancel`, `CREATED` setup token status
- [[source-paypal-save-paypal-ios-sdk]] — PayPal Wallet vault during purchase: `PayPalWebCheckoutClient`, `PayPalWebCheckoutDelegate`, 35 countries, `vault.id` for returning payers
- [[source-paypal-save-cards-ios-sdk]] — card vault during purchase: SwiftUI Toggle, CardDelegate, US-only availability contradiction
- [[source-github-paypal-ios]] — GitHub source: `CardClient` constructor, `paylater` case name gotcha, vault support, Demo ViewModels
- [[source-paypal-ios-in-app-purchases]] — iOS in-app purchase flow (browser-redirect, Apple external payment entitlement)
- [[source-github-paypal-messages-ios]] — GitHub paypal-messages-ios: PayPalMessageConfig API, offer types, delegates, SwiftUI/UIKit integration
