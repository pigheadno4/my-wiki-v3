---
title: "Metronome Revenue Recognition Examples"
type: source
date_ingested: 2026-08-19
canonical_url: "https://docs.metronome.com/guides/reporting-insights/financial-reporting/revenue-recognition-examples.md"
original_format: webpage
raw_files:
  - "metronome/guides/reporting-insights/financial-reporting/revenue-recognition-examples-2026-07-13.md"
tags: [metronome, revenue-recognition, financial-reporting, data-export, invoices, credits, commits]
---

## Overview

This page uses a fictional CloudNet business to illustrate how Metronome customer, contract, invoice, invoice-line-item, and balance-ledger exports can support downstream revenue-recognition analysis. It covers on-demand usage with free credits, prepaid commitment purchase and drawdown, prepaid expiration and overage, and a postpaid commitment with a period-end true-up.

These are provider-authored reporting examples, not an accounting standard, journal-entry specification, or complete close control. Several tables and narrative conclusions conflict arithmetically or semantically, so consumers must reconcile the current export schema and their own accounting policy rather than copy the examples as authoritative calculations.

## Exported evidence model

The examples join five data areas:

- customer metadata maps billing customers to CRM or ERP records;
- contract metadata supplies commercial identifiers such as contract type, opportunity ID, or sales-order ID;
- invoice type distinguishes prepaid purchase, usage, and postpaid true-up charges;
- invoice line items use `commit_id` for revenue-category classification, `product_id` for product attribution, and `starting_at` plus `ending_before` for service periods; and
- balances consolidate credits and commits, with ledger entries for invoice deductions, manual adjustments, expirations, and true-ups.

The page does not define table grain, primary keys, snapshot selection, export freshness, duplicate delivery, correction handling, currency denomination, ERP posting, debits and credits, performance obligations, allocation, breakage policy, tax, refunds, or sign-off. Use the dedicated data-export reference and the parent revenue-recognition guide for those boundaries.

## Scenario 1: On-demand usage with free credits

Customer A receives `$500` of free credits, uses CloudCompute and CloudStorage before and after the credit period, and receives a `$459` usage invoice for uncovered usage. The exported line items separately show gross product charges and negative free-credit applications, while the balance ledger records a `$410` automated deduction and `$90` expiration. The example treats uncovered usage as on-demand revenue and reports the free-credit drawdown and expiration separately.

> [!warning] CloudStorage arithmetic contradiction
> The uncovered CloudStorage line item is `150` units at `0.50`, with total `75`, and the invoice total of `459` equals `384 + 75`. The narrative nevertheless says the merchant can recognize `$150` of CloudStorage revenue. The table supports `$75`, not `$150`; verify the intended amount rather than copying the prose.

The source does not establish whether free-credit use is contra revenue under a merchant's governing policy. The parent guide describes that treatment as possible rather than universal.

## Scenario 2a: Prepaid purchase and first-month drawdown

Customer B prepays `$10,000` for a one-year commitment and receives a stated 20 percent rate discount. The example issues a `$10,000` `CONTRACT_SCHEDULED` invoice, defers that amount, then issues a zero-dollar `CONTRACT_USAGE` invoice whose line items show `$800` of CloudCompute and `$100` of CloudStorage covered by the commit. The ledger starts at `$10,000` and records a `$900` deduction.

> [!warning] Customer-key contradiction
> The Customer table assigns Customer B ID `10002`, and the balance row also uses `10002`, but the Contract row for contract `20002` uses customer ID `10001`, which belongs to Customer A in Scenario 1. Do not use that contract join without correcting and validating the intended customer key.

## Scenario 2b: Prepaid burn-down and expiration

The narrative says months after the first burn `$700` total per month, split `$600` CloudCompute and `$100` CloudStorage. The monthly table and balance ledger agree on an initial `$900` deduction, eleven later `$700` deductions, and `$1,400` expiration, which exactly consumes the `$10,000` balance. Zero-dollar usage invoices record drawdown while the unused remainder expires at the end.

> [!warning] Recognition-total contradiction
> The recognition bullets instead assign `$700` to CloudCompute plus `$100` to CloudStorage for each of months 2–12, totaling `$800` per month. Combined with the stated `$1,400` expiration, those bullets would recognize more than the `$10,000` prepaid amount and conflict with the `$700` monthly table and ledger. The likely corrected product split is not documented; do not invent it.

## Scenario 2c: Prepaid burn-down and overage

The overage variant starts with `$10,000`, reaches `$100` remaining after month 10, then says overage begins in month 11. Its month-11 summary table lists `$1,000` usage, `$900` overage, an `$800` invoice total, and a zero balance, while the detailed invoice is `$900` and its line items sum to `$900` (`800 + 200 - 100`). Month 12 has no balance and a `$1,000` invoice.

> [!warning] Overage calculation and classification contradictions
> The month-11 summary's `$800` invoice conflicts with both its stated `$900` overage and the detailed `$900` invoice. The recognition bullets then label all `$1,000` in months 11 and 12 as prepaid-commit revenue even though only `$100` remained entering month 11 and the scenario explicitly says overage begins then. The page does not provide a reliable corrected product-level split between remaining prepaid drawdown and overage.

## Scenario 3: Postpaid commitment and true-up

Customer C commits to `$10,000`, consumes `$800` per month for twelve months, and reaches `$9,600` of cumulative spending. The example then issues a `$400` `CONTRACT_TRUEUP` invoice and records twelve `$800` automated deductions plus a `$400` `postpaid_trueup` ledger entry.

> [!warning] Invoice-label and identifier contradictions
> The invoice table labels the twelve `$800` rows `CONTRACT_SCHEDULED`, but the concluding bullets call them usage invoices. The table labels the `$400` row `CONTRACT_TRUEUP`, but the conclusion calls it a scheduled invoice. The invoice ID `30011` is also repeated for three different service periods. Preserve the table values as example evidence, but do not infer which labels or IDs are correct without current schema and source-data verification.

## Accounting and implementation boundaries

- The page demonstrates Metronome data relationships and provider-proposed timing; it does not determine whether revenue is earned under GAAP, IFRS, or a merchant's contract-specific policy.
- Invoice issuance, zero-dollar invoices, drawdown, expiration, and true-up are billing events, not by themselves proof of performance-obligation satisfaction, allocation, collectibility, breakage treatment, or posting approval.
- The examples omit voids, regeneration, refunds, credit memos, corrections, restatements, payment state, taxes, foreign currency, close cutoffs, reconciliation tolerances, and auditor approval.
- Because several rows, totals, classifications, and identifiers conflict, implementers should rebuild control totals from current exported records and reconcile them to invoices and ledgers before relying on any recognition output.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-reporting-and-analytics]], [[metronome-credits-and-commits]], [[metronome-invoicing]], [[payment-reconciliation-reporting]]
- Related sources: [[source-metronome-guides-reporting-insights-financial-reporting-revenue-recognition]], [[source-metronome-guides-reporting-insights-financial-reporting-reconcile-data]], [[source-metronome-guides-reporting-insights-data-export-database-reference]]

## Raw Sources

- [[raw/metronome/guides/reporting-insights/financial-reporting/revenue-recognition-examples-2026-07-13|2026-07-13 snapshot — export-table examples for on-demand, prepaid, overage, expiration, and postpaid true-up reporting]]
