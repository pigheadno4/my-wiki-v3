# GitHub Release Retention and Changelog Design

**Status:** Approved
**Date:** 2026-07-15
**Extends:** `2026-07-14-github-repository-collection-design.md`

## Objective

Preserve version-specific repository evidence without creating one wiki source page per release. The first pilot is `paypal/paypal-js`, but the policy is registry-driven and reusable for future companies and repositories.

The system must:

- retain every stable v10 release for the PayPal JS pilot;
- retain selected historical v8 and v9 baselines;
- retain every newly observed stable release in each tracked line;
- archive exact upstream changelog and release-note evidence;
- keep one stable repository source page with a concise per-release ledger; and
- preserve one-packet-at-a-time, full-read ingest.

## Decision

Use a hybrid backfill policy:

| Version line | Historical backfill | Future collection |
| --- | --- | --- |
| v10 | Every stable release | Every stable release |
| v9 | Selected minor baselines | Every stable release |
| v8 | Selected minor baselines | Every stable release |

A selected historical v8 or v9 baseline is:

1. the first stable release in the major line;
2. the latest patch release in every minor line;
3. the latest stable release in the major line;
4. any exact version already referenced by the wiki; or
5. any release identified as a breaking-change or migration boundary.

The collector deduplicates this union before resolving refs.

## Registry Contract

Version retention belongs in repository configuration, not hard-coded collector branches. A repository may define multiple version tracks:

```toml
[[repos.version_tracks]]
selector = "package:@scope/name@10"
backfill = "all-stable"
future = "all-stable"
include_prerelease = false

[[repos.version_tracks]]
selector = "package:@scope/name@9"
backfill = "minor-baselines"
future = "all-stable"
include_prerelease = false
```

The PayPal package namespace is not assumed from the repository name. Task 11 dry-run discovery must determine whether a line belongs to `@paypal/react-paypal-js`, `@paypal/paypal-js`, or another package before committing exact selectors.

Allowed backfill policies are:

- `all-stable`: every stable release in the selected line;
- `minor-baselines`: the historical baseline union defined above; and
- `none`: no historical release backfill.

Allowed future policies are `all-stable` and `none`. Prereleases are excluded unless `include_prerelease = true` or an exact prerelease selector is explicitly requested.

## Version Resolution

A package-major selector such as `package:@scope/name@10` resolves the greatest stable semantic version in major line 10. It must not select a prerelease.

Examples:

| Available | Major selector result |
| --- | --- |
| `10.0.0`, `10.1.3`, `10.1.5` | `10.1.5` |
| `10.1.5`, `10.2.0-beta.1` | `10.1.5` |
| `10.2.0-beta.1` only | fail and require an explicit prerelease selector |

An exact selector such as `package:@scope/name@10.1.3` resolves only that version. An exact prerelease selector may resolve that prerelease. Missing or ambiguous selectors fail without fallback.

The default branch is collected separately when its SHA differs from the latest selected release. Multiple tags or selectors resolving to one SHA create one canonical snapshot with aliases, not duplicate raw evidence.

## Snapshot Evidence

Each selected release creates or reuses one immutable snapshot:

```text
raw/github/<company>/<repo>/snapshots/<snapshot-id>/
├── snapshot.md
├── release-notes.md
└── files/
    ├── CHANGELOG.md
    └── <selected upstream files>
```

`release-notes.md` contains exact upstream GitHub release-note content when available. A repository-owned changelog remains byte-for-byte at its repository-relative path under `files/`. Absence of either artifact is recorded in `snapshot.md`; the collector never fabricates upstream release notes.

Generated summaries, changelog deltas, changed-file lists, and patches remain under `tracking/github/`. They are navigation and review aids, not authoritative evidence.

To make changed public entrypoints and examples reachable during snapshot construction, the snapshot builder contract adds a backward-compatible final parameter:

```python
build_snapshot(
    config,
    ref,
    repo_root,
    raw_root,
    staging_root,
    collection_date,
    prior_snapshot=None,
    capture_kind="canonical",
    changed_paths=(),
) -> SnapshotRecord
```

## Collection Flow

For each configured version track, the collector:

