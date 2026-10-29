---
title: "Boleto Bancário Android Drop-in integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/boleto-bancario/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/boleto-bancario/android-drop-in/2026-09-15.md"
tags: [adyen, boleto-bancario, android, drop-in, voucher, brazil]
---

## Overview

This 2026-09-15-captured Adyen guide adds **Boleto Bancário** to an existing **Android Drop-in** integration, separately for Sessions and Advanced server-side flows. It gives Boleto-specific request fields, optional UI settings, a voucher action for Advanced, and test/live setup. It is an add-on to [[adyen-online-payments]], not a full base integration or proof of a paid voucher or enabled live merchant. The separate [[source-adyen-docs-payment-methods-boleto-bancario|method overview]] describes the Brazilian Boleto de Proposta and later shopper payment paths; this child page does not make voucher presentation final payment. See [[adyen]].

## Key takeaways

- **Sessions prerequisites and fields:** Use an existing Android Drop-in Sessions flow with Checkout API **v68 or later**, and add Boleto Bancário in Customer Area. The /sessions table marks shopperName (first and last name), billingAddress, and socialSecurityNumber (CPF or CNPJ) required. It lists **deliverAt** as optional for the UTC ISO 8601 due date, with a five-day default and next-working-day payment when that date falls on a weekend or national holiday; shopperEmail and shopperStatement are also optional. The billingAddress row names city, country, houseNumberOrName, postalCode, stateOrProvince and street, with a formatting flaw between postalCode and stateOrProvince in the raw. [Raw: lines 25–49]
- **Advanced prerequisites and fields:** Use an existing Android Drop-in Advanced flow, handle **action.type: voucher**, and add Boleto Bancário in Customer Area. Its /payments table marks paymentMethod.type **boletobancario**, shopperName, billingAddress and socialSecurityNumber required. It calls the optional UTC due-date field **deliveryDate**, rather than Sessions **deliverAt**; shopperEmail and shopperStatement remain optional. Do not substitute one flow's field name for the other. [Raw: lines 106–154]
- **Voucher presentation and payment finality:** The Advanced response lists resultCode **PresentToShopper** and a voucher action with a downloadable PDF URL, expiresAt, issuing-bank paymentMethodType, barcode reference, and totalAmount, alongside pspReference. PresentToShopper and voucher issuance are not confirmation of offline payment. The default Portuguese shopperStatement says an order is processed only after confirmed Boleto payment with no paid-amount mismatch; an included custom statement must say payments above or below the original amount or after the due date are not accepted. [Raw: lines 49–58, 154–177]
- **UI and test/live setup:** Both flows list optional setSubmitButtonVisible (default true) and setEmailVisibility (default false) settings. In the **test** Customer Area, a pending Boleto offer can be promoted manually to a sale to simulate payment and test reconciliation; pending/expired Boletos appear under Payments > Offers, while paid/promoted tests appear under Payment list. Live acceptance requires a separate Boleto Bancário request in the **live** Customer Area. Test promotion is not evidence of a real shopper's payment. [Raw: lines 60–104, 116–138, 179–197]

> [!warning] Due date and offer status are distinct
> This child guide labels the optional due-date request fields deliverAt for Sessions and deliveryDate for Advanced, gives a five-day default with a next-working-day weekend/holiday qualification, and calls the Advanced action's expiresAt the time when the due date expires (raw lines 47, 152, 165–177). Its default payment text warns against late or mismatched payments and processing before confirmation (raw lines 49–58, 154–163). The [[source-adyen-docs-payment-methods-boleto-bancario|approved method overview]] says an unpaid transaction remains open in Customer Area for 15 days after the due date before the Boleto expires and status becomes Offer cancelled (overview raw line 39). Preserve these separate statements; an open offer is not proof late payment will be accepted, and the request due date is not evidence of paid status.

## Detail locators

- Add-on scope, Sessions v68+ prerequisite and required/optional /sessions fields: pinned raw lines 15–49.
- Sessions default Portuguese shopperStatement, Android settings and test/live offer simulation: pinned raw lines 51–104.
- Advanced voucher prerequisite, settings and /payments fields: pinned raw lines 106–154.
- Advanced default payment text, PresentToShopper/voucher response fields, test/live setup: pinned raw lines 156–197.
- Method-level Boleto de Proposta, shopper payment paths and due-date/Offer cancelled timing: [[source-adyen-docs-payment-methods-boleto-bancario]] and its pinned raw lines 23–43; this entry's raw_files remains child-only.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-boleto-bancario]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/boleto-bancario/android-drop-in/2026-09-15|Boleto Bancário Android Drop-in guide, captured 2026-09-15]]
