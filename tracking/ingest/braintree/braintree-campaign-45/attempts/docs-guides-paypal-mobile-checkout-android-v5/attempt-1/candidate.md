---
title: "Braintree PayPal Mobile Checkout — Android v5 Route"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/paypal/mobile-checkout/android/v5"
raw_files:
  - "braintree/docs/guides/paypal/mobile-checkout/android/v5-2026-09-16.md"
tags: [braintree, paypal, mobile-checkout, android, ios, eligibility, client-side]
---

## Overview

This 2026-09-16 [[braintree]] website snapshot is routed as Android v5, but its short body is a cross-platform eligibility and availability orientation for PayPal Mobile Checkout. It limits the feature to eligible merchants using a custom client-side integration, gives captured Android and iOS version floors, and names regional and integration exclusions. It does not document a native API, request or tokenization flow, server processing, or a transaction outcome.

The Android v5 URL must not be read as proof of exact Android v5 package behavior: the body itself says Android v4.13+ and iOS v5.11+. Its "not currently available" wording describes this captured website page, not independently verified current support. See [[braintree-android-sdk]] for separately versioned Android implementation evidence and [[paypal-braintree-integration]] for the broader Braintree-versus-direct-PayPal boundary.

## Key takeaways

- The page says PayPal Mobile Checkout is available to eligible merchants using a custom client-side integration. This condition is not evidence that a particular merchant, buyer, account, app, or transaction is eligible.
- The captured body says the feature is available only in Android v4.13+ and iOS v5.11+, and not for Drop-in UI or JavaScript. Those body-level platform statements coexist with the Android v5 route; they do not establish an installed dependency, current SDK support, or exact-package compatibility.
- The page names merchants and customers in the US, Canada, Europe, and the UK as eligible. It says customers in other regions can still use PayPal but will receive the standard web experience. It does not define country-by-country coverage, account enablement, device eligibility, or the boundary of "Europe."
- The page explicitly says this flow does not support in-person point-of-sale transactions or multi-seller payments. It provides no alternative integration or processing lifecycle for either case.

> [!warning] Snapshot and implementation boundary
> This dated website page records eligibility wording and exclusions only. Do not treat its Android v5 route, Android/iOS version floors, or server-side navigation as current support, native implementation, package/GitHub behavior, merchant enablement, successful authorization, capture, settlement, or funding evidence.

## Detail locators

- Source URL, fetch date and page metadata: raw lines 1-10.
- Eligible-merchant condition, custom client-side scope, Android/iOS version floors and Drop-in/JavaScript exclusion: **AVAILABILITY**, raw lines 17-18.
- Merchant and customer regional scope plus standard-web fallback for other customer regions: **ELIGIBILITY**, raw lines 23-28.
- Point-of-sale and multi-seller exclusions: **ELIGIBILITY**, raw lines 30-34.
- The server-side target at raw line 38 was not read for this entry and is navigation only, not evidence of server behavior.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-android-sdk]]
- Integration boundary: [[paypal-braintree-integration]]

## Related raw API references

The linked server-side page was not read for this entry. It is retained as navigation only and supplies no client/server lifecycle or transaction evidence here.

## Raw Sources

- [[raw/braintree/docs/guides/paypal/mobile-checkout/android/v5-2026-09-16|Braintree PayPal Mobile Checkout — Android v5 route (fetched 2026-09-16)]]
