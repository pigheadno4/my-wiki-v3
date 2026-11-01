# C61 fixed-query answers — api-explorer-managed-risk-webhooks-latest-post-balanceplatform-managedrisk-settlementdelay-lifted

Pinned raw: `raw/adyen/api-explorer/managed-risk-webhooks/latest/post/balancePlatform.managedRisk.settlementDelay.lifted/2026-09-15.md`. Canonical retrieval route: [[source-adyen-api-explorer-managed-risk-webhooks-latest-post-balanceplatform-managedrisk-settlementdelay-lifted]]; URL: https://docs.adyen.com/api-explorer/managed-risk-webhooks/latest/post/balancePlatform.managedRisk.settlementDelay.lifted

## Q1

Adyen sends this incoming Managed Risk webhook when it lifts a settlement delay from an account holder's payouts after the risk review period (raw lines 5–7). Required top-level fields are `data`, `environment` (`test` or `live`), and webhook `type`; required nested fields are the affected `accountHolderId` and `reason` (14–21). The reason enum includes `paymentProcessingEnabled`, `settlementDelayChanged`, and `riskReviewPeriodPassed` (18). Optional `data.balancePlatform` identifies the platform; optional `data.creationDate` is event-trigger time, while optional `timestamp` is queue time (16–20). The sample's `data.id` is absent from the field table and cannot be treated as a required identifier (28–36). No amount, account balance, payout transaction, deletion or reversal contract appears in this raw.

## Q2

The response lists HTTP 200 success and permits any `2xx` status to accept the webhook, with optional `notificationResponse` (raw lines 39–47). This is receiver acceptance, not evidence that funds were paid out or received by a bank. The event reports a Managed Risk payout-delay change for an account holder, distinct from the separate balance-account settlement-delay configuration flow; this page gives no delivery order, retry, deduplication, signature, final payout or financial-booking rule (full raw lines 1–47). Retrieval route: [[source-adyen-api-explorer-managed-risk-webhooks-latest-post-balanceplatform-managedrisk-settlementdelay-lifted]]; https://docs.adyen.com/api-explorer/managed-risk-webhooks/latest/post/balancePlatform.managedRisk.settlementDelay.lifted
