---
title: "Braintree PayPal Commerce iOS SDK Setup"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/paypal-commerce-ios/setup"
raw_files:
  - "braintree/docs/guides/paypal-commerce-ios/setup-2026-09-16.md"
tags: [braintree, paypal-commerce, ios, sdk, oauth, apple-pay]
---

## Overview

This Braintree-hosted snapshot documents setup of the historical PayPal Commerce SDK for an iOS app. It covers CocoaPods installation, creation and client-side configuration of a PayPal Commerce OAuth client, app-delegate callbacks, optional Apple Pay and platform integrations, and three ways to present the SDK-provided store. It is distinct from the modular [[braintree-ios-sdk]], its independently versioned GitHub evidence, and ordinary Braintree checkout or Drop-in integration.

The page was fetched on 2026-09-16 and carries source frontmatter timestamps from 2025-04-02, but names no SDK release. Its Objective-C examples and references to iOS 9+, Spotlight, 3D Touch, Facebook login, and listed legacy iPhone models must therefore remain snapshot-scoped rather than being treated as current platform support.

## Key takeaways

- The documented quick-install path adds the `PayPalCommerce` pod directly from the Braintree `paypal-commerce-ios` Git repository. Apps not already using CocoaPods acknowledgements are told to include the linked PayPal Commerce acknowledgements file; a separate non-CocoaPods installation route is linked.
- Setup begins by adding the app in the PayPal Commerce Panel, copying a client ID and secret, importing PayPal Commerce, and configuring it from `application:didFinishLaunchingWithOptions:`. The page explicitly warns that the client ID and secret must be obfuscated. This records the page's historical setup instructions; it does not establish that an account or app is currently eligible, approved, or enabled.
- Apple Pay is conditional on creating an Apple merchant ID and certificate, enabling Apple Pay in the Commerce Panel, enabling the Xcode capability, and configuring the merchant ID. The page also prescribes `Info.plist` entries for status-bar behavior, transport exceptions, query schemes, 3D Touch shortcuts, and privacy-purpose strings; these are page-specific historical directions, not a universal minimum-platform or security baseline.
- Returning-user email login and PayPal login depend on a PayPal Commerce custom URL scheme and app-delegate URL forwarding. The page additionally calls for the bundle-identifier URL scheme. Multiple iOS apps using one PayPal Commerce store require separate OAuth clients so email verification remains functional.
- The page supplies optional app-delegate forwarding for push notification registration and receipt, Spotlight continuation, and 3D Touch shortcut actions. Its 3D Touch availability statement is limited to the specifically listed iPhone 6s/6s Plus/7/7 Plus-era devices in this snapshot.
- Store presentation can be modal, embedded through `paypalCommerceRootViewController` (for example in a tab bar), or standalone through `presentStoreApp` after client configuration. These setup calls and examples are not evidence that a live store was provisioned, a payment method was eligible, or any payment completed.

## Detail locators

- **Quick installation and licensing attribution:** `Quick installation`, raw lines 17–28.
- **OAuth client, SDK configuration, secret-obfuscation warning, and delegate option:** `Configure the client`, raw lines 29–54.
- **Apple Pay prerequisites and merchant-ID configuration:** `Apple Pay`, raw lines 55–67.
- **Historical `Info.plist` keys, exceptions, schemes, shortcuts, and privacy strings:** `Info.plist updates`, raw lines 69–158.
- **Email-based returning-user login, required custom schemes, multiple-app warning, and URL callback forwarding:** `Custom URL scheme for user login` and `URL handling`, raw lines 160–191.
- **Push notifications, Spotlight, 3D Touch availability/forwarding, and Facebook-login route:** raw lines 192–248.
- **Modal, embedded, and standalone store presentation:** `Present the store`, raw lines 249–283.
- **One OAuth client and URL scheme per iOS app sharing a store:** `Multiple iOS apps per store`, raw lines 284–290.

## Related

- [[braintree]]
- [[braintree-ios-sdk]] — modern modular Braintree iOS SDK retrieval route; do not transfer this historical PayPal Commerce SDK page's setup or platform claims to that package.

## Raw Sources

- [[raw/braintree/docs/guides/paypal-commerce-ios/setup-2026-09-16|Braintree PayPal Commerce iOS setup snapshot (fetched 2026-09-16)]]
