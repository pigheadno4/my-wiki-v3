---
title: "Marketplace balance webhook example use cases"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/balance-updates/use-cases"
raw_files:
  - "adyen/docs/marketplaces/balance-updates/use-cases/2026-09-15.md"
tags: [adyen, marketplaces, balance-accounts, webhooks, examples]
---

## Overview

This 2026-09-15 [[adyen]] Marketplace page gives Configuration API **TEST examples** of Balance webhook settings and matching balance-update events for three threshold-alert scopes. Balance webhooks are marked **limited availability / pilot**; the page says processes and documentation may change. These are example configurations and event shapes, not proof of a live balance, completed transfer or bank receipt. [[adyen-platforms]]

## Key takeaways

- To alert when any balance account's **current balance** is below USD 5,000, the first example targets a `balancePlatform`, uses `conditions.balanceType: balance` and `lessThan`, and sets `value: 500000`. To alert when any account of a particular user reaches or falls below USD 5,000, the second targets that `accountHolder` and uses `lessThanOrEqual`. The target scopes are distinct. See raw lines 26–45 and 97–116.
- For **available balance** below a threshold on six users' foreign-currency accounts, the page instructs a separate setting for **each** `balanceAccount`, with its account ID and currency. Its JPY prose says below JPY 1,000, but the example sets `value: 100000` and shows `available: 95000`. This page does not explain that scale; the separate Adyen currency guide says JPY has zero decimal minor units. Do not copy the JPY number as a validated JPY 1,000 threshold without checking the current Balance webhook API contract. See raw lines 169–188, 197–213, 219–234; [[source-adyen-docs-development-resources-currency-codes]] raw lines 164–172.
- All three illustrated events use `balancePlatform.balanceAccount.balance.updated`, `environment: test`, a setting ID, currency, and `balances` containing available, pending, reserved and balance values. The account-holder and individually targeted account examples show `accountHolderId`, but the displayed event data do **not** show a `balanceAccountId`, even for the account-targeted example. Do not infer a particular account solely from these sample payloads. See raw lines 72–95, 143–167 and 215–239.
- Each example supplies one condition, so these examples do not resolve multi-condition matching behavior or establish that a configured alert will always fire. The related configuration guide owns subscription, role, limit and update rules. See raw lines 32–74, 103–145 and 175–217; [[source-adyen-docs-platforms-balance-updates-configure-balance-webhook]].

## Detail locators

- **Pilot caveat and page purpose:** raw lines 15–24.
- **Platform-wide current-balance threshold and TEST event:** raw lines 26–95.
- **Account-holder current-balance threshold and TEST event:** raw lines 97–167.
- **Per-account available-balance settings, JPY mismatch and TEST event:** raw lines 169–239.

## Related

- [[adyen-platforms]]
- [[source-adyen-docs-platforms-balance-updates-use-cases|Parallel Platforms-path use-case examples]]
- [[source-adyen-docs-platforms-balance-updates-configure-balance-webhook|Balance webhook setup and condition rules]]
- [[source-adyen-docs-development-resources-currency-codes|Adyen currency minor-unit reference]]

## Raw Sources

- [[raw/adyen/docs/marketplaces/balance-updates/use-cases/2026-09-15|Adyen Marketplace balance webhook use cases — collected 2026-09-15]]
