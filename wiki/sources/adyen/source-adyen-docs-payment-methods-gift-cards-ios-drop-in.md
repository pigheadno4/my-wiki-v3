---
title: "Gift card iOS Drop-in integration"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/gift-cards/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/gift-cards/ios-drop-in/2026-09-15.md"
tags: [adyen, gift-cards, ios, drop-in, partial-payments]
---

## Overview

This Adyen page, last modified 2025-08-11 and captured 2026-09-15, describes gift-card additions to an existing iOS Drop-in integration. It distinguishes the default /sessions path from the /payments additional-use-case path, with a partial-payment delegate for the latter. See [[adyen]], [[adyen-online-payments]], and [[source-adyen-docs-payment-methods-gift-cards]] for provider onboarding and broader method context. Example code and simulated outcomes do not establish current eligibility or successful live processing.

## Key takeaways

- The page assumes an existing iOS Drop-in integration and intended test gift-card variants added in Customer Area. It says only a limited number of variants can be tested through a simulator; before live use, onboard with a provider and add the variant in live Customer Area (raw lines 23–31). It says no **additional gift-card request fields**; /sessions is the stated default from Drop-in v5.0.0 onward and /payments covers an additional use case (lines 33–38). This does not remove base endpoint fields.
- For the /sessions tab, the guide repeats the v5.0.0 default and says there is **no required gift-card-specific iOS Drop-in integration** (raw lines 40–48). That is a method-specific configuration statement, not a waiver of the existing Drop-in or account setup.
- For /payments, configure a gift-card partial-payment delegate: checkBalance calls /paymentMethods/balance, requestOrder calls /orders with the **total transaction amount** when gift-card balance is short, and cancelOrder calls /orders/cancel on cancellation (raw lines 50–62). The Swift example sketches these methods with placeholder balance/order completions and comments for the API calls; it is not an end-to-end request implementation (lines 64–81). The merchant can use another payment method for the remainder, but this page does not give its complete payment-order recipe; follow the partial-payments guide for that.
- The result section uses /payments response resultCode for the shopper message and separately says the outcome arrives asynchronously in a webhook. It lists Authorised, Cancelled, Error and Refused. Manual capture is an extra step **only when that capture mode is used** (raw lines 83–94). Do not equate a displayed response result with proof of final settlement.
- Provider-dependent test-card numbers and amount-last-three-digit outcome codes are **simulator cases**; test Customer Area Payment list is the status check (raw lines 96–117). For live use, the guide says to onboard with a gift-card provider, add its variant in live Customer Area, and contact Support to add the gift card there; only then does it mention small-amount tests using real gift-card details (lines 119–125). This page does not record a live test or grant operational authorization.

## Detail locators

- Existing iOS Drop-in, limited test variants and provider prerequisite: raw lines 23–31.
- No extra method fields and /sessions versus /payments route: raw lines 33–52.
- /payments partial-payment delegate methods and placeholder Swift sample: raw lines 54–81.
- Response, asynchronous webhook, result codes and conditional manual capture: raw lines 83–94.
- Provider-dependent simulator and live setup: raw lines 96–125.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-gift-cards]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/gift-cards/ios-drop-in/2026-09-15|Gift card iOS Drop-in, captured 2026-09-15]]
