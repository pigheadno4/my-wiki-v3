---
title: "Braintree PayPal App Switch (Beta) for iOS v7"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/paypal/app-switch/ios/v7"
raw_files:
  - "braintree/docs/guides/paypal/app-switch/ios/v7-2026-09-16.md"
tags: [braintree, paypal, ios, app-switch, vault, checkout, beta]
---

## Overview

This 2026-09-16 Braintree website snapshot documents the beta PayPal App Switch route for custom iOS v7 client integrations using [[braintree-ios-sdk]]. It covers one-time PayPal Checkout and PayPal Vault requests: after `tokenize` is called, the SDK attempts to open the PayPal app when it is installed and the user meets the documented eligibility conditions, and otherwise falls back to `ASWebAuthenticationSession`. This is Braintree integration evidence, not standalone `paypal/paypal-ios` behavior, current availability, merchant enablement, or successful payment execution.

## Key takeaways

- The page limits eligibility to US merchants and US customers using a custom client-side integration, and names both PayPal Vault and PayPal Checkout flows. Its availability statement also names one-time and vaulted payments across JavaScript, iOS, and Android; those statements remain qualifications from this dated snapshot, not proof of current account eligibility.
- The app must allowlist `paypal-app-switch-checkout`, configure a Universal Link with a dedicated Braintree return path, add that URL to the app association file, and register the fully qualified domain in the Braintree Control Panel. The registered value must match exactly, including `www.` when applicable.
- Initialize `BTPayPalClient` with the Universal Link and forward the returning URL to `BTAppContextSwitcher.sharedInstance.handleOpen(_:)` from the appropriate SwiftUI, scene-delegate, or app-delegate callback.
- To opt in, construct either `BTPayPalVaultRequest` or `BTPayPalCheckoutRequest` with `enablePayPalAppSwitch: true` and `userAuthenticationEmail`, then pass it to `BTPayPalClient.tokenize(_:completion:)`. The sample sends the returned PayPal nonce to the merchant server; it does not demonstrate the server transaction or its outcome.
- The page advises disabling the payment button immediately after a click and showing a loading indicator while the network call is in progress as duplicate-submission prevention and processing feedback; it does not present this UX guidance as an eligibility, SDK, or tokenization prerequisite.

> [!warning] Historical certificate notice
> The snapshot carries a March 30, 2026 mobile-SDK certificate-expiry warning and names iOS SDK `6.17.0+`, even though this URL is routed as iOS v7. Preserve that dated version tension: the notice does not establish current v7 support, certificate state, or a current upgrade target.

> [!warning] Environment documentation conflict
> This website snapshot documents Sandbox testing through a separately obtained TestFlight PayPal Sandbox app and requires removal of the Production PayPal app from the device. Independently retained implementation evidence summarized in [[braintree-ios-sdk]] records source comments limiting the beta app-switch API to production. Treat this as an environment/version documentation conflict; do not infer current Sandbox or Production operability from either route alone.

## Detail locators

- `IMPORTANT` (raw lines 17–18): historical mobile SDK certificate-expiry notice and its embedded iOS/Android version strings.
- `AVAILABILITY` and `ELIGIBILITY` (raw lines 23–40): stated platform/payment coverage, US/custom-integration conditions, installed-app attempt, and authentication-session fallback.
- Duplicate-submission UX guidance (raw line 42): button disabling and loading-indicator advice, not an eligibility, SDK, or tokenization prerequisite.
- `Using a custom UI` → `Get the SDK` (raw lines 45–74): optional custom button and CocoaPods, Swift Package Manager, and Carthage module setup.
- `Allowlist PayPal URL Scheme` (raw lines 77–90): `LSApplicationQueriesSchemes` entry.
- `Set Up Universal Links` and `Register Universal Link in Control Panel` (raw lines 92–137): dedicated return-path association and exact-domain registration procedure.
- `Set Universal Link in SDK` and `Handle App Context Switching` (raw lines 142–198): `BTPayPalClient` initialization and SwiftUI/scene/app delegate return handling.
- `Invoking the PayPal App Switch Flow` (raw lines 200–256): request opt-in fields, checkout/vault examples, completion result, and example nonce handoff.
- `Testing` (raw lines 258–260): Sandbox-only TestFlight app access and Production-app removal conditions.

## Related

- [[braintree]]
- [[braintree-ios-sdk]]
- [[paypal-braintree-integration]]

## Raw Sources

- [[raw/braintree/docs/guides/paypal/app-switch/ios/v7-2026-09-16|Braintree PayPal App Switch (Beta), iOS v7 — 2026-09-16 snapshot]]
