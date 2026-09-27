---
title: "Braintree Control Panel Reporting Overview"
type: source
date_ingested: 2026-09-26
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/control-panel/reporting/overview"
raw_files:
  - "braintree/articles/control-panel/reporting/overview-2026-09-16.md"
  - "braintree/articles/control-panel/reporting/transaction-level-fee-report-2026-09-16.md"
tags: [braintree, control-panel, reporting, reconciliation, settlement, transaction-fees]
---

## Overview

This collected Braintree article is a routing overview for reporting options in the Control Panel. It groups decline, card-expiry, settlement-batch, transaction-fee, transaction-summary, tax-form and statement reporting while qualifying availability by account setup, business location and, for some reports, merchant or pricing eligibility.

## Key takeaways

- Available Control Panel reports depend on the merchant's account setup and business location. The page directs readers who see an unlisted report in their Control Panel to Braintree for additional information.
- **Decline Analysis** uses Advanced Search results to analyze decline rates and can sort declines by processor response or bank identification number. **Expiring Cards** covers cards in the Vault that are expired or will expire within a selected time range.
- **Settlement Batch Summary** lists the transactions processed in a settlement batch by payment method and can be emailed automatically to Control Panel users. Use the linked report page for report-specific behavior.
- The **Transaction-Level Fee report** provides a transaction-level breakdown of assessed fees. This overview limits it to US merchants on IC+ and blended or flat-rate pricing models.
- **Transaction Summary** separates transactions currently categorized as successful or unsuccessful for a date range and is presented as a processing-trend aid. The **1099-K** entry is limited to applicable Braintree Direct merchants domiciled in the US and is described as required for tax purposes.
- Statement availability depends on account setup and company country. Statements often contain pricing, fee, processing and disbursement details and may help with reconciliation. This overview contains no Dashboard discussion and therefore establishes no Dashboard-versus-reconciliation rule; the separate [[source-braintree-control-panel-overview]] is the retrieval route for Dashboard behavior.

> [!warning] Collected eligibility conflict
> This overview states that the Transaction-Level Fee report is available to US merchants only (overview raw lines 39-44), while the dedicated [[source-braintree-control-panel-reporting-transaction-level-fee-report|Transaction-Level Fee Report]] says it is available by default to US- and Australia-based merchants on IC+ and to US-, Australia-, and Brazil-based merchants on flat-rate or blended pricing (dedicated raw lines 17-18). Both pages were collected on 2026-09-16; neither establishes current eligibility.

## Detail locators

- Report availability qualification and unlisted-report support route: `# Overview`, line 16.
- Decline Analysis purpose and sort categories: `## Decline analysis`, lines 19-23.
- Vault-card time-range scope: `## Expiring cards`, lines 26-29.
- Settlement-batch transaction grouping and automatic email option: `## Settlement Batch Summary`, lines 32-36.
- Transaction-Level Fee report geography, purpose and pricing-model eligibility: `## Transaction-Level Fee report`, lines 39-44.
- Transaction Summary status grouping, date range and trend purpose: `## Transaction Summary`, lines 47-51.
- 1099-K merchant/location qualification and tax-purpose statement: `## 1099-K`, lines 54-58.
- Statement availability, content categories and qualified reconciliation use: `## Statements`, lines 61-70.

## Evidence boundary

> [!warning] Reporting overview, not Dashboard evidence
> This page supplies report categories and the qualifications stated above. It does not mention the Dashboard, and "may help with reconciliation" does not establish that a statement is sufficient for reconciliation. Treat the 2026-09-16 raw as collected evidence rather than proof of current availability, and follow the dedicated report pages for report-specific behavior.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-control-panel]]
- Supporting concept: [[payment-reconciliation-reporting]]
- Separate Dashboard source: [[source-braintree-control-panel-overview]]

## Related raw API references

- [[raw/braintree/articles/control-panel/reporting/decline-analysis-2026-09-16|Braintree Decline Analysis article]] - unread navigation-only report detail; not used as factual evidence here
- [[raw/braintree/articles/control-panel/reporting/expiring-cards-2026-09-16|Braintree Expiring Cards article]] - unread navigation-only report detail; not used as factual evidence here
- [[raw/braintree/articles/control-panel/reporting/settlement-batch-summary-2026-09-16|Braintree Settlement Batch Summary article]] - unread navigation-only report detail; not used as factual evidence here
- [[raw/braintree/articles/control-panel/reporting/transaction-summary-2026-09-16|Braintree Transaction Summary article]] - unread navigation-only report detail; not used as factual evidence here
- [[raw/braintree/articles/control-panel/reporting/1099-k-2026-09-16|Braintree 1099-K article]] - unread navigation-only report detail; not used as factual evidence here

## Raw Sources

- [[raw/braintree/articles/control-panel/reporting/overview-2026-09-16|Braintree Control Panel Reporting Overview]] - complete collected overview covering report categories, stated eligibility qualifications and the limited statement-reconciliation route
- [[raw/braintree/articles/control-panel/reporting/transaction-level-fee-report-2026-09-16|Braintree Transaction-Level Fee Report article]] - complete collected dedicated page used to document the country-eligibility conflict
