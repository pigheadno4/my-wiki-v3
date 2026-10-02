---
title: "Braintree Android SDK v4 to v5 migration"
type: source
date_ingested: 2026-10-02
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/client-sdk/migration/android/v5"
raw_files:
  - "braintree/docs/guides/client-sdk/migration/android/v5-2026-09-16.md"
tags: [braintree, android, sdk, migration]
---

## Overview

This Braintree website guide is a snapshot of the Android client SDK migration from v4 to v5. It routes implementers to version-specific build prerequisites, client construction and result-handling changes, and removed or unavailable integrations; it is historical migration evidence, not proof of current v5 support, merchant eligibility, or successful payment execution.

## Key takeaways

- The guide raises the minimums to Android API 23, Gradle JDK 11+, Kotlin 1.9.10+, and Android Gradle Plugin 8.1.4+, and says every Braintree Android SDK dependency must move to 5.x because v4 and v5 modules are incompatible.
- Payment-method clients are constructed directly with Android context and a tokenization key or client token rather than through a `BraintreeClient`. The data collector moves from `paypal-data-collector` to `data-collector`, and its former `merchantId` argument becomes an optional `riskCorrelationId`.
- Venmo, Google Pay, 3D Secure, PayPal, Local Payment, and SEPA Direct Debit use integration-specific launcher and result patterns, with lifecycle placement and return-handling requirements. These are Android client-side migration concerns; examples route resulting nonces or device data to the merchant server, while this page does not define the server-side transaction contract.
- PayPal v5 requires an Android App Link for returning from the web flow. For browser-switch flows, pending requests must be retained for return handling; minimizing an active Chrome Custom Tab can yield `NoResult`, which is not described as success or failure.
- Material removals and availability limits include the removed Union Pay module (UnionPay cards instead use the card module), unsupported 3DS v1, Visa Checkout not yet available for v5, unsupported Samsung Pay, and unsupported PayPal Native Checkout in favor of the PayPal web integration.

## Detail locators

- **Supported versions and dependency boundary:** `Supported versions` and `Gradle dependencies` (raw lines 22–31).
- **Core client and collection changes:** `Braintree Client`, `Data Collector`, `Card`, and `American Express` (raw lines 41–102).
- **Union Pay and launcher migrations:** `Union Pay`, `Venmo`, `Google Pay`, and `3DS` (raw lines 104–314).
- **Browser-switch integrations:** `PayPal`, `Local Payment`, and `SEPA Direct Debit` (raw lines 316–558).
- **Removed or unavailable integrations:** `Visa Checkout`, `Samsung Pay`, and `PayPal Native Checkout` (raw lines 560–572).
- **Chrome Custom Tab picture-in-picture return condition:** `Chrome Custom Tab Picture-in-Picture` (raw lines 575–598).

## Related

- [[braintree]]
- [[braintree-android-sdk]]

## Raw Sources

- [[raw/braintree/docs/guides/client-sdk/migration/android/v5-2026-09-16|Braintree Android SDK v4-to-v5 migration guide (snapshot 2026-09-16)]]
