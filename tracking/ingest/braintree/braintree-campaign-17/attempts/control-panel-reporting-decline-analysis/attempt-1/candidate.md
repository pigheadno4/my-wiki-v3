---
title: "Braintree Control Panel Decline Analysis"
type: source
date_ingested: 2026-09-27
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/control-panel/reporting/decline-analysis"
raw_files:
  - "braintree/articles/control-panel/reporting/decline-analysis-2026-09-16.md"
tags: [braintree, control-panel, reporting, decline-analysis, transaction-search, processor-declines]
---

## Overview

This collected Braintree article describes a Control Panel workflow for finding processor-declined transactions and analyzing downloaded search results. Its two main analysis views group decline data by processor response or by the card's bank identification number (BIN); it is not a source of transaction-retry rules.

## Key takeaways

- Braintree says it monitors decline rates and may notify a merchant of unusual activity, while merchants can proactively run an advanced search for declined transactions and analyze the results.
- The documented search selects `Processor Declined`, allows a date-range adjustment, and can download the results as CSV. If expected declines are absent and card verification is in use, the article directs the reader to a separate verification search.
- For a processor-response view, the article suggests a pivot table filtered by `Processor Response Text` and routes response meanings to separate developer documentation. Repeated attempts with the same payment method can skew the observed decline rate, so the article suggests removing duplicate CSV values to view unique declines more clearly.
- For a BIN view, the article suggests a pivot table filtered by `First Six of Credit Card`, followed by BIN lookup to investigate patterns by card type, location, possible prohibited transactions, or issuing bank.
- More customer-transaction data can make the analysis more useful; the page gives cardholder names and email addresses as examples. It separately points fraudulent-transaction decline reduction to Braintree Fraud Tools, but does not define retry eligibility, timing, or advice.

## Detail locators

- Monitoring and proactive decline-analysis purpose: `# Decline Analysis`, line 16.
- Processor-declined search, date range, and CSV download: `## Running a decline search`, lines 21-30.
- Card-verification search boundary: `## Running a decline search`, lines 33-34.
- Data-volume and customer-data qualification: `## Analyzing the results`, line 41.
- Processor-response pivot view and separate response-meaning route: `### Processor responses`, line 46.
- Duplicate-attempt skew and unique-decline cleanup: `### Processor responses`, line 48.
- BIN trend view and possible pattern categories: `### Bank identification numbers`, lines 53-57.
- Fraud-tools route: `## Reducing declines`, lines 60-62.

## Evidence boundary

> [!warning] Analysis workflow, not retry guidance
> This page describes how to search and inspect decline data. It does not say whether, when, or how a declined transaction should be retried. Card-verification declines may require the separate verification search, and repeated attempts with one payment method can distort the decline-rate view. Treat the 2026-09-16 raw as collected evidence rather than proof of current Control Panel behavior.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-control-panel]]
- Supporting concept: [[payment-reconciliation-reporting]]

## Raw Sources

- [[raw/braintree/articles/control-panel/reporting/decline-analysis-2026-09-16|Braintree Control Panel Decline Analysis]] - complete collected article covering the processor-declined search, processor-response and BIN analysis views, and their stated limits
