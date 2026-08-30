# Metronome Campaign 31 never-ingested coverage proposal

**Status:** Approved and executed
**Mode:** Five new Minimum Sufficient Sources from never-ingested canonical pages
**Collection baseline:** 226 current English canonical pages; 146 official-document sources; 80 canonical pages never ingested

## Goal

Shift the next campaign from repeated refresh work to new knowledge coverage.
Every selected canonical page currently has no source page. Campaign 31 keeps
the existing mature Metronome controls: one complete raw read per worker, one
isolated source candidate, a different strong Sol complete-source reviewer,
three dynamic native-agent slots, coordinator-only canonical writes, bounded
retries, and one mature close validation.

This proposal adds no registry, classifier, scheduler state, prompt layer,
validator, or performance-monitoring system.

## Mechanical selection boundary

Selection used only the accepted collection run, source canonical URLs, raw
path, line count, documentation section, and prior completed Campaign 12
routing evidence. Raw bodies were not read to prepare this proposal. Metadata
does not authorize facts or a `raw_reference` disposition; every approved job
must still receive a complete raw read.

The first two jobs close known Campaign 12 coverage gaps whose complete-read
calibration already resolved to `source_required`. The remaining three add
distinct customer-billing, alert-mutation, and financial-reporting coverage.

| Job | Raw lines | Archetype | Selection reason |
| --- | ---: | --- | --- |
| `create-custom-field-key-new-source` | 198 | API Mutation / Schema | Campaign 12 found unique required-field, failure, uniqueness, managed-entity, and propagation semantics; no source was created |
| `delete-custom-field-key-new-source` | 151 | API Mutation / Lifecycle | Campaign 12 semantic triage resolved this page to `source_required`; no source was created |
| `set-customer-billing-provider-config-new-source` | 430 | API Mutation / Integration | New customer-to-provider configuration coverage with identifier, routing, replacement, failure, and downstream-authority risk |
| `create-threshold-notification-new-source` | 451 | API Mutation / Alert | New threshold configuration coverage with required schema, evaluation state, failure, lifecycle, and notification-boundary risk |
| `asc-606-revenue-recognition-new-source` | 555 | Financial Reporting Guide | Longest control for accounting-authority, revenue-model, timing, example, limitation, and reconciliation boundaries |

The five latest raws total 1,785 lines. Dispatch the longest financial guide,
the alert mutation, and the customer billing-provider mutation first. The
fixed close audit uses `asc-606-revenue-recognition-new-source`,
`create-custom-field-key-new-source`, and
`set-customer-billing-provider-config-new-source`.

## Worker and review contract

Each worker must read its complete assigned raw and the relevant current
concept/source context, then return one Minimum Sufficient Source. The source
must retain query-critical durable facts, material contradictions and
unknowns, primary concept routes, a raw-detail coverage map, and the exact
path-qualified raw backlink without copying the complete schema or procedure.

For API mutations, distinguish request-body requiredness from payload-field
requiredness, keep every field under its immediate parent schema, separate
endpoint-local identity from API-wide POST idempotency, and preserve durable
failure, lifecycle, and propagation unknowns. For the financial guide,
preserve the source's authority boundary and do not convert product guidance or
worked examples into accounting policy.

Every first attempt receives a complete-source review by a different strong
Sol agent. Only unchanged-hash, non-semantic corrections may receive targeted
review. A factual, authority, material-omission, lifecycle, contradiction, or
shared-evidence defect requires a complete retry and complete review.

## Success and close gates

- Five of five sources finally approved; at least four pass on attempt 1.
- No rejected job, coordinator semantic repair, or more than one full semantic retry.
- Fixed audit passes all nine factual, boundary or contradiction, and exact raw deep-dive checks.
- Canonical sources equal their approved candidates and appear exactly once in company and provider indexes.
- Reviewer-approved primary concept updates and reciprocal links appear exactly once.
- Targeted wiki validation, capsule validation, raw hashes, counts, links, and `git diff --check` run once at close.
- Timing is observational; quality is not waived to meet a target.

## Authorization boundary

This proposal and `manifest.json` do not initialize Campaign 31 or authorize
agent dispatch. Explicit approval of this exact manifest would authorize only
the five complete raw reads, five new source targets, distinct per-page Sol
reviews, bounded retries, approved primary-concept updates, catalog/count/log
updates, fixed audit, close checks, and one local campaign commit.

It does not authorize a sixth page, refresh of the 36 stale existing sources,
bulk ingestion of the remaining inventory, reviewer sampling, Luna or Terra,
rule or code changes, cross-PSP rollout, remote push, or unrelated-file edits.
