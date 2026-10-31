# api-explorer-dispute-webhooks-latest-post-balanceplatform-dispute-created fixed query answers

Pinned raw: `raw/adyen/api-explorer/dispute-webhooks/latest/post/balancePlatform.dispute.created/2026-09-15.md` (SHA-256 `d7b9bfa91361b049a463a7e97ce2b60c00550f432f3a411eb4627d801fbec0e0`). Canonical source route: `wiki/sources/adyen/source-adyen-api-explorer-dispute-webhooks-latest-post-balanceplatform-dispute-created.md`. Canonical URL: https://docs.adyen.com/api-explorer/dispute-webhooks/latest/post/balancePlatform.dispute.created

## Q1

The captured incoming `balancePlatform.dispute.created` Dispute webhook is sent when a dispute is created and, in the page's words, only informs the server of requests (raw lines 5–7). The body requires `data` and outer `type`; all listed fields inside `data` are optional, including dispute resource ID/current status/status detail/type, disputed transaction ID, capture ARN, balance-platform ID, trigger date, description and disputed amount (raw lines 11–27). A supplied amount needs currency and minor-unit integer value; the table says omitted `disputedAmount` means the entire transaction amount is disputed, and a supplied amount cannot exceed that transaction amount (raw lines 19–21). No status/type enums, request example, environment field or numbered webhook version appear in this pinned page.

## Q2

The notification establishes dispute creation as an informational event, not dispute outcome or a decision to accept/defend. Its optional status describes the dispute object, while optional transaction ID and capture ARN identify related transaction/capture contexts; none of these fields proves transfer or payment finality, reversal, fund movement or bank receipt (raw lines 7, 15–26). Any HTTP 2xx accepts the webhook; `notificationResponse` is optional (raw lines 29–37). The page gives no event-specific failure/reversal sequence, delivery ordering, retry, deduplication or signature rule (full raw lines 1–37). Keep this balance-platform contract distinct from Standard dispute notifications.
