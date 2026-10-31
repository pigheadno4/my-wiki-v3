# C59 Balance webhook v1 overview fixed-query answers

## Q1

The 2026-09-15 captured API Explorer overview explicitly labels the family **Balance webhook v1** and says Adyen sends it to inform recipients of balance changes in their balance platform (raw lines 5–7). It gives no event payload schema or field requirements. It says Configuration API conditions can target the whole balance platform, balance accounts of specified account holders, or a specific balance account (lines 9–15). The listed incoming POST routes are `balancePlatform.balanceAccount.balance.block.released` and `balancePlatform.balanceAccount.balance.updated`, summarized as blocked funds released and balance updated (lines 17–23). The `latest` route does not independently establish a newer/current version. Canonical route: [[source-adyen-api-explorer-balance-webhooks-latest-overview]]; https://docs.adyen.com/api-explorer/balance-webhooks/latest/overview.

## Q2

This overview establishes only a notification family, condition scopes and two event routes. It does not supply payload requirements, balance amounts or currency, trigger precision beyond the listed summaries, delivery/retry/order/deduplication or signature rules, or evidence of a transfer, payout, settlement or bank receipt (raw lines 5–23). The linked Configuration API settings page and event-specific POST pages are separate contracts. The explicit v1 title is the captured family version; `latest` is the documentation route label, not current-version proof. Canonical route: [[source-adyen-api-explorer-balance-webhooks-latest-overview]]; https://docs.adyen.com/api-explorer/balance-webhooks/latest/overview.
