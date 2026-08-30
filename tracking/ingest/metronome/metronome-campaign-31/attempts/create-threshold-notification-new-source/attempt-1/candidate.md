---
title: "Metronome API Reference: Create a Threshold Notification"
type: source
date_ingested: 2026-08-30
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/alerts/create-a-threshold-notification"
raw_files:
  - "metronome/api-reference/alerts/create-a-threshold-notification-2026-08-28.md"
tags: [metronome, api, alerts, threshold-notifications, webhooks, idempotency]
---

## Overview

Bearer-authenticated `POST /v1/alerts/create` creates a threshold-notification configuration for one customer or all customers. The operation covers spend, usage, invoice-total, credit, commit, and seat-balance signals; it creates an action signal, not an automatic customer-access, collection, or billing intervention.

## Query-critical facts

- When a JSON payload is supplied, `alert_type`, `name`, and numeric `threshold` are required. The enclosing OpenAPI `requestBody` is not marked `required: true`, so omitted-body behavior is not established. The payload schema does not declare `additionalProperties: false`, so unknown-field handling is also unspecified.
- Supplying UUID `customer_id` scopes the configuration to that customer; omitting it creates a notification for all customers. The twelve documented `alert_type` values span spend, monthly-invoice spend, usage, remaining days, balances or percentages for commits and contract credits, combined credit-and-commit balance, invoice total, and seat balance. The numeric threshold can represent a financial amount, days remaining, or a percentage depending on type; the page does not define denomination, comparison boundary, rounding, or percentage basis.
- Type-specific fields remain under the top-level payload: `billable_metric_id` selects the metric for `usage_threshold_reached`; `group_values` applies only to `spend_threshold_reached`; `invoice_types_filter` applies only to `invoice_total_reached`; and `alert_specifiers` applies only to the combined contract-credit-and-commit balance type. For `low_remaining_seat_balance_reached`, the description conditionally requires the `seat_filter` object, whose own schema requires nested `seat_group_key` while leaving `seat_group_value` optional. The raw reference remains authoritative for every filter, supported-type list, and nested schema.
- `evaluate_on_create` defaults to true: true immediately evaluates existing customers already meeting the threshold, while false evaluates only future customers that trigger it. This does not define a completion response, evaluation snapshot, initial state, latency, ordering with concurrent billing data, or whether a webhook is emitted during the create call.
- Optional 1-128 character `uniqueness_key` is stored as resource identity: reuse prevents another record and documents HTTP `409`, although the operation response map lists only `200`. Separately, the API-wide [[source-metronome-api-reference-idempotency|POST idempotency authority]] applies `Idempotency-Key`: identical same-key parameters replay the original result, changed parameters return `409`, retention is at least 24 hours, and a cached result can be HTTP `500`. The two keys' scope, precedence, failed-attempt consumption, concurrency behavior, and recovery interaction are not defined.
- The OpenAPI `200` response requires only `data.id`, a UUID identifying the created record. The page does not establish read-after-create visibility, the created notification's initial status, or evaluation outcome in the create response.

## Material boundaries

> [!warning] Response-shape conflict
> The narrative says a successful response returns a `CustomerAlert` containing configuration and `ok`, `in_alarm`, or `evaluating` customer status, but the operation's `200` schema and example return only `data.id`. Treat only the UUID response shape as the OpenAPI contract and use the dedicated get operation for current customer evaluation state; this page does not reconcile the conflict.

The page calls evaluation and webhook integration real-time and tells users to configure webhook endpoints before creating notifications. It gives no create-specific evaluation or delivery SLA, payload, destination-selection, retry, deduplication, ordering, signature, or failure guarantee. Dedicated notification guidance documents an ordinary threshold-evaluation cadence and dedicated webhook guidance documents at-least-once delivery; neither turns successful creation or evaluation into automatic access enforcement, payment recovery, invoice finalization, or another downstream action.

Beyond the `uniqueness_key` description's `409`, the operation declares no error responses. It does not define validation failures for incompatible or missing type-specific fields, authorization or not-found behavior, partial creation, rollback, update or archive lifecycle, uniqueness-key release timing, propagation to reads or exports, concurrent creation, or recovery after an ambiguous or cached failure.

## Raw-detail coverage map

Use the exact raw page for the complete twelve-value alert-type enum; every top-level filter and its supported notification types; the `access_type` spellings and QUANTITY/credit-type restriction; custom-field, group-value, seat-filter, invoice-type, and nested alert-specifier schemas; feature annotations; request and response examples; bearer-security declaration; operation ID; and the complete shared OpenAPI tag descriptions. The raw page also preserves the exact narrative-versus-`200` response conflict, conditionally required descriptions, schemas without closed-object declarations, and the absence of an operation-level error catalog.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-alerts-and-notifications]], [[metronome-api-idempotency]], [[metronome-webhooks]]
- Related sources: [[source-metronome-api-reference-alerts-get-a-threshold-notification]], [[source-metronome-api-reference-alerts-reset-a-threshold-notification]], [[source-metronome-guides-customers-billing-set-up-notifications-create-and-manage-notifications]], [[source-metronome-guides-platform-configuration-setup-webhooks]], [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/alerts/create-a-threshold-notification-2026-08-28|2026-08-28 snapshot - complete threshold-notification create narrative, request and nested filter schemas, response schema, and OpenAPI metadata]]
