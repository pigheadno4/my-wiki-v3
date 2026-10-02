---
title: "Braintree iOS SDK v6-to-v7 migration"
type: source
date_ingested: 2026-10-02
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/client-sdk/migration/ios/v7"
raw_files:
  - "braintree/docs/guides/client-sdk/migration/ios/v7-2026-09-16.md"
tags: [braintree, ios, sdk, migration, swift]
---

## Overview

This collected [[braintree]] webpage is a version-specific migration guide for moving a native integration from Braintree iOS SDK v6 to v7. It characterizes v7 as a major release with breaking changes, then routes implementers through the minimum toolchain and deployment target, installation paths, initializer changes, renamed methods, Venmo return handling, and removal of PayPal Native Checkout. It is client-migration guidance rather than a full payment-flow or server-processing specification; use [[braintree-ios-sdk]] for the broader authorization, nonce and merchant-server boundary.

> [!warning] Snapshot and version boundary
> This is a 2026-09-16 snapshot of the iOS v7 migration route. It preserves the requirements and changes stated on that page but does not establish current package support, current account or payment-method eligibility, successful app switching, or successful payment processing.

## Key takeaways

- The guide says v7 internalizes creation of `BTAPIClient`, moves necessary flow parameters into initializers, and updates for newer iOS and Xcode versions. Its stated minimums are Xcode 16.2+, Swift 5.10+, and iOS 16.0; Objective-C applications must enable modules.
- The snapshot lists Swift Package Manager, CocoaPods and Carthage as installation routes. Its Carthage-specific requirement is v0.38.0+ with `carthage update --use-xcframeworks`; these are version-specific migration details, not proof of current installer support.
- The required-code-change sections move request properties to initializers across Card, Venmo, SEPA Direct Debit, Local Payments, 3D Secure and PayPal. They also show feature-client initializers accepting client authorization. This page does not specify how the authorization is generated or how a returned payment method is processed on the merchant server.
- For Venmo, the guide removes the `fallbackToWeb` request parameter: buyers with the Venmo app are sent to it, while buyers without it fall back to their default browser. It also requires a universal link when initializing `BTVenmoClient` for return from either path.
- The guide renames the Local Payment and 3D Secure `startPaymentFlow(with:completion)` methods to `start(with:completion)`. These and the many initializer examples are retained as raw locators rather than reconstructed API specifications.
- For PayPal app switch, the guide requires a simplified `paypal` URL query scheme in `Info.plist`. It separately says PayPal Native Checkout is no longer supported and instructs merchants to remove it and use the PayPal integration; the page does not call that replacement a web flow.

## Detail locators

- v7 rationale, internalized `BTAPIClient`, initializer pattern and changelog route: raw lines 17-29.
- Minimum Xcode, Swift and iOS requirements plus Objective-C module setting: raw lines 32-36.
- Supported installation routes and Carthage v0.38.0+ command: raw lines 39-55.
- Card initializer-only properties and client initializer example: raw lines 58-64.
- Venmo initializer-only properties, browser fallback behavior and required universal link: raw lines 67-77.
- SEPA Direct Debit request and client initializer changes: raw lines 79-91.
- Local Payment request/client changes and renamed start method: raw lines 93-109.
- 3D Secure request/client changes and renamed start method: raw lines 111-129.
- PayPal request/client changes, app-switch query scheme and PayPal Native Checkout removal: raw lines 131-147.
- American Express, Apple Pay, Data Collector, Shopper Insights and PayPal Messaging client initializer examples: raw lines 149-185.

## Related

- [[braintree-ios-sdk]] - native iOS SDK architecture, exact-version evidence boundaries and independently versioned Drop-in distinction.
- [[source-braintree-client-sdk-deprecation-policy-ios-v7]] - separate historical platform and lifecycle policy snapshot; not current v7 support evidence.
- [[source-github-braintree-ios]] - separate cumulative exact-SHA implementation evidence; this website migration snapshot does not replace it.

## Raw Sources

- [[raw/braintree/docs/guides/client-sdk/migration/ios/v7-2026-09-16|Braintree iOS SDK v6-to-v7 migration snapshot (2026-09-16)]]
