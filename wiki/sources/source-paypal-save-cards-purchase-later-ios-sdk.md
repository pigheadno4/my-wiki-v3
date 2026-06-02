---
title: "Save Cards for Purchase Later with the iOS SDK"
type: source
date_ingested: 2026-04-14
original_format: webpage
raw_files:
  - "paypal-save-cards-purchase-later-ios-sdk.md"
tags: [paypal, ios, mobile, vault, card-payments, swift, swiftui, setup-token, payment-tokens, 3d-secure, purchase-later]
---

## Overview

Integration guide for saving credit/debit cards **without a purchase transaction** in iOS apps using the PayPal iOS SDK (Swift). Uses `CardVaultRequest` + `CardClient.vault()` and `CardVaultDelegate`.

Source URL: <https://developer.paypal.com/docs/checkout/save-payment-methods/purchase-later/ios-sdk/cards/>

Last updated: 2025-02-06

## Key Takeaways

### Availability

35 countries assumed (availability section in source shows "See supported countries" without listing — collapsed UI element; pattern consistent with all other card vault integrations).

### Supported card types

American Express, Discover, Mastercard, Visa.

### Installation

Swift Package Manager (or CocoaPods):

1. Add `https://github.com/paypal/paypal-ios/` as SPM repository
2. Select the **CardPayments** framework checkbox

### Flow

1. Server: `POST /v3/vault/setup-tokens` with empty `payment_source.card: {}`
   - New customer: no `customer` field
   - Returning customer: `customer.id` in request body
   - Response: `status: CREATED`
2. Client: build `Card` + `CardVaultRequest(setupTokenID:card:)`
3. `cardClient.vaultDelegate = self` → `cardClient.vault(cardVaultRequest)`
4. `CardVaultDelegate` callbacks fire
5. `didFinishWithVaultResult(vaultResult: CardVaultResult)` → send `vaultResult.setupTokenID` to server
6. Server: `POST /v3/vault/payment-tokens` → payment token + `customer.id`
7. Store both for future charges

### iOS SDK — vault call

```swift
let config = CoreConfig(clientID: "CLIENT_ID", environemnt: .live)
let cardClient = CardClient(config: config)
cardClient.vaultDelegate = self
cardClient.vault(cardVaultRequest)
```

Note: `environemnt` typo in source (same as iOS card during-purchase guide and Android SDK guides).

### `CardVaultDelegate` protocol

```swift
extension MyViewController: CardVaultDelegate {
    func card(_ cardClient: CardClient, didFinishWithVaultResult vaultResult: CardVaultResult) {
        // vaultResult.setupTokenID → send to server
    }
    func card(_ cardClient: CardClient, didFinishWithVaultError error: CoreSDKError) { }
    func cardVaultDidCancel(_ cardClient: CardClient) { }
    func cardThreeDSecureWillLaunch(_ cardClient: CardClient) { }
    func cardThreeDSecureDidFinish(_ cardClient: CardClient) { }
}
```

### Key differences vs iOS card during-purchase vault

| | During purchase | Purchase later |
| --- | --- | --- |
| SDK method | `cardClient.approveOrder(request:)` | `cardClient.vault(cardVaultRequest)` |
| Request object | `CardRequest(orderID:card:sca:)` | `CardVaultRequest(setupTokenID:card:)` |
| Delegate | `CardDelegate` | `CardVaultDelegate` |
| Vault API | Orders API `store_in_vault: ON_SUCCESS` | Setup token → payment token |
| Returning customer | `customer.id` in Create Order body | `customer.id` in setup token request |
| Setup token status | N/A | `CREATED` |

### Key differences vs Android cards purchase-later vault

| | Android | iOS |
| --- | --- | --- |
| Client | `CardClient(config)` | `CardClient(config:)` |
| Method | `cardClient.vault(context, request)` | `cardClient.vault(request)` — no context |
| Listener/delegate | `CardVaultListener` interface | `CardVaultDelegate` protocol |
| Callbacks | `onVaultSuccess/Failure` | `didFinishWithVaultResult/VaultError` |
| 3DS cancel | `onVaultFailure` | `cardVaultDidCancel` |

### Security note

Don't expose payment token IDs client-side — same guidance as all other vault integrations.

## Raw Sources

- [[paypal-save-cards-purchase-later-ios-sdk]] — verbatim integration guide

## Relevant Wiki Pages

- [[paypal-ios-sdk]] — iOS SDK overview (modules, CoreConfig, CardClient, delegates)
- [[paypal-vault]] — Vault concept: setup token → payment token flow
- [[source-paypal-save-cards-ios-sdk]] — iOS card vault during purchase (uses `approveOrder()`)
- [[source-paypal-save-cards-purchase-later-android-sdk]] — Android SDK equivalent
