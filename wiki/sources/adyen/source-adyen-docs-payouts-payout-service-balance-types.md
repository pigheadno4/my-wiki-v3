---
title: "Payout Service path: balance-account balance types"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/balance-types"
raw_files:
  - "adyen/docs/payouts/payout-service/balance-types/2026-09-15.md"
tags: [adyen, payout-service, platforms, balance-accounts, balances]
---

## Overview

This 2026-09-15 [[adyen]] page sits under the **Payout Service** path but describes five **balance-platform balance-account** types for each held currency: Balance/current, Available, Pending, Pending available and Reserved. It gives viewing routes and worked timelines. These are account-balance categories, not evidence that a particular payment settled, payout completed or beneficiary bank received funds. [[adyen-platforms]]

## Key takeaways

- `Balance` or current balance is the sum of already-settled transactions. `Pending` is future-settling transactions and may be positive or negative. `Reserved` includes authorized outgoing transfers not yet booked and blocked funds such as Capital repayments or current-balance payout collateral. `Available` is described as funds available for transfers; `Pending available` anticipates availability after pending settlement. A balance account may carry these separately for several currencies. See raw lines 19–30.
- **Formula/example conflict:** the printed Available formula is the lower of current balance and current minus pending and reserved. Example 1 shows current EUR 100, pending EUR 20, reserved EUR 30 and Available EUR 70, whereas that literal formula yields EUR 50. Example 2 shows current EUR 50, pending EUR -70, reserved EUR 0 and Available EUR -20, whereas the literal formula yields EUR 50. The printed Pending available formula is the lower of pending and pending plus available; Example 2 gives pending EUR -70, available EUR -20 and Pending available EUR -70, whereas that literal formula yields EUR -90. Do not implement either formula from this snapshot alone. See raw lines 24–28, 58–64 and 78–86.
- The examples illustrate an incoming settlement and refund reservation reducing transferable funds, a future refund making Available negative despite positive current balance, and Pending EUR 50 versus Pending available EUR 20 when current balance is EUR -30. These are examples, not live ledger or authorization outcomes. See raw lines 48–104.
- To inspect all currencies, the page points to `GET /balanceAccounts/{id}`, a `balancePlatform.balanceAccount.balance.updated` event or Customer Area balances. It says notifications may guide later top-up or internal-transfer decisions to avoid negative balances; a notification does not itself move money. See raw lines 32–40 and 106–112.

## Detail locators

- **Per-currency definitions, formulas and reserve components:** raw lines 19–30.
- **Notification and balance-viewing routes:** raw lines 32–40.
- **Example 1 incoming-settlement/refund reserve timeline:** raw lines 48–68.
- **Example 2 negative Available and formula conflicts:** raw lines 72–86.
- **Example 3 Pending versus Pending available:** raw lines 90–104.

## Related

- [[adyen-platforms]]
- [[adyen-payouts]] — Payout Service documentation path, distinct from legacy Payout API
- [[source-adyen-docs-platforms-balance-types|Parallel Platforms-path balance definitions]]
- [[source-adyen-docs-payouts-payout-service-balance-updates-configure-balance-webhook|Balance notification setup]]

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/balance-types/2026-09-15|Adyen Payout Service path balance types — collected 2026-09-15]]
