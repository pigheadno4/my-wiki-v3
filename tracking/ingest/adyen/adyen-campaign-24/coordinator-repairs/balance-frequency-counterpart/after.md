---
title: "Adyen Classic Platforms: Reports and fee types"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/reports-and-fees"
raw_files:
  - "adyen/docs/classic-platforms/reports-and-fees/2026-09-15.md"
tags: [adyen, classic-platforms, reporting, reconciliation, fees]
---

## Overview

This 2023-modified, 2026-09-15-captured **Classic Adyen for Platforms** catalog maps Adyen-account and platform-account-holder reports to payment-to-payout reconciliation and fee analysis. It routes new implementations to the separate newer integration guide. This page selects report types and describes fee locations; the linked reports and reconciliation guides own their row grain, settings and procedures. See [[adyen]] and [[adyen-classic-platforms]].

## Key takeaways

- **Adyen-account reports** cover payment processing and invoices. This page labels **Payment accounting report**, **Settlement details report**, and **Monthly invoice** as required for full financial reconciliation. Payment accounting covers payment lifecycle events and their transaction-related fees, including unsettled events, but **excludes platform transaction charges** for payouts, fund transfers and KYC checks. Settlement details covers a payable batch's payment transactions, assessable costs and periodic balance adjustments; the invoice summarizes prior-month fees and adjustments. Received payment details supplies interaction, method and status context.
- **Platform reports** tie events to Classic account holders and their account balances. The page also labels **Marketplace Payments accounting report** as required for full financial reconciliation; it tracks pending and credited/debited changes, including liable and account-holder accounts, at daily or hourly grain. This hub describes Marketpay Balance Report balances as available on a daily basis; the child [[source-adyen-docs-classic-platforms-reports-and-fees-marketpay-balance-report]] separately lists Daily, Weekly, or Monthly report frequency. These descriptions do not establish a daily-only delivery cadence. Marketpay Payout Report lists transactions in a day's payout, but the page says to use it **only for accounts configured with scheduled payouts**. Do not substitute these Classic Marketpay reports for similarly named modern Balance Platform reports.
- The page says Adyen deducts fees from settlement and debits the platform's **liable account**. A monthly fee reconciliation needs totals and breakdowns across reports: Settlement details for settled-transaction fee breakdown, Payment accounting for transaction fees including unsettled items, and Payment processing invoice for monthly totals and monthly charges. Example fee locations include Fund Transfer/Payout/Sub-Merchant Verification service charges in the monthly invoice; the table marks FanF and Merchant Location Fee as **US-only**. These are possible fees, not proof every platform incurred each one.
- A report catalog, sample fee location or payable-batch description does not establish that a particular payment settled, payout reached a bank, or books reconcile. The page routes onward to report preparation and worked reconciliation use cases.

## Detail locators

- Pinned raw lines 15–29: Classic scope, account-versus-platform report distinction and payment-to-payout purpose.
- Pinned raw lines 31–40: Adyen-account report selection and three full-reconciliation labels; lines 42–50: platform report grain, Marketplace Payments label and scheduled-only Marketpay Payout.
- Pinned raw lines 52–77: liable-account fee direction, cross-report fee basis and possible fee table, including US-only entries.
- Pinned raw lines 79–91: preparation and reconciliation-guide routes.

## Related

- [[adyen-classic-platforms]] — Classic account/funds model.
- [[source-adyen-docs-classic-platforms-prepare-reports]] — configuration, download and report joins.
- [[adyen-reporting]] — broader Adyen reporting context; use each product's own report definitions.
- [[adyen-platforms]] — newer model with separate Balance Platform reports.

## Related raw API references

- [[raw/adyen/docs/classic-platforms/reports-and-fees/marketplace-payments-accounting-report/2026-09-15|Marketplace Payments accounting report]]; [[raw/adyen/docs/classic-platforms/reports-and-fees/marketpay-balance-report/2026-09-15|Marketpay Balance Report]]; [[raw/adyen/docs/classic-platforms/reports-and-fees/marketpay-payout-report/2026-09-15|Marketpay Payout Report]] — child report definitions, navigation only.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/reports-and-fees/2026-09-15|Classic Platforms reports-and-fees catalog, captured 2026-09-15]]
