---
title: "Metronome API Idempotency"
type: source
date_ingested: 2026-07-30
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/idempotency"
raw_files:
  - "metronome/api-reference/idempotency-2026-07-13.md"
tags: [metronome, api, idempotency, retries, event-ingestion]
---

## Overview
This API reference defines Metronome's idempotency mechanisms for safely retrying writes without creating duplicate data. The documented mechanism depends on the data being written: usage events use `transaction_id`, customer writes use ingest aliases, select resource-creation endpoints accept `uniqueness_key`, and POST requests can use `Idempotency-Key`.

## Key takeaways
- Accepted usage events with the same `transaction_id` are ignored for 34 days, allowing a sender to retry an event without duplication.
- An ingest alias cannot be moved between customers until it has been removed from the original customer, including when that customer is archived.
- A `uniqueness_key` is stored with the resource; attempting to reuse it returns HTTP `409 Conflict`. The documented examples are contracts, alerts, customer-level commits and credits, and future contract edits.
- `Idempotency-Key` is supported on all POST endpoints. A retry with the same key and identical parameters returns the original result, whereas changed parameters return HTTP `409 Conflict`.
- POST idempotency keys are retained for at least 24 hours, and a cached result can be an HTTP 500 error. An error therefore needs investigation before retrying with a different key.

## Mechanism selection and retry behavior
The source distinguishes resource identity from request-result caching. For event ingestion, `transaction_id` is the idempotency key. For customer provisioning, an ingest alias naturally prevents duplicate entities and conflicting records. For a select set of created resources, use the request-body `uniqueness_key` when the endpoint supports it.

For POST endpoints without a dedicated uniqueness key, send `Idempotency-Key`. Metronome persists the result only after the request begins execution, meaning it has passed validation and does not conflict with another concurrent request. The same key must be reused with identical parameters to receive the original result.

## Error and lifetime boundary
Metronome caches an error returned by an `Idempotency-Key` request and returns that error on subsequent retries using the same key. The source recommends investigating the system state and deciding whether to retry or resolve manually, rather than automatically changing a key after a partial failure.

The documented retry windows differ by mechanism: usage events can be retried within 34 days, while REST API writes using the header have at least a 24-hour retention period. The page recommends deterministic resource keys derived from business data and operation type, UUIDs where deterministic keys are unnecessary, exponential backoff, and reuse of the same retry key.

## Related
- Companies: [[metronome]]
- Concepts: [[metronome-api-idempotency]], [[metronome-event-ingestion]], [[metronome-customers-and-contracts]]
- Related sources: [[source-metronome-api-reference-usage-ingest-events]], [[source-metronome-api-reference-contracts-create-a-contract]]

## Raw Sources
- [[raw/metronome/api-reference/idempotency-2026-07-13|2026-07-13 snapshot — API-wide idempotency mechanisms and retry behavior]]
