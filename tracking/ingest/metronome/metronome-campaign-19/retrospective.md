# Metronome Campaign 19 Retrospective

## Outcome

- Final quality: five of five pages approved; fixed query audit passed 9/9 with no expansion.
- First-pass efficiency: zero of five pages approved on attempt 1, below the manifest target of at least four.
- Retry shape: three unchanged-hash targeted corrections and two full semantic corrections.
- Coordinator content repairs: zero.
- Elapsed time: 2,874 seconds, above the approximately 35-minute desirable target.

## Repeated causes

1. OpenAPI precision affected four pages: operation-level `requestBody` requiredness was conflated with required payload properties, or unspecified `additionalProperties` behavior was overstated.
2. API-wide POST idempotency was omitted on `disable-trueup-for-commit` and `search-events`, causing endpoint-specific unknowns to be stated too broadly.
3. The true-up source updated credits and commits but initially missed the separate invoicing concept and reciprocal link.

## Bounded change

Add three semantic reminders to the existing generated worker preflight:

- separate `requestBody`, payload-property, and `additionalProperties` semantics;
- check Metronome's API-wide POST idempotency authority before declaring retry behavior undocumented;
- audit every relevant existing concept for each durable fact and return reciprocal-link suggestions.

No validator, schema field, scheduler state, retry class, agent role, registry, or monitoring layer is added. Independent review remains mandatory because these checks require semantic judgment.

## Next measurement

Use the unchanged Campaign 19 throughput gates for the next separately approved five-page campaign. Do not expand to 8–10 pages unless first-pass approval and full-retry counts materially improve.
