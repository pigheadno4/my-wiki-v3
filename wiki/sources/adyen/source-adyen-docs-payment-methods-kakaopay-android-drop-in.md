---
title: "KakaoPay Android Drop-in"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/kakaopay/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/kakaopay/android-drop-in/2026-09-15.md"
tags: [adyen, kakaopay, android, drop-in, tokenization]
---

## Overview

This 2026-09-15 Adyen guide adds KakaoPay to an **existing Android Drop-in integration**, split between Sessions and Advanced server-side flows. The base payment instructions and the conditional recurring-token route have different request requirements; neither a redirect nor a token-request field proves a completed payment or issued token. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions base flow:** requires an existing Android Drop-in Sessions integration with **Checkout API v68 or later** and KakaoPay added in Customer Area. It says no additional KakaoPay-specific `/sessions` or Drop-in configuration parameters are needed. This Sessions requirements table does **not** state redirect handling; the explicit `action.type: redirect` row is in Advanced. (raw lines 25–46, 300–309)
- **Advanced base flow:** requires an existing Advanced Android Drop-in integration, redirect handling for `action.type: redirect`, and KakaoPay added in Customer Area. It says no additional KakaoPay-specific Drop-in configuration or `/payments` parameters for a base payment. The Advanced section states no Checkout API minimum; v68 is stated for Sessions and illustrated in recurring curl examples. (raw lines 300–320, 363–384)
- **Recurring creation is conditional:** the guide says to include `storePaymentMethod: true` and `shopperReference` in a `/payments` request. This triggers a Kakao account login and shopper confirmation flow. It says the `recurring.token.created` webhook arrives **when the initial payment has settled**, containing `shopperReference`, `eventId` equal to the initial `pspReference`, and `storedPaymentMethodId`; the merchant server must be able to receive token lifecycle events. These recurring fields qualify the base-flow no-extra-fields wording. (raw lines 48–73, 322–347)
- A later token payment uses `paymentMethod.storedPaymentMethodId` from the webhook or `/listRecurringDetails`, the same `shopperReference`, `shopperInteraction: ContAuth`, and `recurringProcessingModel: Subscription` for fixed intervals or `UnscheduledCardOnFile` for non-fixed intervals. TEST curl and API-library snippets show KRW and `paymentMethod.type: kakaopay`; sample requests do not demonstrate token issuance, approval, authorization, capture or settlement. (raw lines 75–87, 89–285, 349–361, 363–559)
- Examples differ: Java uses **KRW 15000** while curl and most others use **KRW 1000**; Java/PHP/C# include `returnUrl` while curl/Node/Python/Ruby do not. Treat these as sample variations, not a universal amount or return-URL rule. (raw lines 91–141, 152–195, 198–285; repeated at 365–559)
- The test/live prose says a real mobile number registered with a KakaoPay account is needed to test successful **live** payments, separately points to test Customer Area for test-payment status, and requires a KakaoPay request in **live Customer Area** before live acceptance. The wording does not establish actual TEST/LIVE success or live method approval. (raw lines 288–298, 562–570)

## Detail locators

- Sessions prerequisites and base no-extra request/configuration: raw lines 25–46.
- Sessions recurring creation, settlement-gated webhook and later token request: raw lines 48–87.
- TEST recurring examples and variation: raw lines 89–285.
- Advanced redirect/base setup and recurring parallel: raw lines 300–361.
- Advanced examples and test/live wording: raw lines 363–570.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[source-adyen-docs-payment-methods-kakaopay]]
- [[source-adyen-docs-payment-methods-kakaopay-android-component]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/kakaopay/android-drop-in/2026-09-15|Adyen KakaoPay Android Drop-in, 2026-09-15 snapshot]]
