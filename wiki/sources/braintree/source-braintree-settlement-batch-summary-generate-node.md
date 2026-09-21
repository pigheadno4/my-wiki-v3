---
title: "Braintree Settlement Batch Summary Generate (Node.js)"
type: source
date_ingested: 2026-09-21
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/settlement-batch-summary/generate/node"
raw_files:
  - "braintree/docs/reference/request/settlement-batch-summary/generate/node-2026-09-16.md"
tags: [braintree, node-js, settlement, reporting, reconciliation]
---

## Overview

This Braintree Node.js reference documents generating a settlement batch summary that displays total sales and credits for each batch for a particular date. It is a reporting operation, distinct from submitting an individual transaction for settlement.

## Key takeaways

- The summary is scoped to a particular settlement date and displays total sales and credits for each batch. The page says transactions can be grouped by the values of one custom field.
- The callback and Promise examples pass a `settlementDate` and a `groupByCustomField` value to `gateway.settlementBatchSummary.generate()`, then access `result.settlementBatchSummary.records`. These are displayed examples, not a complete request or response schema.
- Calling the method with incorrect arguments may produce validation errors; the linked validation-error reference owns the detailed failures.
- This page does not document `transaction.submitForSettlement()` or establish transaction-level settlement eligibility, state changes, or submission effects.

## Detail locators

- Settlement Batch Summary response-object route: `# Settlement Batch Summary: Generate`, line 15.
- Date, batch totals and single-custom-field grouping scope: `# Settlement Batch Summary: Generate`, line 17.
- Callback request example and records access: `# Settlement Batch Summary: Generate > ### Callback`, lines 18-26.
- Promise request example and records access: `# Settlement Batch Summary: Generate > ### Promise`, lines 28-36.
- Incorrect-argument validation-error route: `# Settlement Batch Summary: Generate > #### Validation Errors`, lines 38-40.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]
- Supporting concept: [[payment-reconciliation-reporting]]

## Related raw API references

- [[raw/braintree/docs/reference/response/settlement-batch-summary/node-2026-09-16|Braintree Node.js Settlement Batch Summary response reference]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/articles/control-panel/custom-fields-2026-09-16|Braintree Control Panel custom-fields article]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/reference/general/validation-errors/all/node-2026-09-16|Braintree Node.js validation-error reference]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/reference/request/transaction/submit-for-settlement/node-2026-09-16|Braintree Node.js transaction submit-for-settlement request]] - navigation only; separate operation not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/reference/request/settlement-batch-summary/generate/node-2026-09-16|Braintree Node.js Settlement Batch Summary generate reference]] - complete collected page covering date-scoped batch totals, single-custom-field grouping, callback and Promise records access, and validation routing
