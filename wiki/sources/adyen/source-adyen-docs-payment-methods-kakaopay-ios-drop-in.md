---
title: "Adyen KakaoPay iOS Drop-in integration"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/kakaopay/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/kakaopay/ios-drop-in/2026-09-15.md"
tags: [adyen, kakaopay, ios, drop-in, recurring]
---

## Overview

This [[adyen]] guide adds KakaoPay to an existing **iOS Drop-in** integration with **Sessions** and **Advanced** server-side paths. A separate recurring section describes initial token creation and later server-side token payments. Base method setup, shopper confirmation, the settlement-conditioned token webhook and a future charge are distinct stages; none alone proves a future authorization, capture or settlement. [[adyen-online-payments]]

## Key takeaways

- **Base Sessions add-on:** The guide requires existing iOS Drop-in Sessions with **Checkout API v68 or later** and KakaoPay added in Customer Area. It says no extra KakaoPay parameters are needed for the base `/sessions` request and no extra client configuration. The Sessions requirements table does **not** separately state redirect handling; follow the linked base flow for action/return behavior. “No extra” is method-specific, not a waiver of base requests or the recurring `/payments` fields below. See raw lines 25–46.
- **Base Advanced add-on:** The Advanced table requires existing iOS Drop-in Advanced, explicit `action.type: redirect` handling and KakaoPay in Customer Area; it says no extra KakaoPay configuration or base `/payments` parameters. It does not restate the Sessions v68+ minimum as an Advanced-specific prerequisite. See raw lines 300–322.
- **Create a recurring token:** In either recurring section, the initial `/payments` request adds `storePaymentMethod: true` and a merchant-unique `shopperReference`. The guide says the shopper logs into Kakao and confirms the recurring transaction; **when the payment has settled**, a `recurring.token.created` webhook contains the shopper reference, initial payment `pspReference` as `eventId`, and `storedPaymentMethodId`. The server must receive token lifecycle events. The page does not specify a separate consent-record mechanism; storage request or shopper return is not the token-created event. See raw lines 48–73 and 324–349.
- **Pay with the token:** A subsequent `/payments` request uses the webhook token or a value from `/listRecurringDetails`, the same `shopperReference`, `shopperInteraction: ContAuth`, and `recurringProcessingModel: Subscription` for fixed intervals or `UnscheduledCardOnFile` for non-fixed intervals. The curl example targets TEST Checkout v68; Node, Python and Ruby examples name API-library versions. Example amounts differ: Java uses KRW 15000 while several others use KRW 1000. These examples do not define a universal iOS SDK version, current live behavior or payment result. See raw lines 75–285 and 351–561.
- **Test/live wording:** Both sections say successful **live** testing needs a real registered KakaoPay mobile number, then point to the **test** Customer Area list for “test payments,” without reconciling those environments. Live acceptance separately calls for a KakaoPay request in **live** Customer Area. A request submission or list lookup does not establish approval or final transaction state. See raw lines 288–298 and 564–574.

## Detail locators

- Sessions base requirements and method-specific additions: raw lines 25–46.
- Sessions token creation/webhook/reuse and examples: raw lines 48–285.
- Advanced base requirements and recurring section/examples: raw lines 300–561.
- Duplicated test/live statements: raw lines 288–298 and 564–574.

## Related

- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[source-adyen-docs-payment-methods-kakaopay]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/kakaopay/ios-drop-in/2026-09-15|Adyen KakaoPay iOS Drop-in guide]]
