---
title: "Gift card Web Drop-in integration"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/gift-cards/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/gift-cards/web-drop-in/2026-09-15.md"
tags: [adyen, gift-cards, web, drop-in, partial-payments]
---

## Overview

This Adyen page, last modified 2023-03-10 and captured 2026-09-15, describes adding gift cards to an existing Web Drop-in integration. It separates /sessions automatic partial payments from an additional-use-case /payments configuration, then gives payment-result and test/live guidance. See [[adyen]], [[adyen-online-payments]], and [[source-adyen-docs-payment-methods-gift-cards]] for provider onboarding and the broader gift-card scope. This snapshot does not establish current provider availability or a live payment outcome.

## Key takeaways

- An existing Web Drop-in integration and the intended gift-card variants in Customer Area are prerequisites for testing (raw lines 26–33). If using Web Drop-in v6, the page says to import AdyenCheckout and Giftcard (lines 35–41). It says no additional gift-card request fields; /sessions is the default from Drop-in v5.0.0 onward, while /payments is for an additional use case (lines 43–48). Base request fields remain applicable.
- In the /sessions tab, Drop-in handles partial payments automatically (raw lines 50–58). This page does not specify a merchant-created order callback for that route.
- In the /payments tab, configure gift-card partial payment with onBalanceCheck to call /paymentMethods/balance, onOrderRequest when balance is short to call /orders with total amount, merchantAccount and reference, and onOrderCancel to call /orders/cancel (raw lines 60–74). The sample code in lines 80–102 is incomplete JavaScript: it places a const declaration within an object and omits separators. Follow the described event/endpoint obligations, not the sample as a ready-to-run implementation. It shows giftcardConfiguration passed under paymentMethodsConfiguration when constructing AdyenCheckout (lines 104–121).
- The result section says to use resultCode from a /payments response to inform the shopper, and separately notes asynchronous webhook outcomes. It lists Authorised, Cancelled, Error and Refused; manual capture is an additional step **only if manual capture is in use** (raw lines 123–134). Do not collapse the shopper-facing result and webhook into proof that every order has settled.
- For testing, provider-dependent test card numbers and last-three-digit amount codes drive simulator Authorised, Refused or Error examples; they are not live guarantees (raw lines 157–178). Before live payments, the page says to onboard with a gift-card provider, add the variant in live Customer Area, and contact Support to add the gift card there; only then does it mention small-amount end-to-end live tests with real details (lines 180–186). The guide itself records no executed live test.

> [!warning] Versioned route and example caveat
> /sessions auto-handling (v5.0.0+ default) and /payments custom balance/order callbacks are different routes. The /payments configuration snippet is syntactically incomplete (raw lines 80–102). Test amount suffixes are simulator behavior, and live acceptance depends on separate provider and Customer Area setup.

## Detail locators

- Existing Drop-in, test variants, v6 import and no-extra-fields/API route: raw lines 26–48.
- /sessions auto partial payments and /payments callback/endpoint table: raw lines 50–74.
- Incomplete configuration example and construction route: raw lines 76–121.
- /payments resultCode table, webhook and conditional manual capture: raw lines 123–134.
- Optional brand logo: raw lines 136–155.
- Test simulator and provider/live setup: raw lines 157–186.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-gift-cards]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/gift-cards/web-drop-in/2026-09-15|Gift card Web Drop-in, captured 2026-09-15]]
