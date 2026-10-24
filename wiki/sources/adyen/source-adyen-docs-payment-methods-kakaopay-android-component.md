---
title: "Adyen KakaoPay Android Component guide"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/kakaopay/android-component"
raw_files:
  - "adyen/docs/payment-methods/kakaopay/android-component/2026-09-15.md"
tags: [adyen, kakaopay, android, component, recurring]
---

## Overview

This [[adyen]] guide adds **KakaoPay** to an existing **Android Components** integration, with separate Sessions and Advanced server-side flows and an additional tokenized recurring-payment route. Both flows require redirect action handling; the page does not specify an app deep-link implementation or establish current account eligibility, successful shopper return, authorization, capture or settlement. [[adyen-online-payments]] [[adyen-tokenization]]

## Key takeaways

- **Base Sessions flow:** Requires an existing Sessions Android Components integration, **Checkout API v68 or later**, `action.type: redirect` handling, and KakaoPay added in Customer Area. The guide says no additional KakaoPay-specific `/sessions` parameters or Component configuration are needed for this base route. The client imports `com.adyen.checkout:instant:YOUR_VERSION` (plus `components-compose` for Compose), obtains `kakaopay` from `checkoutSession`, and creates `InstantPaymentComponent`. A new Compose key is required for each different screen or payment session/reset in the example. See raw lines 23–125.
- **Base Advanced flow:** Requires an existing Advanced Android Components integration, additional redirect-action handling, and KakaoPay added in Customer Area. It likewise says no extra KakaoPay configuration or ordinary `/payments` parameters. Here the client selects `kakaopay` from the `/paymentMethods` response and creates `InstantPaymentComponent`. The Advanced prerequisites do not restate the Sessions table's v68+ version minimum. See raw lines 378–478.
- **Recurring is a separate qualified route:** To request token creation, the server adds `storePaymentMethod: true` and a unique `shopperReference` to **`/payments`**; the shopper logs in to Kakao and confirms the recurring transaction. **After the initial payment has settled**, the `recurring.token.created` webhook provides `storedPaymentMethodId` and related identifiers; the server must receive recurring-token lifecycle webhooks. For later token payments, the guide specifies that token ID, the same shopper reference, `shopperInteraction: ContAuth`, and `recurringProcessingModel: Subscription` for fixed intervals or `UnscheduledCardOnFile` for non-fixed intervals. This does not say that a redirect, initial API response or Kakao confirmation alone creates a usable token. See raw lines 128–167 and 480–519.
- **TEST/LIVE boundary:** The page says a real mobile number registered to a KakaoPay account is needed to test successful KakaoPay live payments, directs test-status checks to TEST Customer Area, and says to submit a KakaoPay request in LIVE Customer Area before accepting live payments. The wording mixes “test” and “live”; it is no proof of a successful test or live merchant activation. KRW values and TEST clients in the recurring snippets are examples, not a standalone country/currency rule. See raw lines 169–366, 368–376, 521–718 and 720–728.

> [!warning] Contradiction
> The base-flow statements that no additional `/sessions` or `/payments` parameters are needed (raw lines 42 and 478) cannot be extended to **recurring**: both recurring sections require extra `/payments` fields for token creation and later token use (raw lines 139–167 and 491–519). Keep the ordinary and recurring scopes separate. The snippets also differ: the curl/Node/Python/Ruby token-payment examples omit `returnUrl`, while Java/PHP/C# include it, and Java uses `KRW` value 15000 where the other examples use 1000 (raw lines 171–365 and 523–717). Do not treat any one example as a complete, universally required request.

## Detail locators

- Sessions prerequisites, redirect, library and Component examples: raw lines 23–125.
- Sessions token creation, settlement-gated webhook and future token request fields: raw lines 128–167.
- Sessions recurring language-specific request examples and test/live notes: raw lines 169–376.
- Advanced prerequisites, Component and ordinary `/payments` statement: raw lines 378–478.
- Advanced repeated recurring route, examples and test/live notes: raw lines 480–728.

## Related

- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/kakaopay/android-component/2026-09-15|Adyen KakaoPay Android Component snapshot]]
