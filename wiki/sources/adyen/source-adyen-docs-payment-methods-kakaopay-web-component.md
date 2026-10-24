---
title: "Adyen KakaoPay Web Component guide"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/kakaopay/web-component"
raw_files:
  - "adyen/docs/payment-methods/kakaopay/web-component/2026-09-15.md"
tags: [adyen, kakaopay, web-components, online-payments, redirects, tokenization]
---

## Overview

This [[adyen]] guide, last modified and captured 2026-09-15, describes **KakaoPay-specific additions** to an existing **Web Components** integration. It separates Sessions and Advanced server flows, both with redirect handling and Customer Area method setup, and describes a recurring-token path. It is not a standalone checkout guide or evidence of current KakaoPay availability, a shopper's completed redirect, authorization, capture, settlement or successful later charge. See [[adyen-online-payments]] and [[adyen-tokenization]].

## Key takeaways

- The **Sessions** branch requires an existing Web Components Sessions flow, **Checkout API v68 or later**, `action.type: redirect` handling, and KakaoPay added in Customer Area. It says no extra KakaoPay parameters for the ordinary `/sessions` creation or extra KakaoPay configuration. The **Advanced** branch similarly requires an existing Web Components Advanced flow, redirect handling and Customer Area setup, and says no extra KakaoPay `/payments` parameters. The v68 minimum appears in the Sessions table only; these no-extra-field statements presuppose the base integration. See raw lines 23–60 and 324–362.
- Both branches import `Redirect` from Adyen Web and show mounting a redirect Component. The literal snippet uses `{ type:kakaopay }` without quotes or a declared `kakaopay` variable, so its method identifier is unresolved as written; the instructions establish the intended Redirect class, not copy-ready code. See raw lines 44–72 and 334–356.
- For recurring use, the page directs an initial server `/payments` request with `storePaymentMethod: true` and a unique `shopperReference`. It says the shopper logs in to a Kakao account and **confirms the recurring transaction**. Only **when the initial payment has settled** does the page say a `recurring.token.created` webhook supplies `storedPaymentMethodId`; receiving that token requires recurring-token lifecycle webhook configuration. Do not equate a setup request, login or confirmation with token receipt or payment settlement. See raw lines 74–99 and 364–389.
- A later token payment uses the stored method ID, matching shopper reference, `shopperInteraction: ContAuth`, and `Subscription` for a fixed interval or `UnscheduledCardOnFile` for a non-fixed interval. The code shows **KRW** test examples at Checkout `/checkout/v68/payments`; the Java examples use 15000 while curl and several other languages use 1000, so these amounts are illustrative, not a single consistent transaction or a complete currency/region availability rule. Several server examples name older libraries and test environments; none proves a live authorization. See raw lines 101–312 and 391–602.
- The testing section says a real mobile number registered with a KakaoPay account is needed to test successful **live** payments, while separately mentioning test-payment status in test Customer Area. It also says a KakaoPay request in live Customer Area is needed before accepting live payments. Treat test/live context as the page states, without inferring an approved account or completed result. The guide does not describe a one-off final-result webhook, refund or capture procedure; those remain with the main integration and other method guidance. See raw lines 314–322 and 604–612.

## Detail locators

- **Sessions requirements, import and redirect initialization:** raw lines 23–72.
- **Sessions recurring token and subsequent `/payments` examples:** raw lines 74–312.
- **Advanced requirements, import, initialization and ordinary payment request:** raw lines 324–362.
- **Advanced recurring token and subsequent `/payments` examples:** raw lines 364–602.
- **Test/live wording and Customer Area method-request gate:** raw lines 314–322 and 604–612.

## Related

- [[adyen-online-payments]]
- [[adyen-tokenization]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/kakaopay/web-component/2026-09-15|KakaoPay Web Component — captured 2026-09-15]]
