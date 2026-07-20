# PayPal JS Focused GitHub Collection Pilot

**Status:** Specification approved; implementation pending
**Date:** 2026-07-20
**Narrows:** `2026-07-14-github-repository-collection-design.md` and `2026-07-15-github-release-retention-design.md`
**Supersedes for implementation:** `2026-07-18-github-source-capsule-design.md`

## Purpose

Prove the original GitHub workflow with one difficult repository before scaling it:

1. collect useful repository evidence into immutable raw snapshots;
2. preserve package release history as the repository evolves;
3. compare each package release with the correct predecessor;
4. ingest new evidence serially into durable wiki knowledge; and
5. answer current, historical, and version-comparison queries from exact evidence.

The pilot repository is `paypal/paypal-js`. It contains two independently versioned packages:

- `@paypal/paypal-js`;
- `@paypal/react-paypal-js`.

`paypal/paypal-checkout-components` is a separate repository. It is not a subdirectory or part of this pilot. The PayPal JS source page may link to it when runtime behavior crosses repository boundaries, but its evidence and release history remain independent.

## Goals

- Track package-qualified releases rather than ambiguous repository-level major versions.
- Save one bounded but source-capable snapshot per exact Git SHA.
- Include TypeScript implementation evidence, not only README and changelog files.
- Reuse one snapshot when multiple package releases share a SHA.
- Exercise both full and delta ingest with chronological release history.
- Keep one cumulative repository source page and one separate repository changelog.
- Keep collection batch-capable while ingest remains user-gated, serial, and full-read for its assigned evidence.
- Provide a small, visible retry and status model.
- Update query routing so version and change questions search the changelog and exact raw evidence.

## Non-Goals

- Mirroring the complete repository for every release.
- Ingesting arbitrary default-branch commits automatically.
- Automatically starting or approving ingest.
- Collecting or ingesting `paypal/paypal-checkout-components` in this pilot.
- Building a general transaction journal, event chain, packet lifecycle, quarantine service, or crash-injection framework.
- Rewriting accepted legacy raw evidence.
- Proving npm package tarballs are byte-equivalent to repository source.
- Generalizing ecosystem-specific source discovery beyond what this pilot needs.

## Evidence Identities

The implementation must keep these identities separate:

### Package release

A package release is identified by its exact package-qualified tag, for example:

```text
@paypal/paypal-js@10.0.3
@paypal/react-paypal-js@10.1.2
```

It records package name, version, release date, exact tag, exact Git SHA, release notes, and previous release for the same package.

### Repository snapshot

A repository snapshot is identified by the full Git SHA. It contains the selected repository files at that exact commit. Two package releases at the same SHA share one snapshot.

Package release notes are separate immutable raw records linked to the snapshot. This permits a later-discovered release at an already collected SHA without mutating the snapshot.

### Change set

A change set is one ingest work item anchored to a repository SHA and an exact set of package release IDs. It contains one or more package release comparisons. When package releases are discovered together at the same SHA, they are grouped into one change set with separate package subsections.

The change set's overall recommended ingest mode is `full` when any included package comparison requires full ingest; otherwise it is `delta`.

## Pilot Version Scope And Order

For each of the two packages, discover exact release tags and process evidence in this order:

1. latest available v8 release as the historical baseline;
2. latest available v9 release;
3. v10.0.0;
4. subsequent v10.0.x releases in semantic-version order;
5. v10.1.0;
6. subsequent v10.1.x releases in semantic-version order; and
7. any later v10 minor lines in semantic-version order if they exist when the pilot runs.

The intended ingest behavior is:

| Transition | Initial recommendation |
| --- | --- |
| no prior package evidence to v8 baseline | `full` |
| v8 baseline to v9 baseline | `full` |
| v9 baseline to v10.0.0 | `full` |
| v10 patch release | `delta`, subject to escalation |
| v10 minor release | classify from evidence |

If a requested major or minor line does not exist for a package, record it as `not_available`; do not invent a repository-level substitute.

Release events are discovered package-by-package but collected by SHA. Their ingest work items are ordered chronologically, with deterministic tag ordering as a tie-breaker.

## Release-Driven Collection

Periodic collection is driven by package-qualified releases and tags:

1. fetch release and tag metadata;
2. resolve each selected tag to an exact commit SHA;
3. compare discovered releases with recorded release mappings;
4. record `unchanged` when no selected release is new;
5. save an immutable package release record and reuse an existing snapshot when a new package release points to a collected SHA;
6. collect a new source capsule when the SHA is new;
7. compare each package release with its previous selected release for the same package;
8. create or update the SHA change set;
9. recommend an ingest mode with explicit reasons; and
10. stop at `awaiting_approval`.

Discovery for one run completes before its change sets are created, so all then-known releases at the same SHA group into one item. An already approved or ingested change set is never mutated. If another package release is discovered later at that SHA, create a new release-only change set that reuses the existing snapshot.

