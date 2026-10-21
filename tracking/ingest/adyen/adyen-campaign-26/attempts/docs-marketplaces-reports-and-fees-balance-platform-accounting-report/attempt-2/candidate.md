---
title: "Adyen Marketplace Balance Platform Accounting Report"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/reports-and-fees/balance-platform-accounting-report"
raw_files:
  - "adyen/docs/marketplaces/reports-and-fees/balance-platform-accounting-report/2026-09-15.md"
tags: [adyen, marketplaces, platforms, reporting, reconciliation]
---

## Overview

This 2023-modified Marketplace field guide, captured 2026-09-15, describes the daily **Balance Platform Accounting Report** for balance changes across all balance accounts in the platform, including the marketplace liable account and user accounts. The ordinary report can be generated on a schedule or manually for one day. The manually generated **Interactive Report** uses the same kind of data but can cover multiple dates and filter account holder, balance account, event Category, Type and Status. [[adyen]] [[adyen-reporting]]

## Key takeaways

- Use report rows to reconcile processed payments, internal transfers, bank-payout balance entries, fees/costs and invoice deductions. For current individual payment state, the guide recommends API responses and webhooks, then daily fund reconciliation with this report. A `bankTransfer` booked row shows a balance-account debit/credit, not independent evidence that the beneficiary bank received funds (raw lines 19–40, 61–96).
- The guide calls **Transfer Id** a pending debit/credit flow: initiated and then authorized/refused events share it. Refunds start a new flow with a new Transfer Id unlinked to the original payment. **Transaction Id** identifies a booked debit/credit; use Transfer Id to associate its booking with the pending flow. Do not equate `received` or `authorised` with booked movement (raw lines 50–57, 231–235).
- Category/Type/Status distinguish bank, internal, platform-payment, issued-card, grants, top-up and other events. Event status updates appear on their status-update day. The guide maps `internal/internalTransfer/booked` to source debit and target credit, and `bank/bankTransfer/booked` to a balance-account debit or credit. `platformPayment` capture/refund/chargeback and `topUp` have separate maps; use the raw tables for each type/status rather than treating all rows as settled sales or completed payouts (raw lines 59–199).
- **Value-date accounting:** Booking Date is when an event took place; Value Date is when the actual balance is credited/debited or available. It can precede, equal or follow booking date. Generated daily reports select balance mutations by Booking Date from 00:00 to next-day 00:00 for the selected day in **Central European Time (CET)**; individual rows also carry Booking/Value Date TimeZone columns. Balance accounts with no transactions are omitted, so report coverage does not mean a zero-activity account has a row (raw lines 200–220, 228–246).
- Standard columns include platform/account-holder/balance-account IDs, Transfer and Transaction IDs, Category/Status/Type, booking/value dates, account and payment currencies, Received/Reserved/Balance register mutations, counterparty account and PSP references. Customer Area can add optional columns including Exchange Rate, Event Id, Capital/Managed Risk fields and **Platform Payment Split Type**. The snapshot marks the additional **Issued Card Scheme Fee** and currency columns “Do not use this column.” Column presence/fee granularity depends on configured report and acquirer data (raw lines 216–347).
- Split types identify the purpose and booking destination of a transaction split: `BalanceAccount` is user share; `Commission` is marketplace commission to the liable balance account; fee, VAT, remainder, surcharge and top-up types use their specified account. The field supports split-line reconciliation; it does not by itself prove a split request was executed in a live payment (raw lines 349–371).
- **Sample inconsistencies:** chargeback prose says EUR 60 but its chargeback rows show EUR 10.97 (raw lines 391–404). The `Top-ups` rows reuse the payout example's Transfer Id `3JTRKZ5VXL07G5UY`, remain `received` with blank Transaction Ids, yet one shows `Balance (PC): 100.00` (raw lines 425–435); do not infer a reliable payout/top-up join or booked top-up from those rows. The report examples are illustrative, not proof of actual account outcomes.

## Detail locators

- Scope, generation, use cases and transfer/transaction definitions: raw lines 17–57. Category/Type/Status maps: lines 59–199. Value dates and report window: lines 200–220.
- Standard and optional columns, availability and split types: raw lines 222–371. Worked capture, refund, chargeback, internal transfer, bank payout and top-up rows: lines 373–435.

## Related

- [[adyen]] — provider.
- [[adyen-reporting]] — report and reconciliation concept.
- [[adyen-platforms]] — Marketplace/platform account context.
- [[source-adyen-docs-platforms-reports-and-fees-balance-platform-accounting-report]] — separate Platforms-path guide.
- [[source-adyen-docs-platforms-prepare-reports-generate-download-reports]] — existing Platforms-path report-generation route.

## Raw Sources

- [[raw/adyen/docs/marketplaces/reports-and-fees/balance-platform-accounting-report/2026-09-15|Marketplace Balance Platform Accounting Report — 2026-09-15 snapshot]]
