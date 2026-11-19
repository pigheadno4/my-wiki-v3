---
title: "Stripe: Use Boleto with Invoices"
type: source
date_ingested: 2026-05-07
original_format: webpage
raw_files:
  - "stripe-boleto-invoices-2025.md"
tags: [stripe, vouchers, boleto, brazil, brl, invoices, send-invoice, charge-automatically, auto-advance]
---

## Summary

Guide for using Boleto with one-off invoices. Parallel to the subscription guide — same collection method logic and customer setup. Key nuance: even `charge_automatically` invoices still require the customer to actively pay the Boleto voucher; Stripe emails a payment link.

## Key Details

**Both `send_invoice` and `charge_automatically` supported** (same decision table as subscriptions guide).

**Invoice creation**:
- `send_invoice`: include `payment_settings.payment_method_types: ['card', 'boleto']` + `days_until_due`
- `charge_automatically`: no explicit PM needed (uses customer default); no `days_until_due`

**`auto_advance`**: when `true`, Stripe auto-finalizes after a few hours. When `false`, manual finalization required.

**Key nuance**: even with `charge_automatically`, customer must still actively pay the Boleto voucher — Stripe emails a link. Boleto is never a true auto-debit.

**Invoice finalization**: sends invoice email. Finalized invoices are legal documents in many jurisdictions — certain fields become unalterable.

**Video tutorial** (CloudFront mp4): invoice editor walkthrough — not downloaded (video file).

## Raw Sources

- [[stripe-boleto-invoices-2025]] — verbatim webpage content (396 lines); fixed `*payment method*` ×1, `*Customers*` ×1, `*subscriptions*` ×2, `*Products*` ×1, `*Prices*` ×1, `*invoices*` ×1, `*sandbox*` ×2; 1 CloudFront .mp4 video URL not downloaded
