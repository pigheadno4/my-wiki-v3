---
title: "Adyen Zip Android Redirect Component earlier versions"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/zip/android-component/earlier-versions"
raw_files:
  - "adyen/docs/payment-methods/zip/android-component/earlier-versions/2026-09-15.md"
tags: [adyen, zip, android, components, redirect, recurring, online-payments]
---

## Overview

This captured [[adyen]] guide is titled **Zip Redirect Component v4.x.x integration** for an existing Android Components integration. It describes Zip method discovery, an AU/AUD redirect payment, return handling, result/webhook interpretation, and a recurring-token route. Its requirements say Advanced flow, while the body also has a `/sessions` tab explicitly described as the default with Components **v5.0.0 or later**. Treat those as version/flow-specific passages, not one uniform v4 recipe. [[adyen-online-payments]]

## Key takeaways

- **Prerequisites and method discovery:** The page calls for an existing Advanced Android Components integration and Zip added in Customer Area. For `/paymentMethods`, it specifies `countryCode: AU`, `amount.currency: AUD`, and `amount.value`; it says the response contains `paymentMethod.type: zip`. It also says to collect shopper details for Zip risk checks and purchased-item information (raw lines 19–45). Discovery and request examples do not establish current merchant or shopper eligibility.
- **Mixed version and request scopes:** The title says v4.x.x, but the `/sessions` tab says it is default with Components v5.0.0 or later; `/payments` is presented for an additional use case. The opening payment instruction names a server `/payments` call with `paymentMethod.type: zip` and `returnUrl` obtained from `RedirectComponent.getReturnUrl(context)`. The tabs' shopper-name/email/date-of-birth/phone/address/line-item rows have blank Required cells, so the prose's collection instruction should not be expanded into a claim that every individual field is universally required. `paymentMethod.clickAndCollect: true` is conditional on pickup in the `/payments` tab. Optional line-item `imageURL` has a stated 500-character maximum (raw lines 47–70, 707–720). The Advanced curl example contains literal `{hint:...}` markup inside its JSON body, so it is not copy-ready (raw lines 724–740).
- **Redirect and result finality:** For the `/payments` path, the response example has `RedirectShopper` and a redirect `action`; the server passes that action to the app. After the shopper returns, the guide says the server posts Redirect Component `actionComponentData.details` to `/payments/details`, then uses `resultCode` for shopper presentation. `Pending` and `Received` mean the final result is unknown and require waiting for an `AUTHORISATION` webhook; if the shopper does not return, webhooks still determine outcome. The listed webhook cases include `AUTHORISATION` true/false and `OFFER_CLOSED` true (raw lines 1401–1472). An example `Authorised` response is not proof of an actual payment.
- **Recurring token route:** This page says Zip recurring transactions are supported. It instructs `storePaymentMethod: true` and `shopperReference` on initial `/payments`; after settlement, a `recurring.token.created` webhook supplies `storedPaymentMethodId`. Future `/payments` uses that ID, the same shopper reference, `shopperInteraction: ContAuth`, and `recurringProcessingModel: Subscription` or `UnscheduledCardOnFile`. Receiving a token event is conditional on a settled initial payment and webhook setup, not guaranteed by the request alone (raw lines 1474–1507; examples 1509–1705).
- **Test/live gate:** Zip test accounts come from Zip's test-credentials page. The guide points to Adyen Customer Area for test status and says to request Zip in live Customer Area before live acceptance (raw lines 1707–1713).

## Detail locators

- Guide identity, requirements and AU/AUD method discovery: pinned raw lines 15–45.
- Payment endpoint/version distinctions and `/sessions` request table/examples: pinned raw lines 47–706.
- `/payments` table, conditional pickup and examples: pinned raw lines 707–1400.
- Redirect, details, result and webhook paths: pinned raw lines 1401–1472.
- Recurring token creation/reuse and test/live gates: pinned raw lines 1474–1719.

## Related

- [[adyen-online-payments]] — online payment architecture and method routes.
- [[adyen-tokenization]] — provider tokenization context; use this pinned guide for the Zip-specific historical claims.

## Raw Sources

- [[raw/adyen/docs/payment-methods/zip/android-component/earlier-versions/2026-09-15|Zip Redirect Component earlier versions, captured 2026-09-15]]
