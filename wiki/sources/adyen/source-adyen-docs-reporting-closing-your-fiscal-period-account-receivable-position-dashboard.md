---
title: "Adyen accounts receivable balance positions"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/reporting/closing-your-fiscal-period/account-receivable-position-dashboard"
raw_files:
  - "adyen/docs/reporting/closing-your-fiscal-period/account-receivable-position-dashboard/2026-09-15.md"
tags: [adyen, reporting, accounts-receivable, fiscal-close, reconciliation]
---

## Overview

This 2026-09-15 Adyen guide describes the Customer Area **Accounts receivable** dashboard for viewing open balance positions at selected Company or Merchant account scope and downloading a transaction CSV for fiscal-period reconciliation. It is reporting evidence for an account and selected date, not proof of bank receipt, final settlement, completed reconciliation, accounting treatment, merchant-of-record identity, or legal ownership of funds. See [[adyen]] and [[adyen-reporting]].

## Key takeaways

- **Access and availability:** The guide requires an online payments or Terminal API integration and the **Merchant Financial** Customer Area role to view the overview and download its report. It states that historical position views can be generated anytime after July 1, 2025; this does not specify the earliest historical position date; for Advancements processing the overview and report become available at the end of March 2026; and they are unavailable for transactions processed in India. These are dated guide claims, not a current entitlement check for a particular account.
- **Generation and time scope:** On first access, the user sets a monthly generation schedule for the selected Company or Merchant account. Calendar-month schedules produce an overview ready on the following month's first day; custom schedules use entered fiscal end dates and stop after the last entered date until more dates are added. After scheduling, users can generate additional historical dates with a selected time zone; generation may take time. The selected account, date, and time zone are essential to interpreting a position.
- **Position identities:** **Total receivable** is described as captured transactions not yet paid out, converted to the account's base currency when multiple currencies are involved. The Company base currency is its invoice currency; the Merchant base currency is its primary settlement currency. **Total balance** is the sum of total receivable, reserve, and deposit. The guide describes reserve as money added by the merchant to cover operational expenses when in-process funds are insufficient, and deposit as an Adyen-held amount for potential payment-processing liabilities; an account may have no deposit. These are distinct position categories, not interchangeable payout or bank-balance amounts.
- **Transaction report:** Generating an overview also generates a CSV for transactions making up the account's total receivable, downloaded from the dashboard for a selected overview date. The page explicitly says Adyen does not send this report via the usual report-ready webhook or configured SFTP delivery. Some columns are disabled by default and users may configure their selection/order. The structure also describes balance types `Capture`, `Deposit`, `Payable`, and `RefundReserve`; the example includes reserve rows. Read report rows and the exact balance type rather than assuming every sample row is an unpaid captured payment.
- **Evidence limits:** `Payable` is described as available for a next payout batch to close that date; this is not a bank-arrival or final payout claim. Reported positions and example CSV values should be reconciled against the merchant's own records and other applicable financial evidence before drawing an accounting conclusion.

## Detail locators

- `## Requirements`, lines 21–32: integration, role, historical-generation availability, Advancements and India limits.
- `## How it works` and `## Generate overviews`, lines 34–78: first-use schedule, monthly/custom dates, manual historical generation, account selection and time zone.
- `## Accounts receivable overview`, lines 80–103: receivable, total balance, reserve, deposit and base-currency definitions.
- `## Download a transaction report`, lines 105–122: CSV retrieval, absence of webhook/SFTP delivery, optional columns.
- `## Report structure`, lines 124–145: row fields, balance types, transaction/base currency and amounts; `## Report example`, lines 151–178: illustrative rows only.

## Related

- [[adyen-reporting]] — reporting concept and reciprocal source route.
- [[adyen-account-structure]] — distinct Company and Merchant account scopes.

## Raw Sources

- [[raw/adyen/docs/reporting/closing-your-fiscal-period/account-receivable-position-dashboard/2026-09-15|Accounts receivable balance positions, captured 2026-09-15]]
