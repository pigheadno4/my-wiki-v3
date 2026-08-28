# Metronome ingestion lessons

This coordinator-owned file records repeated ingest-process failures, not
Metronome product facts. Add a lesson only after it appears on at least two
different pages. Workers and reviewers read only their assigned archetype
section. Replace or delete obsolete checks instead of accumulating variants.

## API Read

- Separate OpenAPI request-body requiredness from required properties inside a
  supplied payload. A required identifier in the payload does not prove the
  request body itself is required. Seen in Campaigns 19 and 22.

## API List / Schema

- Do not describe a documented property set as closed unless
  `additionalProperties: false` is explicit; unknown-property runtime behavior
  otherwise remains undocumented. Seen in Campaigns 19 and 20.
- Verify schema nesting and identity keys before attributing an expanded child
  record to a sibling balance, group, or reconciliation result. Object-level
  requiredness also does not prove a nested property is required. Seen on
  Manage Seats in Campaign 24 and List Seat Balances in Campaign 25.

## API Mutation

- Check the API-wide POST idempotency authority before declaring repeated-call
  behavior wholly undocumented, while keeping endpoint-specific state,
  concurrency, and recovery unknowns separate. Seen in Campaigns 19 and 22.
- When an endpoint, guide, OpenAPI schema, or API-wide authority disagrees on a
  name, field, or supported behavior, preserve the conflict and its scopes;
  do not silently select one as runtime truth. Seen on Edit Contract in
  Campaigns 17 and 25.

## Concept / Guide

- A worked amount, transition, or example retained as a query-critical fact
  needs direct quote coverage; otherwise narrow the summary and route the
  worked detail to raw. Seen in Campaigns 21 and 22.
- When a worked example is governed by a rolling historical or freshness
  window, compare its literal timestamps with the raw snapshot date before
  describing it as runnable. Preserve any stale-example contradiction and the
  required substitution. Seen on API Quickstart in Campaign 24 and SDKs in
  Campaign 25.

## Integration Guide

- Separate Metronome-documented configuration and identifiers from external
  acceptance, delivery, payment, settlement, or reconciliation guarantees.
  Seen in Campaigns 21 and 22.
