---
title: "Metronome Get Billable Metrics for a Customer API"
type: source
date_ingested: 2026-07-30
canonical_url: "https://docs.metronome.com/api-reference/billable-metrics/get-billable-metrics-for-a-customer"
original_format: webpage
raw_files:
  - "metronome/api-reference/billable-metrics/get-billable-metrics-for-a-customer-2026-07-13.md"
tags: [metronome, api, billable-metrics, customers, pagination]
---

## Overview

This API reference documents bearer-authenticated `GET /v1/customers/{customer_id}/billable-metrics`, which lists the billable metrics available for one customer and describes them as metrics tracked for that customer's billing calculations. The endpoint supports cursor pagination, an optional current-plan filter, and optional inclusion of archived metrics. Its response exposes both current billable-metric fields and four deprecated compatibility fields.

## Key takeaways

- `customer_id` is a required UUID path parameter. The page does not define what “available” means across multiple, future, expired, or amended customer contracts, or how a customer's “current plan” is selected.
- `limit` is optional and accepts `1` through `100`; `next_page` is an optional request cursor. Every successful response requires both the `data` array and a nullable `next_page` string.
- `on_current_plan=true` narrows the result to metrics on the customer's current plan, while `include_archived=true` includes archived metrics. Defaults, filter interaction, filter timing relative to pagination, and plan/archive edge cases are not specified.
- Every returned metric requires only UUID `id` and string `name`. Matching filters, aggregation, group keys, custom fields, SQL, archive time, and deprecated fields are optional in the item schema.
- The current metric configuration uses `aggregation_type`, singular `aggregation_key`, nested `group_keys`, `event_type_filter`, and `property_filters`. Deprecated `aggregate`, plural `aggregate_keys`, flat `group_by`, and unstructured `filter` may also appear.
- The response example is internally inconsistent: both example metrics use `aggregation_key: bytes` without a `bytes` property filter even though the field description requires that relationship, and the first metric's deprecated `group_by` values do not match its current `group_keys` values.

## Endpoint and customer scope

- Method and path: `GET /v1/customers/{customer_id}/billable-metrics`
- Production server: `https://api.metronome.com`
- Authentication: OpenAPI HTTP bearer security
- Operation ID: `listBillableMetrics-v1`
- Required input: path parameter `customer_id`, a UUID
- Optional inputs: `limit`, `next_page`, `on_current_plan`, and `include_archived`

The narrative says the operation returns metrics “available” for the specified customer and lets a caller see which metrics are tracked for that customer's billing calculations. It does not define whether availability comes from the customer's active contract, a plan or rate card, product associations, historical contracts, or another source. It also does not say how archived customers, customers without contracts, customer hierarchies, multiple concurrent contracts, or scheduled contract transitions affect the list.

The page documents no request body. It defines only an HTTP `200` response and does not document `400`, `401`, `403`, `404`, `429`, or `5xx` behavior. In particular, it does not say whether a missing, inaccessible, or archived customer produces an error or an empty `data` array.

## Pagination

`limit` is an optional integer with minimum `1` and maximum `100`; this endpoint does not declare a default or recommended page size. `next_page` is an optional string cursor identifying where the next result page should begin.

A successful response requires:

```json
{
  "data": [],
  "next_page": null
}
```

`data` is an array and has no documented minimum or maximum independent of `limit`. `next_page` is required but nullable. The page does not define result ordering, cursor lifetime, stability under concurrent metric or contract changes, cursor binding to the customer and filters, malformed or expired cursor errors, duplicate or skipped-item guarantees, or whether filter changes are permitted while continuing with a cursor. The separate API pagination reference supplies the general traversal convention; this endpoint schema remains the authority for its `1`–`100` limit.

## Current-plan and archive filters

`on_current_plan` is an optional boolean. When it is `true`, the list is filtered to metrics on the customer's current plan. The page does not define `false` or omitted behavior, the meaning of “plan” relative to contracts and rate cards, the effective-time used to choose a current plan, or behavior when several contracts or plan transitions apply.

`include_archived` is an optional boolean. When it is `true`, archived metrics are included. A returned metric's optional `archived_at` is an RFC 3339 timestamp; omission means the metric is not archived. The page does not explicitly state the default when `include_archived` is false or omitted, whether archive filtering occurs before pagination, or how `include_archived=true` combines with `on_current_plan=true`. It also does not define archive propagation, restoration, retention, historical-calculation behavior, or whether an archived metric can still be considered on a current plan.

The example response contains an item with `archived_at`, but no corresponding request query is shown. The example therefore does not establish that archived metrics are returned by default.

## Response schema

HTTP `200` returns an object whose `data` and `next_page` properties are both required. Each `data` item uses `BillableMetricWithDeprecatedFields`, an `allOf` composition over `BillableMetricBase` plus optional `aggregation_type`. Only `id` and `name` are required on the base object.

