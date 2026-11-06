---
title: "Adyen Balance Control API: merchant balance overview"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/BalanceControl/latest/get/balanceOverview/merchants/(merchantAccountCode)/balances"
raw_files:
  - "adyen/api-explorer/BalanceControl/latest/get/balanceOverview/merchants/(merchantAccountCode)/balances/2026-11-07.md"
tags: [adyen, balance-control, merchant-accounts, balances]
---

## Overview

Captured [[adyen]] Balance Control API v2 `GET /balanceOverview/merchants/{merchantAccountCode}/balances` reference. It describes a merchant-account balance overview for a required merchant account code and required `currency` query parameter. The named balance categories are available funds, pending balance, next payout, reserve, and deposit; they have different meanings and must not be collapsed into a single spendable or bank-received amount.

## Key takeaways

- The response table marks `availableFund`, `pendingBalance`, `nextPayout`, `reserve`, `deposit`, and `merchantAccount` optional. When an amount object is present, its `currency` and integer `value` are required within that object; the value is in minor units.
- Available funds are described as settled and available for use. Pending balance is unsettled; next payout is an amount described for the next bank-account payout, not proof of bank receipt. Reserve covers specified operational expenses and deposit is Adyen-withheld coverage for potential losses and liabilities.
- The documented statuses are 200 success, 401 authentication required, 403 insufficient permissions, and 422 request validation error. The error-body properties are optional; `invalidFields` children are required only when that optional array has items.

> [!warning] Contradiction
> The path and response table describe one merchant account with flat optional balance fields, but the 200 example instead contains `merchantBalancesOverview` with two merchant accounts. The capture does not settle the actual response envelope or whether this example belongs to the company-scoped route. Use the table and example as conflicting evidence, not a guarantee of either shape.

> [!warning] Contradiction
> This endpoint's Servers list gives live `https://balance-control-live.adyen.com/balance-control/api/v2`. The captured [[source-adyen-api-explorer-balancecontrol-latest-overview]] also lists that server but its Going live paragraph gives `https://balance-control-live.adyen.com/api/v2`. These snapshots do not resolve which live base path applies.

## Detail locators

- Balance definitions, test/live servers, required path and query inputs: raw lines 5–38.
- Success amount schema and optional parent versus required child fields: raw lines 40–63.
- 401/403/422 structured error schemas: raw lines 66–120. The 200 example and scope/envelope conflict are at lines 122–167.

## Related

- [[adyen-account-structure]] — merchant versus company account and balance terminology.
- [[source-adyen-api-explorer-balancecontrol-latest-overview]] — v2 endpoint overview and live-path conflict.

## Raw Sources

- [[raw/adyen/api-explorer/BalanceControl/latest/get/balanceOverview/merchants/(merchantAccountCode)/balances/2026-11-07|Merchant balance overview, 2026-11-07]]
