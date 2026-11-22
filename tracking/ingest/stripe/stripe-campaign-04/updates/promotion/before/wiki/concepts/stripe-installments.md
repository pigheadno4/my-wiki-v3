---
title: "Stripe: Installments"
type: concept
category: technology
tags: [installments, bnpl, mastercard, mexico, japan, cards, recurring-payments]
---

## Definition

Installments are credit card payments where customers split purchases across multiple billing statements. Stripe supports three distinct installment products across different markets.

## Products

### Mastercard Installments

Customers with a Mastercard Installments virtual card pay in **4 interest-free installments** at checkout. Auto-enrolled when accepting Mastercard — no setup needed. 7 countries (AE/AU/CA/DE/GB/MY/US). Surcharging prohibited. Recurring/subscription purchases declined despite "Yes" in properties. Prohibited MCCs include money transfer, quasi cash, MoneySend. Opt-out: contact support (1-3 days). See [[source-stripe-mastercard-installments]] for details.

### Mexico — Meses Sin Intereses

Mexico-only consumer credit card installment feature. MX Stripe accounts only; MXN only; consumer cards only (no corporate). 6 plan options (3–24 months); merchant receives full amount **minus additional fees** (5%–22.5%); bank handles collection. 33 supported issuers including BBVA, Banorte, Santander, Amex, Nubank, Didi. Custom min/max amounts configurable. Connect supported. See [[source-stripe-mx-installments]] for fees table and full issuer list.

### Japan — 分割払い

Japan card installment feature for Japan Stripe accounts processing JPY on Japanese-issued credit cards. The merchant receives full transaction principal as with standard card payments, while the issuer extends credit and collects installments; funds become available on the ordinary card schedule, with standard payout timing.

**3 plan types**: fixed installments, revolving credit, bonus (paid at customer's company bonus cycle).

**Brand support**:

| Brand | Installments | Revolving | Bonus |
| --- | --- | --- | --- |
| Visa/Mastercard | Up to 60 | ✓ | ✓ |
| JCB | Up to 24 | ✓ | ✓ |
| Diners Club | ✗ | ✓ | ✓ |
| Amex | ✗ | ✗ | ✗ (stopped Dec 2022) |
| Discover | ✗ | ✗ | ✗ |

**Bonus windows**: Summer (Dec 16–Jun 15), Winter (Jul 16–Nov 15). Unavailable Jun 16–Jul 15 and Nov 16–Dec 15. Checkout-to-payment cutoff crossing causes payment failure.

**Restrictions**: Japan Stripe account, Japanese-issued credit card (no debit/prepaid) and JPY. Recurring installment payments are unsupported. For other off-session payments, the guide warns against use when the customer does not select the plan at payment; it does not affirm support in any other off-session case.

## Sources

- [[source-stripe-installments]] — installments overview: 3 products (Mastercard, Mexico, Japan)
- [[source-stripe-mastercard-installments]] — Mastercard Installments: auto-enrolled, 4× interest-free, 7 countries, prohibited MCCs, recurring caveat
- [[source-stripe-mx-installments]] — Mexico meses sin intereses: fees table (3–24mo), 33 supported issuers, requirements, Connect
- [[source-stripe-mx-installments-accept-payment]] — Mexico meses sin intereses integration: Checkout/Elements/Direct API/Invoices/Payment Links, custom settings, test cards
- [[source-stripe-jp-installments]] — Japan installments detail: brand support table, bonus windows, requirements
- [[source-stripe-jp-installments-accept-payment]] — 2026-05-01 Japan installment integration guide for Checkout, Elements, Direct API, Invoices and Payment Links; the 2026-11-07 capture at its canonical URL supplies variant navigation only.
