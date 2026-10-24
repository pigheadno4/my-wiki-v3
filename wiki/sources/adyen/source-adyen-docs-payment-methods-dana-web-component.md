---
title: "Adyen DANA Web Component guide"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/dana/web-component"
raw_files:
  - "adyen/docs/payment-methods/dana/web-component/2026-09-15.md"
tags: [adyen, dana, web, components, recurring]
---

## Overview

This 2026-09-15 [[adyen]] page describes adding **DANA** to an existing **Web Components** integration, with separate Sessions and Advanced server-side flows and a further recurring-token route. Both base flows use a redirect-oriented `Redirect` Component. It is a method-specific supplement, not an end-to-end proof of current ID/IDR merchant eligibility, a completed shopper return, authorization, capture or settlement. The DANA overview is a separate authority for country/currency and method-display conditions. [[adyen-online-payments]] [[adyen-tokenization]]

## Key takeaways

- **Sessions base flow:** Requires existing Sessions Web Components, **Checkout API v68 or later**, redirect handling for `action.type: redirect`, and DANA added in Customer Area. The page says no additional DANA-specific `/sessions` parameters or Component configuration are needed. It imports `Redirect` from `@adyen/adyen-web` and initializes it for DANA; no Web SDK version minimum is stated on this page. See raw lines 23–72.
- **Advanced base flow:** Requires existing Advanced Web Components, redirect handling and DANA in Customer Area. It imports and initializes `Redirect` and says no additional DANA-specific **ordinary** `/payments` parameters are needed. Its requirement table does not restate Sessions' v68+ Checkout API minimum, and this section does not separately repeat the Sessions no-extra-configuration statement. See raw lines 322–360.
- **Recurring token route:** To create a token, the server adds `storePaymentMethod: true` and a unique `shopperReference` to **`/payments`**. Only **when the initial payment has settled** does `recurring.token.created` deliver `storedPaymentMethodId`; the server must receive recurring-token lifecycle webhooks. For later token payments the guide specifies stored ID, same shopper reference, `shopperInteraction: ContAuth`, and `recurringProcessingModel: Subscription` for fixed intervals or `UnscheduledCardOnFile` for non-fixed intervals. Neither a redirect nor an initial API response is described as a usable-token event. See raw lines 74–111 and 362–399.
- **Testing and live gate:** The page says a real mobile number registered with a DANA account is needed to test successful **live** DANA payments, points to TEST Customer Area for test-payment status, and says to request DANA in LIVE Customer Area before accepting live payments. That mixed “test successful live” wording and TEST request examples do not prove either environment is working for a merchant. IDR and amounts in recurring examples do not independently define eligibility; consult [[source-adyen-docs-payment-methods-dana]] for its overview limits. See raw lines 113–320 and 401–608.

> [!warning] Contradiction
> The base-flow no-extra-parameters statements (raw lines 42 and 360) do **not** cover recurring: both recurring sections require extra `/payments` fields (raw lines 85–111 and 373–399). The displayed `Redirect` initialization snippets use `{ type:dana }` with an **unquoted** `dana` identifier (raw lines 71 and 353); the prose identifies DANA but does not define a JavaScript variable named `dana`. Treat those snippets as incomplete until checked against the applicable Adyen Web API. The recurring request examples also vary: Java uses IDR value 15000 while the other examples use 1000; curl/Node/Python/Ruby omit `returnUrl` while Java/PHP/C# include it (raw lines 115–309 and 403–597).

## Detail locators

- Sessions requirements, import/configuration and Component initialization: raw lines 23–72.
- Sessions recurring token creation and future payments: raw lines 74–111.
- Sessions request examples and test/live wording: raw lines 113–320.
- Advanced requirements, import/initialization and base `/payments` statement: raw lines 322–360.
- Advanced recurring route, examples and repeated test/live wording: raw lines 362–608.

## Related

- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[source-adyen-docs-payment-methods-dana]] — DANA overview for ID/IDR, redirect-page lifetime and method-display amount floor.
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/dana/web-component/2026-09-15|Adyen DANA Web Component snapshot]]
