---
title: "Adyen Boleto Bancário React Native Drop-in"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/boleto-bancario/react-native-drop-in"
raw_files:
  - "adyen/docs/payment-methods/boleto-bancario/react-native-drop-in/2026-09-15.md"
tags: [adyen, boleto-bancario, react-native, drop-in, voucher, online-payments]
---

## Overview

This 2026-09-15-captured Adyen guide adds Boleto Bancário to an existing React Native Drop-in integration. It separates Sessions and Advanced server-side flows, specifies identity/address and due-date fields, describes the Advanced voucher response, and explains test offer promotion. It is a method-specific supplement to [[adyen-online-payments]], not a completed-payment record or full base integration. [[adyen]]

## Key takeaways

- **Sessions flow:** The page calls for an existing React Native Sessions-flow Drop-in integration, Checkout API **v68 or later**, and Boleto Bancário added in Customer Area. Its `/sessions` table marks `shopperName` (first/last name), `billingAddress` (city, country, house number/name, postal code, state/province, street), and `socialSecurityNumber` (CPF or CNPJ) required. It lists optional `deliverAt` for due date, `shopperEmail` for sending a copy, and `shopperStatement` for instructions. No method-specific Drop-in configuration is required. The Sessions requirement row's base-integration link points to an **Advanced-flow** URL despite saying Sessions; use its Sessions flow text and the separate Sessions create-session link, rather than treating that URL as a flow change. [Raw: lines 25–65]
- **Advanced flow:** Start with an existing React Native Advanced-flow Drop-in integration handling `action.type: voucher` and add the method in Customer Area. Its `/payments` table marks `paymentMethod.type: boletobancario`, `shopperName`, `billingAddress`, and `socialSecurityNumber` required; it lists optional **`deliveryDate`** (distinct from Sessions `deliverAt`), `shopperEmail`, and `shopperStatement`. No additional method-specific configuration is required. This section does not state an Advanced Checkout API minimum. [Raw: lines 87–119]
- **Due date and instructions:** The two optional due-date rows call for ISO 8601 UTC and say the shopper gets five days by default; a due date on a weekend or national holiday allows payment on the next working day. If a custom `shopperStatement` is supplied, the guide says it should state no higher/lower amount and no payment after due date. If omitted, default Portuguese instructions include no cheque or post-due-date payment, processing only after confirmed matching-amount payment, automatic order cancellation for nonpayment without fine/interest, and no deposit/transfer. The blanket no-late-payment wording and the next-working-day exception coexist in the captured page; do not erase the exception or infer exact bank acceptance policy. [Raw: lines 48–59, 117–128]
- **Voucher presentation versus settlement:** The Advanced response has `action.type: voucher`, `resultCode: PresentToShopper`, `pspReference`, and voucher details: PDF `downloadUrl`, due `expiresAt`, `paymentMethodType` described as issuing bank, barcode `reference`, and `totalAmount`. `PresentToShopper` means presenting the Boleto, not that an offline payment has been made. The approved [[source-adyen-docs-payment-methods-boleto-bancario]] overview separately states that an unpaid Boleto remains open for 15 days after due date before **Offer cancelled**; this child page's default order-cancellation text does not specify that transaction-status timing. [Child raw: lines 121–146; overview raw: line 39]
- **Test/live boundary:** In test Customer Area, a pending Boleto offer can be manually promoted to a sale under **Payments > Offers** using its PSP reference; pending/expired offers remain there, while paid or promoted test offers appear in **Payment list**. The page recommends this for reconciliation testing. Live acceptance requires submitting a Boleto Bancário request in the live Customer Area. Test promotion is a simulation, not live shopper payment. [Raw: lines 67–85, 144–162]

> [!WARNING] Voucher and timing qualifications
> Do not treat `PresentToShopper` or a pending offer as paid. Preserve the page's weekend/holiday next-working-day exception alongside its no-post-due-date instruction text, and attribute the overview's 15-day open/Offer-cancelled timing to that overview rather than silently combining it with the child page's order-cancellation statement.

## Detail locators

- Sessions prerequisites, required/optional fields and default instructions: pinned raw lines 25–65.
- Advanced prerequisites, required/optional fields and voucher response: pinned raw lines 87–142.
- Test promotion, status locations and live request: pinned raw lines 67–85 and 144–162.

## Related

- [[adyen-online-payments]] — provider integration and method routes.
- [[source-adyen-docs-payment-methods-boleto-bancario]] — approved overview for Boleto de Proposta, BR/BRL capability context and unpaid post-due-date transaction timing.

## Raw Sources

- [[raw/adyen/docs/payment-methods/boleto-bancario/react-native-drop-in/2026-09-15|Boleto Bancário React Native Drop-in guide, captured 2026-09-15]]
