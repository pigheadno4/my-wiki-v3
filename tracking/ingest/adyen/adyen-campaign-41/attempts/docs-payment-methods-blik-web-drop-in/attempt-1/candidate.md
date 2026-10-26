---
title: "Adyen BLIK Web Drop-in guide"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/blik/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/blik/web-drop-in/2026-09-15.md"
tags: [adyen, blik, web, drop-in, poland, pending, one-click, tokenization]
---

## Overview

This Adyen BLIK Web Drop-in page was last modified 2020-07-07 and captured 2026-09-15. It adds BLIK to an existing Web Drop-in integration, describing a BLIK-code path and a separate BLIK One Click consent/token path under its `/payments` tab. The source also has `/sessions` guidance. Its `Pending` response and `await` action mean the shopper must finish in the BLIK app; the `AUTHORISATION` webhook supplies the outcome. This historical guide does not prove current merchant enablement, certification, token creation or successful payment. See [[adyen]], [[adyen-online-payments]] and [[adyen-tokenization]].

## Key takeaways

- **Base integration and Sessions:** the requirements row says Web Drop-in v3.9.0 or later and BLIK added in the **test** Customer Area. It points to a Sessions integration link whose URL contains an encoded `/ ?target=_blank` fragment; verify the main guide route. For Web Drop-in v6, the page shows an optional import of `AdyenCheckout` and `Blik`. It states no BLIK-specific Drop-in configuration and no extra BLIK fields for `/sessions`, calling Sessions the default for Drop-in v5.0.0 or later. These versions describe different scope statements, not one universal minimum for all code paths. (raw lines 21–48)
- **BLIK with code under `/payments`:** the guide describes displaying BLIK and a shopper-entered six-digit `blikCode`. For discovery it specifies `/paymentMethods` country `PL`, currency `PLN` and amount in minor units. The response may include `storedPaymentMethods.type: blik` if the shopper previously signed up for One Click. The initial `/payments` request specifies `paymentMethod.type: blik` and `paymentMethod.blikCode`. Its code snippets illustrate PL/PLN and a `777987` code, while the separate test instruction says use `999000`; do not treat the sample code as the test code. (raw lines 62–395, 441–451)
- **Pending and final outcome:** the shown `/payments` response has `resultCode: Pending` and an `await` action for a waiting screen while the shopper completes payment in the BLIK app. `Refused` may also be returned, such as for an incorrect code. The page directs the merchant to an `AUTHORISATION` webhook: `success: false` means failure and `success: true` means shopper completion. A `Pending` response is not authorization or capture. Its “present payment result” sentence tells readers to use the original `/payments` `resultCode`, but the same section explicitly says to wait for webhooks for the outcome; treat the webhook as the final outcome authority. (raw lines 397–439; repeated 502–544)
- **One Click consent and token:** its One Click section adds `shopperReference` to `/paymentMethods` and says to include the stored account `label` when rendering the no-code choice. To request consent for future payments without a six-digit code, it lists `shopperReference`, `storePaymentMethod: true` and `recurringProcessingModel: CardOnFile` with the code-payment fields. If consent is given, a `recurring.token.created` lifecycle webhook carries `storedPaymentMethodId`, initial transaction `eventId` and `shopperReference`. This page does not specify a subsequent token-payment request. The displayed consent curl JSON is malformed: it uses a string `"true"` and omits the comma before `"amount"`; do not copy it as a valid request. The prose names `additionalData.BLIK.APP_LABEL` while the example object spells `Blik.APP_LABEL`; confirm the actual field against the relevant API response before relying on the case. (raw lines 455–567)
- **Testing/live gates:** both paths say to use BLIK code `999000`, follow BLIK guidelines and test end-to-end. The code path says add BLIK in the live Customer Area. The One Click live section additionally says to reach out to BLIK for certification and enablement, then add BLIK in the live Customer Area. These are source-defined gates, not evidence that certification or activation occurred. (raw lines 50–60, 441–451, 569–582)

## Detail locators

- Historical timestamp, Web Drop-in requirements, v6 import and Sessions statement: pinned raw lines 5–48.
- BLIK code discovery, PL/PLN and `/payments` fields/examples: pinned raw lines 62–395.
- Intermediate `Pending`/`await`, waiting screen, `Refused` and webhook outcome: pinned raw lines 397–439.
- One Click discovery, consent fields, malformed curl, token webhook and label-key mismatch: pinned raw lines 455–567.
- Test code and distinct live/One Click certification gates: pinned raw lines 50–60, 441–451 and 569–582.

## Related

- [[adyen-online-payments]] — main provider payment and webhook context
- [[adyen-tokenization]] — provider stored-method lifecycle
- [[source-adyen-docs-payment-methods-blik]] — BLIK overview

## Raw Sources

- [[raw/adyen/docs/payment-methods/blik/web-drop-in/2026-09-15|BLIK Web Drop-in guide, 2020-modified and 2026-09-15-captured]]
