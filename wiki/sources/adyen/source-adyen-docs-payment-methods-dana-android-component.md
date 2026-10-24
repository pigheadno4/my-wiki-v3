---
title: "Adyen DANA Android Component guide"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/dana/android-component"
raw_files:
  - "adyen/docs/payment-methods/dana/android-component/2026-09-15.md"
tags: [adyen, dana, android, component, recurring]
---

## Overview

This 2026-09-15 [[adyen]] guide adds **DANA** to an existing **Android Components** integration. It separates Sessions and Advanced server-side flows, both with redirect action handling, from a further tokenized recurring route. It is a method-specific supplement; it does not itself prove current Indonesia/IDR merchant eligibility, an operating DANA account, successful shopper return, authorization, capture or settlement. [[adyen-online-payments]] [[adyen-tokenization]]

## Key takeaways

- **Sessions base flow:** Requires an existing Sessions Android Components integration, **Checkout API v68 or later**, redirect handling for `action.type: redirect`, and DANA added in Customer Area. The page says no additional DANA-specific `/sessions` fields or Component configuration are needed. Android imports `com.adyen.checkout:instant:YOUR_VERSION` and, for Jetpack Compose, `components-compose`; it gets `dana` from `checkoutSession` and creates `InstantPaymentComponent`. The Compose key must change for a different screen or payment session/reset. See raw lines 23–125.
- **Advanced base flow:** Requires an existing Advanced Android Components integration, additional redirect-action handling and DANA in Customer Area. It says no additional DANA-specific ordinary `/payments` parameters or Component configuration are needed. The client selects `type == "dana"` from `/paymentMethods` and creates `InstantPaymentComponent`. Its requirement table does not independently restate the Sessions v68+ minimum. See raw lines 376–476.
- **Recurring token route:** To create a token, the server adds `storePaymentMethod: true` and a unique `shopperReference` to **`/payments`**. Only **when the initial payment has settled** does the guide say `recurring.token.created` delivers `storedPaymentMethodId`; the server must receive recurring-token lifecycle webhooks. Later token payments add the stored ID, same shopper reference, `shopperInteraction: ContAuth`, and `recurringProcessingModel: Subscription` for fixed intervals or `UnscheduledCardOnFile` for non-fixed intervals. The page does not specify a separate shopper-consent screen or make the redirect/API response proof of token creation. See raw lines 128–165 and 478–515.
- **Testing and live gate:** The page says a real mobile number registered with a DANA account is needed to test successful **live** DANA payments, directs test-payment status checks to TEST Customer Area, and requires a DANA request in LIVE Customer Area before accepting live payments. Its “test successful live” wording spans environments; it does not document a completed test or live merchant enablement. IDR, TEST API clients and amounts in the recurring snippets are examples, not a standalone country/currency eligibility matrix. See raw lines 167–374 and 517–724.

> [!warning] Contradiction
> The base-flow “no additional parameters” statements (raw lines 42 and 476) must not be applied to **recurring**: its token-creation and token-use sections expressly add `/payments` fields (raw lines 139–165 and 489–515). Also, the recurring request examples are not identical: Java uses an IDR amount of 15000 while the other language examples use 1000; curl/Node/Python/Ruby omit `returnUrl` while Java/PHP/C# include it (raw lines 169–363 and 519–713). Do not copy an example as a universal complete request.

## Detail locators

- Sessions prerequisite, method-specific additions, dependencies and Component: raw lines 23–125.
- Sessions token creation, settlement-gated webhook and token-payment fields: raw lines 128–165.
- Sessions recurring examples and TEST/LIVE statements: raw lines 167–374.
- Advanced prerequisite, Component and base `/payments` statement: raw lines 376–476.
- Advanced repeated recurring route, examples and TEST/LIVE statements: raw lines 478–724.

## Related

- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/dana/android-component/2026-09-15|Adyen DANA Android Component snapshot]]
