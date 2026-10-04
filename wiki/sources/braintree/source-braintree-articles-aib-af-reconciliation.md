---
title: "Braintree AIB AF Reconciliation"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/aib-af/reconciliation"
raw_files:
  - "braintree/articles/aib-af/reconciliation-2026-09-16.md"
tags: [braintree, aib-af, reconciliation, reporting, settlement]
---

## Overview

This captured [[braintree]] AIB AF article documents ordinary reconciliation using the AIB Merchant Statement and AIB Transaction Fee Report. General reconciliation compares the statement's **Funding Totals** with bank-account deposits. Transaction-level reconciliation compares the fee report with both the AIB Statement and bank deposits, then derives processing-date net settlement amounts and matches them to statement funding totals.

Treat this as a Braintree-hosted snapshot for the AIB AF route, not as the separate AIB AF `Reconciliation (LR)` document, AIB BF behavior, independent current bank policy, or proof that a particular deposit arrived. The body states no region or pricing model, and links to statements, role permissions, merchant-account IDs, pricing models, Excel help and the Control Panel are navigation rather than evidence that those targets agree with this snapshot.

## Key takeaways

- Access to the AIB Transaction Fee Report is limited to users with the **Create, Run, and Download Reports** role permission. The documented Control Panel procedure selects merchant account scope and a date range. If a merchant processes multiple currencies and has more than one merchant account, all merchant accounts are included by default unless the merchant narrows the Merchant Account ID field.
- The report is based on transaction settlement dates. The article says deposit typically follows settlement by one business day and suggests a wider report date range to capture all transactions in the disbursement being reconciled; this timing statement is not evidence of actual bank receipt.
- In Excel, the article has merchants organize Settlement Amount, Total Fee Amount, Chargeback Amount and Chargeback Fee Amount by Processing Date, then calculate net settlement as Settlement Amount minus all fees and chargebacks.
- Reconciliation matches each PivotTable Processing Date to the statement's Funding Totals date. If the net amount differs, the article suggests rounding Total Fee Amount up to two decimal places because AIB calculates it to as many as five decimals, or checking adjacent report dates because negative balances or time-zone differences can shift exact processing dates.
- **Settlement Amount** is before fees; **Total Fee Amount** includes interchange and Braintree fees but excludes chargeback fees. Although the report exposes **Interchange Amount**, the article says merchants should use only Total Fee Amount for reconciliation regardless of pricing model. It does not supply a fee schedule or establish which pricing model applies.

> [!warning] Reconciliation records are not deposit proof
> Statement Funding Totals, report rows and the article's typical one-business-day timing support a matching procedure; they do not independently establish that a specific deposit reached the merchant's bank account.

> [!warning] Captured ordinary AIB AF scope
> Keep the report procedure, timing, column treatment and discrepancy techniques within this ordinary AIB AF snapshot. Do not transfer them to the AIB AF LR article, AIB BF, another processor/account setup, a merchant agreement, or current independent bank policy.

## Detail locators

- Funding Totals comparison and completed-transfer/bank-statement-text description: `## General reconciliation`, raw lines 17-19.
- Transaction-level comparison purpose: `## Transaction-level reconciliation`, raw lines 22-24.
- Report permission, Control Panel path, merchant-account scope and date-range selection: `### Step one`, raw lines 27-43.
- Settlement-date basis, typical deposit lag and wider-date-range suggestion: raw line 43.
- PivotTable fields and net-settlement calculation: `### Step two`, raw lines 46-58.
- Merchant Statement download route: `### Step three`, raw lines 61-70.
- Processing-date-to-Funding-Totals match and mismatch techniques: `### Step four`, raw lines 73-79.
- Settlement, interchange and total-fee column meanings plus the do-not-use-interchange warning: `## Understand the AIB Transaction Fee Report`, raw lines 82-93.

## Related

- Company: [[braintree]]
- Main concept: [[payment-reconciliation-reporting]]

## Raw Sources

- [[raw/braintree/articles/aib-af/reconciliation-2026-09-16|Braintree AIB AF Reconciliation]] - fully read captured article covering statement and transaction-level matching, report access and date scope, net-settlement calculation, mismatch techniques, and fee-column treatment
