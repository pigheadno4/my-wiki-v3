---
title: "Braintree Wells Flat Statements and Reconciliation"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/wells-flat/statements-reconciliation"
raw_files:
  - "braintree/articles/wells-flat/statements-reconciliation-2026-09-16.md"
tags: [braintree, wells-flat, statements, reconciliation, disbursements, reporting]
---

## Overview

This collected [[braintree]] Wells Flat article describes Braintree statements and statement-based reconciliation: statement contents and account-specific fee sections, matching statement disbursement details to bank deposits, supporting Control Panel reports, and a qualified multi-currency path. It is a Braintree-hosted snapshot for the captured Wells Flat scope, not independent current bank policy, current account or regional eligibility, or proof that a particular deposit arrived.

## Key takeaways

- A Braintree statement is described as a snapshot of settled transactions, Braintree processing fees, and deposits sent to the merchant account. Statements are accessed from **Reports** → **Statements** in the Control Panel; the user needs the **View Statements** role permission.
- The documented primary reconciliation method compares the statement's second-page **Disbursement Details** with bank-account deposits. The article explicitly says not to use the Dashboard or Settlement Batch Summary for reconciliation.
- The statement's **Pricing Schedule** identifies the fee structure for the merchant account, including discount, cross-border, chargeback, and per-transaction fee rates. The **Braintree Fee Details** treatment differs between Braintree's aggregated Amex account and a merchant's own Amex account; use the raw locators rather than transferring these rules to IC+ pricing or another account configuration.
- **Total Disbursed** is account-dependent: with Braintree's aggregated Amex account it includes the listed card brands including Amex, while a merchant with its own Amex account receives Amex disbursements directly from Amex and those funds are excluded. The disbursement date is the date funds were sent, not their availability date; the snapshot says they should appear on the bank statement within 1–2 business days.
- The Control Panel **Disbursement Summary** can show a day's transactions or gross sales and credits by card type, but it excludes transaction fees and omits Amex transactions for merchants using their own Amex account. Access requires the **Create, Run, and Download Reports** role permission.
- For merchants that have multi-currency merchant accounts, the article says transactions are converted to USD without an additional conversion fee and deposited in USD. It says each exchange rate is determined at authorization, applied at disbursement, and can vary within one disbursement; this is captured Wells Flat documentation, not a general regional or bank guarantee.

> [!warning] Scope and reconciliation boundaries
> Braintree Marketplace statements are expressly different and must use the separate Marketplace guide; do not transfer this page's statement or reconciliation treatment to Marketplace. The page also does not establish IC+ reporting rules. A statement date or reported amount is reconciliation evidence, not independent proof of bank availability or a completed individual deposit.

## Detail locators

- Marketplace separation: note before `## Statements`, raw lines 17–18.
- Statement purpose, Control Panel access path, and **View Statements** permission: `## Statements`, raw lines 23–36.
- Statement-section inventory and payment-method-dependent U.S. bank account and Venmo breakdowns: `## Statements`, raw lines 40–56.
- Disbursement, processing, fee, aggregated-Amex, own-Amex, pricing-schedule, and promotion sections: `### Summary page`, raw lines 61–105.
- Primary reconciliation comparison and the Dashboard/Settlement Batch Summary prohibition: `## Reconciliation`, raw lines 108–116.
- Disbursement-date meaning, bank-statement timing statement, and aggregated-versus-own-Amex treatment: `### Disbursement Details`, raw lines 121–133.
- Disbursement Summary purpose, omissions, permission, run steps, and CSV/transaction routes: `### Disbursement Summary report`, raw lines 136–155.
- Dispute-report and transaction-level-fee-report routes: `### Dispute Report` and `### Transaction-level reconciliation`, raw lines 160–169.
- Multi-currency merchant-account prerequisite, USD conversion, exchange-rate timing and CSV lookup: `## Multi-currency reconciliation`, raw lines 172–192.

## Related

- Company: [[braintree]]
- Main concept: [[payment-reconciliation-reporting]]
- Supporting concept: [[braintree-control-panel]]

## Raw Sources

- [[raw/braintree/articles/wells-flat/statements-reconciliation-2026-09-16|Braintree Wells Flat statements and reconciliation article]] - complete collected snapshot covering statements, account- and pricing-qualified fee sections, disbursement matching, report limitations, permissions, and multi-currency reconciliation
