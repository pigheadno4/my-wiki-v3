---
title: "Braintree Transaction-Level Fee Report"
type: source
date_ingested: 2026-09-26
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/control-panel/reporting/transaction-level-fee-report"
raw_files:
  - "braintree/articles/control-panel/reporting/transaction-level-fee-report-2026-09-16.md"
tags: [braintree, control-panel, reporting, transaction-fees, reconciliation]
---

## Overview

This collected Braintree article documents the Control Panel Transaction-Level Fee Report: a downloadable view of transaction and fee information whose contents, availability timing, and reconciliation suitability depend on the merchant's pricing model. In this 2026-09-16 snapshot, the report is available by default to US and Australia merchants on IC+ and to US, Australia, and Brazil merchants on flat-rate or blended pricing.

## Key takeaways

- Access requires the `Create, Run, and Download Reports` role permission. The documented flow selects a merchant account and date range, runs the report, and downloads the resulting file.
- The report covers credit and debit cards, Venmo, Apple Pay, and Google Pay. It excludes American Express transactions processed directly through Amex and all PayPal transactions.
- For flat-rate and blended pricing, the report contains the actual Braintree fees charged per transaction. An individual transaction becomes available three calendar days after its settled amount is disbursed to the merchant's bank account, and Braintree identifies transaction-level reconciliation as one use.
- For IC+ pricing, the report contains interchange estimates and must not be used for reconciliation. An individual transaction becomes available five calendar days after its settled amount is disbursed to the merchant's bank account. The article explains that interchange estimates can be reclassified and that actual interchange fees are passed through as a consolidated month-end sum, so exact transaction-level interchange assessments are unavailable.

> [!warning] Report and money-movement boundary
> The article uses disbursement of the settled amount as the clock for report-data availability. It does not make this report a settlement-status or merchant-account funding ledger, and it does not document settlement or bank-disbursement mechanics. Reconciliation suitability is pricing-model-specific: flat-rate and blended reporting is presented for transaction-level reconciliation, while IC+ estimates are explicitly not.

> [!info] Collected snapshot
> The raw page was fetched on 2026-09-16 and carries page metadata dated 2025-04-02. Those dates preserve provenance; they do not establish current availability, pricing-model eligibility, or report behavior.

## Detail locators

- Default country and pricing-model availability: `# Transaction-Level Fee Report > AVAILABILITY`, lines 17-18.
- Purpose, pricing-model dependency, and supported payment methods: `# Transaction-Level Fee Report`, lines 22-30.
- Required report permission and Control Panel run/download flow: `## Running a Transaction-Level Fee report`, lines 33-43.
- Direct-Amex and PayPal exclusions: `## Running a Transaction-Level Fee report > NOTE`, lines 46-47.
- Flat-rate/blended actual-fee scope, three-calendar-day timing, and transaction-level reconciliation use: `## Flat rate and blended pricing models`, lines 52-63.
- IC+ estimate warning, reported fee categories, five-calendar-day timing, and IC+-priced Venmo qualification: `## IC+ pricing models`, lines 66-87.
- Reclassification, consolidated month-end pass-through, unavailable exact transaction-level interchange assessments, and the no-reconciliation instruction: `### Interchange fee estimates`, lines 101-105.

## Related

- Company: [[braintree]]
- Main concepts: [[braintree-control-panel]], [[payment-reconciliation-reporting]]

## Raw Sources

- [[raw/braintree/articles/control-panel/reporting/transaction-level-fee-report-2026-09-16|Braintree Transaction-Level Fee Report article]] - complete collected page covering availability, permissions, included and excluded payment methods, pricing-model-specific report contents, timing, and reconciliation limits
