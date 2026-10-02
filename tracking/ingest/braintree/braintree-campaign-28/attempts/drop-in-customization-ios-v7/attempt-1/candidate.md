---
title: "Braintree Drop-in Customization for iOS v7 (Route Notice)"
type: source
date_ingested: 2026-10-02
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/drop-in/customization/ios/v7"
raw_files:
  - "braintree/docs/guides/drop-in/customization/ios/v7-2026-09-16.md"
tags: [braintree, ios, drop-in, sdk-lifecycle, deprecation]
---

## Overview

This 2026-09-16 snapshot of a [[braintree]] webpage is titled Customization and sits on an iOS v7 Drop-in route, but its retained body consists of Drop-in lifecycle and SDK-routing notices. It directs merchants toward the modular [[braintree-ios-sdk]] while also saying that iOS v7 is not currently supported through Drop-in.

> [!warning] Route and snapshot boundary
> The `/ios/v7` URL does not prove a v7-compatible Drop-in implementation. The retained body explicitly routes Drop-in users to a v5 implementation guide. This snapshot establishes only what the page said when collected; it is not current support, merchant eligibility, integration-success or payment-processing evidence.

## Key takeaways

- The page schedules Drop-in SDK deprecation for October 1, 2026. It says no new features, improvements or bug fixes will be released after that date, while payment processing will continue to be supported until October 1, 2027.
- It schedules unsupported status for October 1, 2027, after which the Braintree support team will no longer assist with the SDK and payment processing may be suspended at any time. These are documented lifecycle statements, not an observed processing result.
- The stated action is to migrate to the Braintree iOS SDK for ongoing updates, security fixes and support. The main iOS concept preserves the boundary between that modular native SDK and the independently versioned Drop-in package.
- A separate note says the iOS v7 SDK is not currently supported through Drop-in and points Drop-in users to the v5 implementation guide.

## Detail locators

- Drop-in deprecation date, end of feature and bug-fix releases, and stated processing-support window: raw lines 17-18.
- Unsupported date, end of support-team assistance, and possible processing suspension: raw line 20.
- Migration action and alternative Braintree iOS SDK route: raw line 22.
- iOS v7 incompatibility notice and v5 Drop-in guide route: raw lines 27-28.

## Related

- [[braintree]] - provider and product-family context.
- [[braintree-ios-sdk]] - modular native iOS SDK and independently versioned Drop-in boundary.
- [[source-braintree-client-sdk-deprecation-policy-ios-v7]] - historical lifecycle-policy snapshot; not current version-status evidence.
- [[source-braintree-client-sdk-migration-ios-v7]] - website v6-to-v7 migration guide for the modular native SDK.

## Raw Sources

- [[raw/braintree/docs/guides/drop-in/customization/ios/v7-2026-09-16|Braintree Drop-in customization iOS v7 route snapshot (2026-09-16)]]
