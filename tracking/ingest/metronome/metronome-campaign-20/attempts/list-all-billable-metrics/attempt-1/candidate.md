---
title: "Metronome List All Billable Metrics API"
type: source
date_ingested: 2026-08-23
canonical_url: "https://docs.metronome.com/api-reference/billable-metrics/list-all-billable-metrics.md"
original_format: webpage
raw_files:
  - "metronome/api-reference/billable-metrics/list-all-billable-metrics-2026-07-13.md"
tags: [metronome, api, billable-metrics, pagination, archived-metrics]
---

## Overview

This reference documents bearer-authenticated `GET /v1/billable-metrics`, which returns billable metrics with their configurations for programmatic discovery and management. The page specifically suggests using the list to associate metrics with products and audit orphaned or archived metrics; archived metrics are excluded by default and require `include_archived=true`.

## Key takeaways

- The operation has no request body. Its optional query parameters are `limit`, `next_page`, and `include_archived`.
- `limit` accepts integers from `1` through `100`; `next_page` is a string cursor indicating where the following page begins. The page states no default page size or result order.
- HTTP `200` requires both a `data` array and a nullable string `next_page`; `null` is the documented terminal cursor value under the separate API-wide pagination convention.
- Each returned metric requires only UUID `id` and string `name`. Event and property filters, aggregation type and key, group keys, custom fields, SQL, and archive timestamp are optional in this response schema.
- The response exposes complete configurations in the page's wording, but it supplies no metric-type discriminator, version, product association, orphan-status flag, or reason a metric is considered orphaned.

## Request and pagination

The production route is `GET https://api.metronome.com/v1/billable-metrics`, operation ID `listAllBillableMetrics-v1`, under an HTTP bearer-authentication requirement. Because this is a GET operation, request-body requiredness, payload-required properties, and request-body unknown-field behavior do not apply.

`limit` is optional with a minimum of `1` and maximum of `100`. `next_page` is an optional string cursor. A successful response requires both `data` and `next_page`, with the latter nullable. The endpoint does not define its default limit, sort order, cursor lifetime, snapshot consistency, cursor binding to `include_archived`, malformed-cursor errors, or duplicate and skipped-record behavior while configurations change during traversal.

`include_archived` is an optional boolean. Archived metrics are excluded by default, and callers set it to `true` to include them. The page does not define whether archive filtering occurs before pagination, how quickly archival propagates to a traversal, whether an in-progress cursor preserves its original archive scope, or whether archived entries are ordered separately.

## Returned configuration

Every array item uses `BillableMetricV1`; only `id` and `name` are schema-required. The optional fields have these documented meanings and boundaries:

| Field | Documented behavior |
| --- | --- |
| `event_type_filter` | Optional include and exclude arrays for event types; each must be non-empty when present. Overlap, precedence, duplicate, and case behavior are unspecified. |
| `property_filters` | Array of property rules, each requiring `name`; all supplied rules must pass. `exists` can require presence or absence, and value lists admit or reject specified values. |
| `aggregation_type` | Enumerates lower-, title-, and uppercase spellings of COUNT, LATEST, MAX, SUM, and UNIQUE. The enumeration does not promise arbitrary case normalization or define UNIQUE semantics. |
| `aggregation_key` | Event-property key used for aggregation; it must be one of the property-filter names and is inapplicable to count. The response schema does not say which other aggregations require it. |
| `group_keys` | Array of string arrays used to group usage costs into invoice buckets. Non-empty rules, size limits, duplicate behavior, order, and property-filter prerequisites are not stated. |
| `custom_fields` | Object explicitly permitting arbitrary property names whose values are strings. No key, value, count, visibility, or redaction limits are documented. |
| `sql` | SQL query associated with the metric. This endpoint gives no dialect, output contract, limits, redaction rule, or discriminator between SQL and standard metrics. |
| `archived_at` | RFC 3339 timestamp indicating when the metric was archived; omission means it is not archived. |

Except for the string-valued `additionalProperties` declaration on `custom_fields`, the response object schemas do not declare `additionalProperties`; this page therefore does not establish whether undocumented response fields are forbidden, ignored, or may appear. Consumers should not infer a closed response contract from omission alone.

## Matching and schema inconsistencies

All property-filter rules must pass. `exists: true` requires the event property, `exists: false` requires its absence, and null or omission leaves existence optional. `in_values` admits only listed values and must be non-empty when present. The `not_in_values` description says null or an empty list lets all values pass and also says the list must be non-empty when present, leaving empty-list validity contradictory. Interactions among existence checks, value filters, duplicate rules, null values, and include/exclude overlap are not defined.

> [!warning] Aggregation example conflict
> The example uses `aggregation_key: bytes`, but its property filters are named `cpu_hours`, `region`, and `machine_type`, contradicting the schema statement that the aggregation key must be one of the property-filter names. Treat the example as illustrative rather than a validated configuration.

> [!warning] UNIQUE documentation conflict
> This list schema includes `UNIQUE`, while the separate billable-metric guide describes streaming metrics with COUNT, SUM, MAX, and LATEST and directs distinct counts to SQL. This endpoint does not define UNIQUE or reconcile that boundary, so it does not independently establish a streaming distinct-count contract.

The schema does not mark an aggregation, filter set, group-key set, or SQL query as required and provides no standard-versus-SQL discriminator. A missing optional field should therefore not be treated as proof of a metric type or configuration default.

## Operational unknowns

Only HTTP `200` is documented. The page gives no operation-specific error envelope, authorization scope, rate limit, cache behavior, timeout, retry guidance, consistency guarantee, or audit-history field. Because this operation is GET rather than POST, API-wide POST idempotency guarantees are not applicable. Listing a metric also does not associate it with a product, prove that it currently receives matching events, establish that it contributes to an invoice, or itself determine orphan status.

## Related

- Company: [[metronome]]
- Concept: [[metronome-billable-metrics]]
- Related sources: [[source-metronome-api-reference-pagination]], [[source-metronome-api-reference-billable-metrics-create-a-billable-metric]], [[source-metronome-api-reference-billable-metrics-get-a-billable-metric]], [[source-metronome-api-reference-billable-metrics-get-billable-metrics-for-a-customer]], [[source-metronome-api-reference-authentication]], [[source-metronome-api-reference-status-codes]]

## Raw Sources

- [[raw/metronome/api-reference/billable-metrics/list-all-billable-metrics-2026-07-13|2026-07-13 snapshot - account-wide billable-metric listing, pagination, archive filter, and returned configuration schema]]
