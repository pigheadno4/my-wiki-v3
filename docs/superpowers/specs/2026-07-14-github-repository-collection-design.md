# GitHub Repository Collection and Versioned Ingest Design

**Date:** 2026-07-14

**Status:** Approved design

**Scope:** Recurring collection, version tracking, comparison preparation, and serial ingest for PSP GitHub repositories

## Problem

The wiki currently treats GitHub repositories as one-time manual sources: clone a repository, save a mutable stub plus selected files, and create one source summary. That workflow does not reliably support repositories that release frequently, historical major-version comparisons, or a growing registry of PSPs.

It also creates two rule conflicts:

1. The current GitHub rule permits updating accepted stubs and saved excerpts, while the project-wide raw rule requires accepted raw content to remain immutable.
2. The ingest rule requires a complete raw read, but a whole SDK repository is too large and unfocused to be a practical ingest unit.

The new subsystem must collect repositories in batches without allowing collection to become automatic wiki ingest. It must preserve immutable evidence, make repository changes auditable, and keep every LLM ingest cycle small enough to read completely.

## Goals

- Maintain one extensible registry for repositories from PayPal, Braintree, Stripe, Adyen, Metronome, and future companies.
- Batch-check repositories for new releases or commits and skip unchanged state deterministically.
- Preserve selected upstream files in immutable, version-identified raw snapshots.
- Support baseline collection, changed-version collection, and user-requested comparison of any two resolvable versions.
- Keep one stable source summary per repository while retaining its material version history.
- Generate collection and ingest monitoring without hand-editing mutable status files.
- Enforce one complete repository ingest packet at a time.
- Support cheaper models for constrained drafting while reserving semantic judgment for stronger models.
- Divide source pages, analyses, indexes, logs, raw snapshots, and tracking state by company where that improves navigation.

## Non-goals

- Mirroring every file and Git object from every registered repository.
- Collecting every historical tag automatically.
- Automatically starting LLM ingest after collection.
- Replacing GitHub as the authoritative complete repository archive.
- Hard-coding the supported company list or a specific LLM provider.
- Migrating all existing non-GitHub source pages into company folders as part of this subsystem.
- Rewriting existing raw GitHub evidence in place.

## Selected Architecture

Use a registry-driven snapshot pipeline:

```text
human registry
    -> batch repository discovery and collection
    -> immutable curated snapshots
    -> generated status and ingest packets
    -> user approval
    -> one packet at a time ingest
    -> one living source page per repository
    -> optional version analysis pages
```

The alternatives were rejected as follows:

- Extending mutable stubs would be inexpensive but would preserve the raw-immutability conflict and weak version history.
- Full repository mirrors per version would maximize completeness but create excessive storage, noisy diffs, and impractical LLM read requirements.

## Locked Decisions

| Concern | Decision |
| --- | --- |
| Registry | `tracking/github/repo-registry.toml` is the single human-maintained repository registry. |
| Mutable upstream state | Latest versions, collected versions, dates, SHAs, and progress are generated state, not registry fields. |
| Collection | Repositories may be checked and collected in a batch. |
| Ingest | Ingest remains human-kicked-off and strictly one packet at a time. |
| Raw retention | Every accepted repository snapshot is immutable. |
| Raw scope | Save the repository-owned snapshot manifest and exact selected upstream files, not generated diffs or summaries. |
| Source identity | One repository maps to one stable source summary by default. |
| Version analysis | Cross-version interpretation belongs in an analysis page, not a duplicate source page. |
| Wiki layout | Provider-owned wiki content uses company-first paths such as `wiki/sources/paypal/github/`. |
| Operational layout | Raw and tracking stores use source-type-first paths such as `raw/github/paypal/`. |
| Existing evidence | Legacy GitHub stubs and source pages remain valid until a controlled migration. |
| Model routing | Deterministic scripts own discovery and comparison facts; strong models own semantic synthesis and contradiction handling. |

## Artifact Layout

