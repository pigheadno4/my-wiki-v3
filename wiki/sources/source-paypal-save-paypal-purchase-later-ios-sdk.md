---
title: "Save PayPal for Purchase Later with the iOS SDK"
type: source
date_ingested: 2026-04-14
original_format: webpage
raw_files:
  - "paypal-save-paypal-purchase-later-ios-sdk.md"
tags: [paypal, ios, mobile, vault, save-payment-methods, swift, setup-token, payment-tokens, purchase-later, web-payments]
---

## Overview

Integration guide for saving PayPal Wallets **without a purchase transaction** in iOS apps using the PayPal iOS SDK. Uses `PayPalWebCheckoutClient.vault()` with `PayPalVaultRequest` and `PayPalVaultDelegate`.

Source URL: <https://developer.paypal.com/docs/checkout/save-payment-methods/purchase-later/ios-sdk/paypal/>

Last updated: 2024-02-09

## Key Takeaways

### Availability

35 countries assumed (availability section shows "See supported countries" only — collapsed UI element).

### Module

`PayPalWebPayments` (not `CardPayments`):

SPM: `https://github.com/paypal/paypal-ios/` → select **PayPalWebPayments** framework.

### Flow

1. Server: `POST /v3/vault/setup-tokens` with `payment_source.paypal` + `experience_context`
   - Response status: `PAYER_ACTION_REQUIRED`
   - `usage_type: PLATFORM`
2. Client: `PayPalVaultRequest(setupTokenID: setupTokenResponse.setupTokenId)`
3. `PayPalWebCheckoutClient.vault(vaultRequest)` with `vaultDelegate = self`
4. `PayPalVaultDelegate` callbacks fire
5. Server: `POST /v3/vault/payment-tokens` → payment token + `customer.id`
6. Store both for future charges

### Client-side SDK

```swift
let config = CoreConfig(clientID: "CLIENT_ID", environment: .sandbox)
let vaultRequest = PayPalVaultRequest(setupTokenID: setupTokenResponse.setupTokenId)

let paypalClient = PayPalWebCheckoutClient(config: config)
paypalClient.vaultDelegate = self
paypalClient.vault(vaultRequest)

// MARK: - PayPalVaultDelegate
func paypal(_ paypalWebClient: PayPalWebCheckoutClient, didFinishWithVaultResult paypalVaultResult: PayPalVaultResult) { }
func paypal(_ paypalWebClient: PayPalWebCheckoutClient, didFinishWithVaultError vaultError: CoreSDKError) { }
func paypalDidCancel(_ paypalWebClient: PayPalWebCheckoutClient) { }
```

Note: `environment: .sandbox` here (vs `.live` in iOS card purchase-later guide).

### Key differences vs iOS PayPal during-purchase vault

| | During purchase | Purchase later |
| --- | --- | --- |
| SDK method | `PayPalWebCheckoutClient.start(request:)` | `PayPalWebCheckoutClient.vault(vaultRequest)` |
| Request object | `PayPalWebCheckoutRequest(orderID:fundingSource:)` | `PayPalVaultRequest(setupTokenID:)` |
| Delegate | `PayPalWebCheckoutDelegate` | `PayPalVaultDelegate` (`vaultDelegate`) |
| Vault API | Orders API `store_in_vault: ON_SUCCESS` | Setup token → payment token |
| `usage_type` | `MERCHANT` | `PLATFORM` |
| Environment | `.live` (per snippet) | `.sandbox` |

### Key differences vs Android PayPal purchase-later vault

| | Android | iOS |
| --- | --- | --- |
| Client | `PayPalWebCheckoutClient(activity, config, URL_SCHEME)` | `PayPalWebCheckoutClient(config:)` — no activity/URL scheme |
| Method | `paypalClient.vault(vaultRequest)` | `paypalClient.vault(vaultRequest)` |
| Listener/delegate | `vaultListener` (object implementation) | `vaultDelegate` (protocol) |
| Callbacks | `onPayPalWebVaultSuccess/Failure/Canceled` | `didFinishWithVaultResult/VaultError`, `paypalDidCancel` |
| Environment | `.live` | `.sandbox` |

> [!info] `usage_type: PLATFORM` consistent
> Both Android and iOS PayPal purchase-later use `PLATFORM`. Both during-purchase guides use `MERCHANT`. This appears intentional — platform-facilitated (off-session) vs direct merchant (during-purchase) distinction.

## Raw Sources

- [[paypal-save-paypal-purchase-later-ios-sdk]] — verbatim integration guide

## Relevant Wiki Pages

- [[paypal-ios-sdk]] — iOS SDK overview (PayPalWebCheckoutClient, delegates)
- [[paypal-vault]] — Vault concept: setup token → payment token flow
- [[source-paypal-save-paypal-ios-sdk]] — PayPal during-purchase iOS vault (`start()` not `vault()`)
- [[source-paypal-save-paypal-purchase-later-android-sdk]] — Android SDK equivalent (same `PLATFORM` usage_type)
