---
title: "Stripe: Pay with Stripe Balance"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-balance-pay-2025.md"
tags: [stripe, connect, stripe-balance, subscriptions, accounts-v2, billing]
---

## Summary

Connect platform feature (Accounts V2 preview) to collect subscription payments directly from connected accounts' Stripe balances. Subscriptions only; 12 currencies; 34+ countries.

## Key Details

**Eligibility**: active connected account, platform-controlled, `card_payments` capability, Accounts V2 preview, cannot use Dynamic Payment Methods.

**Settlement**: domestic T+0, cross-border T+1.

**Failures**: `insufficient_funds` if balance in specified currency is insufficient. Automatic retries: 1st at ≥24h, 2nd on next Sunday.

**Avoidance**: tailor payout schedules; set minimum balance via Balance Settings API.

**Required consent**: must get connected account approval before first debit.

**BalanceTransaction types**: platform gets `type: payment`; connected account gets `type: stripe_balance_payment_debit`.

## Raw Sources

- [[stripe-balance-pay-2025]] — verbatim webpage content (eligibility, currency table, failure handling, reporting)
