---
title: "Stripe: Payment on Invoice"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-payment-on-invoice-2025.md"
tags: [stripe, bnpl, payment-on-invoice, rechnung, germany, austria, consumer, invoice]
---

## Summary

Overview of Stripe's payment on invoice product — a consumer-facing BNPL for Germany/Austria. Merchant is paid immediately; customer receives a 14-day branded invoice. Risk-based approval using buyer personal data.

## Key Details

**Consumer BNPL** (not B2B) — AT/DE customers, EUR only. DE merchant accounts only.

**14-day customer payment terms** — Stripe sends branded invoice to customer after approval.

**Merchant paid immediately** (immediate notification) — full amount minus fees added to Stripe balance on approval.

**Risk-based approval**: buyer provides name, email, address, date of birth; risk assessment determines approval or decline.

**Payout timing**: T+2 minimum (not standard).

**Connect**: Yes. Manual capture: Yes.

## Raw Sources

- [[stripe-payment-on-invoice-2025]] — verbatim webpage content (62 lines, hub/intro page)
