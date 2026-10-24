---
title: "GCash Web Component"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/gcash/web-component"
raw_files:
  - "adyen/docs/payment-methods/gcash/web-component/2026-09-15.md"
tags: [adyen, gcash, web, components, wallets]
---

## Overview

Adyen's 2026-09-15 GCash Web Component page gives GCash-specific additions to an existing Web Components integration, with separate Sessions and Advanced server-side flow branches. The linked main guides remain the authority for the base flow, redirect and payment-result handling. This snapshot does not establish current eligibility or a successful payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Sessions:** Requires an existing Web Components Sessions integration, Checkout API v68 or later, redirect handling for `action.type: redirect`, and GCash added in Customer Area. The page calls for no additional GCash-specific `/sessions` parameters or Component configuration. Import Adyen Web's `Redirect` class and initialize a Redirect Component for GCash. [Raw lines 25–71]
- **Advanced:** Requires an existing Web Components Advanced integration, redirect handling, and GCash added in Customer Area. Import and initialize `Redirect`; the page calls for no additional GCash-specific ordinary `/payments` request parameters. [Raw lines 322–360]
- **Recurring:** The separate token route asks for `storePaymentMethod: true` and a `shopperReference` of at least three characters on `/payments`. Only after the initial payment settles does the `recurring.token.created` webhook deliver `storedPaymentMethodId`; the merchant server must receive recurring-token lifecycle webhooks. Subsequent `/payments` use that ID, the same shopper reference, `shopperInteraction: ContAuth`, and `recurringProcessingModel: Subscription` or `UnscheduledCardOnFile` according to interval. A redirect or initial request alone is not a token or final payment outcome. [Raw lines 74–111, 362–399]
- **TEST and live:** The examples show TEST API endpoints/clients and PHP amounts, not a general eligibility matrix or proof of execution. The page says successful GCash live payments use a real mobile number registered with GCash, test status can be checked in Customer Area, and live acceptance requires a GCash request in the live Customer Area. Its phrase “test successful GCash live payments” mixes environment terms, so do not infer a TEST simulator from it. [Raw lines 113–310, 312–320, 401–608]

## Detail locators

- Both flow examples initialize `new Redirect(checkout, { type:gcash })` (raw lines 70–72, 352–354). The token `gcash` is unquoted in the literal snippet; treat it as source example text, not verified executable JavaScript.
- Recurring `/payments` examples by language, including `paymentMethod.type: gcash`, stored method ID and PHP amounts: raw lines 113–310 and 401–598. The explicit Checkout API v68+ prerequisite is in the Sessions branch, not stated for Advanced here.
- Redirect return processing, authentication/authorization, final status, capture and settlement beyond the token-created timing are outside this method add-on and require the linked base guides or payment-status evidence.

## Related

- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/gcash/web-component/2026-09-15|GCash Web Component (2026-09-15)]]
