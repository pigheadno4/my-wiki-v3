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

Bearer-authenticated `POST /v1/alerts/create` creates a threshold-notification configuration for one customer or all customers. Subsequent threshold evaluation can produce a notification delivered through configured webhooks as a merchant action signal; creation itself is not an automatic customer-access, collection, payment, or billing intervention.

## Query-critical facts

- When a JSON payload is supplied, `alert_type`, `name`, and numeric `threshold` are required properties. The enclosing OpenAPI `requestBody` is not marked `required: true`, so omitted-body behavior is not established. The payload schema does not declare `additionalProperties: false`, so unknown-field handling is also unspecified.
- Supplying UUID `customer_id` scopes the configuration to that customer; omitting it creates a notification for all customers. The twelve documented `alert_type` values span spend, monthly-invoice spend, usage, remaining days, balances or percentages for commits and contract credits, combined credit-and-commit balance, invoice total, and seat balance. Depending on type, numeric `threshold` can represent a financial amount, days remaining, or a percentage; the page does not define the comparison boundary, rounding, or percentage basis.
- Narrative usage guidance says `billable_metric_id` is required for usage notifications and `credit_type_id` for credit-based threshold notifications, but neither property appears in `CreateCustomerAlertPayload`'s required array. The `credit_type_id` description says it identifies the pricing unit or currency for types that require one and defaults to USD. This narrative-versus-required-array boundary is separate from `seat_filter`: its description says the object is required for `low_remaining_seat_balance_reached`, while the nested `seat_filter` schema itself requires `seat_group_key` and leaves `seat_group_value` optional. The raw reference remains authoritative for all other filters, supported-type lists, and nested schemas.
- `evaluate_on_create` defaults to true: true immediately evaluates existing customers already meeting the threshold, while false evaluates only future customers that trigger it. This does not define a completion response, evaluation snapshot, initial state, latency, ordering with concurrent billing data, or whether a webhook is emitted during the create call.
- The usage guidance says each threshold notification must have a `uniqueness_key` unique within the organization, while the payload required array omits that field even though the schema attaches it to `CreateCustomerAlertPayload`. Its component permits 1-128 characters, stores a resource-level duplicate guard, and says reuse prevents a new record and fails with HTTP `409`; archival guidance says `release_uniqueness_key: true` permits reuse. Separately, the API-wide [[source-metronome-api-reference-idempotency|POST idempotency authority]] applies `Idempotency-Key`: identical same-key parameters replay the original result, changed parameters return `409`, retention is at least 24 hours, and a cached result can be HTTP `500`. Resource uniqueness and request-result replay are distinct. Their interaction or precedence, uniqueness-key normalization, concurrent-creation ordering, release visibility, failed-attempt key consumption, behavior after header-key expiry, and recovery after a cached or ambiguous failure are not defined.

## Material boundaries

> [!warning] Response-shape conflict
> The narrative says success returns a `CustomerAlert` containing the threshold configuration and customer evaluation status (`ok`, `in_alarm`, or `evaluating`), while the OpenAPI `200` schema and example return only UUID `data.id`. The page does not reconcile these representations, so neither should be elevated beyond its documented narrative or OpenAPI scope. Use the dedicated get source for the separately documented current customer-evaluation lookup, not as proof of the create response's observed runtime shape.

The page says threshold notifications trigger webhook notifications and tells users to configure webhook endpoints before creating them. It supplies no create-specific payload, emission condition, evaluation-to-delivery SLA, destination-selection, retry, deduplication, ordering, signature, or failure guarantee. Dedicated notification guidance documents an ordinary threshold-evaluation cadence and dedicated webhook guidance documents at-least-once delivery; neither makes a successful create response evidence that evaluation completed, a webhook was emitted or delivered, or a downstream merchant action succeeded.

Beyond the `uniqueness_key` description's `409`, the operation declares no error responses. It does not define validation failures for incompatible or missing type-specific fields, authorization or not-found behavior, partial creation, rollback, update or archive lifecycle, uniqueness-key release timing, read-after-create visibility, propagation to reads or exports, concurrent creation, or recovery after an ambiguous or cached failure.

## Raw-detail coverage map

Use the exact raw page for the complete twelve-value alert-type enum; every top-level filter and its supported notification types; the `access_type` spellings and QUANTITY/credit-type restriction; custom-field, group-value, seat-filter, invoice-type, and nested alert-specifier schemas; feature annotations; request and response examples; bearer-security declaration; operation ID; and the complete shared OpenAPI tag descriptions. The raw page also preserves the narrative-versus-schema conflicts for `uniqueness_key`, type-specific requiredness, and the success response; conditionally required descriptions; schemas without closed-object declarations; and the absence of an operation-level error catalog.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-alerts-and-notifications]], [[metronome-api-idempotency]], [[metronome-webhooks]]
- Related sources: [[source-metronome-api-reference-alerts-get-a-threshold-notification]], [[source-metronome-api-reference-alerts-reset-a-threshold-notification]], [[source-metronome-guides-customers-billing-set-up-notifications-create-and-manage-notifications]], [[source-metronome-guides-platform-configuration-setup-webhooks]], [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/alerts/create-a-threshold-notification-2026-08-28|2026-08-28 snapshot - complete threshold-notification create narrative, request and nested filter schemas, response schema, and OpenAPI metadata]]
