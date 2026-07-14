---
title: "Metronome Event Ingestion"
type: concept
category: technology
tags: [metronome, usage-events, metering, idempotency]
---

## Definition

Metronome event ingestion accepts application usage payloads through the `/ingest` endpoint. Events carry an idempotency key, occurrence time, customer identifier, event type, and arbitrary properties that downstream billable metrics can filter, aggregate, and group.

## Event contract

- A request can contain up to 100 events.
- `transaction_id` is the event's unique idempotency key; Metronome deduplicates on it so a producer can resend an event without double charging.
- `timestamp` records when usage occurred. The SDK guide permits timestamps up to 34 days in the past.
- `customer_id` may be a Metronome customer ID or an application-defined identifier later registered as an ingest alias.
- `event_type` is application defined, and `properties` can contain arbitrary metering and grouping data.

## Processing boundary

An accepted event is not automatically billable. It must match a billable metric and a customer before it contributes to billing. The SDK guide also warns that a newly created billable metric matches only events sent after the metric was created.

## Sources

- [[source-metronome-guides-get-started-developer-sdks]] — SDK ingestion example, payload fields, limits, deduplication, and matching sequence

## Related

- [[metronome-billable-metrics]]
- [[metronome-customers-and-contracts]]
- [[metronome-usage-based-billing]]

