---
title: "Braintree PayPal Pay Later Messaging — Android v5"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/paypal/messaging/android/v5"
raw_files:
  - "braintree/docs/guides/paypal/messaging/android/v5-2026-09-16.md"
tags: [braintree, paypal, pay-later, android, mobile-sdk, messaging]
---

## Overview

This 2026-09-16 snapshot of a Braintree Android v5-routed website guide describes adding PayPal Pay Later offer messaging to a native Android app. The captured page says the feature is available to eligible merchants using the latest iOS and Android SDKs, but not to merchants using Drop-in; those statements describe the snapshot and do not establish current SDK support, merchant eligibility, offer availability, credit approval, or payment execution. See [[braintree]] and [[braintree-android-sdk]].

## Key takeaways

- The page limits eligibility to merchants in the US, GB, DE, FR, IT, ES, and AU that are current Braintree merchants, use the latest Braintree integration, build native apps with the iOS or Android SDKs, and have a one-time payment integration where Pay Later options are available through PayPal checkout. It also requires compliance with the PayPal Acceptable Use Policy.
- Merchants must not add content, wording, marketing, or other material to Pay Later messages to encourage use. The page says certain categories, including Real Money Gaming, cannot promote Pay Later offers and that additional categories may periodically be found ineligible.
- The captured setup adds `com.braintreepayments.api:paypal-messaging:5.0.0`. The example creates a `PayPalMessagingRequest`, constructs a `PayPalMessagingView` with Android context and an authorization string, calls `start(request)`, sizes the view, and adds it to a layout. Calling `start()` again with a new request is described as an optional re-render path. The pinned dependency is an example in this snapshot, not proof of the currently supported package version.
- The request example supplies amount, page type, logo type, text alignment, and color. The reference section lists their displayed types, values, and defaults; consult the raw table because its `pageType` rendering is damaged rather than reconstructing missing separators or enum qualification.
- Implementing `PayPalMessagingListener` is optional. The page associates callbacks with message click, the start of a PayPal credit application, content loading, successful rendering, and an error. These events do not establish application approval, checkout completion, authorization, settlement, or funding.

> [!warning] Captured-page inconsistencies
> The invocation text and example construct `PayPalMessagingView` with `context` and an authorization string, while the later class table lists `braintreeClient` and `context`. The example listener implements `onPayPalMessagingFailure`, while the method table names `onPayPalMessagingError`. This entry preserves both discrepancies and does not choose a runtime signature without separate version-matched implementation evidence.

## Detail locators

- Availability and explicit Drop-in exclusion: **AVAILABILITY**, lines 17–18.
- Eligible countries, integration prerequisites, content restrictions, and category exclusions: **ELIGIBILITY**, lines 23–36.
- Stated purpose of customized Pay Later offers: line 40.
- Captured Gradle dependency: **Get the SDK → Groovy**, lines 43–53.
- Request/view construction, `start()`, layout insertion, and optional re-render example: **Invoking the Pay Later Messaging Flow → Kotlin**, lines 55–93.
- Optional listener example and its `onPayPalMessagingFailure` spelling: lines 94–120.
- View constructor reference table: **Reference → PayPalMessagingView Class**, lines 122–133.
- Request fields and displayed defaults: **Reference → PayPalMessagingRequest Class**, lines 135–165.
- Listener purpose and method table, including `onPayPalMessagingError`: **Reference → PayPalMessagingListener Interface**, lines 168–178.

## Related

- [[braintree]]
- [[braintree-android-sdk]]

## Raw Sources

- [[raw/braintree/docs/guides/paypal/messaging/android/v5-2026-09-16|Braintree PayPal Pay Later Messaging — Android v5 (fetched 2026-09-16)]]
