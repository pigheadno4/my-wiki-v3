---
title: "Stripe — Multi-Currency Settlement"
type: source
date_ingested: 2026-05-11
original_format: webpage
raw_files:
  - "stripe-payouts-multicurrency-2026.md"
tags: [stripe, payouts, multi-currency, settlement, fx, bank-account]
---

## Summary

Multi-currency settlement lets Stripe accounts avoid FX conversion fees by accruing and paying out in multiple currencies. Requires one bank account per currency.

## Availability

AE, AU, CH, EU, GB, HK, LI, NO, SG, US.

## Setup

1. Dashboard → Payout Settings → **Manage Currencies** → select currencies
2. Attach one bank account per settlement currency (currency must match)
3. Balances accrue per currency; payouts follow configured schedule once minimum balance met

## Key Rules

- No FX fees for payments in configured currencies
- One bank account required per currency — currency must match
- Cannot pay out until minimum balance for that currency is reached
- Payouts follow your existing schedule (manual or automatic)

## Related Pages

- [[stripe-payouts]] — concept page (updated with multi-currency detail)
- [[source-stripe-payouts]] — main payouts reference

## Raw Sources

- [[stripe-payouts-multicurrency-2026]] — verbatim multi-currency settlement guide
