---
title: "Boleto Bancário Web Component"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/boleto-bancario/web-component"
raw_files:
  - "adyen/docs/payment-methods/boleto-bancario/web-component/2026-09-15.md"
tags: [adyen, boleto-bancario, brazil, voucher, web-component]
---

## Overview

This 2026-09-15-captured Adyen guide adds **Boleto Bancário to an existing Web Components integration**. It distinguishes Sessions and Advanced server-side flows, their request fields, voucher presentation, and test payment reconciliation. The `Boleto` Component is initialized for the shopper UI; the documented Advanced `/payments` response returns a voucher action and `PresentToShopper` for presentation. Voucher issuance or that response is not proof that the shopper paid. See [[adyen]], [[adyen-online-payments]], and the method overview [[source-adyen-docs-payment-methods-boleto-bancario]] for method-level lifecycle and capability context.

## Key takeaways

- **Sessions flow** requires an existing Web Components Sessions integration, Checkout API **v68 or later**, and Boleto added in Customer Area (raw lines 25–35). The `/sessions` additions list shopper name, billing address, and CPF/CNPJ `socialSecurityNumber` as required. Its optional `deliverAt` sets a UTC ISO 8601 due date; the page says the default is five days and a weekend or national holiday moves payment to the next working day (raw lines 39–50).
- **Advanced flow** requires an existing Web Components Advanced integration, Customer Area setup, and action handling for `action.type: voucher` (raw lines 151–159). The action-handling link at raw line 158 has a `#handle-the-redirect` fragment despite naming a voucher action; preserve voucher handling and do not infer redirect behavior from that anchor. Its `/payments` additions list `paymentMethod.type: boletobancario`, name, billing address, and CPF/CNPJ as required. Its optional due-date field is **`deliveryDate`**, distinct from Sessions `deliverAt` (raw lines 191–203).
- Both flows import and initialize the `Boleto` Component. Sessions optionally configures collection or prefilling of personal details, billing address, and email (raw lines 63–89, 115–129, 163–186). The displayed configuration object at raw lines 95–113 appears to have incomplete JavaScript object syntax; consult the pinned raw and API/SDK references before using it as executable code.
- For Advanced, the response has voucher action information and `resultCode: PresentToShopper`, including PDF `downloadUrl`, `expiresAt`, barcode `reference`, and amount (raw lines 214–226). This describes voucher presentation, not final paid status.
- Boleto is offline. In **test**, a pending offer can be promoted to a sale in test Customer Area; pending or expired Boletos appear under **Offers**, while paid ones appear under **Payment list**. The guide calls for reconciliation testing. Accepting live Boleto requires a request in live Customer Area (raw lines 131–149, 228–246). A manual test promotion does not prove a live payment.
- If a custom `shopperStatement` is supplied, the page instructs that it say higher or lower payments and payments after the due date are not accepted. Its default Portuguese text also conditions order processing on confirmed payment with no amount difference (raw lines 50–59 and 203–212). Keep due-date and amount rules separate from voucher creation.

## Detail locators

- Sessions prerequisites and `/sessions` fields: raw `## Sessions flow Component`, lines 25–50.
- Sessions optional form configuration and initialization: raw lines 63–129.
- Test simulation, status locations, reconciliation, live request: raw `## Test and go live`, lines 131–149 and 228–246.
- Advanced prerequisites, voucher action handling, and `/payments` fields: raw `## Advanced flow Component`, lines 151–203.
- Advanced voucher result payload: raw lines 214–226.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-boleto-bancario]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/boleto-bancario/web-component/2026-09-15|Boleto Bancário Web Component, captured 2026-09-15]]
