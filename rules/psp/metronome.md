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
