---
title: "Metronome Get a Billable Metric API"
type: source
date_ingested: 2026-07-30
canonical_url: "https://docs.metronome.com/api-reference/billable-metrics/get-a-billable-metric"
original_format: webpage
raw_files:
  - "metronome/api-reference/billable-metrics/get-a-billable-metric-2026-07-13.md"
tags: [metronome, api, billable-metrics, metering, sql-metrics]
---

## Overview

This API reference documents bearer-authenticated `GET /v1/billable-metrics/{billable_metric_id}` for retrieving one billable metric's configuration by UUID. A successful response wraps the metric under `data` and can describe event matching, aggregation, grouping, custom fields, an associated SQL query, and archive state. The endpoint reads configuration; it does not create, edit, restore, or associate the metric with a product.

## Key takeaways

- The only request input is the required `billable_metric_id` path parameter, represented as a UUID. The page documents HTTP `200` success and `404` not found.
- A successful response requires `data`; the referenced metric object requires only `id` and `name`, while its filters, aggregation, group keys, custom fields, SQL, and archive timestamp are optional in this schema.
- Event-type include and exclude lists narrow matching. Every supplied property-filter rule must pass, and a property filter can test existence, allowed values, or excluded values.
- The aggregation enum lists lower-, title-, and uppercase spellings of `COUNT`, `LATEST`, `MAX`, `SUM`, and `UNIQUE`. An aggregation key names an event property, must also be a property-filter name, and does not apply to count.
- Group keys are nested arrays of property names whose entries slice matched events into distinct invoice-usage-cost buckets. Custom fields are a string-valued map.
- SQL is exposed only as an optional query string. This response schema supplies no standard-versus-SQL discriminator and does not define the SQL dialect, required output columns, validation, limits, or redaction behavior.
- An archived metric carries an RFC 3339 `archived_at` timestamp, stops processing new usage events, and remains retrievable for historical reference; omission of the field means the metric is not archived.

## Endpoint and request

The production server is `https://api.metronome.com`, the operation ID is `getBillableMetric-v1`, and the document-level security requirement uses HTTP bearer authentication. The route is `GET /v1/billable-metrics/{billable_metric_id}`. Its sole operation parameter is the required path string `billable_metric_id`, formatted as a UUID. This page defines no query parameters or request body.

HTTP `200` returns an object with required `data`, which references `BillableMetricV1`. HTTP `404` uses the shared not-found response whose JSON body is an `Error` object requiring a string `message`. The operation does not document `400`, `401`, `403`, `429`, or `5xx` behavior, error codes beyond the message, cache semantics, consistency after a configuration change, or retry guidance.

## Returned metric configuration

The metric object requires only two fields: UUID `id` and display-name string `name`. The following fields are optional in the response schema:

| Field | Documented meaning and boundary |
| --- | --- |
| `event_type_filter` | Optional event-type matching rule with `in_values` and `not_in_values`. Each list must be non-empty when present. The page does not define precedence when the same value is included and excluded. |
| `property_filters` | Array of property rules; all rules must pass. Each rule requires `name` and may specify `exists`, `in_values`, or `not_in_values`. |
| `aggregation_type` | One of the listed spelling variants of COUNT, LATEST, MAX, SUM, or UNIQUE. General case-insensitive parsing and UNIQUE semantics are not established. |
| `aggregation_key` | Event-property name used for aggregation; it must be one of the property-filter names and is inapplicable to count. The retrieval schema does not say which non-count variants require it. |
| `group_keys` | Array of arrays of property names. Each outer entry is a set of properties used to slice events into distinct invoice-cost buckets. |
| `custom_fields` | Object with arbitrary property names and string values. No key, value, entry-count, or visibility limits are stated. |
| `sql` | SQL query associated with the metric. This page does not define a SQL response contract or say whether other configuration fields can coexist in a retrieved object. |
| `archived_at` | RFC 3339 archive timestamp. If absent, the metric is not archived. |

The example returns a metric named `CPU Hours` that includes `cpu_usage` events, requires `cpu_hours`, `region`, and `machine_type`, restricts region to `EU` or `NA`, restricts machine type to `slow` or `fast`, sums `cpu_hours`, and exposes separate group-key entries for region and machine type. It is an example, not a statement that these fields or values are universal defaults.

## Matching semantics

`event_type_filter.in_values` admits only listed event types; `not_in_values` rejects listed event types. Both arrays are described as non-empty when present. The schema does not explain behavior when both arrays are supplied, overlap, contain duplicates, or differ only by case.

Each property filter requires an event-property `name`, and all property-filter objects must pass for the event to match the metric. `exists: true` requires the property, `exists: false` requires its absence, and null or omission leaves existence optional. `in_values` admits only listed property values and must be non-empty when present. `not_in_values` rejects listed values, but its description both allows null or an empty list to pass all values and says the array must be non-empty when present.

The page does not define string coercion, null-value handling, duplicate property-filter names, include/exclude precedence, or the interaction between `exists: false` and value lists. It also does not expose a match-test result through this GET operation.

## Aggregation, grouping, and SQL boundaries

The aggregation enum explicitly contains three capitalization variants for each named aggregation. That enumeration should not be generalized to arbitrary capitalization. It also includes `UNIQUE`, while the separate billable-metric guide directs distinct counts to SQL and describes streaming metrics with only COUNT, SUM, MAX, and LATEST.

> [!warning] UNIQUE documentation conflict
> This retrieval schema repeats the create endpoint's undocumented `UNIQUE` enum value, but the billable-metric guide treats distinct counting as a SQL use case. This page supplies neither UNIQUE semantics nor a reconciliation, so clients should not infer that UNIQUE is a supported streaming distinct-count contract without confirmation.

`aggregation_key` identifies the event property to aggregate, must name one of the metric's property filters, and is not applicable when aggregation type is count. The response schema does not mark it required or define behavior for a non-count metric whose key is absent.

Each `group_keys` entry is itself an array, allowing a group to be composed from multiple properties. The schema says groups slice events into distinct invoice-usage-cost buckets, but does not define non-empty constraints, maximum nesting sizes, duplicate or ordering behavior, whether group-key properties must appear in the returned property filters, or cardinality limits.

The optional `sql` field is only described as the query associated with the metric. Unlike the create endpoint's request contract, this GET response schema does not state mutual exclusivity between SQL and standard filter, aggregation, or grouping fields and does not include a metric-type discriminator. Missing fields therefore should not be interpreted as proof of a particular metric type without additional authority.

## Archive and operational boundaries

The narrative says archived metrics no longer process new usage events but remain accessible for historical reference, and the response uses `archived_at` to identify them. This page does not define archival propagation timing, whether already accepted events continue processing, how archive state affects products or historical invoice calculations, restoration support, data retention, or authorization differences for archived metrics.

More generally, the reference provides no update semantics, field mutability rules, response freshness guarantee, rate limit, pagination, expansion controls, version field, audit history, or permissions beyond bearer authentication. It describes retrieving configuration before product association but does not validate product compatibility or perform the association.

## Related

- Company: [[metronome]]
- Concept: [[metronome-billable-metrics]]
- Related sources: [[source-metronome-api-reference-billable-metrics-create-a-billable-metric]], [[source-metronome-guides-implement-metronome-core-concepts-create-billable-metrics]], [[source-metronome-api-reference-authentication]], [[source-metronome-api-reference-status-codes]]

## Raw Sources

- [[raw/metronome/api-reference/billable-metrics/get-a-billable-metric-2026-07-13|2026-07-13 snapshot — get-billable-metric endpoint, response schema, and archive behavior]]
