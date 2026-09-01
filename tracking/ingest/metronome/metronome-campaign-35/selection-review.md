# Metronome Campaign 35 provider-preflight calibration proposal

**Status:** Approved, executed, and closed; final quality 5/5 and fixed audit 9/9
**Mode:** Five new Minimum Sufficient Sources from canonical pages without source coverage
**Current baseline:** 226 current English canonical pages; 166 official-document sources; 60 canonical pages without source coverage

## Goal

Test the smallest Campaign 34 correction: whether one precise Metronome
provider-wide POST execution-admission reminder reduces avoidable retries
without adding a registry, validator, classifier, scheduler feature, prompt
layer, or monitoring system. The campaign retains five pages and the existing
strong Sol worker plus different strong Sol complete-source reviewer model.

Campaign 35 uses four POST operations that must apply the reminder and one GET
negative control that must not inherit it. All five canonical identities lack
a source and have not appeared in an earlier ingest manifest. This avoids
reusing failed candidates or historical worker answers while still retaining
financial, usage, product, legacy migration, and alert-lifecycle pressure.

## Mechanical selection boundary

Selection normalized optional `.md` suffixes and reconciled the current
226-page selected English inventory against 166 official-document source
canonical URLs, leaving 60 uncovered identities. It then used only prior
manifest membership, documentation path, title, introductory header, operation
method visible at the page head, latest raw path, line count, and exact
source-target absence. Raw bodies were not read end to end. These signals
choose the calibration mix but do not authorize source facts, concept updates,
or a routing disposition.

| Job | Raw lines | Risk | Archetype | Selection reason |
| --- | ---: | --- | --- | --- |
| `add-a-manual-balance-entry-new-source` | 233 | high | API Mutation / Financial Ledger | Financial correction control spanning durable ledger events, commit or credit balance, upstream invoice recalculation, and replay-versus-current-state boundaries |
| `get-batched-usage-data-new-source` | 335 | medium-high | API POST Read / Batched Usage | Exercises time windows, multi-customer and multi-metric aggregation, grouping, pagination, analytics completeness, cursor parameter changes, and replay freshness |
| `create-a-product-new-source` | 358 | medium | API Mutation / Product Creation | Exercises request requiredness, product and invoice-line identity, custom fields, later pricing boundaries, response placement, and creation replay |
| `list-customer-plans-new-source` | 244 | medium | Legacy GET / Plans | Negative control: a deprecated reverse-chronological GET requiring current Contracts routing but no POST idempotency fact |
| `archive-a-threshold-notification-new-source` | 217 | high | API Mutation / Alert Lifecycle | Conflict-pressure control spanning all-customer monitoring scope, irreversible archive claims, uniqueness-key release, retained history, current alert authority, and replay versus resource lifecycle |

Total assigned raw size is 1,387 lines, compared with Campaign 34's 2,062.
Dispatch Manual Balance Entry, Batched Usage, and Archive Threshold Notification
first so the two high-risk pages overlap the paginated POST read. The fixed
close audit uses those same three pages to cover financial mutation, POST read,
and alert lifecycle.

No fresh never-manifested guide remains in the 60-page uncovered set. The
remaining uncovered guides all carry Campaign 13–15 pilot history. Excluding
them keeps this calibration independent; it does not conclude that the refined
preflight is validated for guides.

## Worker and review contract

Each worker reads its complete assigned raw, the Minimum Sufficient Source
playbook, relevant current authority sources, and only the matching archetype
lesson. It returns one isolated candidate, exact evidence, primary concept
routes, reciprocal shared proposals, a raw-detail coverage map, and the exact
path-qualified raw backlink.

For each of the four POST jobs, the first attempt must preserve the scoped
provider-wide rule: result persistence starts only after validation passes and
no pre-execution concurrent-request conflict prevents execution; only a
persisted result can replay for identical same-key parameters, while changed
parameters conflict. It must remain separate from endpoint-local uniqueness,
freshness, propagation, concurrency, failure, and recovery. The GET control
must not receive this POST rule.

A different strong Sol agent performs one complete-source review. Before
returning `changes_requested`, it consolidates all visible blockers across the
provider-wide rule, endpoint and current dedicated authorities, defaults and
requiredness, examples versus schema, primary concepts, reciprocal links, and
coverage map. Only unchanged-hash, non-semantic corrections may receive
targeted diff review; factual, authority, lifecycle, contradiction, or material
omission defects require a complete retry and complete review.

## Success and close gates

- Five of five sources finally approved; at least three pass on attempt 1.
- No more than eight total worker attempts, no rejected job, and no coordinator semantic repair.
- No retry is caused by omitting or misstating the POST execution-admission boundary.
- The GET negative control does not import the POST Idempotency-Key rule.
- A later complete review does not newly identify a material blocker already visible in the unchanged first-attempt raw and authority context.
- Fixed audit passes all nine factual, boundary or contradiction, and exact raw deep-dive checks.
- Canonical sources equal approved candidates; primary reciprocal links and reviewer-approved shared updates appear exactly once.
- Existing targeted wiki, capsule, hash, count, link, query-audit, and diff checks run once at close.
- Target elapsed time is at most 45 minutes; timing remains observational and never waives quality.

Passing these gates validates only this narrow API-page preflight correction.
It does not validate guide ingestion, another PSP, reviewer removal, a larger
campaign, or bulk rollout.

## Authorization boundary

This proposal and `manifest.json` do not initialize Campaign 35 or authorize
agent dispatch. Explicit approval of this exact manifest would authorize only
the five complete raw reads, five new source targets, distinct per-page strong
Sol reviews, bounded retries, approved primary-concept updates, catalog/count/
log updates, fixed audit, close checks, and one local campaign commit.

It does not authorize a sixth page, reuse of earlier campaign candidates,
refresh of an existing source, bulk ingest of the remaining inventory, reviewer
sampling or removal, Luna or Terra, rule or code changes, cross-PSP rollout,
remote push, or unrelated-file edits.
