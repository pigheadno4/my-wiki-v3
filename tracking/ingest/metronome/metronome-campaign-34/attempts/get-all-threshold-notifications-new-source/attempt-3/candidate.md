---
title: "Metronome Get All Threshold Notifications API"
type: source
date_ingested: 2026-08-31
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/alerts/get-all-threshold-notifications"
raw_files:
  - "metronome/api-reference/alerts/get-all-threshold-notifications-2026-08-28.md"
tags: [metronome, api, alerts, threshold-notifications, monitoring, pagination]
---

## Overview

This OpenAPI page documents bearer-authenticated `POST /v1/customer-alerts/list`, a customer-scoped collection read for threshold-notification configurations and their current evaluation states. It supports dashboard, admin, triggering-status, and coverage-audit queries, but it is not a notification-history, webhook-delivery, dashboard-rendering, or merchant-action contract.

## Query-critical facts

- Inside a supplied JSON payload, UUID `customer_id` is a required property. The enclosing OpenAPI `requestBody` is not marked `required: true`, so omitted-body behavior is not established; the payload also has no `additionalProperties: false`, so unknown-field behavior is undocumented.
- When `alert_statuses` is absent, the endpoint returns only enabled threshold notifications. A supplied array has `minItems: 1` and can select enabled, disabled, or archived configurations using the documented casing variants; use the exact raw enum rather than normalizing an undocumented input form.
- HTTP `200` requires sibling response-envelope fields `data` and nullable `next_page`. Each `data[]` item requires `customer_status` and nested `alert`; `customer_status` is `ok`, `in_alarm`, `evaluating`, or `null`, with `null` documented for archived notifications. Optional nullable `triggered_by` can state why a threshold was triggered.
- The nested `alert` object carries configuration identity and current monitoring metadata. Its required fields are `id`, `name`, `type`, `status`, `threshold`, and `updated_at`; the timestamp is described as when that notification's customer status was last updated. Type-specific credit, custom-field, group, invoice, seat, access-type, and alert-specifier details remain in the complete raw schema, but the page's complete-configuration wording does not establish exhaustive representation for alert types that conflict with or are absent from its response schema.
- Pagination uses optional query parameter `next_page`; the response cursor is a nullable sibling of `data`, not nested in an alert or array item. Complete traversal requires following each non-null cursor, but the page defines no page-size control, default size, result ordering, total count, cursor lifetime, stable snapshot, duplicate-or-skip behavior under change, or cross-page completeness guarantee.

## Material contradiction

> [!warning] Alert-type and identity conflict
> The assigned response example returns `type: low_credit_balance_reached`, but that value is absent from the same page's eleven-value `Alert.type` response enum. The separate shared Plan-and-Contract authority lists `low_credit_balance_reached` as a Plan alert type, while the current customer-scoped or all-customer create authority instead documents a distinct twelve-value enum that includes `usage_threshold_reached` and supplies `billable_metric_id` for usage notifications; the list page and dedicated get response schemas expose neither that type nor its metric identity. These sources do not establish whether the list example is stale, Plan-scoped, or runtime-valid. Do not merge the Plan and customer/Contract enums, treat the list enum as exhaustive across those surfaces, or assume the returned configuration can represent the unmatched type-specific identity. [[source-metronome-plans-shared-endpoints-notifications]] [[source-metronome-api-reference-alerts-create-a-threshold-notification]] [[source-metronome-api-reference-alerts-get-a-threshold-notification]]

## Material boundaries

The prose calls the endpoint a comprehensive customer view and proposes dashboards, admin panels, triggering checks, and coverage audits. Those uses remain constrained by the default enabled-only filter, cursor traversal, and the alert-type and metric-identity conflict above. The page does not define evaluation cadence, response as-of time, data freshness, polling interval, history retention, or completeness under concurrent configuration or evaluation changes; `updated_at` is per nested alert rather than an envelope snapshot marker.

This operation reads current configuration and evaluation state. It does not create, reset, disable, archive, or enforce a threshold; render or secure a dashboard; emit or deliver a webhook; retain event history; notify a customer; mutate credits, commits, invoices, or entitlements; or guarantee a downstream merchant action. Dedicated alert-lifecycle, webhook, and reporting authorities remain controlling for those surfaces.

