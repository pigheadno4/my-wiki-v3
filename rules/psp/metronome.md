# Provider: Metronome — collection and ingest router

## Read only the applicable workflow

- Collection: use the unchanged profile below with `rules/psp-collection.md`.
- New retrieval-oriented ingest campaigns: after reading `CLAUDE.md` and
  `rules/ingest.md`, read [metronome-ingest.md](metronome-ingest.md), then the
  approved campaign's manifest/selection and trusted role order. That contract
  is self-contained; do not load C37–C39 contracts, proposal files, historical
  lessons, or old attempts as default instructions.
- Historical campaign investigation or explicitly authorized resumption: read
  the relevant section of [metronome-history.md](metronome-history.md) and that
  campaign's original contract. Old campaign evidence remains unchanged.

## Authorization boundary

Metronome alone permits coordinator-controlled parallel ingest after approval
of an exact manifest. The compact retrieval contract must be explicitly named
in that campaign's approved dispatch instructions; this documentation cleanup
does not start or authorize a new campaign, enlarge a manifest, remove review,
or extend parallel/routing permissions to another PSP. Ordinary ingest still
follows the serial workflow in `rules/ingest.md`.

Keep independent Sol review for every new source candidate and its semantic
suggestions. Do not resume Campaign 13/14 jobs, promote their failed-pilot
candidates, use `audit_only`, or generalize historical risk-gated waivers.
Selective raw routing still follows `rules/ingest.md`; metadata alone cannot
exclude unique durable endpoint facts. A query recommendation needs approval
before promotion, even when its raw hash is unchanged.

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
