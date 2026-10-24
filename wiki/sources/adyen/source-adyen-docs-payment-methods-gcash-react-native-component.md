---
title: "Adyen GCash React Native Component"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/gcash/react-native-component"
raw_files:
  - "adyen/docs/payment-methods/gcash/react-native-component/2026-09-15.md"
tags: [adyen, gcash, react-native, components, recurring-payments]
---

## Overview

This [[adyen]] page is at the **React Native Component** URL but titled “GCash React Component” in the raw heading. Its body gives GCash-specific additions to an existing React Native **Components** integration. It explicitly says React Native Components **do not support Sessions flow**; the supported route described here is Advanced. See [[adyen-online-payments]] and [[adyen-tokenization]]. The historical instructions and examples do not establish current merchant enablement, an approved live integration or a completed payment. See raw lines 15–31.

## Advanced base payment

- Requires an existing Advanced React Native Components integration, `action.type: redirect` handling, and GCash added in Customer Area. The **Integration type** link says Components but its URL has `integration=Drop-in`; the redirect and payment step links are Components-scoped. Use the stated Components flow and verify the main guide rather than relying on that mismatched prerequisite link. See raw lines 31–41.
- The guide states no extra GCash configuration and no extra GCash-specific fields for the **ordinary base `/payments`** request. This does not waive the base Advanced integration, redirect handling or later recurring-specific request fields. See raw lines 43–53.

## Recurring and outcome boundary

- To create a GCash shopper token, include `storePaymentMethod: true` and a merchant-unique `shopperReference` of **at least three characters** in `/payments`. The server must receive recurring token lifecycle webhooks. **After the initial payment settles**, `recurring.token.created` carries `shopperReference`, initial payment `pspReference` as `eventId`, and `storedPaymentMethodId`. A request or redirect return is not settlement/token proof. See raw lines 55–78.
- A later token-funded `/payments` request uses `paymentMethod.storedPaymentMethodId` from the webhook (or the stated `/listRecurringDetails` alternative), the same shopper reference, `shopperInteraction: ContAuth`, and `recurringProcessingModel: Subscription` for fixed intervals or `UnscheduledCardOnFile` for non-fixed intervals. The sample uses `PHP` and `Subscription`; these are illustrative, not a successful payment or universal model guarantee. See raw lines 80–115.
- Example server calls use Checkout **TEST** `/checkout/v68/payments`, placeholder keys and TEST language-client settings; Node/Python/Ruby snippets label specific library versions and show idempotency keys. The `v68` example is not a separately stated minimum for this Advanced React Native guide, nor an SDK-version requirement or a live transaction. See raw lines 94–291.
- To test successful **live** payments the page says a real GCash-registered mobile number is needed; **test** status is checked in the test Customer Area; and before live acceptance a GCash request must be submitted in the live Customer Area. These statements are distinct environment/setup conditions and do not prove approval or a completed transaction. The page does not specify a final authorization webhook contract for the initial redirect payment. See raw lines 293–301.

## Detail locators

- **URL/title scope and unsupported Sessions:** raw lines 5–29.
- **Advanced prerequisites and mismatched Drop-in URL:** raw lines 31–41.
- **Base no-extra configuration/payment fields:** raw lines 43–53.
- **Three-character shopper reference and settled-payment token webhook:** raw lines 55–78.
- **Subsequent token payment and models:** raw lines 80–92.
- **TEST snippets/library labels:** raw lines 94–291.
- **Test/live conditions:** raw lines 293–301.

## Related

- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[adyen-webhooks]]

## Related raw API references

- [[raw/adyen/docs/payment-methods/gcash/2026-09-15|GCash overview]] — PH/PHP, redirect lifetime and shopper journey; separate from this React Native Component add-on.

## Raw Sources

- [[raw/adyen/docs/payment-methods/gcash/react-native-component/2026-09-15|GCash React Native Component URL — captured 2026-09-15]]
