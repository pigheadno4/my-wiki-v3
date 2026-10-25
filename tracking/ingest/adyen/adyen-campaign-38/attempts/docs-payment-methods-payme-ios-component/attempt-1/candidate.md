---
title: "PayMe iOS Component"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/payme/ios-component"
raw_files:
  - "adyen/docs/payment-methods/payme/ios-component/2026-09-15.md"
tags: [adyen, payme, ios, components, redirect, online-payments]
---

## Overview

This [[adyen]] page, captured 2026-09-15, explains how to add PayMe to an existing **iOS Components** integration. The Component renders PayMe in the payment form and redirects the shopper to the PayMe app. It says PayMe is supported from iOS Components **v4.0.0**. This is integration guidance, not evidence of current merchant eligibility or an observed payment outcome. See [[adyen-online-payments]] and raw lines 15–23.

## Key takeaways

- Start with an existing iOS Components **Sessions** or **Advanced** server-side flow and add PayMe in the Customer Area. The page calls `/sessions` the default with Components **v5.0.0+**; its `/payments` tab is for an additional use case. These are flow and SDK qualifications, not a Checkout API minimum. See raw lines 25–71.
- Its endpoint tables list `channel` and optional line-item fields. `lineItems.sku` is available with Checkout API **v70+**; this field-specific condition should not be applied to PayMe integration generally. The illustrative `/payments` request uses `paymentMethod.type: payme`, HK/HKD, `channel: iOS`, a `returnUrl` and line items. The code fence is marked `swift` but contains JavaScript `require('@adyen/api-library')`; treat it as an inconsistent example, not executable Swift. See raw lines 47–108.
- For Components **v5.0.0+**, both Sessions and Advanced examples find `.other("payme")`, construct `InstantPaymentComponent`, set the corresponding delegate (`session` or `self`) and call `initiatePayment()`. The **v4.x.x** example instead constructs `InstantPaymentMethod` and passes `paymentData: nil` plus `apiContext`. Use the matching flow/version example; app redirection is an intermediate shopper action, and the page points to the base integration guide for payment outcome handling. See raw lines 110–159.
- In the PayMe **sandbox**, the page says no PayMe app is needed. Amount endings `30`/`81`, `77`/`90`, and `40`/`44` simulate `Authorised`, `OfferCancelled` after PayMe's default **ten-minute** expiry, and payment-request creation `Error`, respectively. These are sandbox simulation rules, not proof of live authorization, capture or settlement. See raw lines 161–171.

## Detail locators

- Scope, supported Components version and flow/setup prerequisites: raw lines 15–41.
- `/sessions` and `/payments` optional parameter tables, Checkout API v70+ `sku` qualification, and illustrative request: raw lines 43–108.
- v5+ Sessions/Advanced and v4.x.x configuration snippets: raw lines 110–159.
- Sandbox amount-outcome table and default expiry statement: raw lines 161–171.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-payme]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/payme/ios-component/2026-09-15|PayMe iOS Component guide — captured 2026-09-15]]
