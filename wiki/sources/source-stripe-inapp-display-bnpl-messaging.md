---
title: "Display BNPL Messaging — Mobile Integration Guide"
type: source
date_ingested: 2026-04-22
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/mobile/display-bnpl-messaging"
raw_files:
  - "stripe-inapp-display-bnpl-messaging-2025.md"
tags: [stripe, mobile, ios, android, bnpl, buy-now-pay-later, payment-method-messaging-element, beta]
---

## Summary

The 2026-04-22 [[stripe|Stripe]] guide describes promotional buy now, pay later messaging for a potential purchase. It includes full preview examples for iOS UIKit, iOS SwiftUI, and Android. The 2026-11-07 capture indexes UIKit, SwiftUI, Android, and React Native documentation. It adds React Native navigation and leaves all four linked implementation bodies outside the capture.

See [[source-stripe-inapp-payment-method-messaging-element]] for the separate mobile overview. Its April capture describes iOS and Android, and its November index also links React Native. The [[source-stripe-payment-method-messaging-element|web guide]] covers a different SDK surface.

## April 2026 Setup and Preview Opt-ins

The guide assumes a Stripe account and configures the platform SDK with a client publishable key. Use test keys during development and live keys for the published app. The following imports and dependency version are from the April examples.

- **iOS**: `@_spi(PaymentMethodMessagingElementPreview) import StripePaymentSheet`
- **Android**: `@OptIn(PaymentMethodMessagingElementPreview::class)`

The April iOS raw includes CocoaPods installation and update examples. The separate October [[source-github-stripe-ios|iOS SDK migration guide]] identifies 26.15.0 as the last native CocoaPods release and routes newer updates through Swift Package Manager or XCFrameworks.

## April 2026 Platform API Comparison

| | iOS UIKit | iOS SwiftUI | Android |
| --- | --- | --- | --- |
| Init | `PaymentMethodMessagingElement.create(configuration:)` async | `PaymentMethodMessagingElement.View(configuration)` | `PaymentMethodMessagingElement.create(application)` then `.configure(configuration)` |
| Result | `.success(element)` / `.noContent` / `.failed` | Phase builder: `.loaded` / `.loading` / `.noContent` / `.failed` | `ConfigureResult.Succeeded` / `.NoContent` / `.Failed` |
| Display | `element.view` → add to UIKit hierarchy | `PaymentMethodMessagingElement.View` SwiftUI component | `paymentMethodMessagingElement.Content()` composable |
| Update | Remove old view + recreate | `@State` config drives auto-reload | Call `.configure()` again and `Content()` auto-updates |

A no-content result means this configuration produced no element to display. The SwiftUI guide mentions an amount below the available methods' minimum as one example. A failure indicates a loading or configuration error. These results describe display behavior and leave customer financing approval, payment confirmation, and settlement unverified.

## iOS UIKit

```swift
@_spi(PaymentMethodMessagingElementPreview) import StripePaymentSheet

let configuration = PaymentMethodMessagingElement.Configuration(amount: 1000, currency: "USD")

switch await PaymentMethodMessagingElement.create(configuration: configuration) {
case .success(let element):
    self.view.addSubview(element.view)
    // set up NSLayoutConstraints
case .noContent:
    // This configuration produced no element to display
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
// Initialize PaymentConfiguration with the application context and publishable key.

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

## April 2026 Configuration Examples

These fields appear in the three archived native examples. The examples supply the purchase amount and currency.

| Option | Default | Notes |
| --- | --- | --- |
| `amount` | — | Example in the smallest currency unit |
| `currency` | — | Example currency code |
| `locale` | Device locale | Can be explicitly set |
| `countryCode` | Customer IP | Can be explicitly set |
| `paymentMethodTypes` | Dashboard dynamic | Override with `[.affirm, .klarna]` etc. |

## April 2026 Appearance Examples

iOS: `PaymentMethodMessagingElement.Appearance(style:, font:, textColor:, infoIconColor:)`

Android: separate `Font()` / `Colors()` / `Appearance()` builder objects with a `Theme.DARK` example.

## React Native 0.82.0 SDK Scope

The separately retained October 2026 [[source-github-stripe-react-native|React Native SDK snapshot]] identifies the component as Public Preview at tag 0.82.0. The typed `configuration` requires `currency` and accepts optional `country`. The same component's inline example uses `currencyCode` and `countryCode`. Its JavaScript wrapper forwards `configuration` as supplied to the native component. Use the tagged TypeScript declaration for the typed API. The discrepancy leaves the native interpretation and the November linked variant's contents unresolved.

## Detail Locators

- April raw lines 71–163 show UIKit initialization, loading results, and replacement on configuration change.
- April raw lines 255–397 show SwiftUI reloads, the optional phase builder, and the manual `viewData` path.
- April raw lines 432–537 show the Android dependency, application context, configure results, and Compose display.
- April raw lines 166–192, 399–425, and 539–598 cover the native configuration and appearance examples.
- October React Native 0.82.0 raw `PaymentMethodMessagingElement.tsx` lines 17–25, 39–43, and 102–109 cover preview, the inline example, and wrapper forwarding. `PaymentMethodMessagingElementComponent.tsx` lines 55–78 define the typed configuration.

## Related Pages

- [[stripe-inapp-payments]] — in-app payments concept page
- [[stripe-payment-method-messaging-element]] — Payment Method Messaging Element concept with separate web and mobile routes
- [[source-stripe-inapp-payment-method-messaging-element]] — mobile overview page

## Raw Sources

- [[raw/stripe-inapp-display-bnpl-messaging-2025|2026-04-22 guide for iOS UIKit, iOS SwiftUI, and Android]]

## Related raw API references

- [[raw/stripe-payments-mobile-display-bnpl-messaging-2026-11-07|2026-11-07 mobile variant index]] — links to iOS UIKit, iOS SwiftUI, Android, and React Native
