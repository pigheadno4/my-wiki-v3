---
title: "Adyen Boleto Bancário Web Drop-in"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/boleto-bancario/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/boleto-bancario/web-drop-in/2026-09-15.md"
tags: [adyen, boleto-bancario, brazil, web, drop-in, voucher]
---

## Overview

This 2026-09-15-captured Adyen guide adds Boleto Bancário to an existing Web Drop-in integration for Sessions or Advanced flow. It covers shopper identity/address fields, voucher due date/instructions, Advanced `voucher` action, and test offer promotion. Boleto is an **offline voucher**: presenting it to the shopper is not payment completion. See [[adyen]], [[adyen-online-payments]], and [[source-adyen-docs-payment-methods-boleto-bancario]] for the separate Boleto de Proposta method overview.

## Key takeaways

- **Sessions:** use an existing Web Drop-in Sessions flow with **Checkout API v68 or later** and Boleto Bancário added in Customer Area. The `/sessions` table marks `shopperName` (first/last), `billingAddress`, and `socialSecurityNumber` (shopper CPF or CNPJ) required. `deliverAt` is an unmarked optional due-date field; `shopperEmail` and `shopperStatement` are also unmarked. The due-date description says ISO 8601 UTC, default five days, with payment possible the next working day if the due date is a weekend or national holiday. See raw lines 25–50.
- **Advanced:** use an existing Web Drop-in Advanced flow, add Boleto in Customer Area and handle `action.type: voucher`. The `/payments` table additionally marks `paymentMethod.type: boletobancario` required, with the same shopper name/address/CPF-or-CNPJ fields. Its optional due-date field is named **`deliveryDate`**, not `deliverAt`; retain the flow-specific names rather than silently merging them. Optional `shopperEmail` is for sending a copy of the form. See raw lines 95–133.
- If you supply `shopperStatement`, the page says to state that payments above/below the original amount or after the due date are not accepted. If left empty, the page supplies Portuguese default instructions including payment confirmation before processing an order, no cheque/deposit/transfer, and automatic order cancellation for nonpayment. These are voucher instructions, not a guarantee that an issued voucher was paid. See raw lines 50–59 and 133–142.
- The Advanced response includes `resultCode: PresentToShopper`, `action.type: voucher`, and voucher details: PDF `downloadUrl`, `expiresAt`, issuing-bank `paymentMethodType`, barcode `reference`, and `totalAmount`. Presenting this response is an issuance step, not paid/final status. The method overview separately states that an unpaid transaction remains open 15 days after its due date before **Offer cancelled**; keep the due date distinct from the later cancellation status. See raw lines 144–156 and [[source-adyen-docs-payment-methods-boleto-bancario]].
- Both flows offer optional individual `Boleto` import for tree shaking. In test, a pending offer can be manually promoted to sale by PSP reference under **Payments > Offers**; pending/expired offers remain there, while paid or test-promoted entries appear in **Payments > Payment list**. This is reconciliation simulation, not real voucher payment. Live acceptance requires a separate request in live Customer Area. See raw lines 61–93 and 107–117, 158–178.
- **Link caveats:** the Advanced base-integration URL contains an encoded template placeholder for `platform`; its voucher action requirement links to a `handle-the-redirect` fragment. Verify the actual Web Drop-in Advanced base/voucher handling path. The table writes `postalCode,stateOrProvince` without separating punctuation; use API field definitions for exact address schema. See raw lines 103–104, 46 and 129.

## Detail locators

- Sessions prerequisites and request table: raw lines 25–50.
- Portuguese default statement and optional import: raw lines 52–71.
- Advanced prerequisites and request table: raw lines 95–133.
- Advanced `PresentToShopper` voucher response fields: raw lines 144–156.
- Test promotion/status and live request: raw lines 73–93 and 158–178.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-boleto-bancario]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/boleto-bancario/web-drop-in/2026-09-15|Fully read Boleto Bancário Web Drop-in raw]]
