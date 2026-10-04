---
title: "Braintree Brazil Reconciliation"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/br/reporting-reconciliation/reconciliation"
raw_files:
  - "braintree/articles/br/reporting-reconciliation/reconciliation-2026-09-16.md"
tags: [braintree, brazil, reconciliation, disbursements, reporting]
---

## Overview

This collected [[braintree]] article at the exact Brazil (`/articles/br/`) route describes using a monthly merchant statement and several reports to reconcile disbursements with bank-account records. Its central workflow compares statement **Disbursement Details** with deposits, then uses the Unified Disbursement Report where debt repayment can make the amount reaching the bank differ from **Total Disbursed** in the PayPal account.

This is a 2026-09-16 Braintree-hosted snapshot of the Brazil route. The body does not identify a pricing model or settlement currency, and it does not establish current account eligibility, independent bank policy, or equivalence with sibling regional or processor-specific articles.

## Key takeaways

- The article identifies the monthly merchant statement as the primary reconciliation tool. In **Disbursement Details**, the **Date** is when the page says funds were disbursed to the merchant's PayPal account before being swept to the bank. Conditional on the merchant using batch settlement, it says Monday-through-Thursday settlements should be deposited the same day, Friday settlements are swept the following Monday, and swept funds should appear on the bank statement within one to two business days. These are page-stated timing expectations, not a settlement or bank-arrival guarantee.
- **Total Disbursed** is said to match the PayPal-account deposit, but some settled funds may be sent to a partnering bank for debt repayment. The article therefore requires the Unified Disbursement Report for reliable reconciliation of deposits to the bank account; a PayPal-account total alone is not sufficient bank-deposit evidence.
- The **Unified Disbursement Report** combines PayPal- and Braintree-processed transactions, details disbursement-impacting sales, refunds, installments, disputes and fees, and can combine multiple Braintree accounts that settle into one PayPal account and are disbursed together. This report description supports reconciliation routing, not proof that any listed event settled or that funds arrived.
- The **Disbursement Summary** can show transactions for a selected day's disbursement or gross sales and credits grouped by card type. The article says it may take one to three business days after disbursement to become available, requires the **Create, Run, and Download Reports** permission, is selected by merchant account and date range, and excludes transaction fees. It recommends first matching the bank-statement deposit to statement **Total Disbursed**, then using Braintree's disbursement date to pull the corresponding summary; the debt-repayment warning above remains controlling when those amounts differ.
- For disputes, the article routes reconciliation to the **Disbursement Date** in the Disputes Financial Impact Report, described as the exact date disbursed funds were credited or debited from the account. That report date is an event anchor within this snapshot, not independent evidence of bank posting, availability or finality.

> [!warning] Brazil snapshot and account scope
> Keep this evidence within the captured Brazil article. The body supplies no pricing-model or currency qualification, and the route alone does not make the guidance current authority for another region, processor arrangement or account program. Multiple Braintree accounts settling into one PayPal account is a documented report use case, not evidence that any particular merchant has that configuration.

> [!warning] Reconciliation is not deposit or settlement proof
> Statement amounts, report event dates and expected sweep or bank-statement timing support a reconciliation procedure only. They do not prove that an individual transaction settled, that a deposit reached or became available in a bank account, that debt repayment was correctly applied, or that a credit or debit is final.

## Detail locators

- Document purpose and monthly-statement-first route: `# Reconciliation` and `## Statement reconciliation`, raw lines 14-21.
- PayPal-account disbursement date, batch-settlement weekday conditions, sweep timing and debt-repayment warning requiring the Unified Disbursement Report: `### Disbursement Details`, raw lines 24-30.
- Unified Disbursement Report coverage, disbursement-impacting event list and multiple-Braintree-account-to-one-PayPal-account use: `### Unified Disbursement Report`, raw lines 40-42.
- Disbursement Summary purpose, one-to-three-business-day availability lag, permission gate, amount/date matching procedure, transaction-fee exclusion and merchant-account/date controls: `### Disbursement Summary report`, raw lines 45-66.
- Disputes Financial Impact Report route and **Disbursement Date** meaning: `### Dispute Report`, raw lines 71-73.

## Related

- Company: [[braintree]]
- Main concept: [[payment-reconciliation-reporting]]
- Linked statement, Unified Disbursement Report, role-permission and disputes-report destinations are navigation unless separately ingested and read; their detailed behavior is not established by this source.

## Raw Sources

- [[raw/braintree/articles/br/reporting-reconciliation/reconciliation-2026-09-16|Braintree Brazil Reconciliation]] - fully read collected article covering statement and report reconciliation, PayPal-to-bank sweep timing, the debt-repayment warning, report availability and permission conditions, and dispute event dates
