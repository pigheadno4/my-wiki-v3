---
title: "Stripe — Minimum Balances for Automatic Payouts"
type: source
date_ingested: 2026-05-11
original_format: webpage
raw_files:
  - "stripe-payouts-minimum-balance-2026.md"
tags: [stripe, payouts, minimum-balance, cash-flow, negative-balance, connect, balance-settings-api]
---

## Summary

Keep a specified amount in your Stripe account after each automatic payout to cover refunds, disputes, and fees. Not supported in Brazil, India, Thailand.

## Key Details

- **Recommended amount**: 4–5× average daily processing volume
- **How it works**: payout = available balance − minimum balance; if below minimum, Stripe renews from available then incoming funds
- **Reconciliation**: minimum balance appears as `-X USD` transaction in Payout Reconciliation Report
- **Not supported**: Brazil, India, Thailand
- **Raising minimum**: accumulates from incoming payments; **Lowering**: released funds on next payout

## Setup

Dashboard → Payout Settings → Minimum Balance section → toggle on → set fixed amount.

## Platforms (Connect) — Balance Settings API

Configure per connected account via `stripe.balanceSettings.update()` with `payments.payouts.minimum_balance_by_currency` (in minor currency units):

- **Set/add**: pass currency code + amount (merge — won't overwrite other currencies)
- **Update**: pass same currency code with new amount
- **Delete single currency**: pass empty string for that currency code
- **Delete all**: pass empty string for entire `minimum_balance_by_currency`
- **Retrieve**: `stripe.balanceSettings.retrieve({ stripeAccount: '...' })`

**Warning**: notify connected accounts before setting — their payout amounts will differ from balance shown.

## Related Pages

- [[stripe-payouts]] — concept page (updated with minimum balance note)
- [[source-stripe-payouts-reconciliation]] — payout reconciliation report

## Raw Sources

- [[stripe-payouts-minimum-balance-2026]] — verbatim minimum balances guide (370 lines, 1 screenshot)
