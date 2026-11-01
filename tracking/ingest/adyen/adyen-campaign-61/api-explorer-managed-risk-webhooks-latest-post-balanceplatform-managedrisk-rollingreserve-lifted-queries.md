# C61 fixed query answers — managed-risk rolling reserve lifted

Canonical source: [[source-adyen-api-explorer-managed-risk-webhooks-latest-post-balanceplatform-managedrisk-rollingreserve-lifted]] · https://docs.adyen.com/api-explorer/managed-risk-webhooks/latest/post/balancePlatform.managedRisk.rollingReserve.lifted

## Q1

Adyen sends the incoming `balancePlatform.managedRisk.rollingReserve.lifted` webhook when it lifts a rolling reserve **policy from an account holder's payouts**. The body table requires `data` with `data.accountHolderId` (the account holder whose risk settings changed), plus top-level `environment` (`test` or `live`) and `type`. `data.balancePlatform` and `data.creationDate` are optional; the latter is the event-trigger time in ISO 8601 extended format. Top-level `timestamp` is optional and denotes queueing time. The sample includes `data.id`, but the table does not define it; the example does not make it required. The reference gives no reserve amount, policy duration, lift propagation schedule, deletion rule, failure/reversal flow, or current account eligibility. Pinned raw: `raw/adyen/api-explorer/managed-risk-webhooks/latest/post/balancePlatform.managedRisk.rollingReserve.lifted/2026-09-15.md:5-36`.

## Q2

The `200 Success` response section says any HTTP `2xx` accepts the webhook; `notificationResponse` is optional. That is webhook receipt acknowledgment, not a separate managed-risk decision or evidence of a payout, reserve release amount, balance posting, settlement, or bank receipt. This event describes the policy lift only. The page does not define delivery ordering, retries, deduplication, signatures, or subsequent financial timing. Its `latest` URL and captured example do not prove current availability or a specific account's state. Pinned raw: `raw/adyen/api-explorer/managed-risk-webhooks/latest/post/balancePlatform.managedRisk.rollingReserve.lifted/2026-09-15.md:5-7,22-45`.
