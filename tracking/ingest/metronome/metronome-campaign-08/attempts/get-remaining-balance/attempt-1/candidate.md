---
title: "Track the remaining balance of a credit or commit"
type: source
date_ingested: 2026-08-01
canonical_url: "https://docs.metronome.com/guides/customers-billing/optimize-customer-experience/get-remaining-balance"
original_format: webpage
raw_files:
  - "metronome/guides/customers-billing/optimize-customer-experience/get-remaining-balance-2026-07-13.md"
tags: [metronome, credits-and-commits, balances, ledgers, invoicing]
---

## Overview

This guide explains two ways to retrieve a customer's remaining Metronome credit or commit balance: a single filtered aggregate from `/getNetBalance`, or individual balances and their signed ledger entries through `listBalances`. It also documents fractional monetary values, effective timestamps, manual adjustments, and the ledger-entry families used for credits plus prepaid and postpaid commits.

## Key takeaways

- `/getNetBalance` returns one customer-scoped aggregate and supports filtering by balance type, currency, pending charges, and custom fields. The guide calls the result real-time but gives no freshness or consistency SLA.
- `listBalances` supports a detailed view in which each credit or commit has a ledger; summing that ledger's signed entries yields the remaining balance for that individual ledger.
- Balance amounts can be fractional. USD amounts are denominated in cents, so `0.8` means $0.008; truncating to an integer loses value, while intentional rounding requires an explicit client policy.
- Ledger entries have a type, a positive or negative amount, and an effective timestamp. Each invoice that consumes a credit or commit produces one invoice-deduction entry whose timestamp is the end of that usage invoice's service period.
- Effective timestamps can be used to present a balance with or without pending charges, but the page does not define cutoff operators, time-zone behavior, or how pending charges map to invoice lifecycle states.
- Positive and negative manual ledger adjustments can correct mistakes or migrate outstanding balances through the Metronome app or `/addManualBalanceLedgerEntry`.

## Aggregate and detailed balance views

The `/getNetBalance` endpoint is the documented aggregate view: it returns one sum of the remaining balance for a customer after the selected balance-type, currency, pending-charge, and custom-field filters are applied. The page does not enumerate the filter values or request and response fields, and a currency filter must not be interpreted as permission to add unlike currencies. It also does not say how the customer aggregate treats multiple contracts, hierarchy, product applicability, or custom pricing units.

The `listBalances` endpoint is the documented detailed view. Each returned credit or commit is associated with its own ledger, and the signed sum of all entries in that ledger is its total remaining balance. The page does not provide pagination, ordering, snapshot-consistency, or response-shape guarantees for this endpoint.

## Ledger arithmetic and effective time

Every ledger entry has a `type`, signed `amount`, and effective `timestamp`. The entry type explains the balance-changing event, while the amount's sign determines whether that event adds to or subtracts from the ledger. Invoice deductions occur once per invoice that consumes the balance, and their effective timestamp is always the end of that usage invoice's service period; this accounting-effective time is not documented as the invoice creation, finalization, delivery, or payment time.

In the worked credit example, a $100 segment starts on September 1, a $63 automated invoice deduction is effective October 1, and the unused $37 expires on October 1. The signed ledger therefore moves from $100 to $37 and then to zero. This illustrates ledger arithmetic, not a universal invoice-finalization sequence or a promise about when an API read observes each entry.

## Credit ledger entry types

- `credit_segment_start` adds the value made accessible when a credit access segment begins.
- `credit_automated_invoice_deduction` records usage-invoice drawdown that applies to the credit.
- `credit_segment_expiration` removes unused value at the end of a credit segment.
- `credit_manual` records a manual credit-ledger adjustment.
- `credit_seat_based_adjustment` adds credit for a seat increment when a recurring credit is linked to a subscription.

## Commit ledger entry types

Postpaid commits use `postpaid_initial_balance` for the starting balance, `postpaid_automated_invoice_deduction` for invoice-covered usage, `postpaid_trueup` for a true-up invoice covering usage outside automated usage invoices, `postpaid_rollover` for unused usage moved to a new contract, `postpaid_manual` for manual adjustments, and `postpaid_commit_expiration` for unused expired value excluding value that rolled over.

Prepaid commits use `prepaid_segment_start` when a segment becomes accessible, `prepaid_automated_invoice_deduction` for applicable usage-invoice drawdown, `prepaid_rollover` for unused usage moved to a new contract, `prepaid_segment_expiration` and `prepaid_commit_expiration` for unused expired value excluding rollover, `prepaid_manual` for manual adjustments, and `prepaid_commit_seat_based_adjustment` for added commit value from a seat increment on a recurring subscription-linked commit. The page gives identical descriptions for the two prepaid expiration types and does not explain their distinct trigger boundaries.

## Manual adjustments and operating boundaries

The Metronome app and `/addManualBalanceLedgerEntry` endpoint accept positive or negative adjustments to one credit or commit ledger. The guide cites correction and migration as examples, but does not define authorization, idempotency, validation, effective-time defaults, reversal behavior, audit metadata, or interaction with finalized invoices.

The balance APIs can support account-health displays, forecasting, and customer-facing balance views, but those use cases do not establish accounting treatment or entitlement enforcement. The page also does not document HTTP methods, exact response schemas, error handling, rate limits, precision limits, rounding mode, currency exponent rules beyond the USD example, cross-currency aggregation, late-entry behavior, or read-after-write consistency.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-credits-and-commits]], [[metronome-customers-and-contracts]], [[metronome-invoicing]]
- Related source: [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-create-a-pre-paid-commit]]

## Raw Sources

- [[raw/metronome/guides/customers-billing/optimize-customer-experience/get-remaining-balance-2026-07-13|2026-07-13 snapshot — aggregate and ledger balance retrieval, signed entries, and effective timestamps]]
