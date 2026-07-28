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
- The SDK guide lists `SUM`, `COUNT`, and `MAX` as supported aggregation operations.
- `group_keys` divide usage into buckets, similar to SQL `GROUP BY`, and can support grouped invoice presentation.
- Context retained on usage events can support later metric changes. The event-design guide uses `domain` for grouped usage reporting and `data_center` for region-specific metrics and prices.

## Lifecycle boundary

The SDK guide states that billable metrics match only usage events sent after metric creation. Creating a metric therefore does not retroactively meter earlier events; the guide sends a new event after creating its example metric.

## Sources

- [[source-metronome-guides-get-started-developer-sdks]] — metric definition, filters, aggregation operations, grouping, and creation-time boundary
- [[source-metronome-guides-events-design-usage-events]] — future metric flexibility and the non-retroactive processing boundary

## Related

- [[metronome-event-ingestion]]
- [[metronome-products-and-rate-cards]]
- [[metronome-usage-based-billing]]
