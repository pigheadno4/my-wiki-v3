---
title: "Braintree PayPal Funding and Reconciliation"
type: source
date_ingested: 2026-09-29
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/guides/payment-methods/paypal/funding-reconciliation"
raw_files:
  - "braintree/articles/guides/payment-methods/paypal/funding-reconciliation-2026-09-16.md"
tags: [braintree, paypal, funding, reconciliation, reporting, control-panel]
---

## Overview

This pinned Braintree article distinguishes where PayPal transaction funds go from the reports and identifiers used to reconcile them. It is a retrieval route for the PayPal Business Account balance, optional bank withdrawal paths, report selection and the PayPal-to-Braintree transaction-ID crosswalk; it does not establish that a gateway transaction status proves an individual withdrawal or bank deposit.

## Key takeaways

- Using PayPal does not change the funding process for credit-card transactions. By default, PayPal funds PayPal transactions to the merchant's PayPal Business Account balance, from which the merchant can withdraw manually or ask PayPal to configure Settlement Withdrawal.
- The article says Settlement Withdrawal automatically sends the previous day's transactions to the merchant's bank within 2-3 business days and provides a daily PayPal-console report for the transactions included in each withdrawal. This page-level timing is not proof that a specific transaction funded or that a bank received a deposit.
- For reconciliation, the article points larger merchants to PayPal Transaction Details and Settlement reports, smaller and medium merchants to the PayPal Monthly Financial Summary, and merchants of any size to using those reports with Braintree's Settlement Batch Summary. The linked reports retain their own scope and authority.
- For a specific PayPal transaction, the article recommends the PayPal console because it exposes details such as assessed fees and net deposit amount that are absent from the Braintree Control Panel. Searches can use the customer's PayPal email address or PayPal Transaction ID.
- The PayPal Transaction ID maps to Braintree's Authorization Unique Transaction ID and is distinct from the Braintree transaction ID. The article also links to Braintree transaction search as an alternative lookup route without claiming that search results prove funding.

## Evidence boundaries

> [!warning] Processing status, report records and funding proof are distinct
> A Braintree transaction ID or gateway lifecycle status is not the PayPal Transaction ID, and neither a transaction record nor a settlement-batch report alone proves that an individual PayPal withdrawal reached a bank account. Preserve the article's PayPal Business Account, Settlement Withdrawal, report and identifier boundaries when investigating money movement.

> [!warning] Snapshot and linked-authority boundary
> The 2026-09-16 snapshot records the article's stated 2-3-business-day Settlement Withdrawal timing and report recommendations. It does not establish present merchant eligibility, current report behavior or a guaranteed deposit time; follow the linked PayPal and Braintree authorities for operational details.

## Detail locators

- Credit-card funding non-effect: `## Funding > NOTE`, lines 20-21.
- Default PayPal Business Account balance, manual withdrawal, Settlement Withdrawal setup, previous-day transfer timing and daily withdrawal report: `## Funding`, lines 25-31.
- Merchant-size report recommendations and use with Braintree Settlement Batch Summary: `## Reconciliation`, lines 34-38.
- PayPal-console-only fee and net-deposit detail, search keys and identifier crosswalk: `### Searching for specific transactions`, lines 41-45.
- Braintree Control Panel lookup steps and alternative API transaction-search route: `### Searching for specific transactions`, lines 47-58.

## Related

- Company: [[braintree]]
- Main concept: [[payment-reconciliation-reporting]]
- Funding context: [[braintree-payment-platform]]
- Control Panel context: [[braintree-control-panel]]
- Separate Braintree batch-report route: [[source-braintree-control-panel-reporting-settlement-batch-summary]]

## Related raw API references

- [[raw/braintree/articles/guides/payment-methods/paypal/setup-guide-2026-09-16|Braintree PayPal Setup Guide article]] - unread navigation-only route for contacting PayPal to configure Settlement Withdrawal; not used as factual evidence here
- [[raw/braintree/articles/control-panel/reporting/settlement-batch-summary-2026-09-16|Braintree Settlement Batch Summary article]] - unread navigation-only report route; not used as factual evidence here
- [[raw/braintree/docs/reference/request/transaction/search/node-2026-09-16|Braintree Node.js transaction search reference]] - unread navigation-only API lookup route; not used as factual evidence here

## Raw Sources

- [[raw/braintree/articles/guides/payment-methods/paypal/funding-reconciliation-2026-09-16|Braintree PayPal Funding and Reconciliation article]] - complete collected page covering PayPal funding destination and withdrawal options, reconciliation report selection, transaction lookup and identifier mapping
