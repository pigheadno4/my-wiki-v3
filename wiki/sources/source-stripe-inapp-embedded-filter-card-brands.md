---
title: "Filter Card Brands — EmbeddedPaymentElement"
type: source
date_ingested: 2026-04-22
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/mobile/embedded-filter-card-brands"
raw_files:
  - "stripe-inapp-embedded-filter-card-brands-2025.md"
tags: [stripe, mobile, ios, android, react-native, embedded-payment-element, card-brand-filtering, card-brands]
---

## Summary

[[stripe]]’s April 22, 2026 guide explains card-brand filtering in the Mobile Embedded Payment Element for iOS, Android and React Native. It assumes a Stripe account and an existing [[source-stripe-inapp-accept-payment-embedded|Mobile Embedded Payment Element integration]]. The November 7 capture identifies the same three platform routes and provides navigation. The April full capture supplies the implementation examples.

## April 22, 2026 — Filter and Examples

For the card form, allow only the listed brands with `allowed` or exclude the listed brands with `disallowed`. The four documented categories are Visa, Mastercard, Amex and Discover. Discover includes Discover, Diners Club, JCB, UnionPay and Elo through Discover Global Network. The guide uses a nonempty Visa and Mastercard allow list on each platform.

| Platform | Dated example configuration |
| --- | --- |
| iOS | Set `cardBrandAcceptance` on an `EmbeddedPaymentElement.Configuration` instance to `.allowed(brands: [.visa, .mastercard])`. The April prose names `EmbeddedPaymentElement.Configuration.CardBrandAcceptance.BrandCategory`. See the retained package qualification below. |
| Android | Call `cardBrandAcceptance` on `EmbeddedPaymentElement.Configuration.Builder`, passing the shared `PaymentSheet.CardBrandAcceptance.allowed` with its Visa and Mastercard categories. |
| React Native | Set `cardBrandAcceptance` on `EmbeddedPaymentElementConfiguration`. The example uses `PaymentSheet.CardBrandAcceptanceFilter.Allowed` and `PaymentSheet.CardBrandCategory.Visa` and `.Mastercard`. |

The April iOS, Android and React Native examples and test-card instructions are at lines 12-57, 63-133 and 139-195, respectively. Those instructions describe how to check whether the UI accepts or blocks a test brand. See [[source-stripe-inapp-filter-card-brands]] for the separate PaymentSheet and Flow Controller guide.

## Platform and SDK Boundaries

**iOS.** The retained StripePaymentSheet 26.11.0 snapshot (`2026-09-30-7037819`) exposes `cardBrandAcceptance` on the distinct Embedded configuration. `EmbeddedPaymentElement.CardBrandAcceptance` and `EmbeddedPaymentElement.BrandCategory` alias `PaymentSheet.CardBrandAcceptance` and its category. The captured Embedded setting defaults to `.all`, applies the filter to `PKPaymentRequest.supportedNetworks` for its Apple Pay flow, describes a client-side control and excludes Link filtering. A dedicated Apple Pay button uses a separate configuration route in the April Embedded acceptance guide.

**Android.** The April Embedded filter guide repeats “Apple Pay” in its Android paragraph. The separate April Android PaymentSheet filter guide names Google Pay, and the April Embedded acceptance guide documents an Android Google Pay configuration and a separate dedicated button route. The retained Android PaymentSheet 23.25.1 defines the shared category and `all()`, `allowed()` and `disallowed()` used by the dated Embedded builder example. The Android setup passages and configuration types leave actual Embedded Google Pay network filtering unverified.

**React Native.** In 0.84.0 (`2026-10-29-33ef1ee`), the Embedded configuration scopes `applePay` to iOS and `googlePay` to Android. The interface describes card-brand filtering as client-side, excludes Link filtering and uses the shared PaymentSheet union for all, allow and disallow. The native Embedded bridges forward that setting. The Android bridge falls back to `all()` when an allow or disallow brands list is missing or contains no recognized brands. With a provided array of strings, the iOS bridge returns the selected filter with the mapped array, even if it is empty. These are versioned input-mapping behaviors. They leave server authorization and actual checkout outcomes unverified.

## Retained SDK Locators

- StripePaymentSheet 26.11.0, snapshot `2026-09-30-7037819`: `StripePaymentSheet.podspec` lines 1-9, `EmbeddedPaymentElementConfiguration.swift` lines 133-138, `EmbeddedPaymentElement.swift` lines 593-611, and `PaymentSheetConfiguration.swift` lines 846-871.
- Android PaymentSheet 23.25.1, snapshot `2026-10-27-bb0d8d0`: `gradle.properties` lines 25-27 and `PaymentSheet.kt` lines 1185-1196 and 3540-3602.
- React Native 0.84.0, snapshot `2026-10-29-33ef1ee`: `src/types/EmbeddedPaymentElement.tsx` lines 133-145 and 191-197, `src/types/PaymentSheet.ts` lines 743-789, `ios/StripeSdkImpl+Embedded.swift` lines 337-344, `ios/StripeSdkImpl+PaymentSheet.swift` lines 261-299, `EmbeddedPaymentElementViewManager.kt` lines 150-165, and `PaymentElementConfig.kt` lines 220-253.

## Related Pages

- [[stripe-inapp-payments]] — native UI and payment configuration context.
- [[source-stripe-inapp-filter-card-brands]] — separate PaymentSheet and Flow Controller filter guide.
- [[source-stripe-inapp-accept-payment-embedded]] — Embedded integration and platform wallet setup.

## Raw Sources

- [[raw/stripe-inapp-embedded-filter-card-brands-2025|Stripe’s April 22, 2026 Embedded Payment Element card-brand guide]] — 195 lines, iOS, Android and React Native, with one reused image.

## Related raw API references

- [[raw/stripe-payments-mobile-embedded-filter-card-brands-2026-11-07|Embedded Payment Element card-brand variant index]] — November 7, 2026 capture, iOS, Android and React Native navigation.
