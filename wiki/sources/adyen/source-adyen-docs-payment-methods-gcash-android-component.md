---
title: "GCash Android Component"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/gcash/android-component"
raw_files:
  - "adyen/docs/payment-methods/gcash/android-component/2026-09-15.md"
tags: [adyen, gcash, android, components, wallets]
---

## Overview

Adyen's 2026-09-15 GCash Android Component page adds GCash to an existing Android Components integration, covering both Sessions and Advanced server-side flows. It gives method-specific additions, while the linked base integration guides supply the underlying payment, redirect/action, and outcome handling. This is historical documentation, not evidence of current merchant eligibility or a completed payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Sessions:** Existing Android Components Sessions flow, Checkout API v68 or later, redirect handling for `action.type: redirect`, and GCash added in Customer Area are prerequisites. The page says no extra GCash-specific `/sessions` parameters or Component configuration are needed; use the `instant` module and `InstantPaymentComponent`. Compose additionally imports `components-compose`. [Raw lines 25–77]
- **Advanced:** Existing Android Components Advanced flow, handling the redirect additional action, and GCash in Customer Area are prerequisites. The page says no extra GCash-specific Component configuration or `/payments` parameters for an ordinary payment; it uses `InstantPaymentComponent` with the GCash method from `/paymentMethods`. [Raw lines 376–476]
- **Recurring:** The page separately supports a shopper-token route: request storage with `storePaymentMethod: true` and a `shopperReference` of at least three characters; after the initial payment settles, a `recurring.token.created` webhook supplies `storedPaymentMethodId`. Future `/payments` use that ID, the same shopper reference, `shopperInteraction: ContAuth`, and `recurringProcessingModel: Subscription` or `UnscheduledCardOnFile` according to interval. The merchant server must receive the recurring-token lifecycle webhook. Do not treat an initial request or redirect as token creation or settlement. [Raw lines 128–165, 478–515]
- **Testing/live:** The page points to Customer Area payment-list checks for test payments, says successful GCash live payments require a real mobile number registered with a GCash account, and requires a GCash request in the live Customer Area before acceptance. Its phrase “test successful GCash live payments” mixes test and live terms; keep the environment wording qualified rather than infer a TEST simulator or live availability from it. [Raw lines 366–374, 716–724]

## Detail locators

- Sessions Compose/non-Compose module and launch examples: raw lines 44–126; Advanced equivalents: lines 386–470. The `YOUR_VERSION` module placeholder is not a specified minimum Android SDK release; the explicit version gate on this page is Checkout API v68+ for Sessions.
- Recurring `/payments` sample payloads use `paymentMethod.type: gcash` and PHP amounts, with TEST endpoints or clients in examples: raw lines 167–364 and 517–714. These are examples, not proof of execution or a universal country/currency eligibility matrix.
- Redirect/action implementation and final payment-state handling are delegated to linked base integration guides; this page provides no result-code or webhook success guarantee.

## Related

- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/gcash/android-component/2026-09-15|GCash Android Component (2026-09-15)]]
