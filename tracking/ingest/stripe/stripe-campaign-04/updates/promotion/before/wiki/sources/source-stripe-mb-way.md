---
title: "Stripe: MB WAY Payments"
type: source
date_ingested: 2026-05-07
original_format: webpage
raw_files:
  - "stripe-mb-way-2025.md"
tags: [stripe, wallets, mb-way, portugal, eur, phone-number, disputes, connect, refunds]
---

## Summary

Overview of Stripe's MB WAY integration — Portugal-only phone-number-based digital wallet. 40 merchant countries. €0.50–€5,000 per transaction, €1,000 daily default limit (adjustable to €10,000). Disputes supported (7-day evidence). 365-day refunds. Statement descriptor ignored.

## Key Details

**API enum**: `mb_way`. EUR only. Portugal customers only.

**Payment flow**: customer provides phone number → push notification in MB WAY app → authorize → immediate confirmation.

**International phone numbers supported** (most Portuguese: +351).

**Transaction limits**: €0.50 – €5,000. Daily cumulative default: €1,000 (customer can adjust up to €10,000 in app).

**40 merchant countries** — includes MX, HK, JP, NZ, US (broad for a Portugal-only wallet).

**Disputes**: Yes — 7-day evidence submission. Fraud, double payments, order/amount discrepancy. Stripe holds amount until resolution.

**Refunds**: 365-day window. Minutes to complete. Full and partial. Multiple partials allowed.

**Statement descriptor**: ignored — `Stripe Inc` shown on bank statements.

**No recurring. No manual capture. Mobile Payment Element not supported.**

**Checkout restrictions**: no subscription mode, no setup mode, no `setup_future_usage`.

**Connect**: all charge types. Capability: `mb_way_payments`.

## Raw Sources

- [[stripe-mb-way-2025]] — verbatim webpage content (177 lines); fixed `*sandbox*` ×1; 1 stripecdn .mp4 video not downloaded
