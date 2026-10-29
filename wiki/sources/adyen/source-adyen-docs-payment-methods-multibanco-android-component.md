---
title: "Multibanco Android Component"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/multibanco/android-component"
raw_files:
  - "adyen/docs/payment-methods/multibanco/android-component/2026-09-15.md"
tags: [adyen, multibanco, android, components, payments]
---

## Overview

This 2026-09-15 guide adds Multibanco to an existing Adyen Android Components integration. It gives separate Sessions and Advanced flow additions, including an `InstantPaymentComponent` UI and test offer promotion. It is a method add-on; use the linked base integration for common request and action handling. See [[adyen]], [[adyen-online-payments]], and the [[source-adyen-docs-payment-methods-multibanco|Multibanco overview]] for voucher context.

## Key takeaways

- **Sessions flow:** requires an existing Android Components Sessions integration, Checkout API v68 or later, and Multibanco added in Customer Area. The guide says no **additional Multibanco-specific** parameters are needed in `/sessions`; it does not dispense with the base request. See raw lines 25–41.
- Import the `instant` module (and `components-compose` when using Jetpack Compose) and use `InstantPaymentComponent` with `PaymentMethodTypes.MULTIBANCO`. It says no extra method configuration is needed. Compose examples require a unique Component key per screen or payment session; view-based mounting is also shown. See raw lines 43–125 and 154–238.
- **Advanced flow:** requires an existing Android Components Advanced integration, handling the additional `action.type: voucher`, and Customer Area setup. The guide says no **additional Multibanco-specific** parameters are needed in `/payments`; the base payment request still applies. The Advanced requirements do not state the Sessions table's v68 minimum. See raw lines 144–152 and 240–244.
- For testing, request Multibanco in the **test Customer Area** first. The page describes a manual test simulation: promote a pending offer to a sale under **Payments → Offers**, then see paid/promoted test offers under **Payment list** and use this to test reconciliation. This is test simulation, not evidence of shopper voucher redemption or live settlement. For live acceptance, separately request Multibanco in the **live Customer Area**. See raw lines 127–142 and 246–261.

## Detail locators

- Sessions prerequisites and request scope: raw lines 25–41.
- Component imports, no extra configuration, Compose/view mounting: raw lines 43–125 and 154–238.
- Advanced voucher action and request scope: raw lines 144–152 and 240–244.
- Test offer promotion, reconciliation and live request: raw lines 127–142 and 246–261.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-multibanco]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/multibanco/android-component/2026-09-15|Multibanco Android Component, captured 2026-09-15]]
