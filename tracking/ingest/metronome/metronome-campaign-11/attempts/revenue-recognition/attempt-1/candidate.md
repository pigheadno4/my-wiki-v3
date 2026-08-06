---
title: "Metronome Revenue Recognition Data Model"
type: source
date_ingested: 2026-08-01
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/reporting-insights/financial-reporting/revenue-recognition"
raw_files:
  - "metronome/guides/reporting-insights/financial-reporting/revenue-recognition-2026-07-13.md"
tags: [metronome, revenue-recognition, financial-reporting, data-export, invoices, credits-and-commits]
---

## Overview

This guide describes the Metronome billing data and query relationships that merchants can use in downstream revenue-recognition workflows for usage-based business models. It maps revenue categories to invoices, line items, balance types, and selected credit and commit ledger entries, and distinguishes finalized-invoice reporting from draft-invoice accrual reporting. Metronome supplies the underlying data through APIs or Data Export but explicitly does not create revenue journal entries.

## Key takeaways

- Metronome says it retains transaction history and ledgers with daily granularity by product and revenue category for downstream reporting through its APIs or Data Export; the merchant or its downstream system remains responsible for journal entries.
- The guide separates on-demand usage, prepaid-commit drawdown, postpaid-commit drawdown, overage, and credit drawdown, with further product-level categorization.
- In the guide's model, prepaid purchases are deferred when invoiced and recognized on drawdown or expiration, while postpaid usage is recognized on drawdown and any remainder on true-up invoicing. These are Metronome's documented reporting treatments, not an independent accounting-policy determination.
- When invoice `line_items` already carry the amount, several automated deduction and true-up ledger entries must be ignored to avoid duplication; prepaid segment expiration is the stated exception because Metronome does not invoice that expiration.
- The page maps `FINALIZED` invoices to recognized-revenue reporting and `DRAFT` invoices to accrued-revenue reporting, but it does not establish that invoice status alone satisfies a particular accounting standard, audit, or close procedure.

## Revenue categories and documented timing

| Category | Metronome's documented reporting treatment |
| --- | --- |
| On-demand usage | Invoiced as consumption occurs; the guide says revenue can be recognized when the invoice is issued. |
| Prepaid commit purchase | Invoiced in advance and associated revenue is deferred. |
| Prepaid commit drawdown | Usage invoices draw down the balance; the guide says revenue is recognized as drawdown occurs. |
| Prepaid commit expiration | Unused value expires at period end; the guide calls this a prepaid-commit true-up and says revenue is recognized at expiration. |
| Postpaid commit drawdown | Actual monthly consumption draws down the minimum-spend commitment and is reported as revenue as it is consumed. |
| Postpaid true-up | If actual spend is below the commitment, Metronome invoices the difference at period end; the guide says revenue is recognized when that true-up invoice is issued. |
| Overage | Consumption above the commitment is invoiced as it occurs and reported as revenue upon invoicing. |
| Free-credit drawdown | Free credits do not affect deferred revenue because they are not paid for, but their drawdown may have a contra-revenue effect. |

The guide says all Metronome usage charges are billed in arrears, with monthly, quarterly, and annual options, while scheduled charges for prepaid-commit purchases are billed in advance and generally treated as deferred revenue. It defines accrued revenue as earned but not yet invoiced or paid and represents it in Metronome through draft usage invoices containing rated but not-yet-invoiced usage events.

The source repeatedly says a merchant is "entitled" to recognize specified amounts and uses "generally" for scheduled-charge deferral. It does not identify an accounting standard or address contract-specific performance obligations, allocation, variable consideration, breakage policy, material rights, collectibility, currency conversion, tax, refunds, credit memos, corrections, or auditor approval. Merchants should therefore treat the timing above as provider documentation for constructing reports, not as a substitute for their accounting policy.

## Ledger and invoice query model

Data Export consolidates credit and commit objects into `balances`. For credit ledgers, `credit_automated_invoice_deduction` reduces the balance from an invoice and should be ignored when reporting from `line_items` on `CONTRACT_USAGE` invoices because the revenue is already present there. The guide says `credit_segment_expiration` is usually ignored because free-credit expiration does not affect revenue.

For commit ledgers, the documented treatments are:

- Ignore `prepaid_automated_invoice_deduction` when using `line_items` from `CONTRACT_USAGE` invoices because the amount is already included.
- Include `prepaid_segment_expiration`; the guide says prepaid expiration is not invoiced by Metronome and should always be recognized in this reporting model.
- Ignore `postpaid_automated_invoice_deduction` when using `line_items` from `CONTRACT_TRUEUP` invoices because the page says the amount is already included there.
- Ignore `postpaid_trueup` when reporting from `line_items` because the amount would be duplicated.

> [!warning] Documentation ambiguity
> The guide separately says postpaid usage is recognized as the commitment draws down each month, but its ledger rule associates `postpaid_automated_invoice_deduction` duplication with `CONTRACT_TRUEUP` line items while reserving that invoice type for end-of-period true-up charges. It does not reconcile whether the automated deduction represents monthly drawdown, true-up, or both. Preserve the literal filter conditions and verify the current export schema and sample data before implementing the query.

The invoice types used by the guide are `CONTRACT_SCHEDULED` for scheduled charges including prepaid purchases, `CONTRACT_USAGE` for usage charges, and `CONTRACT_TRUEUP` for postpaid true-up charges. The page says each invoice has one or more line items. The separate Data Export database reference documents that a `DRAFT_INCOMPLETE` row can temporarily have no total or line items, so the broad statement here should not be generalized to every exported draft state. `invoices.credit_type_id` identifies billing currency, and invoice start and end timestamps identify the service period that the guide maps to the target ERP accounting period. `line_items.product_id` identifies the invoiced product and can map to an ERP SKU or line-item identifier.

When `line_items.commit_id` is populated, the guide joins it to `balances.id`; `balances.type` then classifies the line-item amount as `credit`, `prepaid`, or `postpaid`. When `commit_id` is null, the amount is either on-demand or overage revenue, and client-defined metadata on contracts or commits must distinguish those two categories. The page does not define required metadata keys, completeness checks, or behavior when the metadata is absent or inconsistent.

## Status, export, and accounting boundaries

The guide says filtering invoices to `status = 'FINALIZED'` produces a recognized-revenue report and filtering to `status = 'DRAFT'` produces an accrued-revenue report. Data Export transfers finalized and draft invoices in distinct tables. This page does not define how voids, regeneration, post-finalization corrections, credit memos, refunds, disputes, downstream payment state, or historical restatements alter those reports, and it does not reconcile the status labels with an ERP posting state.

The page also does not specify API pagination, export cadence, freshness, snapshot selection, duplicate-delivery handling, close cutoffs, query examples, journal-entry construction, debits and credits, control totals, reconciliation tolerances, or sign-off. Separate Data Export documentation establishes table-specific grains and delivery caveats, so the simplified relationships here should not be treated as proof that a query is complete, current, duplicate-free, or accounting-correct.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-reporting-and-analytics]], [[metronome-invoicing]], [[metronome-credits-and-commits]], [[payment-reconciliation-reporting]]
- Related sources: [[source-metronome-guides-reporting-insights-data-export-overview]], [[source-metronome-guides-reporting-insights-data-export-database-reference]], [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-create-a-pre-paid-commit]], [[source-metronome-guides-invoices-overview]]

## Raw Sources

- [[raw/metronome/guides/reporting-insights/financial-reporting/revenue-recognition-2026-07-13|2026-07-13 snapshot - revenue categories, ledger treatment, invoice classification, and journal-entry boundary]]
