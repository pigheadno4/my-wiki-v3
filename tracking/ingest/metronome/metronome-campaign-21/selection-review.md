# Metronome Campaign 21 Archetype Pilot Plan

> **For agentic workers:** REQUIRED SUB-SKILL: use the existing coordinator-controlled subagent workflow and apply `archetype-playbook.md` to one assigned source at a time.

**Goal:** Test whether a shared raw-to-source coverage contract plus five document-archetype checklists improves first-pass accuracy, review focus, and cross-provider generality without adding campaign machinery.

**Architecture:** The existing Campaign v2 scheduler, result contracts, Sol workers, independent Sol reviewers, retry policy, coordinator ownership, and close gates remain unchanged. Preliminary archetypes live only in this selection review and each job's existing `routing_reason`; workers and reviewers read the campaign-local playbook, while canonical source, concept, raw-link, company, index, and log behavior stays under the current ingest rules.

**Tech Stack:** Markdown campaign evidence, existing `manage_ingest_pilot.py` Campaign v2 workflow, native Sol subagents, existing wiki and capsule validators.

**Spec:** `tracking/ingest/metronome/metronome-campaign-21/archetype-playbook.md`

## Global constraints

- Status: **awaiting exact-manifest approval**.
- Metadata-only selection does not authorize facts from unread raw bodies.
- No campaign initialization, full raw read, worker dispatch, canonical write, or campaign-state change occurs before exact approval.
- Five pages remain the hard campaign limit; all first attempts receive independent complete-source Sol review.
- The archetype playbook changes reading and review attention only. It adds no registry, schema field, validator, scheduler state, monitoring layer, model-routing rule, or reviewer tier.
- Workers and reviewers remain repository-read-only; the coordinator remains the sole canonical writer.

## Exact five-page selection

| # | Job | Lines | Preliminary archetype | Worker tier | Metadata-visible purpose |
| ---: | --- | ---: | --- | --- | --- |
| 1 | `get-an-invoice` | 1,025 | API Read | strong | Long schema-heavy single-resource read for invoice identity, envelope, state, nested line items, and response boundaries |
| 2 | `list-customers` | 288 | API List / Schema | standard | Paginated collection baseline for filters, item shape, ordering, cursor, and archive visibility |
| 3 | `update-a-customer-name` | 189 | API Mutation | strong | Small mutation for wrapper and payload requiredness, success state, idempotency, errors, and propagation wording |
| 4 | `how-invoicing-works` | 244 | Concept / Guide | strong | Conceptual lifecycle page for definitions, invoice types and states, examples, invariants, ownership, and API boundaries |
| 5 | `aws-marketplace-integration` | 297 | Integration Guide | strong | Marketplace guide for identifier layers, credentials, setup readiness, delivery, payment, and reconciliation boundaries |

Selection used only raw path, source URL header, first heading or introductory metadata, line count, SHA-256, prior-manifest membership, and source-target absence. Except for `how-invoicing-works`, none appeared in an earlier campaign manifest and none has a canonical source target.

`how-invoicing-works` appeared in the closed negative Campaign 13 manifest but remained `attempt 0`, `queued`, and undispatched; no attempt directory or candidate exists. Campaign 21 would process it as a new per-page-review job. Approval does not resume Campaign 13, reuse any Campaign 13 result, or restore its invalid `audit_only` policy.

## Worker and reviewer contract

1. The coordinator dispatches the generated trusted order and the exact campaign-local playbook path.
2. The worker reads the common contract, the preliminary archetype section, and the complete assigned raw page.
3. A material archetype mismatch is reported before result generation; it is corrected through coordinator instruction without adding state or result fields.
4. The worker returns the unchanged Campaign v2 candidate, quotes, receipt, and concept-suggestion contract.
5. A different Sol reviewer reads the complete raw page and applies the same common and archetype coverage contract.
6. Targeted review remains limited to bounded unchanged-hash corrections; factual, lifecycle, contradiction, cross-source, or concept-placement corrections receive full review.

## Close and audit

The coordinator promotes only reviewer-approved candidates, groups approved concept changes by target, updates shared catalogs once, and runs existing close validators once. It does not perform a default third full-source read.

The immutable query sample is:

- standard page: `list-customers`;
- longest/schema-heavy page: `get-an-invoice`;
- ordinary cross-structure sample: `how-invoicing-works`.

Each receives factual retrieval, boundary or contradiction retrieval, and exact raw deep-dive tests. A material partial or fail expands the audit to all five pages.

## Measurement and decision

Campaign 21 succeeds as an archetype pilot only if final content passes and the worker/reviewer process reaches at least four of five first-attempt approvals with no more than one full semantic retry. Missing-link audit expansion is a failure. Approximately 35 minutes or less is desirable.

The retrospective records defects by common or archetype-specific information class. A successful result may support one small provider-rule update that embeds the proven playbook. A failed result keeps the five-page cap and triggers reconsideration of per-page source economics; it does not authorize more prompt layers or infrastructure.

## Authorization boundary

Approval of the exact manifest authorizes initialization, complete reading of only these five raw pages, playbook-guided Sol workers, independent playbook-guided Sol reviewers, bounded retries, reviewer-approved promotion, and the fixed or expanded close audit. It does not authorize another page, a model comparison, Terra or Luna production routing, no-review execution, selective-ingest reclassification, an 8–10 page expansion, Campaign 13 resumption, cross-provider rollout, or remote push.
