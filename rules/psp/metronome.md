# Provider: Metronome - collection profile

> Used with `rules/psp-collection.md` and `scripts/psp_config.toml`. Verified 2026-07-13.

## Ownership and wiki placement

Metronome is a Stripe-owned usage-based billing platform with an independent provider capsule:

- Raw root: `raw/metronome/`
- Provider index: `wiki/metronome-index.md`
- Provider log: `wiki/metronome-log.md`
- Company page: `wiki/companies/metronome.md`
- Source summaries: `wiki/sources/metronome/`
- Concepts: `wiki/concepts/metronome/`

## Discovery sources

| Source | URL | Purpose |
| --- | --- | --- |
| LLM index | `https://docs.metronome.com/llms.txt` | Markdown targets and OpenAPI artifacts |
| Sitemap | `https://docs.metronome.com/sitemap.xml` | Canonical-page coverage and gap detection |

Collect the English union. Exclude `/fr/`, `https://metronome.com/blog`, and `https://status.metronome.com/`, recording each exclusion.

## Pilot baseline

- 208 pages shared by both discovery sources
- 17 additional English sitemap-only pages
- 225 selected English documentation pages
- 2 separate OpenAPI JSON artifacts
- 105 excluded French-localized pages

Treat these as drift-detection baselines, not permanent constants.

## Commands

```bash
python3 scripts/fetch_psp.py metronome --dry-run
python3 scripts/fetch_psp.py metronome --limit 3
python3 scripts/validate_metronome_capsule.py
```

Do not run the full corpus until the limited smoke test, monitor reconciliation, immutable rerun check, and user checkpoint all pass.

After collection and before any ingest pilot, run the capsule validator. It reports the nested pending-ingest queue and fails on source/raw/index/count drift. Collection does not create or update source summaries and never starts ingest.

## Boundary

Collection ends after raw files, run records, aggregate status, and manifest validation. It never starts ingest automatically.

## Worker handoff

For coordinator-controlled ingest, dispatch the generated worker order without retyping its trusted values. Before returning a candidate, the worker must use the order's preflight:

- Copy `canonical_url` exactly into the source-page frontmatter; do not substitute the raw page's fetch URL.
- Return exactly the top-level keys listed in `result_contract.top_level_keys`.
- Give every grounding quote non-empty `text` and `location` values.
- For OpenAPI pages, distinguish the enclosing `requestBody` requiredness from required properties inside its payload schema, and do not infer unknown-field behavior when `additionalProperties` is unspecified.
- For every POST operation, check the existing Metronome API-wide idempotency authority and separate its guarantees from endpoint-specific retry, concurrency, freshness, and recovery unknowns.
- For each durable fact, audit every relevant existing Metronome concept and propose the required reciprocal source links instead of stopping after the first plausible concept.

These are submission checks, not new campaign state. The existing validator remains the fail-closed authority, and an invalid result follows the existing bounded retry path.

These three semantic checks were added after Campaign 19. They are worker reminders, not deterministic proof and not a replacement for independent review.

## Parallel-review campaign allocation

Metronome is explicitly authorized to use the coordinator-controlled exception
in `rules/ingest.md` after the exact campaign manifest is approved. This
authorization is Metronome-specific; every other provider remains serial-only
until its own provider rule grants equivalent authorization.

The coordinator is fixed. All remaining native-agent capacity is a dynamic
pool; worker and reviewer slots are not reserved in advance. At each dispatch:

```text
free_slots = total_subagent_slots - active_workers - active_reviewers
worker_reserve = 1 if queued_jobs > 0 and active_workers == 0 else 0
review_slots = min(candidate_ready, review_cap, free_slots - worker_reserve)
```

Every new worker or reviewer order must fit `free_slots`. Reserve one worker
slot only when queued source jobs remain and no worker is already active; an
active worker satisfies the reserve. Start ready reviews up to `review_slots`,
then fill the remaining free slots with queued workers:

- If no candidate is ready, fill available capacity with workers.
- When a worker finishes, release its slot and prefer a fresh strong reviewer
  for a ready candidate.
- Never start more reviewers than ready candidates.
- Do not delay a ready review merely to reserve another worker slot when a
  worker is already active.
- When the worker queue is empty, all available sub-agent slots may review.
- The reviewer must be a different agent from the candidate's worker.

With the current Codex capacity of three sub-agent slots beside the
coordinator, the intended allocation is:

| Ready candidates | Queued jobs | Reviewers | Workers |
| ---: | --- | ---: | ---: |
| 0 | yes | 0 | 3 |
| 1 | yes | 1 | 2 |
| 2+ | yes | 2 | 1 |
| 1 | no | 1 | 0 |
| 2 | no | 2 | 0 |
| 3+ | no | 3 | 0 |

