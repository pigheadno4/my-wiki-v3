---
title: "Boleto Bancário API-only"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/boleto-bancario/api-only"
raw_files:
  - "adyen/docs/payment-methods/boleto-bancario/api-only/2026-09-15.md"
tags: [adyen, boleto-bancario, api-only, voucher, brazil]
---

## Overview

This 2026-09-15 guide adds Boleto Bancário to an existing Adyen API-only integration. The merchant builds the payment form, discovers the method, makes a `/payments` request, presents the voucher and waits for the final result by webhook. Boleto is an offline voucher method; `PresentToShopper` is not paid status. See [[adyen]], [[adyen-online-payments]], and [[source-adyen-docs-payment-methods-boleto-bancario]].

## Key takeaways

- The guide requires an existing Web API-only Advanced integration, handling a `voucher` additional action, and Boleto Bancário setup in Customer Area. The form collects first/last name, CPF or CNPJ, billing address and email. Its numbered flow says to include information about items intended for purchase, but the shown additional `/payments` field table does not define a line-item parameter. See raw lines 23–47 and 90–102.
- For `/paymentMethods` discovery, specify `countryCode: BR` and `amount.currency: BRL`. The example response shows a method entry with `type: boleto`. In the later `/payments` table, `paymentMethod.type` is required as `boletobancario`; keep these endpoint-specific values distinct rather than substituting one into the other. See raw lines 49–99.
- The `/payments` table also marks `shopperName` (first/last), `billingAddress`, and `socialSecurityNumber` (CPF/CNPJ) required. Optional `deliveryDate` is UTC ISO 8601 due date, defaulting to five days; a weekend or national-holiday due date can be paid on the next working day according to the row. `shopperEmail` and `shopperStatement` are optional; if a statement is supplied, the guide says to disallow higher/lower amounts and after-due-date payments. The default Portuguese instructions say to process the order only after confirmed matching payment and not to accept cheque, deposit, bank transfer or after-date payment. See raw lines 90–111.
- A successful voucher presentation response is described with `action.type: voucher`, `resultCode: PresentToShopper`, PDF `downloadUrl`, due-date `expiresAt`, barcode `reference`, and `totalAmount`. The merchant-built UI should offer PDF download and barcode copy. After presenting it, tell the shopper payment is pending; optional PENDING webhooks can report pending status, while an **AUTHORISATION** webhook carries the final result. Do not fulfill solely from `PresentToShopper`. See raw lines 137–195.
- In test, a pending Boleto can be manually promoted to sale in Customer Area to simulate payment and test reconciliation. Pending/expired vouchers are listed under **Offers**; paid/promoted test offers under **Payment list**. This is not real shopper payment. A separate Boleto request in the **live Customer Area** is needed for live acceptance. See raw lines 197–215.

> [!warning] Example and timing limitations
> The `/payments` curl example uses **EUR** despite BR/BRL discovery and the Boleto overview's BR/BRL matrix; it also contains placeholder `otherData`/`paramOne`/`paramTwo` fields and an inline comment, while omitting the required identity/address fields (raw lines 113–135). It is not copy-ready evidence of a valid Boleto request. The response table calls `action.paymentMethodType` an issuing bank, but its example value is `boletobancario` (lines 140, 164); do not infer a bank code from that example. The due-date row allows next-working-day payment after a weekend/holiday, while its default statement says no payment after the due date (lines 100, 108); preserve both, without promising late acceptance. This child describes `action.expiresAt` as due-date expiry (lines 146, 181), while the linked overview says unpaid transactions remain open 15 days after due date before **Offer cancelled** (overview raw line 39); do not equate due date with final cancellation.

## Detail locators

- Prerequisites and merchant form: raw lines 23–47.
- BR/BRL method discovery and endpoint-specific type values: raw lines 49–99.
- Required/optional request fields and instructions: raw lines 90–111.
- Voucher response, presentation and webhook result: raw lines 137–195.
- Test promotion and live request: raw lines 197–215.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-boleto-bancario]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/boleto-bancario/api-only/2026-09-15|Boleto Bancário API-only, captured 2026-09-15]]
