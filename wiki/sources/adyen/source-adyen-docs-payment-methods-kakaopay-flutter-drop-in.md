---
title: "KakaoPay Flutter Drop-in"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/kakaopay/flutter-drop-in"
raw_files:
  - "adyen/docs/payment-methods/kakaopay/flutter-drop-in/2026-09-15.md"
tags: [adyen, kakaopay, flutter, drop-in, tokenization]
---

## Overview

This 2026-09-15 Adyen guide adds KakaoPay to an **existing Flutter Drop-in integration** for Sessions or Advanced server-side flow. Its base payment add-on and its optional recurring-token path have different request requirements. It delegates redirect handling to the main integration guides and gives no observed payment or token outcome. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions base flow:** requires an existing Flutter Drop-in Sessions integration, **Checkout API v68 or later**, redirect handling for `action.type: redirect`, and contacting **Adyen Support** to add KakaoPay in Customer Area. It says no additional KakaoPay-specific `/sessions` or Drop-in configuration parameters are needed for the base flow. The Sessions integration-type label links to an **advanced-flow** URL, while its redirect and session links point to Sessions. (raw lines 25–48)
- **Advanced base flow:** requires an existing Advanced Flutter Drop-in integration, redirect handling for `action.type: redirect`, and adding KakaoPay in Customer Area. It says no additional KakaoPay-specific Drop-in configuration or `/payments` parameters for the base payment. The section does not state a Checkout API minimum; the v68 prerequisite is in Sessions. Its Customer Area setup phrasing differs from the Sessions Support-contact instruction. (raw lines 300–322)
- **Recurring is conditional and separate:** to create a shopper token, the guide says to include `storePaymentMethod: true` and `shopperReference` in a `/payments` request. That initiates the Kakao account login and shopper confirmation route; it does not mean every base Sessions/Advanced payment needs those fields. The page says a `recurring.token.created` webhook arrives **when the initial payment has settled**, with `shopperReference`, `eventId` equal to the initial `pspReference`, and `storedPaymentMethodId`. The merchant server needs to receive recurring token lifecycle events. Token creation should not be inferred from redirect or request submission alone. (raw lines 50–75, 324–349)
- For a later token payment, the stated `/payments` fields are `paymentMethod.storedPaymentMethodId` (from the webhook or `/listRecurringDetails`), matching `shopperReference`, `shopperInteraction: ContAuth`, and `recurringProcessingModel: Subscription` for fixed intervals or `UnscheduledCardOnFile` for non-fixed intervals. Examples show `paymentMethod.type: kakaopay`, KRW, TEST Checkout v68 curl and language-specific API-library code. These examples illustrate a request shape, not consent, token issuance, authorization, capture or settlement results. (raw lines 77–89, 91–288, 351–363, 365–562)
- Example details differ: curl and most language samples use KRW **1000**, while Java uses **15000**; Java/PHP/C# include `returnUrl` where curl/Node/Python/Ruby examples omit it. No universal amount or return-URL rule should be derived from those snippets. (raw lines 93–143, 154–170, 175–197, 200–288; repeated at 367–561)
- The test/live prose says a **real mobile number registered with a KakaoPay account** is needed to test successful **live** payments, points separately to test Customer Area for test-payment status, and requires a KakaoPay request in live Customer Area before live acceptance. This mixed test/live wording should be preserved rather than treated as proof that TEST and LIVE use the same credentials or that a live request was approved. (raw lines 290–298, 564–572)

## Detail locators

- Sessions prerequisites, redirect, Support setup and no-extra base fields/config: raw lines 25–48.
- Sessions recurring creation, settlement-gated webhook and later token request: raw lines 50–89.
- TEST recurring request/library examples and their amount/returnUrl differences: raw lines 91–288.
- Advanced base-flow requirements and recurring parallel: raw lines 300–363.
- Advanced example repetition and test/live instructions: raw lines 365–572.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[source-adyen-docs-payment-methods-kakaopay]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/kakaopay/flutter-drop-in/2026-09-15|Adyen KakaoPay Flutter Drop-in, 2026-09-15 snapshot]]
