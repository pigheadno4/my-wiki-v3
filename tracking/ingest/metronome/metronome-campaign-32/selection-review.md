# Metronome Campaign 32 five-page coverage proposal

**Status:** Approved and executed on 2026-08-31
**Mode:** Five new Minimum Sufficient Sources from never-ingested canonical pages
**Current baseline:** 226 current English canonical pages; 151 official-document sources; 75 canonical pages never ingested

## Goal

Continue increasing new query coverage while testing a less conflict-dense
five-page mix. Campaign 32 keeps the established mature controls: one complete
raw read per worker, one isolated source candidate, a different strong Sol
complete-source reviewer, three dynamic native-agent slots, coordinator-only
canonical writes, bounded retries, and one mature close validation.

The campaign keeps five pages so timing remains comparable with recent
production campaigns. It intentionally includes only one long schema-heavy
page. This proposal adds no registry, classifier, scheduler state, prompt
layer, validator, or performance-monitoring system.

## Mechanical selection boundary

Selection reconciled the immutable 80-page pre-Campaign-31 planning snapshot
against current official-document source canonical URLs, leaving 75 currently
uncovered pages. It then used documentation path, page title, latest raw path,
line count, and source-target absence. Only raw headers and collection metadata
were inspected; raw bodies were not read end to end and no metadata-only fact
or `raw_reference` disposition is authorized.

| Job | Raw lines | Risk | Archetype | Selection reason |
| --- | ---: | --- | --- | --- |
| `list-invoice-breakdowns-new-source` | 1,150 | high | API Read / Schema | The only schema-heavy control; tests parent-schema placement, time-series and invoice boundaries, pagination or completeness limits, contradictions, and raw-detail routing without copying the full schema |
| `get-embeddable-customer-dashboard-new-source` | 293 | medium | API Read / Embedded UI | Tests customer scope, URL or token authority, authentication and exposure boundaries, lifecycle and freshness unknowns, and separation from general dashboard guidance |
| `create-or-update-customer-ingest-aliases-new-source` | 158 | medium | API Mutation / Identity | Tests alias identity, replacement or merge behavior, event-attribution implications, API-wide POST idempotency, failure, concurrency, and propagation unknowns |
| `archive-billable-metric-new-source` | 162 | medium | API Mutation / Lifecycle | Tests archival preconditions and effects, existing-versus-new object behavior, API-wide POST idempotency, reversibility, failure, and propagation unknowns |
| `guarantee-zero-overages-new-source` | 205 | medium | Pricing Guide / Commit Boundary | Guide control for pricing actors, commit consumption, invoice and access boundaries, worked examples, limitations, contradictions, and merchant-owned enforcement |

The five latest raws total 1,968 lines. Dispatch the invoice-breakdown page,
embeddable-dashboard page, and alias mutation first so the longest read overlaps
two independent medium pages. The fixed close audit uses
`list-invoice-breakdowns-new-source`,
`guarantee-zero-overages-new-source`, and
`create-or-update-customer-ingest-aliases-new-source` to cover the schema-heavy
page, the guide, and an ordinary mutation.

## Worker and review contract

Each worker must read its complete assigned raw and relevant current
concept/source context, then return one Minimum Sufficient Source. Preserve
query-critical durable facts, material contradictions and unknowns, primary
concept routes, a raw-detail coverage map, and the exact path-qualified raw
backlink without reconstructing the complete procedure or schema.

For API pages, distinguish request-body requiredness from payload-field
requiredness, retain fields under their immediate parent schemas, and separate
endpoint-local identity from API-wide POST idempotency. Preserve lifecycle,
visibility, concurrency, partial-result, downstream, and recovery unknowns
when the page does not establish them. For the guide, preserve the boundary
between billing configuration, invoice amount, customer access, and
merchant-owned product enforcement; do not turn an example into a universal
platform guarantee.

Every first attempt receives a complete-source review by a different strong
Sol agent. Only unchanged-hash, non-semantic corrections may receive targeted
review. Factual, authority, material-omission, lifecycle, contradiction, or
shared-evidence defects require a complete retry and complete review.

## Success and close gates

- Five of five sources finally approved; at least four pass on attempt 1.
- No rejected job, coordinator semantic repair, or more than one full semantic retry.
- Fixed audit passes all nine factual, boundary or contradiction, and exact raw deep-dive checks.
- Canonical sources equal their approved candidates and appear exactly once in company and provider indexes.
- Reviewer-approved primary concept updates and reciprocal links appear exactly once.
- Targeted wiki validation, capsule validation, raw hashes, counts, links, and `git diff --check` run once at close.
- Target elapsed time is 30–35 minutes; timing remains observational and never waives quality.

## Authorization boundary

This proposal and `manifest.json` do not initialize Campaign 32 or authorize
agent dispatch. Explicit approval of this exact manifest would authorize only
the five complete raw reads, five new source targets, distinct per-page Sol
reviews, bounded retries, approved primary-concept updates, catalog/count/log
updates, fixed audit, close checks, and one local campaign commit.

It does not authorize a sixth page, refresh of an existing source, bulk ingest
of the remaining inventory, reviewer sampling, Luna or Terra, rule or code
changes, cross-PSP rollout, remote push, or unrelated-file edits.
