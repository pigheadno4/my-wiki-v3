---
title: "Boleto Bancário iOS Drop-in"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/boleto-bancario/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/boleto-bancario/ios-drop-in/2026-09-15.md"
tags: [adyen, boleto-bancario, ios, drop-in, voucher]
---

## Overview

This 2026-09-15-captured Adyen guide adds **Boleto Bancário to an existing iOS Drop-in integration** through either Sessions or Advanced server-side flow. It covers shopper identity and due-date fields, voucher handling, and offline test reconciliation. A voucher or `PresentToShopper` response is not proof of paid status. See [[adyen]], [[adyen-online-payments]], and the method overview [[source-adyen-docs-payment-methods-boleto-bancario]] for voucher lifecycle and method capability context.

## Key takeaways

- **Sessions flow** requires an existing iOS Drop-in Sessions integration, Checkout API **v68 or later**, and Boleto Bancário added in Customer Area. Its `/sessions` additions require `shopperName`, `billingAddress`, and CPF/CNPJ `socialSecurityNumber`. Optional `deliverAt` is a UTC ISO 8601 due date; the page states a five-day default and next-working-day payment when it falls on a weekend or national holiday (raw lines 25–49).
- **Advanced flow** requires an existing iOS Drop-in Advanced integration, Customer Area setup, and handling of the additional `action.type: voucher` action. The requirement points to a base guide anchor named `#handle-the-redirect`, although the actual action identified here is **voucher**; follow the voucher action contract rather than inferring a redirect from that link label (raw lines 88–98).
- Advanced `/payments` additions require `paymentMethod.type: boletobancario`, shopper name, billing address, and CPF/CNPJ. Its optional due-date field is **`deliveryDate`**, distinct from Sessions `deliverAt`; both descriptions specify UTC ISO 8601, a five-day default, and the weekend/holiday next-working-day condition (raw lines 108–120).
- No Boleto-specific Drop-in configuration parameters are added in either flow (raw lines 60–64, 100–104). Optional `shopperEmail` sends a copy of the form. If a custom `shopperStatement` is supplied, the page instructs it to rule out higher/lower amounts and payment after the due date; the default Portuguese text conditions order processing on confirmed payment with no amount difference (raw lines 48–58, 119–129).
- The Advanced response includes `action.type: voucher` and `resultCode: PresentToShopper`, with voucher PDF URL, expiry, issuing-bank indicator, barcode reference, and amount. This is presentation information, not paid confirmation (raw lines 131–143).
- Boleto is offline. In **test**, the page simulates payment by promoting a pending offer to sale in test Customer Area. Pending or expired Boletos are under **Offers**, paid Boletos under **Payment list**; reconciliation should be tested. Before accepting live Boleto payments, submit a request in live Customer Area (raw lines 68–86, 147–165). Manual test promotion is not live-payment evidence.

## Detail locators

- Sessions prerequisite and `/sessions` fields: raw `## Sessions flow Drop-in`, lines 25–49.
- Sessions statement defaults, no extra configuration, and test path: raw lines 51–86.
- Advanced prerequisites and voucher-versus-redirect link mismatch: raw `## Advanced flow Drop-in`, lines 88–104.
- Advanced `/payments` fields and voucher response: raw lines 106–143.
- Advanced test and live request: raw lines 145–165.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-boleto-bancario]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/boleto-bancario/ios-drop-in/2026-09-15|Boleto Bancário iOS Drop-in, captured 2026-09-15]]
