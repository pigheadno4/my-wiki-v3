---
title: "Adyen for Platforms reporting quickstart"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/quickstart-guide/reporting"
raw_files:
  - "adyen/docs/platforms/quickstart-guide/reporting/2026-09-15.md"
tags: [adyen, platforms, reporting, reconciliation, payouts]
---

## Overview

This 2026-09-15 Adyen for Platforms quickstart orients a platform to user-facing dashboard components and custom reports for reconciling balance-platform accounts, payouts, invoices, and payment processing. It is a report-selection and data-consumption guide, not a report schema or proof of an individual payout. Customer Area reports are not directly available to platform users; the platform may need to filter data by balance account before sharing it.

## Key takeaways

- The guide presents Transactions Overview and Payouts Overview components for user dashboards. Its Report Overview/Reports Component wording is time-sensitive: the snapshot says a report-download component is planned or soon available, while also saying current availability is only for the Payout Report. Verify the actual component and report availability before promising it to users. A dashboard label saying a payout was received does not independently establish beneficiary bank receipt.
- For custom reconciliation, distinguish **booking date**, when an event occurs, from **value date**, when a balance account is credited or debited and funds become available there. Settlement delay can put value date after the sales day; the source's Monday-to-Wednesday two-business-day case is an example, not a general SLA. A balance-account value date is not a bank-credit date.
- The Balance Platform Payout Report (BPPR) is described as a daily report of scheduled payouts initiated that day and constituent transactions. Its reconciliation use is limited to managed or custom scheduled payouts, excludes on-demand payouts and cashouts, requires the sales-day settlement model, and can produce incorrect data when more than one scheduled payout occurs on a day. Do not apply its payout composition to unsupported routes or treat an initiated-report row as recipient receipt.
- The Balance Platform Accounting Report (BPAR) tracks platform balance changes such as processed payments, internal transfers, payouts, fees and invoice deductions. Adyen recommends ingesting BPARs for a ledger and excluding status events without actual account money movement, including Received, Authorized, Canceled and Expired. Combine it with the Balance Platform Balance Report for balance reconciliation; preserve row status, account, currency, booking/value dates and report grain. A report row or calculated balance does not establish legal fund ownership or an external bank outcome.
- The page also routes invoice fee checks to Interactive Payment Accounting Report status filters; identifies Fee, Statement, Payment Accounting and Settlement Detail reports for their own distinct purposes; and offers scheduled daily or manual report generation. The linked report specifications govern exact fields, access, cutoff and retention.

## Detail locators

- Opening and `Dashboard components for key use cases` — component versus custom-report options, Customer Area user-access/filtering boundary, Transactions/Payouts/Report Overview state and recommendations (raw lines 15–62).
- `Adyen invoice reconciliation` — IPAR fee-status filters for processing, payment-method and RevenueProtect fees (lines 64–72).
- `Key reporting concepts` — booking date versus value date and settlement-delay example (lines 80–98).
- `Key reports` / `Balance Platform Payout Report` — scheduled-payout report grain, managed/custom-scheduled-only scope, same-day multiplicity warning and sales-day model (lines 99–117).
- `Balance Platform Accounting Report` and `Balances` — balance-change categories, ledger recommendation, nonmovement-status exclusion and Balance Report pairing (lines 119–136).
- Remaining report catalog and `Reporting cadence and consumption` — fee/statement/payment-accounting/settlement-detail roles and daily/manual generation routes (lines 138–175).

## Related

- Company: [[adyen]]
- Main concept: [[adyen-reporting]]
- Platform context: [[adyen-platforms]]
- Related sources: [[source-adyen-docs-platforms-reports-and-fees-payout-report]], [[source-adyen-docs-platforms-reports-and-fees-balance-platform-accounting-report]]

## Raw Sources

- [[raw/adyen/docs/platforms/quickstart-guide/reporting/2026-09-15|2026-09-15 Platforms reporting quickstart]]
