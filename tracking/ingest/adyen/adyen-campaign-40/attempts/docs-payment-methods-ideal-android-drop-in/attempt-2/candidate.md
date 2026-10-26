---
title: "Adyen iDEAL | Wero Android Drop-in"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/ideal/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/ideal/android-drop-in/2026-09-15.md"
tags: [adyen, ideal, wero, android, drop-in, sepa-direct-debit]
---

## Overview

Adyen's 2026-09-15 iDEAL | Wero Android Drop-in page describes method-specific additions to an existing Android Drop-in integration, separately for Sessions and Advanced server-side flows. It also covers SEPA Direct Debit-based recurring payments and qualified TEST/live guidance. See [[adyen]], [[adyen-android-sdk]], and [[adyen-tokenization]].

## Key takeaways

- Sessions requires existing Android Drop-in Sessions with Checkout API v68 or later and iDEAL | Wero added in Customer Area. For the ordinary Sessions payment, the page says no additional `/sessions` parameters or method configuration are needed.
- Advanced requires existing Android Drop-in Advanced, redirect handling for `action.type: redirect`, and iDEAL | Wero added in Customer Area. For the ordinary Advanced payment, the page says no additional `/payments` parameters or method configuration are needed. These no-extra-parameter statements address the base payment flows; the separate recurring route still uses tokenization parameters and later token-payment requests.
- Recurring payments here use **SEPA Direct Debit** tokens rather than an `ideal` token. The page says to use standard SEPA tokenization parameters with no extra SEPA-specific fields; `recurring.token.created` then carries `storedPaymentMethodId`. It restricts tokenized payments to shopper-not-present `Subscription` and `UnscheduledCardOnFile` scenarios. Most later-payment examples include `paymentMethod.type: sepadirectdebit`, stored ID, shopper reference and `ContAuth`, but the Java token-payment snippets in both flows omit `shopperReference` (raw lines 108-128 and 404-424). Do not treat those Java snippets as complete token-payment templates. A `Received` response indicates the request was received, while webhooks are needed to track whether the payment succeeded.
- The iDEAL | Wero TEST environment is described as unreliable; the page recommends live penny tests. When TEST is operating, the `TESTNL2A` issuer offers simulations for success, cancellation, expiration and failure, with expiration yielding `Pending` or `Received`. Those intermediate codes are not payment-success proof. The live penny-test steps require a live issuer bank account and shopper authorization, then checking Customer Area status; the page's live-request heading has no further instruction beneath it, so this source does not specify an additional live onboarding step beyond its Customer Area setup prerequisite.
- The recurring examples are test-endpoint snippets with varying language library versions and amounts; some use an HTTPS web return URL in this Android guide. They are examples, not a complete Android app-return specification or proof of account enablement. This page does not state the separate API-only guide's dated co-branding window.

## Detail locators

- Sessions requirements, base no-extra-parameter/configuration statements: raw lines 25-46.
- Sessions SEPA recurring route, token webhook, shopper-not-present condition and examples: raw lines 48-280.
- Sessions TEST/live guidance, conditional simulations: raw lines 282-320.
- Advanced requirements, redirect, base no-extra-configuration/parameter statements: raw lines 322-342.
- Repeated Advanced recurring route and examples: raw lines 344-576.
- Repeated Advanced TEST/live guidance: raw lines 578-614.

## Raw Sources

- [[raw/adyen/docs/payment-methods/ideal/android-drop-in/2026-09-15|iDEAL | Wero Android Drop-in (2026-09-15 snapshot)]]
