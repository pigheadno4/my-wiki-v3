---
title: "Adyen Balance webhook: blocked funds released"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balance-webhooks/latest/post/balancePlatform.balanceAccount.balance.block.released"
raw_files:
  - "adyen/api-explorer/balance-webhooks/latest/post/balancePlatform.balanceAccount.balance.block.released/2026-09-15.md"
tags: [adyen, balance-webhooks, balance-accounts, blocked-funds]
---

## Overview

This captured Balance Webhooks API Explorer POST reference describes Adyen's incoming `balancePlatform.balanceAccount.balance.block.released` notification. Adyen says it sends the event when previously blocked funds are released, making them available. It gives collateral-for-payments and risk-mitigation holds as possible reasons for a prior block, not as conditions guaranteed for every release. This is an event contract, not a merchant request to release funds. The `latest` route label gives no numbered webhook version. See [[adyen-webhooks]], [[adyen-platforms]], and [[adyen]].

## Key takeaways

- The body requires `data`, `environment` (`test` or `live`), and `type`. Within `data`, the account-holder object, released `amount`, and balance-account object are marked required. `amount.currency` and `amount.value` are required; value is in minor units. The account-holder and balance-account objects' `id`, `description`, and `reference` fields are individually marked optional.
- `blockedBalanceBefore` and `blockedBalanceAfter` are optional snapshots, each with required currency and minor-unit value if present. The optional batch reference, balance-platform ID, event-trigger `creationDate`, and release `valueDate` supply context. The example shows a EUR 25,000-minor-unit release and blocked balance values moving from -100,000 to -75,000 in a test event. Those numbers illustrate a block release; the schema has no `availableBalance` or booked-balance field and does not quantify a general available-balance change.
- This event concerns release of a block on funds, distinct from a new credit, transfer booking, payout, or bank receipt. The response table says any HTTP `2xx` accepts the webhook, with `notificationResponse` optional. The page does not establish delivery order, retry, deduplication, signature verification, or later financial outcome.

## Detail locators

- Event trigger and example hold reasons: pinned raw lines 5–11.
- Required envelope, released amount, identities, optional blocked-balance snapshots and dates: pinned raw lines 15–42.
- Signed blocked-balance test example: pinned raw lines 44–81.
- Acknowledgment response and example: pinned raw lines 82–101.

## Related

- [[adyen-webhooks]] — event and acknowledgment context.
- [[adyen-platforms]] — balance-platform resource context.
- [[source-adyen-docs-platforms-balance-updates]] — separate pilot Balance webhook settings overview.

## Raw Sources

- [[raw/adyen/api-explorer/balance-webhooks/latest/post/balancePlatform.balanceAccount.balance.block.released/2026-09-15|Blocked funds released webhook reference, captured 2026-09-15]]
