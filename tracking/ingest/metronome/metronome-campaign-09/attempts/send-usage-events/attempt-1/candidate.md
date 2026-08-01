---
title: "Metronome Send Usage Events (Events Guide)"
type: source
date_ingested: 2026-08-01
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/events/send-usage-events"
raw_files:
  - "metronome/guides/events/send-usage-events-2026-07-13.md"
tags: [metronome, usage-events, event-ingestion, idempotency, retries, billable-metrics]
---

## Overview

This guide defines the event fields and producer-side operating practices for sending usage data to Metronome through `/ingest` or a Segment connection. Its direct-API guidance combines event-level transaction IDs with a reliable queue, status-specific retries, dead-letter handling, audit logging, resilience tests, deterministic heartbeat IDs, and asynchronous customer provisioning.

## Key takeaways

- A usage event has four required fields—`transaction_id`, `customer_id`, `timestamp`, and `event_type`—plus an optional `properties` object. The page labels all four required values as strings.
- Once Metronome accepts an event, later events with the same `transaction_id` during the next 34 days are ignored as duplicates. The page does not define the exact boundary or the response for a duplicate.
- `customer_id` can be a Metronome customer ID or one of that customer's ingest aliases. `timestamp` must be a four-digit-year RFC 3339 string, drives time-range selection for usage queries and invoices, and is rejected when it is more than 24 hours in the future.
- The guide recommends representing every `properties` key and value as a string to avoid floating-point precision loss; it says Metronome uses arbitrary-precision decimals internally. This recommendation is not a complete endpoint-schema definition.
- For direct `/ingest` delivery, use a reliable queue. Retry network and `5xx` failures until `200`, use increasing exponential delays for repeated `429` responses, and send other `4xx` payload failures to a dead-letter queue instead of automatically retrying them.

## Event fields and identity boundaries

`transaction_id` is the event's duplicate-suppression identity. The documented guarantee is acceptance-relative: after one event is accepted, subsequent uses of that ID within the next 34 days are ignored. The source does not say whether the window is inclusive at exactly 34 days, whether it is measured from first acceptance or later duplicate attempts, how a different payload using the same ID is handled, whether an ID can be safely reused after the window, or how duplicates are represented in the HTTP response.

`customer_id` attributes billable usage to a customer and can carry either the Metronome customer identifier or an ingest alias such as an application account number. One customer can have multiple aliases. The page does not define alias format, uniqueness across customers, reassignment, removal, conflict responses, or the behavior of an event whose alias has not yet been attached.

`timestamp` is the occurrence time used to select events for usage queries and invoice production. This guide rejects timestamps more than 24 hours in the future but does not specify the permitted historical age, precision, timezone-offset normalization, leap-second behavior, or whether exactly 24 hours ahead is accepted.

`event_type` and `properties` describe the event for downstream metrics. The guide permits application-defined event types and recommends string representation for all property keys and values. It does not define property-count, key-length, value-length, nesting, null, boolean, array, or top-level additional-field behavior. Its email example says one property can be aggregated by default, while a derived expression such as `num_recipients * size` requires a SQL-based billable metric.

## Queue, retry, and failure handling

For direct API delivery, the guide recommends a reliable queue such as Amazon SQS or RabbitMQ with a worker that forwards queued events to Metronome. Queue choice, delivery semantics, visibility timeouts, ordering, concurrency, retention, poison-message policy, and worker acknowledgement timing remain implementation-owned and undocumented here.

A network error or `5xx` response can leave a batch partially ingested, so the guide says to retry the call until a `200` is received. Retry safety depends on preserving each event's original `transaction_id`; it must not be generalized to new IDs, non-ingest writes, or permanent uniqueness beyond the stated 34-day duplicate window. The source does not define batch size, partial-result visibility, a retry deadline, maximum attempts, client timeout, or how to reconcile a response lost after server acceptance.

For `429`, back off and retry after a delay, increasing the delay exponentially if rate limiting continues. The guide does not define a starting delay, multiplier, cap, jitter, retry header, rate-limit scope, or terminal condition. For every other `4xx`, it says not to auto-retry: isolate the event in a dead-letter queue, alarm, investigate the payload, and resolve the defect. It does not specify whether a mixed batch must be split before reprocessing or how a corrected event should preserve or replace its transaction ID.

Enable message-queue logging during initial integration and whenever the event structure changes so sent events can be audited. Metronome can configure a trial API failure rate in Sandbox or Production; the page recommends 20% and requires coordinating the rate and test window with a representative. It does not state which status or network failures are injected, whether acceptance can precede an injected failure, or whether the test affects Segment delivery.

## Heartbeats, schema changes, and critical paths

For a per-node, per-minute heartbeat, the guide proposes `<node id>_<floor(unix_now()/60)>` so duplicate sends for the same node and minute share an ID. It recommends two or more heartbeats per measurement period: duplicate suppression prevents double counting while redundant sends reduce the chance that timer imprecision or delay leaves a gap. The page does not define clock-skew tolerance, node-ID escaping or collision resistance, measurement-period alignment, late-arrival behavior, or aggregation across nodes.

> [!warning] Idempotency wording tension
> The heartbeat section says Metronome guarantees that only one event with a given `transaction_id` is processed, while the same page specifically bounds later duplicate suppression to the next 34 days after acceptance. Treat the heartbeat statement as applying to duplicate sends within the documented window, not as proof of permanent global uniqueness.

Changing an event's structure can stop the specific billable metrics it targets from recording usage, so the guide recommends representative-assisted validation and testing for schema changes. Because ingest aliases can match events sent before or after Metronome customer creation, it also recommends keeping Metronome off the critical customer-creation path: create the application customer first and create the matching Metronome record asynchronously. The page does not define the retention or eventual-attribution guarantees needed to turn that recommendation into a complete provisioning design.

## Documentation overlap and unknowns

This canonical route substantially overlaps the already ingested `implement-metronome/core-concepts/send-usage-events` guide. The route and raw snapshot are distinct evidence, but they do not establish two ingestion products or two retry protocols. No contradiction with the current Metronome wiki was found; the current concepts already preserve the 34-day boundary, string-property recommendation, partial-failure retry behavior, heartbeat pattern, and asynchronous provisioning guidance.

Beyond the boundaries above, this page does not document authentication, request-array or response schemas, maximum events or bytes per call, endpoint throughput, numeric rate limits, historical timestamp limits, ordering, atomicity, Segment retry or idempotency behavior, data retention, event-search consistency, metric-match results, or invoice recalculation timing. Use the dedicated API and high-volume sources for those concerns.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-event-ingestion]], [[metronome-api-idempotency]], [[metronome-billable-metrics]], [[metronome-customers-and-contracts]]
- Related sources: [[source-metronome-guides-implement-metronome-core-concepts-send-usage-events]], [[source-metronome-api-reference-usage-ingest-events]], [[source-metronome-api-reference-idempotency]], [[source-metronome-guides-events-design-usage-events]], [[source-metronome-guides-events-high-volume-ingestion]]

## Raw Sources

- [[raw/metronome/guides/events/send-usage-events-2026-07-13|2026-07-13 snapshot — event fields, queueing, retry boundaries, heartbeat idempotency, and asynchronous provisioning]]
