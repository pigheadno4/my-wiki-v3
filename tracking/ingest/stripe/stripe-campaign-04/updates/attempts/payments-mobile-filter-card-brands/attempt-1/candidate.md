---
title: "Filter Card Brands — Mobile"
type: source
date_ingested: 2026-04-22
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/mobile/filter-card-brands"
raw_files:
  - "stripe-inapp-filter-card-brands-2025.md"
tags: [stripe, mobile, ios, android, react-native, card-brand-filtering, payment-sheet, apple-pay, google-pay]
---

## Summary

The April 22, 2026 guide shows how to filter card brands in the mobile PaymentSheet UI, after creating or signing in to a Stripe account and integrating the Mobile Payment Element. The November 7 base capture retains the purpose and routes to iOS, Android, and React Native variants. The configuration and test instructions below come from April or the separately identified SDK declarations.

## Brand and wallet scope

The April guide uses `allowed` to admit only listed card brands and `disallowed` to exclude listed brands. Its examples use Visa, Mastercard, Amex, and Discover. The Discover category includes the entire Discover Global Network group named in the guide: Discover, Diners Club, JCB, UnionPay, and Elo.

The April PaymentSheet guide describes the card form on all three platforms, Apple Pay on iOS and React Native, and Google Pay on Android. The distinct [[source-stripe-inapp-embedded-filter-card-brands]] guide uses `EmbeddedPaymentElement.Configuration.CardBrandAcceptance.BrandCategory` on iOS. Its April Android prose names Apple Pay, while the April PaymentSheet Android variant names Google Pay. That wording is scoped to its own capture and establishes no Android Apple Pay behavior. Both November base pages are navigation indexes.

## Client and confirmation boundary

The retained iOS `2026-09-30-3410ff0` `PaymentSheetConfiguration.swift` lines 230–235, Android `2026-10-27-b792b5d` `PaymentSheet.kt` lines 1185–1196, and React Native 0.76.0 `2026-10-04-ee6e868` `src/types/PaymentSheet.ts` lines 81–87 describe the filter as client-side and say it does not support Link in those snapshots. The React Native declaration also has an `All` default, separate from the explicitly configured `Allowed` and `Disallowed` modes (lines 758–789).

The filter governs the documented client UI. The separate [[source-stripe-inapp-finalize-payments-server]] flow passes a ConfirmationToken to the server, where it creates and attempts to confirm a PaymentIntent, then returns the client secret for the SDK to handle any next actions. UI eligibility and a client secret establish neither server-side brand enforcement nor successful authorization or capture.

## April platform configuration fragments


### iOS (Swift)

Set `cardBrandAcceptance` on `PaymentSheet.Configuration`. The Swift capture joins the configuration declaration and assignment on raw line 48. This fragment isolates the assignment.

```swift
configuration.cardBrandAcceptance = .allowed(brands: [.visa, .mastercard])
// or: .disallowed(brands: [.amex])
```

### Android (Kotlin)

The April variant shows the builder and passes the built configuration to `presentWithPaymentIntent(paymentIntentClientSecret, configuration)`.

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

Pass this property inside `initPaymentSheet`. The April raw joins `cardBrandAcceptance` to the preceding comment and its shown import omits the `PaymentSheet` enum namespace (raw lines 155–175). The retained 0.76.0 `PaymentSheetDeferredIntentScreen.tsx` imports `PaymentSheet` at lines 3–11 and shows the option inside initialization at lines 91–106. These fragments illustrate the configuration and do not establish execution.

```javascript
cardBrandAcceptance: {
  filter: PaymentSheet.CardBrandAcceptanceFilter.Allowed, // or Disallowed
  brands: [PaymentSheet.CardBrandCategory.Visa, PaymentSheet.CardBrandCategory.Mastercard],
}
```

## Historical tests and screenshots

The April guide uses Stripe's test cards to check whether the Mobile Payment Element accepts or blocks the intended brands in the UI. See its iOS lines 54–57, Android lines 118–121, and React Native lines 177–180. The screenshots show the historical disallowed-card presentation. The captured React Native block references the same screenshot asset as iOS.

![iOS card brand filtering](../raw/assets/stripe-inapp-filter-card-brands-ios.png)
![Android card brand filtering](../raw/assets/stripe-inapp-filter-card-brands-android.png)

## Related Pages

- [[stripe]] — provider and source catalog
- [[stripe-inapp-payments]] — mobile PaymentSheet and embedded surface boundaries
- [[source-stripe-inapp-payment-sheet]] — PaymentSheet configuration
- [[source-stripe-inapp-embedded-filter-card-brands]] — parallel EmbeddedPaymentElement guide
- [[source-stripe-inapp-finalize-payments-server]] — separate ConfirmationToken and PaymentIntent flow

## Related raw API references

- [[raw/stripe-payments-mobile-filter-card-brands-2026-11-07]] — navigation index, November 7, 2026, linking to iOS, Android, and React Native variants
- [[raw/stripe-payments-mobile-embedded-filter-card-brands-2026-11-07]] — separate EmbeddedPaymentElement navigation index, November 7, 2026

## Raw Sources

- [[raw/stripe-inapp-filter-card-brands-2025]] — complete April 22, 2026 PaymentSheet card-brand filter capture across iOS, Android, and React Native
