---
title: "Adyen Classic Platforms transactional ledger"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/reconciliation-use-cases/build-transactional-ledger"
raw_files:
  - "adyen/docs/classic-platforms/reconciliation-use-cases/build-transactional-ledger/2026-09-15.md"
tags: [adyen, classic-platforms, reconciliation, ledger, reports, negative-balances]
---

## Overview

This 2023-modified Classic Adyen for Platforms guide, captured 2026-09-15, explains building a transaction ledger by account holder and account from the Marketplace Payments accounting report. It covers credits, debits, fee and payout rows, then compares calculated balances with the MarketPay balance report. New implementations are directed to a separate integration guide. [[adyen]] [[adyen-classic-platforms]]

## Key takeaways

- The Marketplace Payments accounting report shows financial activity within the Classic platform: payment/transfer credits and refund, chargeback, transfer, fee and payout debits. Filter or group by **Account holder** and **Account** to reconstruct each account's transaction history; the page's selected rows are an illustration rather than a complete report (raw lines 19–27, 39–66).
- Split instructions at payment or capture produce account-specific report rows: a two-account payment yields two credit rows, and a split refund yields separate debit rows. If split instructions are absent, Adyen credits/debits the platform liable account instead; a partial refund without split instructions debits the liable account and aggregate entries use `TransferBalance`. All transaction fees are deducted from the liable account and total fees appear as `Fee` (raw lines 29–37). The account receiving a sale or refund effect follows these Classic split instructions, not an inferred modern balance-account model.
- Calculate an account balance by tracking all its credits, debits and payouts in the Marketplace Payments accounting report, or inspect available balances in the separate MarketPay balance report, including the liable account (raw lines 68–72). The worked rows produce EUR 78.28 liable, EUR 0 for AccountHolder_1 and EUR 72 for AccountHolder_2, but are selected illustrative rows, not proof of a live reconciliation (raw lines 45–64, 82–94). A `Payout` report row is not itself evidence of recipient-bank credit.
- Refunds or chargebacks can make a Classic account negative; payout or balance transfer cannot, because only available balance can be paid/transferred. Adyen permits negative balances for up to 30 days and, at month end if an account has remained negative for **more than 30 days**, compensates by debiting the platform liable account. That compensation appears as a `FundTransfer` row; the page also points to account-holder top-ups as an alternative to have holders cover their negative balances (raw lines 74–80).

## Detail locators

- Classic scope, Marketplace Payments report purpose and activity types: raw lines 19–27. Split-credit/debit grain, liable fallback and Fee: raw lines 29–37. Selected ledger columns/rows and grouped summary: raw lines 39–66.
- Balance calculation versus MarketPay balance report: raw lines 68–72. Negative-balance cause, 30-day/month-end liable compensation, `FundTransfer` and available-balance restriction: raw lines 74–80. Selected balance-report example: raw lines 82–94.

## Related

- [[adyen-classic-platforms]] — older account-holder/account money-flow model.
- [[source-adyen-docs-classic-platforms-reconciliation-use-cases]] — Classic reconciliation hub.
- [[source-adyen-docs-classic-platforms-processing-payments]] — Classic split instruction and refund behavior.
- [[adyen-platforms]] — separate newer balance-platform model.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/reconciliation-use-cases/build-transactional-ledger/2026-09-15|Classic transactional ledger, captured 2026-09-15]]
