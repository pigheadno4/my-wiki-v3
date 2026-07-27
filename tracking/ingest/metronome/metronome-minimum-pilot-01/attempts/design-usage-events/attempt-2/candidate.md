---
title: "Metronome Design Usage Events"
type: source
date_ingested: 2026-07-27
original_format: webpage
raw_files:
  - "metronome/guides/events/design-usage-events-2026-07-13.md"
tags: [metronome, usage-events, usage-based-billing, billable-metrics]
---

## Overview

This guide explains how to design usage events for Metronome with a CDN billing example. It frames event design around required billing and notification outcomes, the data and timing available in the originating system, and retaining fields that can support later reporting or pricing changes.

## Key takeaways

- Start from the measures required for billing or operations; the CDN example needs `transfer` events with `bytes`, `transaction_id`, `customer_id`, and `timestamp` to measure customer data transfer for a billing period.
- Event frequency and payload shape should follow what the source system can reliably provide. Individual access-log events and hourly domain summaries can both support monthly invoicing, but have different customer-identifier and notification-cadence implications.
- Include available contextual fields such as domain and data center when possible so future usage reporting and region-specific metrics can use them.
- New billable metrics apply only to future collection and aggregation; they cannot be applied retroactively to historical data.

## Details

### Work backward from requirements

The guide recommends starting with existing requirements or an ideal invoice. In its CDN scenario, the minimum event uses event type `transfer`, a `bytes` property, `transaction_id`, `customer_id`, and `timestamp`; this supports summing bytes for a customer and billing period. The same transfer measure can also support traffic-spike notifications. Pricing details may be adjusted later only if the needed metrics are already present.

### Work forward from available data

The guide contrasts sending an event for each served page with sending incremental per-customer summaries. A globally aggregated detailed log can be forwarded as individual events, while independently logged data centers may need to send hourly summaries from a central system that can map a domain to its customer. The selected cadence must also meet operational notification needs.

### Preserve future options

The guide recommends sending available event data, because the stream pipeline discards irrelevant data during processing. In the example, retaining `domain` enables usage breakdowns by domain, and retaining `data_center` enables filtered regional metrics with individual regional prices. Those future metrics affect only future data collection and aggregation.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-event-ingestion]], [[metronome-billable-metrics]], [[metronome-usage-based-billing]]

## Raw Sources

- [[design-usage-events-2026-07-13]] — verbatim guide on designing Metronome usage events
