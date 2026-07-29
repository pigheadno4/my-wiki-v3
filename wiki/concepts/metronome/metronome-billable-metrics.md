---
title: "Metronome Billable Metrics"
type: concept
category: technology
tags: [metronome, billable-metrics, aggregation, usage-based-billing]
---

## Definition

A Metronome billable metric defines a per-customer aggregation over a selected subset of usage events. It connects raw event data to a chargeable product by declaring which events match, which property to aggregate, how to aggregate it, and how to group the result.

## Matching and aggregation

- `event_type_filter` limits matching by event type and can be omitted to consider all event types.
- `property_filters` declare expected event properties. A property marked `exists=true` prevents matching when that property is absent.
- `aggregation_key` selects the value to aggregate.
- Streaming metrics support `COUNT`, `SUM`, `MAX`, and `LATEST`; `LATEST` uses the most recent property value in the billing period. Distinct counts require a SQL metric.
- `group_keys` divide usage into buckets, similar to SQL `GROUP BY`, and can support grouped invoice presentation.
- A pricing group key permits dimension-specific rates, while a presentation group key creates invoice breakdowns without changing the price.
- When presentation and pricing dimensions are both needed, their properties must be combined in one compound metric group key. On a streaming metric, each group-key property must first use an `Exists` or `In` property filter, and group keys cannot be edited after creation.
- Customer-level group-key cardinality approaching one thousand values can increase API latency; the guide treats this as a reason to contact Metronome, not a hard limit.
- Context retained on usage events can support later metric changes. The event-design guide uses `domain` for grouped usage reporting and `data_center` for region-specific metrics and prices.

## Lifecycle boundary

The SDK and event-design guides state that billable metrics match only usage events sent after metric creation by default. The create-metrics guide adds that Metronome retains raw events and can perform a representative-assisted reflow when earlier events need to apply to a new streaming metric. The page does not define reflow timing, eligibility, cost, or operational limits.

> [!warning] Documentation scope
> The event-design source says new metrics cannot apply retroactively, while the create-metrics guide documents a Metronome-assisted reflow exception. Treat forward-only attribution as the default self-service behavior and reflow as an exception requiring confirmation.

The dashboard quickstart distinguishes streaming metrics for most real-time aggregation use cases from SQL metrics for calculations such as daily averages, unique period counts, or weighted formulas. It also states that group keys, property filters, and aggregation settings cannot be modified after metric creation.

The ingest API reference says accepted events are matched to billable metrics and become immediately available for usage and spend calculations, but it does not define per-event match results or failure behavior.

After metric creation, the guide recommends sending test events through `/ingest` and retrieving them by `transaction_id` through `searchEvents`; the response can show the matched metric and customer.

## Sources

- [[source-metronome-guides-get-started-developer-sdks]] — metric definition, filters, aggregation operations, grouping, and creation-time boundary
- [[source-metronome-guides-events-design-usage-events]] — future metric flexibility and the non-retroactive processing boundary
- [[source-metronome-guides-get-started-metronome-dashboard-quickstart]] — streaming and SQL roles, downstream group-key uses, and immutability
- [[source-metronome-api-reference-usage-ingest-events]] — ingest-time matching statement and response-documentation boundary
- [[source-metronome-guides-implement-metronome-core-concepts-create-billable-metrics]] — streaming and SQL roles, group-key constraints, assisted reflow, and matching tests

## Related

- [[metronome-event-ingestion]]
- [[metronome-products-and-rate-cards]]
- [[metronome-usage-based-billing]]
