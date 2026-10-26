---
title: "Adyen MobilePay iOS Drop-in"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/mobilepay/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/mobilepay/ios-drop-in/2026-09-15.md"
tags: [adyen, mobilepay, ios, drop-in, online-payments]
---

## Overview

Adyen's 2026-09-15 webpage snapshot gives MobilePay-specific additions to an existing iOS Drop-in integration, separated by Sessions and Advanced server-side flows. It points back to the main integration guides for general steps; it is not a complete standalone integration guide. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- For Sessions, the page specifies an existing iOS Drop-in Sessions integration using Checkout API v68 or later and MobilePay added in Customer Area. It says no additional `/sessions` parameters or MobilePay configuration are needed.
- For Advanced, it specifies an existing iOS Drop-in Advanced integration, handling `action.type: redirect`, and MobilePay added in Customer Area. It says no additional MobilePay configuration and ordinarily no extra `/payments` parameters are needed. The exception is a payment intended to generate a token for later MobilePay-wallet payouts.
- For ordinary MobilePay payments, this page says the Adyen test environment cannot be used; its testing path is low-amount payments in live after a live Customer Area request. It directs the merchant to the server's `AUTHORISATION` webhook and Customer Area payment list for status. The snapshot establishes neither present account eligibility nor a completed payment.
- The wallet payout feature is marked experimental and supported only with `/payments`. A token-generating payment requires recurring lifecycle webhook setup and the `telephoneNumber`, `shopperReference`, and `enablePayout`-true parameters. The page directs the merchant to save `storedPaymentMethodId` from the recurring lifecycle webhook for the shopper, then place the token in a later Transfers API `/transfers` request's `counterparty.card.cardIdentification`. Its separate payout test instructions use a Vipps MobilePay test app, the recurring lifecycle webhook, and Transfers API; they do not establish ordinary MobilePay payments as test-environment supported.
- The payout-token prose spells `enablePayout`, but the curl hint spells `enablePayOut`. The curl and language-specific request samples also contain blank currency, payment-method type, or return URL values, and most omit the prose's payout-token fields. Treat them as illustrative snapshot snippets, not verified runnable requests or a resolution of the spelling discrepancy.

## Detail locators

- Sessions requirements and no-additional-parameter/configuration statements: raw lines 25-46.
- Sessions live payment and experimental payout testing instructions: raw lines 48-83.
- Advanced requirements, redirect, configuration, and `/payments` exception: raw lines 85-107.
- Advanced language-specific request snippets, including the curl payout hints: raw lines 109-291.
- Payout-token prerequisites, webhook token, and later transfer: raw lines 293-325.
- Repeated Advanced live payment and payout testing instructions: raw lines 327-362.

## Related

- [[adyen-ios-sdk]] — native Drop-in and integration architecture.
- [[adyen-tokenization]] — broader tokenization context; this page's experimental payout-token path has separate conditions.

## Raw Sources

- [[raw/adyen/docs/payment-methods/mobilepay/ios-drop-in/2026-09-15|MobilePay iOS Drop-in (2026-09-15 snapshot)]]
