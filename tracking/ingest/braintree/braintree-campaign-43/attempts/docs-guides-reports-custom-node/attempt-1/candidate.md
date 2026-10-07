---
title: "Braintree Custom Reports (Node.js)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/reports/custom/node"
raw_files:
  - "braintree/docs/guides/reports/custom/node-2026-09-16.md"
tags: [braintree, reporting, custom-reports, nodejs]
---

## Overview

This 2026-09-16 capture is the unversioned Braintree Node.js website guide for merchant-built custom reporting. It says merchants can generate custom reports through the Braintree API after integrating with Braintree, and presents a sample transaction-search-to-CSV pattern rather than a complete or guaranteed reporting service. See [[braintree]] and [[payment-reconciliation-reporting]].

## Key takeaways

- The sample workflow searches transactions through the Braintree API, iterates over the results, selects transaction values, and writes one CSV row per transaction.
- Setup is merchant-owned: the page directs the reader to supply API keys, choose output fields, consult response-object references for more values, and adjust the search date range. The displayed Node example uses Sandbox placeholders and a settled-date window; it is explicitly one sample among many, not a production prescription.
- Transaction searches are capped at 50,000 results, while all other searches are capped at 10,000 results. A report design must keep those search-result ceilings in view.
- This snapshot does not establish current merchant-account eligibility, report or field availability, successful report generation, completeness of the output, or any payment, authorization, settlement, disbursement, or funding outcome.

## Detail locators

- Custom-report purpose, post-integration starting condition, and Braintree recommendation: `# Custom`, lines 14-20.
- Sample search, iteration, CSV-row workflow, and merchant setup choices: `## Sample reporting script` and `### Remember to`, lines 25-41.
- Node.js example, including gateway placeholders, search window, CSV headers, stream handling, and illustrative settlement-amount access: `### Node`, lines 46-121.
- Result ceilings: `## Search limit`, lines 123-125.
- Linked reference navigation: `## See also`, lines 128-136.

## Related

- [[braintree]]
- [[payment-reconciliation-reporting]]
- [[braintree-server-sdk]]
- [[source-braintree-transaction-search-node]]
- [[source-braintree-search-fields-node]]
- [[source-braintree-search-results-node]]

## Related raw API references

- [[raw/braintree/docs/reference/request/transaction/search/node-2026-09-16|Transaction search (Node.js)]]
- [[raw/braintree/docs/reference/request/customer/search/node-2026-09-16|Customer search (Node.js)]]
- [[raw/braintree/docs/reference/general/searching/search-fields/node-2026-09-16|Search fields (Node.js)]]
- [[raw/braintree/docs/reference/general/searching/search-results/node-2026-09-16|Search results (Node.js)]]

## Raw Sources

- [[raw/braintree/docs/guides/reports/custom/node-2026-09-16|Braintree Custom Reports (Node.js), captured 2026-09-16]]
