---
title: "Adyen KakaoPay Flutter Component"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/kakaopay/flutter-component"
raw_files:
  - "adyen/docs/payment-methods/kakaopay/flutter-component/2026-09-15.md"
tags: [adyen, kakaopay, flutter, components, recurring-payments]
---

## Overview

This [[adyen]] guide describes KakaoPay-specific additions to an existing **Flutter Components** integration, divided into Sessions and Advanced server-side flows. It does not replace the main flow guides. See [[adyen-online-payments]] and [[adyen-tokenization]]. The 2026-09-15 snapshot and illustrative requests do not establish current merchant enablement, token issuance, payment authorization or settlement. See raw lines 15–23.

## Base payment requirements

- **Sessions:** The table requires an existing Sessions Flutter Components integration, Checkout API **v68 or later**, `action.type: redirect` handling, and KakaoPay added in Customer Area. It says a base `/sessions` request needs no extra KakaoPay parameters and no extra KakaoPay Component configuration. The table's **Integration type** link is anomalous: despite its Sessions Components prose, its URL points to `advanced-flow?platform=Flutter&integration=Drop-in`; use the prose and independently verify the proper main guide rather than treating that URL as a matching Sessions Components guide. See raw lines 25–46.
- **Advanced:** The table requires an existing Advanced Flutter Components integration, redirect handling and Customer Area method addition. It likewise says no extra KakaoPay configuration and no extra parameters in the base `/payments` request. The Advanced table's **Integration type** link also says `integration=Drop-in` despite Components prose, while its redirect/payment links do specify Components. The Advanced table does not restate the Sessions v68+ requirement; do not silently transfer that explicit row between sections. See raw lines 298–320.
- These no-extra-parameter statements describe **ordinary base payments**. Both recurring sections specify added fields for token creation and later token-funded `/payments`; the Sessions guide's recurring subsection uses `/payments` despite the base session using `/sessions`. See raw lines 38–46, 57–87, 316–361.

## Recurring token and outcome boundary

- To create a token, the merchant includes `storePaymentMethod: true` and its unique `shopperReference` in `/payments`. The shopper logs in to a Kakao account and confirms the recurring transaction. After the initial payment **has settled**, the merchant server must receive `recurring.token.created`, carrying `shopperReference`, initial payment `pspReference` as `eventId`, and `storedPaymentMethodId`. Shopper confirmation or request submission does not itself establish settlement or a reusable token. See raw lines 48–73 and 322–347.
- Subsequent `/payments` requests use `paymentMethod.storedPaymentMethodId` from that webhook (with `/listRecurringDetails` stated as an alternative retrieval route), the original shopper reference, `shopperInteraction: ContAuth`, and `recurringProcessingModel: Subscription` for fixed intervals or `UnscheduledCardOnFile` for non-fixed intervals. The code examples select `Subscription` and `KRW`; they are not proof that another model/currency is enabled or that any payment succeeded. See raw lines 75–110 and 349–384.
- Samples use Checkout **test** `v68/payments`, placeholder keys and TEST client settings, and identify particular server-library versions (Node v16.1.0, Python v12.0.0, Ruby v9.1.0). Node, Python and Ruby examples show idempotency keys; this is snippet detail, not a universal assertion about every shown client or a live operation. See raw lines 89–286 and 363–560.
- The page says successful **live** KakaoPay payment testing requires a real registered mobile number; test payment status can be checked in the **test** Customer Area; before live acceptance, a request for KakaoPay must be submitted in the **live** Customer Area. These are distinct conditions and checks, not proof of approval or a successful live payment. See raw lines 288–296 and 562–570.

## Detail locators

- **Sessions requirements, anomalous main-guide URL and base no-extra fields/configuration:** raw lines 25–46.
- **Sessions token creation, settlement webhook and subsequent charge fields:** raw lines 48–87.
- **Advanced requirements, anomalous Drop-in link and base no-extra fields/configuration:** raw lines 298–320.
- **Advanced repeated token flow:** raw lines 322–361.
- **Test snippets, environments and library-version labels:** raw lines 89–286 and 363–560.
- **Testing/live setup boundary:** raw lines 288–296 and 562–570.

## Related

- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[adyen-webhooks]]

## Related raw API references

- [[raw/adyen/docs/payment-methods/kakaopay/2026-09-15|KakaoPay overview]] — method capability and channel context; distinct from this Flutter Components guide.

## Raw Sources

- [[raw/adyen/docs/payment-methods/kakaopay/flutter-component/2026-09-15|KakaoPay Flutter Component — captured 2026-09-15]]