```text
tracking/github/
+-- repo-registry.toml                  # human-maintained intent
+-- status.json                         # generated machine-readable summary
+-- collection-status.md                # generated collection dashboard
+-- ingest-status.md                    # generated ingest queue/dashboard
+-- runs/
|   `-- <run-id>/
|       +-- manifest.json
|       +-- manifest.md
|       `-- events.jsonl
`-- repos/<company>/<repo>/
    +-- version-index.json
    +-- version-index.md
    +-- packets/
    |   `-- <packet-id>/
    |       +-- packet.json
    |       +-- ingest-packet.md
    |       +-- changed-files.txt
    |       +-- source-diff.patch
    |       `-- state-events.jsonl
    `-- comparisons/
        `-- <from-ref>-to-<to-ref>/
            +-- comparison.json
            +-- comparison.md
            +-- changed-files.txt
            `-- source-diff.patch

raw/github/<company>/<repo>/snapshots/
`-- <collection-date>-<version-or-ref>-<short-sha>/
    +-- snapshot.md
    `-- files/
        `-- <repository-relative paths>

wiki/
+-- <company>-index.md
+-- <company>-log.md
+-- sources/<company>/github/
|   `-- source-github-<repo>.md
`-- analyses/<company>/github/
    `-- analysis-<repo>-<version-comparison>.md
```

`raw/` contains immutable evidence. `tracking/` contains mutable generated state, derived diffs, ingest instructions, and progress. `wiki/` contains the maintained knowledge layer.

## Repository Registry Contract

The registry records stable collection intent only. A representative row is:

```toml
[[repos]]
id = "paypal/paypal-js"
company = "paypal"
url = "https://github.com/paypal/paypal-js"
enabled = true
repo_type = "web-sdk"
priority = "tier1"
collection_frequency = "weekly"
track = "releases-and-default-branch"
version_strategy = "monorepo-packages"
requested_refs = [
  "default-branch",
  "package:@paypal/react-paypal-js@10",
  "package:@paypal/react-paypal-js@9",
  "package:@paypal/react-paypal-js@8",
]
key_paths = [
  "README.md",
  "CHANGELOG.md",
  "packages/paypal-js",
  "packages/react-paypal-js",
]
exclude_paths = [
  "node_modules",
  "dist",
  "coverage",
  "*.lock",
]
```

Required fields are `id`, `company`, `url`, `enabled`, `repo_type`, `priority`, `track`, and `version_strategy`. Optional path and reference fields refine deterministic discovery. `enabled = false` preserves a known repository in the registry without selecting it for normal scheduled collection.

The registry must not contain `latest_version`, `latest_sha`, `last_collected_at`, collected-version lists, ingest progress, or run results. Those values drift and belong in generated state.

Priority tiers mean:

| Priority | Typical repositories | Default treatment |
| --- | --- | --- |
| `tier1` | Payment SDKs, checkout components, API specifications, first-party integration samples | Frequent collection and pilot eligibility |
| `tier2` | Server SDKs, drop-ins, release repositories, Postman collections, supporting tooling | Moderate collection frequency |
| `tier3` | Logos, utilities, automation, internal release tooling | Infrequent or on-demand collection |

Adding a company requires only valid new registry rows. The collector derives company and repository directories from those rows; company names are not hard-coded in script control flow.

The initial registry seeds the complete repository inventory supplied for PayPal, Braintree, Stripe, Metronome, and Adyen. Pilot rows start enabled. Non-pilot rows remain registered with an explicit priority and on-demand or disabled collection policy until their key paths and version strategy are reviewed. This preserves the inventory without making the first production run collect every repository.

## Version Identity and Discovery

A collected version is identified by this tuple:

```text
repository ID + ref kind + ref name + commit SHA
```

A raw snapshot identity additionally includes `capture_kind` and capture revision so an explicit supplement cannot be confused with a new upstream version.

`ref kind` is one of `release`, `tag`, `branch`, `commit`, or `package-version`. Collection metadata also records collection time, upstream commit time, release publication time when available, and every discovered alias pointing to the same SHA.

Version resolution follows the repository's configured strategy. The default fallback order is:

1. GitHub release when releases are present and selected.
2. Semver tag when usable tags are present.
3. Configured package version for monorepos.
4. Default-branch commit SHA.

Two tags that resolve to the same commit do not create duplicate raw snapshots. The version index records both aliases against the existing snapshot.

