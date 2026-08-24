# Metronome Campaign 21 Archetype Playbook

## Purpose

This pilot standardizes how structurally similar technical documentation is read, summarized, and reviewed. It is a coverage guide for raw-to-source transformation, not a new campaign schema, routing registry, or substitute for complete raw-page reading and independent semantic review.

The source page remains a query-oriented semantic index. It should preserve the durable facts, boundaries, contradictions, and navigation needed to decide when a future query must deep-dive into the immutable raw page. It does not need to restate every raw field.

## Common coverage contract

Every worker and reviewer checks these six information classes. Heading names may vary when a clearer source structure exists; these are coverage obligations, not a mandatory prose template.

1. Documented purpose and safe query-routing use, without inventing a recommendation.
2. Core durable behavior, identities, state, and required inputs or outputs.
3. Important boundaries, explicitly undocumented behavior, and evidence limits.
4. Contradictions within the page or against existing source and concept authorities.
5. Fact-bearing concept placement and reciprocal source links.
6. Exact canonical URL, assigned raw file, and path-qualified `## Raw Sources` backlink.

`## Raw Sources` contains only raw pages read completely and used as factual evidence. Navigation-only material remains under `## Related raw API references` and cannot support source facts.

## API Read

Check resource identity, path and query parameters, authentication, response envelope, required versus optional versus nullable response fields, archived or deprecated state, errors, visibility, freshness, consistency, and read-after-write limits.

Do not infer lifecycle, retention, not-found behavior, ordering, authorization scope, or historical visibility merely because a response field exists.

## API List / Schema

In addition to API Read concerns, check filter defaults, cursor location, page-size limits, terminal cursor representation, ordering, cursor lifetime, snapshot consistency, archive inclusion, response-item required fields, union or discriminator behavior, and example-versus-schema conflicts.

Absence of an OpenAPI `requestBody` documents no request schema; it does not prove how a runtime handles a supplied body. Endpoint-specific pagination must not be flattened into an API-wide convention.

## API Mutation

Check operation-level request-body requiredness separately from payload-property requiredness, nested selectors and mutual exclusions, success identity and state, validation and error surfaces, API-wide idempotency versus resource uniqueness, concurrency, partial failure, retry and recovery, lifecycle transitions, and downstream propagation.

Do not convert a successful mutation response into proof of invoice, payment, tax, accounting, export, webhook, or external-system completion unless the raw page explicitly establishes that outcome.

## Concept / Guide

Check definitions, prerequisites, actors and ownership, lifecycle or state progression, invariants, recommendations, worked examples, exceptions, and cross-reference authority. Separate a durable rule from illustrative payloads, amounts, diagrams, and preferred practices.

Preserve differences between product behavior and merchant-owned policy. A guide that links an API does not replace that API's exact request, response, error, or idempotency contract.

## Integration Guide

Check account, customer, contract, invoice, and external-provider identifier layers; credentials and sensitive configuration; supported provider or method combinations; setup prerequisites; activation and readiness; delivery, payment, tax, and reconciliation boundaries; failure, retry, rotation, rollback, and operational ownership.

Configuration success or a returned identifier does not prove downstream readiness, external acceptance, delivery, settlement, or reconciliation.

## Worker application

The manifest `routing_reason` names the preliminary archetype. The worker reads this playbook and then the complete assigned raw page. If the full page materially belongs to another archetype, the worker reports the mismatch to the coordinator before producing a result; the coordinator supplies the corrected playbook section without changing campaign state or result schema.

The worker returns the existing Campaign v2 result contract unchanged. Archetype coverage appears in the source candidate, grounding quotes, unknowns, contradictions, and concept suggestions rather than in new JSON fields.

## Reviewer application

The independent reviewer reads the complete raw page and uses the same common and archetype-specific coverage contract. Review asks whether the candidate enables accurate fact retrieval, preserves query-critical limits, and navigates back to exact raw evidence. It does not demand exhaustive field transcription or reject a candidate merely for using different headings.

Mechanical hash, URL, quote, schema, and link checks remain separate. Archetype guidance narrows semantic attention; it does not replace semantic judgment.

## Pilot measurement

- Five independently approved pages remain the campaign limit.
- At least four of five pages should pass on attempt 1.
- No more than one full semantic retry should be required.
- No audit expansion should be caused by missing concept placement or backlinks.
- Approximately 35 minutes or less remains desirable, not a correctness gate.

The retrospective attributes review defects to the applicable archetype information class. Success may justify a later small provider-rule update. Failure does not authorize a registry, new schema, additional reviewer layer, or larger campaign.
