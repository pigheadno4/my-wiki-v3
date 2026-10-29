---
title: "Boleto Bancário iOS Component integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/boleto-bancario/ios-component"
raw_files:
  - "adyen/docs/payment-methods/boleto-bancario/ios-component/2026-09-15.md"
tags: [adyen, boleto-bancario, ios, components, voucher, brazil]
---

## Overview

This 2026-09-15-captured Adyen guide adds **Boleto Bancário to an existing iOS Components integration**. It separates Sessions and Advanced server-side flows, required shopper details, `BoletoComponent` initialization, voucher action/response, and test/live setup. Boleto is an offline voucher method: issuing or presenting a voucher is not confirmation that the shopper paid it. See [[adyen]], [[adyen-online-payments]] and the [[source-adyen-docs-payment-methods-boleto-bancario|method overview]].

## Key takeaways

- **Sessions prerequisites:** existing iOS Components Sessions flow, Checkout API **v68 or later**, and Boleto Bancário added in Customer Area. The `/sessions` table marks `shopperName` (first/last), `billingAddress`, and `socialSecurityNumber` (CPF or CNPJ) required. It lists `deliverAt` as an optional UTC ISO 8601 due date, with five days by default and next-working-day payment if the specified date falls on a weekend or national holiday; `shopperEmail` and `shopperStatement` are optional (raw lines 25–50). The table's `postalCode,stateOrProvince` formatting is compressed; use the linked API schema rather than treating it as one field.
- **Advanced prerequisites:** existing iOS Components Advanced flow, `action.type: voucher` handling, and Customer Area setup. Its integration-type link points to an **iOS Drop-in Advanced URL**, although the action/payment links use Components; follow the flow heading and matching Components base guide. The `/payments` table adds required `paymentMethod.type = boletobancario`, `shopperName`, `billingAddress`, and `socialSecurityNumber`. It calls the optional UTC due-date field **`deliveryDate`**, rather than Sessions' `deliverAt`; `shopperEmail` and `shopperStatement` remain optional (raw lines 112–123, 154–168).
- If supplied, `shopperStatement` should say payments of higher/lower amounts or after the due date are not accepted. If omitted, the page supplies Portuguese default instructions that say the order is processed **only after payment confirmation** and no amount discrepancy; nonpayment cancels the order. Preserve the page's next-working-day due-date qualification alongside the default statement's generic no-after-due-date wording, rather than promising acceptance of late payments (raw lines 48–59, 166–177).
- Both flows say no extra Boleto-specific Component configuration is needed and initialize `BoletoComponent` after checking for `BoletoPaymentMethod`. Sessions delegates to the session; Advanced delegates to the merchant integration. The snippets illustrate UI initialization, not a full base integration (raw lines 61–90, 124–152).
- In Advanced, the response has `resultCode: PresentToShopper`, `action.type: voucher`, `pspReference`, and voucher action fields including PDF `downloadUrl`, `expiresAt`, bank-indicating `paymentMethodType`, barcode `reference`, and `totalAmount`. **PresentToShopper is voucher presentation, not paid status** (raw lines 179–191). Test Customer Area can simulate payment by promoting a pending offer to sale; pending/expired Boletos remain under Offers and paid/promoted ones appear in Payment list. A live Customer Area request is required before live acceptance (raw lines 92–110, 193–211).
- The separate [[source-adyen-docs-payment-methods-boleto-bancario|method overview]] calls this **Boleto de Proposta**, explains BR/BRL voucher payment routes, and says an unpaid Boleto remains open in Customer Area for **15 days after its due date** before `Offer cancelled`. Keep that later status transition separate from the child guide's default five-day payment due date (overview pinned raw lines 23–43).

## Detail locators

- Sessions prerequisites, identity fields, due-date and statement rules: raw lines 25–59.
- Sessions no-extra-configuration, Component initialization, test/live simulation: raw lines 61–110.
- Advanced prerequisites and mismatched Drop-in integration link: raw lines 112–123.
- Advanced Component initialization and request fields: raw lines 124–177.
- Advanced `PresentToShopper` voucher response: raw lines 179–191.
- Advanced test/live simulation: raw lines 193–211.
- Method-level Boleto de Proposta, BR/BRL and due-date-to-`Offer cancelled` timing: [[source-adyen-docs-payment-methods-boleto-bancario]] and its pinned raw lines 23–43; this entry's raw_files remains child-only.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-boleto-bancario]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/boleto-bancario/ios-component/2026-09-15|Boleto Bancário iOS Component guide, captured 2026-09-15]]