Normal collection permits one canonical version snapshot per commit SHA. An explicitly requested supplemental capture may preserve newly identified files from the same SHA without mutating that canonical snapshot. A supplement has its own snapshot identity and immutable `-rN` path, is labeled `capture_kind = "supplement"`, and does not represent a new upstream version.

Prior-snapshot selection is deterministic. A release compares with the greatest previously collected lower semantic version in the same release line unless the request names another baseline. A tracked branch compares with the previous collected SHA for that branch. A package version compares within the same package namespace. If no compatible prior snapshot exists, the work is classified as a baseline.

The system collects selected current state and explicitly requested historical refs. It does not materialize all tags merely because they exist. A comparison request may resolve and collect a missing historical snapshot on demand.

## Collection CLI and Modes

One CLI provides a stable entry point while focused Python modules own registry parsing, Git operations, snapshot preparation, comparison, and reporting. The implementation remains Python 3.9 compatible.

Expected commands are:

```bash
python scripts/collect_github_repos.py collect --all
python scripts/collect_github_repos.py collect --company paypal
python scripts/collect_github_repos.py collect --repo paypal/paypal-js
python scripts/collect_github_repos.py compare --repo paypal/paypal-js --from v9 --to latest
python scripts/collect_github_repos.py prepare --repo paypal/paypal-js --ref latest
python scripts/collect_github_repos.py status
python scripts/collect_github_repos.py packet-state --repo paypal/paypal-js --packet <packet-id> --from awaiting-review --to approved
```

`collect` checks upstream state and writes accepted snapshots plus run records. `compare` resolves two versions and writes a derived comparison packet. `prepare` regenerates one ingest packet from an existing snapshot without ingesting it. `status` regenerates dashboards from machine-readable records. `packet-state` validates one explicit lifecycle transition and appends it to the packet's event history.

## Collection Data Flow

For every selected repository, the collector:

1. Validates the registry row.
2. Clones or fetches into a temporary directory outside `raw/`.
3. Detects the default branch, releases, tags, package versions, submodules, and Git LFS usage.
4. Resolves the requested ref to an exact commit SHA.
5. Looks up that SHA in the generated version index.
6. Marks an existing SHA as unchanged and creates no raw copy.
7. For a new SHA, classifies the work as a baseline or a change from the selected prior snapshot.
8. Selects candidate key files using registry paths plus deterministic defaults.
9. Applies path, type, and size safety limits.
10. Writes the snapshot into staging.
11. Validates snapshot identity, file hashes, manifest coverage, and write boundaries.
12. Atomically promotes the validated snapshot to `raw/`.
13. Generates the baseline or delta ingest packet under `tracking/`.
14. Appends the run event and regenerates status views.
15. Removes the temporary clone.

The collector stops after manifest creation and a terminal summary. In an interactive run, that summary is the user notification. External email, chat, or scheduled-task notifications require a separately approved automation and are not implicit in this design.

## Snapshot Contract

`snapshot.md` is the source-page anchor and the complete navigation guide for the saved evidence. It contains:

- Repository URL and registry ID
- Company and repository type
- Exact ref kind and ref name
- Full commit SHA
- Capture kind and revision
- Collection date and upstream dates
- Prior snapshot identity when applicable
- Version aliases that resolve to the SHA
- A table of every saved file, its repository-relative path, hash, size, and purpose
- Detection notes for submodules, Git LFS, generated content, and omitted oversized files

Files beneath `files/` are copied byte-for-byte from the checked-out commit. The collector never edits an accepted snapshot. If later investigation finds an important omitted file, it creates a new supplemental snapshot or recollects the same ref under a distinct immutable revision; it does not enrich the accepted snapshot in place.

Generated unified diffs, summaries, and changed-file classifications never go under `raw/`. They remain reproducible tracking artifacts.

## Key-File Selection

Key-file selection combines deterministic defaults with registry overrides:

- Always consider README files, changelogs, release notes, package manifests, API specifications, public SDK entry points, migration guides, and first-party examples.
- Prefer paths listed in `key_paths`.
- Exclude dependencies, generated build output, coverage, caches, vendored trees, lockfiles unless dependency movement is itself relevant, and binary assets without wiki value.
- Preserve deleted-file information in change packets even though deleted files cannot appear in the new raw snapshot.
- Enforce configurable per-file and total-snapshot size limits.
- Record every excluded candidate and reason in generated packet metadata.

For a new repository, the packet emphasizes baseline understanding. For a changed repository, it emphasizes material deltas while retaining enough current files to understand the new state.

## Ingest Packet Types

### Baseline packet

Created for a repository with no prior accepted snapshot. It contains repository identity, the complete saved-file inventory, suggested reading order, repository structure summary, detected products/packages, and candidate wiki concepts. It points only to files inside one immutable snapshot.

### Delta packet

Created when a new SHA differs from the selected prior snapshot. It contains changed, added, renamed, and deleted files; release-note and changelog deltas; filtered source diffs; likely breaking changes; and the exact current files required to verify those changes.

### Version-comparison packet

Created by an explicit comparison command. It resolves both endpoints, collects either missing snapshot if approved by the command scope, and generates a comparison packet without modifying wiki content. Comparison may run from old to new or new to old; direction is always recorded.

All packet Markdown is derived navigation, not authoritative evidence. Claims entering the wiki must be verified against the packet's referenced raw files.

## Collection and Ingest State Machines

Collection uses terminally reconcilable states:

```text
selected -> resolving -> cloning -> inspecting
                                  |-> unchanged
                                  |-> collected-baseline
                                  |-> collected-change
                                  |-> retry-pending
                                  `-> failed
```

Every selected repository/ref must end the run in exactly one terminal state. Failed collection creates no raw snapshot.

Ingest packets use a separate lifecycle:

```text
awaiting-review -> approved -> ingesting -> ingested
                     |             |-> validation-failed
                     `-> rejected
```

Collection never moves a packet from `awaiting-review` to `approved`. User approval or an explicitly approved coordinator action owns that transition.

## Serial Ingest Contract

The unit of GitHub ingest is exactly one baseline, delta, or version-comparison packet.

Before changing any wiki page, the ingest agent must read in full:

1. `ingest-packet.md` for the selected packet.
2. The referenced immutable `snapshot.md` file or files.
3. Every raw key file named in the packet's required reading set.

The agent does not claim to have read the complete upstream repository. It claims to have read the complete curated packet and every raw file on its required list.

One cycle then completes, in order:

1. Extract 3-5 exact grounding quotes with raw paths and line locations.
2. Perform the mandatory concept audit.
3. Create or update the stable repository source page.
4. Update company and concept pages when evidence requires it.
5. Create or update a version analysis only for a material comparison.
6. Check contradictions against existing wiki claims.
7. Update the company index and company log.
8. Update root navigation only for cross-company or generic content.
9. Run focused deterministic validation.
10. Write the ingest receipt and move the packet to its terminal state.

No second packet starts until the current cycle is ingested or explicitly closed as rejected or failed.

## Stable Source Page Contract

One repository maps to one living source page by default:

```text
wiki/sources/paypal/github/source-github-paypal-js.md
```

Its frontmatter follows the source schema and lists every ingested snapshot anchor newest first:

```yaml
raw_files:
  - "github/paypal/paypal-js/snapshots/2026-07-14-v10.2.0-a1b2c3d/snapshot.md"
  - "github/paypal/paypal-js/snapshots/2026-07-14-v9.5.1-d4e5f6a/snapshot.md"
```

The body describes the current supported repository state and includes a concise `## Version history` table for material changes. It does not embed complete diffs or duplicate a full summary for every snapshot. `## Raw Sources` uses path-qualified wikilinks because many repository snapshots share the basename `snapshot.md`.

Recollection does not increase company `source_count`; the repository still owns one source summary. A separate version-specific source page is allowed only when a major line is maintained as an effectively separate product with distinct integration semantics. That is an explicit exception, not the default.

The existing `source-github-paypal-js.md` and `source-github-paypal-js-v6.md` should eventually consolidate under this rule, with compatibility links preserved for existing wikilinks.

## Version Analysis Contract

A material comparison creates or updates a company-scoped analysis page such as:

