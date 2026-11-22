---
title: "Address Element — Mobile Overview"
type: source
date_ingested: 2026-04-22
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/mobile/address-element"
raw_files:
  - "stripe-inapp-address-element-2025.md"
tags: [stripe, mobile, ios, android, react-native, address-element, autocomplete, billing-address, shipping-address]
---

## Summary

The April 22, 2026 overview describes an embeddable UI for collecting complete shipping and billing addresses in an app, including full billing addresses for uses such as tax. The November 7, 2026 parent page links to iOS, Android and React Native overview variants. The separate [[source-stripe-inapp-collect-addresses|Collect addresses implementation guide]] provides April implementation details. Its November parent page has four links because it splits iOS into UIKit and SwiftUI.

## April 2026 Features

- **236 regional address formats**, including right-to-left formats.
- **Autocomplete.** The overview describes built-in suggestions. The implementation guide says iOS enables autocomplete by default. Android, including React Native on Android, requires the Google Places SDK and API key to enable suggestions. The captures give no measured conversion improvement.
- **Saved-address prefill.** An address can be prefilled when it is already saved for the customer.
- **Appearance API.** Configure the component’s appearance to match the integration.
- **Availability.** The April overview lists availability for web, iOS, Android and React Native SDKs. Its iOS section describes integration and data passing with Payment Sheet and Payment Element. Its Android and React Native sections name Payment Element and Link. These descriptions are specific to the April variants.

## Address data in mobile and web integrations

In the April mobile implementation guide, the documented iOS UIKit and Android examples optionally pass the collected address as `PaymentSheet.Configuration.shippingDetails`. React Native uses `defaultShippingDetails`. When populated, the payment UI prefills billing and shows an option to use the shipping address for billing. The guide documents `PaymentIntent.shipping` when the intent is confirmed with the configured details. Completing the mobile address UI or prefilling fields does not confirm payment or automatically persist an address server-side.

The separate [[source-stripe-address-element|web Address Element]] guide documents routing address and payment data on confirmation when the components share a Stripe.js Elements instance. See [[stripe-address-element]] for that web route.

## Images

![iOS address autocomplete flow](../raw/assets/stripe-inapp-address-element-ios-overview.png)
![Android address autocomplete flow](../raw/assets/stripe-inapp-address-element-android-overview.png)

## Related Pages

- [[stripe-inapp-payments]] — mobile payments concept
- [[source-stripe-inapp-payment-sheet]] — Payment Sheet
- [[source-stripe-inapp-accept-payment-embedded]] — EmbeddedPaymentElement
- [[stripe]] — Stripe company profile

## Raw Sources

- [[raw/stripe-inapp-address-element-2025|Mobile Address Element overview, captured 2026-04-22]] — verbatim overview page (66 lines, 2 images)

## Related raw API references

- [[raw/stripe-payments-mobile-address-element-2026-11-07|Mobile Address Element overview variant index]] — 2026-11-07 navigation capture for iOS, Android and React Native.
