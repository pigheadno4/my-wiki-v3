---
title: "Braintree Control Panel Settlement Batch Summary"
type: source
date_ingested: 2026-09-26
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/control-panel/reporting/settlement-batch-summary"
raw_files:
  - "braintree/articles/control-panel/reporting/settlement-batch-summary-2026-09-16.md"
tags: [braintree, control-panel, reporting, settlement, reconciliation]
---

## Overview

This Braintree Control Panel article documents the Settlement Batch Summary report for processor settlement batches. The report displays total sales and credits per batch and can be scoped by date range, merchant account, and payment-type exclusions; it is a reporting view, not evidence of an API response or completed bank funding.

## Key takeaways

- Braintree describes settlement batches as groups of transactions submitted for settlement and sent to processors. The report totals sales and credits for each batch; its controls can narrow results by date range, merchant account, and excluded payment types.
- Access requires the Create, Run, and Download Reports role permission. Settlement Batch Summaries are unavailable for marketplace sub-merchant accounts, and CSV downloads are limited to 40,000 rows.
- PayPal transactions can be excluded to better reconcile this report with Braintree disbursements. For merchants using their own American Express account, excluding Amex may help because those funds are not included in Braintree deposits. These statements distinguish report reconciliation from proof that a batch or transaction has funded.
- The cutoff deciding which transactions enter a batch depends on the account setup and cannot be changed. The article does not provide a universal cutoff time or document individual transaction settlement-state transitions.
- A Control Panel user can opt into a daily Settlement Batch Summary email and optionally include a card-type breakdown. A user with Manage Users permission can enable the daily email for another user.

> [!warning] Report, API, and funding boundaries
> This page documents a Control Panel report and email delivery settings. It does not document the Node.js Settlement Batch Summary API response, settlement submission, final transaction status, or a ledger of deposits arriving at a merchant's bank.

## Detail locators

- Batch meaning, totals, and report-scope controls: `# Settlement Batch Summary`, line 16.
- Required report permission and Control Panel run/download steps: `## Running a Settlement Batch Summary`, lines 21-31.
- Marketplace sub-merchant unavailability: `## Running a Settlement Batch Summary > NOTE`, lines 34-35.
- PayPal-disbursement and own-Amex-account deposit reconciliation boundaries: `### Excluding PayPal or American Express transactions`, lines 40-42.
- Account-dependent, unchangeable batch cutoff: `### Settlement batch cutoff times`, lines 45-47.
- Per-user daily email, optional card-type breakdown, and Manage Users administration: `## Emailing Settlement Batch Summaries`, lines 50-72.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-control-panel]]
- Supporting concept: [[payment-reconciliation-reporting]]
- Separate Node.js API reporting route: [[source-braintree-settlement-batch-summary-generate-node]]

## Raw Sources

- [[raw/braintree/articles/control-panel/reporting/settlement-batch-summary-2026-09-16|Braintree Control Panel Settlement Batch Summary article]] - complete collected page covering batch totals, report access and filters, exclusions, cutoff behavior, availability, and daily email settings
