---
title: "Adyen Boleto Bancário React Native Component"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/boleto-bancario/react-native-component"
raw_files:
  - "adyen/docs/payment-methods/boleto-bancario/react-native-component/2026-09-15.md"
tags: [adyen, boleto-bancario, react-native, components, voucher]
---

## Overview

This 2026-09-15-captured Adyen guide adds Boleto Bancário to an existing **Advanced React Native Components** integration. React Native Components Sessions is explicitly unavailable. The Advanced server `/payments` response provides a voucher action for presentation; Boleto is offline, so `PresentToShopper` does not mean the shopper paid. See [[adyen]], [[adyen-online-payments]], and [[source-adyen-docs-payment-methods-boleto-bancario]] for the Boleto de Proposta method overview.

## Key takeaways

- Begin with an existing Advanced React Native Components integration, voucher-action handling, and Boleto Bancário added in Customer Area. No additional Boleto Component configuration parameters are specified. The requirements-table link says Components but selects `integration=Drop-in`; nearby payment and action links select Components. The voucher action link uses a `#handle-the-redirect` fragment despite stating `action.type: voucher`; do not infer a redirect action from that anchor. See raw lines 25–53.
- The `/payments` table marks `paymentMethod.type: boletobancario`, `shopperName` first/last, `billingAddress`, and `socialSecurityNumber` (shopper CPF or CNPJ) required. `deliveryDate`, `shopperEmail`, and `shopperStatement` are unmarked optional. The due-date description specifies ISO 8601 UTC, a five-day default, and next-working-day payment if due date falls on a weekend or national holiday. The address row prints `postalCode,stateOrProvince` without a separator; consult the API schema for exact fields. See raw lines 55–63.
- If a custom `shopperStatement` is supplied, it should state that payment above/below the original amount or after the due date is not accepted. If omitted, default Portuguese instructions include processing the order only after confirmed payment with matching amount and automatic cancellation for nonpayment. These are voucher instructions, not payment-finality evidence. See raw lines 63–72.
- The documented `/payments` response has `resultCode: PresentToShopper` and `action.type: voucher`; the action contains PDF `downloadUrl`, `expiresAt`, issuing-bank `paymentMethodType`, barcode `reference`, and `totalAmount`. It is a voucher issuance/presentation stage. The separate method overview says unpaid transactions stay open 15 days after due date before **Offer cancelled**; preserve that distinction from the initial five-day default due date. See raw lines 74–86 and [[source-adyen-docs-payment-methods-boleto-bancario]].
- In test, a pending offer may be manually promoted to sale under **Payments > Offers** using its PSP reference; pending/expired offers remain under Offers and paid/test-promoted payments appear in **Payment list**. This is reconciliation simulation, not a real voucher redemption. Live acceptance requires a separate request in live Customer Area. See raw lines 88–106.

## Detail locators

- Sessions exclusion and Advanced prerequisites/link mismatches: raw lines 25–53.
- Required request fields, optional due date and instructions: raw lines 55–72.
- Advanced voucher response fields: raw lines 74–86.
- Test promotion, status routes and live request: raw lines 88–106.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-boleto-bancario]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/boleto-bancario/react-native-component/2026-09-15|Fully read Boleto Bancário React Native Component raw]]
