# Metronome Campaign 23 Minimum Sufficient Source playbook

## Purpose

This bounded playbook tests whether a source can remain a reliable query
router without reconstructing its complete raw page. Raw remains complete
evidence, source preserves query-critical durable knowledge and navigation,
and concepts preserve cross-source synthesis. This playbook adds no routing
state, schema field, validator, scheduler, or hard content-size limit.

## Minimum Sufficient Source contract

Every candidate preserves:

1. a concise overview of page purpose and scope;
2. the durable facts needed to select the page and avoid a materially wrong
   integration decision;
3. material boundaries or contradictions;
4. a coverage map routing detailed schemas, enums, examples, errors, SQL, or
   setup steps to the exact raw page;
5. primary concept links; and
6. canonical URL, `raw_files`, and an exact path-qualified raw backlink.

Three to seven facts, one to three boundaries, and one to three primary
concepts are normal semantic ranges, not acceptance caps. Include more only
when the page purpose requires it. Do not copy fields merely to fill a quota.

## Primary versus secondary concepts

A primary concept directly defines the page purpose, operation, lifecycle, or
integration outcome; omitting it would impair a realistic query. A secondary
concept represents an optional field, incidental schema surface, or tangential
capability that exact raw navigation can cover safely.

Workers must identify primary concepts. They may return secondary suggestions,
but a missing secondary concept does not fail the candidate or consume a retry.

## Coverage map and raw evidence boundary

The coverage map names detail categories present in the assigned raw; it does
not summarize every item. `Raw Sources` contains only pages read completely and
used as evidence. An unread navigation page belongs under
`Related raw API references` and cannot support a source claim.

## API Read overlay

Preserve object identity, lookup purpose, key locator, returned state,
time-view or history semantics, and material visibility or consistency
boundaries. Route complete schemas, nullable fields, examples, and error
catalogs to raw. Separate request-body requiredness from required properties
inside a supplied payload.

## API List / Schema overlay

Preserve collection scope, principal filters and pagination, documented
ordering or time windows, completeness limits, and material schema/example
conflicts. Route the full filter, cursor, enum, and object catalogs to raw. Do
not infer a closed schema without explicit `additionalProperties: false`.

## API Mutation overlay

Preserve preconditions, principal state transition, observable result, and
material lifecycle, financial, failure, propagation, retry, concurrency, or
idempotency semantics established by official authority. Route the full
payload and error catalog to raw. Keep API-wide POST idempotency distinct from
endpoint-specific state and recovery behavior.

## Concept / Guide overlay

Preserve the definition, principal actors, lifecycle or data flow, decision
points, material integration limits, and important conflicts. Route long
worked examples, variants, calculations, and operational walkthroughs to raw.
Do not elevate a product guide into legal, accounting, or compliance authority.

## Integration Guide overlay

Preserve the integration outcome, system boundary, responsibility split,
identity mapping, state or data flow, recovery behavior, and relevant
environment scope. Route detailed setup steps, UI paths, payloads, optional
settings, and troubleshooting to raw. Do not turn Metronome documentation into
a complete guarantee of the external platform.

## Worker submission check

Before returning the unchanged Campaign v2 result, confirm each core fact and
material boundary is accurate and grounded, every primary concept is routed,
the coverage map exposes central raw-detail categories, and the canonical/raw
links are exact. Quotes ground retained claims; they do not need to reproduce
every raw schema table.

## Reviewer blocking defects

Return `changes_requested` only for a core factual error; a material omission
affecting integration, amount, state, lifecycle, or failure treatment; an
authority error; a missing material contradiction; a missing or incorrect
primary concept; a broken evidence route; or a coverage-map omission hiding an
entire detail category central to page purpose.

## Reviewer non-blocking coordinator actions

Approve when remaining work is limited to a secondary concept, ordinary raw
detail, non-material wording/formatting, a mechanically repairable quote range,
or company/index/log work. Record the bounded follow-up in the existing review
`reason` and decide existing shared update IDs normally. Do not add a
`coordinator_actions` result field.

## Retry scope

Use targeted review only when the raw hash is unchanged and the complete prior
review enumerated a bounded local correction. Use full review for core
misunderstanding, material omission, authority confusion, new factual meaning,
or unresolved contradiction. Secondary issues do not consume an attempt.

## Pilot measurement

Record first-pass approvals, bounded and full retries, attempts, review scope,
elapsed time, fixed query results, exact raw deep dive, and primary-concept
reciprocity in existing campaign evidence. The five-page limit and comparison
with Campaigns 20 through 22 guide the decision; no measurement becomes a new
validator rule.