Release records are content-hashed. Recollection of an unchanged package version, SHA, and release-note hash is `unchanged`. If upstream release notes change without a new tag or SHA, preserve a new dated release-record revision and create a delta-review item describing the metadata change; do not rewrite the prior record.

The periodic workflow does not collect or ingest arbitrary `main` commits. A user may request an exact branch or SHA for investigation; the result must be labeled `unreleased` and cannot silently become package release history.

## Source Capsule Boundary

Every selected new SHA stores a bounded source capsule containing:

- exact repository, tag, SHA, author date, commit date, and collection date metadata;
- root `README.md`, `package.json`, lockfile, license, and relevant changeset metadata;
- each tracked package's `README.md`, `package.json`, changelog when present, and release metadata;
- public package entry points and exported TypeScript types;
- local `.ts` and `.tsx` files transitively imported by those public entry points;
- changed package source, documentation, examples, and tests relevant to the release, even when outside the normal public-entrypoint closure; and
- a manifest of every collected and excluded file with its selection or exclusion reason.

Generated output, dependency directories, coverage, caches, minified bundles, large fixtures, and unrelated workspaces are excluded by default. Numeric file and byte budgets remain repository policy, not hardcoded PayPal branches. A budget overflow stops collection for review rather than silently truncating evidence.

If a future query requires an excluded file, collect a small immutable exact-SHA supplement linked to the original snapshot. The pilot does not require a generalized supplement packet lifecycle.

## Raw And Tracking Layout

Stable repository intent remains in:

```text
tracking/github/repo-registry.toml
```

Changing operational state is not stored in the registry. The focused pilot uses:

```text
tracking/github/work-items.json
tracking/github/status.md
```

`work-items.json` is the machine-readable authority for discovery, collection, approval, ingest recommendation, attempts, and final state. `status.md` is a generated human-readable view and must not be edited as an independent authority.

Raw evidence uses source-type-first organization:

```text
raw/github/paypal/paypal-js/
├── snapshots/
│   └── 2026-07-07-3caece5/
│       ├── manifest.json
│       └── files/
│           ├── README.md
│           ├── package.json
│           └── packages/
│               ├── paypal-js/
│               └── react-paypal-js/
└── releases/
    ├── paypal-js/10.0.3/2026-07-07/
    │   ├── manifest.json
    │   └── release-notes.md
    └── react-paypal-js/10.1.2/2026-07-07/
        ├── manifest.json
        └── release-notes.md
```

The date belongs to the immutable snapshot or release-record directory, while collected source files preserve original repository-relative paths. This preserves imports, path-qualified citations, and meaningful diffs.

The snapshot manifest records the full SHA, collection date, triggering refs observed at collection, file hashes, sizes, and selection decisions. It does not claim to be an exhaustive mutable list of every release later mapped to that SHA. Each package release manifest is the immutable authority for package name, version, tag, release date, collected date, release-note hash, and linked snapshot SHA. Generated tracking state indexes these immutable records.

Raw manifests are provenance sidecars, not upstream narrative content or wiki summaries. Detailed claims still cite the captured upstream files or release notes.

Mechanical comparison artifacts may live under the repository's tracking area. They must link to immutable raw snapshots and must not be presented as upstream raw content.

## Work Item State

The minimum successful state flow is:

```text
discovered -> collected -> awaiting_approval -> ingesting -> ingested
```

Additional terminal or review states are:

```text
unchanged
not_available
collection_failed
needs_manual_review
```

Each collected work item records:

- repository and exact SHA;
- package-qualified releases at that SHA;
- per-package predecessor and comparison paths;
- per-package recommended ingest mode and reasons;
- overall recommended ingest mode;
- collection date and manifest path;
- attempts and last error when applicable; and
- approval and ingest status.

The collector recommends. Only the user approves or changes the ingest mode and starts ingest.

## Full And Delta Ingest

All ingest remains serial: one approved SHA change set at a time. Batch collection never implies batch ingest.

### Full ingest

Use full ingest for:

- a repository's first evidence;
- a package's first selected version;
- a major-version transition;
- architecture, package export, primary integration model, security, or material payment-behavior changes; or
- any release whose impact cannot be isolated confidently.

The ingest agent must read the complete existing source page, the complete selected source capsule assigned to the change set, release notes, package comparisons, and relevant prior-version context. It then adds the new package or major-version knowledge while preserving validated historical knowledge.

Full ingest does not replace the source page with latest-only content. It may reorganize headings only when needed to add the new version coherently, and it must preserve older version findings and their evidence links.

### Delta ingest

Use delta ingest for contained patch or minor updates. The ingest agent must read in full:

- the current cumulative source page;
- release notes;
- the generated comparison;
- every changed source, documentation, example, and test file assigned to the change set; and
- the affected package and major-version section.

It updates only affected knowledge and appends the changelog entry. It need not reread unchanged historical raw files.

