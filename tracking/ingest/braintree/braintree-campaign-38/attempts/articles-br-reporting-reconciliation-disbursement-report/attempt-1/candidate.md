---
title: "Braintree Brazil Disbursement Report"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/br/reporting-reconciliation/disbursement-report"
raw_files:
  - "braintree/articles/br/reporting-reconciliation/disbursement-report-2026-09-16.md"
tags: [braintree, brazil, disbursement, reconciliation, reporting]
---

## Overview

This collected [[braintree]] article at the exact Brazil (`/articles/br/`) route identifies itself as Disbursement Report version 1.1. It presents the report as a way to reconcile daily PayPal and Braintree deposits with a system of record, using both batch summaries and event-level detail for payment events that affected a deposit. The documented file has Header, Summary, Detail and Footer sections.

This is a 2026-09-16 documentation snapshot, not proof that the report is currently available to a particular account, that a payment settled, or that a deposit reached a bank account. The page does not document access permissions, delivery, generation schedule, merchant pricing rates or current eligibility.

## Key takeaways

- The Summary represents each reporting-period disbursement batch as a line item and identifies merchant-account amount, transfer and destination-bank context. The Detail represents disbursement-impacting events such as transactions and disputes, while the Footer provides record and file counts for ingestion checks.
- For the documented Brazil reconciliation route, the page tells the reader to match a PayPal bank-statement deposit to Summary **Net Disbursed Amount**, use **Funding Account** to group Detail rows, and sum **Net Disbursed** within each group. It says Brazil's **Funding Account** value will always be a PayPal Account Number because PayPal Wallet and credit/debit-card transactions are disbursed through a PayPal account. This is the report's stated matching method and account-routing rule, not evidence that any particular deposit arrived.
- The page supplies separate report-event procedures for sales/refunds, installment disbursements and adjustments, and disputes. For disputes, it says a **Chargeback** should be **Lost** with a negative amount, while a **Chargeback reversal** should be **Won** with a positive amount; these are report-record expectations rather than proof of an external dispute outcome. Use the raw locators for the exact record-type, subtype and identifier filters.
- Time and currency meanings are field-specific. The Header carries report generation date and timezone. Detail distinguishes object creation, settlement and disbursement dates; **Settlement date** is stated to populate only for sales and refunds. Detail also separates transaction currency and settlement currency, includes an exchange rate when those currencies differ, and records gross, fee and net values. These fields describe the report snapshot and do not establish pricing terms or exchange-rate authority.
- The Summary includes a separate **Previous failed disbursement amount** when a prior failed disbursement is included in the current day's disbursement. Do not treat a current report total as if it necessarily contains only newly disbursed events.

> [!warning] Scope and money-movement boundary
> Keep the account-routing statement within this captured Brazil report route. The route and report fields do not establish current account eligibility, another region's behavior, bank policy, fund availability, settlement finality or successful deposit.

> [!warning] Pricing and currency boundary
> Fee, gross, net, transaction-currency, settlement-currency and exchange-rate fields are reconciliation data. The page does not state a merchant's pricing model or rates, validate a conversion, or make the report independent pricing authority.

> [!warning] Captured data-dictionary wording defect
> The **RD** dictionary row says Detail rows belong to the Summary section, and the **RF** dictionary row similarly says Footer rows belong to the Summary section, even though the report-format section defines separate Detail and Footer sections. Preserve those statements as unresolved source wording defects; do not use them to relabel RD or RF rows as Summary rows.

## Detail locators

- Document version and central reconciliation purpose: `## Document Version 1.1` and `## Report Definition`, raw lines 17–24.
- Four-section structure and section purposes: `## Report format`, raw lines 27–55.
- Deposit matching, Brazil PayPal Account Number funding-account rule, Detail grouping and per-record-type transition: `## How to Use the Report` through `### Reconciling deposit amount to funding account in PayPal`, raw lines 58–71.
- Sales/refunds and installment record filters, identifiers, dates, transfer IDs and net values: raw lines 74–100.
- Dispute identifier, amount, subtype, status and sign expectations: `### Reconciling disputes`, raw lines 103–112.
- Report-generated date and timezone fields: `### Report Header Data Dictionary`, raw lines 120–129.
- Summary transfer, bank-account, currency, current amount and previous-failed-disbursement fields: `### Report Summary Data Dictionary`, raw lines 132–143.
- Detail object/account identifiers, event dates, transaction-versus-settlement currency, amount/fee/net fields and exchange rate: `### Report Detail Data Dictionary`, raw lines 146–185.
- Captured RD and RF section-description defects: raw lines 150 and 192.
- Footer file and record counts: `### Footer Data dictionary`, raw lines 188–195.
- Exact record types and subtypes: `## Record types and subtypes`, raw lines 198–221.
- Version history: `## Changelog`, raw lines 240–245.

## Related

- Company: [[braintree]]
- Main concept: [[payment-reconciliation-reporting]]

## Raw Sources

- [[raw/braintree/articles/br/reporting-reconciliation/disbursement-report-2026-09-16|Braintree Brazil Disbursement Report]] - fully read 2026-09-16 snapshot of version 1.1, its Brazil funding-account rule, reconciliation procedure, event/date/currency fields and data-dictionary wording defects
