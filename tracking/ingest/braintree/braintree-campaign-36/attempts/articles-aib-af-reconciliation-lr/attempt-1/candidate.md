---
title: "Braintree AIB AF Reconciliation (LR)"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/aib-af/reconciliation-lr"
raw_files:
  - "braintree/articles/aib-af/reconciliation-lr-2026-09-16.md"
tags: [braintree, aib-af, reconciliation, reporting, settlement]
---

## Overview

This collected `Reconciliation (LR)` article under Braintree's AIB AF path documents two reconciliation routes: comparing statement Funding Totals with bank-account deposits, and using the Transaction Fee Report to reconcile daily deposits from Braintree AIB funded accounts with merchant records and clear receivables. The report combines summarized disbursement information with event-level transaction, dispute, fee and adjustment records.

The snapshot is Braintree-hosted AIB AF documentation, not independent current bank authority or evidence of current account, region or pricing eligibility. It must not be transferred to AIB BF, ordinary AIB AF reconciliation, or other processor/account arrangements. A report row, transfer reference or expected match does not prove that an individual deposit reached the merchant's bank account; the documented record types expressly include failed disbursements.

## Key takeaways

- For general reconciliation, the article directs merchants to compare the AIB Merchant Statement's **Funding Totals** with bank-account deposits. That statement section is described as containing completed bank-transfer details for the billing period and the text expected on bank statements.
- For transaction-level reconciliation, the Transaction Fee Report is scoped to daily deposits from Braintree AIB funded accounts. It contains Gateway Transaction Records, Accounting Based Records and Summary Records; each Summary Record represents a disbursement and includes its per-MID total and Transfer ID.
- The deposit-matching procedure uses the Transfer ID, Summary **Net Disbursed** amounts and Transaction Disbursement Key. It instructs merchants to total settlement, fee and chargeback amounts per key, truncate totals to two decimals rather than round, and confirm that all disbursement-impacting items are present before reconciling by record type.
- Settlement treatment is qualified: for sales and refunds, net-settlement merchants use amounts net of fees, while gross-settlement merchants are routed to the separate fee-reconciliation procedure. The article also provides two gross-settlement sample files, one for daily credit and one for fee debit.
- The data dictionary marks **Card Type Group** and **Region Relation** as EMEA-only fields, but the page does not state a general regional eligibility rule. Detailed fields, record types and subtypes remain in the raw locator rather than being treated as a universal schema or fee schedule.

> [!warning] Report evidence is not deposit proof
> The documented report and matching procedure support reconciliation but do not independently prove settlement or bank receipt. The report can contain a **Failed disbursement** record when a bank deposit fails.

> [!warning] Captured AIB AF LR scope
> Keep the net/gross treatment, field definitions and procedures within this captured AIB AF `Reconciliation (LR)` article. Do not conflate it with ordinary reconciliation, AIB BF, sibling idempotency documentation, another processor/account setup, or current independent bank policy.

## Detail locators

- General statement-to-deposit comparison and transaction-level report purpose: `## General reconciliation` and `## Transaction-level reconciliation`, raw lines 17-24.
- Net and gross sample-file routes: `## Sample files`, raw lines 27-41.
- Report categories and per-disbursement Summary Record: `### Transaction-level fee report format`, raw lines 44-66.
- Transfer-ID matching, per-key calculations, truncation rules and the all-items-present condition: `### How to Use the Report > #### Reconciling deposit amount to the reported amounts`, raw lines 69-89.
- Sales/refunds, net-versus-gross qualification, disputes and gross-settlement fee reconciliation: raw lines 92-134.
- Field definitions, including EMEA-only fields and transfer/disbursement keys: `### Data dictionary for Report Records`, raw lines 137-175.
- Record-type and subtype meanings, including failed disbursement and gross-settlement processing fees: `### Record types and Subtypes`, raw lines 178-207.

## Related

- Company: [[braintree]]
- Main concept: [[payment-reconciliation-reporting]]

## Raw Sources

- [[raw/braintree/articles/aib-af/reconciliation-lr-2026-09-16|Braintree AIB AF Reconciliation (LR) article]] - complete collected snapshot covering statement and Transaction Fee Report reconciliation, net/gross qualifications, deposit matching, report fields and record types
