# Metronome Campaign 27 first-pass-rate pilot proposal

**Status:** Exact manifest approved; campaign completed 2026-08-29
**Mode:** Five-page existing-source refresh
**Collection baseline:** 81 changed, 1 new, and 146 unchanged current targets

## Goal

Test whether a small, representative campaign can reach at least four first-pass
approvals out of five while retaining complete raw reads and independent
per-page review. The campaign deliberately favors bounded pages over another
longest/high-risk stress sample, but retains one schema-heavy API page so the
result is not based only on easy inputs.

This proposal changes no scheduler, result schema, global rule, validator, or
review policy. It adds no registry or performance-monitoring subsystem. The
five Campaign 26 lessons are embedded only in the job-specific routing reasons.

## Metadata and collection-evidence selection

Selection used current collection state, raw path, line count, SHA-256, stored
diff size, existing-source presence, documentation archetype, and recent-
campaign exclusion. Raw bodies were not read in full to prepare this proposal;
workers and reviewers must still complete their assigned reads.

| Job | Raw lines | Diff lines | Archetype | Selection reason |
| --- | ---: | ---: | --- | --- |
| `allowlist-refresh` | 43 | 9 | Concept / Guide | Short configuration page that should exercise the clean fast path |
| `authentication-refresh` | 112 | 22 | API Overview | Security-sensitive overview with bounded credential and authority semantics |
| `regenerate-an-invoice-refresh` | 166 | 11 | API Mutation | Mutation prerequisites, lifecycle effect, and failure boundaries |
| `custom-invoice-integrations-refresh` | 168 | 26 | Integration Guide | Cross-system responsibility, invoice flow, and reconciliation boundaries |
| `get-a-product-refresh` | 433 | 24 | API Read / Schema | One longer structured page to test schema-scope discipline without a field-catalog rewrite |

The fixed close audit uses `authentication-refresh`,
`custom-invoice-integrations-refresh`, and `get-a-product-refresh` to cover
overview, integration, and schema-heavy API behavior.

## First-pass worker contract

Each worker must:

1. Read the complete 2026-08-28 raw and complete current source target. Treat
   the stored diff as navigation only.
2. Return one complete, coarse-grained source candidate; prepend the current raw
   path, retain prior immutable raw history, and preserve still-valid durable
   facts.
3. Qualify broader-versus-narrower schema applicability and never generalize an
   endpoint-local field or behavior into a provider-wide rule.
4. Distinguish general lifecycle or effective-dating behavior from fields that
   are editable only for a particular resource or operation.
5. Preserve existing adjacent shared facts when suggesting an update; do not
   replace a whole shared passage merely to add one fact.
6. Supply byte-exact raw quote coverage for every fact-bearing shared-file
   suggestion.
7. Audit raw backlinks plus umbrella and primary-concept reciprocal routes
   before returning the candidate.

## Review, success gates, and close

- Use strong Sol workers and different strong Sol complete-source reviewers.
- Keep three dynamic native-agent slots and no batch barrier.
- The first review reads the complete assigned raw and candidate.
- A bounded correction may receive targeted diff review only under the existing
  unchanged-hash rule. Factual error, important omission, authority error, or
  material interpretation change requires complete review.
- The coordinator does not perform a third full raw read or silently repair
  source semantics. It handles approved promotion, reviewer-approved shared
  suggestions, reciprocal links, raw ordering, company/index/log closure, and
  mechanical validation.
- Required close result: five of five finally approved, at least four of five
  approved on the first attempt, no rejected job, no coordinator semantic
  repair, and no more than one full semantic retry.
- The fixed three-page query audit must pass all nine checks. Existing targeted
  wiki checks, capsule validation, hash/link/count checks, and
  `git diff --check` must pass once at close.
- Thirty minutes is an observation target, not a quality waiver. Only
  `started_at` and `completed_at` are used for timing.

## Authorization boundary

This file and `manifest.json` are a proposal only. They do not initialize the
campaign or authorize agent dispatch. Separate approval of the exact manifest
would authorize complete reads of only these five current raw pages, updates to
only the five named existing source targets, distinct per-page Sol reviews,
bounded retries, reviewer-approved shared updates, canonical promotion, and the
existing close gates.

It does not authorize a sixth page, bulk ingestion of the remaining collection
round, reviewer sampling, Luna or Terra routing, scheduler/schema/rule/validator
changes, cross-PSP rollout, remote push, or unrelated-file modification.
