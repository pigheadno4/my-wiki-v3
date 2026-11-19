---
title: "Japan Card Installments (分割払い)"
type: concept
category: technology
tags: [japan, installments, cards, jpy, bonus-payments, stripe-japan]
---

Part of [[stripe-installments]] — Stripe's installments family (also includes Mastercard Installments and Mexico meses sin intereses).

## Definition

Japan card installments (分割払い) let customers split credit-card purchases over multiple billing statements. The merchant receives the full transaction amount as with a standard card payment, while the card issuer provides credit and collects installments; funds become available on the same schedule as other card payments, with standard payout timing.

**Restrictions**: Japan Stripe accounts, Japanese-issued credit cards (not debit or prepaid) and JPY. Recurring installment payments are marked unsupported. The guide also says not to use installments for other off-session payments where the customer does not choose the plan when making the payment; it does not establish support for another off-session case.

## Plan Types

| Plan | Description |
| --- | --- |
| Installments | Fixed split over N payments (Visa/MC: up to 60; JCB: up to 24) |
| Revolving | Open-ended revolving credit |
| Bonus | Paid at customer's company bonus cycle |

## Brand Support

| Brand | Installments | Revolving | Bonus |
| --- | --- | --- | --- |
| Visa/Mastercard | Up to 60 | ✓ | ✓ |
| JCB | Up to 24 | ✓ | ✓ |
| Diners Club | ✗ | ✓ | ✓ |
| Amex | ✗ | ✗ | ✗ |
| Discover | ✗ | ✗ | ✗ |

Amex stopped installments Dec 2022 (cardholders use post-checkout あと分割 instead).

## Fees

No additional merchant fees. Customer may pay interest to their card company (typically no interest for 2-installment or bonus plans).

## Bonus Payment Windows

Available:
- **Summer**: Dec 16 – Jun 15
- **Winter**: Jul 16 – Nov 15

Unavailable: Jun 16–Jul 15 and Nov 16–Dec 15.

**Edge cases**: Customer who starts checkout during availability but completes after cutoff → payment fails. Separate auth/capture: bonus captured outside window may appear as normal card charge or shift to next bonus cycle.

## Sources

- [[source-stripe-jp-installments]] — primary source: properties, brand support table, bonus windows, requirements
- [[source-stripe-jp-installments-accept-payment]] — 2026-05-01 full integration guide for Checkout, Payment Element, Direct API, Invoices, Payment Links and sandbox cards; its 2026-11-07 canonical capture is only a five-variant navigation index. With dynamic payment methods, the May guide says installments appear automatically and the `enabled` field is omitted in the PaymentIntent path.
