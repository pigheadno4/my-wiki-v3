---
title: "PayPal iOS SDK: Integrate Card Payments"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-ios-card-payments.md"
tags: [paypal, ios, mobile, swift, card-payments, 3d-secure, sca, web-payments, fraud-protection, payment-buttons, swiftui, uikit, orders-api]
---

## PayPal iOS SDK: Integrate Card Payments

Official integration guide for accepting PayPal, credit, and debit card payments in iOS apps using the PayPal Mobile iOS SDK (Swift).

Source URL: <https://developer.paypal.com/docs/checkout/advanced/ios/>

Last updated: 2026-01-30

Sample integration repo: <https://github.com/paypal-examples/paypal-ios-sdk-demo-app>

## Key Takeaways

### iOS vs Android — key differences

| Aspect | iOS | Android |
| ------ | --- | ------- |
| Package manager | Swift Package Manager / CocoaPods | Maven Central / Gradle |
| Card client | `CardClient(config: coreConfig)` | `CardClient(context, coreConfig)` |
| Result handling | `CardDelegate` protocol | `ApproveOrderListener` interface |
| 3DS options | `.scaWhenRequired` / `.scaAlways` | `SCA.SCA_WHEN_REQUIRED` / `SCA.SCA_ALWAYS` |
| Web payments | `PayPalWebCheckoutClient` (delegate-based) | `PayPalWebCheckoutClient` (listener-based) |
| Buttons | UIKit + SwiftUI via `PayPalButton.Representable()` | XML layout + Kotlin |
| Fraud protection | `PayPalDataCollector(config:)` — no location consent flag | `PayPalDataCollectorRequest(hasUserLocationConsent)` |

### Card Payments flow (8 steps)

1. Add `CardPayments` via Swift Package Manager or CocoaPods (`pod 'PayPal/CardPayments'`)
2. `CoreConfig(clientID:, environment:)` → `CardClient(config:)`
3. Server creates order → returns `ORDER_ID`
4. Build `Card(number:, expirationMonth:, expirationYear:, securityCode:, cardholderName:, billingAddress:)`
5. `CardRequest(orderID:, card:, sca: .scaAlways)`
6. `cardClient.approveOrder(request: cardRequest)` — no Activity/Context needed
7. Implement `CardDelegate`: `didFinishWithResult`, `didFinishWithError`, `cardDidCancel`, `cardThreeDSecureWillLaunch`, `cardThreeDSecureDidFinish`
8. On `didFinishWithResult` → server calls capture or authorize

### iOS `CardClient` — no `Context` needed

Unlike Android's `CardClient(context, config)`, iOS is just `CardClient(config: coreConfig)` — simpler constructor.

### `PayPalWebCheckoutRequest` funding sources (iOS)

```swift
PayPalWebCheckoutRequest(orderID: "ORDER_ID", fundingSource: .paypal)
// Options: .paypal (default), .payLater, .payPalCredit
```

Same 3 options as Android — no Venmo.

### SwiftUI button support

iOS provides `PayPalButton.Representable()` for SwiftUI integration — not available on Android (Android is XML/Compose only).

### Fraud protection — simpler than Android

iOS `dataCollector.collectDeviceData()` takes no arguments. No location consent flag required (unlike Android which requires `hasUserLocationConsent`).

### Apple external payment entitlement

The page notes: "In certain countries, Apple allows apps to link to an external website for processing payments" — this is a reference to Apple's external payment link entitlement, required for some payment flows on iOS.

## Raw Sources

- [[paypal-ios-card-payments]] — verbatim webpage content
- See also [[source-github-paypal-ios]] — source code layer with `paylater` case name gotcha and vault support

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[source-paypal-android-card-payments]] — Android equivalent (compare iOS vs Android patterns)
- [[source-github-paypal-android]] — Android SDK source (note: `CardClient` takes Context on Android, not on iOS)
