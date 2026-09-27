---
title: "Braintree Control Panel Transaction Summary"
type: source
date_ingested: 2026-09-26
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/control-panel/reporting/transaction-summary"
raw_files:
  - "braintree/articles/control-panel/reporting/transaction-summary-2026-09-16.md"
tags: [braintree, control-panel, reporting, transaction-status, reconciliation]
---

## Overview

This collected Braintree article documents the Control Panel Transaction Summary, a high-level, Dashboard-like report of transactions currently categorized as successful or unsuccessful within a selected date range. It supports processing-trend analysis rather than reconciliation.

## Key takeaways

- The report can be run for a selected date range and grouped according to the user's chosen fields.
- In the results table, the selected Group by fields form the rows and transaction statuses form the columns. Displayed amounts represent transactions currently in each status.
- **Do not use current status categorization for reconciliation.** Braintree warns that transaction statuses can change, so the Transaction Summary is a trend-identification tool rather than a reconciliation record.

## Detail locators

- High-level purpose, current successful/unsuccessful categorization and Dashboard comparison: `# Transaction Summary`, line 16.
- Processing-trend use and reconciliation warning: `# Transaction Summary`, line 18.
- Grouping and date-range controls: `## Running a Transaction Summary`, lines 21-29.
- Row, column and current-status amount semantics: `## Interpreting Transaction Summary results`, lines 32-36.

## Evidence boundary

> [!warning] Current categorization is not reconciliation
> The displayed amounts reflect transactions currently in their statuses, and those statuses can change. This collected 2026-09-16 page does not establish settlement, funding, or reconciliation finality.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-control-panel]]
- Supporting concept: [[payment-reconciliation-reporting]]

## Raw Sources

- [[raw/braintree/articles/control-panel/reporting/transaction-summary-2026-09-16|Braintree Control Panel Transaction Summary]] - complete collected article covering report purpose, filters, grouping, status-based results and the reconciliation warning
