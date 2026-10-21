---
title: "Marketplace liable account summary"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/reconciliation-use-cases/liable-account-summary"
raw_files:
  - "adyen/docs/marketplaces/reconciliation-use-cases/liable-account-summary/2026-09-15.md"
tags: [adyen, marketplaces, reporting, reconciliation, liable-accounts]
---

## Overview

This 2026-09-15 [[adyen]] Marketplace guide describes the Customer Area **Liable account summary** dashboard for aggregated financial activity on a platform's liable balance accounts. For a selected period, account and currency it shows starting and ending balances and categories of adjustments, commission, fees and other movements. It aids reconciliation at the liable-account scope; it does not contain transaction-level records or prove bank receipt or accounting sign-off. [[adyen-reporting]]

## Key takeaways

- Access requires the **Download Balance Platform reports** user role. At the merchant-account level, the dashboard covers liable balance accounts associated with the configured balance platform account. Filters select date range, one or all liable balance accounts, and currency. Date data uses the account-configured timezone and Sales day payout configuration; data appears after each sales-day close. Categories appear only when there is underlying data for the selected period. See raw lines 30–52.
- Ending balance is starting balance plus aggregate Adjustments, Commission, Fees and Others; category selection shows a transaction-type breakdown with count, amount and total. Adjustments include bank transfers, top-ups, internal transfers and reserve changes; Commission includes liable-account splits, refunds and chargebacks. These are liable-account aggregates rather than payment-level proof. See raw lines 54–58 and 79–86.
- The summary lacks transaction-level data. Use the Balance Platform Accounting Report for the constituent records and the category-reference table for event mappings. A complete reconciliation workflow needs other reports too. See raw lines 60–70 and 90–142.
- The fee view covers only fees charged to the liable account. Its account timezone differs from the Payment processing invoice's CET period, and when fees are split with account holders, liable-booked fees will not match all invoice fees. Align account scope and time periods before comparison. See raw lines 72–77.
- The page names period-end book closing as a dashboard use case, but its own report caveat leaves accounting approval and live money-movement outcomes outside this summary's evidence. See raw lines 23–28 and 60–77.

## Detail locators

- **Purpose and role-gated access:** raw lines 15–44.
- **Date/account/currency filters, timezone and availability:** raw lines 46–52.
- **Balance formula and category drilldown:** raw lines 54–58.
- **Transaction-level and invoice comparison limits:** raw lines 60–77.
- **Category-to-accounting-report mapping, including fees:** raw lines 79–142.

## Related

- [[adyen-reporting]]
- [[adyen-platforms]]
- [[source-adyen-docs-platforms-reconciliation-use-cases-liable-account-summary|Parallel Platforms-path dashboard guide]]
- [[source-adyen-docs-marketplaces-reports-and-fees-balance-platform-accounting-report|Transaction-level accounting report reference]]

## Raw Sources

- [[raw/adyen/docs/marketplaces/reconciliation-use-cases/liable-account-summary/2026-09-15|Adyen Marketplace liable account summary — collected 2026-09-15]]
