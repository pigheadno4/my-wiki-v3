---
title: "Adyen BLIK iOS Component guide"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/blik/ios-component"
raw_files:
  - "adyen/docs/payment-methods/blik/ios-component/2026-09-15.md"
tags: [adyen, blik, ios, components, poland, tokenization]
---

## Overview

This 2026-09-15 Adyen page describes adding BLIK to an existing iOS Components integration. It gives distinct v5.0.0-or-later Sessions and Advanced Component delegate examples, an earlier-version example, and later `/payments` instructions for BLIK with code and BLIK One Click. The latter server-side passages should not be read as extra `/sessions` fields or as proof that an iOS Component payment completed. See [[adyen]], [[adyen-online-payments]], [[adyen-ios-sdk]] and [[adyen-tokenization]].

## Key takeaways

- The page requires an existing iOS Components integration, at least Components v3.8.0 for BLIK, and BLIK added in the test Customer Area. Its v5.0.0-or-later Swift examples select `BLIKPaymentMethod`, create `BLIKComponent`, and set the delegate to `session` for Sessions or `self` for Advanced. An earlier-version example uses `FormComponentStyle` and `apiContext`. The page says no BLIK-specific Component configuration is required, and its `/sessions` tab says no extra BLIK fields are needed. The earlier-version section labels itself `v4.x.x`, while its prose says only an earlier version; do not infer support below the stated v3.8.0 minimum.
- The subsequent `/paymentMethods` and `/payments` sections describe a BLIK-with-code server route: PL and PLN discovery; `paymentMethod.type: blik` plus the shopper-entered six-digit `blikCode` in `/payments`. Its `Pending` response and `action` lead to a waiting screen while the shopper confirms in the BLIK app. The page says the `AUTHORISATION` webhook, with `success` true or false, supplies the eventual payment outcome; `Pending` is not success. It also lists `Refused`, for example an incorrect code. These sections appear after a duplicated Test and go live heading and are not presented as an iOS Component-specific callback contract.
- For BLIK One Click, the page asks for `shopperReference` in `/paymentMethods` and says a stored BLIK method appears for a previously signed-up shopper. It describes a consent request using `shopperReference`, `storePaymentMethod: true`, and `recurringProcessingModel: CardOnFile` alongside a code payment. After consent, a `recurring.token.created` webhook supplies a stored method ID, event ID and shopper reference; a later `/paymentMethods` response supplies a linked-issuer label. The page does not describe a complete later no-code payment request or guarantee token creation.
- TEST instructions give code `999000` and end-to-end testing. The page requires adding BLIK in the live Customer Area; its One Click live section additionally calls for BLIK certification and enablement. This captured documentation does not establish current account eligibility, certification, or live execution.
- Source caveats: the first `/paymentMethods` paragraph repeats `paymentMethod.type: blik` and conditions a `storedPaymentMethods` entry on earlier One Click signup, whereas the later One Click paragraph states both appear without that condition. The consent curl example has `storePaymentMethod` as a string and omits a comma after `recurringProcessingModel`, so it is not a valid literal JSON request. The prose names `additionalData.BLIK.APP_LABEL` while its example uses `Blik.APP_LABEL`. The page also mixes BLIK-app completion with a bank-app waiting-screen label and tells an iOS guide to redirect to a website. Preserve those source differences rather than treating either wording or the examples as a resolved integration contract.

## Detail locators

- Requirements and Component versions/delegates: pinned raw lines 21–85; `/sessions` field note: lines 87–95.
- BLIK-with-code discovery/request and multi-language examples: pinned raw lines 109–128 and 130–441; `Pending` action, waiting screen, webhook and `Refused`: lines 444–486.
- One Click discovery, consent, example and result/webhook: pinned raw lines 500–601; issuer-label prose/example discrepancy: lines 601–614.
- TEST/live steps and One Click certification: pinned raw lines 97–107, 488–498 and 616–629.

## Related

- [[adyen-online-payments]] — main online-payment and result-state concept
- [[adyen-ios-sdk]] — native Component and Sessions/Advanced boundary
- [[adyen-tokenization]] — stored-method and token webhook context

## Raw Sources

- [[raw/adyen/docs/payment-methods/blik/ios-component/2026-09-15|BLIK iOS Component guide, 2026-09-15]]
