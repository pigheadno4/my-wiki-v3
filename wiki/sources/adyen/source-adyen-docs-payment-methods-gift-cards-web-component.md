---
title: "Gift card Web Component"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/gift-cards/web-component"
raw_files:
  - "adyen/docs/payment-methods/gift-cards/web-component/2026-09-15.md"
tags: [adyen, gift-cards, web, components, partial-payments]
---

## Overview

This 2026-09-15-captured Adyen guide adds gift-card payments to an existing Web Components integration. It separates Sessions, Sessions with a merchant-owned Pay button, and /payments paths, each with different balance and partial-order behavior. See [[adyen]], [[adyen-online-payments]], and [[source-adyen-docs-payment-methods-gift-cards]] for provider onboarding and broader gift-card scope. Sample outcomes do not prove current account enablement or real payment success.

## Key takeaways

- The guide assumes existing Web Components and says to add each gift-card variant intended for testing in Customer Area. It says no additional gift-card request fields; /sessions is the default for Components v5.0.0 or later, while /payments is offered for an additional use case (raw lines 28–40). Base endpoint fields still apply.
- **Sessions Component:** this tab says Components v5.18.0+. Configure onOrderCreated(orderStatus) for a gift card whose balance is below the transaction amount; orderStatus.remainingAmount gives the remainder, and the existing AdyenCheckout instance can create another method's Component for it (raw lines 56–70). iDEAL and card are examples (lines 72–105). Construction differs for v6.0.0+ (new Giftcard) versus v5.x.x or earlier (checkout.create); mount only after availability is checked (lines 107–140).
- **Sessions with own Pay button:** this tab says Components v5.21.0+. The button must call balanceCheck(); if balance covers the full amount, onRequiringConfirmation calls for shopper confirmation before submit() makes payment. A short balance invokes onOrderCreated for the remainder (raw lines 142–162). The sample uses window.giftcard without showing a global assignment and has incomplete object syntax; do not copy it as a full runnable recipe (lines 164–181). A later mount example explicitly calls isAvailable() (lines 224–242).
- **/payments Component:** this tab applies if /payments was implemented or Components were integrated before v5.18.0. Configure onBalanceCheck to call /paymentMethods/balance. If balance is short, no payment has yet been made: onOrderRequest creates a full-amount /orders order and onOrderCancel calls /orders/cancel; subsequent partial /payments calls take place outside the Component using pspReference, orderData and remainingAmount (raw lines 244–265, 326–354). The onOrderRequest table label has stray []() markup, and the JS event example omits separators; use the prose and endpoint route rather than treating the snippet as copy-ready (lines 260–287).
- Test card numbers and amount-last-three-digit outcomes are provider-dependent simulator examples, not production guarantees (raw lines 377–398). Before live payments, the page says to onboard with a provider, add its variant in live Customer Area and contact Support to add the gift card there; it suggests real-detail, small-amount end-to-end live tests afterward (lines 400–406). This snapshot does not establish a current provider agreement or authorize live operations.

> [!warning] Version and example scope
> Keep Sessions onOrderCreated remainder handling separate from the explicit /payments balance/order/partial-payment path. The own-button and /payments JavaScript snippets are incomplete, and the first Sessions mount snippet calls .then() on the Component while later snippets show isAvailable() (raw lines 128–140, 164–181, 224–242, 267–287, 311–324). Verify the SDK version and base integration before using a sample.

## Detail locators

- Requirements and API-reference scope: raw lines 28–40.
- Sessions v5.18+ partial-order callback, versioned construction and mount: raw lines 56–140.
- Own-button v5.21+ balance check and confirmation: raw lines 142–242.
- /payments balance/order/cancel callbacks and external partial payments: raw lines 244–354.
- Optional custom logo: raw lines 356–375.
- Provider-dependent simulator and live onboarding steps: raw lines 377–406.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-gift-cards]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/gift-cards/web-component/2026-09-15|Gift card Web Component, captured 2026-09-15]]
