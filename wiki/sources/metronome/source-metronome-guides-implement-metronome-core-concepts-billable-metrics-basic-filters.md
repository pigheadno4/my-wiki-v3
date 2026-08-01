---
title: "Metronome Create Streaming Billable Metrics"
type: source
date_ingested: 2026-08-01
canonical_url: "https://docs.metronome.com/guides/implement-metronome/core-concepts/billable-metrics-basic-filters"
original_format: webpage
raw_files:
  - "metronome/guides/implement-metronome/core-concepts/billable-metrics-basic-filters-2026-07-13.md"
tags: [metronome, billable-metrics, streaming-metrics, filters, aggregation]
---

## Overview

This guide shows how to create a streaming billable metric with Metronome's Basic Filters editor or an equivalent API request. Its worked example matches successful `api_request` events, requires a `user_id`, counts the matched calls, and groups the result by user.

## Key takeaways

- Every metric defined with the Basic Filters editor is a streaming billable metric; the editor supplies structured filters and aggregations over the usage stream.
- In the worked `API Calls` metric, the event type is `api_request`, `status` must be in `success`, and `user_id` must exist. Metronome uses `user_id` as a group key, so the count is broken out by user.
- Streaming billable metrics support `COUNT`, `SUM`, `MAX`, and `LATEST`. The example selects `COUNT`; the guide directs `UNIQUE` aggregation to a SQL billable metric.
- The equivalent create request represents the event match as `event_type_filter.in_values`, represents both property conditions under `property_filters`, sets `aggregation_type` to `COUNT`, and uses the compound-array form `group_keys: [ ["user_id"] ]`.

## Matching, filtering, and grouping

The UI flow selects `api_request` as the event type. It applies an `In` filter that admits `status: success` and an `Exists` filter for `user_id`. The latter property is also configured as a group key. For this example, the resulting metric counts successful API calls and breaks that count out by `user_id`.

The equivalent API payload makes the `status` condition explicit as both `exists: true` and `in_values: ["success"]`; it represents `user_id` with `exists: true`. The page demonstrates these conditions together but does not define general boolean composition across several property filters, include/exclude precedence, case sensitivity, type coercion, or behavior for malformed property values. It also does not explain whether the UI adds `exists: true` automatically when an `In` filter is selected.

## Aggregation and streaming boundaries

The example uses `COUNT` to count calls rather than sum or average a property. The guide lists four streaming aggregation types: `COUNT`, `SUM`, `MAX`, and `LATEST`; it sends `UNIQUE` to the SQL metric path. It does not define the aggregation key requirements or value handling for `SUM`, `MAX`, and `LATEST`, nor the ordering rule for `LATEST`.

> [!warning] Aggregation contract mismatch
> This guide presents `COUNT`, `SUM`, `MAX`, and `LATEST` as the streaming set and directs `UNIQUE` to a SQL billable metric. The create and retrieval API references also enumerate `UNIQUE` in `aggregation_type` without defining its semantics or reconciling whether it is a supported streaming operation. Treat streaming `UNIQUE` support as unresolved.

All Basic Filters metrics are identified as streaming, but this page does not specify ingestion-to-aggregation latency, throughput, event ordering, duplicate handling, billing-period windows, late-event behavior, historical backfill or reflow, metric editability, or when a saved metric begins matching events. The API sample documents the create payload only; it does not show the response, errors, idempotency, authentication scope, or persistence guarantees.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-billable-metrics]], [[metronome-event-ingestion]], [[metronome-usage-based-billing]]
- Related sources: [[source-metronome-guides-implement-metronome-core-concepts-create-billable-metrics]], [[source-metronome-api-reference-billable-metrics-create-a-billable-metric]], [[source-metronome-api-reference-billable-metrics-get-a-billable-metric]]

## Raw Sources

- [[raw/metronome/guides/implement-metronome/core-concepts/billable-metrics-basic-filters-2026-07-13|2026-07-13 snapshot — Basic Filters setup, event matching, aggregation, grouping, and equivalent API payload]]
