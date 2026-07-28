---
title: "Metronome Usage Events at Scale"
type: source
date_ingested: 2026-07-28
canonical_url: "https://docs.metronome.com/guides/events/high-volume-ingestion"
original_format: webpage
raw_files:
  - "metronome/guides/events/high-volume-ingestion-2026-07-13.md"
tags: [metronome, usage-events, event-ingestion, data-integrity]
---

## Overview
Metronome’s Usage events at scale guide describes high-throughput usage-event ingestion and tools for monitoring event data. It also outlines programmatic controls and recovery considerations for maintaining data integrity as event volume grows.

## Key takeaways
- Metronome states that its infrastructure supports up to 110,000 events per second, while the default ingest rate limit starts at 5,000 events per second.
- Clients can submit up to 100 usage events in one request to the ingest endpoint.
- The event UI supports inspection, searching, payload review, attribution review, and CSV export; the Event Search API can be used to sample events and validate billable-metric matching.
- The guide describes a 34-day historical ingest and deduplication window through the ingest endpoint for recovery and replay.

## Details
The guide recommends batching events when sending high volumes: send an array of usage-event objects in a POST request to the ingest endpoint, following the documented event schema.

For inspection, the event explorer can help validate ingestion, matching to billable metrics, and duplicate events. The documented controls include time-based event and duplicate-event graphs, searches by customer, duplicate status, billable metric, and transaction ID, complete event payload views, attribution views, and CSV export.

For sustained high-volume reliability, the guide recommends automated programmatic checks alongside queueing, retry, logging, alerting, and dead-letter-queue practices. It identifies Event Search API sampling as a control for detecting schema changes that could prevent events from matching active billable metrics.

The guide says the 34-day historical ingest and deduplication window uses the same ingest endpoint and can support replaying more than 24 hours of traffic, with draft invoices and credit ledgers re-rated in real time. It states that corrections beyond 34 days are handled by Metronome’s operations team.

## Related
- Coordinator audit: determine whether existing Metronome company and platform-specific concept pages should receive links or updates before promotion.

## Raw Sources
- [[raw/metronome/guides/events/high-volume-ingestion-2026-07-13|high-volume-ingestion-2026-07-13]] — verbatim Metronome documentation page.