---
title: "Metronome SDK API Walkthrough"
type: source
date_ingested: 2026-08-27
canonical_url: "https://docs.metronome.com/api-reference/sdks.md"
original_format: webpage
raw_files:
  - "metronome/api-reference/sdks-2026-07-13.md"
tags: [metronome, developer-sdks, usage-based-billing, event-ingestion, billable-metrics, rate-cards, contracts]
---

## Overview

This reference walkthrough uses Metronome's Python, Node.js, Ruby, and Go SDKs to connect an application to a basic usage-billing flow. It is a practical route from client setup and usage ingestion through billable-metric, customer, product, rate-card, and contract creation to a running draft invoice; it is not a complete SDK transport specification or an authority for every underlying API contract.

## Query-critical facts

- The four SDKs advertise typed Metronome endpoints and objects, pagination support, and configurable automatic request retries. The page states a default of up to three retries after failure, but does not identify the retryable failure set, counting convention, backoff, jitter, timeout policy, method safety, or whether an SDK injects or preserves an API-wide `Idempotency-Key`.
- SDK clients use an API-key bearer token and default to `METRONOME_BEARER_TOKEN` when the token is omitted from the constructor. The page does not define token scope, environment isolation, rotation, expiry, or permissions; the dedicated authorization references remain controlling.
- The walkthrough's data path is usage event -> billable metric -> customer association -> usage product and rate-card price -> customer contract -> draft invoice. The initial accepted event is not yet billable: it must be matched to a metric and customer, while the contract supplies the terms that allow invoice generation.
- One ingest request can carry up to 100 events. The page describes `transaction_id` as the event-level deduplication key, permits event timestamps up to 34 days in the past, accepts a Metronome ID or application-defined customer identifier, and leaves `event_type` plus arbitrary `properties` to the producer. It does not define the duplicate-detection lifetime, collision behavior for changed payloads, partial-batch outcomes, or how generic SDK retries interact with event deduplication.
- A billable metric filters events, selects a property to aggregate, supports the documented `SUM`, `COUNT`, and `MAX` operations, and can group results for invoice presentation. The page states that metrics match only events sent after metric creation; it does not define reflow, propagation latency, correction, or metric-mutation behavior.
- An ingest alias can join application-owned customer identity to usage sent before the Metronome customer is provisioned. The example then connects a usage product to the metric, applies quantity conversion and presentation grouping, creates a reusable rate card, and creates a customer contract from that card; dedicated endpoint references remain authoritative for required fields, lifecycle, validation, and recovery.
- The rate example says USD values use cents while other currencies use whole units, and it uses effective dates for price evolution. The contract example says billing periods after `starting_at` generate invoices and that current-period draft line items update seconds after usage arrives; neither statement is a service-level, finalized-invoice, downstream delivery, collection, tax, accounting, or reconciliation guarantee.

## Material boundaries and conflicts

- Automatic SDK retries are a transport policy, not proof that a repeated mutation is safe. Event `transaction_id` deduplication is distinct from the API-wide `Idempotency-Key` contract for POST operations, and this page does not establish whether retry attempts retain either identity or how to recover after an ambiguous result.
- The language examples are illustrative rather than a parity contract. Python, Node.js, and Ruby create the sample contract at `2024-08-01`, while Go uses `2024-09-01`; Python, Node.js, and Ruby supply metric `group_keys`, while Go omits them although the prose relies on `user_id` grouping. Confirm current language-specific call shapes in the linked SDK repositories.

> [!warning] Parallel canonical route and stale wiki caveats
> The wiki already contains [[source-metronome-guides-get-started-developer-sdks]], a separately canonicalized summary of the same broad walkthrough under `/guides/get-started/developer-sdks`. That summary records Ruby-client and Node-namespace inconsistencies that are not present in this assigned snapshot, whose examples use `metronome.v1` and `client.v1`; the Go timestamp and group-key differences remain. Do not claim that either canonical supersedes the other without collection or upstream authority.

## Raw-detail coverage map

Use the complete raw snapshot for all four installation commands and client constructors; SDK repository links; bearer-token setup; generic SDK feature wording; every Python, Node.js, Ruby, and Go call shape; usage payloads, limits, identifiers, timestamps, properties, and screenshots; billable-metric filters, aggregation fields, grouping, forward-only matching statement, and examples; customer creation and alias association; product type, presentation, quantity conversion, and external-item note; rate-card creation, entitlement, flat and tiered rates, denomination, and effective dates; contract creation, start-time differences, draft-invoice timing, later usage batches, and screenshots. Dedicated endpoint and SDK repositories remain the authority for complete schemas, version-specific behavior, error catalogs, idempotency, retries, lifecycle, and operational guarantees.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-usage-based-billing]], [[metronome-event-ingestion]], [[metronome-billable-metrics]], [[metronome-products-and-rate-cards]], [[metronome-customers-and-contracts]], [[metronome-invoicing]], [[metronome-api-idempotency]]
- Additional affected concepts: [[metronome-currencies-and-custom-pricing-units]], [[metronome-integrations]]
- Related sources: [[source-metronome-guides-get-started-developer-sdks]], [[source-metronome-api-reference-authentication]], [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/sdks-2026-07-13|2026-07-13 snapshot - complete four-language SDK usage-billing walkthrough, retry boundary, object flow, example conflicts, and raw implementation details]]
