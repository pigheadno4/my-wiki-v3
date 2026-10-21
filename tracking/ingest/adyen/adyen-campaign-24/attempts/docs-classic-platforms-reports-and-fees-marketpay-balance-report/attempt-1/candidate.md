---
title: "Adyen Classic Platforms Marketpay Balance Report"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/reports-and-fees/marketpay-balance-report"
raw_files:
  - "adyen/docs/classic-platforms/reports-and-fees/marketpay-balance-report/2026-09-15.md"
tags: [adyen, classic-platforms, reporting, reconciliation, balances]
---

## Overview

This 2023-modified [[adyen-classic-platforms]] report reference from [[adyen]], captured 2026-09-15, defines the Marketpay Balance Report for balances across platform account holders and their accounts. It is a Classic account-balance snapshot/report route, not a transaction ledger, verification result, payout confirmation or bank-receipt record. Keep its virtual-account fields distinct from modern Balance Platform resource naming.

## Key takeaways

- The report uses the **CET** time zone. The stated filename pattern is `MarketPay_balance_YYYY_MM_DD.csv`; subscription is **Default** and frequency can be **Daily, Weekly, or Monthly**. The existing Classic reports hub summarizes it as daily account balances, while this child reference explicitly lists all three frequencies; use this page's frequency field for the report definition. See raw lines 19–29.
- The first four lines are report summary text, including a report time and “Accounts balance”; line 5 is the header, and each subsequent line is a separate entry. The raw page links to a sample CSV, but does not inline its full contents. See raw lines 31–50.
- Columns identify **Marketplace**, **Account Holder** (`accountHolderCode`), **Virtual Account** (`accountCode`, printed as 9- or 16-character limit), and a three-character ISO **Currency**. **Balance** is available balance; **Pending Credit** and **Pending Debit** are their respective pending balances for that virtual account and currency. All three amount columns are fixed-point numbers in **minor units**. Do not read them as major-unit amounts or infer a completed payout. See raw lines 52–64.
- The page routes use of the report to reconciling platform account balances in a separate transactional-ledger guide. It does not supply a per-transaction movement history, formula reconciling to a bank account, or a current account-specific report. See raw lines 23–25 and 48–64.

## Detail locators

- CET, report purpose, filename, subscription and frequency: raw lines 19–29.
- Sample link, four summary lines, header and entry grain: raw lines 31–50.
- Column names, identifiers, currency and minor-unit balance fields: raw lines 52–64.

## Related

- [[adyen]] — provider profile.
- [[adyen-classic-platforms]] — Classic account/report model.
- [[source-adyen-docs-classic-platforms-reports-and-fees]] — Classic report hub; its daily-only summary is narrower than this child page's Daily, Weekly, or Monthly frequency line.
- [[source-adyen-docs-classic-platforms-reconciliation-use-cases-build-transactional-ledger]] — separate account-balance reconciliation steps.
- [[adyen-reporting]] — broader report navigation, without equating Classic and modern reports.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/reports-and-fees/marketpay-balance-report/2026-09-15|Marketpay Balance Report — pinned 2026-09-15 raw snapshot]]
