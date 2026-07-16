---
title: "Design usage events"
type: source
date_ingested: 2026-07-16
canonical_url: "https://docs.metronome.com/guides/events/design-usage-events"
original_format: webpage
raw_files:
  - "metronome/guides/events/design-usage-events-2026-07-13.md"
tags: [metronome, usage events, usage-based billing, billable metrics]
---

## Overview

This guide explains how to design Metronome usage events for usage-based billing, using a hypothetical CDN integration and three principles: work backward from needs, work forward from available data, and maximize flexibility. [q1]

## Key takeaways

- Design usage events by starting from existing requirements or an ideal invoice; pricing can be applied or adjusted later if the required metrics are present. [q2]
- For invoicing and traffic-spike notifications, the minimum event measures data transfer and includes event type, bytes, transaction ID, customer ID, and timestamp. [q2]
- Choose event timing and content according to business needs and available system data; incremental summaries and per-page events can provide the same monthly invoicing ability. [q3]
- Send as much data as possible so later invoice breakdowns and regional pricing can use fields such as domain and data_center. [q4, q5]
- Billable metrics are stream-based and are not retroactive; changes affect future collection and aggregation only. [q5]

## Details

### Design usage events

- The guide frames usage-event design as important because Metronome success depends on the data provided, and it applies the discussion to a hypothetical CDN integration for usage-based billing. [q1]
- The guide establishes three principles: work backward from what is needed, work forward from what is available, and maximize flexibility. [q1]

### Work backward from what you need​

- Start from existing requirements or an ideal invoice. Exact pricing may be unknown initially and can be applied or adjusted later if required metrics are in place. [q2]
- The CDN example needs data transfer for both invoicing and unusual-traffic notifications. [q2]
- The bare-minimum example contains event_type, a bytes property, transaction_id, customer_id, and timestamp, and supports summing bytes for transfer events by customer and billing period. [q2]

### Work forward from what you have​

- Consider available data and how it may support future needs, including event timing and additional contextual fields such as data center, domain, file type, and URL. [q3]
- Sending incremental per-customer summaries or sending an event for every served page can provide the same month-end invoicing ability; the choice depends on needs. [q3]
- Existing-system architecture influences timing and content: centralized Apache Flume logs support individual events as logs arrive, while independent data-center logs without customer-database access favor hourly domain summaries with central customer lookup. [q3]
- The hypothetical customer-support team confirms that an hourly cadence is fast enough for its desired traffic-spike notifications. [q3]

### Maximize your flexibility​

- Because business needs evolve, the guide recommends creating a flexible system that can adapt rather than attempting to anticipate every future requirement. [q4]
- Metronome flexibility is maximized by sending as much data as possible; the stream pipeline handles high throughput and discards irrelevant data during processing. [q4]
- Including domain enables querying Metronome usage data grouped by domain for invoice breakdowns. [q4]
- Including data_center enables filtering usage events, mapping data centers to regions, defining regional billable metrics, and setting individual regional prices. [q5]
- New billable metrics cannot be applied to historical data because stream changes affect only future data collection and aggregation. [q5]

## Change history

- 2026-07-16: gpt-5.6-luna comparison-pilot draft from the assigned raw snapshot.

## Related

- Company: [[metronome]]
- Concepts: coordinator concept audit required before promotion.

## Raw Sources

- [[raw/metronome/guides/events/design-usage-events-2026-07-13|Design usage events]]
