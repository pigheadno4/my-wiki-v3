---
title: "Adyen Scalapay Android Component integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/scalapay/android-component"
raw_files:
  - "adyen/docs/payment-methods/scalapay/android-component/2026-09-15.md"
tags: [adyen, scalapay, android, components, sessions, advanced, bnpl]
---

## Overview

This 2026-09-15 Adyen Docs guide adds Scalapay to an existing Android Components integration using Sessions or Advanced flow. It supplies method-specific setup, component snippets and an Advanced `/payments` example. The guide does not establish merchant eligibility, shopper approval, live activation or payment outcome. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- Both flows require Android Components v5.0.0+ and Scalapay added in Customer Area. The page says activation defaults to standard pricing; merchants should contact an account manager before activation to check eligibility for Enterprise pricing. The Sessions branch adds no method-specific session request fields or configuration. Its snippets import `com.adyen.checkout:instant`, plus `components-compose` for Jetpack Compose, and get `PaymentMethodTypes.SCALAPAY` before launching the instant payment Component.
- The Advanced branch likewise adds no Scalapay-specific configuration and obtains the payment method from `/paymentMethods`. Its sample server `/payments` request uses `paymentMethod.type: scalapay_3x`, IT, EUR 1000 minor units, shopper name and an Android app return URL. This is one sample for the 3x type, not a statement about every Scalapay product, country, currency or shopper eligibility. The page leaves redirect/action handling and final outcomes to the linked base integration.
- The Advanced Compose sample creates `cardComponent = InstantComponent.PROVIDER.get(...)` but passes `instantComponent` to `AdyenComponent`; the function is named `ComposableCardComponent`. The non-Compose sample similarly calls its `InstantComponent` variable `cardComponent`. These naming inconsistencies make the snippets unsuitable as copy-ready evidence without checking the base guide and the installed SDK version. The Advanced base links show version-specific query strings (v5.2.0), while the requirement says minimum v5.0.0; a link alone does not change the stated minimum.
- The test section routes to Scalapay test scenarios and a test Customer Area payment list. It says to submit a Scalapay request in live Customer Area before accepting live payments. This is a setup condition, not confirmation of a granted live request or tested transaction.

## Detail locators

- Sessions/Advanced requirements and pricing qualification: pinned raw lines 23–32 and 137–146. Sessions no-extra-field/config, imports and launch snippets: lines 34–135.
- Advanced configuration/import, Compose/non-Compose snippets and variable mismatch: lines 148–231. Advanced payment sample, API-library snippets and IT/EUR/`scalapay_3x` scope: lines 233–594.
- Test and live request routes: lines 596–609.

## Related

- [[adyen-online-payments]] — main provider payment integration concept

## Raw Sources

- [[raw/adyen/docs/payment-methods/scalapay/android-component/2026-09-15|Scalapay Android Component guide, captured 2026-09-15]]
