---
title: "Adyen Platforms Liable account summary"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/reconciliation-use-cases/liable-account-summary"
raw_files:
  - "adyen/docs/platforms/reconciliation-use-cases/liable-account-summary/2026-09-15.md"
tags: [adyen, platforms, reporting, reconciliation, liable-accounts]
---

## Overview

This 2026-09-15 Adyen for Platforms guide describes the **Liable account summary** Customer Area dashboard for aggregated financial activity on a platform's liable balance accounts. It shows starting and ending balances and totals for adjustments, commission, fees, and other activity over a selected date range. It is a high-level reconciliation aid, not a transaction ledger, final accounting sign-off, or proof of bank receipt.

## Key takeaways

- Access requires the **Download Balance Platform reports** user role. From the merchant-account level, the view displays the liable balance accounts associated with the configured balance platform account. Filters are date range, all or one liable balance account, and currency. The date data uses the account's configured timezone and sales-day-payout settings; data becomes available at the close of each sales day. Categories appear only when underlying data exists in the selected period, so absence of a category is period/filter dependent.
- The dashboard calculates ending balance from starting balance plus aggregate adjustments, commission, fees, and others. Selecting a category shows transaction-type counts and amounts. Adjustments cover movements such as bank transfers, top-ups, internal transfers, invoice deductions and reserve changes; commission includes liable-account splits as well as refund and chargeback effects; fees cover transaction fees. These are category aggregates and sign-sensitive balance movements, not a list of individual payment references.
- For transaction-level lines and reference tracing, use the **Balance Platform Accounting Report**; the summary itself has no transaction-level data. Its category-reference tables map dashboard items to report `category`/`type` values, including `platformPayment` capture/refund/chargeback, `bank` `bankTransfer`, `internal` movements, and `topUp`. The raw table also distinguishes fee-related columns from aggregated processing-fee `type=fee` rows; consult the exact report fields before joining or summing.
- The dashboard shows only fees charged to the liable account. The liable-account timezone differs from the Payment processing invoice's CET period; when fees are split with account holders, liable-account booked fees will not match all invoice fees. Reconciliation therefore needs report/period/account alignment and other sources. A bank-transfer category row is an accounting cross-reference, not independent proof that a bank transfer settled or reached its beneficiary.
- The page presents month/quarter/year book closing as a use case for the dashboard, but explicitly calls for a combination of reports for a complete reconciliation workflow. A selected dashboard period or matching total alone does not establish accounting approval or a completed live money movement.

## Detail locators

- `## Access the summary` / `### Filter the summary`: role, merchant-account route, account/currency/date filters, sales-day timing and timezone.
- `## Understand the summary`: balance formula and category drilldown.
- `### Reconcile with other reports`: transaction-level accounting report and invoice mismatch qualifications.
- `## Categories`: category meanings and report cross-reference table for adjustments, commission, fees and others.

## Related

- [[adyen-reporting]] — main reporting and reconciliation concept.
- [[adyen-platforms]] — parent Platforms context.
- [[adyen]] — provider profile.

## Raw Sources

- [[raw/adyen/docs/platforms/reconciliation-use-cases/liable-account-summary/2026-09-15|Adyen Liable account summary guide (fetched 2026-09-15)]]
