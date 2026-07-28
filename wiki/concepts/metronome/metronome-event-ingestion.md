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

## Event design

Metronome recommends working backward from billing and operational outcomes, then forward from the timing and data available in the source system. A producer can send detailed events as activity occurs or send periodic summaries; the appropriate choice depends on whether the producer can resolve `customer_id` and whether the cadence meets needs such as usage-spike notifications.

Keeping available context in `properties` preserves future options. In the documentation's CDN example, `domain` supports per-domain usage breakdowns and `data_center` supports later regional metrics and pricing.

## Processing boundary

An accepted event is not automatically billable. It must match a billable metric and a customer before it contributes to billing. The SDK guide also warns that a newly created billable metric matches only events sent after the metric was created.

## Invoice preview boundary

The Preview Events API provides a separate, non-ingestion path for testing how supplied events would affect a customer's invoices under the current contract configuration. `replace` mode ignores historical usage, while `merge` combines the supplied events with existing usage. Preview transaction IDs are checked against historical events from the previous 34 days, but contracts with SQL billable metrics are not supported.

## Sources

- [[source-metronome-guides-get-started-developer-sdks]] — SDK ingestion example, payload fields, limits, deduplication, and matching sequence
- [[source-metronome-guides-events-design-usage-events]] — event-design principles, cadence tradeoffs, and contextual-property examples
- [[source-metronome-api-reference-invoices-preview-events]] — event-to-invoice preview modes, deduplication behavior, and limitations

## Related

- [[metronome-billable-metrics]]
- [[metronome-customers-and-contracts]]
- [[metronome-usage-based-billing]]
