---
title: "Braintree AIB BF Reconciliation"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/aib-bf/reconciliation"
raw_files:
  - "braintree/articles/aib-bf/reconciliation-2026-09-16.md"
tags: [braintree, aib-bf, reconciliation, disbursements, reporting, fees]
---

## Overview

This collected [[braintree]] article at the exact AIB BF route explains reconciliation using statement Disbursement Details, bank deposits, the Control Panel Disbursement Summary, dispute reporting and transaction-level fee calculations. The AIB BF path label is retained without expanding it or transferring the guidance to AIB AF, LR, another account or region, or current independent bank authority.

## Key takeaways

- The article says most merchants compare the Disbursement Details on the second page of a Braintree statement with bank-account deposits. For more granular work, it describes calculating fees per transaction. It expressly says the Dashboard and Settlement Batch Summary may be helpful but should not be used for reconciliation.
- In Disbursement Details, the Date is Braintree's disbursement date, the fee breakdown is per disbursement, and the Total Disbursed amount is stated to match the bank-statement deposit. The page says funds should appear within 1–3 business days depending on the bank, then separately says that typical 1–3-business-day timing can vary. These statements are snapshot guidance, not proof that a particular deposit arrived or a current bank timing guarantee.
- The Disbursement Summary can expose individual transactions for a day's disbursement or gross sales and credits grouped by card type. It may not become available until 1–3 business days after disbursement, requires the Create, Run, and Download Reports permission, and does not include transaction fees. The article recommends matching the bank deposit amount to Total Disbursed first and then using Braintree's disbursement date to select the corresponding summary.
- For disputes, the article points to the Disbursement Date in the Disputes Financial Impact Report as the date disbursed funds were credited to or debited from the account. This is the article's reporting route, not independent evidence of bank movement.
- For transaction-level fee calculations, the article directs a transaction search filtered by Disbursed date range, followed by the account statement's Pricing Schedule and a round-down step. It also points to a Transaction Fee Report for fees assessed and deducted from specific sale transactions, available at the beginning of each month. The linked pricing, statement, dispute and Control Panel pages are navigation targets only; this source does not establish that their detailed behavior or terms agree with this snapshot.

> [!warning] Exact scope and reconciliation limits
> Keep this evidence within the captured AIB BF article. Do not treat it as AIB AF or LR guidance, current independent bank authority, account eligibility, proof of an individual deposit or dispute movement, or a guarantee of 1–3-business-day timing. Do not use the Dashboard or Settlement Batch Summary as reconciliation evidence on the strength of this page, and do not treat the Disbursement Summary as including transaction fees.

## Detail locators

- Primary statement-to-bank matching method, granular fee option and explicit Dashboard/Settlement Batch Summary warning: `# Reconciliation`, raw lines 16–22.
- Disbursement date meaning, conditional bank timing, fee breakdown and Total Disbursed matching statement: `## Disbursement Details`, raw lines 27–31.
- Disbursement Summary purpose, availability delay, permission gate, variable arrival timing and transaction-fee exclusion: `## Disbursement Summary report`, raw lines 34–42.
- Control Panel steps, merchant-account/date-range selection, CSV totals and per-day transaction view: raw lines 47–57.
- Dispute reconciliation via the Disputes Financial Impact Report's Disbursement Date: `## Reconciling disputes`, raw lines 60–62.
- Disbursed-date transaction-search steps, Pricing Schedule lookup, round-down instruction and monthly Transaction Fee Report route: `## Calculating fees on a transaction level`, raw lines 65–84.

## Related

- Company: [[braintree]]
- Main concept: [[payment-reconciliation-reporting]]
- Supporting concept: [[braintree-control-panel]]
- Linked statement, pricing, dispute, permission, Dashboard and Settlement Batch Summary destinations are navigation only and were not used as behavioral evidence for this entry.

## Raw Sources

- [[raw/braintree/articles/aib-bf/reconciliation-2026-09-16|Braintree AIB BF Reconciliation]] - fully read collected article covering statement-to-bank matching, disbursement-report conditions, disputes and transaction-level fee calculation
