---
title: "Adyen Scalapay Android Drop-in integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/scalapay/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/scalapay/android-drop-in/2026-09-15.md"
tags: [adyen, scalapay, android, drop-in, sessions, advanced, bnpl]
---

## Overview

This 2026-09-15 Adyen Docs guide adds Scalapay to an existing Android Drop-in integration through Sessions or Advanced flow. It covers method request fields, a sample Advanced `/payments` call, configuration and test/live routes. This dated page does not prove merchant enablement, shopper approval or payment execution. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- Both Sessions and Advanced require an existing Android Drop-in integration at version 5.0.0 or later and Scalapay added in Customer Area. Adyen says activation defaults to standard pricing; before activating, contact the account manager to verify eligibility for Enterprise pricing. `/sessions` is the default path with Drop-in v5.0.0+; `/payments` is presented for an additional use case. Neither flow requires extra Scalapay Drop-in configuration.
- Both API tables mark shopper `countryCode` and `shopperName` (`firstName`, `lastName`) required. The listed countries in the request rows are IT, FR, PT and ES. Billing/delivery addresses and line items are shown as optional in those tables. The `/payments` table additionally lists optional airline outbound flight date or lodging check-in date, saying to provide either field for the applicable transaction; it does not authorize combining both. The page gives no country-to-currency matrix.
- The Advanced `/payments` sample is one IT/EUR request with `paymentMethod.type: scalapay_3x`, shopper name, amount 1000 minor units and an app return URL. It does not establish that all Scalapay products, currencies or shoppers are available. The C# and Go sample object initializers spell `countryCode` with a lowercase initial while other fields use capitalized model properties; treat those snippets as illustrative and verify against the installed API-library version. The page leaves redirect and final outcome behavior to the linked base Drop-in integration.
- The test section links Scalapay test scenarios and a test Customer Area payment list. Before accepting live Scalapay payments, it says to submit a request in the live Customer Area. A request instruction or TEST sample is not evidence of live enablement or successful payment.

## Detail locators

- Sessions/Advanced prerequisites, pricing and flow selection: pinned raw lines 21–47. Request tables and conditional travel data: lines 49–71.
- Advanced IT/EUR `scalapay_3x` example and language-specific API-library snippets: lines 73–428; C#/Go `countryCode` capitalization appears at lines 228/307.
- No method-specific Drop-in configuration: lines 430–438. Test and live request routes: lines 440–453.

## Related

- [[adyen-online-payments]] — main provider payment integration concept

## Raw Sources

- [[raw/adyen/docs/payment-methods/scalapay/android-drop-in/2026-09-15|Scalapay Android Drop-in guide, captured 2026-09-15]]
