---
title: "Save PayPal with the iOS SDK"
type: source
date_ingested: 2026-04-14
original_format: webpage
raw_files:
  - "paypal-save-paypal-ios-sdk.md"
tags: [paypal, ios, mobile, vault, save-payment-methods, swift, swiftui, payment-tokens, orders-api, web-checkout]
---

## Overview

Integration guide for saving PayPal Wallets during purchase in iOS apps using the PayPal iOS SDK. Uses `PayPalWebCheckoutClient` (browser-based web checkout) rather than `CardClient`.

Source URL: <https://developer.paypal.com/docs/checkout/save-payment-methods/during-purchase/ios-sdk/paypal/>

Last updated: 2025-03-06

## Key Takeaways

### Availability

35 countries — same as Android PayPal Wallet vault and all other PayPal Wallet vault integrations. Notably **not** US-only (unlike iOS card vault which says US only).

### Flow

1. Create order server-side with `payment_source.paypal.attributes.vault.store_in_vault: ON_SUCCESS`
2. Send `orderId` to iOS SDK
3. `PayPalWebCheckoutClient.start(request: PayPalWebCheckoutRequest(orderID:fundingSource:.paypal))` — launches browser-based PayPal Web Checkout
4. Payer approves; delegate callbacks fire
5. Capture/authorize order server-side → response contains `vault.id` + `customer.id`
6. Store both; use `vault.id` as payment source for returning payers

### SDK setup

```swift
func startPayPalVaultDuringPurchase() {
    let config = CoreConfig(clientID: "CLIENT_ID", environment: .live)
    let payPalClient = PayPalWebCheckoutClient(config: config)
    payPalClient.delegate = self
    let payPalRequest = PayPalWebCheckoutRequest(orderID: order.id, fundingSource: .paypal)
    payPalWebCheckoutClient.start(request: payPalRequest)
}

// PayPalWebCheckoutDelegate
func payPal(_ payPalClient: PayPalWebCheckoutClient, didFinishWithResult result: PayPalWebCheckoutResult) {
    // Capture or authorize on server
}
func payPal(_ payPalClient: PayPalWebCheckoutClient, didFinishWithError error: CoreSDKError) { }
func payPalDidCancel(_ payPalClient: PayPalWebCheckoutClient) { }
```

Note: snippet uses `environment: .live` (not `.sandbox`) — may reflect that this flow requires live testing.

### PayPal button (SwiftUI)

```swift
PayPalButton.Representable() {
    // Create order server-side, then call start()
}
```

### Create Order payload

Identical to Android PayPal Wallet vault:

```json
{
  "payment_source": {
    "paypal": {
      "attributes": {
        "vault": {
          "store_in_vault": "ON_SUCCESS",
          "usage_type": "MERCHANT",
          "customer_type": "CONSUMER"
        }
      }
    }
  }
}
```

### Returning payer

Use saved `vault.id` as payment source in subsequent Create Order — same as Android.

### APPROVED vs VAULTED

Same pattern as all other integrations — subscribe to `VAULT.PAYMENT-TOKEN.CREATED` webhook if `vault.status: APPROVED`.

### Key differences vs iOS card vault

| | Cards (iOS SDK) | PayPal Wallet (iOS SDK) |
| --- | --- | --- |
| Client class | `CardClient` | `PayPalWebCheckoutClient` |
| Delegate | `CardDelegate` | `PayPalWebCheckoutDelegate` |
| Checkout UX | Inline card fields | Browser-based Web Checkout |
| Availability | **US only** (per docs) | 35 countries |
| Returning payer | `customer.id` in Create Order body | `vault.id` as payment source |

### Key differences vs Android PayPal Wallet vault

| | Android | iOS |
| --- | --- | --- |
| Client class | `PayPalWebClient` | `PayPalWebCheckoutClient` |
| Listener/delegate | `PayPalWebCheckoutListener` | `PayPalWebCheckoutDelegate` |
| Button | `AndroidView { PayPalButton }` | `PayPalButton.Representable()` |
| Deep link config | `deepLinkUrlScheme` string | Implicit (no param shown) |
| Environment in snippet | `.sandbox` | `.live` |

> [!warning] PayPal's own guidance
> Same as all PayPal Wallet vault guides — page warns "Don't save PayPal as a payment method during purchase" while being a guide for exactly that.

## Raw Sources

- [[paypal-save-paypal-ios-sdk]] — verbatim integration guide

## Relevant Wiki Pages

- [[paypal-ios-sdk]] — iOS SDK overview (modules, CoreConfig, PayPalWebCheckoutClient, delegates)
- [[paypal-vault]] — Vault concept: token types, APPROVED/VAULTED, webhook
- [[source-paypal-save-cards-ios-sdk]] — Card vault iOS SDK (same SDK, different client/availability)
- [[source-paypal-save-paypal-android-sdk]] — Android SDK equivalent for PayPal Wallet vault
