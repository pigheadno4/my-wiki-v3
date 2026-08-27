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

This reference walkthrough uses Metronome's Python, Node.js, Ruby, and Go SDKs to connect an application to a basic usage-billing flow. It routes from client setup and usage ingestion through billable-metric, customer, product, rate-card, and contract creation to a draft invoice; its fixed worked chronology cannot be replayed unchanged, and it is not a complete SDK transport or underlying API contract.

## Query-critical facts

- The four SDKs advertise typed Metronome endpoints and objects, pagination support, and configurable automatic request retries. The page states a default of up to three retries after failure, but does not identify the retryable failure set, counting convention, backoff, jitter, timeout policy, method safety, or whether an SDK injects or preserves an API-wide `Idempotency-Key`.
- SDK clients use an API-key bearer token and default to `METRONOME_BEARER_TOKEN` when the token is omitted from the constructor. The page does not define token scope, environment isolation, rotation, expiry, or permissions; dedicated authorization sources remain controlling.
- The intended data path is usage event -> billable metric -> customer association -> usage product and rate-card price -> customer contract -> draft invoice. That path is conditional: the page's event must be accepted, sent after metric creation to match by default, associated with a customer, covered by a contract period, rated, and reflected on a draft before the claimed invoice outcome can be evaluated.
- One ingest request can carry up to 100 events. The page describes `transaction_id` as the event-level deduplication key, permits event timestamps up to 34 days in the past, accepts a Metronome ID or application-defined customer identifier, and leaves `event_type` plus arbitrary `properties` to the producer. It does not define changed-payload collisions, partial-batch outcomes, or how generic SDK retries interact with event deduplication; the dedicated idempotency authority limits duplicate suppression to 34 days.
- A billable metric filters events, selects a property to aggregate, supports the documented `SUM`, `COUNT`, and `MAX` operations, and can group results for invoice presentation. The page states that metrics match only events sent after metric creation; it does not define reflow, propagation latency, correction, or metric-mutation behavior.
- An ingest alias can join application-owned customer identity to usage sent before the Metronome customer is provisioned. The example then connects a usage product to the metric, applies quantity conversion and presentation grouping, creates a reusable rate card, and creates a customer contract from that card; dedicated endpoint references remain authoritative for required fields, lifecycle, validation, and recovery.
- The rate example says USD values use cents while other currencies use whole units, and it uses effective dates for price evolution. The contract prose says periods after `starting_at` generate invoices and current-period draft line items update seconds after usage arrives; neither statement is a service-level, finalized-invoice, downstream delivery, collection, tax, accounting, or reconciliation guarantee.

## Material boundaries and conflicts

> [!warning] Stale usage chronology breaks the worked flow
> Every usage payload shown by this snapshot is dated in August 2024: the initial and post-metric events use August 1, and the final batch uses August 15, 16, and 17. The page was fetched July 13, 2026 and itself permits historical ingestion only up to 34 days, so none of those payloads can be ingested unchanged at snapshot time. Replace every timestamp with a current, non-future value inside the rolling window and preserve unique transaction IDs before expecting acceptance, metric matching, customer association, rating, or a running draft invoice. The page's unqualified narration that the event entered Metronome, matched, and reached invoice totals is historical illustration, not a reproducible result for the literal payloads.

> [!warning] Go sequence does not establish the narrated invoice outcome
> The Go metric omits `group_keys`, although the walkthrough says `user_id` is the metric group key, the Go product sets `PresentationGroupKey` to `user_id`, and the final invoice narration relies on previously applied group keys. The Go contract also starts September 1, 2024 after every shown usage event, while the other languages start August 1 and the prose says invoices cover periods after `starting_at` and previously sent usage was applied. As written, the Go sequence does not establish either application of the shown August usage to its contract or the claimed user-grouped invoice presentation. Confirm the current Go call shape, add the required metric grouping when applicable, and use temporally valid events that occur after metric creation and within the contract's billable period before treating the outcome as demonstrated.

- Automatic SDK retries are a transport policy, not proof that a repeated mutation is safe. Event `transaction_id` deduplication is distinct from the API-wide `Idempotency-Key` contract for POST operations, and this page does not establish whether retry attempts retain either identity or how to recover after an ambiguous result.

> [!warning] Parallel canonical route and stale wiki caveats
> The wiki already contains [[source-metronome-guides-get-started-developer-sdks]], a separately canonicalized summary of the same broad walkthrough under `/guides/get-started/developer-sdks`. Its Ruby client-variable caveat still applies: this snapshot initializes `metronome` and uses it for the first Ruby ingest call, then switches to `client` in later Ruby snippets. Its Node namespace caveat does not apply to this snapshot, whose shown Node calls use `client.v1`; its treatment of the fixed timestamps as merely illustrative also understates the stale-ingest and Go contract-period conflicts identified here. Do not claim that either canonical supersedes the other without collection or upstream authority.

## Raw-detail coverage map

Use the complete raw snapshot for all four installation commands and client constructors; SDK repository links; bearer-token setup; generic SDK feature wording; every Python, Node.js, Ruby, and Go call shape; all stale August 1, 15, 16, and 17 usage timestamps, their unique transaction IDs, and the page's 34-day historical-ingest limit; usage payload fields, batching, screenshots, and narrated acceptance and matching claims; billable-metric filters, aggregation fields, language-specific grouping difference, forward-only matching statement, and examples; customer creation and alias association; product types, presentation grouping, quantity conversion, and external-item note; rate-card creation, entitlement, flat and tiered rates, denomination, and effective dates; the August-versus-September contract-start difference, post-start billing-period prose, draft-invoice timing, final usage batches, grouping claim, and screenshots. Dedicated endpoint and SDK repositories remain authoritative for complete schemas, version-specific behavior, error catalogs, idempotency, retries, lifecycle, and operational guarantees.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-usage-based-billing]], [[metronome-event-ingestion]], [[metronome-billable-metrics]], [[metronome-products-and-rate-cards]], [[metronome-customers-and-contracts]], [[metronome-invoicing]], [[metronome-api-idempotency]]
- Additional affected concepts: [[metronome-currencies-and-custom-pricing-units]], [[metronome-integrations]]
- Related sources: [[source-metronome-guides-get-started-developer-sdks]], [[source-metronome-api-reference-authentication]], [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/sdks-2026-07-13|2026-07-13 snapshot - complete four-language SDK walkthrough, stale event chronology, Go lifecycle and grouping conflicts, retry boundary, and raw implementation details]]
