---
title: "Braintree Australia Reconciliation"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/au/reconciliation"
raw_files:
  - "braintree/articles/au/reconciliation-2026-09-16.md"
tags: [braintree, australia, reconciliation, statements, control-panel]
---

## Overview

This collected [[braintree]] article at the exact Australia (`/articles/au/`) route documents use of a monthly merchant statement and Control Panel reports to reconcile Braintree disbursement records with bank-statement deposits, transaction and billable-event fees, and disputes. It identifies the monthly merchant statement as the primary reconciliation tool and routes detailed matching to Disbursement Details, the Transaction-Level Fee report, the Disbursement Summary and the Dispute Report.

This is a 2026-09-16 Braintree-hosted snapshot of the Australia route. The body does not identify a merchant-account program, pricing model, settlement currency or multi-currency conversion rule. Do not transfer its account, fee, timing or report guidance to generic APAC, another regional or processor-specific article, or a sibling account arrangement.

## Key takeaways

- In statement **Disbursement Details**, the **Date** is when Braintree says it disbursed funds and **Total Disbursed** is the amount the article expects to match the bank-statement deposit. It says settled funds should be deposited the same day for NAB business accounts and reflected within one to two business days for other banks; later it says the typical one-to-two-business-day arrival timeframe can vary. These are snapshot reconciliation expectations, not independent bank commitments or proof that a particular deposit arrived.
- To reconcile statement **Braintree Fee Details**, the article directs the merchant to download a Transaction-Level Fee report for the same date range. **Creation Date** drives statement **Quantity** for transaction fees and most billable events, while event-specific billed-date or disbursement-date filters drive **Total Billed**. Because creation and billing can occur in different periods, the two values must be reconciled separately.
- The event procedures distinguish two-step authorization, refund, decline and verification anchors. An authorization created at month-end may have an authorization fee but no settlement date until a later report; verification fees are not listed in the Transaction-Level Fee report and instead route to a date-matched Verification Search. Use the raw locators for the exact filters and fields.
- The **Disbursement Summary** shows transactions for a selected day's disbursement or gross sales and credits grouped by card type. It can take one to three business days after disbursement to become available, requires the **Create, Run, and Download Reports** permission, is selected by merchant account and date range, and excludes transaction fees. The article recommends first matching the bank-statement deposit amount to statement **Total Disbursed**, then using Braintree's disbursement date to select the summary.
- The **Dispute Report** uses its **Disbursement Date** for Open or Won disputes to indicate when disputed funds were credited or debited, and the article positions that field for reconciliation and chargeback analysis. This is a report event anchor, not independent evidence of actual bank posting, fund availability or finality.

> [!warning] Australia snapshot and unresolved account scope
> Keep this evidence within the captured Australia article. The body supplies no merchant-account program, pricing-model, currency or conversion qualification, and the route does not make the guidance generic APAC authority. Consult the dedicated [[source-braintree-control-panel-reporting-transaction-level-fee-report|Transaction-Level Fee Report]] source for its separate pricing-model and eligibility boundaries before relying on that report for a pricing-specific reconciliation use.

> [!warning] Reconciliation anchors are not fund-arrival proof
> Statement dates, report dates, **Total Disbursed** matching, and the article's bank-timing language support a reconciliation procedure. They do not prove that any individual transaction settled, that a deposit reached or became available in a bank account, or that a dispute credit or debit actually posted.

> [!warning] Source wording ambiguity
> In the decline-fee **Total Billed** procedure, the final bullet says the remaining rows equal the number of “refund fees” billed even though the section and filters refer to decline fees. Preserve that captured wording as an unresolved source defect; do not silently convert it into a verified decline-fee result.

## Detail locators

- Document purpose and monthly-statement-first route: `# Reconciliation` and `## Statement reconciliation`, raw lines 14–21.
- Disbursement date meaning, NAB-versus-other-bank timing and **Total Disbursed** matching: `### Disbursement Details`, raw lines 24–26.
- Transaction-Level Fee report date alignment, **Creation Date**, statement **Quantity**, and created-versus-billed separation: `### Braintree Fee Details` through `#### Reconciling billable event fees`, raw lines 29–38.
- Two-step authorization identity plus separate **Created Date** and **Auth Fee Billed Date** filters, including the cross-statement-period example: `##### Authorizations`, raw lines 41–59.
- Refund **Created Date** versus **Disbursement Date** filters: `##### Refunds`, raw lines 62–78.
- Decline **Created Date** versus **Declined Fee Billed Date** filters and the captured “refund fees” wording defect: `##### Declines`, raw lines 81–97.
- Verification-fee exclusion from the Transaction-Level Fee report and the Verification Search route: `##### Verifications`, raw lines 100–110.
- Disbursement Summary purpose, availability lag, permission gate, variable bank-arrival timing, transaction-fee exclusion, merchant-account/date selection, CSV and per-day transaction routes: `### Disbursement Summary report`, raw lines 118–139.
- Advanced Search route for billable events: `### Advanced search`, raw lines 144–146.
- Dispute Report permission, access path, fields and **Disbursement Date** meaning: `### Dispute Report`, raw lines 149–158.

## Related

- Company: [[braintree]]
- Main concept: [[payment-reconciliation-reporting]]
- Supporting concept: [[braintree-control-panel]]
- Related pricing-specific report authority: [[source-braintree-control-panel-reporting-transaction-level-fee-report]]
- Linked statement, permission, search and report destinations are navigation unless separately ingested and read; their detailed behavior is not established by this source.

## Raw Sources

- [[raw/braintree/articles/au/reconciliation-2026-09-16|Braintree Australia Reconciliation]] - fully read collected article covering monthly statement reconciliation, event-date fee matching, Disbursement Summary use and dispute-report anchors
