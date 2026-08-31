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

The product-access overview positions alerts and notifications as communication about entitlement-state changes. It does not define alert evaluation, transport, delivery, latency, ordering, or access-enforcement behavior, so dedicated notification and webhook sources remain authoritative. [[source-metronome-guides-customers-billing-manage-customers-manage-product-access]]

### Point-in-time threshold lookup

`POST /v1/customer-alerts/list` returns threshold-notification configurations and current evaluation states for the required customer UUID property inside a supplied payload. The default collection contains enabled configurations only; optional non-empty `alert_statuses` can include enabled, disabled, or archived configurations. Each response item requires nested `alert` configuration and nullable `customer_status`, otherwise `ok`, `in_alarm`, or `evaluating`; archived configurations return null status. Optional `triggered_by` can state why a threshold fired, and nested `alert.updated_at` is described as the customer-status update time. Complete traversal requires following nullable envelope `next_page`, while ordering, total count, cursor lifetime, snapshot consistency, duplicate-or-skip behavior, evaluation freshness, and history completeness are undocumented.

> [!warning] Alert-type and identity conflict
> The list response example returns `low_credit_balance_reached`, which is absent from the same page's eleven-value `Alert.type` enum but appears in the separate shared Plan authority. The current customer/all-customer create authority instead includes `usage_threshold_reached` plus `billable_metric_id`, while the list and dedicated get response schemas omit both that type and its metric identity. Do not infer whether the example is stale, Plan-scoped, or runtime-valid, do not merge Plan and customer/Contract enums, and do not treat the returned configuration as exhaustive for unmatched types. This remains a current monitoring read, not alert creation, reset, archival, webhook delivery, entitlement enforcement, or merchant action. [[source-metronome-api-reference-alerts-get-all-threshold-notifications]] [[source-metronome-plans-shared-endpoints-notifications]] [[source-metronome-api-reference-alerts-create-a-threshold-notification]] [[source-metronome-api-reference-alerts-get-a-threshold-notification]]

`POST /v1/customer-alerts/get` retrieves the current evaluation state and configuration for one customer/threshold-notification pair identified by customer and alert UUIDs. `customer_status` is `ok`, `in_alarm`, `evaluating`, or `null` for an archived notification; archived lookup still returns the alert configuration. The operation is targeted rather than bulk and returns current state rather than history, which the page routes to webhook notifications or event logs. The API-wide POST idempotency rule means a same-key retry can replay an earlier result rather than establish a fresh evaluation. The narrative lists `updated_at` with the customer-alert surface, but the schema and example nest it under `alert`, so clients should not assume a top-level path. [[source-metronome-api-reference-alerts-get-a-threshold-notification]]

### Shared Plan and Contract endpoint surface

Metronome documents a shared alert endpoint family for Plans and Contracts: `/alerts/create`, `/customer-alerts/get`, `/customer-alerts/list`, `/customer-alerts/reset`, and `/alerts/archive`. The shared overview says entity-targeted input and response parameters can differ, but it does not identify which fields vary or provide HTTP methods, version prefixes, or operation schemas. For plan targeting, it lists `low_credit_balance_reached`, `low_remaining_days_in_plan_reached`, `low_remaining_credit_percentage_reached`, and `usage_threshold_reached` as supported `alert_type` values. Its unversioned `/customer-alerts/reset` route label does not replace the dedicated reference's `POST /v1/customer-alerts/reset` contract.

### Manual threshold reset

`POST /v1/customer-alerts/reset` accepts a Metronome customer UUID and threshold-notification UUID, clears cached evaluation state, and immediately initiates a fresh assessment against current thresholds. The reassessment runs in the background: `200` confirms reset and initiation but returns no body and does not reveal the resulting alert state. A breached threshold may produce a new webhook notification. The page does not define eligible current states, archived-alert behavior, an `EVALUATING` transition, completion signaling, error responses, duplicate suppression, retry safety, idempotency, concurrent-reset ordering, or whether repeated resets re-emit alarms. Its `requestBody` also lacks `required: true` even though both object properties are required.

Metronome separates threshold, system, and offset notifications. Threshold notifications monitor conditions such as spend or available credit; system notifications follow object creation, updates, or configured timestamps; offset notifications follow user-defined schedules relative to lifecycle events.

System and offset notifications are stateless. Threshold notifications are continuously evaluated, use `OK` and `IN_ALARM` as their ongoing states, and list `EVALUATING` before the initial evaluation. Evaluation occurs at least every three minutes, and the guide documents firing within five minutes after triggering usage is ingested. A return from `IN_ALARM` to `OK` may emit an optional `*_resolved` event.

The Data Export `alert` table now documents nullable `customer_id`: a null value means the configured alert applies to all customers. This identifies warehouse row scope only; it does not establish evaluation cadence, webhook delivery, ordering, or reset behavior. [[source-metronome-guides-reporting-insights-data-export-database-reference]]

Archiving a customer stops notifications associated with that customer from being triggered. The archive page does not specify the timing of that suppression or treatment of notification work already generated or in flight. [[source-metronome-api-reference-customers-archive-a-customer]]


