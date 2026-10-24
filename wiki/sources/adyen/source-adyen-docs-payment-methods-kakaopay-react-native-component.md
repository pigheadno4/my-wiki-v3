---
title: "KakaoPay React Native Component"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/kakaopay/react-native-component"
raw_files:
  - "adyen/docs/payment-methods/kakaopay/react-native-component/2026-09-15.md"
tags: [adyen, kakaopay, react-native, components, tokenization]
---

## Overview

This 2026-09-15 Adyen guide at a **React Native Component** URL says React Native Components **do not support Sessions flow** and gives only an **Advanced** KakaoPay add-on. The page title itself reads “KakaoPay React Component,” while its prerequisite names React Native; preserve that title/URL discrepancy rather than treating it as a separate Web React guide. Setup and recurring request examples do not prove a live payment or token was created. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- The Sessions section explicitly says **React Native Components do not support Sessions flow**. Advanced requires an existing React Native Components Advanced integration, redirect handling for `action.type: redirect`, and KakaoPay added in Customer Area. The Advanced **Integration type** link points to `integration=Drop-in` despite its Components label; the redirect and payment links point to Components. No SDK or Checkout API minimum is stated for the Advanced integration on this page. (raw lines 25–41, 49–53)
- For a **base Advanced payment**, the page says no additional KakaoPay-specific configuration or `/payments` parameters. That statement does not remove the separate conditional fields for requesting a recurring token. (raw lines 43–53, 55–80)
- To request a **recurring token**, include `storePaymentMethod: true` and `shopperReference` in the initial `/payments` request. This triggers Kakao account login and shopper confirmation. The guide says a `recurring.token.created` webhook containing `shopperReference`, initial payment `pspReference` as `eventId`, and `storedPaymentMethodId` is received **when the payment has settled**; the merchant server must receive token lifecycle events. Request submission or redirect is not token issuance. (raw lines 55–80)
- A later token payment uses `paymentMethod.storedPaymentMethodId` (from the webhook or `/listRecurringDetails`), matching `shopperReference`, `shopperInteraction: ContAuth`, and `recurringProcessingModel: Subscription` for fixed intervals or `UnscheduledCardOnFile` for non-fixed intervals. TEST Checkout **v68** curl and several language-library examples illustrate `paymentMethod.type: kakaopay` and KRW; these are sample requests, not a stated minimum version or an observed authorization/capture/settlement. (raw lines 82–117, 119–293)
- The samples vary: curl and most libraries use KRW **1000**, while Java uses **15000**; Java/PHP/C# include `returnUrl`, while curl/Node/Python/Ruby omit it. Do not infer a universal amount or return-URL requirement from these examples. (raw lines 98–148, 159–203, 205–293)
- The test/live prose says a **real mobile number registered with a KakaoPay account** is needed to test successful **live** payments, separately points to **test Customer Area** for test-payment status, and requires a request for KakaoPay in **live Customer Area** before live acceptance. It reports neither method approval nor an actual payment or recurring webhook outcome. (raw lines 295–303)

## Detail locators

- Sessions unsupported and Advanced prerequisites/link mismatch: raw lines 25–41.
- Base Advanced configuration/parameter statements: raw lines 43–53.
- Initial recurring request, Kakao confirmation and settlement-gated token webhook: raw lines 55–80.
- Later token payment fields and TEST examples: raw lines 82–293.
- TEST/live wording and separate live request: raw lines 295–303.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[source-adyen-docs-payment-methods-kakaopay]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/kakaopay/react-native-component/2026-09-15|Adyen KakaoPay React Native Component, 2026-09-15 snapshot]]