A patch or minor release escalates to full ingest when it changes public exports, architecture, security handling, SDK initialization, payment behavior, or has broad or ambiguous impact. Semver alone never overrides evidence.

## Cumulative Source And Changelog Pages

Wiki knowledge uses provider-first organization:

```text
wiki/sources/paypal/github/source-github-paypal-js.md
wiki/sources/paypal/github/changelog-github-paypal-js.md
```

The source page is cumulative repository knowledge. It contains:

- current package versions;
- repository purpose, architecture, and responsibility boundary;
- separate package sections;
- separate v8, v9, and v10 major-version subsections where evidence exists;
- current and historical public APIs and integration behavior;
- cross-version compatibility and migration findings;
- evidence gaps and links to independently tracked related repositories; and
- path-qualified raw snapshot links.

Validated historical findings are never removed merely because a new version exists. Removal is allowed only for a proven factual error, exact duplicate, or wrong package/version attribution, and the correction must be recorded in the changelog.

The changelog is chronological release synthesis. It has separate package timelines and groups releases that share a SHA into one repository change set. Each package entry records from/to versions, release date, SHA, ingest mode, important changes, developer or merchant impact, migration action, source-page sections updated, and links to release notes, comparisons, manifests, and exact raw files.

The changelog is a navigation and synthesis layer, not the sole authority for detailed implementation claims.

## Query Routing

`rules/query-and-synthesis.md` owns general routing. `rules/github-repos.md` owns GitHub-specific version resolution. `CLAUDE.md` links to those rules without duplicating them.

The rules must require this evidence order:

| Query | Required routing |
| --- | --- |
| current integration or API behavior | cumulative source page, then latest exact snapshot when implementation detail is needed |
| latest change or new feature | source page, changelog, then linked release notes/comparison/raw snapshot |
| version-specific behavior | changelog, exact package-qualified release, then linked SHA snapshot |
| upgrade or version comparison | both changelog entries, package comparison, then both exact snapshots |
| deep source question | exact SHA source capsule; never changelog summary alone |
| historical behavior | historical source-page version section, changelog entry, and exact snapshot |

Agents must identify the package before interpreting a version such as "PayPal JS v10." Related repositories are searched only when the question crosses the documented responsibility boundary, and the answer must identify the different evidence authority. Unreleased branch or SHA evidence must be labeled as unreleased.

## Failure Protection

Snapshots are assembled in a temporary sibling directory and published only after collection, hashing, and manifest validation succeed. A failed attempt must not publish a partial snapshot, create an ingest item, alter the last successful snapshot, or change accepted wiki knowledge.

Transient Git and network errors receive at most three attempts in one run. After three failed attempts, record `collection_failed` with category, message, attempt count, and date. Retry during the next periodic run. After three consecutively failed runs, change the item to `needs_manual_review` and pause automatic retries.

Invalid tags, access denial, invalid registry policy, secret findings, unsafe paths, and budget overflow go directly to `needs_manual_review`. An explicit retry command may resume the item after correction.

This pilot requires safe temporary publication and bounded retries, not the superseded design's generalized journal, event chain, retry epochs, quarantine store, or crash matrix.

## Minimal Operations

The implementation must support these user intents; exact CLI spelling may follow existing script conventions:

- collect the focused repository or one exact package release;
- show discovery, collection, failure, approval, and ingest status;
- compare two package-qualified releases;
- approve or override one work item's ingest mode;
- show the next serial ingest item; and
- explicitly retry a failed item.

No operation may combine approval with ingest automatically.

## Pilot Acceptance Criteria

The pilot is complete when all of the following are demonstrated locally:

1. Both package release histories are discovered with package-qualified identities.
2. Latest v8 and v9 baselines and every selected v10 release are processed chronologically.
3. Same-SHA package releases reuse one immutable snapshot and one grouped work item.
4. Snapshots contain the approved TypeScript source capsule and a complete manifest.
5. Per-package comparisons use the previous selected release of the same package.
6. Full and delta recommendations include deterministic reasons and escalation signals.
7. No ingest begins without user approval, and approved items ingest one at a time.
8. Full ingest preserves historical version knowledge while adding the new version.
9. Delta ingest changes only affected knowledge and appends the changelog.
10. Failure handling preserves the last good state and visibly reports blocked work.
11. Query rules route current, historical, change, comparison, and deep-source questions to the correct evidence.
12. The cumulative source page and changelog can answer the approved pilot queries with exact raw links.

## Deferred Until After The Pilot

The following work requires a demonstrated need and a separate approved design:

- generalized packet state machines;
- write-ahead journals and immutable event chains;
- multi-artifact crash recovery and crash-injection matrices;
- generalized quarantine and retry-epoch semantics;
- automated cross-repository dependency collection;
- broad registry migration and collection of every listed repository; and
- ecosystem adapters beyond this focused npm monorepo pilot.

Reusable exact-Git reading, workspace discovery, source selection, secret scanning, and budget primitives may remain. Deferred infrastructure must not block or redefine this pilot.
