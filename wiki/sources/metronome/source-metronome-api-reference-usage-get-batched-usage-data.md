---
title: "Metronome API: Get Batched Usage Data"
type: source
date_ingested: 2026-09-01
canonical_url: "https://docs.metronome.com/api-reference/usage/get-batched-usage-data"
original_format: webpage
raw_files:
  - "metronome/api-reference/usage/get-batched-usage-data-2026-07-13.md"
tags: [metronome, api, usage, billable-metrics, analytics, pagination]
---

## Overview

Bearer-authenticated `POST /v1/usage` retrieves aggregated usage across multiple customers and billable metrics in one query, divided into requested hourly, daily, or full-period windows. It is a post-metric analytics and reporting read; it does not return raw submitted events, prices, costs, invoice state, or an accounting-complete billing population.

## Query-critical facts

- Within a supplied JSON payload, `window_size`, `starting_on`, and `ending_before` are required. The enclosing OpenAPI `requestBody` is not marked required, so omitted-body behavior is not established. The payload schema does not declare `additionalProperties: false`, so unknown-field handling is also undocumented.
- `customer_ids` is an optional array of Metronome customer UUIDs; omitting it requests usage for all customers. `billable_metrics` is an optional array of metric selectors; omitting it requests all billable metrics, while every supplied selector requires UUID `id`. The page does not define empty-array behavior, identifier validation beyond UUID format, archived-resource visibility, or the semantics of mixing missing, inaccessible, or unrelated customer and metric IDs.
- A supplied metric selector may include `group_by`, whose supplied object requires `key`. Optional `values` has 1 through 200 nonempty strings; omitting `values` requests all available values, up to 200. The page does not define which 200 values are selected, their order, a continuation mechanism for excess group values, duplicate-value behavior, or whether omitted `group_by` returns ungrouped usage.
- `window_size` accepts documented lower-, title-, and uppercase variants of `hour`, `day`, and `none`. Hour and day segment the selected interval into hourly or daily aggregates. `none` uses the entire specified period as one time window, but the batched response can still distinguish customers, metrics, and grouped values; the raw provides no `none` response example resolving overall result-row cardinality. The page also does not define timezone alignment, partial-window behavior, maximum interval, retention, or late-event treatment.
- Optional query `next_page` indicates where the next result page begins. HTTP `200` requires a top-level `data` array and nullable sibling `next_page`; the separate [[source-metronome-api-reference-pagination|pagination authority]] supplies repeat-with-cursor-until-null traversal. Each immediate `data[]` aggregate requires customer and metric identity, start and end timestamps, and nullable numeric `value`; optional `groups` maps group values to nullable numbers, where null means no usage matched that group value.

## Material boundaries

- The narrative lists `next_page` as if it were contained by each `UsageBatchAggregate`, but the response schema and example place one nullable cursor at the top-level envelope beside `data`. Clients should follow the schema and example placement.
- The current [[source-metronome-guides-implement-metronome-core-concepts-non-monotonically-increasing-metrics|non-monotonically increasing metric authority]] qualifies usage-query values for `LATEST` metrics only: usage endpoints return the absolute latest reported value within each requested window, whereas invoice breakdowns return incremental quantity and associated cost for each window. This does not define other aggregation types or establish pricing, invoice equality, freshness, or accounting completeness. This API page remains authoritative for request and response shape; the guide is the metric-calculation authority.
- The current [[source-metronome-guides-customers-billing-optimize-customer-experience-customer-dashboards-and-reporting|customer-dashboard guide]] calls batched `/v1/usage` with singular customer and metric selectors, deprecated top-level `group_by`, and grouped item fields aligned with the distinct [[source-metronome-api-reference-usage-get-usage-data-with-paginated-groupings|`/v1/usage/groups` authority]]. Do not normalize that mixed worked example into either current contract. Use this dedicated API page for `/v1/usage` request nesting, required bounds and window, optional per-metric grouping, aggregate fields, and query-cursor placement.
- The endpoint has no query `limit`, documented ordering, total count, default page size, cursor lifetime, filter-binding rule, stable snapshot, duplicate-or-skip behavior, as-of selector, read-after-ingest timing, or freshness guarantee. Completing cursor traversal therefore does not prove an immutable or newly current usage population.
- Under the separate API-wide [[source-metronome-api-reference-idempotency|idempotency authority]], a provided-key result is persisted only after the request begins execution, meaning validation passed and no pre-execution concurrent-request conflict prevented execution. Only after that admission and persistence do identical same-key parameters replay the original result. Advancing query `next_page` changes parameters, so reusing that key returns HTTP `409 Conflict`; validation failures and pre-execution concurrency conflicts are not established cached results. Replay is not a fresh usage calculation or a stable pagination snapshot. This endpoint adds no requirement to send the header, no preferred key policy for later pages, and no endpoint-specific retry, recovery, concurrency, cursor-replay, or freshness guarantee.
- This page is authoritative for batched aggregate request and response shape, not raw-event acceptance, transaction-ID deduplication, customer or metric matching success, metric-definition correctness, pricing, invoice reconciliation, capacity enforcement, financial reporting, or accounting completeness. Its dashboard, reporting, monitoring, and capacity-planning use cases do not elevate the result into billing or ledger authority.

