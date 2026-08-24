# Metronome Campaign 22 Archetype v2 Pilot Plan

> **For agentic workers:** use the existing coordinator-controlled subagent workflow and apply `archetype-playbook.md` to one assigned source at a time.

**Goal:** Test whether claim-to-evidence closure, authority separation, and concept-impact sweep improve first-pass accuracy without adding campaign machinery.

**Architecture:** Existing Campaign v2 scheduling, result contracts, Sol workers, independent Sol reviewers, bounded retries, coordinator ownership, and close gates remain unchanged. The v2 checks exist only in this campaign-local playbook and introduce no state or output fields.

**Tech Stack:** Markdown campaign evidence, existing `manage_ingest_pilot.py` workflow, native Sol subagents, and existing wiki and capsule validators.

**Spec:** `tracking/ingest/metronome/metronome-campaign-22/archetype-playbook.md`

## Global constraints

- Status: **awaiting exact-manifest approval**.
- Selection used metadata only and does not authorize facts from unread raw bodies.
- No initialization, complete raw read, worker dispatch, canonical write, or campaign-state change occurs before exact approval.
- Five pages remain the hard limit; every attempt-1 candidate receives independent complete-source Sol review.
- Workers and reviewers remain repository-read-only; the coordinator remains the sole canonical and shared-file writer.
- No scheduler, schema, validator, registry, monitoring layer, model-routing rule, or production provider rule changes.

## Exact five-page selection

| # | Job | Lines | Preliminary archetype | Worker tier | Metadata-visible purpose |
| ---: | --- | ---: | --- | --- | --- |
| 1 | `get-a-product` | 441 | API Read | strong | Single-product retrieval selected for identity, response envelope, product state, reusable schemas, and read boundaries |
| 2 | `list-products` | 459 | API List / Schema | standard | Product collection selected for filters, pagination, returned item shape, ordering, and schema reuse |
| 3 | `archive-a-customer` | 180 | API Mutation | strong | Small archive mutation selected for requiredness, success state, idempotency, lifecycle, errors, and propagation |
| 4 | `non-monotonically-increasing-metrics` | 213 | Concept / Guide | strong | Metric guide selected for definitions, invariants, examples, ownership, and API-authority boundaries |
| 5 | `sfdc-integration` | 239 | Integration Guide | strong | Salesforce integration selected for identifier layers, setup, synchronization, lifecycle, and external-system boundaries |

Selection used only raw path, source URL header, first heading, line count, SHA-256, prior-manifest membership, and source-target absence. All five canonical source targets are absent.

`non-monotonically-increasing-metrics` appeared in closed negative Campaign 13 but remained `attempt 0`, `queued`, and undispatched with no attempt directory or candidate. Campaign 22 treats it as a new per-page-review job and may not reuse or resume Campaign 13 evidence.

## Worker and reviewer contract

1. The coordinator dispatches the generated trusted order and exact playbook path.
2. The worker reads the common coverage contract, assigned archetype, three v2 submission checks, and complete assigned raw.
3. The worker returns the unchanged Campaign v2 source, quotes, receipt, and shared-suggestion contract.
4. A different Sol reviewer independently reads the complete raw and applies the same checks.
5. Semantic, authority, contradiction, lifecycle, or concept-placement corrections receive full review; bounded unchanged-hash evidence corrections receive targeted review.
6. The coordinator does not perform a default third full-source review.

## Close and audit

Only reviewer-approved candidates may be promoted. The coordinator groups approved concept updates by exact target, writes each shared target once, derives company/index/log changes mechanically, and runs close validators once.

The immutable query sample is:

- standard short mutation: `archive-a-customer`;
- longest/schema-heavy page: `list-products`;
- ordinary cross-structure sample: `non-monotonically-increasing-metrics`.

Each receives factual retrieval, boundary or contradiction retrieval, and exact raw deep-dive tests. Any material partial or fail expands the semantic audit to all five pages.

## Measurement and decision

Campaign 22 demonstrates a v2 improvement only if final content passes, at least four of five pages pass attempt 1, no more than one full semantic retry occurs, and no concept/link defect expands the audit. Approximately 35 minutes or less to final reviewer approval remains desirable.

The retrospective compares Campaign 22 directly with Campaign 21's 0/5 first-pass approvals, four full semantic retry cycles, thirteen attempts, and approximately 44-minute review path. A failed result keeps the playbook campaign-local and triggers no additional machinery.

## Authorization boundary

Approval of the exact manifest authorizes initialization, complete reading of only these five raw pages, playbook-guided Sol workers, independent Sol reviewers, bounded retries, reviewer-approved promotion, and the fixed or expanded close audit. It does not authorize another page, Campaign 13 resumption, Terra or Luna routing, no-review execution, selective-ingest reclassification, a larger campaign, cross-provider rollout, production-rule changes, remote push, or unrelated-file modification.
