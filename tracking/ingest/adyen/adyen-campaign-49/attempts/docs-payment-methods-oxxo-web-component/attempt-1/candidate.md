---
title: "OXXO Web Component"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/oxxo/web-component"
raw_files:
  - "adyen/docs/payment-methods/oxxo/web-component/2026-09-15.md"
tags: [adyen, oxxo, web, components, voucher]
---

## Overview

This 2026-09-15 guide adds OXXO to an existing Adyen Web Components integration for Sessions or Advanced server-side flow. OXXO is an offline cash voucher method, described further in [[source-adyen-docs-payment-methods-oxxo]]. Voucher creation and presentation are separate from payment confirmation. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Sessions flow:** requires an existing Web Components Sessions integration, Checkout API v68 or later, and adding OXXO in Customer Area. The guide says no **additional OXXO-specific** `/sessions` parameters or Component configuration are needed. It imports `Oxxo` from Adyen Web and mounts `new Oxxo(checkout, ...)`. See raw lines 25–75.
- **Advanced flow:** requires an existing Web Components Advanced integration, handling an additional `action.type: voucher`, and Customer Area setup. It uses the `Oxxo` import/component and says no **additional OXXO-specific** `/payments` parameters. Its requirements table does not state the Sessions v68 minimum. The base integration still supplies common request and action handling. See raw lines 100–142.
- The voucher first appears as an **Open** offer in Customer Area. Webhooks are needed to follow its status; optional OXXO **PENDING** webhooks report pending vouchers. When the shopper pays at an OXXO store, the offer becomes a sale and status **Received**; the final payment result comes in an **AUTHORISATION** webhook. Treat Open, Received and final authorization as distinct stages. The linked overview says OXXO confirmation typically arrives within one business day but may take longer, and describes a seven-day open period after an unpaid voucher's due date before expiry; this child does not define those timing rules. See child raw lines 77–85 and 144–152; overview raw lines 23–31.
- In test, a pending offer can be manually promoted to sale to simulate OXXO payment and test reconciliation. Paid or promoted test vouchers appear in **Payment list**. This simulation is not evidence that a shopper paid cash. Before live acceptance, separately request OXXO in the **live Customer Area**. See raw lines 87–98 and 154–165.

> [!warning] Action link label
> The Advanced action-handling prerequisite states `action.type: voucher` but its base-guide URL uses a `#handle-the-redirect` anchor (raw line 107). The anchor label does not turn the OXXO action into a redirect; follow the stated voucher type and base guide's applicable action handling.

## Detail locators

- Sessions requirements, import and Component mount: raw lines 25–75.
- Advanced requirements, import, mount and request scope: raw lines 100–142.
- Offline status/webhook sequence and test/live setup: raw lines 77–98 and 144–165.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-oxxo]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/oxxo/web-component/2026-09-15|OXXO Web Component, captured 2026-09-15]]
