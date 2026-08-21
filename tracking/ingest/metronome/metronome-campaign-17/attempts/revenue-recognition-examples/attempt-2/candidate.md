---
title: "Metronome Revenue Recognition Examples"
type: source
date_ingested: 2026-08-20
canonical_url: "https://docs.metronome.com/guides/reporting-insights/financial-reporting/revenue-recognition-examples.md"
original_format: webpage
raw_files:
  - "metronome/guides/reporting-insights/financial-reporting/revenue-recognition-examples-2026-07-13.md"
tags: [metronome, revenue-recognition, financial-reporting, data-export, invoices, credits, commits]
---

## Overview

This page uses a fictional CloudNet business to illustrate how Metronome customer, contract, invoice, invoice-line-item, and balance-ledger exports can support downstream revenue-recognition analysis. It covers on-demand usage with free credits, prepaid commitment purchase and drawdown, prepaid expiration and overage, and a postpaid commitment with a period-end true-up.

These are provider-authored reporting examples, not an accounting standard, journal-entry specification, or complete close control. Several sample keys, table fields, totals, and narrative conclusions conflict, so the examples must not be copied as executable schema or authoritative accounting calculations.

## Exported evidence model

The introductory table says customer and contract metadata map billing records to CRM or ERP entities; invoice type distinguishes prepaid purchases, usage, and postpaid true-ups; invoice-line-item `commit_id`, `product_id`, `starting_at`, and `ending_before` classify revenue, attribute products, and identify service periods; and balance type plus ledger entries expose credit and commit deductions, adjustments, expirations, and true-ups.

> [!warning] Illustrative schema does not match its own field names
> The introduction names `invoices.type`, `line_items.product_id`, and `balances.type`. The scenario tables instead label the invoice field `invoice_type`, supply `product_name` without a `product_id` column, and vary the balance-type header among `ledger type`, `ledger_type`, and `commit_type`. Treat these as illustrative displays, not executable current Data Export schemas; reconcile table names, columns, grain, and joins against the current database reference.

The examples do not define table grain, snapshot selection, export freshness, duplicate delivery, correction handling, currency denomination, ERP posting, debits and credits, performance obligations, allocation, breakage policy, tax, refunds, or sign-off.

## Identifier scope and join boundary

The sample identifiers cannot safely be treated as globally unique across the page:

- Customer B is ID `10002`, and balance `50002` also uses customer `10002`, but contract `20002` uses customer `10001`, which belongs to Customer A.
- Invoice IDs `30002` through `30012` recur across Customer B contract `20002` and Customer C contract `20003`. Within Scenario 3, invoice ID `30011` is reused for three different service periods.
- Line-item IDs `40005` and `40006` recur between Scenario 1 and Scenario 2a, while `40006` through `40008` recur between Scenario 2a and Scenario 2c for different invoices and meanings.
- Ledger-entry IDs beginning with `60001` recur under balances `50001`, `50002`, and `50003`.

The page may intend Scenarios 2a–2c and Scenario 3 as isolated alternatives rather than one mergeable dataset, but it does not state an identifier namespace. Do not assume global uniqueness, silently renumber examples, or combine and join scenarios by these IDs without current source-data and key-scope verification.

## Scenario 1: On-demand usage with free credits

Customer A receives `$500` of free credits and uses CloudCompute and CloudStorage before and after the credit period. The `$459` usage invoice separates gross product charges and negative free-credit applications; the balance ledger records a `$410` automated deduction and `$90` expiration. The conclusion treats uncovered usage as on-demand revenue and reports free-credit application and expiration separately.

> [!warning] CloudStorage arithmetic contradiction
> The uncovered CloudStorage line item is `150` units at `0.50`, total `75`, and the invoice total `459` equals `384 + 75`. The narrative nevertheless says the merchant can recognize `$150` of CloudStorage revenue. The table supports `$75`, not `$150`; the intended prose correction is not stated.

The parent guide says free credits are unpaid and their drawdown may have a contra-revenue effect. This example does not establish that treatment under a merchant's governing policy.

## Scenario 2a: Prepaid purchase and first-month drawdown

Customer B prepays `$10,000` for one year and receives a stated 20 percent discount. The example issues a `$10,000` `CONTRACT_SCHEDULED` invoice, defers that amount, then issues a zero-dollar `CONTRACT_USAGE` invoice with `$800` of CloudCompute and `$100` of CloudStorage covered by the commit. The ledger starts at `$10,000` and records a `$900` deduction.

The Customer B/contract customer-key conflict described above makes the sample unsafe as a direct join specification.

## Scenario 2b: Prepaid burn-down and expiration

