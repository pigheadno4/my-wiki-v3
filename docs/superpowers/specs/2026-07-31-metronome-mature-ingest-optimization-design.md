# Metronome Mature Ingest Optimization Design

**Date:** 2026-07-31
**Status:** User-approved direction; written design awaiting final review
**Scope:** Metronome Campaign 08 and later campaigns only

## Goal

Reduce retry and coordinator time while preserving one complete independent
Sol review of every first-attempt source candidate. Reuse approved worker and
reviewer output for bounded corrections and shared-file updates instead of
repeating the same semantic work.

## Non-goals

This change does not add a new scheduler, backend abstraction, worktree model,
agent registry, rollback system, or event-level performance telemetry. It does
not authorize parallel ingest for another provider.

## Simplified production mode

Campaign 08 carries forward the approved dynamic scheduler and applies these
rules as one operating mode:

- Sol is the default worker and every first attempt receives an independent
  Sol review. Terra is used only for genuinely templated, isolated pages that
  require no semantic update to a shared concept.
- Keep three dynamic sub-agent slots beside the coordinator. A completed
  worker immediately releases its slot; the scheduler assigns that slot to a
  ready reviewer or the next worker without waiting for a batch barrier.
- The first reviewer reads the complete raw source.
- A retry limited to links, frontmatter, wording, or an already-identified
  omitted field uses targeted diff review when the raw hash is unchanged.
- A retry caused by factual error, material omission, misunderstanding, new
  evidence, or unresolved content risk receives another complete-source
  review.
- The coordinator does not perform a default full-source reread. It owns final
  approval, canonical promotion, shared-file writes, reciprocal links, and
  final mechanical validation.
- Each campaign runs one campaign-close wiki validation, one Metronome capsule
  validation, and the predetermined three-page query audit. It does not repeat
  global validation between individual promotions.
- Timing adds only `started_at` and `completed_at`; no event-level performance
  monitoring system is introduced.

## Review modes

Every first-attempt candidate receives the existing complete-source review by
a Sol reviewer who is different from the worker.

When that reviewer requests changes, the review records one of two scopes:

- `targeted`: the raw hash is unchanged, the requested corrections are fully
  enumerated, and they concern only mechanical defects or bounded omissions
  already identified during the complete-source review. The corrected
  candidate introduces no unrelated semantic change, new factual claim, new
  quote, new concept target, or unresolved contradiction.
- `full`: the correction changes or adds factual meaning, evidence, quotes,
  boundaries, contradictions, concept selection, or any content whose safety
  cannot be established from the prior review and the candidate diff.

For a targeted retry, prefer a follow-up to the same Sol reviewer that issued
the change request. It checks only:

1. every enumerated requested change was resolved;
2. the candidate diff contains no unrelated semantic change;
3. candidate, receipt, and shared-file suggestions remain consistent;
4. deterministic link, schema, URL, quote, and raw-hash checks pass.

If the prior reviewer is unavailable, another Sol reviewer may perform the
same targeted check from the prior candidate, prior review, corrected
candidate, and their diff. Any uncertainty promotes the retry to `full`.

A full retry receives a new complete-source Sol review. The existing maximum
of three worker attempts remains unchanged. Targeted review reduces duplicate
reading; it never converts an unresolved content problem into a mechanical
check.

## Shared-file update contract

Workers continue returning one isolated source candidate and structured
suggestions. Each suggested shared update identifies:

- the exact target path;
- the update kind: durable fact, reciprocal source link, catalog entry, log
  entry, or calculated count;
- an insertion anchor or existing section;
- the proposed Markdown for semantic updates;
- the grounding quote identifiers for factual prose;
- explicit warnings or unresolved conflicts.

The Sol reviewer approves or rejects each shared update as part of the source
review. An approved source candidate does not automatically approve an unsafe
or unnecessary shared update.

The coordinator consumes approved updates as follows:

1. Group them by exact target path and deduplicate source links.
2. Generate catalog entries, log entries, and `source_count` mechanically from
   approved campaign metadata; do not ask a model to rewrite them.
3. For concepts and factual company-page prose, read each target once and
   apply the reviewer-approved Markdown patches together at the named anchors.
4. Resolve only collisions between approved patches, duplicate facts, or
   contradictions with the current target. Do not resynthesize every worker
   response from scratch.
5. Write each shared file once, then run exhaustive backlink, duplicate,
   count, and link checks at campaign close.

If two approved suggestions materially disagree, the coordinator pauses only
that target reduction, resolves the conflict from the relevant review evidence,
and rereads raw content only when the reviews do not settle it. Other jobs and
unaffected target reductions continue.

## Model routing

Sol is the default worker. In particular, route pages that modify shared
concepts, require cross-source reasoning, carry schema-heavy contracts, or have
contradiction risk to Sol. Terra is limited to isolated, templated pages whose
anticipated shared changes are mechanical catalog, log, link, and count
updates. Every first attempt still has an independent Sol reviewer.

## Coordinator boundary

The coordinator owns canonical writes and final approval but does not perform
a default third full-source read. Its review is limited to:

- approved candidate and review state;
- shared-update grouping and collisions;
- source-to-concept and concept-to-source backlinks;
- company and provider catalog completeness;
- calculated counts, hashes, duplicates, and final validators.

## Validation and timing

Run handoff validation for each candidate and review. Run the targeted wiki
validation, shared-file checks, and Metronome capsule validator once at campaign
close. Keep the predetermined three-page query audit; expand only on a material
partial or failure. Do not rerun the full unit suite for a documentation-only
mature campaign.

Record only campaign `started_at` and `completed_at`. These two timestamps are
enough to establish a Campaign 08 baseline without adding event telemetry.

## Acceptance

The mature optimization is acceptable when:

- every first attempt has a distinct complete-source Sol review;
- every targeted retry satisfies the bounded eligibility rules and records its
  prior attempt and change requests;
- content-risk retries receive a full review;
- approved shared updates are grouped and each shared target is normally
  written once;
- the coordinator performs no undeclared default full-source reread;
- campaign-close checks and the predetermined query audit pass;
- the monitor reports worker attempts, full reviews, targeted reviews,
  coordinator repairs, and elapsed campaign time.

Campaign 08 is operational ingest and the first measured mature-mode baseline,
not another standalone scheduler experiment.
