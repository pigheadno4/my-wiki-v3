---
title: "Metronome Create a Billable Metric API"
type: source
date_ingested: 2026-07-30
canonical_url: "https://docs.metronome.com/api-reference/billable-metrics/create-a-billable-metric"
original_format: webpage
raw_files:
  - "metronome/api-reference/billable-metrics/create-a-billable-metric-2026-07-13.md"
tags: [metronome, api, billable-metrics, streaming-metrics, sql-metrics]
---

## Overview

This API reference documents Metronome's bearer-authenticated `POST https://api.metronome.com/v1/billable-metrics/create` endpoint. It creates one billable-metric resource from either standard filtering and aggregation fields or a mutually exclusive SQL query, then returns the created metric's UUID for use with products, usage endpoints, and alerts.

## Key takeaways

- The request is JSON and the OpenAPI operation uses bearer authentication against the production API host.
- `name` is the only field in the payload schema's top-level `required` array. A supplied `sql` query excludes `aggregation_type`, `event_type_filter`, `property_filters`, `aggregation_key`, and `group_keys`; `custom_fields` is not named in that exclusion list.
- Standard definitions filter events by event type and properties, aggregate with a case-insensitive-looking enum of `COUNT`, `LATEST`, `MAX`, `SUM`, or `UNIQUE` spellings, and can group invoice usage costs into nested sets of property keys. The page does not explicitly promise case-insensitive handling beyond listing three spellings of every enum member.
- A successful HTTP `200` response contains required `data.id` as a UUID. The operation defines no non-200 response, error envelope, rate limit, or retry behavior.
- Several conditional rules conflict or remain incomplete: `aggregation_key` is described as required without SQL but inapplicable to `count`, the request body itself is not marked required, and `not_in_values` is described as both allowing empty input and requiring a non-empty array when present.

## Endpoint and authentication

- Method and path: `POST /v1/billable-metrics/create`
- Production base URL: `https://api.metronome.com`
- Security scheme: HTTP bearer authentication (`bearerAuth`)
- Request media type: `application/json`
- Operation ID: `createBillableMetricV1-v1`

The OpenAPI `requestBody` points to `CreateBillableMetricV1Payload` but does not set `required: true`. This page therefore does not establish whether an omitted body is rejected before schema validation. It also does not show the literal `Authorization` header or define token scope, expiry, or lifecycle behavior.

## Request schema

| Field | Schema and documented behavior |
| --- | --- |
| `name` | Required string and display name. No length, uniqueness, normalization, or character constraints are documented. |
| `sql` | Optional string containing the SQL query. Mutually exclusive with `aggregation_type`, `event_type_filter`, `property_filters`, `aggregation_key`, and `group_keys`; when supplied, those five fields must be omitted. The page does not define a SQL dialect, output contract, validation behavior, query limits, or whether `custom_fields` can accompany SQL beyond its omission from the exclusion list. |
| `event_type_filter` | Optional object with `in_values` and `not_in_values` string arrays. Each array must be non-empty when present. |
| `property_filters` | Optional array of property-filter objects. Every filter rule must pass for an event to match the metric. |
| `aggregation_type` | Optional at the top-level schema level. Accepted enum spellings are `count`, `Count`, `COUNT`, `latest`, `Latest`, `LATEST`, `max`, `Max`, `MAX`, `sum`, `Sum`, `SUM`, `unique`, `Unique`, and `UNIQUE`. |
| `aggregation_key` | Optional in the top-level `required` array but separately described as required when `sql` is absent. It must name one of the property filters and is not applicable to `count`. |
| `group_keys` | Optional array whose items are arrays of strings. Each inner set names properties used to slice events into distinct invoice-usage-cost buckets. |
| `custom_fields` | Optional object with arbitrary keys and string values. No key, value, or entry-count limits are documented. |

The example creates `CPU Hours`, includes only `cpu_usage` events, requires `cpu_hours`, `region`, and `machine_type`, restricts the latter two properties to named values, performs `SUM` over `cpu_hours`, and supplies separate singleton group-key sets for `region` and `machine_type`.

## Filter semantics

