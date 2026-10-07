---
title: "Braintree PayPal Pay Later Messaging for iOS v7"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/paypal/messaging/ios/v7"
raw_files:
  - "braintree/docs/guides/paypal/messaging/ios/v7-2026-09-16.md"
tags: [braintree, paypal, pay-later, messaging, ios, sdk]
---

## Overview

This 2026-09-16 snapshot of a [[braintree]] website guide on the iOS v7 route documents how a native iOS app can display a PayPal Pay Later message view with customized payment offers through the [[braintree-ios-sdk]]. The page describes creating an authorized `BTAPIClient`, constructing a `BTPayPalMessagingView` and `BTPayPalMessagingRequest`, placing the view, and starting the request. It is documentation evidence, not proof of current SDK availability, merchant or customer eligibility, runtime rendering, offer approval, or payment execution.

## Key takeaways

- The captured page says Pay Later Messaging is available to merchants using the latest iOS and Android SDKs and is unavailable through Drop-in. Although this source is routed under iOS v7, it does not name an exact iOS package release.
- The page limits availability to eligible merchants in the US, GB, DE, FR, IT, ES, and AU. Its integration conditions include being a current Braintree merchant, using the latest Braintree integration, building native apps with the iOS or Android SDK, and having a one-time payment integration where Pay Later options are available through PayPal checkout.
- Merchants must follow the linked PayPal Acceptable Use Policy and must not add content, wording, marketing, or other material to Pay Later messages to encourage product use; the page says PayPal reserves the right to act under the linked User Agreement. It also says categories such as Real Money Gaming are ineligible to promote Pay Later offers and that additional ineligible categories may be identified periodically.
- The iOS invocation sequence creates `BTAPIClient` with a client token or tokenization key, then launches `BTPayPalMessagingView` with `BTPayPalMessagingRequest`. The sample's amount, page type, logo, alignment, color, layout, and re-render call are illustrative implementation detail rather than universal requirements.
- `BTPayPalMessagingDelegate` is optional and exposes selection, application-start, appearance/loading, rendered, and error lifecycle events.

## Detail locators

- Availability, eligible countries, merchant/integration conditions, content restrictions, category exclusions, and described experience: raw lines 17–38.
- CocoaPods, Swift Package Manager, and Carthage dependency/framework instructions: raw lines 41–62.
- `BTAPIClient`, `BTPayPalMessagingView`, request construction, view layout, `start`, and optional re-render example: raw lines 65–107.
- Optional delegate example and lifecycle callbacks: raw lines 108–136.
- `BTPayPalMessagingView` authorization argument and `BTPayPalMessagingRequest` arguments, values, and defaults: raw lines 138–180.
- Delegate method reference: raw lines 183–193.

## Related

- [[braintree-ios-sdk]]
- [[braintree]]

## Raw Sources

- [[raw/braintree/docs/guides/paypal/messaging/ios/v7-2026-09-16|Braintree PayPal Pay Later Messaging — iOS v7 (2026-09-16)]]
