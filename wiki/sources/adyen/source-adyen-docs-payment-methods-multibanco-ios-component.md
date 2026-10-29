---
title: "Multibanco iOS Component"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/multibanco/ios-component"
raw_files:
  - "adyen/docs/payment-methods/multibanco/ios-component/2026-09-15.md"
tags: [adyen, multibanco, ios, components, payments]
---

## Overview

This 2026-09-15 guide gives Multibanco-specific additions to an existing Adyen iOS Components integration for Sessions or Advanced server-side flow. It initializes `InstantPaymentComponent` and describes test offer promotion. See [[adyen]], [[adyen-online-payments]], and the [[source-adyen-docs-payment-methods-multibanco|Multibanco overview]] for the voucher payment context.

## Key takeaways

- **Sessions flow:** requires an existing iOS Components Sessions integration, Checkout API v68 or later, and Multibanco added in Customer Area. The guide says no **additional method-specific** parameters are needed for `/sessions` and no additional Component configuration is needed; the base integration still applies. Its example selects `.other("multibanco")`, initializes `InstantPaymentComponent`, sets the session as delegate, and calls `initiatePayment()`. See raw lines 25–69.
- **Advanced flow:** requires an existing iOS Components Advanced integration, handling an additional `action.type: voucher`, and Customer Area setup. It likewise says no extra method configuration or `/payments` parameters. Its Component example sets the merchant's own object as delegate before `initiatePayment()`. The Advanced requirements table does not state the Sessions table's v68 minimum. See raw lines 88–131.
- Before testing, submit a Multibanco request in the **test Customer Area**. The test instructions simulate payment by promoting a pending offer to sale under **Payments → Offers**, then checking paid/promoted test offers under **Payment list** for reconciliation. This manual promotion is a test simulation, not evidence of real voucher redemption or live settlement. A separate request in the **live Customer Area** is needed before accepting live Multibanco payments. See raw lines 71–86 and 133–148.

> [!warning] Advanced base-guide link
> At raw line 96, the requirement text says **Advanced flow iOS Components integration**, but its URL has `integration=Drop-in`. The action-handling link at line 97 uses `integration=Components` with a `#handle-the-redirect` anchor even though the stated action type is `voucher`. Follow the iOS Components base integration route with care; these link labels alone do not establish voucher handling behavior.

## Detail locators

- Sessions prerequisites, request scope and Component initialization: raw lines 25–69.
- Advanced prerequisites, voucher action, initialization and request scope: raw lines 88–131.
- Test offer-to-sale simulation, reconciliation and live request: raw lines 71–86 and 133–148.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-multibanco]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/multibanco/ios-component/2026-09-15|Multibanco iOS Component, captured 2026-09-15]]
