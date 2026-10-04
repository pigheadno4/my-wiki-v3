---
title: "Braintree Wells IC+ Statements and Reconciliation"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/wells-ic/statements-reconciliation"
raw_files:
  - "braintree/articles/wells-ic/statements-reconciliation-2026-09-16.md"
tags: [braintree, wells-ic, statements, reconciliation, control-panel]
---

## Overview

This collected Braintree Wells IC article documents Control Panel statements and reconciliation for its captured IC+ scope. It explains statement access and fee sections, the different event timing used for interchange and Braintree fees, and ways to compare disbursement records with bank-account deposits.

This is Braintree-hosted snapshot evidence, not current independent bank policy, current account eligibility, or proof that a particular withdrawal or deposit occurred. Its pricing, account, timing, and reconciliation statements must not be transferred to flat-rate or blended pricing, Braintree Marketplace, or other processor/account arrangements.

## Key takeaways

- Statements are accessed through the Control Panel Reports area, and the `View Statements` role permission is required when a user cannot access or see that area.
- In the captured IC+ scope, the article separates card-association interchange/pass-through fees from Braintree fees. It says both are debited on the third business day of the following month as two separate withdrawals.
- The Pass-Through Fee Report provides the specific-fee breakdown by the end of the third business day of the following month. Interchange is billed by settlement timing while Braintree fees are billed by disbursement timing, so the pass-through section's sales volume does not align with the statement's Disbursement Summary gross sales.
- For reconciliation, the article directs merchants to compare statement Disbursement Details with bank deposits: it expects funds within one to two business days after the displayed disbursement date and says Total Disbursed will match the bank-statement deposit. Treat this as the article's reconciliation method and timing expectation, not evidence of any individual funded deposit or an independent bank commitment.
- Amex treatment depends on account arrangement: Braintree's aggregated Amex account includes Amex in Total Disbursed, while an own-Amex account leaves Amex funds out because Amex handles those disbursements directly. The Disbursement Summary also excludes transaction fees and, for merchants with their own Amex account, Amex transactions.
- Braintree Marketplace is expressly routed to a different statements and reconciliation guide; this page must not be used as Marketplace statement authority.

> [!warning] Captured scope only
> Keep every pricing, withdrawal, account, Amex, currency, and reconciliation statement within this captured Braintree Wells IC+ article's scope. Do not apply it to flat-rate or blended pricing, Braintree Marketplace, a different processor/account setup, or current independent bank policy.

> [!warning] Reconciliation is not deposit proof
> The article's expected bank-appearance timing and matching method do not prove settlement, withdrawal, bank receipt, or the funding of a specific transaction or deposit. Current operational decisions require current account-specific confirmation.

## Detail locators

- Marketplace exclusion and separate-guide route: `# IC+ Statements and Reconciliation > NOTE`, raw lines 17-18.
- Control Panel statement path and `View Statements` permission: `## Statements`, raw lines 23-34.
- Routine statement inventory and payment-method-dependent breakdowns: `## Statements`, raw lines 38-54.
- IC+ fee categories, separate following-month withdrawals, Braintree-fee rows, and aggregated-versus-own-Amex treatment: `#### Fee Details`, raw lines 74-96.
- Pass-through fee meaning, report path and availability, and settlement-versus-disbursement timing mismatch: `##### Pass-Through Fee Details`, raw lines 99-111.
- Kount fee-section condition and merchant-account pricing schedule: raw lines 114-121.
- Disbursement Details matching method, timing expectation, and aggregated-versus-own-Amex treatment: `### Disbursement Details`, raw lines 127-133.
- Permission-gated Disbursement Summary procedure and its transaction-fee/own-Amex exclusions: `### Disbursement Summary report`, raw lines 136-155.
- Dispute-report and transaction-search reconciliation routes: raw lines 160-178.
- Multi-currency merchant-account qualification, USD conversion statement, exchange-rate timing, and CSV lookup path: `## Multi-currency reconciliation`, raw lines 181-201.

## Related

- Company: [[braintree]]
- Main concept: [[payment-reconciliation-reporting]]

## Raw Sources

- [[raw/braintree/articles/wells-ic/statements-reconciliation-2026-09-16|Braintree Wells IC+ Statements and Reconciliation article]] - complete collected snapshot covering IC+ statements, fee timing, Disbursement Details matching, account-qualified Amex handling, and multi-currency reconciliation
