---
title: "Stripe: Customer Balance Reconciliation"
type: source
date_ingested: 2026-05-05
original_format: webpage
raw_files:
  - "stripe-customer-balance-reconciliation-2025.md"
tags: [stripe, customer-balance, bank-transfers, reconciliation, webhooks, invoicing]
---

## Summary

Deep-dive on customer cash balance reconciliation: automatic vs manual modes, per-region reconciliation priority order, manual reconciliation API, the `cash_balance.funds_available` webhook, unreconciled fund handling, and the credit balance distinction.

## Key Details

**Reconciliation modes**: `automatic` (account default) or `manual`. Override per customer: `stripe.customers.update(id, { cash_balance: { settings: { reconciliation_mode: 'manual' } } })`. Reset to account default with `reconciliation_mode: 'merchant_default'`. Also works for Accounts v2 via `/v1/customers/acct_xxxxx`.

**Automatic reconciliation — priority order** (US/UK/EU/MX):
1. Match bank transfer reference → single invoice by invoice number
2. Match reference → single PI with matching `display_bank_transfer_instructions.reference`
3. Find exact-amount group (1–5 invoices+PIs) → prefer smallest group → most invoices → oldest PIs
4. Fund oldest fully-fundable invoices first
5. Apply remainder to oldest incomplete PIs

JP simplified (no reference matching): find exact group → oldest invoices → oldest PIs.

**Invoice eligibility**: `open` + not past due OR became overdue within last 30 days.

**Manual reconciliation API**: `stripe.paymentIntents.applyCustomerBalance(PAYMENTINTENT_ID, { amount, currency })`. Amount optional (defaults to remaining). Also works for open Invoices via Dashboard (Charge customer → Cash Balance).

**Webhook**: `cash_balance.funds_available` — always contains full current cash balance (not just newly added funds). Handle by listing customer PIs → filter eligible ones → call `applyCustomerBalance` in chronological order.

**Unreconciled funds**: auto-return attempt at 75 days; swept to Stripe balance at 90 days.

**Credit balance** (distinct from cash balance): Invoices-only feature; applied at invoice finalization to reduce amount due. See Customer Credit Balance docs for details.

## Raw Sources

- [[stripe-customer-balance-reconciliation-2025]] — verbatim webpage content (311 lines); fixed 7× `_italic_` → `*italic*`; downloaded 4 CDN images to `raw/assets/`
