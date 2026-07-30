# Metronome Parallel-Review Campaign Design

**Date:** 2026-07-30
**Status:** User-approved design; implementation and exact Campaign 07 page selection pending
**Scope:** A bounded ten-page Campaign 07 pilot

## Goal

Reduce wall-clock time without removing the independent full-source quality
gate. Every source receives one worker read and one separate Sol reviewer read.
The coordinator focuses on canonical writes, shared-file synthesis, links,
counts, validation, and final approval rather than rereading every standard raw
page.

## Non-goals

This pilot does not add:

- permanent worker or reviewer identities;
- a role registry or model-switching state;
- concurrent repository writers;
- per-agent worktrees;
- a new job state;
- automatic crash reconciliation or rollback;
- a complex risk-scoring system;
- a batch source summary spanning several raw pages.

## Roles

### Worker

One worker reads one complete raw page, extracts three to five exact quotes, and
returns the existing fixed-schema candidate and shared-file suggestions. It
writes no repository file.

### Sol reviewer

A fresh Sol agent reads the same complete raw page, candidate, quotes, and
relevant current concepts/source context. It semantically assesses the
shared-file suggestions, but does not reread the full company page, provider
index, or log. It either approves the candidate and its suggestions or requests
a new bounded attempt. The worker and reviewer cannot be the same agent.

Approval means the candidate is canonical-ready; the reviewer does not create a
second source-page schema. This keeps the current result contract.

### Coordinator

The coordinator does not normally reread approved standard raw pages. It:

- owns campaign tracking and all repository writes;
- groups approved suggestions by shared target;
- performs concept-first reduction;
- writes approved sources;
- reconciles contradictions and links;
- updates company, index, log, and counts once;
- runs deterministic checks and final approval.

It performs a full raw read only for disputes, uncertain reviews, unresolved
retry risk, manifest-designated high-risk pages, and final audit samples.

## Dynamic slot policy

The coordinator occupies one native-agent slot. Remaining capacity is assigned
from current queue counts, not fixed roles.

```text
free_slots = total_subagent_slots - active_workers - active_reviewers
worker_reserve = 1 if queued_jobs > 0 and active_workers == 0 else 0
review_slots = min(candidate_ready, review_cap, free_slots - worker_reserve)

start ready reviews up to review_slots
fill the remaining free slots with queued workers
```

Every new order must fit `free_slots`. For the current Codex four-agent runtime,
`total_subagent_slots` is three and
`review_cap` is two while worker jobs remain. A released worker slot immediately
enters the same allocation loop. The reserve is zero while any worker is active,
so a ready review is not starved to hold an additional worker slot. There is no
five-job batch barrier.

## Minimal scheduler change

The current states already include `candidate_ready` and `reviewing`. Campaign
07 needs only narrow scheduling and tracking support: validate the manifest's
`review_concurrency` into campaign configuration, then support more than one
concurrent `reviewing` job under one shared slot budget:

1. Count active workers and reviewers to calculate `free_slots`.
2. Set `worker_reserve` to one only when queued jobs remain and no worker is
   active.
3. Prefer ready reviews up to `review_concurrency` and `free_slots -
   worker_reserve`.
4. Fill remaining free slots with queued workers.
5. Record the worker identity when its order is dispatched.
6. Persist a `review.json` for each review attempt with reviewer identity,
   reviewer model, and verdict.

No state-machine expansion, backend abstraction, worktree, or new persistent
role model is part of this pilot.

## Campaign-level promotion

Canonical promotion remains coordinator-only:

1. Collect reviewer-approved candidates and suggestions.
2. Group suggestions by concept.
3. Merge durable facts and planned source wikilinks, then read and update each
   affected concept once before its corresponding source is written.
4. Write each independently approved source page.
5. Verify fact-based concept citations and contradictions; repair a defect if
   one is found.
6. Update the Metronome company page, index, log, and counts once.

Campaign tracking preserves per-job candidates, attempts, failures, reviews,
and approvals, so shared-file reduction does not remove source-level
traceability.

## Validation

Per worker:

- raw SHA-256;
- canonical URL;
- exact result keys;
- three to five byte-matching quotes.

Per reviewer:

- full raw read;
- factual and boundary completeness;
- contradiction and unknown preservation;
- raw/source/related-link intent;
- shared-file suggestion completeness.

At campaign close:

- validate all promoted source pages together;
- validate every touched concept and company page together;
- check every campaign raw link and manifest hash;
- have the coordinator exhaustively check the company page, provider index,
  provider log, links, and counts once;
- run the Metronome capsule validator once;
- run the full unit suite only if campaign code, rules, or validators changed.

## Independent audit

The immutable approved manifest records three distinct audit job IDs before
execution:

1. one standard page;
2. the longest or schema-heaviest page;
3. one ordinary manifest sample.

The auditor reads those complete raw/source pairs and asks one core, one
boundary, and one trap question per page. Any material partial or fail expands
the audit to all ten pages. Deterministic link, duplicate, hash, and count checks
always cover all ten.

## Acceptance

Campaign 07 may validate this workflow only if:

- every promoted page has a distinct worker and Sol reviewer;
- no worker or reviewer writes repository files;
- coordinator raw rereads are limited to declared exceptions;
- planned shared-file reduction is applied once, except for a repair found by
  later verification;
- all campaign-wide deterministic checks pass;
- the three-page audit passes without material expansion findings;
- elapsed time and coordinator repair work improve over Campaign 06;
- no quality regression appears in the sampled query audit.

Campaign 07 success authorizes proposing this as the mature Metronome
documentation-ingest mode. It does not automatically authorize larger
concurrency or use for other providers.
