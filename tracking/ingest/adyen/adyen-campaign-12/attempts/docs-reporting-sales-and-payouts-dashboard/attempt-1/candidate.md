---
title: "Sales to payouts dashboard | Adyen Docs"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/reporting/sales-and-payouts-dashboard"
raw_files:
  - "adyen/docs/reporting/sales-and-payouts-dashboard/2026-09-15.md"
tags: [adyen, reporting, sales, payouts, balances]
---

## Overview

This 2026-09-15 [[adyen]] Docs snapshot describes the Customer Area **Sales to payouts** dashboard for a selected merchant account and date range. Its Sales and Payouts tabs summarize different transaction-status sets and show day/week/month charts and batch details. Dashboard labels and a bank instruction letter are reporting/tracing aids, not independent evidence that a bank credited funds. [[adyen-reporting]]

## Key takeaways

- From **Balances** > **Sales to payouts**, a company-account user is prompted to choose a merchant account and then a date range. The page describes CSV export. It does not state access roles, chart currency, time zone or date-cutoff rule; do not infer those from the selected range or screenshots.
- On **Sales**, Sales totals transactions in `SentForSettle` or `Settled`; Refunds totals `SentForRefund` or `Refunded`; Sales minus Refunds is their difference; Pending includes `SentForSettle` and `SentForRefund`. Therefore the Sales amount includes pending settlement and must not be read as settled-only sales. Sales and refund history bars use pending, ready-for-payout and paid-out categories, with selectable day/week/month increments.
- Selecting a Sales history bar opens batch-level details (batch number, payout status, sales, sales minus refunds) and a payment-method breakdown. The cited May 06 screenshot is an example, not a general date or amount rule.
- On **Payouts**, Sales and Refunds count `Settled` and `Refunded` transactions respectively, and the summary adds transaction costs, adjustments and the amount described as paid out to the bank account. Adjustment examples include chargebacks, deposit corrections, invoice deductions and balance transfers. Payout history and expanded batch details can show batch payout status, amounts and adjustment breakdown.
- The dashboard provides batch-detail CSV and a bank instruction letter whose details can help track a payout to the bank. Its payout status and letter do not independently verify arrival in, or credit by, the merchant's bank account.

## Detail locators

- **Dashboard access, merchant account, date range, tabs and CSV export:** raw lines 19–31.
- **Sales summary status definitions, charts and batch drilldown:** raw lines 33–73.
- **Payouts summary, history, batch details and bank instruction letter:** raw lines 75–116.

## Related

- [[adyen]]
- [[adyen-reporting]]
- [[source-adyen-docs-reporting-settlement-reconciliation-transaction-level]] — transaction reconciliation within payout batches

## Raw Sources

- [[raw/adyen/docs/reporting/sales-and-payouts-dashboard/2026-09-15|Adyen Sales to payouts dashboard — collected 2026-09-15]]
