# Metronome Campaign 34 preflight-calibration proposal

**Status:** Exact manifest executed and closed on 2026-09-01
**Mode:** Five new Minimum Sufficient Sources from never-ingested canonical pages
**Current baseline:** 226 current English canonical pages; 161 official-document sources; 65 canonical pages never ingested

## Goal

Test whether the strengthened worker and reviewer preflights improve first-pass
completeness without changing the scheduler or reducing the five-page workload.
Campaign 34 uses one authority-fan-out guide and four medium API pages across
usage analytics, alert monitoring, customer configuration, and product
lifecycle. Its 2,062 raw lines remain comparable with Campaign 33's 2,047.

The campaign keeps the mature controls: one complete raw read per worker, one
isolated Minimum Sufficient Source, a different strong Sol complete-source
reviewer, three dynamic native-agent slots, coordinator-only canonical writes,
bounded retries, and one mature close validation. It adds no registry,
classifier, scheduler state, validator, prompt layer, or performance system.

## Mechanical selection boundary

Selection normalized optional `.md` suffixes and reconciled the current
226-page selected English inventory against the 161 official-document source
canonical URLs, leaving 65 uncovered identities. It then used documentation
path, title and introductory header, latest raw path, line count, and exact
source-target absence. Raw bodies were not read end to end. These metadata and
header signals choose the calibration mix but do not authorize source facts,
concept updates, or a `raw_reference` disposition.

| Job | Raw lines | Risk | Archetype | Selection reason |
| --- | ---: | --- | --- | --- |
| `customer-dashboards-and-reporting-new-source` | 724 | high | Guide / Customer Reporting | The sole high-risk authority-fan-out control: its header spans API-powered usage, spend, balance, invoice, self-serve, data-export, and embeddable-dashboard surfaces, so the complete read must reconcile worked requests and responses with current dedicated authorities rather than treating guide examples as complete contracts |
| `get-usage-data-with-paginated-groupings-new-source` | 482 | medium | API Read / Dimensional Usage | Tests customer and billable-metric scope, complete compound grouping, filtering, window and pagination placement, analytics completeness, primary reporting routes, and exact evidence without reproducing the full schema |
| `get-all-threshold-notifications-new-source` | 529 | medium | API List / Alert Monitoring | Tests customer scope, default and explicit status filters, configuration versus current evaluation state, pagination, response placement, freshness and completeness unknowns, and alert, reporting, and dashboard query routes |
| `update-customer-configuration-new-source` | 158 | medium | API Mutation / Customer Configuration | Tests customer identity, integration and billing configuration scope versus core customer data, supplied-payload requiredness, API-wide POST idempotency, response placement, propagation, failure, and recovery boundaries |
| `archive-product-new-source` | 169 | medium | API Mutation / Product Lifecycle | Tests existing-rate behavior versus new-rate availability, irreversibility and retained visibility, API-wide POST idempotency, response identity, failure, propagation, and historical-rating unknowns |

Dispatch the customer-dashboard guide, paginated usage read, and alert list
first so the longest complete read overlaps two independent medium pages. The
fixed close audit uses `customer-dashboards-and-reporting-new-source`,
`get-all-threshold-notifications-new-source`, and
`archive-product-new-source` for the longest authority-fan-out guide, an
ordinary API list, and the short standard lifecycle page.

## Worker and review contract

Each worker must read its complete assigned raw and relevant current
concept/source context, then return one Minimum Sufficient Source. Preserve
query-critical durable facts, material contradictions and unknowns, every
primary concept route, a raw-detail coverage map, and the exact path-qualified
raw backlink without reconstructing the complete procedure or schema.

The generated worker order carries the strengthened preflight:

- compare every retained guide request and response field against current
  dedicated API authorities, preserving omitted-field blast radius, defaults,
  units, requiredness, field names, enums, and contradictions;
- distinguish request-body requiredness, required payload properties, and
  open-object behavior, and directly ground query-critical method, path,
  authentication, and immediate-parent response placement;
- separate API-wide POST idempotency from endpoint-local uniqueness, freshness,
  concurrency, propagation, failure, and recovery behavior;
- audit every realistic query route and return fact-bearing reciprocal source
  proposals for all primary concepts rather than stopping at the first match.

Every first attempt receives a complete-source review by a different strong
Sol agent. Before returning `changes_requested`, the reviewer performs one
blocker-completeness pass across the coverage map, worked examples, dedicated
authorities, primary query routes, and reciprocal links and returns all
currently visible material blockers together. Only unchanged-hash,
non-semantic corrections may receive targeted diff review. Factual, authority,
material-omission, lifecycle, contradiction, or shared-evidence defects require
a complete retry and complete review.

## Success and close gates

- Five of five sources finally approved; at least four pass on attempt 1.
- No rejected job, coordinator semantic repair, or more than one full semantic retry.
- A later full review must not newly identify a material blocker already visible in the unchanged first-attempt raw and authority context; if it does, record the reviewer-completeness calibration as failed even when final quality passes.
- Fixed audit passes all nine factual, boundary or contradiction, and exact raw deep-dive checks.
- Canonical sources equal their approved candidates and appear exactly once in company and provider indexes.
- Reviewer-approved primary concept updates and reciprocal links appear exactly once.
- Targeted wiki validation, capsule validation, raw hashes, counts, links, and `git diff --check` run once at close.
- Target elapsed time is at most 45 minutes; timing remains observational and never waives quality.

## Authorization boundary

This proposal and `manifest.json` do not initialize Campaign 34 or authorize
agent dispatch. Explicit approval of this exact manifest would authorize only
the five complete raw reads, five new source targets, distinct per-page Sol
reviews, bounded retries, approved primary-concept updates, catalog/count/log
updates, fixed audit, close checks, and one local campaign commit.

It does not authorize a sixth page, refresh of an existing source, bulk ingest
of the remaining inventory, reviewer sampling, Luna or Terra, rule or code
changes, cross-PSP rollout, remote push, or unrelated-file edits.
