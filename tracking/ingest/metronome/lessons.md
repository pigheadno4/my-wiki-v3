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

## API Mutation

- Check the API-wide POST idempotency authority before declaring repeated-call
  behavior wholly undocumented, while keeping endpoint-specific state,
  concurrency, and recovery unknowns separate. Seen in Campaigns 19 and 22.

## Concept / Guide

- A worked amount, transition, or example retained as a query-critical fact
  needs direct quote coverage; otherwise narrow the summary and route the
  worked detail to raw. Seen in Campaigns 21 and 22.

## Integration Guide

- Separate Metronome-documented configuration and identifiers from external
  acceptance, delivery, payment, settlement, or reconciliation guarantees.
  Seen in Campaigns 21 and 22.