```text
wiki/analyses/paypal/github/analysis-paypal-js-v8-v9-v10.md
```

The analysis covers behavior changes, public API changes, migration requirements, removed capabilities, compatibility, and operational implications. It cites the stable source page and the relevant immutable snapshots. Mechanical changed-file lists remain in tracking.

A version analysis is not created for formatting-only changes, generated-file churn, lockfile-only updates, or minor changes with no integration consequence.

## Index and Log Division

`wiki/index.md` remains the root router for companies, generic concepts, cross-company comparisons, and major analyses. It does not list every GitHub source.

`wiki/<company>-index.md` owns that company's company page, provider-specific concepts, documentation sources, GitHub source pages, and links to company-specific analyses. Its GitHub section may be generated from source metadata while curated descriptions remain preserved.

`wiki/log.md` becomes the root and cross-company log router. Provider operations append to:

```text
wiki/paypal-log.md
wiki/braintree-log.md
wiki/stripe-log.md
wiki/adyen-log.md
wiki/metronome-log.md
```

The existing large root log is divided once with a deterministic migration that preserves entry text and order. Ambiguous or cross-company entries remain in the root log. Detailed GitHub collection attempts and per-file diffs remain in tracking rather than the query-facing wiki logs.

## Monitoring Contracts

`collection-status.md` reports company, repository, priority, configured tracking strategy, latest upstream identity, latest collected identity, last collection time, collection state, and failures.

`ingest-status.md` reports packet ID, repository, packet type, from/to versions, collection run, approval state, ingest state, source-page target, and validation result.

`version-index.json` is authoritative generated state for collected identities. `version-index.md` is its human-readable projection. Status Markdown is never hand-edited; scripts regenerate it from JSON and JSONL records.

## Model Routing and Quality Gates

Deterministic scripts own:

- Ref resolution and commit identity
- File hashes and byte equality
- Version aliases
- Changed, added, deleted, and renamed file lists
- Snapshot and packet schema validation
- Status transitions and dashboard generation
- Raw-path and write-boundary checks

A lower-cost model may draft a baseline or delta source summary after reading the complete packet. It may not resolve contradictions, merge concepts, decide migration significance, or update shared wiki state without strong-model review.

A strong model owns:

- Final key-file relevance review for ambiguous repositories
- Concept audit and taxonomy decisions
- Behavioral and API-change interpretation
- Contradiction detection
- Version-comparison analysis
- Final source-page approval and shared wiki updates

Every accepted ingest requires:

- 3-5 exact grounding quotes verified against raw paths
- Zero unsupported canonical claims
- Complete required-file reads recorded in the receipt
- Correct source identity and newest-first raw anchors
- No raw mutations
- Focused `validate_wiki.py` success
- GitHub snapshot and packet validator success
- Company index, company log, and generated ingest status agreement

## Safety and Failure Handling

- GitHub API rate limits are cached and reported; Git operations remain a fallback when API metadata is unavailable.
- Retryable network and Git failures produce `retry-pending` or `failed` run events, never partial raw snapshots.
- Submodules and Git LFS are detected and reported. They are not recursively downloaded unless the registry explicitly enables them.
- Binary, generated, vendored, oversized, and high-churn files are excluded by policy and recorded.
- Sample credentials and tokens are scanned before snapshots are committed. Findings are reported for review because verbatim vendor samples can trigger GitHub push protection.
- Temporary clones are removed after terminal recording. Their location is never treated as durable evidence.
- Same-day recollection of a different SHA uses a distinct version/ref and SHA directory; accepted paths are never overwritten.
- A malformed or missing requested ref fails explicitly and does not silently fall back to `latest`.
- An unqualified monorepo major such as `v9` fails as ambiguous when multiple packages could match. The registry or command must name the package namespace or exact tag.

## Legacy Migration

The repository currently has 23 flat GitHub stubs, 23 detail directories, and 23 corresponding source summaries. Migration is incremental:

