---
title: "Metronome Event Ingestion"
type: concept
category: technology
tags: [metronome, usage-events, metering, idempotency]
---

## Definition

Metronome event ingestion accepts application usage payloads through the `/ingest` endpoint. Events carry an idempotency key, occurrence time, customer identifier, event type, and optional properties that downstream billable metrics can filter, aggregate, and group.

## Event contract

## Commercial event-count boundary

For Metronome's platform-pricing terminology, one Event is each discrete JSON object submitted to and accepted through the ingestion API. Examples such as API calls, storage measurements, and data transfers describe what an accepted object may represent; this source does not define how rejected, retried, or duplicate submissions affect commercial counts. [[source-metronome-guides-platform-configuration-metronome-pricing-model]]

- `POST /v1/ingest` is bearer authenticated and accepts a JSON array containing one to 100 events.
- `transaction_id` is the event's required, nonempty idempotency key, with a maximum length of 128 characters; Metronome documents a 34-day duplicate-detection window.
- `timestamp` is required and RFC 3339 formatted. The API reference permits historical events up to 34 days in the past.
- `customer_id` is required and may be a Metronome customer ID or an application-defined ingest alias.
- Customer creation accepts up to 2,000 ingest aliases of 1–128 characters each; the older `external_id` alias field is deprecated.
- `event_type` is a required nonempty string, and optional `properties` can contain metering and grouping data. The endpoint schema treats the map as an object, while the implementation guide recommends representing every property key and value as a string to avoid floating-point precision loss; Metronome says it computes with arbitrary-precision decimals internally.
- The dashboard quickstart describes `transaction_id`, `customer_id`, `event_type`, and `timestamp` as required and permits up to 2,000 event properties.

## Event design

Metronome recommends working backward from billing and operational outcomes, then forward from the timing and data available in the source system. A producer can send detailed events as activity occurs or send periodic summaries; the appropriate choice depends on whether the producer can resolve `customer_id` and whether the cadence meets needs such as usage-spike notifications.

Keeping available context in `properties` preserves future options. In the documentation's CDN example, `domain` supports per-domain usage breakdowns and `data_center` supports later regional metrics and pricing.

## Segment destination mapping boundary

Metronome's Segment integration uses the Metronome (Actions) destination and requires explicit mappings for `transaction_id`, `customer_id`, RFC 3339 `timestamp`, `event_type`, and `properties`, even when source and destination names match. The default maps Segment `messageId` to `transaction_id`, while another Segment field may be selected manually. This is an adapter-specific mapping contract: unlike the direct `/ingest` schema, which treats `properties` as optional, the Segment destination requires a mapping slot for it. The page's unqualified exactly-once wording does not replace the separately documented 34-day duplicate-suppression boundary, and it does not define whether Segment retries preserve `messageId`.

## Processing boundary

An accepted event is not automatically billable. It must match a billable metric and a customer before it contributes to billing. New streaming metrics match later events by default; the create-metrics guide says Metronome retains raw events and can perform a representative-assisted reflow for earlier events, without documenting service guarantees.

One event can feed multiple billable metrics. Metronome presents this separation as allowing the producer's instrumentation to remain stable while metering configuration changes, but the architecture guide does not define edit eligibility, effective timing, or retroactive behavior; the forward-only default and assisted-reflow exception below still apply.

The ingest reference documents only a `200 Success` response without a body schema. It does not define partial-batch acceptance, validation errors, duplicate indicators, ordering, retry semantics, future timestamps, payload-collision behavior, or whether the 34-day cutoff is inclusive.

## Scale, observability, and recovery

A correction guide applies compensating usage only while the current-period invoice is `DRAFT`: send a new event with a negative quantity or value that matches the affected product's billable metric. For a previous-period `finalized` invoice, it says usage events cannot be corrected or adjusted; use a future credit or an external A/R credit memo instead. Its separate full-invoice re-bill flow negates and replaces usage before voiding and regeneration, but does not reconcile that ordering with the finalized-invoice rule, so the invoice-state precondition remains ambiguous.

> [!warning] Documentation scope conflict
> [[source-metronome-guides-invoices-invoice-optimization-issue-credit-memos]] calls external invoicing/customer-A/R voiding, cancellation, and regeneration the only credit-and-rebill option beyond 34 days, while [[source-metronome-guides-events-high-volume-ingestion]] says corrections beyond 34 days are handled by Metronome operations. The documentation does not establish whether these are separate self-service invoice re-billing and operations-assisted usage-correction scopes. Do not treat the routes as interchangeable; verify the applicable route with Metronome.

> [!warning] Heartbeat idempotency scope
> The send-events guide says only one event with a given `transaction_id` is processed in its heartbeat section, but the same page specifically limits later duplicate suppression to the next 34 days after an event is accepted. Use deterministic period IDs for duplicate sends within that documented window; do not infer permanent global uniqueness or safe reuse behavior after day 34.

