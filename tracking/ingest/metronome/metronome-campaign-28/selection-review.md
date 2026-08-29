# Metronome Campaign 28 first-pass confirmation proposal

**Status:** Exact manifest approved; campaign completed 2026-08-29
**Mode:** Five-page existing-source refresh
**Collection baseline:** 81 changed, 1 new, and 146 unchanged current targets

## Goal

Confirm that Campaign 27's first-pass improvement extends to a different page
mix before increasing campaign size. Campaign 28 retains five pages and the
same worker, review, retry, promotion, and close contracts while adding two
roughly 450-line API controls. Success requires at least four first-pass
approvals without weakening complete raw reads or independent review.

This proposal changes no scheduler, result schema, global rule, validator,
model route, or monitoring format. It adds no registry, timing subsystem, or
new archetype contract. Campaign 27's bounded reminders are embedded only in
the job-specific routing reasons.

## Metadata and collection-evidence selection

Selection used current collection state, raw path, line count, SHA-256, stored
diff size, existing-source presence, documentation archetype, and distance
from the source identity's prior campaign. Raw bodies were not read in full to
prepare this proposal; workers and reviewers must still complete their
assigned reads.

| Job | Raw lines | Diff lines | Archetype | Prior campaign | Selection reason |
| --- | ---: | ---: | --- | --- | --- |
| `manage-product-access-refresh` | 53 | 11 | Concept / Guide | 08 | Short customer-access guide for the clean fast path |
| `anrok-refresh` | 105 | 38 | Integration Guide | 10 | Tax and invoice responsibility across Metronome, Stripe, and Anrok |
| `data-export-overview-refresh` | 134 | 23 | Reporting / Guide | 03 | Export delivery, ownership, cadence, completeness, and schema-authority boundaries |
| `list-products-refresh` | 451 | 24 | API List / Schema | 22 | Pagination, archive filtering, history surfaces, and List-versus-Get schema scope |
| `create-a-credit-refresh` | 454 | 46 | API Mutation | 20 | Financial mutation, selectors, resource identity, idempotency, and failure boundaries |

The fixed close audit uses `anrok-refresh`, `list-products-refresh`, and
`create-a-credit-refresh` to cover cross-system integration, the schema-heavy
list page, and the longest financial mutation page.

## First-pass worker contract

Each worker must:

1. Read the complete 2026-08-28 raw and complete current source target. Treat
   the stored diff as navigation only.
2. Return one complete, coarse-grained source candidate; prepend the current raw
   path, retain prior immutable raw history, and preserve still-valid durable
   facts.
3. Qualify broader-versus-narrower schema applicability and never generalize a
   page-local field, annotation, provider behavior, or example.
4. Separate general lifecycle and API-wide authority from operation-specific
   financial, retry, failure, and reconciliation behavior.
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
  `git diff --check` run once at close.
- Thirty-five minutes is an observation target, not a quality waiver. Only
  `started_at` and `completed_at` are used for timing.

## Authorization boundary

This file and `manifest.json` are a proposal only. They do not initialize the
campaign or authorize agent dispatch. Separate approval of the exact manifest
would authorize complete reads of only these five current raw pages, updates to
only the five named existing source targets, distinct per-page Sol reviews,
bounded retries, reviewer-approved shared updates, canonical promotion, and the
existing close gates.

It does not authorize a sixth page, an 8-10 page expansion, bulk ingestion of
the remaining collection round, reviewer sampling, Luna or Terra routing,
scheduler/schema/rule/validator changes, cross-PSP rollout, remote push, or
unrelated-file modification.
