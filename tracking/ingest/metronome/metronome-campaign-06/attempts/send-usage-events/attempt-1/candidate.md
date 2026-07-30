---
title: "Metronome Send Usage Events"
type: source
date_ingested: 2026-07-30
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/implement-metronome/core-concepts/send-usage-events"
raw_files:
  - "metronome/guides/implement-metronome/core-concepts/send-usage-events-2026-07-13.md"
tags: [metronome, usage-events, event-ingestion, idempotency, retries, billable-metrics]
---

## Overview

This implementation guide defines the producer-side shape and operating practices for sending usage events to Metronome. Events can be sent through `/ingest` or a Metronome-to-Segment connection; the direct-API guidance focuses on a durable queue, status-specific retry handling, idempotent transaction IDs, and avoiding a dependency on Metronome in the customer-creation critical path.

## Key takeaways

- A usage event has four required string fields — `transaction_id`, `customer_id`, `timestamp`, and `event_type` — plus an optional `properties` map. `customer_id` can be a Metronome customer ID or any ingest alias assigned to that customer.
- Accepted duplicate `transaction_id` values are ignored for 34 days. For periodic heartbeats, use a deterministic ID such as `<node id>_<floor(unix_now()/60)>` and send two or more heartbeats per measurement period so delayed or imprecise timers do not leave a gap.
- `timestamp` must be RFC 3339 with a four-digit year; timestamps more than 24 hours ahead are rejected. This timestamp also bounds which events are selected for usage queries and invoice generation.
- Represent every `properties` key and value as a string. The guide ties that recommendation to avoiding floating-point precision loss and states that Metronome uses arbitrary-precision decimals internally.
- For direct `/ingest` delivery, use a reliable queue. Retry network and `5xx` failures until `200`; on `429`, back off and then use increasing exponential delays if rate limiting continues; do not auto-retry other `4xx` responses.

## Event contract and metric use

`transaction_id` is the required unique event identifier used for duplicate suppression. `customer_id` identifies the customer responsible for billing; an ingest alias can be an identifier from the producer system, such as an email address or account number, and one customer can have multiple aliases. `event_type` and `properties` supply the details that support billing. The guide illustrates `http_request` with `domain` and `bytes_sent`, and `cache_invalidation` with `number_of_files`.

The guide says a billable metric aggregates one property by default. Its email example uses `event_type: email_sent` with string-valued `num_recipients` and `size`, which can support recipient-count or maximum-size charging. A derived measure such as total data sent (`num_recipients` multiplied by `size`) requires SQL-based billable metrics.

## Direct-API delivery sequence

1. Put direct-API usage events on a reliable queue, then have a worker pull events and send them to Metronome. The source names Amazon SQS and RabbitMQ as examples.
2. If `/ingest` has a network error or returns `5xx`, treat the result as potentially partial: retry the failed call until `200`. Reusing each event's `transaction_id` makes those retries safe against duplicate processing.
3. If `/ingest` returns `429`, wait and retry; if rate limiting continues, increase the wait exponentially.
4. If `/ingest` returns any other `4xx`, do not retry automatically. Move the event to a dead-letter queue, trigger an alarm, investigate the payload, and resolve the issue.
5. Enable message-queue logging during the initial integration and whenever the event structure changes, so the exact sent events can be audited.

For resilience testing, Metronome can configure an automatic API failure rate for a chosen interval and environment; the guide recommends 20% and says to arrange the rate, enable/disable timing, and sandbox-versus-production scope with a Metronome representative.

## Heartbeats and change safety

The source distinguishes user-action events from periodic state-measurement heartbeats. A per-node, per-minute heartbeat can encode both node ID and minute bucket in its deterministic transaction ID, making duplicates from the same node and minute share an ID. Send two or more heartbeats per measurement period: duplicates are ignored and the extra sends reduce the risk of a missed measurement from timer imprecision or a temporary delay.

> [!warning] Event-schema changes
> Usage events target specific billable metrics. A data-structure change can stop downstream metrics from being recorded. The source advises working with a Metronome representative to validate and test any event-structure change before it causes disruption.

> [!warning] Property representation boundary
> This guide says all `properties` keys and values should be strings. The existing event-ingestion concept's broad statement that properties contain arbitrary data should be qualified on promotion; the separate ingest-endpoint reference needs to remain the authority for its OpenAPI schema rather than treating that broader wording as proof that numeric producer values are recommended here.

## Availability and documentation boundaries

Because ingest aliases can match events sent before or after Metronome customer creation, the guide recommends creating the customer in the producer's system first and creating the matching Metronome customer asynchronously. Teams should verify that Metronome is not a blocker on the customer-creation path.

This guide does not specify `/ingest` authentication, request-array shape or batch size, payload-size limits, rate-limit value, property-count or property-length limits, event-type naming constraints, Segment delivery/retry semantics, response bodies, duplicate indicators, ordering, partial-batch results, or whether exactly 24 hours in the future is accepted. It says accepted duplicates are ignored within the next 34 days, but does not define the exact boundary, collision behavior for different payloads sharing an ID, or the API response for a duplicate.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-event-ingestion]], [[metronome-api-idempotency]], [[metronome-billable-metrics]], [[metronome-customers-and-contracts]]
- Related sources: [[source-metronome-api-reference-usage-ingest-events]], [[source-metronome-api-reference-idempotency]], [[source-metronome-guides-implement-metronome-core-concepts-create-billable-metrics]]

## Raw Sources

- [[raw/metronome/guides/implement-metronome/core-concepts/send-usage-events-2026-07-13|2026-07-13 snapshot — usage-event schema, direct-ingest resilience, and heartbeat guidance]]
