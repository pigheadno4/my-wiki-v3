---
title: "Accept In-App Payments with the Embedded Payment Element"
type: source
date_ingested: 2026-04-22
original_format: webpage
raw_files:
  - "stripe-inapp-accept-payment-embedded-2025.md"
tags: [stripe, mobile, ios, android, react-native, embedded-payment-element, embedded, scrollview, height-changes, mandate, formsheet]
---

## Summary

Full integration guide for the Embedded Mobile Payment Element (`EmbeddedPaymentElement`) across iOS (UIKit + SwiftUI), Android, and React Native. Covers initialization, height management, `update()`, `formSheetAction`, mandate display, and saved cards.

## Key Integration Requirements

- **Must be in a ScrollView**: `EmbeddedPaymentElement.view` doesn't have a fixed size and can change height — embed in `UIScrollView` (UIKit) or `ScrollView` (SwiftUI)
- **iOS UIKit**: requires `presentingViewController` and `delegate` to be set after `create()`
- **iOS SwiftUI**: use `EmbeddedPaymentElementViewModel` as `@StateObject`, render `EmbeddedPaymentElementView`

## iOS UIKit Pattern

```swift
// 1. Create async
let embeddedPaymentElement = try await EmbeddedPaymentElement.create(
  intentConfiguration: intentConfig, configuration: configuration
)
embeddedPaymentElement.presentingViewController = self
embeddedPaymentElement.delegate = self

// 2. Add to UIScrollView
scrollView.addSubview(embeddedPaymentElement.view)

// 3. Confirm
let result = await embeddedPaymentElement.confirm()
```

## Handle Height Changes (UIKit)

```swift
extension MyVC: EmbeddedPaymentElementDelegate {
  func embeddedPaymentElementDidUpdateHeight(embeddedPaymentElement: EmbeddedPaymentElement) {
    self.view.setNeedsLayout()
    self.view.layoutIfNeeded()
  }
}
```

Test: call `embeddedPaymentElement?.testHeightChange()` in DEBUG.

## `paymentOption` — Selected PM Details

- `.label`: e.g. "····4242"
- `.image`: e.g. Visa logo
- `.billing_details`, `.mandateText`

Delegate: `embeddedPaymentElementDidUpdatePaymentOption` — fires when PM selection changes.

## `update()` — Cart Changes

```swift
let result = await embeddedPaymentElement?.update(intentConfiguration: updatedIntentConfig)
// .succeeded | .failed | .canceled (when subsequent update cancels this one)
```

May change the selected payment option. Handle `.failed` by retrying (show alert + retry button).

## `formSheetAction: .confirm()` — Pay Immediately in Sheet

```swift
configuration.formSheetAction = .confirm(completion: { result in
  // .completed | .failed | .canceled
})
```

Button in the form sheet says "Pay now" and confirms immediately instead of returning to your checkout.

## Mandate Display

```swift
// Disable built-in mandate display
configuration.embeddedViewDisplaysMandateText = false

// Render yourself (must be near buy button for compliance)
let mandateTextView = UITextView()
mandateTextView.attributedText = embeddedPaymentElement.paymentOption?.mandateText
```

## `clearPaymentOption()` — Deselect PM

```swift
embeddedPaymentElement?.clearPaymentOption()
// or: embeddedViewModel.clearPaymentOption()
```

Useful when you have external payment options (e.g. Apple Pay button) and need to deselect.

## Images

![iOS embedded example](../raw/assets/stripe-inapp-ios-embedded.png)
![Android embedded example](../raw/assets/stripe-inapp-android-embedded.png)
![Embedded pay immediately](../raw/assets/stripe-inapp-embedded-pay-immediate.png)

## Related Pages

- [[stripe-inapp-payments]] — concept page
- [[source-stripe-inapp-payment-element]] — Payment Element overview

## Raw Sources

- [[stripe-inapp-accept-payment-embedded-2025]] — verbatim embedded PE integration guide (9657 lines, iOS+Android+RN)