## Offset notifications

### System lifecycle event-type discovery

`POST /v2/notifications/system/list` lists available read-only system lifecycle event-type configurations that can be used when creating offset notifications. A successful response requires a `data` array and may include a nullable string `cursor`; each configuration requires `type` and `policy`, while the policy requires a lifecycle-event `type`. The schema gives `contract.create` and `contract.start` only as examples, and the response example shows `SYSTEM_LIFECYCLE_EVENT` with `contract.create`. An optional `is_enabled` field reports whether webhook publishing for the lifecycle event is enabled. The page does not provide a request body, pagination input, exhaustive event-type catalog, enablement control, or offset-validation semantics.

Offset notifications apply a user-configured hour, day, week, month, or year displacement to a known system-event date. They can be managed in the UI or created with `POST /v2/notifications/create` using an ISO 8601 offset policy. The payload omits the threshold payload's `properties` field, and its `timestamp` records the source event time rather than the calculated offset fire time.

Offset generation is prospective: past fire times are not replayed, moving a fire time into the past does not produce a notification, and archiving the configuration before fire time prevents it. Offsets cannot fire before `.create`, `.edit`, or `.archive` events. For recurring commits, a before-`commit.segment.start` offset longer than the one-period-ahead child-generation horizon fires when the future child commit is created rather than at the earlier requested time.

## Customer-configured controls

### Threshold-notification creation contract

`POST /v1/alerts/create` creates a customer-scoped or all-customer threshold configuration. Within a supplied payload, `alert_type`, `name`, and numeric `threshold` are required; the request-body wrapper is not marked required. Narrative guidance additionally requires `billable_metric_id` for usage notifications and `credit_type_id` for credit-based notifications, but neither appears in the payload required array; `credit_type_id` selects the applicable pricing unit or currency and defaults to USD. Separately, the `seat_filter` description requires that object for `low_remaining_seat_balance_reached`, and its nested schema requires `seat_group_key` while leaving `seat_group_value` optional. `evaluate_on_create` defaults to true and immediately evaluates existing customers already meeting the threshold; false limits evaluation to future customers that trigger it. The page does not define the evaluation snapshot, completion, initial state, or notification timing. Its narrative says success returns `CustomerAlert` configuration and customer evaluation status, while the OpenAPI `200` schema and example return only UUID `data.id`; preserve the unresolved response-shape conflict without treating either representation as observed runtime truth. [[source-metronome-api-reference-alerts-create-a-threshold-notification]]

Separately, [[source-metronome-plans-shared-endpoints-notifications]] documents the shared unversioned `/alerts/create` route as creating a Plan or Contract alert and says entity-targeted input and response parameters differ. It lists Plan `alert_type` values `low_credit_balance_reached`, `low_remaining_days_in_plan_reached`, `low_remaining_credit_percentage_reached`, and `usage_threshold_reached`, while [[source-metronome-api-reference-alerts-create-a-threshold-notification]] documents customer-scoped or all-customer `POST /v1/alerts/create` with the distinct twelve-value `CreateCustomerAlertPayload` enum. Do not merge these enums or infer the Plan surface's HTTP method, version prefix, payload mapping, precedence, migration status, or runtime support.

The custom-field key creation page says values on commits, credits, and contracts can scope alert evaluation and illustrates a spend threshold limited to contracts with `contract_type=paygo`. Creating the key does not set that value or create, evaluate, reset, archive, or deliver an alert. The page does not define filter matching, missing-value treatment, evaluation timing, state, webhook delivery, or enforcement behavior; dedicated alert and webhook authorities remain controlling. [[source-metronome-api-reference-custom-fields-create-a-custom-field-key]]

A customer- or contract-level credit-balance threshold explicitly excludes seat-scoped credits. Seat-scoped monitoring instead uses `low_remaining_seat_balance_reached`. The guide requires the request-body `seat_filter` object when creating that notification and says the object provides `seat_group_key`; it does not independently establish the nested `seat_group_key` property as required. Optional `seat_filter.seat_group_value` narrows monitoring or lookup to one seat. Webhook receipt can drive merchant-owned access gating, but the guide does not make the alert an entitlement mutation. Its specific-seat get example is malformed JSON because it omits a comma between `alert_id` and `seat_filter`. [[source-metronome-guides-pricing-packaging-subscription-manage-seats]]

Credit and commit threshold notifications can monitor remaining balance, percent remaining, or days remaining. Custom fields can narrow a policy to a subset of commits or credits; the worked UI example selects **Contract credit balance** at `$0`, filters credit entities by `credit_type: free_trial`, and scopes the notification to selected customers. The guide presents product cutoff, renewal, and upsell as downstream use cases, but does not establish automatic access enforcement, entitlement mutation, customer communication, or sales action.

A merchant can create customer-scoped threshold alerts for billing-period spend, low remaining commit balance, and usage-invoice total. The spend-limit examples use `spend_threshold_reached` for both soft and hard limits; their names, thresholds, and merchant actions distinguish them rather than a documented native severity or enforcement field. Store returned alert IDs so webhook signals can be matched to the intended customer and rule. When a limit changes, the guide archives the previous alert before creating a replacement, without defining atomic replacement or gap behavior.

