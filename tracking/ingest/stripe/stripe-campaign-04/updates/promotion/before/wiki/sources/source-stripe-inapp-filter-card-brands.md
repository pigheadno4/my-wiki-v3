---
title: "Filter Card Brands — Mobile"
type: source
date_ingested: 2026-04-22
original_format: webpage
raw_files:
  - "stripe-inapp-filter-card-brands-2025.md"
tags: [stripe, mobile, ios, android, react-native, card-brand-filtering, payment-sheet, apple-pay, google-pay]
---

## Summary

Mobile card brand filtering for iOS, Android, and React Native Payment Sheet. Applies to both the card form AND Apple Pay (iOS/RN) / Google Pay (Android). Two modes: `allowed` or `disallowed`.

## Key Facts

- **4 brand values**: `visa`, `mastercard`, `amex`, `discover`
- **`discover` = entire Discover Global Network**: Discover, Diners Club, JCB, UnionPay, and Elo
- **Scope**: filters both the credit card form AND Apple Pay (iOS/RN) / Google Pay (Android)

## Platform APIs

### iOS (Swift)

```swift
configuration.cardBrandAcceptance = .allowed(brands: [.visa, .mastercard])
// or: .disallowed(brands: [.amex])
```

### Android (Kotlin)

```kotlin
PaymentSheet.Configuration.Builder("Example, Inc.")
  .cardBrandAcceptance(
    PaymentSheet.CardBrandAcceptance.allowed(
      listOf(
        PaymentSheet.CardBrandAcceptance.BrandCategory.Visa,
        PaymentSheet.CardBrandAcceptance.BrandCategory.Mastercard
      )
    )
  )
  .build()
```

### React Native

```javascript
cardBrandAcceptance: {
  filter: PaymentSheet.CardBrandAcceptanceFilter.Allowed, // or Disallowed
  brands: [PaymentSheet.CardBrandCategory.Visa, PaymentSheet.CardBrandCategory.Mastercard],
}
```

## Images

![iOS card brand filtering](../raw/assets/stripe-inapp-filter-card-brands-ios.png)
![Android card brand filtering](../raw/assets/stripe-inapp-filter-card-brands-android.png)

## Related Pages

- [[stripe-inapp-payments]] — concept page
- [[source-stripe-inapp-payment-sheet]] — Payment Sheet detail

## Raw Sources

- [[stripe-inapp-filter-card-brands-2025]] — verbatim card brand filtering guide (180 lines, iOS+Android+RN)
