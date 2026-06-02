---
title: "Stripe: Alipay Payments"
type: source
date_ingested: 2026-05-07
original_format: webpage
raw_files:
  - "stripe-alipay-2025.md"
tags: [stripe, wallets, alipay, china, cny, multi-currency, connect, recurring]
---

## Summary

Overview of Stripe's Alipay integration — China's dominant digital wallet, billion+ users. Multi-currency (CNY default + 10 settlement currencies). 39 merchant countries. 90-day refunds (async, 5 min). Recurring invite-only. Connect partial (Direct/on_behalf_of private preview). Dual prohibited business list (Stripe + Alipay).

## Key Details

**API enum**: `alipay`. CNY default (always shown to customer). 10 additional currencies by merchant country.

**Customer**: Chinese consumers, overseas Chinese, Chinese travelers worldwide.

**Settlement currencies**: CNY (any country), AUD (AU), CAD (CA), EUR (EU), GBP (GB), HKD (HK), JPY (JP), MYR (MY), NZD (NZ), SGD (SG), USD (US).

**39 merchant countries** — including HK, JP, MY, SG, NZ (broader than most wallets).

**Refunds**: 90-day window. Asynchronous, up to 5 minutes. No disputes.

**Recurring**: requires approval — subscriptions and invoicing invite-only.

**Connect**: partial — Destination and Separate charges supported; Direct charges and `on_behalf_of` are private preview. Capability: `alipay_payments`.

**Prohibited categories**: dual list — Stripe's standard restricted businesses PLUS Alipay's own prohibited business list (stripe.com/legal/alipay).

**No manual capture. No SetupIntents.**

## Raw Sources

- [[stripe-alipay-2025]] — verbatim webpage content (170 lines); fixed `*webhook*` ×1
