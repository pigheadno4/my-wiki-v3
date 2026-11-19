---
title: "Customer Balance (Stripe)"
type: concept
category: technology
tags: [stripe, customer-balance, bank-transfers, payments, reconciliation, invoicing]
---

## Definition

The Stripe customer balance is a per-customer ledger with two distinct sub-balances:

| Type | Purpose | Usable for payment? |
| --- | --- | --- |
| **Cash balance** | Reconciliation layer for incoming bank transfers | Yes — up to available amount |
| **Invoice balance** | Liability offset between merchant and customer | No — only offsets future invoices |

## Cash Balance

Funds flow in when customers overpay via bank transfer or when transfers aren't automatically reconciled. Each customer can hold cash balances in multiple currencies (one per accepted bank transfer currency).

**Constraints**: cannot be topped up directly; not a digital wallet or e-money; can only be used for future payments or returned to the customer's bank account.

**Retrieve**: `stripe.customers.retrieve(id, { expand: ['cash_balance'] })`. Also works for Accounts v2 objects: `GET /v1/customers/acct_xxxxx`.

**Pay from cash balance**: `paymentIntents.create({ payment_method_types: ['customer_balance'], payment_method_data: { type: 'customer_balance' }, confirm: true })`. Succeeds immediately if sufficient; fails otherwise.

## Reconciliation

**Modes**: `automatic` (default) or `manual`. Override per customer: `stripe.customers.update(id, { cash_balance: { settings: { reconciliation_mode: 'manual' } } })`. Reset with `merchant_default`.

**Automatic priority order** (US/UK/EU/MX):

1. Match reference → single invoice (by invoice number)
2. Match reference → single PI (by `display_bank_transfer_instructions.reference`)
3. Find exact-amount group (1–5 invoices+PIs) → smallest → most invoices → oldest PIs
4. Fund oldest fully-fundable invoices
5. Apply remainder to oldest incomplete PIs

JP uses a simplified 3-step version (no reference matching).

Invoice eligible: `open` + not past due OR became overdue within last 30 days.

**Manual reconciliation API**: `stripe.paymentIntents.applyCustomerBalance(id, { amount?, currency })`. Also applicable to open Invoices via Dashboard.

**Webhook**: `cash_balance.funds_available` — always contains full current balance (not just new funds).

**Unreconciled funds**: auto-return attempt at **75 days**; swept to Stripe balance at **90 days**.

## Invoice Balance (Credit Balance)

Adjusted via Customer Balance Transactions. Applied at invoice finalization to reduce amount due. Represents a liability — not spendable as cash. Distinct from credit balance (see Customer Credit Balance docs).

## Cash Balance Transaction Types

| Type | Description |
| --- | --- |
| `funded` | Customer made a bank transfer; funds may auto-apply to open PaymentIntents |
| `applied_to_payment` | Funds applied to a PaymentIntent (auto or manual reconciliation) |
| `unapplied_from_payment` | Partially funded PaymentIntent was modified/canceled; funds returned to cash balance |
| `refunded_from_payment` | Successful PaymentIntent refunded back to cash balance |
| `return_initiated` | Unspent funds being returned to customer's bank account |
| `return_canceled` | Return attempt canceled (bank details not collected or refund canceled) |
| `transferred_to_balance` | Funds swept to merchant's Stripe balance due to failed refund or missing bank details |

## Funding Instructions

`stripe.customers.createFundingInstructions(id, { funding_type: 'bank_transfer', bank_transfer: { type }, currency })` — retrieve virtual bank account details without a PaymentIntent.

Per-region `financial_addresses` format: US → ABA (ACH/wire) + SWIFT; UK → sort_code (Bacs/FPS); EU → IBAN/BIC (SEPA, max 1,000 VBANs, ES unavailable); JP → zengin; MX → SPEI/CLABE.

Live mode: unique VBAN per customer. Account ownership PDF letter downloadable from Dashboard.

## See Also

- [[stripe-bank-transfers]] — primary funding mechanism for the cash balance
- [[source-stripe-customer-balance]] — overview: two balance types, transaction types, payment from balance API

## Sources

- [[source-stripe-customer-balance]] — balance types, retrieve API, pay-from-balance, 7 transaction type definitions
- [[source-stripe-customer-balance-reconciliation]] — automatic priority order (5-step per region), manual reconciliation API, cash_balance.funds_available webhook, 75/90-day unreconciled fund rules
- [[source-stripe-customer-balance-funding-instructions]] — createFundingInstructions API, per-region financial_addresses schemas, EU VBAN limit, account ownership letter
