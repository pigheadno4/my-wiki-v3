---
title: "Braintree Settlement Batch Summary Response (Node.js)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/response/settlement-batch-summary/node"
raw_files:
  - "braintree/docs/reference/response/settlement-batch-summary/node-2026-09-16.md"
tags: [braintree, node-js, settlement, reporting, response-objects]
---

## Overview

This collected Braintree Node.js website response reference shows callback and Promise examples that generate a Settlement Batch Summary and read `result.settlementBatchSummary.records`, followed by an example records data structure. It is an example-oriented response route, not a complete response schema or proof of report availability, generation, settlement, funding or reconciliation.

## Key takeaways

- Both displayed server-side Node.js examples call `gateway.settlementBatchSummary.generate()` with a `settlementDate` and `groupByCustomField`, then access `result.settlementBatchSummary.records`. They illustrate callback and Promise consumption; they do not establish parameter requiredness, validation behavior, an exact SDK package or version, or successful execution for a particular account.
- The displayed records array contains example keys for the selected custom field, card type, count, merchant account ID, transaction kind and settled amount. The page explicitly labels the structure an example, so it does not establish a closed field inventory, field requiredness, types, completeness, grouping semantics, or values returned for every merchant or batch.
- This response page does not define client-side behavior, account or processor eligibility, settlement-batch generation semantics, transaction lifecycle transitions, report history or current support. The separate generate request reference owns the documented date-scoped reporting purpose; neither page is proof that transactions settled, funds were disbursed or a reconciliation completed.

## Detail locators

- Callback invocation and `records` access: `# Settlement Batch Summary > ## Examples > ### Generating Settlement Batch Summary > ### Callbacks`, lines 23-31.
- Promise invocation and `records` access: `# Settlement Batch Summary > ## Examples > ### Generating Settlement Batch Summary > ### Promises`, lines 33-41.
- Example-only records-data-structure qualification: `# Settlement Batch Summary > ## Examples > ### Records data structure`, lines 43-46.
- Displayed example record keys and values: `# Settlement Batch Summary > ## Examples > ### Records data structure > ### JSON`, lines 47-66.

## Evidence boundaries

> [!warning] Example response data is not settlement or reconciliation proof
> Preserve the page's example-only scope. The snapshot does not establish exact Node.js package behavior, current SDK or account support, response completeness, successful report generation, transaction-level settlement, later funding or completed reconciliation.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]
- Reporting context: [[payment-reconciliation-reporting]]
- Request and purpose route: [[source-braintree-settlement-batch-summary-generate-node]]

## Raw Sources

- [[raw/braintree/docs/reference/response/settlement-batch-summary/node-2026-09-16|Braintree Settlement Batch Summary response reference - Node.js]] - complete collected page containing callback and Promise usage examples plus an example records structure
