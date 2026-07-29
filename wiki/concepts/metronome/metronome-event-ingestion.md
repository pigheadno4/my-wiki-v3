---
title: "Metronome Event Ingestion"
type: concept
category: technology
tags: [metronome, usage-events, metering, idempotency]
---

## Definition

Metronome event ingestion accepts application usage payloads through the `/ingest` endpoint. Events carry an idempotency key, occurrence time, customer identifier, event type, and arbitrary properties that downstream billable metrics can filter, aggregate, and group.

## Event contract

- `POST /v1/ingest` is bearer authenticated and accepts a JSON array containing one to 100 events.
- `transaction_id` is the event's required, nonempty idempotency key, with a maximum length of 128 characters; Metronome documents a 34-day duplicate-detection window.
- `timestamp` is required and RFC 3339 formatted. The API reference permits historical events up to 34 days in the past.
- `customer_id` is required and may be a Metronome customer ID or an application-defined ingest alias.
- `event_type` is a required nonempty string, and optional `properties` can contain arbitrary metering and grouping data.
- The dashboard quickstart describes `transaction_id`, `customer_id`, `event_type`, and `timestamp` as required and permits up to 2,000 event properties.

## Event design

Metronome recommends working backward from billing and operational outcomes, then forward from the timing and data available in the source system. A producer can send detailed events as activity occurs or send periodic summaries; the appropriate choice depends on whether the producer can resolve `customer_id` and whether the cadence meets needs such as usage-spike notifications.

Keeping available context in `properties` preserves future options. In the documentation's CDN example, `domain` supports per-domain usage breakdowns and `data_center` supports later regional metrics and pricing.

## Processing boundary

An accepted event is not automatically billable. It must match a billable metric and a customer before it contributes to billing. The SDK guide also warns that a newly created billable metric matches only events sent after the metric was created.

The ingest reference documents only a `200 Success` response without a body schema. It does not define partial-batch acceptance, validation errors, duplicate indicators, ordering, retry semantics, future timestamps, payload-collision behavior, or whether the 34-day cutoff is inclusive.

## Scale, observability, and recovery

- The API reference advertises support for 100,000 events per second and says capacity can scale beyond that figure. The separate high-volume guide describes infrastructure capacity up to 110,000 events per second and a default account limit of 5,000 events per second that can be increased by contacting Metronome; these are different scopes, not one interchangeable limit.
- High-volume producers can batch up to 100 events in one ingest request.
- The event explorer can inspect payloads, duplicates, customer and billable-metric attribution, transaction IDs, and CSV exports. For continuous checks, the Event Search API can sample raw events and verify that they still match active billable metrics.
- The scale guide recommends queueing, retries, message-queue logging, alerting, and dead-letter queues around the producer pipeline.
- Historical ingest and deduplication use a 34-day window through the same ingest endpoint. The guide says this supports traffic replay and real-time re-rating of draft invoices and credit ledgers; older corrections require Metronome operations.

## Invoice preview boundary

The Preview Events API provides a separate, non-ingestion path for testing how supplied events would affect a customer's invoices under the current contract configuration. `replace` mode ignores historical usage, while `merge` combines the supplied events with existing usage. Preview transaction IDs are checked against historical events from the previous 34 days, but contracts with SQL billable metrics are not supported.

Dashboard test-event entry is a separate Sandbox-only path. Its transaction ID must be unique, its timestamp must be within the prior 34 days, and its event type and properties must match the configured billable metric. Production events use the API.

## Sources

- [[source-metronome-guides-get-started-developer-sdks]] — SDK ingestion example, payload fields, limits, deduplication, and matching sequence
- [[source-metronome-guides-events-design-usage-events]] — event-design principles, cadence tradeoffs, and contextual-property examples
- [[source-metronome-guides-events-high-volume-ingestion]] — throughput, batching, observability, and recovery controls
- [[source-metronome-api-reference-invoices-preview-events]] — event-to-invoice preview modes, deduplication behavior, and limitations
- [[source-metronome-guides-get-started-metronome-dashboard-quickstart]] — required fields, property limit, and Sandbox test-event boundary
- [[source-metronome-api-reference-usage-ingest-events]] — endpoint authentication, exact event schema, idempotency window, response gaps, and advertised capacity

## Related

- [[metronome-billable-metrics]]
- [[metronome-customers-and-contracts]]
- [[metronome-usage-based-billing]]
