---
title: "Adyen Marketplace verify balances"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/reconciliation-use-cases/verify-balances"
raw_files:
  - "adyen/docs/marketplaces/reconciliation-use-cases/verify-balances/2026-09-15.md"
tags: [adyen, marketplaces, platforms, reporting, balances, reconciliation]
---

## Overview

This 2026-09-15 Marketplace worked guide gives two ways to spot-check **balance positions** for user and liable balance accounts: read opening/closing positions from the daily Balance Platform Balance Report at the account–currency grain, or calculate changes by summing **Balance (PC)** entries from the Balance Platform Accounting Report for the selected balance account. It also describes negative-balance compensation and warning events. A historical report position does not establish current cash available for a new payout or a completed external transfer. [[adyen]] [[adyen-reporting]]

## Key takeaways

- The Balance Report shows a chosen day's **opening and closing balance** by account holder, balance account and currency, including the liable account. Get the specific-date report and filter to the account/currency of interest; the worked 2022-06-08 example has one account with separate USD and CAD rows and another with USD (raw lines 21–43).
- The Accounting Report route filters the desired balance account and sums **Balance (PC)** mutations. Its worked payment shows `received` and `authorised` on the 2023-01-18 **booking date** with zero Balance (PC); on 2023-01-20 **value date**, the captured split becomes available. The same PSP reference has separate user, liable-commission and fee-account rows, so do not sum every account into one user's position (raw lines 45–69).
- A negative user balance can follow refunds or chargebacks. The guide says Adyen permits it for up to 30 days and, **at month-end if it has been negative for more than 30 days**, compensates by internally transferring from the platform liable balance account. The Accounting Report entry can show `Negative Balance compensation for {AccountHolderId}`; Transfer `created`/`updated` webhooks use `category: internal` and `type: internalTransfer`. This is a liable-to-user balance-account movement, not an external bank payout (raw lines 71–82).
- The page says payouts and balance transfers can use only available balance and cannot themselves create a negative balance. It offers user bank-account top-up routes as ways to avoid liable-account compensation; a requested top-up or sweep setup is not evidence that funds arrived before compensation (raw lines 82, 124–129).
- An optional **negativeBalanceCompensationWarning.scheduled** webhook can notify after a negative balance exceeds a configured threshold, default **20 days**; Support can change that threshold. The TEST example identifies negative balance account, account holder, liable source account, signed amount, `negativeBalanceSince`, and `scheduledCompensationAt`, with compensation conditional on the deficit not being resolved by then (raw lines 84–122).
- **Example timing conflict:** the warning sample says the deficit began 2024-10-19, its webhook `creationDate` is 2024-10-22 (three days later), and scheduled compensation is 2024-12-01 (about 43 days later). Those timestamps do not demonstrate the text's “over 20 days” warning threshold or a specific 30-day/month-end execution schedule. Treat them as illustrative data, not a timer guarantee (raw lines 73, 86–115).

## Detail locators

- Daily Balance Report account/currency snapshots: raw lines 19–43. Accounting Report filter, Balance (PC) sum and value-dated split example: lines 45–69.
- Negative-balance causes, month-end compensation, report/webhook identifiers and available-balance limit: lines 71–82. Optional warning, sample timestamps and top-up alternatives: lines 84–129.

## Related

- [[adyen]] — provider.
- [[adyen-reporting]] — report and reconciliation concept.
- [[adyen-platforms]] — modern marketplace/platform context.
- [[source-adyen-docs-platforms-reconciliation-use-cases-verify-balances]] — separate Platforms-path guide.
- [[source-adyen-docs-platforms-reports-and-fees-balance-report]] — daily balance snapshot reference.
- [[source-adyen-docs-platforms-reports-and-fees-balance-platform-accounting-report]] — accounting mutation reference.
- [[source-adyen-docs-platforms-top-up-balance-account-on-demand-top-ups]] — separate top-up process.

## Raw Sources

- [[raw/adyen/docs/marketplaces/reconciliation-use-cases/verify-balances/2026-09-15|Marketplace verify balances — 2026-09-15 snapshot]]
