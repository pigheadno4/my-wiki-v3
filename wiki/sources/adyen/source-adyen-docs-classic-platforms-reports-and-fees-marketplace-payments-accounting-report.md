---
title: "Adyen Classic Platforms: Marketplace Payments accounting report"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/reports-and-fees/marketplace-payments-accounting-report"
raw_files:
  - "adyen/docs/classic-platforms/reports-and-fees/marketplace-payments-accounting-report/2026-09-15.md"
tags: [adyen, classic-platforms, reporting, reconciliation, ledger]
---

## Overview

This 2023-modified, 2026-09-15-captured **Classic Adyen for Platforms** page defines the Marketplace Payments accounting report for financial status changes, events and modifications across marketplace/platform payments. It proposes the report for a transactional ledger across platform accounts and for reconciling fees debited from the platform's liable account. This is a Classic account-holder/account report, not a modern Balance Platform report. [[adyen]] [[adyen-classic-platforms]] (raw lines 15–25)

## Key takeaways

- The report is a default subscription at hourly or daily frequency. The daily filename is `marketplace_payments_accounting_report_YYYY_MM_DD.csv`; the hourly filename adds `hourly` and `HH_UTC`. The page says the platform's time-zone setting affects report data, so the period and time-zone basis must be checked when reconciling rows. (raw lines 19–33)
- Each line below the header is a separate entry, rather than a whole-payment summary. The columns identify marketplace, account holder and account; carry separate action, payment, modification, payout and chargeback PSP references; and include booking date/time-zone, main amount/currency, record type and balance currency. The Payment PSP reference may be empty for a non-payment action. Use the individual column definitions for joins and the sample only as an example. (raw lines 35–69)
- `Record Type` identifies whether an entry changes the pending balance, available `Balance (BC)`, or both. `PendingCredit` is a captured payment still unavailable for payout because Adyen has not received funds; `Credited` moves settled funds into available balance. `PendingDebit` is an initiated refund before deduction; `Debited` records the deduction. Failed/reversed credit or debit, chargeback, second chargeback and fund-transfer records have distinct effects in the table. Do not equate a pending booking with settled, payable funds. (raw lines 66–69, 85–109)
- Bank-account `Payout` and `VirtualAccountPayoutReturned` rows differ from card `PayoutInitiated`, `PaidOut` and `PayoutFailed`. A card `PayoutInitiated` row deducts available balance at initiation and must not be read as a completed payout or bank receipt. `PendingFundTransfer` is limited to beneficiary-setup accounts. (raw lines 107–114)
- `TransferBalance` has a version boundary: older report versions include payment costs in the aggregate; for new platforms it is limited to credits/debits that could not be booked because split instructions/reference were missing or a technical issue occurred. The table's prose calls the separate payment-cost type `Fee`, while the immediately following record-type row is labeled `NewFee`. Preserve both labels as a source discrepancy rather than silently normalizing them. The `NewFee`, deposit correction, invoice deduction, merchant pay-in/reversal and manual-correction types are default for new platforms; existing platforms must contact Support to enable them. (raw lines 115–125)
- **Dated California column difference:** This report's column table still describes `Refund terms` as California-bank-payout “Right To Refund” text (raw line 73). The fully read Classic release notes state under **2022-03-14 — Reports** that Adyen removed that text from the column for California bank payouts (release-note raw lines 412–416). Thus the table is not evidence that the text remains populated in a later report. The captured pages leave the column's exact later value unspecified.
- The report specifies booked platform/account balances and record meanings. It does not by itself prove that any particular payment settled, a payout completed, or a bank received funds.

## Detail locators

- Raw lines 49–79: full column types and definitions, including account identifiers, different PSP references, `Pending (BC)`, `Balance (BC)`, conditional exchange rate, payout bank details and reserved columns.
- Raw lines 85–125: full record-type/affected-balance matrix, including reversal, chargeback and liable-account adjustment types and the Support opt-in note.
- Classic release-note raw lines 356–366: 2022-04-11 addition of chargeback references and 2022-04-04 UTC hourly-generation fix; lines 412–416: California `Refund terms` text removal; lines 459–463: 2022-02-21 card-payout booking-duplication fix. These dated changes do not establish a live report configuration.

## Related

- [[adyen-classic-platforms]] — Classic account-holder/account model.
- [[source-adyen-docs-classic-platforms-reports-and-fees]] — parent report selection and fees catalog.
- [[source-adyen-docs-classic-platforms-release-notes]] — dated report changes. Fully read counterpart: [[raw/adyen/docs/classic-platforms/release-notes/2026-09-15|Classic Platforms release notes, captured 2026-09-15]].

## Raw Sources

- [[raw/adyen/docs/classic-platforms/reports-and-fees/marketplace-payments-accounting-report/2026-09-15|Marketplace Payments accounting report, captured 2026-09-15]]
