---
title: "Metronome API: Get Usage Data with Paginated Groupings"
type: source
date_ingested: 2026-08-31
canonical_url: "https://docs.metronome.com/api-reference/usage/get-usage-data-with-paginated-groupings"
original_format: webpage
raw_files:
  - "metronome/api-reference/usage/get-usage-data-with-paginated-groupings-2026-07-13.md"
tags: [metronome, api, usage, billable-metrics, grouping, pagination]
---

## Overview

Bearer-authenticated `POST /v1/usage/groups` retrieves aggregated usage for one customer and billable metric, divided into requested time windows and simple or compound metric dimensions. It is a usage-analysis read for dimensional exploration and merchant-built dashboards; it does not return prices, costs, invoice state, or a durable dashboard resource.

## Query-critical facts

- Within a supplied JSON payload, UUID `customer_id`, UUID `billable_metric_id`, and `window_size` are required. The enclosing OpenAPI `requestBody` is not marked required, so omitted-body behavior is not established.
- `window_size` accepts documented case variants of `hour`, `day`, and `none`: hour or day segments the requested period, while none produces one aggregate for the full period. Optional `starting_on` and exclusive-style `ending_before` date-time fields select the period. Alternatively, `current_period: true` requests the current billing period and errors when the customer is uncontracted or either explicit bound is also supplied.
- `group_key` is an array supporting one or multiple dimensions. For streaming metrics it must match a complete simple or compound group-key definition on the billable metric; partial compound combinations are unsupported, and `group_key` cannot be combined with deprecated single-key `group_by`.
- `group_filters` maps dimensions to accepted values. Every filter key must occur in `group_key`; omitting a dimension or giving it an empty array includes all values for that dimension.
- Optional query `limit` accepts 1 through 100 and query `next_page` supplies the continuation cursor. HTTP `200` requires a top-level `data` array plus nullable top-level `next_page`; complete traversal requires continuing until that sibling cursor is null.
- Each aggregate represents one `starting_on`/`ending_before` window, one grouped dimension map, and a nullable numeric usage `value`. Deprecated required-but-nullable `group_key` and `group_value` fields remain in the aggregate schema for single-key compatibility.

## Material boundaries

- The narrative calls the result an array of `PagedUsageAggregate` objects containing `next_page`, but the response schema and both examples place `next_page` once at the top level beside `data`. Clients should follow the schema/example envelope rather than look for a cursor on each aggregate.
- The prose says group values can be null when events lack the group property, while the `group` map schema permits string values and does not mark them nullable; `group` is also omitted from the aggregate required array. Preserve this documentation conflict instead of assuming a closed parser contract.
- For compound grouping, the prose states that the default and maximum limit are 100; the query schema encodes only a 1-to-100 range and no default. The page defines no result ordering, total count, cursor lifetime, stable pagination snapshot, duplicate-or-skip behavior across pages, retention, as-of selector, freshness SLA, or read-after-write visibility. A completed traversal is therefore not proof of an immutable or current usage population.
- This POST read is also covered by the separate API-wide [[source-metronome-api-reference-idempotency|idempotency authority]]: identical same-key parameters replay the original result. Replay is recovery of that result, not proof of a fresh usage calculation or a newly established pagination snapshot; this endpoint adds no read-specific cache, cursor/key interaction, retry, or ambiguous-failure contract.
- The endpoint supports dimensional usage analytics and dashboard inputs, but does not establish billable-metric configuration validity, pricing or invoice reconciliation, accounting completeness, dashboard refresh behavior, or authorization beyond bearer authentication.

## Raw detail coverage

The complete request and response schemas, casing variants, deprecated single-group fields, payload examples, compound-group examples, group-map and filter-map shapes, exact requiredness and nullability, query limits, cursor fields, security declaration, and OpenAPI component definitions remain in the full raw reference linked below.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-billable-metrics]], [[metronome-reporting-and-analytics]], [[metronome-usage-based-billing]], [[metronome-api-idempotency]]
- Related source: [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/usage/get-usage-data-with-paginated-groupings-2026-07-13|2026-07-13 snapshot - complete dimensional usage query, grouping, time-window, response, and pagination reference]]