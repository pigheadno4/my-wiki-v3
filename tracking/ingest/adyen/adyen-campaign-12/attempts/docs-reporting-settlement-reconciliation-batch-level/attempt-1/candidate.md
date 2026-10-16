---
title: "Adyen batch-level settlement reconciliation"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/reporting/settlement-reconciliation/batch-level"
raw_files:
  - "adyen/docs/reporting/settlement-reconciliation/batch-level/2026-09-15.md"
tags: [adyen, reporting, settlement, reconciliation]
---

## Overview

This Adyen webpage snapshot explains how to use the **Aggregate Settlement Details Report** to identify payout batches in a date range and compare their reported totals with a bank statement. It is a batch-level report workflow, not a transaction-by-transaction ledger or independent evidence that a bank received a payout. See [[adyen]] and [[adyen-reporting]].

## Key takeaways

- Find a batch by **Batch Number**. One batch may occupy multiple report entries because its settlements span creation dates, payment methods, journal types, or currencies (raw lines 23–34). A batch number alone therefore does not identify a single row or a single currency amount.
- For entries whose **Journal Type** is `Settled`, the guide describes each entry as a group of transactions. `Gross Credit` is the group total, `Bank/Card Commission` and `DCC Markup` are deductions, `Num Txs` is its transaction count, and `Net Credit` is described as gross less those two fee/markup amounts (raw lines 60–68). Do not apply that formula to every journal type or treat an aggregated entry as one payment.
- The examples illustrate two distinct tasks: batch 604 has `Settled` and `Balancetransfer` rows across USD, EUR, and SEK (raw lines 36–58); batch 608 totals `Net Credit`, commission, and transaction counts in EUR from three `Settled` rows (lines 70–82). These are examples, not universal values or a rule to add unlike currencies. The table has separate `Net Debit (NC)` and `Net Credit (NC)` columns; no universal sign convention is established on this page.
- The guide frames reconciliation **against a bank statement**. The report supplies a batch identifier and report amounts to compare; this page contains no bank-statement entry or receipt confirmation for any particular batch. Its description of `Net Credit` as an amount settled to a bank account must be read within that comparison workflow.

## Detail locators

- `Step 1: Find settlement batches`, raw lines 23–58: batch number, reasons for multiple entries, and the mixed-journal/mixed-currency illustration.
- `Step 2: Find the total transaction amounts and fees in a batch`, raw lines 60–82: `Settled`-entry fields and same-currency EUR calculation example.
- `See also`, raw lines 84–86: navigation to transaction-level reconciliation for a different grain.

## Related

- [[adyen-reporting]] — reporting and reconciliation evidence boundary.
- [[source-adyen-docs-reporting-settlement-reconciliation-batch-level-aggregate-settlement-details-report]] — report-specific fields and generation details.
- [[source-adyen-docs-reporting-settlement-reconciliation-transaction-level]] — transaction-level reconciliation route.

## Raw Sources

- [[raw/adyen/docs/reporting/settlement-reconciliation/batch-level/2026-09-15|Batch-level reconciliation, fetched 2026-09-15]]
