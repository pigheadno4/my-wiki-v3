---
title: "Adyen Google Pay Flutter Drop-in"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/google-pay/flutter-drop-in"
raw_files:
  - "adyen/docs/payment-methods/google-pay/flutter-drop-in/2026-09-15.md"
tags: [adyen, google-pay, flutter, drop-in, online-payments]
---

## Overview

This 2026-09-15 guide adds Google Pay to an **existing Flutter Drop-in integration** using either Sessions or Advanced server-side flow. It directs the merchant to Google's Android Pay setup and to add Google Pay in Adyen Customer Area. Its method-specific instructions concern Drop-in configuration and TEST/LIVE readiness; the referenced main integration guides own the underlying server requests, callbacks and payment outcomes. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- Both tabs require an existing **Flutter Drop-in** integration and Customer Area method setup. Sessions says Google Pay needs **no additional fields** in the existing `/sessions` request; Advanced says the same for `/payments`. These are method-specific additions, not a claim that the base server requests can omit their normal required fields. The page does not state a Checkout API or Flutter SDK minimum version. (raw lines 21–49)
- Both flows say to add Google Pay properties to the Flutter configuration object. `googlePayEnvironment` can be `test` or `production`. The shown configuration snippet is incomplete and omits punctuation/closure, so it is illustrative rather than ready-to-run code. After configuration, Sessions says initialize/show Drop-in; Advanced says add its required callbacks. (raw lines 51–72, 97–103)
- Optional configuration lists `merchantAccount` but describes it as **Google Merchant ID**, with any value for testing and a Google Pay & Wallet Console ID before LIVE; do not confuse this page's label with the Adyen merchant account field in other API requests. Other listed knobs include merchant display name, total-price status, allowed card networks/auth methods, prepaid/credit-card eligibility, shopper email and address collection. `panOnly` is described as stored card PAN/expiry data; `cryptogram3DS` as Android device-token data with a device-generated cryptogram. These labels do not prove completed shopper authentication, authorization or transaction eligibility. The `assuranceDetailsRequired` description is truncated after “Set to true to require,” leaving its exact object/behavior unspecified in this page. (raw lines 74–95)
- TEST requires a Google account/wallet. The guide offers Google's test-card suite (FPAN, DPAN only through native Android/Chrome on Android, and 3DS2 scenarios) or real cards in the wallet mapped to Adyen same-brand test cards without a charge. Without the suite, it says Amex or Discover is required to trigger the specified 3DS2 challenge tests. Test payment status can be checked in test Customer Area; these are test fixtures, not live authorization evidence. (raw lines 105–129)
- For LIVE, the guide **recommends** testing Google's Android API scenarios and **requires/checks** the API Clientside Encryption Payments role, a configured Google Merchant ID in live Customer Area, and Google's Android production-deploy steps. It says Google Pay is available live only if the shopper is logged into Google and has at least one valid payment method. This dated checklist does not prove provider approval, merchant enablement, actual payment, capture or settlement. (raw lines 131–142)

## Detail locators

- Flutter Sessions versus Advanced prerequisites and server-request statements: raw lines 21–49.
- Required environment and optional Flutter config, plus callback split: raw lines 51–103.
- TEST wallet/card scenarios: raw lines 105–129.
- LIVE role, Merchant ID, deploy and shopper conditions: raw lines 131–142.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-google-pay]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/google-pay/flutter-drop-in/2026-09-15|Adyen Google Pay Flutter Drop-in guide, 2026-09-15 snapshot]]
