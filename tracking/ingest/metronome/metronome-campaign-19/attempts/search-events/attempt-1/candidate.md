---
title: "Metronome API: Search Events"
type: source
date_ingested: 2026-08-21
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/usage/search-events.md"
raw_files:
  - "metronome/api-reference/usage/search-events-2026-07-13.md"
tags: [metronome, api, usage-events, observability, billable-metrics]
---

## Overview

This API reference documents `POST /v1/events/search`, a bearer-authenticated observability endpoint that retrieves recent usage events by transaction ID. Metronome positions it for sampling event-to-customer and event-to-billable-metric matching, duplicate diagnostics, and investigation of potential usage-pipeline revenue leakage. It is not an exhaustive event export or proof that billing is complete or revenue leakage has been prevented.

## Key takeaways

- Search is limited to events that occurred within the last 34 days and is keyed by supplied transaction IDs. The page does not define the exact cutoff clock or whether the boundary is inclusive.
- The endpoint is described as heavily rate limited and sampling-only. It provides no numeric limit and explicitly says not to check every event.
- A successful response can expose the event's required identity and timing fields plus optional properties, processing time, duplicate flag, matched customer, and matched billable metrics.
- The page frames sampled matching checks as a way to detect risks from dropped, delayed, reformatted, or misconfigured events, but it does not guarantee complete detection, prevention, invoice accuracy, or revenue recovery.
- The endpoint documents only HTTP `200`; it does not define error responses, missing-ID behavior, result ordering, pagination, snapshot consistency, or read-after-ingest timing.

## Request contract

The production endpoint is `POST /v1/events/search` under the OpenAPI document's global bearer scheme. Its JSON payload schema requires `transactionIds`, an array of strings, when a body is supplied. The OpenAPI `requestBody` object itself is not marked required, and the array has no documented minimum, maximum, uniqueness rule, or per-ID length or format constraint.

This source's 34-day rule is a search-eligibility boundary based on when an event occurred. It must not be silently treated as the same contract as the separately documented acceptance-relative ingest duplicate-suppression window or the historical-ingest backdating limit. The page does not specify behavior exactly at the search cutoff.

## Response and matching diagnostics

HTTP `200` returns a top-level array. Each event item requires `id`, `transaction_id`, `customer_id`, `event_type`, and RFC 3339 `timestamp`. Optional fields include an open `properties` object, RFC 3339 `processed_at`, boolean `is_duplicate`, a `matched_customer` object, and an array of `matched_billable_metrics`. The matched-customer description is conditional on a match being found.

Each matched-metric item inherits a schema that requires `id` and `name`. Optional current configuration includes `aggregation_type`, `group_keys`, `aggregation_key`, event-type and property filters, custom fields, SQL, and `archived_at`; the same response object retains deprecated `group_by`, `aggregate`, `aggregate_keys`, and `filter` fields. The search-specific aggregation enum includes case variants of count, latest, max, sum, and unique plus lowercase `custom_sql`. That enum does not establish case normalization or resolve the existing `UNIQUE`-versus-SQL-distinct guidance conflict.

The response's property-filter descriptions say all rules must pass and define existence, inclusion, and exclusion conditions. The `not_in_values` description says null or empty permits all values and also says the field must be non-empty if present. Preserve that internal ambiguity rather than inferring whether an explicitly empty array is valid. These returned fields describe diagnostic metric configuration; they do not mutate a metric.

The introductory prose calls out processing status, but the response schema defines no explicit `status` property; it exposes optional `processed_at` and `is_duplicate` fields instead. It also describes complete event details while the schema does not require `properties`, either match field, or either processing/duplicate field. Do not infer presence beyond the schema.

The response can help diagnose whether sampled events are attributed to a customer and active billable metrics. The page does not define whether matching reflects ingest-time configuration, search-time configuration, or another snapshot; whether an empty or absent metric list distinguishes no match from unavailable diagnostics; how duplicates are selected or related to an accepted original; or whether `is_duplicate` uses the same timing semantics as ingest duplicate suppression.

## Sampling and revenue-leakage boundary

Metronome recommends random sampling rather than per-event checks and cites upstream failures, event-format changes, and misconfigured metrics as possible sources of silent revenue loss. The endpoint can support merchant-built leakage alerts and investigations, but the page supplies no sampling method, coverage target, false-negative rate, alert contract, response-latency guarantee, or remediation workflow. The phrases "validates the integrity", "prevent silent revenue loss", and "in real-time" are product positioning and intended use, not service guarantees.

A stored sampled event with expected matches is evidence about that returned event only. It does not prove that all producer events arrived, every intended customer or metric matched, quantities were rated correctly, invoices included the results, downstream billing succeeded, or revenue was fully captured.

## API boundaries and unknowns

The operation lists no `400`, `401`, `403`, `404`, `409`, `429`, or `5xx` response contract even though it is bearer secured and described as heavily rate limited. The page does not define how absent, expired, malformed, or duplicate requested IDs are represented; whether one result is returned per input ID; whether extra events can appear; result ordering; pagination or truncation; maximum response size; partial results; timeouts; caching; consistency across repeated calls; rate-limit headers; retry guidance; or authorization scope beyond the global bearer scheme.

No contradiction was found with the existing high-volume-ingestion, billable-metric testing, or production-readiness summaries when this endpoint is treated as a bounded sampling diagnostic rather than a completeness or revenue guarantee.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-event-ingestion]], [[metronome-billable-metrics]]
- Related sources: [[source-metronome-guides-events-high-volume-ingestion]], [[source-metronome-guides-implement-metronome-core-concepts-create-billable-metrics]], [[source-metronome-guides-implement-metronome-production-checklist]], [[source-metronome-api-reference-usage-ingest-events]]

## Raw Sources

- [[raw/metronome/api-reference/usage/search-events-2026-07-13|2026-07-13 snapshot — transaction-ID event search, matching diagnostics, response schema, and sampling boundary]]
