---
title: "Balance Platform Accounting Report | Adyen Payout Service path"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/reports-and-fees/balance-platform-accounting-report"
raw_files:
  - "adyen/docs/payouts/payout-service/reports-and-fees/balance-platform-accounting-report/2026-09-15.md"
tags: [adyen, payout-service, reporting, reconciliation, balance-platform]
---

## Overview

This 2026-09-15-captured [[adyen]] Payout Service-path [[adyen-reporting]] reference describes the Balance Platform Accounting Report: a daily account-change report for **all** balance accounts in a balance platform, including liable and user accounts. It also describes a manually generated interactive variant with multi-day, account and event filters. The report's columns identify financial-service applicability across issuing, payouts and platform payments; the Payout Service URL does not make every column or split type a Payout Service-only rule. See raw lines 15–29 and **Report structure**.

## Key takeaways

- The daily report can be generated automatically on a schedule or manually for a day; the interactive report is manual, with date-range, account-holder/balance-account and Category/Type/Status filters. The page lists processed payments, internal transfers, bank payouts and fees/invoice deductions as reconciliation uses. For current individual-payment status it recommends API responses/webhooks, followed by daily report reconciliation (raw lines 19–40). A report row alone is not an independently verified beneficiary-bank receipt.
- A **Transfer Id** groups pending credit/debit events: initiated then authorized or refused, with no booked money movement yet. A refund starts its own received/authorised/refunded transfer and new Transfer Id rather than linking to the original payment's Transfer Id. A **Transaction Id** marks a debit or credit booked on a balance account, and its Transfer Id can link it back to the transfer. Do not treat transfer receipt/authorization as a booked balance change; a booked bank-category balance-account debit still does not confirm receipt by an external bank beneficiary (raw **Transfers and transactions**, lines 50–55; **bank event category**, lines 71–79).
- Category, Type and Status distinguish platform-payment, internal, bank and card events; the page maps bank booked/returned/rejected, card booked, and internal fee/transfer/return/correction cases in its event tables. The report contains events on the day each status update occurs (raw **Events in the report**, lines 57–114). Use the exact category/type/status row before assigning financial meaning.
- The report uses value-date accounting: Booking Date identifies when the event occurred, while Value Date identifies when the balance-account amount is available or debited. The two may differ, and Value Date need not be after Booking Date. The generated report covers booking-date mutations from midnight to the following midnight for the selected day in **CET**; accounts with no transactions do not appear (raw lines 116–136, 144–146). A missing row is therefore not proof that an account has a zero balance.

## Detail locators

- The daily and interactive generation routes and intended uses: raw lines 19–40.
- Event category/type/status reference, including bank returns and internal-transfer/fee/correction rows: raw lines 50–114.
- Received, authorised and captured EUR example with separate Booking/Value Dates: raw lines 116–126. Sample columns may differ from a generated report according to balance-platform settings (line 130).
- Standard fields, financial-service applicability and account/transfer/transaction/currency/register references: raw lines 132–238. Additional columns are excluded by default and can be added in Customer Area (lines 239–263).
- The cross-service split-type column and examples, including user-share, liable-account commission, fee, VAT, remainder and surcharge: raw lines 265–284. These are report labels, not evidence that a given Payout Service payment used a split.

## Related

- [[adyen-reporting]] — report grain and evidence boundary.
- [[adyen-payouts]] — Payout Service versus other disbursement models.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/reports-and-fees/balance-platform-accounting-report/2026-09-15|Balance Platform Accounting Report, captured 2026-09-15]]
