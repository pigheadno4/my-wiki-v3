---
title: "Braintree PayPal Client-Side Implementation for iOS v7"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/paypal/client-side/ios/v7"
raw_files:
  - "braintree/docs/guides/paypal/client-side/ios/v7-2026-09-16.md"
tags: [braintree, paypal, ios, mobile, client-sdk, tokenization]
---

## Overview

This 2026-09-16 snapshot of [[braintree]]'s iOS v7-routed client-side PayPal guide covers SDK setup and SDK-managed PayPal buttons that present an `ASWebAuthenticationSession`, launch PayPal authentication, and tokenize the result for a final nonce callback. It is captured website guidance for [[braintree-ios-sdk]], not proof of current package support, account eligibility, fallback behavior, or a completed payment transaction.

> [!warning] Captured certificate deadline
> The page says Braintree Mobile SDK SSL certificates were set to expire on March 30, 2026, directs iOS integrations to SDK 6.17.0 or newer for the replacement certificates, and warns that traffic from published app versions retaining older SDK certificates would fail unless those versions were decommissioned or force-upgraded by the deadline. This dated wording on an iOS v7 route does not establish current certificate, lifecycle, or exact-package status; separately retained package evidence belongs to [[braintree-ios-sdk]].

## Key takeaways

- Before adding PayPal, the guide routes the merchant to integrate the Braintree iOS SDK and create, verify, and link a PayPal account in the Braintree Control Panel.
- Installation examples use the `Braintree` CocoaPod; Swift Package Manager names `BraintreePayPal` and `PayPalDataCollector`; Carthage names `BraintreeCore`, `BraintreePayPal`, `BraintreeDataCollector`, and `PPRiskMagnes`. These captured setup names are not evidence of current package compatibility.
- The page says initiating PayPal authorization presents and dismisses an `ASWebAuthenticationSession` from the top-most view. It does not document a PayPal app-switch branch or state a condition under which this session is a fallback, so no fallback or current runtime behavior should be inferred.
- The SDK payment button handles its loading and disabled state, invokes tokenization with the supplied request, and reports a nonce or error. The page characterizes its internal scope as authentication through tokenization; the final nonce still is not evidence of server-side transaction creation, authorization, capture, settlement, or funding.
- The SwiftUI and UIKit-wrapped examples construct `BTPayPalCheckoutRequest(amount: "10.00")` and a `PayPalButton`; the amount, color, width, and callback branches are examples rather than guarantees or a complete transaction procedure.
- Further configuration branches into One-Time Payments, Vaulted Payments, or Recurring Payments. Those linked pages are navigation rather than evidence read for this entry.

## Detail locators

- Historical mobile SSL-certificate expiry, stated iOS 6.17.0+ remediation, and affected-version traffic consequence: first IMPORTANT block, raw lines 17-22; repeated iOS-only notice at raw lines 116-119.
- Braintree iOS SDK and linked PayPal-account prerequisites: `## Setup`, raw lines 27-34.
- CocoaPods, Swift Package Manager, and Carthage setup names: `### Get the SDK`, raw lines 36-52.
- `ASWebAuthenticationSession` presentation and dismissal: `## Showing a PayPal button`, raw lines 53-55.
- SDK payment-button responsibilities and authentication-through-tokenization scope: `### Using our Payment Buttons`, raw lines 56-60.
- SwiftUI request, button, styling, and nonce/error callback example: raw lines 63-82.
- UIKit-wrapped SwiftUI example: raw lines 83-105.
- Additional-data route and linked header-file documentation: raw lines 107-113.
- One-Time, Vaulted, and Recurring next-step routes: `## Next: Choose your integration`, raw lines 122-131.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-ios-sdk]]

## Related raw API references

The captured page links to Braintree iOS SDK setup, PayPal account setup, Braintree iOS PayPal header files, One-Time Payments, Vaulted Payments, Recurring Payments, and a Vault-versus-Checkout comparison. Those linked targets were not read for this entry and are retained only as navigation.

## Raw Sources

- [[raw/braintree/docs/guides/paypal/client-side/ios/v7-2026-09-16|Braintree PayPal Client-Side Implementation for iOS v7 (captured 2026-09-16)]]
