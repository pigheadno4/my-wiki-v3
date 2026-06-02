---
title: "Stripe: Vouchers Overview"
type: source
date_ingested: 2026-05-07
original_format: webpage
raw_files:
  - "stripe-vouchers-2025.md"
tags: [stripe, vouchers, boleto, konbini, multibanco, oxxo, cash, in-person, brazil, japan, portugal, mexico]
---

## Summary

Hub page for Stripe's 4 cash voucher payment methods: Boleto (Brazil), Konbini (Japan), Multibanco (Portugal), OXXO (Mexico). Customers complete online checkout then pay in-person at convenience stores/ATMs. Not suitable for immediate delivery or businesses requiring refunds.

## Key Details

**Payment flow**: customer selects voucher at checkout → receives digital voucher code (email/app) → pays with cash at authorized location (convenience store, ATM, bank) → payment confirmed.

**Four methods**:

| Method | API enum | Country | SetupIntents | setup_future_usage | Subscriptions | Invoicing |
| --- | --- | --- | --- | --- | --- | --- |
| Boleto | `boleto` | Brazil | Yes | Yes | Yes | Yes |
| Konbini | `konbini` | Japan | No | No | Yes (send_invoice) | Yes (send_invoice) |
| Multibanco | `multibanco` | Portugal | No | No | Yes (send_invoice) | Yes (send_invoice) |
| OXXO | `oxxo` | Mexico | No | No | No | No |

**No manual capture. No redirect required.** All use PaymentIntents.

**Konbini Connect**: restricted — requires invite to create charges on behalf of other accounts.

**Not suitable for**: immediate delivery (1 business day confirmation); businesses needing refunds (not all methods support them).

## Raw Sources

- [[stripe-vouchers-2025]] — verbatim webpage content (49 lines); no italic fixes; 1 SVG flow diagram downloaded to assets/
