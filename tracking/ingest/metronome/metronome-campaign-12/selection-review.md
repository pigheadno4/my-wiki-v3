# Metronome Campaign 12 Selective-Ingest Pilot Review

Status: pending exact-manifest approval

Manifest: [manifest.json](manifest.json)

This is an uninitialized six-page classification proposal for a bounded
selective-ingest pilot. Selection used canonical URLs, documentation hierarchy,
inventory metadata, immutable paths and hashes, and source-target absence. No
selected raw body was read in full, no pilot task has been dispatched, and
ingestion has not started.

## Exact classifications

| Order | Job | Initial disposition | Pilot action | Native task |
| ---: | --- | --- | --- | --- |
| 1 | `custom-fields-overview` | `source_required` | `generate_source` | Sol overview worker, then independent Sol review |
| 2 | `create-custom-field-key` | `raw_reference` | `audit_raw_reference` | One complete Sol audit read; no source generation |
| 3 | `delete-custom-field-key` | `semantic_triage` | `review_triage` | Sol triage worker, then independent Sol decision review; no source generation |
| 4 | `list-custom-field-keys` | `raw_reference` | `navigation_only` | None |
| 5 | `set-custom-field-values` | `semantic_triage` | `record_only` | None |
| 6 | `delete-custom-fields` | `semantic_triage` | `record_only` | None |

The pilot has three simultaneous initial native tasks and at most five complete
reads: two for overview generation and review, one for the create-key
raw-reference audit, and two for delete-key semantic triage and review. All five
agents are Sol.

## Fixed quality queries

1. `What are Metronome Custom Fields and what role does the overview document establish?` — must answer from the overview source.
2. `What exact request fields are needed to create a custom-field key?` — must route to and completely read create-key raw; the overview must not supply the schema.
3. `What happens to existing values when a custom-field key is deleted?` — must route to delete-key raw and state only what that raw supports.

## No-expansion rule

A material partial or failure in an audit, review, or fixed query records a
pilot miss and sets the eventual pilot verdict to revise. It does not expand
the pilot into reading the other three endpoint pages or retry a delete-key
classification disagreement. A disagreement promotes delete-key's future
disposition to `source_required` once, without generating its source in this
pilot.

## Approval boundary

Approval authorizes only the three selected pilot tasks. It does not authorize
source generation for the five endpoint pages, initialize the production
campaign scheduler, or create the cross-provider routing registry.

Until explicit approval, do not create a monitor, agent order, attempt, source
candidate, canonical wiki change, or ingest log entry, and do not dispatch any
pilot agent.
