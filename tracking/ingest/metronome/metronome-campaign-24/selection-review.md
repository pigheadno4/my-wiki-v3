# Metronome Campaign 24 confirmation proposal

**Status:** Awaiting exact-manifest approval
**Mode:** Eight-page dry-run campaign with per-page independent review
**Source baseline:** 225 canonical raw pages, 137 source pages, 94 raw pages without source summaries

## Goal

Confirm Campaign 23's Minimum Sufficient Source result at a moderately larger
scale while exercising the newly approved operational optimizations: automatic
review-order persistence and serial incremental promotion immediately after an
individual approval. This campaign does not change the source contract, model
routing, result schema, retry policy, validators, or coordinator ownership.

Eight pages are large enough to keep the three native-agent slots cycling
through workers and reviewers, but intentionally remain below a ten-page bulk
campaign. All workers and reviewers use strong Sol models. Every first attempt
still receives a complete-source review by a different agent.

## Metadata-only selection

Selection used raw path, line count, SHA-256, canonical source URL, prior
campaign membership, source-target absence, and the capsule pending list. No
selected raw body was read to prepare this proposal. All eight raw paths remain
in the 94-page pending list, and every declared source target is absent.

| Job | Archetype | Lines | Prior campaign state | Purpose |
| --- | --- | ---: | --- | --- |
| `get-the-rate-schedule-for-a-contract` | API Read | 504 | none | Longest/schema-heavy sample |
| `list-credit-ledger-entries` | API List / Schema | 367 | none | Ledger filters, pagination, and completeness |
| `update-invoice-issue-date` | API Mutation | 190 | none | Short state-changing mutation |
| `get-audit-logs` | API List / Schema | 327 | none | Security-oriented list and visibility boundaries |
| `gcp` | Integration Guide | 343 | none | External responsibility and data-flow boundaries |
| `api-quickstart` | Concept / Guide | 435 | Campaign 13 queued, attempt 0 | End-to-end onboarding guide |
| `system-notifications` | Concept / Guide | 388 | Campaign 13 queued, attempt 0 | Notification lifecycle and delivery routing |
| `manage-seats` | Concept / Guide | 194 | Campaign 15 rejected, attempt 1 | Known old-contract semantic defect check |

The first five pages are absent from every earlier Metronome manifest.
`api-quickstart` and `system-notifications` were never dispatched in Campaign
13 and have no attempt artifacts. `manage-seats` deliberately tests whether
the new contract prevents the old unassigned-seat mistake. Campaign 24 must
generate all three candidates from scratch and may not read or reuse any prior
candidate, receipt, suggestion, failure, or review as source evidence.

## Execution and promotion

- Use the unchanged Campaign 23 Minimum Sufficient Source playbook and the
  matching section of `tracking/ingest/metronome/lessons.md`.
- Keep at most three native subagents active beside the coordinator, with
  dynamic worker/reviewer allocation and no batch barrier.
- Persist each trusted review order automatically before reviewer dispatch.
- After an individual reviewer approval, the coordinator may serially apply
  that job's approved primary-concept changes, promote its exact candidate,
  and run targeted checks while unrelated agents continue.
- Company, provider index, provider log, aggregate counts, capsule validation,
  fixed query audit, and the campaign commit remain one close-stage operation.
- A pause stops new dispatch and promotion but preserves completed evidence and
  already promoted approved pages for recovery.

## Fixed audit and decision

The immutable three-page audit sample is:

- `update-invoice-issue-date`: standard short mutation;
- `get-the-rate-schedule-for-a-contract`: longest/schema-heaviest page; and
- `gcp`: ordinary cross-system integration page.

Each audit checks factual retrieval, a material boundary or contradiction,
exact raw deep-dive navigation, and primary-concept reciprocity. A material
partial or failure expands the semantic audit to all eight pages. Mechanical
hash, canonical URL, candidate equality, raw backlink, duplicate, touched-link,
and count checks cover every promoted page.

Record first-pass approvals, bounded versus full retries, attempts, review
scope, time to final approval, total close time, coordinator repairs, fixed or
expanded query results, raw deep-dive success, and primary-concept reciprocity
using existing campaign files only. Do not add a performance registry.

The confirmation passes only if final content quality passes and the result
does not regress to the repeated complete rereads seen before Campaign 23.
Throughput is evaluated from the recorded times rather than a hard time limit.
Cross-PSP rollout, reviewer sampling, Luna/Terra routing, and bulk migration
remain separate decisions.

## Authorization boundary

Approval of this exact manifest authorizes adding a narrow Campaign 24 clause
to the Metronome provider rule, initializing this campaign, complete reads of
only these eight raw pages, strong-model workers, distinct complete-source
strong-model reviewers, bounded retries, reviewer-approved incremental
promotion, and fixed or expanded close audit. It does not authorize a ninth
page, reuse of closed campaign outputs, reviewer sampling, another provider,
remote push, or unrelated-file modification.