| Field | Schema and documented behavior |
| --- | --- |
| `id` | Required UUID identifying the billable metric. |
| `name` | Required string. No length, uniqueness, normalization, or character rules are documented. |
| `aggregation_type` | Optional enum containing lower-, title-, and uppercase spellings of `COUNT`, `LATEST`, `MAX`, `SUM`, and `UNIQUE`. The list does not establish arbitrary case-insensitive parsing, and `UNIQUE` semantics are not defined. |
| `aggregation_key` | Optional string naming the event property to aggregate. It must be one of the property-filter names and does not apply to count. The list schema does not say which non-count types require it. |
| `event_type_filter` | Optional include/exclude rule for the event type. Each supplied list must be non-empty. |
| `property_filters` | Optional array of property rules; all supplied rules must pass. Each rule requires `name` and may specify `exists`, `in_values`, and `not_in_values`. |
| `group_keys` | Optional array of string arrays. Each inner set names properties used to slice matched events into distinct invoice-usage-cost buckets. |
| `custom_fields` | Optional object with arbitrary keys and string values. No key, value, count, or visibility limits are stated. |
| `sql` | Optional string containing the associated SQL query. No SQL dialect, output contract, validation, complexity limit, or redaction behavior is documented. |
| `archived_at` | Optional RFC 3339 timestamp recording when the metric was archived; omission means it is not archived. |
| `group_by` | Deprecated flat array of strings; use `group_keys` instead. |
| `aggregate` | Deprecated string; use `aggregation_type` instead. |
| `aggregate_keys` | Deprecated array of strings; use singular `aggregation_key` instead. |
| `filter` | Deprecated free-form object with arbitrary properties; use `property_filters` and `event_type_filter` instead. |

No field identifies whether a returned metric is SQL-based or standard. The schema also does not state mutual exclusivity between `sql` and the standard filter, aggregation, and grouping fields, so coexistence or omission in a list response should not be treated as a reliable metric-type discriminator.

## Matching, aggregation, and grouping

`event_type_filter.in_values` admits only listed event types; `not_in_values` rejects listed event types. Both must be non-empty when present. The page does not define precedence when a value appears in both lists, behavior for an empty filter object, duplicate handling, or case sensitivity.

Every property-filter rule must pass. `exists: true` requires the property, `exists: false` requires it to be absent, and null or omission makes existence optional. `in_values` admits only listed values and must be non-empty when present. `not_in_values` rejects listed values, but its description both says null or empty lets all values pass and says the array must be non-empty when present. The page does not define string coercion, null event values, duplicate property-filter names, include/exclude precedence, or how value lists interact with `exists: false`.

The aggregation enum explicitly enumerates three capitalization variants for five names; it does not promise other capitalization. This list endpoint repeats the create endpoint's undocumented `UNIQUE` value, while the billable-metric guide describes streaming metrics as `COUNT`, `SUM`, `MAX`, and `LATEST` and directs distinct counts to SQL. The page does not reconcile those sources or define whether `UNIQUE` is a supported streaming distinct-count contract.

`group_keys` is nested rather than flat, permitting each outer entry to contain a set of property names. The page documents no non-empty constraint, maximum number or size of groups, duplicate or ordering behavior, property-filter prerequisite, or cardinality limit.

## Deprecated fields and example defects

The response type deliberately includes legacy and replacement fields, but it supplies no migration, equivalence, or precedence rules when both forms appear. In the first example item, `aggregate: sum` and `aggregation_type: SUM` differ only in case, while `aggregate_keys: [bytes]` and `aggregation_key: bytes` are structurally compatible. Its `group_by: [cluster, region]`, however, does not match `group_keys: [[region], [machine_type]]`. The page does not say which grouping representation a client should trust.

Both example metrics set `aggregation_key` to `bytes`, but their property filters are named `cpu_hours`, `region`, and `machine_type`. This violates the schema description requiring the aggregation key to be one of the property-filter names. The examples therefore should not be used as validated configuration payloads.

The deprecated `filter` is an arbitrary object, so this page does not define a deterministic conversion from it to separate event-type and property filters. Likewise, plural `aggregate_keys` may hold multiple strings while current `aggregation_key` is singular, and flat `group_by` cannot express the nested sets in `group_keys`; no lossy-conversion or fallback behavior is documented.

## Errors, consistency, and other unknowns

- No error envelope or status is documented for invalid UUIDs, nonexistent customers, inaccessible customers, invalid filters, malformed cursors, or authentication failure.
- No endpoint-specific rate limit, retry rule, timeout, cache policy, consistency guarantee, snapshot boundary, or response version is defined.
- It is unknown whether a page is a consistent snapshot when metrics, plans, contracts, or archive state change during traversal.
- Metric ordering and the interaction among `on_current_plan`, `include_archived`, and pagination are unspecified.
- The response does not explain why a metric is available to the customer, identify the plan/contract/product that supplies it, or expose an association effective period.
- The schema gives no current-versus-deprecated precedence, SQL-versus-standard discriminator, SQL contract, or complete aggregation semantics.
- The page documents no archive lifecycle beyond inclusion filtering and the `archived_at` timestamp.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-billable-metrics]], [[metronome-customers-and-contracts]]
- Related sources: [[source-metronome-api-reference-pagination]], [[source-metronome-api-reference-billable-metrics-create-a-billable-metric]], [[source-metronome-api-reference-authentication]], [[source-metronome-api-reference-status-codes]]

## Raw Sources

- [[raw/metronome/api-reference/billable-metrics/get-billable-metrics-for-a-customer-2026-07-13|2026-07-13 snapshot — customer-scoped billable-metric list endpoint, filters, pagination, response schema, and deprecated fields]]
