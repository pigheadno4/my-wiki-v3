---
title: "Metronome Ingest Events API"
type: source
date_ingested: 2026-07-29
canonical_url: "https://docs.metronome.com/api-reference/usage/ingest-events"
original_format: webpage
raw_files:
  - "metronome/api-reference/usage/ingest-events-2026-07-13.md"
tags: [metronome, usage-events, event-ingestion, api-reference]
---

## Overview

This API reference documents Metronome's bearer-authenticated `POST https://api.metronome.com/v1/ingest` endpoint for sending usage events that feed customer matching, billable metrics, credit drawdown, spend calculations, and invoicing. The request schema accepts a JSON array of one to 100 events, while the narrative describes real-time processing, a 34-day historical-ingest and deduplication window, and support for 100,000 events per second without pre-aggregation.

## Key takeaways

- The endpoint uses HTTP bearer authentication and accepts `application/json` containing an array of one to 100 event objects.
- Every event requires nonempty `transaction_id`, `customer_id`, and `event_type` strings plus an RFC 3339 `timestamp`; `properties` is optional and permits arbitrary property names and values.
- `transaction_id` is the event-level idempotency key, is limited to 128 characters, and participates in a documented 34-day duplicate-detection window in which duplicates are ignored.
- `customer_id` may be either the Metronome customer UUID or an ingest alias from the producer's system. Event type and properties support billable-metric matching, grouping, pricing dimensions, cost breakdowns, and related calculations.
- Historical events may be backdated up to 34 days and immediately affect live customer spend. The page advertises support for 100,000 events per second and says capacity can scale beyond that figure, but it does not state an endpoint rate limit.

## Details

### Endpoint and authentication

The production server is `https://api.metronome.com`; the operation is `POST /v1/ingest`, uses the OpenAPI operation ID `ingest-v1`, and inherits the document's HTTP bearer security scheme. The request content type is `application/json`. The OpenAPI `requestBody` object does not itself declare `required: true`, so this page does not explicitly establish body omission behavior even though the operation is documented as ingesting an event array.

### Request and event schema

The JSON payload is an array with `minItems: 1` and `maxItems: 100`. Each event has four required fields:

- `transaction_id`: nonempty string, maximum 128 characters. Metronome describes it as the idempotency key and recommends UUIDs for one-time events, deterministic IDs for heartbeat events, and enough context to prevent collisions across event sources.
- `customer_id`: nonempty string. The prose permits either the UUID returned when a Metronome customer is created or an ingest alias such as an email or account number; a customer may have multiple aliases.
- `event_type`: nonempty string used for billable-metric matching. The page recommends descriptive names aligned with the product surface.
- `timestamp`: string described as RFC 3339 formatted. The prose permits historical timestamps up to 34 days in the past.

`properties` is optional and is defined as an object with `additionalProperties: true`. The page describes these values as flexible metadata for metric matching, group keys, pricing dimensions, customer-facing cost breakdowns, and internal cost-of-goods analysis. It does not specify limits for property count, nesting, keys, or values. The event object schema does not set `additionalProperties: false`; the page therefore does not document whether unrecognized top-level event fields are accepted, ignored, or rejected.

### Identity, deduplication, and processing

Metronome states that `transaction_id` ensures an event is processed exactly once and that duplicate events are automatically detected and ignored within a 34-day deduplication window. The page does not define whether the window is inclusive at exactly 34 days, how collisions with different payloads are handled, or what result identifies a duplicate to the caller.

The narrative says events are validated and processed in real time, matched to customers by customer ID or ingest alias, matched to billable metrics, and immediately available for usage and spend calculations. It does not define per-event versus whole-batch validation, partial acceptance, ordering, or retry behavior, so those runtime semantics should not be inferred from this reference.

### Response and documented limits

The OpenAPI response table documents only HTTP `200` with the description `Success`; it provides no response-body schema. No non-200 status codes, structured errors, duplicate indicators, per-event results, or validation-failure behavior are specified on this page.

The documented request limit is 100 events per batch. The narrative claims support for 100,000 events per second without pre-aggregation or rollups and says the system can scale upward, but does not state a default account limit, a rate-limit response, or how additional capacity is enabled. The separate high-volume guide states infrastructure capacity up to 110,000 events per second and a default account limit of 5,000; those claims describe different scopes and should not be collapsed into a single endpoint limit.

This page also does not define future-timestamp handling or the precise cutoff semantics for backdating and deduplication.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-event-ingestion]], [[metronome-billable-metrics]], [[metronome-usage-based-billing]]
- Related sources: [[source-metronome-api-reference-idempotency]], [[source-metronome-guides-events-high-volume-ingestion]], [[source-metronome-guides-events-design-usage-events]], [[source-metronome-guides-get-started-developer-sdks]]

## Raw Sources

- [[raw/metronome/api-reference/usage/ingest-events-2026-07-13|2026-07-13 snapshot — Ingest Events API endpoint and schema]]
