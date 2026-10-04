---
title: "Braintree Brazil Activity Report"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/br/reporting-reconciliation/activity-report"
raw_files:
  - "braintree/articles/br/reporting-reconciliation/activity-report-2026-09-16.md"
tags: [braintree, brazil, reporting, reconciliation, installments, disbursements]
---

## Overview

This collected Braintree document-version-1.1 page describes the Brazil Activity Report as a daily, previous-processing-day report of transactions that were **Submitted for Settlement** or **Settlement Declined**. Its stated purpose is to support receivables forecasting with projected disbursement dates and total transaction fees, including installment adjustments caused by refunds or disputes. It is a dated reporting snapshot, not proof that a transaction settled, a disbursement occurred, or funds reached a deposit account.

## Key takeaways

- The report-event scope is status-qualified: it covers the prior processing day's transactions in the two named states, rather than completed settlement alone. It covers credit- and debit-card sales and refunds, newly created installments, and installment adjustments.
- For Brazil card transactions, the page describes a 2-to-30-day disbursement range depending on card type, gives 30 days as the default, and says Predefined Funds Anticipation lets merchants pay a premium to accelerate credit-card funding. Its table lists 30 days for credit cards and 2 days for debit cards. These collected values and the premium feature are snapshot guidance, not a current SLA, rate schedule, merchant-specific agreement, or eligibility determination.
- A newly created installment's Projected Disbursement Date is initially `NULL` and is described as being populated within twelve hours. The page says installment records should be stored separately because they are paid over time and need individual reconciliation.
- Refunds and lost disputes adjust every installment equally according to the page. Adjustments can affect installments already disbursed or still due; an adjustment to an already-disbursed installment is described as being netted from the next disbursement and therefore needing separate tracking.
- The data dictionary distinguishes presentment currency and amount from settlement currency and amount. It also identifies the Merchant Account ID used to process the transaction and a Total Fee Amount assessed upon disbursement; the page does not supply an exchange-rate rule, a fixed report currency, a numeric fee schedule, or merchant-account eligibility criteria.

> [!warning] Projection and money-movement boundary
> `Submitted for Settlement` is not the same as settled, and a Projected Disbursement Date is a forecast rather than proof of settlement, disbursement, bank arrival, or final reconciliation. The report's status and projected-date records must not be converted into claims that a particular money-movement event completed.

> [!warning] Brazil, account and pricing snapshot
> The page was fetched on 2026-09-16, carries document version 1.1 and page metadata dated 2025-04-02, and sits on a `/br/` route with Brazil-specific timing prose. That provenance does not establish current policy, availability for every Brazil merchant account, the price or eligibility of Predefined Funds Anticipation, or applicability to a sibling region or processor route.

## Detail locators

- Document version and changelog: `## Document Version 1.1`, raw lines 17-19; `## Changelog`, raw lines 185-190.
- Daily report event scope, purpose, fees and installment-adjustment coverage: `## Report Definition`, raw lines 22-32.
- Brazil card timing, default timing, paid anticipation feature and card-type table: `## Obtaining projected disbursement dates`, raw lines 35-44.
- Standard sale/refund record matching and projected-date storage: `### Standard sale and refund transactions`, raw lines 47-55.
- Initial installment response data, `NULL` projected date, twelve-hour population statement and separate-record guidance: `### Sale transactions with installments`, raw lines 57-67.
- Installment-adjustment causes, effects, netting and reconciliation treatment: `## Installment adjustments`, raw lines 78-123.
- Merchant-account, report-event date, presentment/settlement currency and amount, projected date, reason, adjuster and total-fee field meanings: `## Data dictionary of Activity Report`, raw lines 130-157.
- Record-type and payment-instrument value tables: `## Record types and subtypes`, raw lines 160-166; `## Payment instrument types and subtypes`, raw lines 169-182.

## Related

- Company: [[braintree]]
- Main concept: [[payment-reconciliation-reporting]]

## Raw Sources

- [[raw/braintree/articles/br/reporting-reconciliation/activity-report-2026-09-16|Braintree Brazil Activity Report]] - fully read 2026-09-16 snapshot of document version 1.1 covering prior-processing-day report events, projected disbursement and fee forecasting, installment adjustments, and the report data dictionary
