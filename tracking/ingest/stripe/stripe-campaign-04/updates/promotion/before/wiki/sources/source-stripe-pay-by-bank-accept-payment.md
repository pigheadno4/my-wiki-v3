---
title: "Stripe: Accept a Pay by Bank Payment"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-pay-by-bank-accept-payment-2025.md"
tags: [stripe, real-time-payments, pay-by-bank, open-banking, uk, europe, checkout, payment-intents, elements]
---

## Summary

Integration guide for Pay by Bank via Checkout and Elements (PaymentIntents). Confirms API enum `pay_by_bank` for UK/Europe open banking product. Notable: `statement_descriptor` required in `payment_method_options`. No Direct API path.

## Key Details

**API enum**: `pay_by_bank`. EUR and GBP only. Redirect-based.

**Two integration paths**:
- **Checkout**: `payment_method_types: ['pay_by_bank']`; must set `payment_method_options.pay_by_bank.statement_descriptor` (business name or identifier shown on customer's bank statement)
- **Elements (PaymentIntents)**: standard `stripe.confirmPayment` with `return_url`; no Direct API path

**`statement_descriptor` required** — unique among real-time methods; appears on customer's bank statement to identify the transaction.

**Supported business locations (Checkout)**: DE and GB only (remaining EU countries in private preview).

**Test data**:
- "Authorize test payment" → success
- "Fail test payment" → authentication failure

**Refund timing**: up to 730 days; arrives next business day but can take up to 7 days to show as successful.

**Note**: Stripe's Elements guide text says "turn **Swish** on in payment methods settings" — likely a copy-paste error; should say Pay by Bank.

## Raw Sources

- [[stripe-pay-by-bank-accept-payment-2025]] — verbatim webpage content (640 lines); fixed `*Prices*` ×1, `*subscription*` ×1, `*client secret*` ×1