1. Treat each existing stub plus detail directory as an immutable legacy baseline.
2. Add registry rows for selected repositories without moving old evidence immediately.
3. On the first new collection, create the new nested snapshot and link both legacy and new anchors from the stable source page.
4. Move GitHub source pages into company-first folders with a deterministic path migration; filenames stay stable so Obsidian basename links continue to resolve.
5. Consolidate duplicate version-specific source pages only after backlinks and source content are audited.
6. Update validators and orphan detection to understand nested GitHub snapshots before enabling production collection.

No migration rewrites accepted legacy raw content.

## Pilot Repositories

The first pilot set is:

| Repository | Versions | What it tests |
| --- | --- | --- |
| `paypal/paypal-js` | package-qualified current v10 line, latest v9, latest v8 | Monorepo packages, historical major comparison, duplicate source-page consolidation |
| `paypal-examples/v6-web-sdk-sample-integration` | current plus one prior material ref when available | New-repository baseline and sample-app key-file selection |
| `braintree/braintree_ios` | current plus previous major | Native mobile SDK and Venmo-related integration evidence |
| `stripe/stripe-ios` | current plus previous major | Large SDK, release history, generated-file filtering |
| `Adyen/adyen-web` | current plus previous major | A non-PayPal web SDK and cross-provider generality |

The pilot runs serially by repository even though collection tooling supports batch operation. `paypal/paypal-js` runs first because it exercises the most difficult version strategy.

Pilot success requires:

- Registry validation and version resolution for every pilot row
- Correct unchanged detection by SHA
- Immutable baseline and changed snapshots
- Useful baseline, delta, and explicit comparison packets
- No generated diff under `raw/`
- One stable source page updated from one complete packet
- One material version analysis grounded in two or more snapshots
- Accurate collection and ingest dashboards
- Snapshot size and required-reading set small enough for complete LLM review
- All deterministic validators passing

## Testing Strategy

Unit tests cover registry parsing, version resolution fallbacks, SHA alias deduplication, path selection, exclusion rules, snapshot naming, state transitions, and status rendering.

Fixture-based tests use small local Git repositories to cover baseline collection, unchanged recollection, changed files, deleted files, renamed files, same-SHA tags, malformed refs, monorepo package versions, submodule detection, and size-limit rejection without requiring network access.

Integration smoke tests use one small public pilot repository only after fixture tests pass. Network-dependent tests are opt-in and record the exact upstream SHA so results remain explainable.

Validator tests cover nested `raw_files:` paths, path-qualified `snapshot.md` wikilinks, orphan snapshot detection, source-page identity, newest-first snapshot ordering, and agreement between packet state and dashboards.

## Implementation Sequence

1. Update the root directory map and keep `rules/github-repos.md` as the standalone GitHub workflow.
2. Rewrite the GitHub rule around registry, snapshot, packet, and serial-ingest contracts; clarify the repository ingest unit in `rules/ingest.md` and nested orphan checks in `rules/lint.md`.
3. Add registry parsing and validation, seed the complete supplied repository inventory, and enable only pilot rows initially.
4. Add fixture repositories and tests for snapshot and version logic.
5. Implement collection, comparison, packet, and reporting modules behind `collect_github_repos.py`.
6. Add nested GitHub snapshot and source-page validation.
7. Add company-first GitHub source and analysis directories plus provider log routing.
8. Run the `paypal/paypal-js` pilot and review its artifacts before running the other pilot repositories.
9. Run the remaining pilots serially and decide which registered non-pilot rows to enable next.
10. Plan the deterministic legacy source/log migration only after the new workflow passes pilot validation.

## Acceptance Criteria

The subsystem is ready for routine use when:

- A new company or repository can be added through one registry row without script edits.
- A batch run can classify every selected repository/ref into a terminal state.
- Unchanged repositories create no new raw snapshot or ingest work.
- Changed and requested historical refs create immutable, uniquely identified snapshots.
- Generated comparison artifacts remain outside `raw/`.
- The collector stops before ingest and produces a reviewable manifest.
- One approved packet can be read completely and ingested without opening another packet.
- One stable source page can represent current repository state and material history.
- Provider indexes and logs receive provider-specific entries while the root remains a router.
- Lower-cost drafts cannot bypass strong-model judgment gates or deterministic validation.
- Existing legacy raw evidence remains intact and queryable throughout migration.
