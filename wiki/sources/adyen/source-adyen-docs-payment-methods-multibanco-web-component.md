---
title: "Adyen Multibanco Web Component"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/multibanco/web-component"
raw_files:
  - "adyen/docs/payment-methods/multibanco/web-component/2026-09-15.md"
tags: [adyen, multibanco, web, components, sessions, advanced-flow]
---

## Overview

This 2026-09-15-captured Adyen guide adds Multibanco to an existing Web Components integration. It covers Sessions and Advanced flows, `Multibanco` Web Component import/initialization, voucher action handling, and test offer promotion. Multibanco's method overview explains that a shopper receives a voucher at checkout and pays later through ATM or online banking; a voucher or pending offer is not a paid sale. See [[adyen]], [[adyen-online-payments]], and [[source-adyen-docs-payment-methods-multibanco]].

## Key takeaways

- **Sessions:** use an existing Web Components Sessions flow with **Checkout API v68 or later** and Multibanco added in Customer Area. This page says no **additional Multibanco** parameters are needed for `/sessions` and no extra Multibanco Component configuration is needed. It instructs importing `Multibanco` from `@adyen/adyen-web` and initializing/mounting the Component. Base integration request/configuration requirements still apply. See raw lines 25–75.
- **Advanced:** use an existing Web Components Advanced flow, handle the additional `action.type: voucher`, and add Multibanco in Customer Area. Import, initialize and mount `Multibanco`. This page says no additional Multibanco parameters are needed in `/payments`; that does not remove the base payment request or action handling. The v68 minimum is stated in the Sessions requirements table only. See raw lines 94–136.
- To test, first request Multibanco in the **test** Customer Area. The page describes simulating payment by selecting the pending offer's PSP reference under **Payments > Offers** and choosing **Promote offer to sale**, then checking **Payments > Payment list**. This manual promotion is a test/reconciliation action, not evidence that a shopper redeemed a real voucher. See raw lines 77–90 and 138–151.
- Live acceptance separately requires submitting a Multibanco request in the **live** Customer Area. The page does not establish current account enablement or a completed live transaction. See raw lines 92 and 153.

## Detail locators

- Sessions prerequisites, no extra request/configuration parameters, import and initialization: raw lines 25–75.
- Advanced prerequisites, voucher action, import and no extra request parameters: raw lines 94–136.
- Test pending-offer promotion and reconciliation: raw lines 77–90 and 138–151.
- Separate live Customer Area request: raw lines 92 and 153.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-multibanco]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/multibanco/web-component/2026-09-15|Fully read Multibanco Web Component raw]]
