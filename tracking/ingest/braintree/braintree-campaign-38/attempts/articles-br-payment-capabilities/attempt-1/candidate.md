---
title: "Braintree Brazil Payment Capabilities"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/br/payment-capabilities"
raw_files:
  - "braintree/articles/br/payment-capabilities-2026-09-16.md"
tags: [braintree, brazil, installments, payments, disbursements, disputes]
---

## Overview

This collected Braintree Brazil-path article describes installment sale transactions: the customer selects an installment count in the checkout workflow, the sale amount is divided across that count, and the article says Braintree supports plans spanning two to twelve months. It is a 2026-09-16 documentation snapshot, not proof of current support, merchant or customer eligibility, account enablement, transaction execution, disbursement, settlement or funding.

The page does not identify a currency, card brand, SDK version, API version, environment or merchant-account eligibility rule. The separately retained [[source-braintree-articles-br-overview|Brazil Overview]] limits its own direct-link portal audience to Braintree Direct recipients with at least one merchant account located in Brazil and funded by Braintree, while also saying account nuances vary by location and setup. Keep that sibling account context separate: it does not prove that every such account can use installments or that this article applies outside the documented Brazil path.

## Key takeaways

- For a customer who opts into installments, the article says the installment amount is debited every 30 days and the merchant is also paid that amount every 30 days until the plan is fulfilled. This is the page's documented cadence, not proof of a particular debit, merchant payment, settlement or bank arrival.
- Installment transaction disbursements are described as divided evenly across the installment count; when the transaction total does not divide evenly, the remainder is paid with the final installment. The linked settlement and funding article remains the authority for its own lifecycle details.
- Using installment payments requires integration updates for transaction creation and management. The page routes exact creating, refunding and search procedures to the dedicated installments article; those linked procedures were not read as evidence for this entry.
- The page says dispute finding and response do not change for installment transactions: a dispute is assessed against the single transaction, and a customer cannot dispute one installment. Associated dispute debits and credits are described as applied evenly across all installments of the disputed transaction. This does not prove a dispute outcome or statement reconciliation.
- The page routes installment lifecycle tracking to Activity, Disbursement and Transaction Level Fee reports, and dispute financial reconciliation to the Disputes Financial Impact Report. Report schemas, availability, timing and account eligibility remain in their linked sources.

> [!warning] Brazil-path snapshot and absent eligibility details
> Preserve the page's Brazil path, customer opt-in condition, 2–12-month range and 30-day wording. Do not infer a currency, supported card or payment method, universal Braintree or PayPal capability, eligibility for every Brazil merchant account, another region's support, current availability, or successful payment and funding from this snapshot.

## Detail locators

- Brazil installment sale description, checkout-selected count and two-to-twelve-month span: `## Installments`, raw line 16.
- Customer debit and merchant payment cadence: `## Installments`, raw line 18.
- Named lifecycle-report routes: `### Installment Reporting`, raw lines 21-28.
- Even installment disbursement and final-installment remainder: `### Installment Disbursements`, raw line 33.
- Integration-update prerequisite and create/refund/search navigation: `### Creating and Managing Installment payments`, raw lines 36-43.
- Transaction-level dispute treatment and inability to dispute one installment: `### Chargebacks, retrievals, and pre-arbitratition cases on installments`, raw line 48.
- Even application of dispute debits and credits plus reconciliation-report route: same section, raw line 50.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]
- Brazil direct-link account context: [[source-braintree-articles-br-overview]]

## Related raw API references

The following linked pages are navigation targets and were not read as factual evidence for this entry:

- [[raw/braintree/articles/br/transactions/installments-2026-09-16|Braintree Brazil installment transaction procedures]]
- [[raw/braintree/articles/br/transactions/settlement-funding-timeline-2026-09-16|Braintree Brazil settlement and funding timeline]]
- [[raw/braintree/articles/br/reporting-reconciliation/activity-report-2026-09-16|Braintree Brazil Activity Report]]
- [[raw/braintree/articles/br/reporting-reconciliation/disbursement-report-2026-09-16|Braintree Brazil Disbursement Report]]
- [[raw/braintree/articles/br/reporting-reconciliation/transaction-level-fee-report-2026-09-16|Braintree Brazil Transaction Level Fee Report]]
- [[raw/braintree/articles/br/chargebacks-retrievals-prearbs-2026-09-16|Braintree Brazil chargebacks, retrievals and pre-arbitration article]]

## Raw Sources

- [[raw/braintree/articles/br/payment-capabilities-2026-09-16|Braintree Brazil Payment Capabilities]] - fully read 2026-09-16 snapshot covering installment range and cadence, disbursement allocation, integration navigation and transaction-level dispute treatment
