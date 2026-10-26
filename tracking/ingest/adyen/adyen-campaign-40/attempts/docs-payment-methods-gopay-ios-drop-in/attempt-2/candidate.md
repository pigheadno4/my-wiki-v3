---
title: "Adyen GoPay iOS Drop-in"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/gopay/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/gopay/ios-drop-in/2026-09-15.md"
tags: [adyen, gopay, ios, drop-in, redirect, recurring-payments]
---

## Overview

Adyen's 2026-09-15 GoPay iOS Drop-in page describes GoPay-specific additions to an existing iOS Drop-in integration, separately for Sessions and Advanced server-side flows. It also describes token creation and distinct later `Subscription` and `CardOnFile` payments. See [[adyen]], [[adyen-ios-sdk]], and [[adyen-tokenization]].

## Key takeaways

- Sessions requires an existing iOS Drop-in Sessions integration using Checkout API v68 or later and GoPay added in Customer Area. Its `/sessions` table marks `shopperInteractionDevice` and `channel` required, with the channel set to the applicable platform. The sample uses ID/IDR and `channel: iOS`, but the device example is a quoted multi-line Chrome object and does not establish a validated runnable request or a universal country/currency eligibility rule.
- Advanced requires an existing iOS Drop-in Advanced integration, redirect handling for `action.type: redirect`, and GoPay added in Customer Area. Its `/payments` table marks `paymentMethod.type: gopay_wallet`, `browserInfo` and `channel` required. It says no GoPay-specific Drop-in configuration is needed, as does Sessions. The Advanced example returns `RedirectShopper` with a redirect action, an intermediate step rather than final authorization.
- The Advanced example uses `channel: web`, a Windows/Chrome `browserInfo`, and an HTTPS web checkout return URL despite the iOS guide. Treat these as source example inconsistencies, not iOS channel or return-URL requirements. The Sessions example's iOS channel and app-scheme return URL are examples, not a complete app-return integration specification. Neither primary curl request is copyable as printed: both the Sessions `/sessions` and Advanced `/payments` samples omit a shell line continuation after `-X POST`, and both put unescaped inner double quotes inside quoted `shopperInteractionDevice` or `browserInfo` values (raw lines 49-71 and 396-425).
- To create a GoPay token, the page calls for `storePaymentMethod: true`, a shopper-unique `shopperReference` of at least three characters, and `recurringProcessingModel` in `/payments`. Only after initial payment settlement does `recurring.token.created` supply `storedPaymentMethodId`; the server must receive recurring-token lifecycle events. Later `Subscription` uses the stored ID, shopper reference, `shopperInteraction: ContAuth`, and `recurringProcessingModel: Subscription`.
- Later `CardOnFile` differs: the shopper must enter a PIN at GoPay in a challenge flow after redirect. A `RedirectShopper` response supplies the action URL; after return the integration calls `/payments/details` with `redirectResult`. The page gives final processed-payment status through an `AUTHORISATION` webhook; its `success: true` lines are examples, not a promised outcome. Many subscription snippets leave currency, method type or return URL blank, so they are not runnable values.
- For testing, the page says to contact Adyen Support and refers to GoPay's knowledge base. Live acceptance requires a separate GoPay request in live Customer Area. The snapshot proves neither current enablement nor an executed payment.

## Detail locators

- Sessions prerequisites, required `/sessions` fields, example and no-extra-configuration statement: raw lines 25-77.
- Sessions token creation, settlement webhook and Subscription fields: raw lines 79-114; language samples and status text: lines 116-325.
- Sessions `CardOnFile` challenge/details and test/live gates: raw lines 327-362.
- Advanced prerequisites, required `/payments` fields, inconsistent iOS example and redirect response: raw lines 364-441.
- Repeated Advanced token and Subscription sections: raw lines 443-689.
- Repeated Advanced `CardOnFile` and test/live guidance: raw lines 691-726.

## Raw Sources

- [[raw/adyen/docs/payment-methods/gopay/ios-drop-in/2026-09-15|GoPay iOS Drop-in (2026-09-15 snapshot)]]
