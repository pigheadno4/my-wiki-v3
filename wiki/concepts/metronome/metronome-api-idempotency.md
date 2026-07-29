---
title: "Metronome API Idempotency"
type: concept
category: technology
tags: [metronome, api, idempotency, retries]
---

## Definition

Metronome uses several idempotency mechanisms rather than one universal key. The correct mechanism depends on whether a client is ingesting usage, associating customers, creating a resource with a supported uniqueness field, or retrying a POST request.

## Mechanisms

| Mechanism | Scope | Duplicate or conflict behavior | Documented lifetime |
| --- | --- | --- | --- |
| `transaction_id` | Usage events sent through `/ingest` or Segment | Later events with the same ID are ignored | 34 days |
| Ingest alias | Customer writes and usage attribution | An alias already assigned to a customer conflicts until it is removed | Until released |
| `uniqueness_key` | Supported resource-creation endpoints | Reuse returns HTTP `409 Conflict` | Until released; the overview notes release is available only for alerts |
| `Idempotency-Key` | All POST endpoints | Identical parameters return the original result; changed parameters return HTTP `409 Conflict` | At least 24 hours |

The documented `uniqueness_key` examples include contracts, alerts, and customer-level commits and credits. The source labels contract-edit support as coming soon, so support should be verified against the specific endpoint rather than inferred for all writes.

## Retry and error boundary

Metronome persists an `Idempotency-Key` result after a request begins execution—that is, after validation and concurrent-request conflict checks. The cached result can be an HTTP `500` error. Reusing that key returns the cached error, so the source recommends investigating system state and deciding whether to resolve manually or retry instead of automatically switching keys after a partial failure.

The best-practice guidance recommends deterministic keys derived from business identity and operation type for resource operations, UUIDs where deterministic identity is unnecessary, exponential backoff, and reuse of the same key within its lifetime. The separate status-code reference advises verifying that a resource was not partially created after a `5XX` response, but its suggestion to retry with a different key must be reconciled with the idempotency page's manual-investigation warning for cached errors.

## Related platform concepts

- [[metronome-event-ingestion]] owns the usage-event schema, matching, deduplication, and processing boundaries.
- [[metronome-customers-and-contracts]] owns ingest-alias assignment and resource lifecycle.
- [[metronome-credits-and-commits]] covers uniqueness keys on credit and commit creation.

## Sources

- [[source-metronome-api-reference-idempotency]] — mechanism selection, key lifetimes, conflict behavior, cached errors, and retry guidance
- [[source-metronome-api-reference-status-codes]] — API-wide conflict, rate-limit, and server-error recovery guidance

## Related

- [[metronome]]
- [[metronome-security-principles]]
