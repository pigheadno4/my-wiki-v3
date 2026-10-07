---
title: "Braintree Settlement Batch Summaries Guide (Node.js)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/reports/settlement-batch-summaries/node"
raw_files:
  - "braintree/docs/guides/reports/settlement-batch-summaries/node-2026-09-16.md"
tags: [braintree, node-js, reporting, settlement, reconciliation]
---

## Overview

This collected Braintree Node.js website guide describes generating a Settlement Batch Summary whose records report total sales and credits for each batch for a particular settlement date. The guide documents a reporting action through `gateway.settlementBatchSummary.generate()`; it does not document submitting an individual transaction for settlement.

## Key takeaways

- The summary is scoped to a particular settlement date and reports total sales and credits for each batch.
- Callback and Promise examples call `gateway.settlementBatchSummary.generate()` and access `result.settlementBatchSummary.records`. These are Node.js examples, not a complete SDK contract or proof that a report was generated for an account.
- `groupByCustomField` is optional. The guide says transactions can be grouped by one custom field's values; grouping is not a prerequisite for generating the summary.
- The records section is expressly an example data structure. It displays `custom_field_1`, `card_type`, `count`, `merchant_account_id`, `kind`, and `amount_settled`; the page does not establish that every field is required or returned for every account or record.
- The page does not state a timezone or batch-day cutoff, account eligibility or merchant-account selection behavior, report completeness guarantee, or any transaction settlement, funding, disbursement, or deposit effect. This unversioned website snapshot is also distinct from versioned Braintree Node SDK or GitHub implementation evidence.

## Detail locators

- Report purpose, per-date batch totals, and single-custom-field grouping: `# Settlement Batch Summaries`, line 16.
- Callback invocation and records access: `# Settlement Batch Summaries > ### Callback`, lines 19-24.
- Promise invocation and records access: `# Settlement Batch Summaries > ### Promise`, lines 29-34.
- Settlement-date parameter meaning and optional grouping parameter: `# Settlement Batch Summaries > ## Parameters`, lines 40-41.
- Example-only qualification and displayed record fields: `# Settlement Batch Summaries > ## Records data structure`, lines 44-67.

## Related

- Company: [[braintree]]
- Main concept: [[payment-reconciliation-reporting]]
- Supporting concept: [[braintree-server-sdk]]
- Related request reference: [[source-braintree-settlement-batch-summary-generate-node]]

## Related raw API references

- [[raw/braintree/articles/control-panel/custom-fields-2026-09-16|Braintree Control Panel custom-fields article]] - navigation only; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/guides/reports/settlement-batch-summaries/node-2026-09-16|Braintree Node.js Settlement Batch Summaries guide]] - fully read collected webpage covering the report purpose, date and optional grouping parameters, callback and Promise examples, and example records structure
