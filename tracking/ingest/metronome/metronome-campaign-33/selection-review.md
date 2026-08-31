# Metronome Campaign 33 five-page first-pass proposal

**Status:** Approved and executed on 2026-08-31
**Mode:** Five new Minimum Sufficient Sources from never-ingested canonical pages
**Current baseline:** 226 current English canonical pages; 156 official-document sources; 70 canonical pages never ingested

## Goal

Keep the five-page production pressure test while improving first-pass
completeness. Campaign 33 uses one high-risk schema-heavy financial mutation
and four medium-risk pages across temporal reads, lifecycle mutation,
deprecated reporting, and notification configuration. It does not reduce the
page count or raw-line workload to manufacture a faster result.

The campaign reuses the mature controls: one complete raw read per worker, one
isolated Minimum Sufficient Source, a different strong Sol complete-source
reviewer, three dynamic native-agent slots, coordinator-only canonical writes,
bounded retries, and one mature close validation. It adds no registry,
classifier, scheduler state, validator, prompt layer, or performance system.

## Mechanical selection boundary

Selection reconciled the immutable 80-page pre-Campaign-31 planning snapshot
against current official-document source canonical URLs. Campaigns 31 and 32
covered ten of those pages, leaving 70 currently uncovered. Selection then
used documentation path, page title and introductory header, latest raw path,
line count, and source-target absence. Raw bodies were not read end to end and
no metadata-only fact or `raw_reference` disposition is authorized.

| Job | Raw lines | Risk | Archetype | Selection reason |
| --- | ---: | --- | --- | --- |
| `create-historical-invoices-new-source` | 1,054 | high | API Mutation / Financial Backfill | The sole high-risk control; tests contract and historical-period scope, preview-versus-creation authority, custom usage-line schema, invoice-state and reconciliation boundaries, POST idempotency, and exact raw routing without copying the full schema |
| `create-alert-specifiers-new-source` | 254 | medium | Guide / Balance Segmentation | Tests default combined-balance behavior, include, exclude, and grouping configuration, custom-field authority, alert evaluation and delivery boundaries, worked patterns, and merchant-owned response behavior |
| `get-subscription-seats-history-new-source` | 299 | medium | API Read / Temporal History | Tests subscription identity, covering-date and range filters, schedule and quantity history, temporal completeness, returned ordering, and future-versus-recorded-state boundaries |
| `update-a-billable-metric-new-source` | 185 | medium | API Mutation / Metric Lifecycle | Tests name-only mutation versus immutable calculation configuration, replacement workflow boundaries, POST idempotency, response identity, propagation, and historical reporting unknowns |
| `get-customer-costs-new-source` | 255 | medium | API Read / Deprecated Plans | Tests daily pending-cost scope, credit and line-item breakdowns, unsupported metric boundary, deprecated Plans authority versus Contracts migration, and completeness, invoice, and downstream limits |

The five latest raws total 2,047 lines, close to Campaign 32's 1,968-line
workload. Dispatch the historical-invoice page, alert-specifier guide, and
subscription-seat history first so the longest complete read overlaps two
independent medium pages. The fixed close audit uses
`create-historical-invoices-new-source`,
`create-alert-specifiers-new-source`, and
`update-a-billable-metric-new-source` to cover the schema-heavy mutation, the
guide, and an ordinary mutation.

## Worker and review contract

Each worker must read its complete assigned raw and relevant current
concept/source context, then return one Minimum Sufficient Source. Preserve
query-critical durable facts, material contradictions and unknowns, primary
concept routes, a raw-detail coverage map, and the exact path-qualified raw
backlink without reconstructing the complete procedure or schema.

Campaign 32's observed first-pass gaps become direct submission reminders,
not a new checklist or validator:

- identify every primary concept route and its reciprocal fact-bearing source link;
- name the exact authority for cross-source currency, invoice, lifecycle, or migration claims;
- distinguish an undocumented response schema or example from an asserted empty runtime response;
- directly quote any numeric worked example whose unit or interpretation affects the summary.

For API pages, distinguish request-body requiredness from payload-field
requiredness, retain fields under their immediate parent schemas, and separate
endpoint-local identity from API-wide POST idempotency. Preserve lifecycle,
visibility, concurrency, partial-result, downstream, and recovery unknowns
when the page does not establish them. For the guide, keep alert configuration,
evaluation, delivery, balance mutation, invoicing, and merchant-owned customer
action as separate authorities.

Every first attempt receives a complete-source review by a different strong
Sol agent. Only unchanged-hash, non-semantic corrections may receive targeted
diff review. Factual, authority, material-omission, lifecycle, contradiction,
or shared-evidence defects require a complete retry and complete review.

## Success and close gates

- Five of five sources finally approved; at least four pass on attempt 1.
- No rejected job, coordinator semantic repair, or more than one full semantic retry.
- Fixed audit passes all nine factual, boundary or contradiction, and exact raw deep-dive checks.
- Canonical sources equal their approved candidates and appear exactly once in company and provider indexes.
- Reviewer-approved primary concept updates and reciprocal links appear exactly once.
- Targeted wiki validation, capsule validation, raw hashes, counts, links, and `git diff --check` run once at close.
- Target elapsed time is at most 45 minutes; timing remains observational and never waives quality.

## Authorization boundary

This proposal and `manifest.json` do not initialize Campaign 33 or authorize
agent dispatch. Explicit approval of this exact manifest would authorize only
the five complete raw reads, five new source targets, distinct per-page Sol
reviews, bounded retries, approved primary-concept updates, catalog/count/log
updates, fixed audit, close checks, and one local campaign commit.

It does not authorize a sixth page, refresh of an existing source, bulk ingest
of the remaining inventory, reviewer sampling, Luna or Terra, rule or code
changes, cross-PSP rollout, remote push, or unrelated-file edits.
