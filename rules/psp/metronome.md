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

These are submission checks, not new campaign state. The existing validator remains the fail-closed authority, and an invalid result follows the existing bounded retry path.

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
`shared_update_plan` by grouping updates by exact target, applies each shared
target once, and runs the campaign-close wiki, capsule, and predetermined
three-page query-audit validations once. The coordinator does not perform a
default third full-source reread.
