---
title: "Filter Card Brands — EmbeddedPaymentElement"
type: source
date_ingested: 2026-04-22
original_format: webpage
raw_files:
  - "stripe-inapp-embedded-filter-card-brands-2025.md"
tags: [stripe, mobile, ios, android, react-native, embedded-payment-element, card-brand-filtering, card-brands]
---

## Summary

EmbeddedPaymentElement-specific card brand filtering guide. Parallel to the PaymentSheet variant (`source-stripe-inapp-filter-card-brands`) but uses `EmbeddedPaymentElement.Configuration`. Same 4 brands and discover-network definition.

> See also [[source-stripe-inapp-filter-card-brands]] for the PaymentSheet/FlowController variant.

## Shared Facts (All Platforms)

- **Scope**: credit card form + Apple Pay cards
- **Two modes**: `allowed` (accept only listed brands) or `disallowed` (reject listed brands)
- **4 brand values**: visa, mastercard, amex, discover
- **discover** = entire Discover Global Network: Discover, Diners Club, JCB, UnionPay, Elo

## iOS (Swift)

Property: `EmbeddedPaymentElement.Configuration.cardBrandAcceptance`
Enum type: `EmbeddedPaymentElement.Configuration.CardBrandAcceptance.BrandCategory`

```swift
import StripePaymentSheet

var configuration = EmbeddedPaymentElement.Configuration()
configuration.cardBrandAcceptance = .allowed(brands: [.visa, .mastercard])
```

## Android (Kotlin/Compose)

Method: `.cardBrandAcceptance()` on `EmbeddedPaymentElement.Configuration.Builder`
Enum type: `PaymentSheet.CardBrandAcceptance.BrandCategory`

```kotlin
EmbeddedPaymentElement.Configuration.Builder("Powdur")
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

## React Native

Property: `cardBrandAcceptance` on `EmbeddedPaymentElementConfiguration`
Enum types: `PaymentSheet.CardBrandAcceptanceFilter` (Allowed/Disallowed), `PaymentSheet.CardBrandCategory`

```javascript
const elementConfig: EmbeddedPaymentElementConfiguration = {
  cardBrandAcceptance: {
    filter: PaymentSheet.CardBrandAcceptanceFilter.Allowed,
    brands: [
      PaymentSheet.CardBrandCategory.Visa,
      PaymentSheet.CardBrandCategory.Mastercard,
    ],
  },
};
```

## API Differences vs PaymentSheet Variant

| | PaymentSheet | EmbeddedPaymentElement |
| --- | --- | --- |
| iOS config type | `PaymentSheet.Configuration` | `EmbeddedPaymentElement.Configuration` |
| iOS enum namespace | `PaymentSheet.CardBrandAcceptance.BrandCategory` | `EmbeddedPaymentElement.Configuration.CardBrandAcceptance.BrandCategory` |
| Android | same `PaymentSheet.CardBrandAcceptance` | same `PaymentSheet.CardBrandAcceptance` |
| React Native | same `PaymentSheet.CardBrandCategory` | same `PaymentSheet.CardBrandCategory` |

## Related Pages

- [[stripe-inapp-payments]] — in-app payments concept page
- [[source-stripe-inapp-filter-card-brands]] — PaymentSheet/FlowController card brand filtering
- [[source-stripe-inapp-accept-payment-embedded]] — EmbeddedPaymentElement integration guide

## Raw Sources

- [[stripe-inapp-embedded-filter-card-brands-2025]] — verbatim guide (196 lines, iOS+Android+React Native, 1 image reused)
