---
title: "Metronome Alerts and Notifications"
type: concept
category: technology
tags: [metronome, alerts, notifications, credits, trials]
---

## Definition

Metronome alerts evaluate a configured billing condition and produce a notification that merchant systems can use as an action signal. Alert-definition semantics are separate from the HTTP delivery, retry, deduplication, and signature-verification mechanics in [[metronome-webhooks]].

## Trial credit-balance example

A customer-scoped Contract credit-balance alert with a `$0` threshold can signal that a capped trial credit has been exhausted or expired. The guide's notification type is `alerts.low_remaining_contract_credit_and_commit_balance_reached`, with example fields including `customer_id`, `alert_id`, `threshold`, `alert_name`, `credit_type_id`, `remaining_balance`, and `triggered_by`.

The merchant owns any email, access restriction, or feature re-enablement that follows the notification. The source does not establish whether the threshold isolates the trial credit or aggregates other contract balances, how `triggered_by` classifies expiration or simultaneous triggers, or whether “real-time” implies a specific latency.

## Notification types and lifecycle

### Shared Plan and Contract endpoint surface

Metronome documents a shared alert endpoint family for Plans and Contracts: `/alerts/create`, `/customer-alerts/get`, `/customer-alerts/list`, `/customer-alerts/reset`, and `/alerts/archive`. The shared overview says entity-targeted input and response parameters can differ, but it does not identify which fields vary or provide HTTP methods, version prefixes, or operation schemas. For plan targeting, it lists `low_credit_balance_reached`, `low_remaining_days_in_plan_reached`, `low_remaining_credit_percentage_reached`, and `usage_threshold_reached` as supported `alert_type` values. Its unversioned `/customer-alerts/reset` route label does not replace the dedicated reference's `POST /v1/customer-alerts/reset` contract.

### Manual threshold reset

`POST /v1/customer-alerts/reset` accepts a Metronome customer UUID and threshold-notification UUID, clears cached evaluation state, and immediately initiates a fresh assessment against current thresholds. The reassessment runs in the background: `200` confirms reset and initiation but returns no body and does not reveal the resulting alert state. A breached threshold may produce a new webhook notification. The page does not define eligible current states, archived-alert behavior, an `EVALUATING` transition, completion signaling, error responses, duplicate suppression, retry safety, idempotency, concurrent-reset ordering, or whether repeated resets re-emit alarms. Its `requestBody` also lacks `required: true` even though both object properties are required.

Metronome separates threshold, system, and offset notifications. Threshold notifications monitor conditions such as spend or available credit; system notifications follow object creation, updates, or configured timestamps; offset notifications follow user-defined schedules relative to lifecycle events.

System and offset notifications are stateless. Threshold notifications are continuously evaluated, use `OK` and `IN_ALARM` as their ongoing states, and list `EVALUATING` before the initial evaluation. Evaluation occurs at least every three minutes, and the guide documents firing within five minutes after triggering usage is ingested. A return from `IN_ALARM` to `OK` may emit an optional `*_resolved` event.

## Offset notifications

### System lifecycle event-type discovery

`POST /v2/notifications/system/list` lists available read-only system lifecycle event-type configurations that can be used when creating offset notifications. A successful response requires a `data` array and may include a nullable string `cursor`; each configuration requires `type` and `policy`, while the policy requires a lifecycle-event `type`. The schema gives `contract.create` and `contract.start` only as examples, and the response example shows `SYSTEM_LIFECYCLE_EVENT` with `contract.create`. An optional `is_enabled` field reports whether webhook publishing for the lifecycle event is enabled. The page does not provide a request body, pagination input, exhaustive event-type catalog, enablement control, or offset-validation semantics.

Offset notifications apply a user-configured hour, day, week, month, or year displacement to a known system-event date. They can be managed in the UI or created with `POST /v2/notifications/create` using an ISO 8601 offset policy. The payload omits the threshold payload's `properties` field, and its `timestamp` records the source event time rather than the calculated offset fire time.

Offset generation is prospective: past fire times are not replayed, moving a fire time into the past does not produce a notification, and archiving the configuration before fire time prevents it. Offsets cannot fire before `.create`, `.edit`, or `.archive` events. For recurring commits, a before-`commit.segment.start` offset longer than the one-period-ahead child-generation horizon fires when the future child commit is created rather than at the earlier requested time.

