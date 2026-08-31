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

Bearer-authenticated `POST /v1/usage/groups` retrieves aggregated usage for one customer and billable metric, divided into requested time windows and simple or compound metric dimensions. It is a post-metric usage-analysis read for dimensional exploration and merchant-built dashboards; it does not return raw submitted events, prices, costs, invoice state, or a durable dashboard resource.

## Query-critical facts

- Within a supplied JSON payload, UUID `customer_id`, UUID `billable_metric_id`, and `window_size` are required. The enclosing OpenAPI `requestBody` is not marked required, so omitted-body behavior is not established.
- `window_size` accepts documented case variants of `hour`, `day`, and `none`. Hour and day segment the selected period into hourly or daily windows; none uses one full-period time window, without establishing that grouping yields only one response row. Optional `starting_on` and `ending_before` date-time fields select the period. Alternatively, `current_period: true` requests the current billing period and returns an error when the customer is uncontracted or when `starting_on` and `ending_before` are specified together. The examples cover day windows only, not a `none` response or `current_period` request.
- `group_key` is an array supporting one or multiple dimensions. For streaming metrics it must match a complete simple or compound group-key definition on the billable metric; partial compound combinations are unsupported, and `group_key` cannot be combined with deprecated single-key `group_by`.
- `group_filters` maps dimensions to accepted values. Every filter key must occur in `group_key`; omitting a dimension or giving it an empty array includes all values for that dimension.
- Optional query `limit` accepts 1 through 100 and query `next_page` supplies the continuation cursor. HTTP `200` requires a top-level `data` array plus nullable top-level `next_page`; the separate [[source-metronome-api-reference-pagination|pagination authority]] says complete traversal repeats with the returned cursor until `next_page` is null.
- Each aggregate represents one `starting_on`/`ending_before` window, one grouped dimension map, and a nullable numeric usage `value`. Deprecated required-but-nullable `group_key` and `group_value` fields remain in the aggregate schema for single-key compatibility.

## Material boundaries

- The narrative calls the result an array of `PagedUsageAggregate` objects containing `next_page`, but the response schema and both examples place `next_page` once at the top level beside `data`. Clients should follow the schema/example envelope rather than look for a cursor on each aggregate.
- The prose says group values can be null when events lack the group property, while the `group` map schema permits string values and does not mark them nullable; `group` is also omitted from the aggregate required array. Preserve this documentation conflict instead of assuming a closed parser contract.
- For compound grouping, the prose states that the default and maximum limit are 100; the endpoint query schema encodes only a 1-to-100 range and no default. The separate pagination authority supplies general traversal guidance but does not create an endpoint default.
- The current [[source-metronome-guides-implement-metronome-core-concepts-non-monotonically-increasing-metrics|non-monotonically increasing metric authority]] qualifies this endpoint for `LATEST` metrics only: usage reads return the absolute latest reported value within each requested window, whereas invoice breakdowns return incremental quantity and associated cost for each window. This distinction does not define other aggregation types or establish pricing, invoice equality, freshness, or accounting completeness; endpoint request and response shape remains with this API reference, while metric calculation remains with the guide.
- Under the separate API-wide [[source-metronome-api-reference-idempotency|idempotency authority]], identical parameters under a provided same `Idempotency-Key` replay the original result. Advancing query `next_page` changes parameters, so using that same key returns HTTP `409 Conflict`. Replay is not a fresh usage calculation or a stable pagination snapshot, and this endpoint adds no cursor lifetime, cross-page snapshot, no-key or different-key policy, read-after-write timing, endpoint-specific recovery, ordering, total count, duplicate-or-skip, retention, as-of, or freshness guarantee.
- The endpoint reads aggregated event data after customer and billable-metric matching. It does not establish raw-event acceptance, transaction-ID deduplication, matching success, ingest recovery, pricing, invoice reconciliation, accounting completeness, dashboard refresh behavior, or authorization beyond bearer authentication.

## Raw-detail coverage map

| Raw detail category | Exact raw coverage |
| --- | --- |
| Operation and request identity | Production server, bearer security, `POST /v1/usage/groups`, operation ID, query parameters, unmarked request-body requiredness, and payload-required customer, metric, and window properties |
| Time-window selection and examples | Hour, day, and none casing variants; hourly/daily segmentation; one full-period window for none without response-row cardinality inference; explicit date-time bounds; exact `current_period` error wording for an uncontracted customer or jointly specified bounds; and day-only request/response examples with no none-window response example |
| Grouping and filtering | Deprecated single-key `group_by`; simple and complete compound `group_key`; streaming-metric key identity; partial-compound exclusion; filter-map shape; member-key requirement; omitted and empty-filter behavior; and simple/compound examples |
| Results and documentation conflicts | Aggregate required fields, nullable value, deprecated nullable single-key fields, optional group map, narrative-versus-schema group nullability, and narrative-versus-schema cursor placement |
| Pagination and replay boundaries | Endpoint query `limit` range and `next_page`, required nullable response cursor, compound-only narrative default wording, repeat-until-null route to the pagination authority, API-wide same-key replay and changed-parameter conflict route, and endpoint-local ordering, snapshot, freshness, and recovery unknowns |
| Cross-surface calculation and ingest boundaries | `LATEST` absolute usage-window values versus incremental invoice-breakdown quantity and cost in the dedicated metric guide, plus aggregated post-metric reads versus raw-event submission, deduplication, matching, and recovery in dedicated ingestion authorities |

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-billable-metrics]], [[metronome-reporting-and-analytics]], [[metronome-usage-based-billing]], [[metronome-event-ingestion]], [[metronome-api-idempotency]]
- Related sources: [[source-metronome-api-reference-idempotency]], [[source-metronome-api-reference-pagination]], [[source-metronome-guides-implement-metronome-core-concepts-non-monotonically-increasing-metrics]]

## Raw Sources

- [[raw/metronome/api-reference/usage/get-usage-data-with-paginated-groupings-2026-07-13|2026-07-13 snapshot - complete dimensional usage query, grouping, time-window, response, and pagination reference]]
