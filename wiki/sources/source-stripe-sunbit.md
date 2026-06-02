---
title: "Stripe: Sunbit Payments"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-sunbit-2025.md"
tags: [stripe, bnpl, sunbit, buy-now-pay-later, consumer, us, installments, connect]
---

## Summary

Overview of Sunbit as a Stripe consumer BNPL for the US. 3/6/12/18-month installments; Connect supported; no manual capture. ~175 prohibited categories.

## Key Details

**Consumer BNPL** — US only, USD only. Pay in 3, 6, 12, or 18 monthly installments. **Connect supported** with `sunbit_payments` capability. **No manual capture**.

**Transaction limits**: min $60, max ~$20,000.

**Additional requirements**: no surcharging; financed amount must ≤ price of goods delivered; Sunbit handles customer payment collection.

**Disputes**: 12-day evidence window.

**Refunds**: 180-day window; async (up to 5 min). `refund.updated`/`refund.failed` webhooks.

**Connect**: all 5 charge types supported. `sunbit_payments` capability required.

**Prohibited categories**: ~175 categories (extensive list covering general retail, services, digital goods, restaurants, healthcare, travel).

## Raw Sources

- [[stripe-sunbit-2025]] — verbatim webpage content (381 lines); fixed `_webhook_` + `_Connect_` → `*italic*`; MP4 video URL left as-is