Backend capacity is discovered at runtime. The campaign's configured
concurrency is a ceiling, not a promise that every platform exposes that many
native agents.

## Campaign 08 mature-mode routing and operation

Campaign 08 and later Metronome campaigns use simplified production mode only
after the exact campaign manifest is approved. Sol is the default worker.
Terra is limited to genuinely templated, isolated pages that need no semantic
update to a shared concept; every first attempt still receives an independent
complete-source Sol review by an agent other than its worker.

Keep three dynamic sub-agent slots beside the coordinator. A completed worker
or reviewer immediately releases its slot for a ready review or the next
queued worker; do not wait for a batch barrier. For a bounded unchanged-hash
retry covering only links, frontmatter, wording, or an already-identified
omitted field, use targeted diff review and prefer the Sol reviewer that
requested the change. If that reviewer is unavailable, another Sol reviewer
may perform the same targeted check; any factual, uncertain, or broader
correction receives a full complete-source review.

The coordinator remains the only canonical writer and explicitly completes
the campaign after its terminal approval and campaign-close checks. It records
only `started_at` and `completed_at`, consumes the reviewer-approved
`shared_update_plan`, and runs the campaign-close wiki, capsule, and
predetermined three-page query-audit validations once. In close-only mode it
groups updates by exact target and applies each target once; the incremental
mode below instead applies each approved update once while keeping all writes
serial. The coordinator does not perform a default third full-source reread.

## Incremental promotion after approval

For future explicitly approved Metronome campaigns, the coordinator may use
idle time while unrelated workers and reviewers continue. As soon as one job
has an `approved` review, the coordinator may serially apply that job's
reviewer-approved concept updates, promote its approved candidate, and run the
targeted checks for those files. Concept updates still precede that source.

This permission does not allow workers or reviewers to write canonical files,
does not allow promotion from `candidate_ready` or `reviewing`, and does not
change the campaign's retry or review gates. The coordinator resolves shared
target collisions in approval order and checks every approved `update_id`
exactly once at close. Company, provider index, provider log, aggregate counts,
capsule validation, the fixed query audit, and the full campaign commit remain
one close-stage operation. If the campaign pauses, stop new promotion work and
retain already promoted approved pages as recoverable campaign state.

## Campaign 09 compact production mode

Campaign 09 and later retain the same worker, reviewer, targeted-retry, and
three-page audit quality gates, but remove avoidable approval and close-stage
work:

- A reviewer may list an approved shared update as its `update_id` string in
  `shared_update_decisions`. Only a rejected update needs the legacy object
  with `update_id`, `verdict: rejected`, and a concise `reason`. Legacy detailed
  approval objects remain valid for existing campaign evidence.
- Workers leave the `company`, `index`, and `log` suggestion arrays empty.
  At campaign close, the coordinator derives one company catalog entry and one
  provider-index entry per approved source from the canonical source wikilink
  and title, writes one consolidated campaign-log entry from the manifest and
  approved job records, and recomputes counts from the promoted corpus. These
  mechanical entries do not require per-entry reviewer prose.
- Workers continue to suggest only fact-bearing concept changes, reciprocal
  source links, and contradictions that require semantic judgment.
- The coordinator groups approved concept suggestions by exact target and
  applies each target once. Do not spawn a separate shared-close proposal
  agent by default. Request a narrow additional review only for an actual
  conflict or unresolved semantic uncertainty.

This is a throughput simplification, not a weaker content gate: first attempts
still receive full-source independent Sol review, bounded unchanged-hash fixes
still receive targeted review, canonical sources must still equal approved
candidates, and the existing close validators and immutable query sample still
run once.

## Campaign 11 worker routing

Campaign 11 and later Metronome production campaigns use Sol for every worker.
Terra remains disabled for Metronome production ingest unless a separately
approved future pilot demonstrates that it can meet the same concept-update and
quote-grounding gate. This changes only worker routing; the existing independent
Sol review, retry, coordinator ownership, and campaign-close gates remain the
same.

After the coordinator generates a worker order, dispatch that native agent and
confirm that the dispatch returned an agent identifier before processing other
completion events. Order generation alone is not evidence that a worker is
active. If dispatch is interrupted, reconcile that job and its existing order
before issuing another order. This is an operating discipline only; do not add
a second scheduler, state schema, or monitoring layer for it.

## Campaign 12 selective-ingest pilot authorization

