---
title: "Japan Card Installments (分割払い)"
type: concept
category: technology
tags: [japan, installments, cards, jpy, bonus-payments, stripe-japan]
---

Part of [[stripe-installments]] — Stripe's installments family (also includes Mastercard Installments and Mexico meses sin intereses).

## Definition

Japan card installments (分割払い) allow customers to split credit card purchases over multiple billing statements. Merchant receives full amount upfront; card company handles credit and collection.

**Restrictions**: Japan Stripe accounts only; JP-issued credit cards only (no debit/prepaid); JPY only; no recurring/off-session use.

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
- [[source-stripe-jp-installments-accept-payment]] — integration guide: Checkout, Payment Element, Direct API (4-step), Invoices, Payment Links; test cards
