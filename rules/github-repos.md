# Rule: GitHub repository collection and versioned ingest

> This rule governs GitHub repositories such as SDKs, sample apps, integration tools, and API specifications. You arrived here from the CLAUDE.md Workflow Index. It is the standalone workflow for registry-driven collection, packet preparation, and serial wiki ingest.

## Collection modes

GitHub collection may batch-check selected repositories and refs. It resolves each requested ref to an exact commit SHA, records an unchanged result without creating a raw copy, and creates a snapshot only for a new capture identity.

Use `tracking/github/repo-registry.toml` to select normal collection. An explicit comparison can resolve two requested refs and prepare a comparison packet. Collection, comparison, and packet preparation stop before wiki ingest; they never automatically write wiki content.

## Registry contract

`tracking/github/repo-registry.toml` is the single human-maintained repository registry. Each row records stable collection intent: `id`, `company`, `url`, `enabled`, `repo_type`, `priority`, `track`, and `version_strategy`. Optional requested refs, key paths, and exclusions refine deterministic discovery.

The registry must not contain latest versions, SHAs, collected-version lists, collection dates, ingest progress, or run results. Those mutable values are generated state under `tracking/github/`. Adding a company requires valid registry rows only; collectors derive company and repository directories from those rows rather than hard-coding company names.

## Immutable snapshot contract

Every accepted GitHub capture is an immutable snapshot under:

```text
raw/github/<company>/<repo>/snapshots/<collection-date>-<version-or-ref>-<short-sha>/
```

Each immutable snapshot contains `snapshot.md`, the repository-owned manifest, and `files/`, which preserves the selected upstream files at their repository-relative paths. The manifest records repository identity, exact ref and full SHA, `capture_kind`, capture revision, relevant dates and aliases, every saved file with hash, size, and purpose, and omitted-file or repository-detection notes.

Accepted files under `raw/` are immutable. Normal recollection never edits a legacy stub or accepted snapshot. Exact upstream files and the snapshot manifest belong in `raw/`; generated diffs, summaries, status, and packets belong in `tracking/`.

If later review requires an omitted file for the same upstream SHA, create a new immutable `-rN` capture with `capture_kind = "supplement"`. Do not enrich or overwrite the canonical snapshot.

## Baseline, delta, and comparison packets

Generated packets live under `tracking/github/repos/<company>/<repo>/`. A baseline packet covers a first accepted snapshot. A delta packet covers a new snapshot against the deterministic prior compatible snapshot. A comparison packet is created only by an explicit comparison request and records both endpoints and direction.

Packets may include generated changed-file lists, filtered diffs, summaries, suggested reading order, and candidate concepts. They are navigation and status artifacts, not raw evidence. Every packet identifies its required reading set of immutable raw files.

## Collection-to-ingest boundary

Collection may batch, but ingest is human-kicked-off. Collection validates and promotes immutable snapshots, generates packets and tracking state, then leaves packets awaiting review. Only user approval or an explicitly approved coordinator action can move a packet to approved; collection never performs that transition.

The tooling must remain compatible with Python 3.9.6 and add no mandatory third-party dependency. Network-dependent collection and smoke checks remain outside the default unit-test suite.

## Serial repository ingest

Ingest exactly one approved baseline, delta, or comparison packet at a time. A complete cycle processes one packet as the GitHub ingest unit. Before changing wiki content, read the complete `ingest-packet.md`, every referenced `snapshot.md`, and every file in the packet's required reading set in full. Do not claim to have read the whole upstream repository.

Complete the packet's concept audit, stable source page update, evidence-driven company and concept updates, material version analysis when applicable, contradiction check, company index and log update, focused validation, receipt, and terminal packet state before starting another packet. Follow `rules/ingest.md` for the shared one-source discipline.

## Stable source page and version history

One repository maps to one stable source page unless a separately approved exception applies. Use company-first paths such as:

```text
wiki/sources/paypal/github/source-github-paypal-js.md
```

The source page lists its ingested snapshot manifests newest first in `raw_files:` and maintains concise material version history. It links to path-qualified raw snapshots and does not duplicate generated diffs. Recollection updates the stable source page without increasing the company's source count. A material cross-version interpretation belongs in `wiki/analyses/<company>/github/`, not in a duplicate version source page.

## Add a company or repository

Add a valid row to `tracking/github/repo-registry.toml` with the required stable fields and reviewed optional refs, key paths, and exclusions. Choose the company slug that routes raw snapshots to `raw/github/<company>/` and wiki content to company-first paths. Do not add company-specific script branches or mutable collection results to the registry.

Enable a row only when its collection policy is ready for normal selection. Registered but disabled or on-demand rows remain inventory without becoming scheduled collection work.

## Legacy stub compatibility

Existing flat GitHub stubs and detail directories remain immutable legacy baselines and queryable evidence. On a repository's first new collection, create a new nested snapshot and link both the legacy and new evidence from the stable source page as appropriate.

Normal recollection never edits a legacy stub or detail directory. A separate migration may relocate source pages or consolidate duplicate version pages only after backlink and content review; it never rewrites accepted legacy raw content.

## Validation and monitoring

Run `python3 scripts/validate_github_collection.py` to validate `raw/github/` snapshots, `tracking/github/` packets and generated state, source identity, newest-first snapshot anchors, and raw/tracking boundaries. The validator is deterministic and does not require network access.

`tracking/github/` owns generated version indexes, run records, packet lifecycle events, collection status, and ingest status. Generated status Markdown is regenerated from machine-readable JSON and JSONL records and is never hand-edited.