- The API reference advertises support for 100,000 events per second and says capacity can scale beyond that figure. The separate high-volume guide describes infrastructure capacity up to 110,000 events per second and a default account limit of 5,000 events per second that can be increased by contacting Metronome; these are different scopes, not one interchangeable limit.
- High-volume producers can batch up to 100 events in one ingest request.
- The event explorer can inspect payloads, duplicates, customer and billable-metric attribution, transaction IDs, and CSV exports. For continuous checks, the Event Search API can sample raw events and verify that they still match active billable metrics.
- The scale guide recommends queueing, retries, message-queue logging, alerting, and dead-letter queues around the producer pipeline.
- Historical ingest and deduplication use a 34-day window through the same ingest endpoint. The guide says this supports traffic replay and real-time re-rating of draft invoices and credit ledgers; older corrections require Metronome operations.
- For direct API delivery, the implementation guide says to retry network and `5xx` failures until `200` because a failed call can be partially ingested. On `429`, back off with increasing exponential delays; move other `4xx` payload failures to a dead-letter queue instead of automatically retrying them.
- Metronome can configure a chosen trial API failure rate in Sandbox or Production; the guide recommends 20%. Producers should log message-queue traffic during initial integration and whenever the event structure changes.
- Periodic heartbeat events should use a deterministic transaction ID such as `<node id>_<floor(unix_now()/60)>` and send at least two heartbeats per measurement period. Duplicate IDs are ignored, reducing the chance that timer imprecision or delay leaves a measurement gap.

## Invoice preview boundary

The Preview Events API provides a separate, non-ingestion path for testing how supplied events would affect a customer's invoices under the current contract configuration. `replace` mode ignores historical usage, while `merge` combines the supplied events with existing usage. Preview transaction IDs are checked against historical events from the previous 34 days, but contracts with SQL billable metrics are not supported.

Dashboard test-event entry is a separate Sandbox-only path. Its transaction ID must be unique, its timestamp must be within the prior 34 days, and its event type and properties must match the configured billable metric. Production events use the API.

Preview Events is a simulation path: submitted events affect only the preview calculation and are not processed or billed. The guide says transaction IDs duplicating an `/ingest` event from the prior 34 days are deduplicated, but it does not say whether a preview reserves an ID or changes later ingest behavior. It also says duplicate IDs within one preview request are deduplicated, contradicting the dedicated API reference's statement that same-request duplicates cause an error.

The endpoint has an 8 RPS per-client limit and is not suitable for validating every event in real time. The guide recommends caching similar calculations and batching preview events, without defining cache validity, batch size, rate-limit headers, latency, or retry behavior. A customer invoice containing SQL-based billable metrics causes HTTP 400.

## Architecture-planning checklist

Before selecting an ingest design, identify usage origins and reliable delivery, choose event or batch cadence from generation and change behavior, plan for peak volume and velocity, carry grouping keys required by pricing dimensions, and retain contextual fields that make spend interpretable. This planning source does not itself define schemas, transport, throughput, cardinality, freshness, replay, or correction guarantees.

## Production-readiness checklist boundary

Metronome's go-live checklist recommends queueing usage events, sampling `searchEvents` to confirm active-metric matching, load-testing expected peaks, and injecting ingestion failures. It also places `properties` under required fields, directly contradicting the dedicated ingest reference's optional `properties` schema. Separately, the checklist asks teams to exercise 14-day backdating, while the dedicated ingest sources document a 34-day historical-ingest window. The checklist does not call 14 days a maximum, so days 15–34 remain outside its stated test coverage rather than forming mutually exclusive limits or a retention conflict. [[source-metronome-guides-implement-metronome-production-checklist]]

## Sources

- [[source-metronome-integrations-platform-integrations-segment]] - Segment destination setup, explicit five-field mapping contract, default `messageId` transaction identity, and managed-delivery unknowns

- [[source-metronome-guides-invoices-invoice-optimization-issue-credit-memos]] — negative usage-event correction for draft invoices, the finalized-invoice boundary, and the conflicting beyond-34-day credit-and-rebill route
- [[source-metronome-guides-events-send-usage-events]] — alternate canonical events-guide route for event fields, string-property guidance, direct-ingest retry handling, heartbeat IDs, and the 34-day scope tension

- [[source-metronome-guides-get-started-developer-sdks]] — SDK ingestion example, payload fields, limits, deduplication, and matching sequence
- [[source-metronome-guides-events-design-usage-events]] — event-design principles, cadence tradeoffs, and contextual-property examples
- [[source-metronome-guides-events-high-volume-ingestion]] — throughput, batching, observability, and recovery controls
- [[source-metronome-api-reference-invoices-preview-events]] — event-to-invoice preview modes, deduplication behavior, and limitations
- [[source-metronome-guides-get-started-metronome-dashboard-quickstart]] — required fields, property limit, and Sandbox test-event boundary
- [[source-metronome-api-reference-usage-ingest-events]] — endpoint authentication, exact event schema, idempotency window, response gaps, and advertised capacity
- [[source-metronome-api-reference-idempotency]] — transaction-ID duplicate suppression, retention, and retry guidance
- [[source-metronome-guides-implement-metronome-core-concepts-create-billable-metrics]] — post-ingest matching test and assisted-reflow exception
- [[source-metronome-api-reference-customers-create-a-customer]] — ingest-alias provisioning, limits, and deprecation boundary
- [[source-metronome-guides-implement-metronome-core-concepts-send-usage-events]] — producer-side event representation, retry and DLQ behavior, resilience testing, and heartbeat guidance
- [[source-metronome-guides-get-started-how-metronome-works]] — one-event-to-many-metrics relationship and instrumentation boundary
- [[source-metronome-guides-implement-metronome-planning-your-billing-architecture]] — data-origin, cadence, scale, dimension, and context checklist
- [[source-metronome-guides-customers-billing-optimize-customer-experience-preview-event-cost]] — non-ingestion simulation boundary, transaction-ID conflict, 8 RPS limit, batching guidance, and SQL-metric exclusion

## Related

- [[metronome-billable-metrics]]
- [[metronome-customers-and-contracts]]
- [[metronome-usage-based-billing]]
- [[metronome-api-idempotency]]
