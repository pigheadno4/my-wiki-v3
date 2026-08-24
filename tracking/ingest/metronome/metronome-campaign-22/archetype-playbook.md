# Metronome Campaign 22 Archetype Playbook v2

## Purpose

This bounded pilot tests whether three submission checks improve first-pass accuracy for structurally similar payment-company documentation. The playbook guides complete raw reading, query-oriented source generation, and independent review. It is not a new campaign schema, routing registry, validator, or substitute for semantic judgment.

The source page remains a semantic index: retain the durable facts, boundaries, contradictions, concept routes, and raw deep-dive link needed for future queries without restating every raw field.

## Common coverage contract

Every worker and reviewer checks:

1. Documented purpose and safe query-routing use.
2. Core identities, state, required inputs and outputs, and durable behavior.
3. Important limits, explicitly undocumented behavior, and evidence boundaries.
4. Contradictions within the assigned raw or against existing authorities.
5. Fact-bearing concept placement and reciprocal source links.
6. Exact canonical URL, assigned raw file, and path-qualified `## Raw Sources` backlink.

`## Raw Sources` contains only pages read completely and used as factual evidence. Navigation-only pages belong under `## Related raw API references` and cannot support source facts.

## Three v2 submission checks

### 1. Claim-to-evidence closure

Before returning a result, map every query-critical source claim and every proposed shared durable fact to the selected `quote_indexes`. The cited exact raw excerpts must directly establish the complete retained statement. If the evidence establishes only part of a statement, narrow the statement rather than leave an unsupported extension.

Use three to five evidence excerpts. Prefer bounded contiguous passages covering the important facts; do not inflate the source into an exhaustive schema transcription merely to justify more claims.

### 2. Authority separation

Keep assigned-raw facts separate from facts supplied by existing source authorities. Attribute cross-source behavior to the authority that actually documents it, add that source under `## Related`, and preserve unresolved differences instead of synthesizing them away.

A related source or raw reference does not become evidence for the assigned page. In particular, do not attribute create, read, mutation, lifecycle, idempotency, delivery, payment, tax, settlement, accounting, or reconciliation behavior to an endpoint that does not establish it.

### 3. Concept-impact sweep

After identifying durable facts, inspect every relevant existing Metronome concept, not only the first plausible target. Each affected concept receives a bounded durable-fact suggestion and reciprocal source-link suggestion. Do not create a new concept when an existing concept already owns the topic, and do not update a concept merely because it is tangentially related.

## API Read

Check resource identity, authentication, path and query parameters, response envelope, required versus optional versus nullable fields, archived or deprecated state, errors, visibility, freshness, consistency, and read-after-write limits.

Do not infer lifecycle, retention, not-found behavior, ordering, authorization scope, or historical visibility merely because a response field exists.

## API List / Schema

In addition to API Read concerns, check filter defaults and interactions, cursor location, page-size limits, terminal cursor representation, ordering, cursor lifetime, snapshot consistency, archive inclusion, response-item required fields, reusable schemas, and example-versus-schema conflicts.

Absence of an OpenAPI `requestBody` documents no request schema; it does not prove runtime treatment of a supplied body. Keep endpoint-specific pagination distinct from API-wide conventions.

## API Mutation

Check operation-level request-body requiredness separately from payload-property requiredness, nested selectors, success identity and state, validation and error surfaces, API-wide idempotency versus resource uniqueness, concurrency, partial failure, retry and recovery, lifecycle transitions, and downstream propagation.

A successful mutation response does not prove invoice, payment, tax, accounting, export, webhook, or external-system completion unless the assigned raw explicitly establishes that result.

## Concept / Guide

Check definitions, prerequisites, actors and ownership, lifecycle progression, invariants, recommendations, worked examples, exceptions, and cross-reference authority. Separate durable rules from illustrative payloads, amounts, diagrams, and preferred practices.

A guide linking an API does not replace that API's exact request, response, error, or idempotency contract.

## Integration Guide

Check account, customer, contract, invoice, and external-provider identifiers; credentials and sensitive configuration; supported combinations; setup prerequisites; activation and readiness; delivery, payment, tax, settlement, and reconciliation boundaries; failure, retry, rotation, rollback, and operational ownership.

Configuration success or a returned identifier does not prove external acceptance, downstream delivery, payment, settlement, or reconciliation.

## Worker application

The worker reads this playbook and the complete assigned raw, applies the preliminary archetype from `routing_reason`, and returns the unchanged Campaign v2 result contract. A material archetype mismatch is reported before result generation. No new output field records the three checks; they are submission discipline only.

## Reviewer application

The independent reviewer reads the complete assigned raw and applies the same coverage and submission checks. Review asks whether every retained query-critical claim is accurate, directly grounded or correctly attributed, placed in every affected concept, and navigable back to immutable raw evidence.

Mechanical hash, URL, substring, schema, and link checks remain separate. A semantic, lifecycle, contradiction, authority, or concept-placement correction receives full review; an unchanged-hash evidence-only correction may receive targeted review.

## Pilot measurement

- Five independently approved pages remain the hard limit.
- At least four of five pages should pass attempt 1.
- No more than one full semantic retry should be required.
- No audit expansion should result from missing concept placement or backlinks.
- Approximately 35 minutes or less to final reviewer approval remains desirable, not a correctness gate.

Failure does not authorize another prompt layer, registry, schema field, validator, reviewer tier, larger campaign, or cross-provider rollout.
