---
title: "Display BNPL Messaging — Mobile Integration Guide"
type: source
date_ingested: 2026-04-22
original_format: webpage
raw_files:
  - "stripe-inapp-display-bnpl-messaging-2025.md"
tags: [stripe, mobile, ios, android, bnpl, buy-now-pay-later, payment-method-messaging-element, beta]
---

## Summary

Full integration guide for the mobile Payment Method Messaging Element across iOS UIKit, iOS SwiftUI, and Android. Beta feature on all platforms. No React Native section.

> See also [[source-stripe-inapp-payment-method-messaging-element]] for the overview page, and [[source-stripe-payment-method-messaging-element]] for the web variant.

## Beta Import Required

- **iOS**: `@_spi(PaymentMethodMessagingElementPreview) import StripePaymentSheet`
- **Android**: `@OptIn(PaymentMethodMessagingElementPreview::class)`

## Platform API Comparison

| | iOS UIKit | iOS SwiftUI | Android |
| --- | --- | --- | --- |
| Init | `PaymentMethodMessagingElement.create(configuration:)` async | `PaymentMethodMessagingElement.View(configuration)` | `PaymentMethodMessagingElement.create(application)` then `.configure(configuration)` |
| Result | `.success(element)` / `.noContent` / `.failed` | Phase builder: `.loaded` / `.loading` / `.noContent` / `.failed` | `ConfigureResult.Succeeded` / `.NoContent` / `.Failed` |
| Display | `element.view` → add to UIKit hierarchy | `PaymentMethodMessagingElement.View` SwiftUI component | `paymentMethodMessagingElement.Content()` composable |
| Update | Remove old view + recreate | `@State` config drives auto-reload | Call `.configure()` again; `Content()` auto-updates |

## iOS UIKit

```swift
@_spi(PaymentMethodMessagingElementPreview) import StripePaymentSheet

let configuration = PaymentMethodMessagingElement.Configuration(amount: 1000, currency: "USD")

switch await PaymentMethodMessagingElement.create(configuration: configuration) {
case .success(let element):
    self.view.addSubview(element.view)
    // set up NSLayoutConstraints
case .noContent:
    // no eligible BNPL plans for this amount/currency/country
case .failed(let error):
    // unrecoverable error
}
```

## iOS SwiftUI

```swift
// Auto-reload when @State price changes
PaymentMethodMessagingElement.View(.init(amount: price, currency: "usd"))

// Phase-based (optional):
PaymentMethodMessagingElement.View(configuration) { phase in
    switch phase {
    case .loaded(let view): view
    case .loading: MyLoadingView()
    case .noContent: EmptyView()
    case .failed(let error): /* log */ EmptyView()
    }
}

// MVVM path (optional):
// PaymentMethodMessagingElement.create() → element.viewData
// PaymentMethodMessagingElement.View(viewData)
```

## Android (Kotlin/Compose)

```kotlin
// Separate dependency: com.stripe:payment-method-messaging:23.5.0
// (NOT the main stripe-android dependency)

// ViewModel
val paymentMethodMessagingElement = PaymentMethodMessagingElement.create(getApplication())

val result = paymentMethodMessagingElement.configure(
    PaymentMethodMessagingElement.Configuration()
        .amount(10000L).currency("usd")
)
// result: ConfigureResult.Succeeded / .NoContent / .Failed

// Activity / Composable
viewModel.paymentMethodMessagingElement.Content()         // auto-updates on re-configure
viewModel.paymentMethodMessagingElement.Content(appearance) // with appearance
```

## Configuration Options (All Platforms)

| Option | Default | Notes |
| --- | --- | --- |
| `amount` | — | Required; smallest currency unit |
| `currency` | — | Required |
| `locale` | Device locale | Can be explicitly set |
| `countryCode` | Customer IP | Can be explicitly set |
| `paymentMethodTypes` | Dashboard dynamic | Override with `[.affirm, .klarna]` etc. |

## Appearance (All Platforms)

iOS: `PaymentMethodMessagingElement.Appearance(style:, font:, textColor:, infoIconColor:)`

Android: separate `Font()` / `Colors()` / `Appearance()` builder objects with `.theme(DARK/LIGHT)` option.

## Related Pages

- [[stripe-inapp-payments]] — in-app payments concept page
- [[stripe-payment-method-messaging-element]] — web BNPL messaging concept (no clientSecret, Affirm/Afterpay/Klarna)
- [[source-stripe-inapp-payment-method-messaging-element]] — mobile overview page

## Raw Sources

- [[stripe-inapp-display-bnpl-messaging-2025]] — verbatim guide (~599 lines, iOS UIKit + iOS SwiftUI + Android)
