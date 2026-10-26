---
title: "Adyen GoPay Web Drop-in"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/gopay/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/gopay/web-drop-in/2026-09-15.md"
tags: [adyen, gopay, web, drop-in, redirect, recurring-payments]
---

## Overview

Adyen's 2026-09-15 GoPay Web Drop-in page describes GoPay-specific additions to an existing Web Drop-in integration, separately for Sessions and Advanced server-side flows. It also describes token creation and distinct `Subscription` and `CardOnFile` later-payment paths. See [[adyen]], [[adyen-online-payments]], and [[adyen-tokenization]].

## Key takeaways

- Sessions requires existing Web Drop-in Sessions, Checkout API v68 or later, redirect handling for `action.type: redirect`, and GoPay added in Customer Area. The `/sessions` table marks `shopperInteractionDevice` and `channel` required; the channel must match the applicable platform. Its example uses ID/IDR and `channel: web`, but those sample values do not establish a general country/currency eligibility rule or required casing. The example's embedded device object is rendered as a quoted multi-line string, so it is not a validated runnable JSON request.
- Advanced requires existing Web Drop-in Advanced, redirect handling and Customer Area setup. Its `/payments` table marks `paymentMethod.type: gopay_wallet`, `browserInfo` and `channel` required. The example returns `RedirectShopper` with `action.type: redirect`; that is a shopper action, not final authorization. Its browser-info example likewise renders an object inside a quoted multi-line value. The Advanced main-guide URL contains an encoded unresolved platform template, so use the textual requirement rather than treating that URL as a verified resolved route.
- Individual `Redirect` import with `AdyenCheckout` and `Dropin` is optional for tree shaking in either flow; the page does not require a separate GoPay Component import.
- For recurring GoPay, the initial `/payments` token request includes `storePaymentMethod: true`, a shopper-unique `shopperReference` of at least three characters, and `recurringProcessingModel`. The `recurring.token.created` webhook supplies `storedPaymentMethodId` only after the initial payment settles; the server must receive recurring-token lifecycle events. `Subscription` later payments use the stored ID, shopper reference, `shopperInteraction: ContAuth`, and `recurringProcessingModel: Subscription`.
- `CardOnFile` later payments use their own processing model and **require a shopper PIN challenge** through redirect to GoPay. After return, call `/payments/details` with `redirectResult`. Both recurring sections say the `AUTHORISATION` webhook gives final status after processing; the examples show `success: true` but do not guarantee success. Many subscription code samples leave currency, payment-method type or return URL blank, so their blanks are not usable values. The generic initial payment, token-creation and later-payment stages must not be conflated.
- For GoPay testing, the page says to contact Adyen Support and refers to GoPay's knowledge base. Live acceptance requires a separate GoPay request in live Customer Area. This snapshot does not establish current account enablement or any executed payment.

## Detail locators

- Sessions prerequisites, marked required fields, example and optional `Redirect` import: raw lines 25-85.
- Sessions token-creation conditions, settlement webhook, subscription flow: raw lines 87-123; subscription language samples and outcome text: lines 124-334.
- Sessions `CardOnFile` PIN/redirect/details and test/live gates: raw lines 335-370.
- Advanced prerequisites, unresolved link, marked required fields, example redirect and optional import: raw lines 372-455.
- Repeated Advanced token creation and subscription flow: raw lines 457-704.
- Repeated Advanced `CardOnFile` and test/live gates: raw lines 705-740.

## Raw Sources

- [[raw/adyen/docs/payment-methods/gopay/web-drop-in/2026-09-15|GoPay Web Drop-in (2026-09-15 snapshot)]]
