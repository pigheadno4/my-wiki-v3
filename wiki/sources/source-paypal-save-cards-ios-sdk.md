---
title: "Save Cards with the iOS SDK"
type: source
date_ingested: 2026-04-14
original_format: webpage
raw_files:
  - "paypal-save-cards-ios-sdk.md"
tags: [paypal, ios, mobile, vault, card-payments, swift, swiftui, 3d-secure, sca, payment-tokens, save-payment-methods]
---

## Overview

Integration guide for saving credit/debit cards during purchase in iOS apps using the PayPal iOS SDK (Swift/SwiftUI). Extends the existing advanced card payments integration with vault support.

Source URL: <https://developer.paypal.com/docs/checkout/save-payment-methods/during-purchase/ios-sdk/cards/>

Last updated: 2025-02-27

## Key Takeaways

### Availability

> [!warning] Contradiction — US only vs 35 countries
> This page states availability is **US only** ("In the US only. For both desktop and mobile web."). The Android SDK card vault and JS SDK card vault both support 35 countries. This may be a documentation error or a genuine iOS-specific restriction — treat with caution until confirmed.

### UX — Save toggle (SwiftUI)

```swift
VStack {
    Toggle("Save your card", isOn: $shouldSaveCard)
}
```

SwiftUI `Toggle` — iOS equivalent of Android Compose `Checkbox`.

### Create Order — first-time payer

```json
{
  "payment_source": {
    "card": {
      "attributes": {
        "vault": {
          "store_in_vault": "ON_SUCCESS"
        }
      }
    }
  }
}
```

### Create Order — returning payer

```json
{
  "payment_source": {
    "card": {
      "attributes": {
        "vault": { "store_in_vault": "ON_SUCCESS" },
        "customer": { "id": "PayPal-generated-customer-id" }
      }
    }
  }
}
```

Same as Android SDK — `customer.id` in `payment_source.card.attributes.customer`.

### iOS SDK — CardRequest + approve

```swift
// 1. Build Card with billing address (reduces auth challenges)
let card = Card(
    number: "4005519200000004",
    expirationMonth: "01",
    expirationYear: "2025",
    securityCode: "123",
    cardholderName: "Jane Smith",
    billingAddress: Address(addressLine1: "123 Main St.", ...)
)

// 2. Build CardRequest
let cardRequest = CardRequest(
    orderID: "ORDER_ID",
    card: card,
    sca: .scaAlways  // default: .scaWhenRequired
)

// 3. Approve
let coreConfig = CoreConfig(clientID: "CLIENT_ID", environment: .sandbox)
let cardClient = CardClient(config: coreConfig)
cardClient.delegate = self
cardClient.approveOrder(request: cardRequest)

// 4. CardDelegate callbacks
extension MyViewController: CardDelegate {
    func card(_ cardClient: CardClient, didFinishWithResult result: CardResult) { }
    func card(_ cardClient: CardClient, didFinishWithError error: CoreSDKError) { }
    func cardDidCancel(_ cardClient: CardClient) { }
    func cardThreeDSecureWillLaunch(_ cardClient: CardClient) { }
    func cardThreeDSecureDidFinish(_ cardClient: CardClient) { }
}
```

### APPROVED vs VAULTED

Same pattern as all other integrations — subscribe to `VAULT.PAYMENT-TOKEN.CREATED` webhook if `vault.status: APPROVED`.

### Key differences vs Android card vault

| | Android | iOS |
| --- | --- | --- |
| UI element | Compose `Checkbox` | SwiftUI `Toggle` |
| Client class | `CardClient(activity, coreConfig)` | `CardClient(config: coreConfig)` |
| Result handling | `ApproveOrderListener` | `CardDelegate` protocol |
| SCA enum | `SCA.SCA_ALWAYS` | `.scaAlways` |
| Availability | 35 countries | **US only** (per docs) |

### Next steps

- RTAU (real-time account updater) — same as Android
- Subsequent transactions: use saved `vault.id` with Orders API

## Raw Sources

- [[paypal-save-cards-ios-sdk]] — verbatim integration guide

## Relevant Wiki Pages

- [[paypal-ios-sdk]] — iOS SDK overview (modules, CoreConfig, CardClient, CardDelegate)
- [[paypal-vault]] — Vault concept: token types, APPROVED/VAULTED, webhook
- [[source-paypal-ios-card-payments]] — Base card payments iOS integration (prerequisite)
- [[source-paypal-save-cards-android-sdk]] — Android SDK equivalent
