# Metronome Campaign 20 Selection Review

- Status: **awaiting exact-manifest approval**
- Purpose: measure whether the three Campaign 19 worker-preflight corrections improve first-pass quality without changing campaign size, scheduler state, reviewer policy, or close gates.
- Scheduler mode: `dry_run`; no campaign state, worker order, complete raw read, model task, or canonical wiki write is authorized until this exact manifest is approved.
- Selection method: metadata only — capsule pending status, raw path, source URL header, first heading, line count, SHA-256, historical-manifest membership, and source-target absence. Raw bodies were not read completely and support no factual claims.
- Historical isolation: all five pages are pending capsule orphans, have no canonical source target, and have never appeared in an earlier Metronome campaign manifest. No Campaign 12–15 candidate, suggestion, or disposition is reused.
- Runtime: one Sol coordinator plus at most three dynamic native-agent slots. All workers use Sol; `standard` and `strong` remain routing hints, and every first attempt receives an independent full-source Sol review by a different agent.

## Exact five-page selection

| # | Job | Lines | Worker tier | Metadata-visible purpose |
| ---: | --- | ---: | --- | --- |
| 1 | `get-a-customer` | 242 | standard | Short read baseline for request, response, and identity handling |
| 2 | `list-all-billable-metrics` | 319 | standard | Moderate listing page for pagination, schema, and existing concept coverage |
| 3 | `list-balances` | 1,464 | strong | Longest and schema-heaviest page; credits, balances, ledgers, and pagination may intersect |
| 4 | `create-a-credit` | 433 | strong | Mutation selected to exercise OpenAPI precision, global POST rules, lifecycle, and concept placement |
| 5 | `set-up-account-level-billing-provider` | 203 | strong | Integration mutation selected to exercise global POST rules, configuration boundaries, and multiple concepts |

This is a representative five-page measurement, not corpus-scale production. The selection deliberately includes two read-oriented baselines and three higher-judgment pages while keeping the same campaign size as Campaign 19.

## Worker pre-submit gate

The generated worker order supplies the existing six-item preflight. After one complete raw-page read and before handoff, each worker must:

1. Copy the trusted canonical URL, return only the fixed result keys, and provide three to five non-empty byte-exact grounding quotes.
2. For OpenAPI pages, distinguish operation-level `requestBody` requiredness, required properties inside the payload schema, and unspecified `additionalProperties` behavior.
3. For every POST operation, check the existing Metronome API-wide idempotency authority and separate its guarantees from endpoint-specific retry, concurrency, freshness, and recovery unknowns.
4. For each durable fact, audit every relevant existing Metronome concept and return the necessary reciprocal source-link suggestions.
5. Preserve response limits, lifecycle and propagation effects, failure behavior, rate limits or historical windows, contradictions, and explicitly undocumented behavior.
6. Rehearse factual retrieval, boundary or contradiction handling, and exact raw deep-dive navigation against the candidate.

These are worker reminders, not new deterministic validation and not a substitute for independent review.

## Review and retry gate

Every first attempt receives an independent complete-source Sol review. An unchanged-hash correction limited to links, frontmatter, wording, or an already-identified evidence omission may use targeted diff review. Factual, uncertain, lifecycle, schema, cross-source, or concept-placement corrections require another complete-source review. Maximum attempts remain three.

## Coordinator close

Only approved candidates may be promoted. The coordinator applies grouped reviewer-approved concept updates once, promotes byte-equal canonical sources, derives company/index/log/count changes mechanically, checks reciprocal links once, and runs the existing touched-page, raw-hash, duplicate-entry, capsule, and fixed-query validations once. It does not perform a default third full-source read.

## Immutable query audit

- Standard page: `get-a-customer`
- Longest/schema page: `list-balances`
- Ordinary mutation sample: `create-a-credit`

Each receives exactly three future-query tests: factual retrieval, boundary/contradiction handling, and exact raw deep dive. A material partial or fail expands the audit to all five pages. Mechanical link defects are corrected before the query audit and do not create another audit framework.

## Throughput gate

Use the same small measurement as Campaign 19:

- At least four of five pages approved on attempt 1.
- No more than one full semantic retry.
- No audit expansion caused by a mechanical link omission.
- Approximately 35 minutes or less of visible active work is desirable, not a correctness gate.

If these materially improve over Campaign 19's zero-of-five first-pass result, a separately approved future campaign may consider 8–10 pages. Failure keeps the campaign size at five and triggers analysis of the remaining semantic defects, not another framework change.

## Authorization boundary

Approval of this exact manifest authorizes initialization, complete reads of only these five raw pages, independent per-page reviews, bounded retries, the fixed or expanded audit rule, and coordinator promotion of reviewer-approved jobs after all close gates pass. It does not authorize another page, reuse of old non-promotion candidates, selective-routing reclassification, a model comparison, an 8–10 page expansion, cross-provider rollout, or remote push.
