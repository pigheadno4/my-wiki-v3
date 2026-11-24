---
title: "Stripe — Payout Reconciliation"
type: source
date_ingested: 2026-05-11
original_format: webpage
raw_files:
  - "stripe-payouts-reconciliation-2026.md"
tags: [stripe, payouts, reconciliation, balance-transactions, api, webhook]
---

## Summary

How to identify which transactions are included in a given automatic payout via Dashboard, report, or API using BalanceTransactions.

## Key Rules

- **Automatic payouts**: Stripe tracks which transactions are included — reconcilable via API
- **Manual payouts**: Stripe cannot identify included transactions — merchant responsible for reconciliation
- **`payout.reconciliation_completed` webhook**: signals when reconciliation data is ready

## API Flow

1. Get payout ID (`po_xxx`) via webhook, List Payouts API, or own DB
2. List BalanceTransactions filtered by payout:
   ```js
   stripe.balanceTransactions.list({ payout: 'po_xxx' })
   ```
3. Optionally expand source objects inline:
   ```js
   stripe.balanceTransactions.list({ payout: 'po_xxx', expand: ['data.source'] })
   ```

## BalanceTransaction `type` Values

`charge`, `refund`, `stripe_fee`, `payout` (the payout itself) — see balance transaction types docs for full list.

## `source` Property

Identifies the underlying object: `ch_xxx` for Charge, `re_xxx` for Refund. Use `expand` to inline without extra API calls.

## Related Pages

- [[stripe-payouts]] — concept page (updated with reconciliation note)
- [[source-stripe-payouts]] — payout overview

## Raw Sources

- [[stripe-payouts-reconciliation-2026]] — verbatim payout reconciliation guide
