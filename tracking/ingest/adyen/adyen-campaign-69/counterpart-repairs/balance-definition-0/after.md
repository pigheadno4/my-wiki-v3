---
title: "Adyen Balance Control API v2: company merchant balances overview"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/BalanceControl/latest/get/balanceOverview/companies/(companyAccountCode)/balances"
raw_files:
  - "adyen/api-explorer/BalanceControl/latest/get/balanceOverview/companies/(companyAccountCode)/balances/2026-11-07.md"
tags: [adyen, balance-control, company-account, merchant-account, balances]
---

## Overview

This November 2026 Balance Control API v2 GET reference returns a balance overview for merchant accounts under the company account identified in the path, for a required currency query. Its purpose text describes available funds as settled and available for use, and separately describes unsettled pending balance, next payout amount, reserve, and deposit. A separate account-balances guide uses a broader available-funds definition; see the warning below. It is an account-balance lookup, not a transfer, payout execution, or bank-receipt record. [[adyen]] [[adyen-account-structure]]

## Key takeaways

- `companyAccountCode` is a required company-account path identifier and `currency` is a required query string. The reference lists TEST and Live `/balance-control/api/v2` servers. It does not give this operation a specific caller role, default currency, pagination, idempotency, or refresh/timing guarantee. The separate family overview recommends `X-API-Key` authentication and a distinct Live key; that is overview guidance, not an operation-specific role statement. [[source-adyen-api-explorer-balancecontrol-latest-overview]]
- The purpose text defines available funds as settled and available for use, pending balance as not yet settled, next payout as an amount to be settled to the bank account with the next payout, reserve as available for specified operational expenses, and deposit as withheld for potential processing liabilities. The operation presents these as distinct response categories; `nextPayout` is prospective, not evidence of bank credit. Do not equate this operation's `availableFund` description with the account-balances guide's aggregate available-funds formula.
- `200` means the request succeeded. Its body schema makes `merchantBalancesOverview` optional; merchant rows and all five balance objects and `merchantAccount` are optional within the row. Where an amount object exists, `currency` is a three-character ISO code and `value` is an integer in minor units, both required inside that object. The example shows two merchant accounts, different currencies, a negative pending value, and omitted categories; it does not define all actual responses or settle how a particular `currency` filter affects returned rows.
- The reference lists `401` authentication required, `403` insufficient permissions, and `422` validation error, with optional error-envelope fields. This readback does not establish current Live access, completed settlement, successful payout, or bank receipt.

> [!warning] Contradiction
> This operation describes available funds as settled and available for use, separately from pending balance, which is not yet settled. The 2026-09-15-captured [[source-adyen-docs-account-balances]] guide instead says total available funds can include unsettled Pending, Next payout, Reserve, and conditionally eligible Negative refund allowance. The captures do not explain whether or how the API `availableFund` field maps to that broader formula; do not treat them as interchangeable. [[raw/adyen/api-explorer/BalanceControl/latest/get/balanceOverview/companies/(companyAccountCode)/balances/2026-11-07#L7|operation raw lines 7–17]] [[raw/adyen/docs/account/balances/2026-09-15#L37|guide raw lines 37–49]]

> [!warning] Contradiction
> This operation's Servers section lists the Live base as `https://balance-control-live.adyen.com/balance-control/api/v2`, while the separately captured Balance Control v2 overview's Going live prose gives `https://balance-control-live.adyen.com/api/v2` and its own Servers section uses the longer base. The snapshots do not resolve the applicable Live route. [[source-adyen-api-explorer-balancecontrol-latest-overview]]

## Detail locators

- Company scope, five balance definitions, TEST/Live servers and required path/query fields: [[raw/adyen/api-explorer/BalanceControl/latest/get/balanceOverview/companies/(companyAccountCode)/balances/2026-11-07#L5|raw lines 5–38]].
- Optional `200` row/amount schema and `401`/`403`/`422` error envelopes: [[raw/adyen/api-explorer/BalanceControl/latest/get/balanceOverview/companies/(companyAccountCode)/balances/2026-11-07#L40|raw lines 40–121]].
- Illustrative two-merchant response: [[raw/adyen/api-explorer/BalanceControl/latest/get/balanceOverview/companies/(companyAccountCode)/balances/2026-11-07#L123|raw lines 123–168]].
- Related overview's API-key guidance and divergent Live base: [[raw/adyen/api-explorer/BalanceControl/latest/overview/2026-09-15#L9|overview raw lines 9–38]].

## Related

- [[adyen-account-structure]] — company and merchant account hierarchy.
- [[adyen-reporting]] — financial evidence and reconciliation boundaries.
- [[source-adyen-api-explorer-balancecontrol-latest-overview]] — Balance Control API v2 family overview and Live-base conflict.
- [[adyen]] — provider index.

## Raw Sources

- [[raw/adyen/api-explorer/BalanceControl/latest/get/balanceOverview/companies/(companyAccountCode)/balances/2026-11-07|Captured Balance Control API v2 company balances GET reference]]
