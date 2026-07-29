---
title: "Metronome Create Billable Metrics"
type: source
date_ingested: 2026-07-30
canonical_url: "https://docs.metronome.com/guides/implement-metronome/core-concepts/create-billable-metrics"
original_format: webpage
raw_files:
  - "metronome/guides/implement-metronome/core-concepts/create-billable-metrics-2026-07-13.md"
tags: [metronome, billable-metrics, usage-based-billing, metering]
---

## Overview

This guide explains how to design, configure, and test Metronome billable metrics, the queries that turn raw usage events into invoice-line quantities and alert inputs. It distinguishes streaming metrics from SQL metrics, defines how group keys connect metering to invoice presentation and dimensional pricing, and identifies creation-time and cardinality constraints.

## Key takeaways

- A billable metric filters and aggregates the event stream into the quantity used for an invoice line item. Products supply invoice presentation, rate cards attach list prices, and contracts can override rates and generate customer invoices.
- Design each metric around one usage component that may be priced independently. The guide recommends considering customer value, invoice expectations, available event properties, event scale, and required calculation latency.
- Streaming billable metrics support `COUNT`, `SUM`, `MAX`, and `LATEST`; `LATEST` returns the most recent property value in the billing period. Use a SQL billable metric for more complex calculations, including distinct counts.
- A streaming metric must exist before incoming usage is associated with it by default. Metronome retains raw events and can perform a representative-assisted reflow when earlier events need to apply to a new streaming metric.
- Group keys must be defined at the metric layer before downstream use. They support invoice presentation and dimension-specific pricing, but streaming-metric group keys cannot be edited after creation.
- After creating a metric, send test events through the ingest endpoint and look them up by `transaction_id` with `searchEvents` to verify billable-metric and customer matching.

## Billable metrics in the pricing model

A billable metric is the metering layer between usage events and commercial configuration. It selects relevant events and computes quantities. A product controls how those quantities appear as invoice line items, a rate card assigns product rates, and a customer contract can override rates and uses the calculated quantities when generating invoices.

The guide recommends defining the usage components first. Examples include API-call counts, input and output tokens, GB-hours of storage, and user counts. When one event carries several independently chargeable values—such as CPU utilization, memory use, and cloud region—separate metrics should aggregate the individual properties that may contribute to pricing.

## Streaming and SQL metrics

Streaming billable metrics are intended for high-throughput, low-latency workflows that can use simple filters and the `COUNT`, `SUM`, `MAX`, or `LATEST` aggregations. `LATEST` bills on the most recent value observed for a property during the billing period, such as the latest seat count or storage reading. Streaming metrics also support real-time alerting across high-volume customer populations.

SQL billable metrics support calculations that basic streaming filters cannot express. The guide specifically directs distinct counting, such as unique users, to a SQL metric using `count(distinct …)`. It says SQL metrics can provide comparable alerting performance for many workloads, while complex queries or large numbers of SQL metrics may require Metronome guidance to meet latency goals.

A streaming metric must be defined before usage is attributed to it by default. Although this is a creation-time processing boundary, the guide also says Metronome retains raw events and can perform a reflow on request so earlier events apply to a newly created streaming metric. The page does not define reflow availability, timing, cost, or operational limits.

> [!warning] Retroactivity wording
> The separate event-design guide says new billable metrics cannot apply retroactively to historical data. This guide documents a representative-assisted reflow exception. Treat forward-only matching as the default and confirm any historical reflow directly with Metronome.

## Group keys

Group keys name event properties that can break usage out in downstream pricing and packaging, similarly to SQL `GROUP BY`. A presentation group key separates invoice quantities by a property such as `user_id`; a pricing group key allows different rates for dimensions such as cloud provider and region. When a product needs both presentation and pricing dimensions, all properties must be combined into one compound group key on the billable metric.

For a streaming metric, a group-key property must first appear in the property filters with an `Exists` or `In` filter. Streaming group keys are not editable after metric creation. For a SQL metric, any selected property outside the required `value` column can be a group key. The guide warns that customer-level group-key cardinality approaching one thousand possible values can increase API latency and should be reviewed with a Metronome representative.

## Filters, aggregation, and testing

The Basic Filters editor creates streaming metrics using predefined filters and aggregations. The SQL Editor creates SQL metrics for custom calculations. After configuration, the guide recommends sending test events through the ingest endpoint, then calling `searchEvents` with their transaction IDs. The search response identifies matched billable metrics and, when present, the matched customer; missing matches indicate that the metric definition or customer association needs investigation.

## Scope and boundaries

- The guide defines metric-design and testing behavior but does not provide the complete create-billable-metric API schema.
- It does not state exact alerting latency, streaming throughput limits, SQL query limits, or reflow service guarantees.
- The approximately one-thousand-value group-key note is a threshold for contacting Metronome, not a documented hard cardinality limit.
- The testing flow verifies matching; the page does not describe invoice finalization or payment collection.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-billable-metrics]], [[metronome-event-ingestion]], [[metronome-products-and-rate-cards]], [[metronome-usage-based-billing]]
- Related source: [[source-metronome-guides-events-design-usage-events]]

## Raw Sources

- [[raw/metronome/guides/implement-metronome/core-concepts/create-billable-metrics-2026-07-13|2026-07-13 snapshot — billable metric design, configuration, and testing guide]]