Because the read uses POST, the separate API-wide [[metronome-api-idempotency|`Idempotency-Key` authority]] applies. When an `Idempotency-Key` request begins executing—meaning it has passed validation and does not conflict with another concurrent request—the API-call result is persisted; identical same-key parameters then replay that original result. The authority does not establish persisted replay results for validation failures or pre-execution concurrent-request conflicts. For admitted requests, changed parameters return HTTP `409`, keys persist for at least 24 hours, and a cached result can be HTTP `500`. Advancing `next_page` changes request parameters, so reuse of the same key for the next cursor is governed by the changed-parameter `409` rule rather than being wholly undocumented. A same-key replay of identical parameters is not a fresh threshold evaluation or a new pagination snapshot. Neither this endpoint nor the API-wide authority requires header use here, prescribes a preferred new-key policy for cursor pages, or establishes cross-page snapshot stability. Beyond the API-wide admission boundary, this endpoint adds no behavior for absent, different, or expired keys; concurrent alert configuration or evaluation changes; cursor lifetime or replay; cached-error recovery; or read-after-change visibility. [[source-metronome-api-reference-idempotency]]

The operation lists only HTTP `200`; it supplies no endpoint-specific invalid-customer, invalid-status, cursor, authentication, authorization, throttling, timeout, or server-error contract. Schemas without closed-object declarations do not prove response exhaustiveness or request unknown-field acceptance.

## Raw-detail coverage map

- **Operation and request:** production server, bearer scheme, POST path and operation ID, unmarked request-body wrapper, required customer UUID property inside a supplied payload, optional non-empty configuration-status array, casing variants, and enabled-only default are in raw.
- **Response placement and traversal:** required envelope `data` and nullable sibling `next_page`, request query cursor, the two-item example including `low_credit_balance_reached`, and absent page-size, ordering, total-count, snapshot, and freshness guarantees are in raw; the example value is not in the page's response enum.
- **Current state and configuration:** nullable evaluation state, optional trigger reason, required nested alert metadata, the eleven-value list/get response enum, three configuration statuses, threshold and timestamp semantics, and type-specific filter schemas are in raw. The separate Plan authority includes the example's `low_credit_balance_reached`, while the current customer/all-customer create authority includes `usage_threshold_reached` plus `billable_metric_id`; do not treat the list response configuration as exhaustive for those unmatched types.
- **Nested schema catalog:** credit type, uniqueness key, custom-field, group-key and group-value, invoice-type, seat, access-type, and inclusive/exclusive alert-specifier structures plus feature annotations remain in the exact raw page.
- **Evidence and authority boundary:** the raw preserves the dashboard/admin and audit use cases, default-versus-explicit filtering, pagination guidance, example values, complete eleven-value response enum, absent closed-schema declarations, and missing endpoint error catalog. The worked example, list schema, shared Plan authority, and current customer/all-customer create authority disagree on representable alert types and usage-metric identity; dedicated alert, reporting, webhook, and idempotency authorities remain controlling for lifecycle, delivery, external presentation, history, replay, and recovery semantics.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-alerts-and-notifications]], [[metronome-reporting-and-analytics]], [[metronome-api-idempotency]], [[metronome-webhooks]]
- Related sources: [[source-metronome-api-reference-alerts-get-a-threshold-notification]], [[source-metronome-api-reference-alerts-create-a-threshold-notification]], [[source-metronome-api-reference-alerts-reset-a-threshold-notification]], [[source-metronome-plans-shared-endpoints-notifications]], [[source-metronome-guides-customers-billing-set-up-notifications-create-and-manage-notifications]], [[source-metronome-guides-platform-configuration-setup-webhooks]], [[source-metronome-guides-reporting-insights-in-app-reporting]], [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/alerts/get-all-threshold-notifications-2026-08-28|2026-08-28 snapshot - complete customer-scoped threshold-notification list narrative, filters, current-state response, pagination, nested configuration schemas, and OpenAPI metadata]]
