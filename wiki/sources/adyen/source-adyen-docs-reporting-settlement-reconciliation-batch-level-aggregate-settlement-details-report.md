---
title: "Aggregate settlement details report | Adyen Docs"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/reporting/settlement-reconciliation/batch-level/aggregate-settlement-details-report"
raw_files:
  - "adyen/docs/reporting/settlement-reconciliation/batch-level/aggregate-settlement-details-report/2026-09-15.md"
tags: [adyen, reporting, settlement-reconciliation, aggregate-report, merchant-payout]
---

## Overview

This 2026-09-15 [[adyen]] Docs snapshot defines the Aggregate settlement details report for **batch-level** settlement reconciliation. It shows payout batches in a selected date range, with credits, debits and transaction counts split by merchant account, store, terminal, payment method, journal type and creation date. This is an aggregate entry report, distinct from a transaction-level Settlement details report. [[adyen-reporting]]

## Key takeaways

- The report is available at company-account and merchant-account scope. It can be retrieved manually or automatically. The selected Customer Area date range follows **Batch Closed Date**, which is the date the settlement batch closed and resulted in `MerchantPayout` and/or `BalanceTransfer` to the next batch. The report uses the account's time-zone setting. See raw lines 19–36, 75–79.
- Its first two lines summarize account code, start/end dates, possible aggregation criteria and multiple country codes. Subsequent lines are separate aggregate entries. Default fields include account/store/terminal, batch number, method, creation date/time zone, journal type, gross and net debit/credit columns, exchange rate, commission, DCC markup and transaction count. Store and terminal are empty for balance-level bookings such as `MerchantPayout` or fees, or when that dimension is not enabled. See raw lines 44–99.
- **Creation Date** is the sale day for payment-level bookings, related to terminal transaction or capture date; for balance-level bookings it is the Adyen booking timestamp. **Gross Currency** is transaction currency; **Net Currency** is settlement currency. Gross and net debit/credit occupy distinct columns; the raw defines `Net Debit` and `Net Credit` as request amounts less Bank/Card Commission. Bank/Card Commission includes markup, scheme fee and interchange. A negative DCC Markup indicates a credit to the account, not a universal sign rule for all amount fields. See raw lines 73–99.
- Optional fields include Payable booking date, a `MerchantPayout`-only payout reference, and Settlement Flow. The payout reference can match the description of a transfer on a bank statement, but its presence in this report does not prove that a particular bank received funds. Account-dependent reports may contain columns beyond the sample. Configuring columns or their order can affect automated consumers and requires one of Merchant admin, Merchant report, Merchant financial or Merchant POS Report roles. These are **column-configuration** roles; this page does not state a separate role requirement for generating the report. See raw lines 38–42, 101–130.

## Detail locators

- **Purpose, aggregation dimensions, account scope, date range and time zone:** raw lines 15–36.
- **Summary and entry structure:** raw lines 44–64.
- **Default journal, currency, amount, fee and count fields:** raw lines 66–99.
- **Optional columns, payout-reference scope and configuration roles:** raw lines 101–130.

## Related

- [[adyen]]
- [[adyen-reporting]]
- [[source-adyen-docs-reporting-settlement-reconciliation-transaction-level-settlement-details-report]] — distinct transaction-level report

## Raw Sources

- [[raw/adyen/docs/reporting/settlement-reconciliation/batch-level/aggregate-settlement-details-report/2026-09-15|Aggregate settlement details report — collected 2026-09-15]]