1. lists remote tag metadata without downloading every tag object;
2. filters by exact package namespace and major line;
3. excludes prereleases by default;
4. applies the configured historical or future selection policy;
5. compares selected refs with the generated version index;
6. fetches only missing selected ref objects;
7. creates or reuses one immutable snapshot per SHA;
8. preserves exact changelog and release-note evidence;
9. generates one packet per newly collected release; and
10. leaves every packet in `awaiting-review`.

Collection may process several releases in one run. It never approves or ingests a packet.

Periodic runs classify refs as follows:

- known tag and known SHA: unchanged;
- new alias for a known SHA: update generated aliases without a new snapshot;
- new stable release: create a snapshot and delta packet;
- prerelease not explicitly enabled: excluded with a recorded reason;
- missing or malformed evidence: failed or review-needed, with no wiki mutation; and
- deleted or rewritten upstream tag: preserve archived evidence and report the discrepancy.

## Serial Ingest

Every release packet remains an independent ingest unit. Before writing wiki content, read its packet, referenced manifests, release notes, changelog, and complete required-reading set.

Recommended PayPal JS order:

1. ingest the latest stable v10 packet to establish current repository state;
2. ingest historical v10 packets one at a time;
3. ingest selected v9 packets one at a time;
4. ingest selected v8 packets one at a time; and
5. approve and ingest explicit v8-to-v9 and v9-to-v10 comparison packets separately.

No second packet starts until the current packet reaches a valid terminal state.

## Stable Source Page

All ingested repository releases contribute to one stable page:

```text
wiki/sources/paypal/github/source-github-paypal-js.md
```

The page contains a concise ledger:

```text
Version | Release date | Commit | Snapshot | Changelog | Release notes | Change summary | Migration impact
```

Each row links to immutable evidence. `Change summary` and `Migration impact` are evidence-backed wiki interpretation, not copied release-note text. Full changelog content remains in raw evidence; mechanical deltas remain in tracking.

The page keeps current integration guidance separate from historical release rows. It does not create a source page for every patch version. Existing `paypal-js`, `paypal-js-v6`, and `react-paypal-js-v8` source identities are consolidated only after backlink and product-boundary review; compatibility pages remain where historical identity is meaningful.

## Analysis Policy

A snapshot and source-ledger row exist for every retained release. A separate analysis page is created only for material behavior, API, compatibility, or migration changes.

Patch-level formatting, lockfile, generated-file, or documentation-only changes do not create standalone analysis pages. Explicit major or material minor comparisons may update:

```text
wiki/analyses/paypal/github/analysis-paypal-js-v8-v9-v10.md
```

## Validation and Failure Handling

Validation must confirm:

- every configured track resolves to the intended package namespace;
- major selectors exclude prereleases unless enabled;
- every retained release maps to one version-index entry;
- every unique SHA maps to at most one canonical snapshot;
- every source-ledger link resolves to immutable raw evidence;
- release-note and changelog absence is explicit rather than silently omitted;
- no generated patch or summary appears under `raw/`; and
- no packet is marked ingested after failed wiki or collection validation.

Collection failure for one release does not promote a partial snapshot. Other selected releases may complete, but the run manifest must reconcile every selected ref to a terminal collection state.

## Testing

Deterministic local tests must cover:

- stable-only major selection when a newer prerelease exists;
- exact prerelease selection;
- all-stable and minor-baseline selection;
- deduplication of overlapping baseline rules;
- one snapshot for same-SHA aliases;
- default branch differing from the latest release;
- changelog and release-note preservation;
- absent release evidence;
- periodic discovery of one new patch release;
- rewritten or deleted tag reporting; and
- one packet per new release with no automatic ingest transition.

Network-dependent PayPal verification remains outside the default unit suite.

## Implementation Impact

Before resuming implementation, update the existing plan so:

- Task 4 adds shared version semantics and registry release tracks;
- Task 5 discovers retained releases and exact available release notes;
- Task 6 accepts `changed_paths` and completes archive-safety remediation;
- Task 7 packets include release-note and changelog evidence links;
- Task 8 CLI enumerates configured version tracks and future releases;
- Task 9 validates release retention and source-ledger evidence;
- Task 10 proves multi-release behavior locally; and
- Tasks 11-12 apply the hybrid PayPal JS policy and serial release ingest.

The live-pilot hard user gate remains unchanged.
