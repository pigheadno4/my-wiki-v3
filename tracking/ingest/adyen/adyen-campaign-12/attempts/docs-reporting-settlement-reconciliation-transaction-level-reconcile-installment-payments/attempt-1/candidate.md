---
title: "Adyen installments and advancements in Brazil"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/reporting/settlement-reconciliation/transaction-level/reconcile-installment-payments"
raw_files:
  - "adyen/docs/reporting/settlement-reconciliation/transaction-level/reconcile-installment-payments/2026-09-15.md"
tags: [adyen, brazil, installments, advancements, reporting, reconciliation]
---

## Overview

This 2026-09-15 Adyen guide describes **Brazil-specific credit-card installment and advancement flows** and routes readers to the reports used to track installments, refunds, forecast amounts, and advancement batches. In the described ordinary flow, the merchant receives each installment as the scheme pays it; advancements are an optional, separately enabled path for upfront funds. The journal states and report entries are not, by themselves, proof of a particular bank receipt or final accounting outcome. See [[adyen]] and [[adyen-reporting]].

## Key takeaways

- **Installment lifecycle and grain:** The page sequences `Received`, `Authorised`, capture/`SentForSettle`, one `SettledInInstallments` entry **per payment**, an `OpenInstallment` entry **per installment**, then a `SettledInstallment` entry for each installment when settled. That settled amount moves under the **Payable** report header for payout. A payment-level `SettledInInstallments` entry must not be counted as each installment having settled or arrived at a bank.
- **Refund lifecycle:** A refund request creates `SentForRefund`; `RefundedInInstallments` occurs when the shopper is refunded and is one entry per payment in installments. The page says its amount matches `SentForRefund`. Each installment also has an `OpenInstallment` entry paired with a `RefundedInstallment` entry under the Installments report header. Keep request, shopper refund, and per-installment report entries separate.
- **Report choice and signs:** Settlement details is the route for installment-level reconciliation. Monthly/Daily finance reports in installments summarize amounts credited or debited to the account: `SettledInstallment` is credit; `RefundedInstallment`, `Chargeback`, `SecondChargeback`, and some `SuspendInstallment` entries are debits, with `SuspendInstallment` not applying to every advancement type. The Forecast report estimates **net** amounts and dates, but refunds and chargebacks can make actual credited amounts differ. A forecast is not a payout or bank-arrival confirmation.
- **Open-installment status:** The Payment accounting report can track open installments if `Payout Date`, `Installments (PC)`, `Installment`, and `Booking Type` columns are enabled; the guide directs readers to Support if needed. `Installments (PC)` is described as credited amount, with a negative value indicating a refund debit. `Installment` is a sequence such as 2/6. `Booking Type` includes `FIRST` captured/sent to scheme, `ACCELL` accelerated due to a refund request, `REPRESENTMENT` after chargeback defense, and `RETRY` after an initial failed installment capture. These labels describe report classification, not a successful later payout or defense outcome.
- **Advancements and scope:** The guide says an enabled advancement can pay upfront for installment payments, within one day, and instructs merchants to contact an account manager or Support for fee details and enablement. For reconciliation it says advancements cover **batches** of installment payments sharing an advancement code; check `Advanced (PC)` and `Advancement Code` in Payment accounting, sum same-code `Advancement (PC)` rows, and compare with the amount received. This page does not give a fee rate or prove a specific merchant is eligible, enabled, paid, or reconciled. The separate [[source-adyen-docs-reporting-settlement-reconciliation-transaction-level-advancements-detail-report]] owns its own merchant-account grain and cost/fee fields.

## Detail locators

- Lines 15–29: Brazil-only scope, ordinary installments versus optional advancements, and coverage.
- `## Installments lifecycle`, lines 31–40: payment-versus-installment journal grain and report-header transitions.
- `### Installment refunds`, lines 42–48: request, shopper-refund and installment-entry sequence.
- `## Installment reports and reconciliation`, lines 50–78: Settlement details, finance-report credit/debit states and Forecast caveat.
- `### Track the status of open installments`, lines 80–99: required optional columns, signed `Installments (PC)`, sequence and booking-type meanings.
- `## Advancements`, lines 101–117: enablement/fee contact, stated timing, batch/code matching and comparison workflow.

## Related

- [[adyen-reporting]] — reciprocal reporting route.
- [[source-adyen-docs-reporting-settlement-reconciliation-transaction-level-advancements-detail-report]] — separate advancement report grain, cost and fee field definitions.
- [[source-adyen-docs-reporting-settlement-reconciliation-transaction-level-settlement-details-report]] — separate settlement-detail report field authority.

## Raw Sources

- [[raw/adyen/docs/reporting/settlement-reconciliation/transaction-level/reconcile-installment-payments/2026-09-15|Installments and advancements in Brazil, captured 2026-09-15]]
