---
title: "Stripe — Payout Reconciliation"
type: source
date_ingested: 2026-05-11
date_updated: 2026-11-22
original_format: webpage
canonical_url: https://docs.stripe.com/payouts/reconciliation
raw_files:
  - "stripe-payouts-reconciliation-2026-11-07.md"
  - "stripe-payouts-reconciliation-2026.md"
tags: [stripe, payouts, reconciliation, balance-transactions, api, webhook]
---

## Summary

The May 11 and November 7, 2026 guides explain how to identify the transactions in a [[stripe]] automatic payout through the Dashboard, the payout reconciliation report, or the Balance Transactions API.

## Key Rules

- **Automatic payouts** — Stripe tracks the transactions included in payouts it makes on the account's payout schedule.
- **Manual payouts** — the merchant controls timing and amount and reconciles the payout against its own transaction history.
- **`payout.reconciliation_completed` webhook** — one way to obtain the payout ID for reconciliation.

## API Flow

The Node.js request examples come from the May guide. The November guide shows the same list and expansion parameters in cURL.

1. Get the payout ID (`po_xxx`) from `payout.reconciliation_completed`, the List Payouts API, or your database. Retrieving that Payout returns properties such as amount, currency, and status. Use the Balance Transactions list for its component entries.
2. List BalanceTransactions with the automatic payout's ID in the `payout` filter. The default is up to 10 results. Set `limit` to change the page size, and use Stripe's auto-pagination to retrieve every page when reconciling the full payout. See the [November List Balance Transactions API reference](../../raw/stripe-api-balance-transactions-list-2026-11-07.md#L60-L70).
   ```js
   stripe.balanceTransactions.list({ payout: 'po_xxx' })
   ```
3. Optionally expand source objects inline:
   ```js
   stripe.balanceTransactions.list({ payout: 'po_xxx', expand: ['data.source'] })
   ```

## BalanceTransaction `type` Values

Examples include `charge`, `refund`, `stripe_fee`, and `payout` for the payout itself.

## `source` Property

Identifies the underlying object, such as `ch_xxx` for a Charge or `re_xxx` for a Refund. Expanding `data.source` includes those objects without a separate retrieval call for each entry.

## Related Pages

- [[stripe-payouts]] — payout reconciliation concept
- [[source-stripe-payouts]] — payout overview

## Raw Sources

- [[raw/stripe-payouts-reconciliation-2026-11-07|November 7, 2026 payout reconciliation guide]]
- [[raw/stripe-payouts-reconciliation-2026|May 11, 2026 payout reconciliation guide]] — verbatim payout reconciliation guide