Campaign 12 is a bounded Metronome-only calibration pilot and may begin only
after its exact manifest is explicitly approved. It runs outside the production
campaign scheduler and schema; do not pass its manifest to
`manage_ingest_pilot.py` or create a second scheduler, state schema, or
monitoring layer.

All five native agents are Sol: the overview worker, overview reviewer,
create-key raw-reference auditor, delete-key semantic-triage worker, and
delete-key semantic-triage reviewer. Dispatch exactly three simultaneous
initial native tasks: overview source generation, the create-key raw-reference
audit, and delete-key semantic triage. As slots free, dispatch an independent
overview reviewer and an independent delete-key triage reviewer. Preserve the
dispatch-confirm discipline above for every order.

Only the overview task may generate a source candidate. Do not generate a
source for create-key or delete-key during this pilot. The create-key audit
tests its `raw_reference` classification. The delete-key task decides its
future disposition; reviewer disagreement promotes that future disposition to
`source_required` and is recorded once without a retry loop.

The overview may list the five endpoint pages under
`## Related raw API references`, but those navigation-only links cannot support
overview facts. The other three classified endpoint pages receive no native
task and no complete read in this pilot.

## Post-Campaign 12 selective-routing calibration

Campaign 12 ended with `verdict = revise_routing_rule`. The metadata-only route
for `Create a Custom Field Key` was unsafe because the sampled page uniquely
carried required-field, durable failure, uniqueness, managed-entity, and
invoice-propagation facts.

```text
unsafe old route = Create a Custom Field Key -> raw_reference
corrected metadata route = Create a Custom Field Key -> semantic_triage
observed complete-read result = source_required
```

Apply the shared endpoint rule in `rules/ingest.md`: when metadata cannot rule
out unique durable endpoint facts, require semantic triage rather than direct
`raw_reference` classification. This calibration does not promote every API
endpoint; after a complete read, another endpoint may still resolve to
`raw_reference`.

Do not alter the completed Campaign 12 manifest or evidence, reclassify the
remaining corpus, create a routing registry, or treat this calibration as
authorization for a new campaign.

## Post-Campaign 13 sampled-review calibration

Campaign 13 tested Luna Max workers with independent full-source review on a
fixed audit sample. Both completed audit reviews found material semantic or
grounding problems. Promotion was held, the remaining jobs were not dispatched,
and no candidate or shared suggestion was promoted to the canonical wiki.

Preserve the campaign directory as negative-calibration evidence. Do not resume
its queued jobs, promote its mechanically approved candidates, or initialize a
new `audit_only` campaign. The runtime rejects `review_policy: "audit_only"`.

## Post-Campaign 14 no-review calibration

Campaign 14 tested five Sol-medium full-read workers against independent
Sol-high complete-source review. The result was `0/5`: every page required a
material semantic correction after deterministic validation, including missed
contradictions, accounting and integration boundaries, API-schema details, or
shared-concept updates. No canonical wiki content was promoted.

Keep independent strong-model review for every Metronome source candidate and
its shared semantic suggestions. Deterministic hash, quote, schema, URL, and
link checks remain mandatory but do not replace semantic review. Do not resume
Campaign 14 retries or generalize a no-review policy to another provider. Any
future optimization requires a new bounded manifest and explicit approval.

## Campaign 23 Minimum Sufficient Source pilot authorization

Campaign 23 is a bounded five-page Metronome-only pilot and may be initialized
only after its exact manifest is explicitly approved. It changes source
granularity and the review blocking contract, not collection, routing,
scheduling, result schemas, model routing, or close validation.

Each strong-model worker reads the complete assigned raw page, the campaign
playbook, and only the matching section of
`tracking/ingest/metronome/lessons.md`. It produces one Minimum Sufficient
Source with an overview, query-critical durable facts, material boundaries or
contradictions, a raw-detail coverage map, primary concept routes, and the
exact path-qualified raw backlink. Numeric ranges in the playbook are semantic
guidance and are not hard caps.

A different strong-model reviewer reads the complete assigned raw page and
applies the same archetype overlay. `changes_requested` is limited to a core
factual error, a material omission that changes an integration decision, an
authority error, a missing material contradiction, a missing or incorrect
primary concept, a broken evidence route, or a coverage-map gap that hides an
entire detail category central to the page purpose.

Secondary concept gaps, ordinary schema details left in raw, non-material
wording or formatting, mechanically repairable quote ranges, and mechanical
company/index/log work are non-blocking. The reviewer returns `approved`,
records any such follow-up in the existing `reason`, and approves or rejects
the existing shared update IDs normally. Do not add a `coordinator_actions`
schema field.