Spend alerts can be scoped with `group_values`, polled with customer-alert get/list endpoints, or consumed through webhooks. A hard-limit alarm, a zero commit balance, or any other threshold remains an action signal: the merchant owns customer communication, sales workflows, service cutoff, and later restoration. The guide does not establish an end-to-end latency guarantee, automatic entitlement mutation, maximum overshoot, payment outcome, or access-denial guarantee.

`spend_threshold_reached` evaluates usage-based spend before credit and commit drawdown. `invoice_total_reached` evaluates after drawdown and can be filtered to usage invoices. `low_remaining_commit_balance_reached` signals a configured commit-balance threshold, but the page does not define exactly which balances aggregate into it.

The prepaid-credit model uses `alerts.low_remaining_contract_credit_and_commit_balance_reached` at a zero threshold as a merchant action signal. The merchant stores the entitlement flag in its own database, checks it before each protected action, and changes it from payment and balance signals; the alert does not itself suspend product access. Because the same guide calls the webhook real-time without a latency, ordering, or consistency contract, the dedicated webhook delivery semantics remain authoritative.

For a parent contract's shared commit, child consumption does not automatically trigger the parent's commit-balance alert. The hierarchy guide says alerts evaluate when the parent receives usage and child-only usage may delay the parent alert until parent usage arrives. It gives no evaluation-latency or eventual-evaluation guarantee; webhook delivery mechanics remain a separate concern. Its next spend-alert bullet is truncated after `parent spend alerts only include parent's`, so no spend scope should be inferred from that sentence.

For `low_remaining_contract_credit_and_commit_balance_reached`, the default customer evaluation combines all active commits and credits into one balance and one threshold notification. `alert_specifiers` can include balances by ANDed custom-field conditions, OR multiple specifiers, remove balances through same-scope ORed exclusions, or evaluate each value of one custom-field key independently. Customer configuration scope is separate: the first two worked bodies omit `customer_id`, which the current create authority makes all-customer; the grouped guide explicitly applies that alert to all customers and all current and future promotions. A webhook's customer ID identifies the crossing customer's group rather than narrowing the stored configuration. The three create illustrations omit `uniqueness_key` and `credit_type_id` even though create prose calls each required for this use, while the payload required array omits both; they are matching illustrations, not complete requests. `uniqueness_key` resource duplication is distinct from API-wide `Idempotency-Key` result replay. The property-level default-USD statement and separate USD-cent authority do not justify converting the guide's literal `threshold: 10000` without accepted pricing-unit and scaling evidence. Same-key replay of the POST status lookup is not fresh evaluation proof. The guide lookup response keeps `customer_status: in_alarm` but uses `data.alert.alert_type`, `status: active`, and no `updated_at`; the dedicated current get schema instead requires `data.alert.type`, requires `updated_at`, and limits status to `enabled`, `archived`, or `disabled`. Keep the dedicated get source authoritative and do not normalize either response representation into runtime truth. Configuration, evaluation, delivery, balance mutation, invoicing, and merchant action remain separate, and the guide retains its singular/plural filter and `ContractCreditorCommit`/`ContractCreditOrCommit` tensions. [[source-metronome-guides-customers-billing-set-up-notifications-create-alert-specifiers]] [[source-metronome-api-reference-alerts-create-a-threshold-notification]] [[source-metronome-api-reference-alerts-get-a-threshold-notification]] [[source-metronome-api-reference-idempotency]] [[source-metronome-guides-pricing-packaging-make-pricing-changes-use-currency-custompricingunits]] [[source-metronome-guides-customers-billing-optimize-customer-experience-customer-controls]]

## Sources

- [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-guarantee-zero-overages]] - balance-threshold or webhook signals as inputs to merchant-owned post-commit access gating rather than native usage rejection
- [[source-metronome-guides-customers-billing-manage-customers-manage-product-access]] - product-access navigation framing alerts and notifications as communication about entitlement-state changes
- [[source-metronome-guides-pricing-packaging-subscription-manage-seats]] — exclusion of seat-scoped credits from general balance alerts, seat-filter object requiredness, optional one-seat scoping, malformed lookup example, and merchant-owned access response

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

- [[source-metronome-api-reference-customers-archive-a-customer]] - customer-archive suppression of associated notification triggers, with timing and already-generated or in-flight scope unspecified
- [[source-metronome-guides-customers-billing-set-up-notifications-system-notifications]] - contract, commit, and credit lifecycle policy catalog; account-wide enablement; payload-family distinction; and prospective-only, immutable-policy boundaries


- [[source-metronome-api-reference-alerts-get-a-threshold-notification]] — customer/notification identity, current evaluation state, archived-state behavior, targeted-read scope, configuration response, and timestamp-path conflict

## Related

- [[metronome-webhooks]]
- [[metronome-credits-and-commits]]
- [[metronome-customers-and-contracts]]
- [[metronome-usage-based-billing]]
