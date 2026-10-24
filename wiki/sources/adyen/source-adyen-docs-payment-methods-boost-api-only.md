---
title: "Boost Wallet for API only"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/boost/api-only"
raw_files:
  - "adyen/docs/payment-methods/boost/api-only/2026-09-15.md"
tags: [adyen, boost, wallet, malaysia, api-only, online-payments]
---

## Overview

This 2026-09-15 capture describes Boost Wallet as an add-on to an existing Adyen Advanced Web API-only integration. The page covers MY/MYR payment-method discovery and redirect handling, rather than a complete standalone checkout or evidence of a successful payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Prerequisites and roles:** the merchant must already have the linked API-only Web integration, handle a redirect action, and add Boost Wallet in Customer Area. The merchant builds the payment form; the guide says no extra form fields. These are documented setup steps, not proof of merchant eligibility or an enabled account. (raw lines 17–40)
- **Method discovery:** the guide says to send `countryCode: MY` and `amount.currency: MYR` to `/paymentMethods`; its example response identifies Boost as `molpay_boost`. The `/v72` endpoint and MYR 1000 amount are example values, not a universal minimum or proof of current availability. (raw lines 42–49, 52–338)
- **Payment request and redirect:** the illustrated `/v72/payments` request carries amount, reference, return URL and merchant account. The illustrated response has `resultCode: RedirectShopper` and a GET redirect action for `molpay_boost`. This is an example of an intermediate redirect response, not observed authorization, capture or settlement. The example request omits a `paymentMethod` field; do not treat it as independently verified executable payload. (raw lines 340–634)
- **Source inconsistencies:** the “How it works” sequence tells the merchant to include additional item information in the payment request, yet the linked additional-parameters section says none are needed and its payment examples show no item information. The guide also uses checkout TEST URLs in examples while stating there is no Boost Wallet test environment and describing penny tests in LIVE. These statements remain unresolved in this snapshot; the examples cannot establish a usable Boost TEST path. (raw lines 31–36, 340–618, 624–638)
- **Limits:** the page does not establish a current live setup, final asynchronous outcome, tokenization, recurring payments, capture or refund behavior. It documents a historical integration route only. (raw lines 17–21, 620–642)

## Detail locators

- Existing API-only Web integration, redirect support and Customer Area setup: raw lines 23–29.
- Merchant-built form, item-information statement and no extra form fields: raw lines 31–40.
- MY/MYR discovery and `molpay_boost` example: raw lines 42–49, 327–338.
- Additional-parameter contradiction and payment request examples: raw lines 340–618.
- Redirect response example and TEST/LIVE contradiction: raw lines 620–638.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/boost/api-only/2026-09-15|Adyen Boost Wallet API-only guide, 2026-09-15 snapshot]]
