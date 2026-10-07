---
title: "Braintree PayPal Mobile Checkout - JavaScript v3 route"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/paypal/mobile-checkout/javascript/v3"
raw_files:
  - "braintree/docs/guides/paypal/mobile-checkout/javascript/v3-2026-09-16.md"
tags: [braintree, paypal, mobile-checkout, javascript-v3, android, ios, deprecation]
---

## Overview

This fully read [[braintree]] website snapshot is stored at a JavaScript v3 route, but its retained body is a short availability and removal notice for PayPal Mobile Checkout on Android and iOS custom client-side integrations. It directs migration to web checkout integration routes and contains no setup, tokenization, server-processing or payment-execution procedure.

## Key takeaways

- The page says PayPal Mobile Checkout will be removed in the next major version and directs merchants to separate Android or iOS web checkout integration routes. It does not name that major version or document the migration steps.
- In this snapshot, the feature is described as available only to eligible merchants using a custom client-side integration on Android v4.13+ or iOS v5.11+. The same notice explicitly says it is not currently available for Drop-in UI or JavaScript, despite the JavaScript v3 URL.
- The stated merchant and customer regions are the US, Canada, Europe and the UK. Customers in other regions are described as still able to complete a PayPal transaction, but through the standard web experience rather than PayPal Mobile Checkout.
- The notice excludes in-person point-of-sale transactions and multi-seller payments.

## Evidence boundaries

> [!warning] Route and platform mismatch
> The canonical URL is JavaScript v3-routed, while the retained body explicitly excludes JavaScript and describes Android/iOS SDK-family availability. Do not use the route name as JavaScript implementation evidence or infer native setup behavior absent from the page.

> [!warning] Historical snapshot, not current availability
> The page was captured on 2026-09-16 and says removal will occur in an unnamed next major version. That preserves the captured documentation state, not present support, a removal version, merchant enablement, customer eligibility, successful migration or payment execution.

> [!warning] Website scope is separate from exact package history
> The Android v4.13+ and iOS v5.11+ labels are website statements, not commit-qualified GitHub or exact installed-package evidence. They must not replace the separately retained [[braintree-android-sdk]] or [[braintree-ios-sdk]] histories.

## Detail locators

- Next-major removal and Android/iOS web checkout migration navigation: raw line 17.
- Eligible-merchant and custom-client condition, Android v4.13+/iOS v5.11+ floor, and Drop-in/JavaScript exclusion: raw lines 20-21.
- Merchant/customer region list and other-region standard-web-experience condition: raw lines 24-25.
- In-person PoS and multi-seller exclusions: raw lines 25-27.

## Related

- Company: [[braintree]]
- Main payment-method context: [[braintree-payment-methods]]
- Native Android SDK context and separate versioned GitHub history: [[braintree-android-sdk]]
- Native iOS SDK context and separate versioned GitHub history: [[braintree-ios-sdk]]

## Related raw API references

- [Android v4 web checkout route](https://developer.paypal.com/braintree/docs/guides/paypal/checkout-with-paypal/android/v4) - unread navigation linked by the removal notice; no target-page behavior is inferred.
- [iOS v6 web checkout route](https://developer.paypal.com/braintree/docs/guides/paypal/checkout-with-paypal/ios/v6) - unread navigation linked by the removal notice; no target-page behavior is inferred.

## Raw Sources

- [[raw/braintree/docs/guides/paypal/mobile-checkout/javascript/v3-2026-09-16|Braintree PayPal Mobile Checkout - JavaScript v3 route]] - fully read pinned website snapshot containing the removal, platform availability, regional eligibility and unsupported-use notices
