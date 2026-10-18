---
title: "Adyen Platforms CashOut overview"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/cash-out-instantly"
raw_files:
  - "adyen/docs/platforms/cash-out-instantly/2026-09-15.md"
tags: [adyen, platforms, cashout, pending-balance, instant-payouts]
---

## Overview

This Adyen for Platforms CashOut overview (last modified 2020-09-11; captured 2026-09-15) describes a user-requested cashout of funds in a user's pending available balance before normal settlement makes them available. A cashout request can fund the user's balance account; an instant payout to the user's transfer instrument is a separate conditional leg when that instrument is specified. Later settlement triggers repayment of the cashout amount from the user's balance account. See [[adyen]], [[adyen-platforms]] and the separate request guide linked in the raw.

## Key takeaways

- **Amount and legs:** The requested cashout amount must not exceed the user's pending available balance; if an optional fee is charged, amount plus fee must fit that balance. The page describes Cashout Funding credit to the user's balance account, Cashout Instant Payout only if a transfer instrument is specified, Cashout Fee debit from the user balance account to the platform liable balance account if charged, and Cashout Repayment debit when the captured payments settle. Its dated seller example illustrates this sequence; it does not show a specific completed operation. The example says January 1 sales with a two-day settlement delay become available January 3, yet labels the repayment settlement date January 1. Treat that date as an internal inconsistency and do not infer an exact repayment date from the example.
- **Availability and return:** The captured support table lists Australia/AUD, EEA/EUR, US/USD and UK/GBP. Cashout availability also depends on the receiving bank's ability to support instant payouts. If it cannot, the funds are returned and the cashout amount is added back to the source balance account's pending available balance. The Australia footnote warns of possible ANZ rail rate-limiting delays. Listed regions are snapshot support, not a live eligibility check or guaranteed bank arrival.
- **Limits and timing:** The documented minimum is 0.01. A rolling 24-hour maximum per balance account is configured at balance-platform level with Adyen approval. The page lists no daily count limit but imposes a same-balance-account cooldown: a successful request must finish processing before another can be initiated, usually about one minute and up to ten minutes. Pass-through-settlement payment-method proceeds, such as the example Affirm, are excluded from pending available and cannot be cashed out.
- **Evidence and reporting:** The daily Statement report follows balance movements. The Payout report is generated on days with scheduled payouts; after a full cashout there may be no scheduled payout and hence no Payout report for that account that day. Transfer webhooks are the guide's real-time tracking route. TEST-only bank details and the described insufficient-funds/missing-capability failure scenarios are testing instructions, not live result proof. A cashout request, funding entry or report row does not by itself establish bank receipt.

## Detail locators

- Pending-available context, cashout purpose, amount/fee limits and four transfer legs: pinned raw lines 15-46.
- Support table, receiving-bank return condition and Australia warning: pinned raw lines 48-59.
- Minimum, approved rolling maximum, cooldown and pass-through exclusions: pinned raw lines 61-69.
- Statement/Payout report behavior and transfer webhook route: pinned raw lines 71-87.
- TEST-only setup, failure scenarios and child request/webhook navigation: pinned raw lines 89-108.

## Related

- [[adyen-platforms]] — main Platforms concept and reciprocal source route.
- [[source-adyen-docs-platforms-custom-payouts]] — related external payout route.

## Related raw API references

- [[raw/adyen/docs/platforms/cash-out-instantly/cashout-request/2026-09-15|Cashout request]] — child operation guide; navigation only.
- [[raw/adyen/docs/platforms/cash-out-instantly/cashout-webhooks/2026-09-15|Cashout webhooks]] — child event guide; navigation only.

## Raw Sources

- [[raw/adyen/docs/platforms/cash-out-instantly/2026-09-15|Adyen Cash out pending funds instantly, captured 2026-09-15]]