`event_type_filter.in_values` includes only listed event types, while `not_in_values` excludes listed event types. Both are optional and must be non-empty if present. The schema does not define the result when both arrays are supplied, when their values overlap, or when the filter object is empty.

Each `property_filters` entry requires `name`. Its optional controls are:

- `exists: true` accepts only events containing the property; `false` accepts only events without it; null or omission makes existence optional.
- `in_values` accepts only listed property values; when undefined, all values pass. It must be non-empty when present.
- `not_in_values` rejects listed property values. Its description says null or empty means all values pass, then says it must be non-empty when present.

All property-filter entries must pass for an event to match. The page does not define how `exists: false` interacts with either value list, how overlapping include/exclude values are resolved, whether property values are coerced to strings, or whether duplicate filters for the same property are allowed.

## Aggregation and group keys

The narrative calls metrics built from standard filters and aggregation **Streaming billable metrics**, optimized for ultra-low latency and high-throughput workflows, and directs more flexible aggregation requirements to SQL billable metrics. It gives no numeric latency, throughput, availability, or query-complexity limits.

`aggregation_key` selects the event property to aggregate, must equal a property-filter name, and does not apply to `count`. However, its field-level description first says it specifies the aggregation type and then says it is required whenever SQL is absent. That wording conflicts with the separate `aggregation_type` field, with `aggregation_key` being inapplicable to `count`, and with the payload's required array containing only `name`.

> [!warning] Aggregation documentation conflict
> The endpoint enum includes `unique`, `Unique`, and `UNIQUE` among standard aggregation types. The separate create-billable-metrics guide says streaming metrics support `COUNT`, `SUM`, `MAX`, and `LATEST` and directs distinct counting to SQL. This endpoint does not define `UNIQUE` semantics or reconcile that difference, so callers should not infer that API `UNIQUE` is the same operation as SQL distinct counting.

`group_keys` is an array of string arrays rather than a flat list. Each entry is a set of event-property names used to divide usage costs into invoice buckets; the example supplies `[["region"], ["machine_type"]]`. The endpoint schema gives no non-empty requirement, maximum number of sets or properties, duplicate behavior, cardinality limit, ordering guarantee, or explicit property-filter prerequisite.

## Response

HTTP `200` is the only documented response. Its JSON object requires `data`, and `data` requires an `id` string in UUID format:

```json
{
  "data": {
    "id": "58fb0650-e54a-4d17-93cb-ba8e56c32c65"
  }
}
```

The narrative says the created metric can be used in products, usage endpoints, and alerts. It also says setup workflows can create individual or multiple metrics, but this operation accepts one object and returns one ID; the page defines no batch request or multi-ID response, so "multiple" may mean repeated endpoint calls rather than one batch.

## Errors, limits, contradictions, and unknowns

- No `4xx` or `5xx` responses, validation-error shape, authentication-failure response, or endpoint-specific conflict behavior is defined.
- No rate limit, retry policy, idempotency behavior, timeout, or partial-creation recovery rule is stated on this page.
- Beyond non-empty filter arrays and the aggregation-key/property-filter relationship, there are no numeric request, SQL, custom-field, filter, or group-key limits.
- The OpenAPI does not mark the request body required even though a supplied payload requires `name`.
- The `aggregation_key` descriptions conflict over whether it selects an event property or an aggregation type, and its no-SQL requirement conflicts with its `count` exclusion and the schema's required array.
- The `not_in_values` description simultaneously allows an empty value and requires a non-empty array when present.
- The page does not define interactions between include and exclude filters, compound group-key behavior, the meaning of `UNIQUE`, SQL result requirements, or case normalization for aggregation enum values.
- The request schema and response are singular despite narrative language about creating multiple metrics in a setup workflow.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-billable-metrics]], [[metronome-event-ingestion]], [[metronome-products-and-rate-cards]], [[metronome-usage-based-billing]]
- Related sources: [[source-metronome-guides-implement-metronome-core-concepts-create-billable-metrics]], [[source-metronome-api-reference-authentication]], [[source-metronome-api-reference-status-codes]], [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/billable-metrics/create-a-billable-metric-2026-07-13|2026-07-13 snapshot — create-billable-metric endpoint schema, filters, aggregation, grouping, and response]]
