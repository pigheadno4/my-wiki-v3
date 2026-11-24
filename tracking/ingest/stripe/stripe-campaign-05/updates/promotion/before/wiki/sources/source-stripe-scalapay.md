---
title: "Stripe: Scalapay Payments"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-scalapay-2025.md"
tags: [stripe, bnpl, scalapay, buy-now-pay-later, consumer, installments, europe, eur]
---

## Summary

Overview of Scalapay as a Stripe consumer BNPL (Pay in 3 or 4) for European customers. EUR-only across all 28 merchant countries. No Connect. Shorter 90-day refund window. Approval-based merchant categories.

## Key Details

**Consumer BNPL** — Pay in 3 or 4 installments. **EUR only** across all 28 merchant countries (including US, AU, CA, SG). **No Connect support**.

**Transaction limits**: min €5, max ~€5,000.

**Allowed categories**: "At discretion of Scalapay" — no published list; approval-based.

**Disputes**: 12-day evidence window.

**Refunds**: **90-day** window (shorter than Billie/Kriya/Mondu's 180 days); async (up to 5 min). `refund.updated`/`refund.failed` webhooks.

## Raw Sources

- [[stripe-scalapay-2025]] — verbatim webpage content (170 lines); fixed `_webhook_` → `*webhook*`; MP4 video URL left as-is
