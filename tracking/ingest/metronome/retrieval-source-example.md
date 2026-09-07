# Retrieval-oriented source example: List Custom Field Keys

Status: design example only; the canonical source remains unchanged. The assigned 2026-07-13 raw was read in full for this example. Existing canonical source warnings supply context for the known cross-document conflict below; this is not a fresh revalidation of the pagination authority.

## Before and proposed treatment

| Current source content | Proposed treatment |
| --- | --- |
| Purpose, active key definitions, entity filtering | Keep |
| Organization-wide completeness uncertainty repeated in multiple sections | Avoid the unsupported organization-wide assertion; keep scope conservative |
| Detailed field requiredness, open-object semantics, enum count | Route to OpenAPI fields and schema in raw |
| API-wide idempotency explanation plus endpoint recovery unknowns | Related authority link, without claiming endpoint-specific behavior |
| Pagination conflict repeated in facts, boundaries, and coverage map | One scoped warning and two evidence routes |
| Multiple concept fact paragraphs | Main custom-fields reciprocal navigation; semantic edits only if existing concept meaning changes |

## Proposed source body

The following fenced text illustrates the body only. Existing canonical URL and exact raw_files provenance remain required in frontmatter.

```markdown
## Overview

Documents `POST /v1/customFields/listKeys` for discovering active custom-field key definitions, optionally filtered by entity type. Useful when finding available keys before assigning values or inspecting custom-field configuration.

## Key facts

- Lists key definitions, rather than values assigned to individual entity instances.
- Supports entity-type filtering and paginated results. Request fields, result structure, and entity identifiers are in the raw OpenAPI reference.

## Implementation attention

The existing pagination source and this endpoint reference describe pagination parameters differently. Check both before implementing pagination; this summary does not resolve the accepted page-size parameters or limits. See [[source-metronome-api-reference-pagination]] and the raw snapshot below.

## Find details in raw

- Endpoint request and response: `paths → /v1/customFields/listKeys → post` in the OpenAPI block.
- Entity filter values: `components → schemas → ManagedEntity`.
- Pagination cursor: `components → parameters → NextPage`, plus the operation's response schema.

## Related

- Company: [[metronome]]
- Main concept: [[metronome-custom-fields]]
- Custom-field behavior and mutation navigation: [[source-metronome-api-reference-custom-fields]]
- General POST retry rules: [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/custom-fields/list-custom-field-keys-2026-07-13|List custom field keys — exact request, response, entity enum, and cursor evidence]]
```

## Example reciprocal concept suggestion

Under the existing custom-fields concept's source navigation:

```markdown
- [[source-metronome-api-reference-custom-fields-list-custom-field-keys]] — discover active key definitions by entity type; request, response, and pagination evidence.
```

## Acceptance examples

- "Where can I find the API for discovering keys before setting values?" must reach this source and its raw.
- "What fields are returned for each key?" must reach the operation response schema, then read the raw to answer.
- Calling this an organization-wide inventory is a factual blocker. Narrowing that wording without changing the rest of the source can receive targeted review.
- Omitting the full ManagedEntity enum from the source is acceptable because the named raw route finds it directly.
- Omitting every API-wide replay condition is acceptable while the source makes no replay guarantee and routes that question to its authority.
- Removing the known pagination warning while adding an unqualified parameter or limit claim is a blocker.

This example demonstrates a smaller claim surface. It does not establish production quality or speed until the proposed five-page retrieval evaluation is run.
