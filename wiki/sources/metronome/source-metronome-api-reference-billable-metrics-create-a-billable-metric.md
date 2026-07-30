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

This reference documents bearer-authenticated `POST /v1/billable-metrics/create`. It creates one metric from standard filters and aggregation fields or a mutually exclusive SQL query, then returns the created UUID for use with products, usage endpoints, and alerts.

## Request shape

The OpenAPI request body is JSON but is not itself marked `required: true`. The payload schema requires only `name`.

| Field | Documented behavior |
| --- | --- |
| `name` | Required display-name string; no length, uniqueness, or normalization rules. |
| `sql` | Mutually exclusive with aggregation type, event-type filter, property filters, aggregation key, and group keys. SQL dialect, output contract, validation, and limits are not defined. |
| `event_type_filter` | Optional include/exclude string arrays, each non-empty when present. |
| `property_filters` | Optional array; all filter objects must pass for an event to match. |
| `aggregation_type` | Lists lower-, title-, and uppercase spellings of COUNT, LATEST, MAX, SUM, and UNIQUE. This does not explicitly promise general case-insensitive handling. |
| `aggregation_key` | Must name a property filter and is not applicable to count, yet is also described as required whenever SQL is absent. |
| `group_keys` | Array of string arrays used to slice invoice usage costs into buckets. |
| `custom_fields` | Arbitrary string-valued map; no key, value, or entry limits. |

The example includes `cpu_usage` events, requires `cpu_hours`, `region`, and `machine_type`, restricts region and machine values, sums `cpu_hours`, and supplies `[["region"], ["machine_type"]]`.

## Filtering

Event include/exclude interactions, overlapping values, and an empty filter object are undefined. Each property filter requires a name. `exists` can require presence, require absence, or leave existence optional; include values allow only matches and exclude values reject matches.

The `not_in_values` description says null or empty allows all values and then says the array must be non-empty when present. Interactions between `exists: false` and value lists, duplicate filters, coercion, and include/exclude precedence are undocumented.

## Aggregation and grouping

Standard definitions are called streaming metrics and SQL is recommended for more flexible aggregation. No numeric latency, throughput, availability, or query-complexity guarantees are given.

> [!warning] Aggregation conflicts
> `aggregation_key` is variously described as the property to aggregate, the aggregation type, required without SQL, and inapplicable to count. Only `name` appears in the schema's required array.

> [!warning] UNIQUE conflict
> This endpoint enumerates `UNIQUE`, while the separate metric guide limits streaming metrics to COUNT, SUM, MAX, and LATEST and directs distinct counts to SQL. The endpoint does not define UNIQUE or reconcile the difference.

Nested `group_keys` have no non-empty rule, maximum, duplicate behavior, cardinality limit, ordering guarantee, or explicit property-filter prerequisite.

## Response and operational boundaries

HTTP `200` returns required `data.id` as a UUID. No non-200 responses, error envelope, rate limit, retry policy, idempotency behavior, timeout, or partial-creation recovery are documented.

The narrative mentions creating multiple metrics as part of a setup workflow, but this operation accepts one object and returns one ID. It does not define a batch create.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-billable-metrics]], [[metronome-event-ingestion]], [[metronome-products-and-rate-cards]], [[metronome-usage-based-billing]]
- Related sources: [[source-metronome-guides-implement-metronome-core-concepts-create-billable-metrics]], [[source-metronome-api-reference-authentication]], [[source-metronome-api-reference-status-codes]], [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/billable-metrics/create-a-billable-metric-2026-07-13|2026-07-13 snapshot — create endpoint schema, filters, aggregation, grouping, and response]]
