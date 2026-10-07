---
title: "Braintree PayPal Mobile Checkout - iOS v7 Route"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/paypal/mobile-checkout/ios/v7"
raw_files:
  - "braintree/docs/guides/paypal/mobile-checkout/ios/v7-2026-09-16.md"
tags: [braintree, paypal, mobile-checkout, ios-v7, android, custom-integration]
---

## Overview

This fully read 2026-09-16 [[braintree]] website snapshot is stored at an iOS v7 route, but its retained body is a brief cross-platform availability and regional-eligibility notice for PayPal Mobile Checkout in custom native-mobile client integrations. It names Android v4.13+ and iOS v5.11+ rather than documenting an iOS v7 API, setup procedure, tokenization flow, server handoff or payment lifecycle.

## Key takeaways

- The captured notice describes PayPal Mobile Checkout as available only to eligible merchants using a custom client-side integration, with Android v4.13+ and iOS v5.11+ named as version floors. These are website statements preserved from the snapshot, not exact installed-package or GitHub revision evidence.
- The same body says the feature is not currently available for Drop-in UI or JavaScript. Despite the iOS v7 URL, it gives no iOS v7-specific method, request type, callback or SDK-installation instructions.
- The stated eligible merchant and customer regions are the US, Canada, Europe and the UK. Customers in other regions are described as able to complete a PayPal transaction through the standard web experience rather than PayPal Mobile Checkout.
- The capture ends immediately after saying the flow does not support "the following"; the missing list cannot be reconstructed from this raw, so no unsupported transaction types or use cases are asserted here.

## Evidence boundaries

> [!warning] Route, SDK and history boundary
> The canonical URL is iOS v7-routed, while the retained body also discusses Android and names only an iOS v5.11+ floor. Do not treat the route label as iOS v7 implementation evidence or merge these website statements into the separately versioned [[braintree-ios-sdk]] GitHub history.

> [!warning] Historical snapshot, incomplete capture
> This page was captured on 2026-09-16, and its wording preserves that documentation snapshot rather than proving current support, merchant or customer eligibility, account enablement, exact SDK compatibility, browser/native runtime behavior or payment execution. The raw ends before the promised unsupported-flow list.

## Detail locators

- Source URL, fetch date, discovery channels and page metadata: raw lines 1-10.
- Eligible-merchant/custom-client condition, Android v4.13+ and iOS v5.11+ labels, and Drop-in UI/JavaScript exclusion: `AVAILABILITY`, raw lines 16-17.
- Merchant/customer regions, other-region standard-web-experience condition and truncated unsupported-flow introduction: `ELIGIBILITY`, raw lines 20-22.

## Related

- Company: [[braintree]]
- Main concept and separate exact-version implementation history: [[braintree-ios-sdk]]
- Braintree PayPal processing context: [[paypal-braintree-integration]]

## Raw Sources

- [[raw/braintree/docs/guides/paypal/mobile-checkout/ios/v7-2026-09-16|Braintree PayPal Mobile Checkout - iOS v7 route (captured 2026-09-16)]] - fully read pinned website snapshot containing the short availability and eligibility notice and its truncated unsupported-flow introduction
