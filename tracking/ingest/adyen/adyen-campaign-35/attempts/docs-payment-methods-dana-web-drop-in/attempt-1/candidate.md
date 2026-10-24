---
title: "Adyen DANA Web Drop-in"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/dana/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/dana/web-drop-in/2026-09-16.md"
tags: [adyen, dana, web-drop-in, redirect-payments, recurring-payments]
---

## Overview

This [[adyen]] guide adds DANA to an **existing Web Drop-in** integration in separate Sessions and Advanced flows. It gives DANA-specific additions, not the whole base Web implementation. The pinned raw is captured **2026-09-16**, while this source was ingested 2026-10-25. See [[adyen-online-payments]] and [[adyen-tokenization]]. Its examples and instructions do not prove current merchant eligibility, a settled initial payment or a reusable token. See raw lines 1–23.

## Base requests and redirect

- **Sessions:** Requires an existing Sessions Web Drop-in integration, Checkout API **v68 or later**, redirect handling for `action.type: redirect`, and DANA added in Customer Area. No additional DANA-specific fields are needed for the ordinary `/sessions` request. Optional tree-shaken Adyen Web import includes `Redirect`. See raw lines 25–54.
- **Advanced:** Requires an existing Advanced Web Drop-in integration, redirect handling and DANA added in Customer Area. Its Integration type link contains an **unresolved encoded platform template** at raw line 314 despite saying Web Drop-in; use the stated Web context and Web-scoped Advanced step links at lines 315 and 322, rather than treating that prerequisite URL as reliable. The Advanced section does not repeat the Sessions v68 minimum. No additional DANA-specific fields are needed for the ordinary base `/payments` request; optional tree-shaken import likewise includes `Redirect`. See raw lines 306–334.
- “No additional parameters” is a **base-payment** statement only. Both recurring sections then require specific fields in `/payments`; the Sessions recurring subsection uses `/payments` despite the base Sessions payment-session request using `/sessions`. Keep these request contexts distinct. See raw lines 40–42, 65–93, 332–373.

## Recurring and outcome boundary

- To create a token, include `storePaymentMethod: true` and a merchant-unique `shopperReference` in `/payments`. The merchant server must be configured to receive recurring token lifecycle events. **When the payment has settled**, `recurring.token.created` carries `shopperReference`, the initial payment's `pspReference` as `eventId`, and `storedPaymentMethodId`. Redirect handling or request submission is not itself proof of settlement or token creation. See raw lines 56–79 and 336–359.
- Later token-funded `/payments` includes `paymentMethod.storedPaymentMethodId` from that webhook (or the stated `/listRecurringDetails` alternative), the same shopper reference, `shopperInteraction: ContAuth`, and `recurringProcessingModel: Subscription` for fixed-interval contracts or `UnscheduledCardOnFile` for non-fixed intervals. The sample selects `Subscription` and `IDR`; that does not guarantee payment success or universal model eligibility. See raw lines 81–115 and 361–395.
- The samples use TEST `/checkout/v68/payments`, API-key placeholders and TEST server-library settings; Node/Python/Ruby snippets name their library versions and show idempotency-key examples. These illustrate request shape, not a live transaction, a Web SDK version minimum or a guarantee that all language snippets are equivalent. See raw lines 95–292 and 375–572.
- The repeated test/live section says a real DANA-registered mobile number is needed to test successful **live** payments, **test** payment status is checked in test Customer Area, and accepting **live** DANA payments first requires a request in live Customer Area. Those are separate environment/approval conditions, not evidence that a request was accepted or an actual payment completed. See raw lines 294–304 and 574–584.

## Detail locators

- **Sessions requirements, base request and optional import:** raw lines 25–54.
- **Advanced requirements, unresolved template and base request:** raw lines 306–334.
- **Token creation and settlement-gated webhook:** raw lines 56–79 and 336–359.
- **Later token fields and model choice:** raw lines 81–93 and 361–373.
- **TEST example/library scope:** raw lines 95–292 and 375–572.
- **Test/live qualification:** raw lines 294–304 and 574–584.

## Related

- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[adyen-webhooks]]

## Related raw API references

- [[raw/adyen/docs/payment-methods/dana/2026-09-15|DANA overview]] — ID/IDR method scope, five-minute default redirect lifetime and 300-IDR floor; separate from this Web implementation guide.

## Raw Sources

- [[raw/adyen/docs/payment-methods/dana/web-drop-in/2026-09-16|DANA Web Drop-in — captured 2026-09-16]]
