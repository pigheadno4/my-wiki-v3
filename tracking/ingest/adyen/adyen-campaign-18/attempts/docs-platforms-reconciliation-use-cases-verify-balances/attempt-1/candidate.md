---
title: "Adyen Platforms balance verification with reports"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/reconciliation-use-cases/verify-balances"
raw_files:
  - "adyen/docs/platforms/reconciliation-use-cases/verify-balances/2026-09-15.md"
tags: [adyen, platforms, reconciliation, balances, reporting]
---

## Overview

This 2026-09-15 Adyen for Platforms reconciliation guide explains two report-based ways to spot-check balance-account positions: the Balance Platform Balance Report for a given day's opening and closing balances, and the Balance Platform Accounting Report for a filtered balance-account calculation using Balance (PC) entries. It also describes negative-balance compensation from the platform liable account and an advance warning webhook. These are historical reporting and process routes, not proof of a live available balance, a completed user payout or beneficiary bank receipt. See [[adyen]], [[adyen-reporting]] and [[adyen-platforms]].

## Key takeaways

- **Daily position grain:** Get the Balance Platform Balance Report for a specific date, then filter it. The guide says it shows opening and closing positions for account holders, balance accounts (including liable), and currencies on that day. Its example has separate USD and CAD rows for one balance account. Keep date, account and currency together; a daily snapshot is not a transaction-event ledger or necessarily the balance available at a later payout request.
- **Accounting grain and signs:** To calculate from the Balance Platform Accounting Report, filter to the balance account and sum Balance (PC), considering value-date accounting. In the worked payment-split example, received and authorised rows have zero Balance (PC) before availability; the captured row carries the amount on its later value date. The same PSP payment reference also has distinct user, liable and fee balance-account split rows; do not add them together as though they were one account balance. Signed Received (PC), Reserved (PC), and Balance (PC) values move between buckets in the example, including a negative fee-account amount. The 2022/2023 sample rows are illustrations, not account-specific proof.
- **Negative-balance path:** The guide says refunds or chargebacks can cause a negative balance, while payout or transfer is limited to available funds. It describes Adyen allowing negative balances up to 30 days and, at month end if an account has been negative for more than 30 days, compensation by debiting the platform liable balance account. The compensation is an internal transfer; the Accounting Report entry is identified by a Negative Balance compensation description/reference and transfer webhooks carry internal/internalTransfer. This is not a bank payout.
- **Advance notice and alternatives:** The page describes an optional warning webhook after an account has been negative for over 20 days by default, with a scheduled internal compensation date and support route to change that threshold. The TEST webhook payload is illustrative and conditional: it says compensation occurs if the negative amount remains uncompensated by the scheduled time. The guide offers account-holder on-demand top-up or scheduled top-up from a registered bank account as ways to avoid the liable-account transfer; those are separate operations, not automatic outcomes of viewing a warning.

## Detail locators

- Purpose and two report routes: pinned raw lines 15-26.
- Balance Report date/account/currency example: pinned raw lines 28-43.
- Accounting Report filter/sum, value-date explanation and split/sign example: pinned raw lines 45-69.
- Negative-balance compensation, report/webhook grain and available-only boundary: pinned raw lines 71-82.
- Optional warning, TEST payload, default threshold and top-up routes: pinned raw lines 84-129.

## Related

- [[adyen-reporting]] — main reporting/reconciliation concept and reciprocal source route.
- [[adyen-platforms]] — parent platform context.

## Related raw API references

- [[raw/adyen/docs/platforms/reports-and-fees/balance-report/2026-09-15|Balance Platform Balance Report]] — detailed report fields; navigation only.
- [[raw/adyen/docs/platforms/reports-and-fees/balance-platform-accounting-report/2026-09-15|Balance Platform Accounting Report]] — detailed report fields; navigation only.

## Raw Sources

- [[raw/adyen/docs/platforms/reconciliation-use-cases/verify-balances/2026-09-15|Adyen Verify balances, captured 2026-09-15]]