## Raw-detail coverage map

| Raw detail category | Exact raw coverage |
| --- | --- |
| Operation and request identity | Production server, bearer security, `POST /v1/usage`, operation ID, query cursor reference, unmarked request-body requiredness, and supplied-payload required properties |
| Batch scope and selectors | Optional customer UUID array with all-customer omission behavior; optional metric-selector array with all-metric omission behavior; per-selector required UUID `id`; nested optional `group_by`; and unspecified empty-array, inaccessible-ID, and cross-scope behavior |
| Time-window contract | Required date-time bounds, hour/day/none casing variants, hourly and daily segmentation, one full-period window for `none` without overall response-row cardinality inference, no `none` response example, and the exact daily worked interval example |
| Group selection and result values | Required group key inside a supplied grouping object; optional 1-200 nonempty values; omitted-values all-available behavior capped at 200; aggregate identity and timestamps; nullable numeric value; optional arbitrary group-value map; and documented null meaning |
| Response placement and examples | Required top-level `data` plus nullable sibling `next_page`, two daily aggregate examples, narrative-versus-schema cursor-placement conflict, and the absence of grouped or `none` response examples |
| Pagination and replay boundaries | Query `next_page` without endpoint `limit`; repeat-until-null route to the separate pagination authority; API-wide execution-admission prerequisite; admitted identical-parameter replay; changed-cursor HTTP 409 boundary; uncached validation and pre-execution concurrency failures; and endpoint-local ordering, snapshot, freshness, and recovery unknowns |
| Cross-surface calculation and billing authority | For `LATEST` only, absolute latest usage value in each requested window versus incremental invoice-breakdown quantity and cost in the metric guide; other aggregation types, pricing, invoice equality, freshness, and accounting completeness remain unestablished |
| Cross-surface worked-example conflict | Dashboard guide's batched path combined with singular selectors, deprecated top-level grouping, and grouped-route item fields; this page's plural/nested request, required bounds and window, aggregate fields, optional groups, and query cursor remain the current `/v1/usage` shape |
| Event-ingestion boundary | Aggregated post-metric output versus raw-event acceptance, transaction-ID deduplication, customer and metric matching, ingest recovery, and read-after-ingest behavior in dedicated authorities |

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-billable-metrics]], [[metronome-reporting-and-analytics]], [[metronome-usage-based-billing]], [[metronome-event-ingestion]], [[metronome-api-idempotency]]
- Related sources: [[source-metronome-api-reference-idempotency]], [[source-metronome-api-reference-pagination]], [[source-metronome-api-reference-usage-get-usage-data-with-paginated-groupings]], [[source-metronome-guides-implement-metronome-core-concepts-non-monotonically-increasing-metrics]], [[source-metronome-guides-customers-billing-optimize-customer-experience-customer-dashboards-and-reporting]]

## Raw Sources

- [[raw/metronome/api-reference/usage/get-batched-usage-data-2026-07-13|2026-07-13 snapshot - complete batched usage query, time-window, grouping, aggregate, and pagination reference]]
