---
title: "Braintree PayPal Commerce iOS PayPalCommerceDelegate"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/paypal-commerce-ios/paypal-commerce-delegate"
raw_files:
  - "braintree/docs/guides/paypal-commerce-ios/paypal-commerce-delegate-2026-09-16.md"
tags: [braintree, paypal-commerce, ios, sdk, delegate]
---

## Overview

This Braintree-hosted snapshot documents `PayPalCommerceDelegate` for the historical PayPal Commerce iOS SDK. After client configuration, the delegate can receive store-dismissal callbacks when the store is presented modally, or tell an app using an embedded store and custom purchase buttons to make that store visible. These are client-side presentation and lifecycle responsibilities, not a server-side payment flow.

The page was fetched on 2026-09-16 and carries source frontmatter timestamps from 2025-04-01, but identifies no SDK release or environment. Treat its Objective-C protocol methods as historical, unversioned snapshot evidence distinct from the modern modular [[braintree-ios-sdk]] and its separately versioned GitHub implementation evidence; the page does not establish current availability, exact-package support, runtime behavior, store provisioning, or successful payment execution.

## Key takeaways

- For a modally presented store, the page says to set the delegate after configuring the client. An implementation may provide either or both of `paypalCommerceWillDismissWithTransitionDuration:` and `paypalCommerceDidDismiss` to receive dismissal lifecycle callbacks.
- For a store embedded in a tab bar controller or similar container where custom buttons trigger purchases, the app is responsible for displaying the store. After setting the delegate, it implements `paypalCommerceShouldBeVisible` and makes the store visible in that callback.
- The tab-bar example says to make the store's view controller the `selectedViewController`. This is an example of fulfilling the visibility responsibility, not a universal container requirement or proof that a purchase completed.

## Detail locators

- **Modal presentation condition and post-configuration delegate setup:** raw lines 16-23.
- **Optional modal dismissal protocol callbacks:** raw lines 24-29.
- **Embedded/custom-button condition and app-owned display responsibility:** raw lines 31-37.
- **Visibility callback and tab-bar example:** raw lines 38-44.

## Related

- [[braintree]]
- [[braintree-ios-sdk]] — modern modular Braintree iOS SDK retrieval route; do not transfer this historical PayPal Commerce delegate API to that package.
- [[source-braintree-docs-guides-paypal-commerce-ios-overview|Braintree PayPal Commerce iOS SDK Overview]]
- [[source-braintree-docs-guides-paypal-commerce-ios-setup|Braintree PayPal Commerce iOS SDK Setup]]

## Raw Sources

- [[raw/braintree/docs/guides/paypal-commerce-ios/paypal-commerce-delegate-2026-09-16|Braintree PayPal Commerce iOS PayPalCommerceDelegate snapshot (fetched 2026-09-16)]]
