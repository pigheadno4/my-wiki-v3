# Metronome Campaign 26 recollection pilot proposal

**Status:** Awaiting exact-manifest execution approval
**Mode:** Five-page source refresh and one new-source confirmation
**Collection baseline:** 81 changed, 1 new, and 146 unchanged current targets

## Goal

Validate the existing ingestion workflow against the first Metronome
recollection round without scaling to all changed pages. Four jobs update an
existing source from a newer immutable raw snapshot; one job creates a source
for the round's only new canonical page. Every worker reads its complete latest
raw, returns a complete candidate, and preserves the older raw route when
updating an existing source. Every candidate receives a different strong Sol
complete-source review before promotion.

This proposal changes no scheduler, result schema, reviewer policy, source
contract, or validator. The coordinator remains the only canonical writer and
uses the post-Campaign 25 longest/high-risk-first dispatch guidance.

## Metadata and collection-evidence selection

Selection used current collection state, raw path, line count, SHA-256, stored
diff size, existing-source presence, and documentation archetype. The raw
bodies were not read in full to prepare this proposal; workers and reviewers
must still complete their assigned reads.

| Job | Raw lines | Diff lines | Archetype | Source action | Selection reason |
| --- | ---: | ---: | --- | --- | --- |
| `edit-a-contract-refresh` | 4,683 | 304 | API Mutation | update | Longest/high-risk mutation sample; lifecycle, financial, idempotency, and authority boundaries |
| `database-reference-refresh` | 1,607 | 102 | API List / Schema | update | Schema-heavy warehouse reference and row-grain/navigation behavior |
| `stripe-tax-refresh` | 188 | 58 | Integration Guide | update | Cross-system tax, invoice finalization, mapping, and downstream authority |
| `create-products-contracts-refresh` | 130 | 63 | Concept / Guide | update | Short conceptual refresh for the fast path |
| `token-billing` | 258 | new page | Concept / Guide | create | Only new canonical page in the collection round |

Dispatch begins with `edit-a-contract-refresh`, then
`database-reference-refresh`; the remaining slots take the shorter jobs. This
ordering is advisory and uses no new campaign field. The fixed close audit uses
`edit-a-contract-refresh`, `database-reference-refresh`, and `token-billing`.

## Refresh contract

For each refresh job, the worker must:

1. Read the complete 2026-08-28 raw and the complete current source target.
2. Treat the stored diff as navigation only, never as a substitute for the
   latest complete raw read.
3. Return the complete updated source page, prepend the 2026-08-28 raw path in
   `raw_files`, retain the older raw path, and add both exact raw backlinks.
4. Preserve still-valid facts, explicit contradictions, primary concepts, and
   durable authority boundaries; remove or qualify facts made stale by the new
   snapshot.
5. Return only reviewer-ready shared-file suggestions. The coordinator applies
   approved shared updates serially.

`token-billing` follows the same Minimum Sufficient Source and Concept / Guide
contract as a new source. Its full read decides the durable facts and primary
concept routes; metadata selection does not pre-authorize product claims.

## Review and close

- Use strong Sol workers and different strong Sol complete-source reviewers.
- Keep three dynamic native-agent slots and no batch barrier.
- A bounded correction may receive targeted diff review only under the existing
  unchanged-hash rule; material factual or authority changes require a complete
  review.
- The coordinator does not perform a default third full raw read. It validates
  approved candidate promotion, shared suggestions, reciprocal links, raw
  version order, company/index/log/count closure, and the fixed query audit.
- This documentation-only campaign uses targeted wiki checks, capsule
  validation, hash/link/count checks, and `git diff --check`; it does not run the
  full unit suite unless code, rules, or validators change during execution.

## Authorization boundary

This file and `manifest.json` are a proposal only. They do not initialize the
campaign or authorize agent dispatch. Separate approval of the exact manifest
would authorize complete reads of only these five current raw pages, updates to
the four named existing sources, creation of the one named new source, distinct
per-page Sol reviews, bounded retries, reviewer-approved shared updates,
canonical promotion, and the existing close gates.

It does not authorize a sixth page, bulk ingestion of the remaining collection
round, reviewer sampling, Luna or Terra routing, scheduler/schema/validator
changes, cross-PSP rollout, remote push, or unrelated-file modification.
