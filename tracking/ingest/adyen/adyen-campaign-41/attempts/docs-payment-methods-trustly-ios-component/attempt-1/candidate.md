---
title: "Adyen Trustly iOS Redirect Component"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/trustly/ios-component"
raw_files:
  - "adyen/docs/payment-methods/trustly/ios-component/2026-09-15.md"
tags: [adyen, trustly, ios, components, redirect]
---

## Overview

Adyen's 2026-09-15 Trustly iOS Redirect Component page adds Trustly to an existing iOS Components integration. It describes method setup, v5 versus v4 Component construction, TEST credentials and a separate live Customer Area request. See [[adyen]], [[adyen-ios-sdk]], and [[source-adyen-docs-payment-methods-trustly]].

## Key takeaways

- An existing iOS Components integration and adding Trustly in the **test** Customer Area are prerequisites. The page says no Trustly-specific additional `/sessions` or `/payments` fields; it calls `/sessions` the default with Components v5.0.0 or later and mentions `/payments` for an additional use case (raw lines 21-33).
- For iOS Components v5.0.0 or later, the Sessions and Advanced examples check for `.other("trustly")`, create `InstantPaymentComponent`, and call `initiatePayment()`. The Sessions example assigns `session` as delegate; the Advanced example assigns `self`. The historical v4.x.x branch instead checks `TrustlyPaymentMethod.self`, creates `TrustlyComponent` with `apiContext` and `FormComponentStyle`, and presents it. The page says there are no other Trustly-specific Components configuration steps (raw lines 35-90).
- The page describes Trustly's TEST environment and example Login ID/Personal number format `YYMMDD-XXXX` using any digits, and points to the test Customer Area for status. Before live acceptance, it says to submit a Trustly request in the **live** Customer Area. These instructions do not prove the method is enabled for any merchant or that a payment ran (raw lines 92-98).
- **Funds warning from the separate approved [[source-adyen-docs-payment-methods-trustly|Trustly overview]]:** a successful `AUTHORISATION` webhook means checks passed and a bank transfer was initiated, **not that Adyen has received funds**. The transfer can still fail; the overview says Trustly chargebacks cannot be defended. The child Component page does not state this outcome rule or a separate capture/settlement procedure (overview raw lines 38-53; this child raw lines 15-104). Do not treat Component initiation, return or an authorization notification as cleared funds.

## Detail locators

- Child prerequisites and API-reference scope: raw lines 21-33.
- v5 Sessions/Advanced and historical v4 Component examples: raw lines 35-90.
- Child TEST and live Customer Area steps: raw lines 92-98.
- Separate Trustly overview funds-versus-authorization warning: [[source-adyen-docs-payment-methods-trustly]], overview raw lines 38-53.

## Raw Sources

- [[raw/adyen/docs/payment-methods/trustly/ios-component/2026-09-15|Trustly iOS Redirect Component (2026-09-15 snapshot)]]
