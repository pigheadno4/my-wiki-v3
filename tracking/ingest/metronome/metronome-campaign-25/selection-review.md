# Metronome Campaign 25 shadow risk-review proposal

**Status:** Awaiting exact-manifest approval
**Mode:** Six-page dry-run calibration with actual per-page review and a shadow risk-based cutoff
**Source baseline:** 225 canonical raw pages, 145 source pages, 86 raw pages without source summaries

## Goal

Test whether a conservative review-risk route could reduce independent semantic
reviews without placing an unreviewed source into the canonical wiki. The only
policy under calibration is reviewer coverage. Strong Sol workers, complete raw
reads, the Minimum Sufficient Source contract, existing result schemas,
coordinator ownership, retries, promotion checks, and close validation remain
unchanged.

Campaign 25 is a shadow experiment. The existing scheduler continues to use
`review_policy: per_page`, and every candidate receives a different strong Sol
complete-source reviewer before real promotion. The coordinator records the
time at which the proposed risk policy would have considered the provisional
group releasable, then dispatches the deferred reviews. Those later reviews
measure possible semantic escapes; they are not omitted from the real campaign.

## Metadata-only selection

Selection used raw path, source URL header, line count, SHA-256, prior-manifest
membership, source-target absence, and the capsule pending list. No selected raw
body was read to prepare this proposal. All six source targets are absent, all
six raw pages remain in the pending list, and none of the six job IDs appears in
an earlier Metronome manifest.

| Job | Lines | Preliminary archetype | Shadow route | Metadata-visible reason |
| --- | ---: | --- | --- | --- |
| `edit-a-contract` | 4,532 | API Mutation | mandatory full review | State-changing contract mutation and longest/schema-heaviest page |
| `list-seat-balances` | 503 | API List / Schema | mandatory full review | Financial balances, collection completeness, and schema interpretation |
| `netsuite` | 456 | Integration Guide | mandatory full review | Cross-system responsibility, invoice delivery, and reconciliation boundaries |
| `get-a-threshold-notification` | 619 | API Read | provisional sample pool | Read-only retrieval with no mutation visible from metadata |
| `get-plan-details` | 280 | API Read | provisional sample pool | Compact read-only plan retrieval; worker must escalate if financial or lifecycle semantics appear |
| `sdks` | 947 | Reference Overview | provisional sample pool | SDK/reference routing page with no state change visible from metadata |

`get-a-threshold-notification` is the fixed immediate shadow sample.
`get-plan-details` and `sdks` are the two deferred shadow reviews. The fixed
campaign-close query audit covers `edit-a-contract`,
`get-a-threshold-notification`, and `sdks`.

## One-way risk escalation

The preliminary route is not a permanent page label. Each worker already reads
its complete assigned raw and reports whether it found any of these triggers:

- state mutation or lifecycle transition;
- financial, accounting, pricing, balance, credit, invoice, tax, or revenue semantics;
- durable failure, retry, idempotency, concurrency, or propagation behavior;
- cross-system authority, delivery, settlement, or reconciliation boundaries;
- nested requiredness, material pagination/completeness, time-window, or schema-versus-narrative conflict.

A provisional job that finds any trigger is escalated to mandatory full review
before the shadow cutoff. A mandatory job can never be downgraded. The worker
uses its existing quote locations to support the escalation note; Campaign 25
does not add a result-contract field, registry, score, classifier agent, or
state transition.

## Shadow execution

1. Run all six jobs through the existing Campaign 24 Minimum Sufficient Source
   worker contract, with at most three native agents beside the coordinator.
2. Dispatch complete-source reviews immediately for the three mandatory jobs.
3. After the provisional workers finish, record their one-way escalation
   decisions. Dispatch mandatory reviews for any escalation.
4. If at least one provisional job remains eligible, dispatch the fixed
   immediate sample `get-a-threshold-notification`. If it was escalated, the
   shadow result is inconclusive rather than substituting a convenient sample.
5. If the fixed sample has a material defect, record the shadow policy as
   failed and dispatch the two deferred reviews normally. Do not calculate a
   simulated release time.
6. If the fixed sample passes, record the simulated release time and the jobs
   the shadow policy would have released. Then dispatch the deferred reviews.
7. Promote nothing until every real per-page review is approved. Apply shared
   updates and run the existing targeted and capsule checks normally.

The simulated timestamp is analytical evidence only. It never authorizes a
canonical write, changes a job state, or bypasses the scheduler.

## Decision rule

The risk route passes this calibration only when:

- every preliminary mandatory page is correctly retained for full review;
- no provisional worker fails to escalate a page containing a listed trigger;
- the fixed immediate sample has no material defect;
- both deferred shadow reviews find no material defect that would have escaped
  under the simulated policy; and
- the fixed query audit passes factual retrieval, material boundaries, exact
  raw deep-dive navigation, and primary-concept reciprocity.

Any missed trigger or material deferred-review finding yields
`revise_risk_rule`; it does not trigger a new retry campaign automatically. A
passing result may support a separately approved live-review pilot for
Metronome only. It does not authorize reviewer sampling for Stripe, Adyen,
PayPal, Braintree, or another provider.

## Authorization boundary

Approval of this exact manifest authorizes adding a narrow Campaign 25 clause
to the Metronome provider rule, campaign initialization, complete reads of only
these six raw pages, strong Sol workers, distinct strong Sol complete-source
reviewers, the shadow dispatch ordering above, bounded retries, reviewer-
approved promotion, and fixed or expanded close audit. It does not authorize
an unreviewed canonical source, a seventh page, scheduler/schema/validator
changes, Luna or Terra routing, a live sampled-review policy, cross-PSP rollout,
remote push, or unrelated-file modification.
