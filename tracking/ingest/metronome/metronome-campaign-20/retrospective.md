# Metronome Campaign 20 Retrospective

## Outcome

- Final quality: five of five pages approved; the fixed query audit passed 9/9 with no expansion.
- First-pass efficiency: zero of five pages approved on attempt 1, below the target of at least four.
- Retry shape: twelve worker attempts and twelve reviews — nine full and three targeted.
- Coordinator content repairs: zero.
- Elapsed time: 3,464 seconds (57 minutes 44 seconds), above the approximately 35-minute desirable target.

## What the preflight changed

Campaign 20 gave every worker the three Campaign 19 reminders: distinguish request-wrapper and payload-schema semantics, check API-wide POST idempotency, and audit every relevant concept. These reminders did not materially improve first-pass approval or elapsed time. They prevented some older omissions, but reviewers still found page-specific schema, evidence, contradiction, and concept-placement defects.

## Defect pattern by document archetype

- API Read: response nullability, required envelopes, archive visibility, and exact concept anchors.
- API List/schema: absence of a request schema versus runtime behavior, pagination boundaries, examples that conflict with schemas, and reusable response maps.
- API List/schema-heavy: union and envelope mapping, endpoint-specific versus global conventions, lifecycle visibility, cross-authority enums, and evidence for absence claims.
- API Mutation: wrapper versus payload requiredness, nested selector logic, error surfaces, resource uniqueness versus request replay, and lifecycle or propagation unknowns.
- Integration Setup + Mutation: provider enums, secret-bearing open configuration, returned identity layers, provider-side effects, readiness, and reconciliation boundaries.

The independent close audit found that the final sources preserve these distinctions and passed the fixed query sample. The archetype annotations explain the retries; they do not justify a new registry, schema, or validation framework.

## Decision

Do not expand the next campaign to 8–10 pages. Keep the five-page cap and independent semantic review. For a future separately approved campaign, add only a small archetype-specific reading checklist to the existing worker order, derived from the five bullets above, and measure first-pass approval again. Do not change campaign state, create a routing registry, or add another monitoring layer.