Use targeted review only for an unchanged-hash bounded correction whose exact
scope was identified by the prior complete review. Core misunderstanding,
material omission, authority confusion, new factual meaning, or unresolved
contradiction receives a full semantic retry and complete review. Secondary
issues do not consume a worker attempt.

The coordinator accepts the reviewer verdict, performs bounded non-semantic
repairs, applies approved primary concept changes, verifies reciprocal links,
promotes canonical sources, and runs close checks. It does not perform a
default third complete raw read. Campaign close records first-pass approvals,
bounded retries, full semantic retries, attempts, elapsed time, query audit,
raw deep-dive success, and primary-concept reciprocity using existing files
only.

This authorization does not apply to Campaign 22 evidence, another provider,
reviewer sampling, a larger campaign, or bulk migration.

## Campaign 24 Minimum Sufficient Source confirmation authorization

Campaign 24 is authorized only for the exact eight jobs and three audit job
IDs in its approved manifest. It reuses the unchanged Campaign 23 Minimum
Sufficient Source playbook and matching archetype lessons; it does not change
collection, routing, result schemas, model routing, retry policy, or close
validation.

Every job uses a strong Sol worker and a different strong Sol complete-source
reviewer. Keep three dynamic native-agent slots beside the coordinator and no
batch barrier. Persist the trusted review order before reviewer dispatch. Once
one job is independently approved, the coordinator may serially apply only
that job's approved primary-concept changes, promote its exact candidate, and
run targeted checks while unrelated agents continue. Company, provider index,
provider log, counts, capsule validation, fixed query audit, and the campaign
commit remain one close-stage operation.

`api-quickstart`, `system-notifications`, and `manage-seats` are fresh Campaign
24 jobs. Do not read or reuse their earlier campaign candidates, receipts,
suggestions, failures, or reviews as source evidence. This authorization does
not permit a ninth page, reviewer sampling, Luna or Terra routing, another
provider, cross-PSP rollout, or bulk migration.

## Campaign 25 shadow risk-review authorization

Campaign 25 is authorized only for the exact six jobs and three audit job IDs
in its approved manifest. It is a shadow calibration of reviewer coverage, not
a live sampled-review policy. The existing scheduler remains
`review_policy: per_page`, and every source candidate receives a complete raw
read by a different strong Sol reviewer before canonical promotion.

The three preliminary mandatory jobs are `edit-a-contract`,
`list-seat-balances`, and `netsuite`. The provisional sample pool is
`get-a-threshold-notification`, `get-plan-details`, and `sdks`, with
`get-a-threshold-notification` fixed as the immediate shadow sample. A worker
that finds a state or lifecycle transition; financial semantics; durable
failure, retry, idempotency, concurrency, or propagation behavior;
cross-system authority or reconciliation boundaries; or material schema,
time-window, pagination, requiredness, or narrative conflict must report the
trigger using its existing quote locations. That report escalates a
provisional job to mandatory review before the simulated cutoff. A mandatory
job cannot be downgraded.

If the fixed sample remains eligible and passes its complete review, the
coordinator records the time and exact candidate set the proposed policy would
have released, then dispatches the two deferred shadow reviews. If the sample
is escalated, the shadow result is inconclusive; if it has a material defect,
the shadow policy fails. Any material defect or missed escalation found by a
deferred review yields `revise_risk_rule`. In every outcome, real promotion
waits for all applicable per-page reviews and existing close gates.

Record the preliminary route, worker escalation decision, simulated cutoff,
and deferred-review findings in existing Campaign 25 evidence only. Do not add
a result-contract field, registry, score, classifier agent, scheduler state,
validator, or performance-monitoring layer. This authorization does not permit
an unreviewed canonical source, a seventh page, Luna or Terra routing, another
provider, cross-PSP rollout, or bulk migration.

## Post-Campaign 25 planning and close simplification

For each separately approved later Metronome campaign, use the raw corpus
metadata already available during selection to consider total raw lines, the
largest single page, and semantic risk in addition to page count. This is an
advisory dispatch order, not new manifest or scheduler state: start the longest
or highest-risk pages first so their complete reads overlap shorter work and do
not become avoidable tail latency. Keep the existing dynamic slots, per-page
strong Sol worker and independent strong Sol reviewer, bounded retry policy,
and coordinator-owned promotion unchanged.

For a documentation-only campaign close, follow the mature close path already
defined in `rules/ingest.md`: run the targeted wiki and capsule checks plus the
existing hash, link, count, query-audit, and diff checks. Run the full unit suite
only when the campaign changes code, rules, or validators. Do not add a
registry, timing schema, scheduler feature, or performance-monitoring layer to
implement this ordering or close-path choice.
