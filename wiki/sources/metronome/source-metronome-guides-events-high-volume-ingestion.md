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

This guide describes Metronome's high-throughput usage-event ingestion, event-inspection tools, and operational controls for maintaining data integrity as volume grows.

## Key takeaways

- Metronome documents infrastructure capacity of up to 110,000 events per second (6.6 million per minute), while the default ingest rate limit starts at 5,000 events per second.
- Clients can submit up to 100 usage events in one request to the ingest endpoint.
- The event UI supports inspection, searching, payload review, attribution review, and CSV export; the Event Search API can sample events and validate billable-metric matching.
- The guide describes a 34-day historical ingest and deduplication window through the ingest endpoint for recovery and replay.

## Details

### High-throughput ingestion

The guide recommends batching events when sending high volumes: submit an array of up to 100 usage-event objects in a POST request to the ingest endpoint. Higher throughput than the default 5,000-events-per-second limit requires contacting Metronome.

### Inspection and observability

The event explorer can validate ingestion, matching to customers and billable metrics, and duplicate events. Its documented controls include time-based event and duplicate-event graphs, searches by customer, duplicate status, billable metric, and transaction ID, complete payload views, attribution views, and CSV export.

For sustained reliability, the guide recommends automated checks plus queueing, retries, message-queue logging, alerting, and dead-letter queues. It identifies Event Search API sampling as a control for detecting upstream schema changes that could stop events from matching active billable metrics.

### Recovery boundary

The 34-day historical ingest and deduplication window uses the same ingest endpoint. Metronome says it supports replaying more than 24 hours of traffic and re-rating draft invoices and credit ledgers in real time. Corrections beyond 34 days are handled by Metronome's operations team.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-event-ingestion]], [[metronome-billable-metrics]]

## Raw Sources

- [[raw/metronome/guides/events/high-volume-ingestion-2026-07-13|2026-07-13 snapshot — throughput, observability, and recovery guidance]]
