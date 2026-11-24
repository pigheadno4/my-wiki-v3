---
title: "Stripe: Pix Automático"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-pix-automatico-2025.md"
tags: [stripe, real-time-payments, pix, brazil, brl, pix-automatico, recurring, mandates, pre-debit, iof]
---

## Summary

Overview of Pix Automático — Stripe's mandate-based recurring Pix payment system. Customers authorize mandates in their bank app. Built-in 3-day pre-debit notification cycle. Not available for BR-based merchant accounts.

## Key Details

**Mandate authorization**: customer authorizes amount and billing cycle in bank app during initial payment. Free trials create mandate without initial charge.

**3-day pre-debit notification**: bank automatically notifies customer 3 days before each charge with exact amount and cancellation option. No merchant action required. Effective billing = schedule + 3 days. PaymentIntent in `processing` during this window.

**Processing timeline**: ~3 days to confirmation; up to 7 days with retries.

**Retries**: on failure (insufficient funds, network), Stripe retries once daily for 3 more days (payment stays in `processing`). Stripe Billing also supports 1-day retry for missed scheduling (contact Stripe to enable).

**Mandate customization** via `payment_method_options.pix.mandate_options`:

| Field | Default |
| --- | --- |
| `reference` | Business display name |
| `amount` | 400 BRL |
| `amount_type` | `maximum` |
| `amount_includes_iof` | `never` |
| `payment_schedule` | `monthly` |
| `end_date` | No expiry |
| `start_date` | Current date + 3 days |

**Daily schedule prohibited** — `payment_schedule: daily` causes all payments to fail.

**IOF applies** per recurring transaction. Same handling as one-time Pix.

**Not available for BR-based merchant accounts** (international merchants only for Pix Automático).

## Raw Sources

- [[stripe-pix-automatico-2025]] — verbatim webpage content (79 lines); no italic fixes needed
