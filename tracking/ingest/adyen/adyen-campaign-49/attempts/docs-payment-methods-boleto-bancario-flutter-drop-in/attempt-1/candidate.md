---
title: "Boleto Bancário Flutter Drop-in"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/boleto-bancario/flutter-drop-in"
raw_files:
  - "adyen/docs/payment-methods/boleto-bancario/flutter-drop-in/2026-09-15.md"
tags: [adyen, boleto-bancario, flutter, drop-in, voucher]
---

## Overview

This 2026-09-15 guide describes Boleto Bancário-specific additions to an existing Flutter Drop-in integration, split between Sessions and Advanced server-side flows. Boleto is an offline voucher method; voucher presentation is not paid status. See [[adyen]], [[adyen-online-payments]], and [[source-adyen-docs-payment-methods-boleto-bancario]] for the method overview.

## Key takeaways

- **Sessions flow:** requires an existing Flutter Drop-in Sessions integration, Checkout API v68 or later, and contacting Support to add Boleto Bancário in Customer Area. Its `/sessions` table requires shopper first/last name, billing address, and CPF or CNPJ as `socialSecurityNumber`. Optional `deliverAt` is the due date in UTC ISO 8601; the page says the default is five days and a weekend or national-holiday due date can be paid on the next working day. `shopperEmail` and `shopperStatement` are optional. No extra method configuration is needed. See raw lines 25–65.
- **Advanced flow:** requires an existing Flutter Drop-in Advanced integration, `voucher` additional-action handling, and Boleto Bancário in Customer Area. Its `/payments` table requires `paymentMethod.type = boletobancario`, shopper first/last name, billing address, and CPF/CNPJ; optional due date is called `deliveryDate` here, with the same five-day and next-working-day description. Email and statement are optional; no additional method configuration is stated. The Advanced requirements table does not state the Sessions v68 minimum. See raw lines 87–119.
- If `shopperStatement` is supplied, the guide says it should instruct that higher/lower amounts and payments after due date are not accepted. When omitted, default Portuguese instructions cover no cheque or after-date payment, processing only after confirmed matching payment, no penalty/interest for nonpayment, automatic order cancellation, and no deposit or bank transfer. These are the guide's displayed statement instructions, not proof that a pending voucher is paid. See raw lines 50–59 and 119–128.
- The Advanced response is described as `resultCode: PresentToShopper` with `action.type: voucher`; the action carries a PDF `downloadUrl`, `expiresAt` described as the due-date expiry, issuing-bank `paymentMethodType`, barcode `reference`, and `totalAmount`. Present the voucher and wait for actual payment confirmation before treating the order as paid. See raw lines 130–142.
- Testing is offline: in the test Customer Area, a pending offer can be manually promoted to sale to simulate payment and exercise reconciliation. Pending/expired Boletos are listed under **Offers** and paid/promoted test Boletos under **Payment list**. This test promotion is not a real shopper payment. Live acceptance requires a separate Boleto request in the **live Customer Area**. See raw lines 67–85 and 144–162.

> [!warning] Timing and navigation qualifications
> The Sessions requirement text says Sessions Flutter Drop-in but links to an `advanced-flow` URL (raw line 33); its `/sessions` step at line 41 points to the Sessions flow. The Advanced voucher-action link uses a redirect-named anchor (line 96), which does not change the stated `voucher` action type. The optional due-date names differ by endpoint: `deliverAt` for `/sessions` (line 48), `deliveryDate` for `/payments` (line 117). The next-working-day exception in these rows sits beside default statement wording against payment after due date (lines 56, 125); preserve both rather than promising late acceptance. This child calls `action.expiresAt` due-date expiry (line 139), while the linked method overview says an unpaid transaction remains open 15 days after the due date before **Offer cancelled** (overview raw line 39). Do not equate the displayed due date with final transaction cancellation.

## Detail locators

- Sessions prerequisites and request table: raw lines 25–65.
- Advanced prerequisites and request table: raw lines 87–119.
- Default Portuguese statement and voucher response: raw lines 50–59 and 121–142.
- Test promotion and live enablement: raw lines 67–85 and 144–162.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-boleto-bancario]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/boleto-bancario/flutter-drop-in/2026-09-15|Boleto Bancário Flutter Drop-in, captured 2026-09-15]]
