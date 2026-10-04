---
title: "Braintree Brazil Transaction-Level Fee Report"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/br/reporting-reconciliation/transaction-level-fee-report"
raw_files:
  - "braintree/articles/br/reporting-reconciliation/transaction-level-fee-report-2026-09-16.md"
tags: [braintree, brazil, reporting, reconciliation, installments, funds-anticipation]
---

## Overview

This collected [[braintree]] Brazil-route article, labeled Document Version 1.0, describes the Transaction-Level Fee report's transaction and fee detail for Brazil. It says report detail depends on whether the merchant has IC+ or flat-rate/blended pricing, lists credit and debit cards, Venmo, Apple Pay and Google Pay as supported payment methods, and adds Brazil-specific installment and Funds Anticipation fee detail.

Its central reconciliation use is narrow: locate installment disbursement or adjustment records, inspect the documented fee columns, and compare each installment's **Total Fee Amount** with **Net Settlement Fees** for the same line item in the separately linked Disbursement Report. This is a report-matching procedure, not evidence that a transaction settled, an installment was disbursed, a refund completed, or funds reached a bank account.

## Key takeaways

- For Brazil installments, the page names Visa and Mastercard credit cards and PayPal Wallet transactions, and says **Discount Fees** and **Pre-defined Funds Anticipation Fees** are assessed per installment. The page does not establish debit-card installment support or transfer this Brazil-specific capability to another region.
- For disbursed installments, it directs operators to **Record Type = Installment** and **Record Subtype = Disbursements**, use **Transaction ID** to identify the installment, and inspect **Discount**, **Per Transaction Fee**, **Funds Anticipation Rate**, **Braintree Total Amount**, and **Total Fee Amount**. Its formulas use settlement amount, but the page supplies no denomination, precision or rounding rule.
- For installment refunds, discount-fee credits may depend on the merchant's pricing agreement, and only fully refunded installment transactions have associated refunded fees. The refund amount is divided equally across installments and reported with **Record Subtype = Adjustment**; the raw locator preserves the credit columns and formulas.
- For both installment disbursements and adjustments, the article says installment **Total Fee Amount** should equal **Net Settlement Fees** for the same Disbursement Report line item. The linked report is separate authority, so this source does not establish its access, completeness, timing, settlement finality or bank-posting behavior.
- The page states that Brazil credit-card transactions take 30 days to disburse by default and describes **Pre-defined Funds Anticipation** as an agreed schedule and rate that pays all credit-card transactions earlier, including standard transactions and installments. The rate columns support fee calculation for a sale or refund; this snapshot does not establish a current universal timeline, account eligibility, an agreed rate, payout execution or arrival.

> [!warning] Pricing-model and reconciliation boundary
> This Brazil page says report detail depends on IC+ versus flat-rate/blended pricing and then gives installment reconciliation instructions without restating a pricing-model limit. The separately ingested [[source-braintree-control-panel-reporting-transaction-level-fee-report|general Transaction-Level Fee Report page]] says Brazil availability is by default for flat-rate/blended merchants, while IC+ report interchange values are estimates and must not be used for reconciliation. Do not use the Brazil article to override that pricing-specific limit or infer Brazil IC+ availability; obtain account-specific clarification before relying on installment fee matching under IC+.

> [!warning] Brazil route, account and currency scope
> Keep this evidence within the captured Brazil route. The body does not identify a merchant-account program, settlement currency, conversion behavior, fee denomination, numeric rate, precision or rounding rule. Its report table later lists Samsung Pay and Bank Account rows even though the report-definition support list names only cards, Venmo, Apple Pay and Google Pay; treat that table as a field-value locator, not proof of added payment-method support.

> [!warning] Snapshot and money-movement boundary
> The raw was fetched on 2026-09-16 and carries page metadata updated 2025-04-01 plus a version-1.0 changelog dated 2021-02-18. Those dates preserve provenance, not current policy. Report rows, fee formulas, a scheduled earlier payout and a cross-report match do not prove payment execution, settlement, disbursement, refund completion or bank arrival for any transaction.

## Detail locators

- Document version and changelog route: `## Document Version 1.0`, raw lines 17-19; initial-version row, raw lines 124-128.
- Report purpose, pricing-model dependency and supported-method list: `## Report Definition`, raw lines 22-30.
- Brazil-specific installment and Funds Anticipation additions plus the separate report-running route: `## Report Definition`, raw lines 32-38.
- Brazil installment payment-method and per-installment fee scope: `### Installments`, raw lines 41-49.
- Disbursement record selectors, identity field, fee columns and formulas: `#### Reconciling Fees for Installment Disbursements`, raw lines 52-64.
- Refund-credit and fully-refunded qualifications, equal division and adjustment record selector: `#### Reconciling Fees for Installment Adjustments`, raw lines 69-85.
- Transaction-Level Fee Report to Disbursement Report line-item equality statement: raw line 89.
- Default 30-day statement, agreed Pre-defined Funds Anticipation schedule/rate, transaction scope and rate-column calculation: `### Funds Anticipation`, raw lines 92-100.
- Record type/subtype table: `## Record types and subtypes`, raw lines 103-109.
- Payment-instrument field table, including rows beyond the earlier support list: `## Payment instrument types and subtypes`, raw lines 112-121.

## Related

- Company: [[braintree]]
- Main concept: [[payment-reconciliation-reporting]]
- Pricing-model-specific report authority and reconciliation limit: [[source-braintree-control-panel-reporting-transaction-level-fee-report]]

## Related raw API references

- [[raw/braintree/articles/br/payment-capabilities-2026-09-16|Braintree Brazil Payment Capabilities]] - linked installment-capability navigation; not read as factual evidence for this source
- [[raw/braintree/articles/br/reporting-reconciliation/disbursement-report-2026-09-16|Braintree Brazil Disbursement Report]] - linked line-item comparison destination; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/articles/br/reporting-reconciliation/transaction-level-fee-report-2026-09-16|Braintree Brazil Transaction-Level Fee Report]] - fully read version-1.0 snapshot covering Brazil installment fee matching, refund adjustments, Funds Anticipation and report field locators
