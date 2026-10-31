---
title: "Adyen Balance webhook: balance-account balance updated"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balance-webhooks/latest/post/balancePlatform.balanceAccount.balance.updated"
raw_files:
  - "adyen/api-explorer/balance-webhooks/latest/post/balancePlatform.balanceAccount.balance.updated/2026-09-15.md"
tags: [adyen, balance-platform, webhooks, balances]
---

## Overview

Captured API Explorer `latest` POST reference for the incoming `balancePlatform.balanceAccount.balance.updated` Balance webhook. Adyen says it sends this event when the specified balance type reaches or drops below a configured threshold. It reports balance values for a balance account and currency; the alert alone is not evidence of a particular transfer, booked transaction, payout, or bank receipt. See [[adyen]], [[adyen-platforms]], and [[adyen-webhooks]].

## Key takeaways

- The body table requires `data`, `data.balanceAccountId`, `data.balances`, `data.currency`, `data.settingIds`, `environment`, and `type`. `settingIds` identifies balance-webhook settings; the example shows two IDs, without establishing a required count.
- Within the required `balances` object, each listed integer is **optional**: `available` is available for use, `balance` is the sum of transactions already settled, `pending` is the sum of transactions to be settled in the future, and `reserved` is held in reserve. These distinct descriptions do not supply a formula or show which balance type crossed which threshold in a given payload.
- `currency` is a three-character ISO currency code. `data.balancePlatform`, event `creationDate`, and queued `timestamp` are optional; `environment` is `test` or `live`. The USD amounts in the request example are illustrative values, not thresholds or proof of financial movement.
- The response section says any HTTP `2xx` accepts the webhook; its `200`/`[accepted]` response is a receiver acknowledgement, not a separate balance or transaction outcome. This captured `latest` page does not establish a numbered version, current availability, or delivery guarantees.

## Detail locators

- Event type and threshold trigger: raw lines 5–7 and 50–52.
- Required body fields and optional balance types: raw lines 9–27.
- Illustrative account, setting IDs, currency, and balances: raw lines 29–53.
- Receiver acknowledgement: raw lines 54–73.

## Related

- [[adyen]]
- [[adyen-platforms]]
- [[adyen-webhooks]]

## Raw Sources

- [[raw/adyen/api-explorer/balance-webhooks/latest/post/balancePlatform.balanceAccount.balance.updated/2026-09-15|Captured balance-account balance-updated webhook reference]]
