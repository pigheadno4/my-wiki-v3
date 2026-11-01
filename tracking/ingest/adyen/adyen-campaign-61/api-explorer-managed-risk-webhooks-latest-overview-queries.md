# C61 fixed retrieval answers: Managed risk webhooks v1 overview

Pinned raw: `raw/adyen/api-explorer/managed-risk-webhooks/latest/overview/2026-09-15.md`. Canonical source: [[source-adyen-api-explorer-managed-risk-webhooks-latest-overview]]; https://docs.adyen.com/api-explorer/managed-risk-webhooks/latest/overview.

## Q1

The captured page is an **incoming Adyen webhook catalog**, headed **Managed risk webhooks v1**. Adyen sends these events to customers using Adyen Managed Risk when it adjusts risk measures applied to account holders' payouts based on risk level. It names settlement delays, rolling reserves, and reserve waivers (raw lines 5–11). The eight listed POST routes are `balancePlatform.managedRisk.balance.block.released`, `balancePlatform.managedRisk.reserveWaiver.applied`, `balancePlatform.managedRisk.reserveWaiver.removed`, `balancePlatform.managedRisk.rollingReserve.applied`, `balancePlatform.managedRisk.rollingReserve.lifted`, `balancePlatform.managedRisk.rollingReserve.updated`, `balancePlatform.managedRisk.settlementDelay.lifted`, and `balancePlatform.managedRisk.settlementDelay.updated` (raw lines 13–25). This overview gives no resource IDs, payload or response fields, limits, or event-specific lifecycle/timing conditions; those belong to child references. [[source-adyen-api-explorer-managed-risk-webhooks-latest-overview]]

## Q2

The overview establishes only the family purpose and eight event routes. It does **not** document receiver acknowledgement, event payload, request acceptance, delivery order, retry, deduplication, signature, or the result of an individual risk-policy change. In particular, a listed release, reserve-waiver, rolling-reserve, or settlement-delay event is not evidence here of a completed payout, balance-account credit, or bank receipt (raw lines 5–25). No deprecation or migration notice appears in this overview. The `latest` URL and v1 heading identify this captured snapshot, not current customer eligibility. Follow the specific POST event reference for its fields and response contract. [[source-adyen-api-explorer-managed-risk-webhooks-latest-overview]]