## Customer-configured controls

Credit and commit threshold notifications can monitor remaining balance, percent remaining, or days remaining. Custom fields can narrow a policy to a subset of commits or credits; the worked UI example selects **Contract credit balance** at `$0`, filters credit entities by `credit_type: free_trial`, and scopes the notification to selected customers. The guide presents product cutoff, renewal, and upsell as downstream use cases, but does not establish automatic access enforcement, entitlement mutation, customer communication, or sales action.

A merchant can create customer-scoped threshold alerts for billing-period spend, low remaining commit balance, and usage-invoice total. The spend-limit examples use `spend_threshold_reached` for both soft and hard limits; their names, thresholds, and merchant actions distinguish them rather than a documented native severity or enforcement field. Store returned alert IDs so webhook signals can be matched to the intended customer and rule. When a limit changes, the guide archives the previous alert before creating a replacement, without defining atomic replacement or gap behavior.

Spend alerts can be scoped with `group_values`, polled with customer-alert get/list endpoints, or consumed through webhooks. A hard-limit alarm, a zero commit balance, or any other threshold remains an action signal: the merchant owns customer communication, sales workflows, service cutoff, and later restoration. The guide does not establish an end-to-end latency guarantee, automatic entitlement mutation, maximum overshoot, payment outcome, or access-denial guarantee.

`spend_threshold_reached` evaluates usage-based spend before credit and commit drawdown. `invoice_total_reached` evaluates after drawdown and can be filtered to usage invoices. `low_remaining_commit_balance_reached` signals a configured commit-balance threshold, but the page does not define exactly which balances aggregate into it.

The prepaid-credit model uses `alerts.low_remaining_contract_credit_and_commit_balance_reached` at a zero threshold as a merchant action signal. The merchant stores the entitlement flag in its own database, checks it before each protected action, and changes it from payment and balance signals; the alert does not itself suspend product access. Because the same guide calls the webhook real-time without a latency, ordering, or consistency contract, the dedicated webhook delivery semantics remain authoritative.

For a parent contract's shared commit, child consumption does not automatically trigger the parent's commit-balance alert. The hierarchy guide says alerts evaluate when the parent receives usage and child-only usage may delay the parent alert until parent usage arrives. It gives no evaluation-latency or eventual-evaluation guarantee; webhook delivery mechanics remain a separate concern. Its next spend-alert bullet is truncated after `parent spend alerts only include parent's`, so no spend scope should be inferred from that sentence.

## Sources

- [[source-metronome-guides-pricing-packaging-billing-model-guides-prepaid-credits]] — zero-balance entitlement signal and merchant-owned access-control boundary in a prepaid-credit flow
- [[source-metronome-guides-pricing-packaging-billing-model-guides-model-hierarchical-customer-relationships]] — parent commit-alert evaluation limitation and truncated parent-spend-alert statement

- [[source-metronome-plans-shared-endpoints-notifications]] - shared Plan and Contract alert routes, entity-specific parameter boundary, and plan-targeted alert types

- [[source-metronome-api-reference-notifications-list-system-notification-event-types]] - read-only system lifecycle event-type discovery, response schema, and offset-notification applicability

- [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-alerts]] — remaining-balance, percent-remaining, and days-remaining thresholds with custom-field scoping and enforcement boundaries
- [[source-metronome-api-reference-alerts-reset-a-threshold-notification]] — customer-scoped threshold reset, cached-state clearing, asynchronous reassessment, empty `200` response, and retry unknowns

- [[source-metronome-guides-pricing-packaging-billing-model-guides-create-a-trial]] — customer-scoped trial alert, threshold, payload fields, and merchant-action boundary
- [[source-metronome-guides-customers-billing-set-up-notifications-create-and-manage-notifications]] — notification families, evaluation timing, state transitions, and operating guidance
- [[source-metronome-guides-customers-billing-set-up-notifications-offset-notifications]] — relative scheduling, payload timestamp semantics, prospective firing rules, and recurring-commit caveat
- [[source-metronome-guides-customers-billing-optimize-customer-experience-customer-controls]] — customer-configured spend, grouped-dimension, commit-balance, and invoice-total alert patterns with merchant-action boundaries

## Related

- [[metronome-webhooks]]
- [[metronome-credits-and-commits]]
- [[metronome-customers-and-contracts]]
- [[metronome-usage-based-billing]]
