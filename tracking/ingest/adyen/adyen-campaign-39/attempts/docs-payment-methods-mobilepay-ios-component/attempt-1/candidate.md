---
title: "Adyen MobilePay iOS Component"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/mobilepay/ios-component"
raw_files:
  - "adyen/docs/payment-methods/mobilepay/ios-component/2026-09-15.md"
tags: [adyen, mobilepay, ios, components, online-payments]
---

## Overview

Adyen's 2026-09-15 webpage snapshot describes the MobilePay-specific additions to an existing iOS Components integration using either the Sessions or Advanced server-side flow. It uses `InstantPaymentComponent` for the MobilePay payment method; it is an add-on guide, not a complete integration guide. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- For Sessions, the page requires an existing iOS Components Sessions integration, Checkout API v68 or later, redirect handling for `action.type: redirect`, and MobilePay added in Customer Area. It says no extra `/sessions` parameters or MobilePay configuration are needed. The Sessions example selects `.other("mobilepay")`, assigns the session as delegate, and initiates payment.
- For Advanced, the page requires an existing iOS Components Advanced integration, redirect handling, and MobilePay added in Customer Area. It says no MobilePay configuration is needed and ordinarily no extra `/payments` parameters; the Component example assigns the merchant delegate and initiates payment.
- The page says ordinary MobilePay payments cannot be tested in Adyen's test environment: low-amount live payments after a live Customer Area request are its test path. It directs the merchant to receive the `AUTHORISATION` webhook and inspect the payment list for status. This snapshot does not establish current account eligibility or any completed payment.
- Future payouts to MobilePay wallets are a separate experimental feature that the page says is supported only with `/payments`. For a token-generating payment it calls for the recurring lifecycle webhook and `telephoneNumber`, `shopperReference`, and `enablePayout` set true; save the webhook's `storedPaymentMethodId` against the shopper reference, then use that token in a later Transfers API `/transfers` request's `counterparty.card.cardIdentification`. The page separately describes testing this payout path with a Vipps MobilePay test app, a recurring lifecycle webhook, and Transfers API; this does not erase its live-only statement for ordinary MobilePay payment testing.
- There are source inconsistencies to preserve: the token-creation prose spells `enablePayout`, while the curl sample spells `enablePayOut`; the Advanced iOS Components requirement links to a main guide URL whose query says `integration=Drop-in`. Several language samples omit the prose's token fields or leave currency, payment-method type, or return URL blank. Treat the prose and examples as snapshot evidence, not a validated runnable request or resolution of those discrepancies.

## Detail locators

- Sessions requirements, request/configuration and Swift initialization: raw lines 25-70.
- Sessions live test and experimental payout-test instructions: raw lines 72-105.
- Advanced requirements, no extra configuration, initialization and ordinary `/payments` exception: raw lines 107-150.
- Advanced language-specific illustrative requests: raw lines 152-334; token-field hints occur in the curl block at lines 169-171.
- Payout-token prerequisites, webhook token, later transfer request: raw lines 336-368.
- Repeated Advanced live-test and payout-test instructions: raw lines 370-403.

## Related

- [[adyen-ios-sdk]] — native Component and integration architecture.
- [[adyen-tokenization]] — broader tokenization context; this page's experimental payout-token route has its own conditions.

## Raw Sources

- [[raw/adyen/docs/payment-methods/mobilepay/ios-component/2026-09-15|MobilePay iOS Component (2026-09-15 snapshot)]]