The narrative says the later months burn `$700` total, split `$600` CloudCompute and `$100` CloudStorage. The monthly table and ledger agree on an initial `$900` deduction, eleven later `$700` deductions, and `$1,400` expiration, exactly exhausting the `$10,000` balance.

> [!warning] Recognition-total contradiction
> The conclusion instead assigns `$700` to CloudCompute plus `$100` to CloudStorage for each of months 2–12, totaling `$800` per month. Combined with the stated `$1,400` expiration, those conclusions exceed both the monthly drawdown and original prepaid amount. The source does not identify the corrected product split; do not invent it.

## Scenario 2c: Prepaid burn-down and overage

This alternative reaches `$100` remaining after month 10 and says overage begins in month 11. Its month-11 summary table lists `$1,000` usage, `$900` overage, an `$800` invoice total, and a zero balance, while the detailed invoice total is `$900` and its line items sum to `$900` (`800 + 200 - 100`). Month 12 has no remaining balance and a `$1,000` invoice.

> [!warning] Overage amount and revenue-classification conflicts
> The month-11 `$800` summary invoice conflicts with both its `$900` stated overage and the detailed `$900` invoice. The conclusion labels all `$1,000` in months 11 and 12 as prepaid-commit revenue even though only `$100` remained entering month 11 and the page says overage starts then.
>
> The detailed month-11 gross CloudCompute and CloudStorage rows both carry `commit_id: 50002`, and balance `50002` is labeled `PREPAID`. Under the parent guide's query model, a populated commit ID joins through `balances.type`, while a null commit ID can mean on-demand or overage and still requires client metadata to distinguish those categories. The example therefore calls the detailed rows overage while its own join fields classify them through a prepaid balance. It does not support a corrected allocation or a general overage-classification rule.

## Scenario 3: Postpaid commitment and true-up

Customer C commits to `$10,000`, consumes `$800` per month for twelve months, and reaches `$9,600` cumulative spending. The table then shows a `$400` `CONTRACT_TRUEUP` invoice and records twelve `$800` automated deductions plus a `$400` `postpaid_trueup` ledger entry.

> [!warning] Invoice-label and identifier conflicts
> The invoice table labels the twelve `$800` rows `CONTRACT_SCHEDULED`, but the conclusion calls them usage invoices. The table labels the `$400` row `CONTRACT_TRUEUP`, but the conclusion calls it scheduled. Invoice `30011` is repeated for three periods, and IDs `30002`–`30012` overlap the Customer B examples. Do not infer corrected invoice types or identifiers.

## Parent query rule and double-count boundary

The parent revenue-recognition guide supplies the query rule that the examples omit: when the same amount is already represented in invoice line items under that model, do not add `credit_automated_invoice_deduction`, `prepaid_automated_invoice_deduction`, `postpaid_automated_invoice_deduction`, or `postpaid_trueup` ledger amounts again. It separately includes `prepaid_segment_expiration` because that expiration is not invoiced in the parent's model. Apply these as the parent's documented query filters, not as a universal accounting rule; the parent also records an unresolved ambiguity around postpaid automated deductions and true-up line items.

This boundary is crucial because each CloudNet scenario presents invoice line items beside ledger deductions. Summing both without the parent's exclusions would double count amounts already represented through line items.

## Accounting and implementation boundaries

- Metronome's examples and parent query model do not determine whether revenue is earned under GAAP, IFRS, or a merchant's contract-specific policy.
- Invoice issuance, zero-dollar invoices, drawdown, expiration, and true-up do not by themselves prove performance-obligation satisfaction, allocation, variable-consideration treatment, collectibility, breakage policy, or posting approval.
- The examples omit voids, regeneration, refunds, credit memos, corrections, restatements, payment state, taxes, foreign currency, close cutoffs, reconciliation tolerances, and auditor approval.
- Because IDs, fields, totals, and classifications conflict, implementers should rebuild control totals from current exported records and reconcile invoices, line items, and ledgers before relying on recognition output. Do not invent corrected sample values.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-reporting-and-analytics]], [[metronome-credits-and-commits]], [[metronome-invoicing]], [[payment-reconciliation-reporting]]
- Related sources: [[source-metronome-guides-reporting-insights-financial-reporting-revenue-recognition]], [[source-metronome-guides-reporting-insights-financial-reporting-reconcile-data]], [[source-metronome-guides-reporting-insights-data-export-database-reference]]

## Raw Sources

- [[raw/metronome/guides/reporting-insights/financial-reporting/revenue-recognition-examples-2026-07-13|2026-07-13 snapshot — complete CloudNet export examples for on-demand, prepaid, expiration, overage, and postpaid true-up reporting]]
