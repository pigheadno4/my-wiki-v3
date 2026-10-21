---
title: "Adyen Classic Platforms Marketpay Payout Report"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/reports-and-fees/marketpay-payout-report"
raw_files:
  - "adyen/docs/classic-platforms/reports-and-fees/marketpay-payout-report/2026-09-15.md"
tags: [adyen, classic-platforms, payouts, reporting, reconciliation]
---

## Overview

The Marketpay Payout Report is a Classic Platforms CSV for reconciling each account holder's automatic payout with included debit and credit transactions. It is available only for automatic payouts and describes payouts initiated within the day. This is Classic account-holder/account reporting, distinct from modern balance-platform payout reports. See [[adyen]] and [[adyen-classic-platforms]]. A reported payout or `Payout` record is not, by itself, evidence of beneficiary-bank receipt; Classic payout notifications and returns require separate tracking.

## Key takeaways

- The report uses the configured reporting time zone. Filter by **Account Holder**, **Account**, and **Currency** to identify transactions for a particular account. The page says it generates one record line per account per currency, while its structure section says each line is a separate entry and its record-type table includes transaction types; read the row's `Record Type` rather than assuming every entry is a payout summary.
- Pending refunds or chargebacks can withhold an amount from payout, leaving a non-zero `Rolling Balance` on that account's payout line. The remaining balance carries into the next report for reconciliation; it is not a lost amount or proof of a later payout.
- The file pattern is `marketpay_payout_YYYY_MM_DD.csv`; Customer Area subscription can be Daily, Weekly, or Monthly. The first line names the report, the second is the header, and subsequent lines are entries. Key columns include account-holder/account identifiers, several distinct payment/modification/payout references, booking date and report time zone, currency, amount and rolling balance.
- Record types distinguish settled credits, reversed or failed credits/debits, refunds, chargebacks and reversals, inter-account `FundTransfer`, `Payout`, and `VirtualAccountPayoutReturned`. For `TransferBalance`, earlier report versions include payment costs; on new platforms it covers credits/debits not booked because of missing split instructions/reference or a technical issue, with other postings such as payment costs under separate types including `Fee`. This is a version/lifecycle distinction, not a universal mapping.
- `DeprecatedManualCorrected` remains for existing platforms and is replaced for new platforms by `ManualCorrectionCredited` and `ManualCorrectionDebited`. The asterisked new `Fee`, deposit correction, invoice deduction, merchant pay-in/reversal and manual-correction types are enabled by default for new platforms; existing platforms are told to contact Support to enable them. A report row states an accounting classification in this snapshot, not successful external settlement or bank credit.

## Detail locators

- Report purpose, time-zone effect, automatic-payout-only scope, filters, withheld amount and rolling-balance carry: raw lines 15–27. Filename, subscription, frequency and sample link: lines 29–35.
- File structure and full column definitions, including distinct PSP references and amount meanings: lines 37–66. All record-type definitions and old/new-platform accounting qualification: lines 68–96.

## Related

- [[adyen]] — provider context.
- [[adyen-classic-platforms]] — Classic account-holder/account and payout model.
- [[source-adyen-docs-classic-platforms-reports-and-fees]] — Classic report selection hub.
- [[source-adyen-docs-classic-platforms-payouts-payout-notifications]] — separate payout-status and possible bank-return tracking.
- [[source-adyen-docs-classic-platforms-prepare-reports]] — report configuration and reconciliation joins.

## Related raw API references

- The raw page links to the time-zone setting, automatic-payout guide, sample CSV and reconciliation use cases; their linked contents are separate evidence.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/reports-and-fees/marketpay-payout-report/2026-09-15|Adyen Docs: Marketpay Payout Report (2026-09-15 snapshot)]]
