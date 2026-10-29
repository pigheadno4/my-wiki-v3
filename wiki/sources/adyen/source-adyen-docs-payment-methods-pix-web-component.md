---
title: "Pix Web Component integration"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/pix/web-component"
raw_files:
  - "adyen/docs/payment-methods/pix/web-component/2026-09-15.md"
tags: [adyen, pix, web, components, qr-code, brazil]
---

## Overview

This 2026-09-15-captured Adyen guide adds **Pix to an existing Web Components integration** through Sessions or Advanced server-side flow. It covers BRL purchase fields, the `Pix` Component and QR-code action, display/expiry timing, refunds, and asynchronous test/live status. A generated QR code or `Pending` result is not confirmation that the shopper transferred funds. See [[adyen]], [[adyen-online-payments]] and the [[source-adyen-docs-payment-methods-pix|Pix method overview]] for Brazil local-entity and transaction conditions.

## Key takeaways

- **Sessions:** requires an existing Web Components Sessions integration, Checkout API **v68 or later**, and Pix in Customer Area. The method-specific `/sessions` table marks final `amount` required; shopper name, CPF/CNPJ `socialSecurityNumber`, `shopperStatement` (maximum **140 characters**) and line-item ID/amount fields have blank required cells. The captured examples use **BR/BRL** and an old `sessionValidity` timestamp; do not copy that expired timestamp as a current expiry setting or infer that example-only `paymentMethod` is required by this table (raw lines 25–91, 94–505).
- **Sessions UI:** import `Pix` from `@adyen/adyen-web`, configure `countdownTime` as the number of minutes after the QR code loads for shopper payment (**15** by default), and optionally set `personalDetailsRequired: true` to require personal details (**false** by default). Initialize with the `Pix` class. The countdown is a Component display/payment timer and should not be conflated with the Advanced `sessionValidity` payment-expiry default (raw lines 507–553, 625).
- **Advanced:** requires an existing Web Components Advanced integration configured for `action.type: qrCode`, plus Pix in Customer Area. Import/initialize `Pix`. The `/payments` table marks `paymentMethod` from front-end `state.data.paymentMethod` and final `amount` required. Shopper name and CPF/CNPJ are optional but **advised together** to help the shopper identify the payment; `shopperStatement` is optional and, if provided, must be **under 60 characters** in this flow, unlike the Sessions table's 140-character maximum. The optional `sessionValidity` payment-expiry default is **1 hour on Checkout API v71 or earlier** or **24 hours on v72 or later**. Example v72 requests use an old 2025 validity date; the response example is `Pending` with a `qrCode` action and QR data, not paid status (raw lines 574–629, 631–671, 1117–1137).
- **Refund and outcome boundary:** the guide says a payment can be refunded **within 90 days** in Customer Area or via API. Pix is asynchronous. In test Customer Area, a pending offer can be manually promoted to a sale for reconciliation testing; paid/promoted test offers appear under **Payments > Payment list**. A request to add Pix in **live Customer Area** is required before accepting live payments. Test promotion is a simulation, not a real Pix transfer or proof of merchant enablement (raw lines 555–572, 1139–1156).
- The separate [[source-adyen-docs-payment-methods-pix|overview]] describes Pix as BR/BRL QR-based direct bank transfer and states that the merchant needs a **local entity in Brazil** to accept it. It also lists transaction checks/rejection conditions and a dispute mechanism. Those method-level conditions are not waived by the child guide's Customer Area setup or request examples (overview pinned raw lines 23–67).

## Detail locators

- Sessions prerequisites, required amount and optional shopper/statement/line-item fields: raw lines 25–50; examples lines 52–505.
- Pix import, countdown/personal-details configuration and initialization: raw lines 507–553.
- Sessions refunds, asynchronous test offer promotion and live request: raw lines 555–572.
- Advanced prerequisites, QR action and required request fields: raw lines 574–629.
- Advanced examples and Pending/qrCode response: raw lines 631–1137.
- Advanced refunds, test reconciliation and live gate: raw lines 1139–1156.
- Method-level Brazil local entity, BR/BRL, transaction checks and dispute route: [[source-adyen-docs-payment-methods-pix]] and its pinned raw lines 23–67; this entry's raw_files remains child-only.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-pix]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/pix/web-component/2026-09-15|Pix Web Component guide, captured 2026-09-15]]
