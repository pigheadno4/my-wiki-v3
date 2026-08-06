---
title: "Metronome Segment Integration"
type: source
date_ingested: 2026-08-01
original_format: webpage
canonical_url: "https://docs.metronome.com/integrations/platform-integrations/segment"
raw_files:
  - "metronome/integrations/platform-integrations/segment-2026-07-13.md"
tags: [metronome, segment, usage-events, event-ingestion, idempotency, integrations]
---

## Overview

This guide configures Segment's Metronome (Actions) destination to send usage events into Metronome. It covers destination setup, the Segment-side mapping contract, the default transaction-ID mapping, and condition-based Destination Actions; it does not define the direct `/ingest` transport or Segment's delivery guarantees.

## Key takeaways

- Setup selects Metronome (Actions) from Segment's Destinations Catalog, attaches a Segment source, names the destination, and stores a Metronome API token in its settings.
- The destination requires explicit mappings for `transaction_id`, `customer_id`, `timestamp`, `event_type`, and `properties`, even when source and destination property names match. This is stricter than the direct ingest schema's optional `properties` field and should be treated as a Segment adapter requirement, not a replacement API schema.
- Segment's default mapping uses `messageId` as Metronome's `transaction_id`; a user can instead map any Segment event field. The page's unqualified exactly-once wording does not extend Metronome's separately documented 34-day duplicate-suppression window.
- Destination Actions can add mappings with conditional triggers that determine which Segment data reaches Metronome. The page calls these actions `subscriptions`, meaning Segment destination routing rules rather than Metronome customer billing subscriptions or contracts.

## Setup and mapping contract

The setup flow creates a Metronome (Actions) destination for a selected Segment source and authenticates it with a Metronome API token. The page does not define token permissions, environment binding, rotation, secret handling, validation, or whether one destination can safely target several Metronome environments.

Within Segment, every one of the five listed Metronome fields needs a mapping: string-valued `transaction_id`, `customer_id`, `timestamp`, and `event_type`, plus an object-valued `properties`. `timestamp` is described as RFC 3339. The direct event guide and ingest API reference describe `properties` as optional, so the requirement here is specific to configuring this destination. It does not prove that direct `/ingest` payloads must always contain `properties`.

The page says `customer_id` identifies the Metronome customer to which the event applies, but it does not state whether the Segment mapping may use a Metronome customer UUID, an ingest alias, or both. It also does not establish an automatic mapping from Segment `userId`, anonymous IDs, or any other identity field; that choice remains part of the explicit mapping.

The worked `analytics.track` event is present as text, but the resulting field mapping appears only in an image. The captured source therefore does not provide byte-readable evidence for the example's individual mapping expressions, and those expressions should not be reconstructed from the example payload alone.

## Transaction identity and conditional delivery

The default configuration maps Segment `messageId` to Metronome `transaction_id`, while allowing another Segment field to be chosen. The guide says this field ensures exactly-once processing but gives no time window, collision behavior, replay behavior, or duplicate response. Dedicated Metronome event sources bound duplicate suppression to 34 days after acceptance, so this page must not be read as evidence of permanent global uniqueness.

Additional Destination Actions let users create more trigger-and-mapping combinations. A trigger can contain any number of conditions; the example excludes events when `User ID` contains the company's email domain. This is a routing example, not evidence that email filtering, a specific user field, or a particular trigger is required. It also does not document trigger evaluation order, overlap between actions, duplicate delivery when several triggers match, failure handling, retry behavior, ordering, backfill, or observability.

## Field and delivery boundaries

> [!warning] Segment mapping versus direct-ingest schema
> This guide calls all five mappings required, including `properties`, while the direct usage-event guide and ingest API reference call `properties` optional. Preserve the scopes separately: Segment requires an explicit mapping slot for this destination, but that does not change the base `/ingest` event schema.

The source provides no request batching, payload-size, throughput, timeout, response, retry, partial-ingestion, dead-letter, rate-limit, timestamp-window, customer-alias, or event-property limit for Segment delivery. Direct `/ingest` queue and retry guidance must not be assumed to describe Segment's managed destination, and the source does not say whether Segment retries preserve `messageId`.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-integrations]], [[metronome-event-ingestion]], [[metronome-api-idempotency]], [[metronome-customers-and-contracts]]
- Related sources: [[source-metronome-guides-events-send-usage-events]], [[source-metronome-guides-implement-metronome-core-concepts-send-usage-events]], [[source-metronome-api-reference-usage-ingest-events]]

## Raw Sources

- [[raw/metronome/integrations/platform-integrations/segment-2026-07-13|2026-07-13 snapshot - Segment destination setup, required mappings, transaction-ID default, and conditional Destination Actions]]
