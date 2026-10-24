---
title: "Adyen KakaoPay React Native Drop-in integration"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/kakaopay/react-native-drop-in"
raw_files:
  - "adyen/docs/payment-methods/kakaopay/react-native-drop-in/2026-09-15.md"
tags: [adyen, kakaopay, react-native, drop-in, recurring, redirect]
---

## Overview

This [[adyen]] guide adds KakaoPay to an existing **React Native Drop-in** integration using **Sessions** or **Advanced** server-side flows. It separately documents recurring-token creation and later token payments through `/payments`. The method add-on, shopper redirect, token-creation request, settlement-conditioned token webhook and later payment request are distinct events; none alone proves final authorization, capture or settlement of a later charge. [[adyen-online-payments]]

## Key takeaways

- **Base Sessions add-on:** The guide requires existing React Native Drop-in Sessions, **Checkout API v68 or later**, `action.type: redirect` handling and KakaoPay added in Customer Area. It says no extra KakaoPay parameters for the base `/sessions` request and no extra KakaoPay client configuration. Its integration-type label says Sessions but its URL points to **Advanced** Drop-in; the other Sessions-step URLs point to Sessions. The no-extra statement is method-specific, not an empty base request or a waiver of the recurring `/payments` fields below. See raw lines 25–48.
- **Base Advanced add-on:** The Advanced section requires an existing React Native Drop-in Advanced flow, redirect handling and Customer Area method setup. It says no extra KakaoPay client configuration or base `/payments` parameters. The Advanced table does **not** restate the Sessions v68+ requirement. The later recurring-token instructions are conditional additions for tokenization and use, not a contradiction of the one-time base add-on. See raw lines 300–322 and 324–363.
- **Create a recurring token:** For the recurring flow, the guide instructs a `/payments` request with `storePaymentMethod: true` and a merchant-unique `shopperReference`, followed by the shopper's Kakao login and confirmation. It says **when the payment has settled**, a `recurring.token.created` webhook carries `shopperReference`, initial-payment `pspReference` as `eventId`, and `storedPaymentMethodId`. The server must receive recurring-token lifecycle events. Requesting storage or observing shopper confirmation is not the token-created event. The page does not specify a separate consent-record mechanism or guarantee that settlement will occur. See raw lines 50–75 and 324–349.
- **Use a token later:** The later `/payments` request uses the webhook token (or a value obtained from `/listRecurringDetails`), the same `shopperReference`, `shopperInteraction: ContAuth`, and `recurringProcessingModel: Subscription` for fixed intervals or `UnscheduledCardOnFile` for non-fixed intervals. Example requests show `type: kakaopay`, KRW and merchant/reference placeholders. The curl sample targets TEST Checkout v68; Node, Python and Ruby snippets name particular API-library versions, so none defines a universal React Native SDK or current API requirement. Sample amounts differ, including Java's KRW 15000 versus KRW 1000 in other examples. See raw lines 77–288 and 351–562.
- **TEST/LIVE wording:** Both sections say successful **live** payment testing needs a real mobile number registered with a KakaoPay account, then point to the **test** Customer Area payment list for “test payments”; the page does not reconcile those environments. It separately says to submit a KakaoPay request in **live** Customer Area before accepting live payments. A submitted request or payment-list lookup does not prove live approval or a final outcome. See raw lines 290–298 and 564–572.

## Detail locators

- Sessions base requirements and method-specific additions: raw lines 25–48.
- Sessions token creation/webhook/reuse: raw lines 50–89; versioned example variants: raw lines 91–288.
- Advanced base requirements and token lifecycle: raw lines 300–363; examples: raw lines 365–562.
- Test/live statements: raw lines 290–298 and 564–572.

## Related

- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[source-adyen-docs-payment-methods-kakaopay]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/kakaopay/react-native-drop-in/2026-09-15|Adyen KakaoPay React Native Drop-in guide]]
