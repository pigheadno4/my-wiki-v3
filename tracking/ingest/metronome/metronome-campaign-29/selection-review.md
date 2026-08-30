# Metronome Campaign 29 bounded first-pass correction proposal

**Status:** Complete; 5/5 finally approved and promoted on 2026-08-30
**Mode:** Five-page existing-source refresh
**Collection baseline:** 81 changed, 1 new, and 146 unchanged current targets

## Goal

Test two bounded worker-brief corrections after Campaign 28 reached final
quality but missed its first-pass and retry-count throughput gates. Campaign 29
retains five pages, strong Sol workers, independent complete-source Sol review,
dynamic slots, existing retry rules, incremental promotion, and the mature
close path.

The only new campaign-local reminders are:

1. Assign every query-critical field to its immediate parent schema and keep
   response-envelope, top-level resource, nested state or update, List, Get,
   and mutation scopes separate.
2. Preserve raw financial units and source authority before paraphrasing; do
   not broaden terms or convert endpoint-local behavior into a general rule.

This proposal changes no scheduler, result schema, provider rule, validator,
model route, registry, timing format, or monitoring layer. Controller-only
attempt staging is restated as an existing ownership boundary, not a third
semantic experiment.

## Metadata and collection-evidence selection

Selection used current collection state, raw path, line count, SHA-256, stored
diff size, existing-source presence, archetype, and distance from the source
identity's prior campaign. Raw bodies were not read in full to prepare this
proposal; workers and reviewers must still complete their assigned reads.

The initial dispatch order puts the two API controls and the integration page
first so the 1,144-line longest read overlaps shorter work rather than becoming
tail latency.

| Job | Raw lines | Diff lines | Archetype | Prior campaign | Selection reason |
| --- | ---: | ---: | --- | --- | --- |
| `list-invoices-refresh` | 1,144 | 45 | API List / Schema | 23 | Longest control for immediate-parent schema placement, pagination, lifecycle, and List authority |
| `edit-a-commit-refresh` | 469 | 21 | API Mutation / Financial | 03 | Financial-unit, lifecycle, selector, and endpoint-versus-API-wide authority control |
| `avalara-refresh` | 86 | 30 | Integration Guide | 10 | Metronome-versus-Avalara tax, invoice, failure, and reconciliation responsibility |
| `in-app-reporting-refresh` | 178 | 43 | Reporting / Guide | 11 | Reporting access, embedding, data-authority, freshness, completeness, and security boundaries |
| `role-based-access-rbac-refresh` | 66 | 29 | Concept / Security Guide | 07 | Short clean-path control for exact role, permission, enforcement, and propagation scope |

The five latest raws total 1,943 lines. The fixed close audit uses
`list-invoices-refresh`, `edit-a-commit-refresh`, and `avalara-refresh` to cover
the two corrected worker reminders plus a cross-system integration control.

## Worker and staging contract

Each worker must:

1. Read the complete 2026-08-28 raw and complete current source target. Treat
   the stored diff as navigation only.
2. Return one complete Minimum Sufficient Source candidate with query-critical
   facts, material boundaries or contradictions, a raw-detail coverage map,
   primary concept routes, newest-first immutable history, and an exact
   path-qualified raw backlink.
3. Apply the immediate-parent schema and exact-unit or authority reminders
   above when they are relevant; do not force irrelevant schema or financial
   sections onto a page.
4. Preserve existing adjacent shared facts, ground every factual shared-file
   suggestion with an exact raw quote, and audit primary-concept reciprocal
   routes.
5. Return only the fixed result object outside the repository. The controller
   alone writes `candidate.md`, `receipt.json`, `suggestions.json`, campaign
   state, canonical pages, shared files, and the commit.

## Review, success gates, and close

- Use strong Sol workers and different strong Sol complete-source reviewers.
- Keep three dynamic native-agent slots and no batch barrier.
- Every first review reads the complete assigned raw and candidate.
- A bounded unchanged-hash correction may receive targeted review only when it
  changes no factual meaning. Schema placement, financial meaning, authority,
  material omission, or contradiction fixes require complete review.
- The coordinator does not perform a default third full raw read or silently
  repair source semantics. It promotes only reviewer-approved candidates and
  shared updates, then performs shared catalogs, links, counts, and mechanical
  close checks once.
- Required close result: five of five finally approved, at least four of five
  approved on the first attempt, no rejected job, no coordinator semantic
  repair, and no more than one full semantic retry.
- The fixed three-page query audit must pass all nine checks. Existing targeted
  wiki checks, capsule validation, raw-hash, link, count, candidate-equality,
  and `git diff --check` checks run once at close.
- Thirty-five minutes remains an observation target, not a quality waiver.
  Only campaign-level `started_at` and `completed_at` are recorded.

## Authorization boundary

This file and `manifest.json` are proposal artifacts only. They do not
initialize Campaign 29 or authorize agent dispatch. Separate approval of this
exact manifest would authorize complete reads of only these five current raw
pages, updates to only the five named existing source targets, distinct
per-page Sol reviews, bounded retries, reviewer-approved shared updates,
canonical promotion, the fixed three-page audit, mature close checks, and one
local campaign commit.

It does not authorize a sixth page, larger campaign, bulk ingestion, reviewer
sampling, Luna or Terra routing, rule or code changes, cross-PSP rollout,
remote push, or unrelated-file modification.
