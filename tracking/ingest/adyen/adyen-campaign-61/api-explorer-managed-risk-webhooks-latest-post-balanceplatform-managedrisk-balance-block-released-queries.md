# Managed Risk blocked-balance release retrieval checks

## Q1 — What happened, and what financial outcome does this event establish?

Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-platforms.md` → `[[source-adyen-api-explorer-managed-risk-webhooks-latest-post-balanceplatform-managedrisk-balance-block-released]]` ([canonical URL](https://docs.adyen.com/api-explorer/managed-risk-webhooks/latest/post/balancePlatform.managedRisk.balance.block.released)). The pinned raw identifies an incoming webhook sent when previously blocked funds are released and made available (lines 5–7). `data.amount` is the released amount in minor units (lines 19–21); optional before/after blocked-balance objects are separate snapshots (lines 28–33). The example's negative balances are illustrative (lines 62–69), not a general sign or payout rule. The event does not establish bank receipt.

## Q2 — Which identifiers, dates and acknowledgement rule are specified?

Route: `[[source-adyen-api-explorer-managed-risk-webhooks-latest-post-balanceplatform-managedrisk-balance-block-released]]` ([canonical URL](https://docs.adyen.com/api-explorer/managed-risk-webhooks/latest/post/balancePlatform.managedRisk.balance.block.released)) → pinned raw lines 9–38, 78–86. Required top-level fields are `data`, `environment` and `type`; within `data`, account-holder and balance-account objects plus `amount` are required, while their ID/reference properties are optional (lines 14–25, 36–38). `creationDate` is event trigger time, `valueDate` is release time and `timestamp` is queue time; each is optional (lines 34–37). Any HTTP `2xx` accepts the webhook (lines 78–86), separate from the fund-release state.
