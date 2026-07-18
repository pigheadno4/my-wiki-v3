# GitHub Tracked Source Capsule and Deep-Dive Design

**Status:** Revised after second decline review; pending final user review
**Date:** 2026-07-18
**Extends:** `2026-07-14-github-repository-collection-design.md` and `2026-07-15-github-release-retention-design.md`

## Problem

The GitHub collector currently preserves repository documentation, package manifests, changelogs, release notes, and selected changed public files. TypeScript coverage is accidental: a source file is retained only when it is an explicit registry key path or a changed path matching the public-entrypoint heuristic.

The PayPal JS pilot exposes the gap. Its 15 canonical snapshots contain only sparse TypeScript entrypoints, so later implementation questions may not be answerable from retained raw evidence. Saving every repository file for every release would make full-read ingest impractical.

The collector needs a bounded, deterministic tracked-source capsule for selected packages, plus immutable same-SHA deep-dive supplements for questions outside the capsule.

## Goals

- Preserve complete tracked source within an explicit package scope.
- Include required internal workspace packages without collecting unrelated packages.
- Keep every capsule packet within a numeric, preflighted full-reading budget.
- State exactly what is complete and what remains unverified.
- Retain canonical snapshots and all supplements as first-class immutable evidence.
- Support shared-SHA package releases without attaching evidence to the wrong identity.
- Add same-SHA supplement packets without rewriting or superseding release packets.
- Recover deterministically from crashes across raw, index, and packet publication.
- Retry transient failures within a fixed bound and quarantine repeated failures.
- Keep collection batchable and ingest user-gated, serial, and full-read.

## Non-Goals

- Mirroring a complete Git repository.
- Claiming equivalence between tracked source and a published npm artifact.
- Executing repository code, package managers, builds, tests, or generators.
- Parsing JavaScript or TypeScript import graphs in the first adapter.
- Collecting external dependency source.
- Covering Swift, Android, PHP, Ruby, or other ecosystems with an npm adapter.
- Automatically approving or ingesting any packet.
- Rewriting existing PayPal JS snapshots or packets.

## Corrected Architecture

The earlier draft proposed replacing unapproved release packets after adding capsule evidence. That approach is rejected. Replacement packets create stale delta graphs and require an irreversible supersession event across several filesystem namespaces.

The corrected design keeps release evidence and source-capsule evidence as separate ingest units:

```text
release collection
    -> immutable canonical release snapshot
    -> baseline or delta release packet

source capsule collection at the same SHA
    -> immutable -rN supplement
    -> same-SHA supplement packet
```

This applies to existing and future releases. A source capsule is always a supplement, never an in-place enrichment of a canonical snapshot. Existing release packets remain byte-for-byte unchanged. A capsule packet reads and ingests only the newly attached capsule evidence, with the canonical manifest as provenance context.

The first adapter is named `npm-tracked-source-v1`. This name deliberately avoids claiming verified correspondence with generated npm artifacts.

## Normative Registry Schema

`capsules` becomes an optional array on a repository row. Unknown keys remain errors.

```toml
[[repos.capsules]]
id = "react-paypal-js-runtime"
adapter = "npm-tracked-source-v1"
focus_packages = ["@paypal/react-paypal-js"]
dependency_scope = "internal-runtime-closure"
default_required_roots = ["src"]
default_generated_target_roots = ["dist"]
include_paths = []
excluded_categories = ["tests", "stories", "fixtures"]
secret_detector = "text-secrets-v1"
max_file_bytes = 512000
max_capsule_files = 120
max_capsule_utf8_bytes = 750000
max_packet_files = 160
max_packet_utf8_bytes = 1000000

[[repos.capsules.package_overrides]]
name = "@paypal/paypal-js"
required_roots = ["src", "types"]
generated_target_roots = ["dist"]
include_paths = []

[[repos.secret_allowlist]]
path = "path/to/reviewed-file.ts"
blob_oid = "<40-or-64-lowercase-hex>"
detector_code = "<stable-detector-code>"
```

Each capsule object has these exact fields:

| Field | Required | Type | Rule |
| --- | --- | --- | --- |
| `id` | yes | string | Unique repository-local ASCII slug matching `[a-z0-9][a-z0-9-]{0,62}`. |
| `adapter` | yes | string | Exactly `npm-tracked-source-v1`. |
| `focus_packages` | yes | list of strings | Non-empty, unique ASCII npm package names accepted by the existing package-tag parser. |
| `dependency_scope` | no | string | Defaults to and may only equal `internal-runtime-closure`. |
| `default_required_roots` | no | list of paths | Defaults to `["src"]`. Package-relative POSIX paths. |
| `default_generated_target_roots` | no | list of paths | Defaults to empty. Package-relative top-level directories explicitly reviewed as generated output. |
| `include_paths` | no | list of paths | Defaults to empty. Applied package-relative to every included package. |
| `excluded_categories` | no | list of enums | Defaults to `tests`, `stories`, and `fixtures`; only those values are accepted in v1. |
| `secret_detector` | no | string | Defaults to and may only equal `text-secrets-v1`. |
| `max_file_bytes` | no | integer | Defaults to 512,000; positive raw-byte limit for one file. |
| `max_capsule_files` | no | integer | Defaults to 120; positive count of saved upstream files. |
| `max_capsule_utf8_bytes` | no | integer | Defaults to 750,000; positive sum of saved upstream file bytes. |
| `max_packet_files` | no | integer | Defaults to 160; positive full-reading file count. |
| `max_packet_utf8_bytes` | no | integer | Defaults to 1,000,000; positive full-reading byte count. |
| `package_overrides` | no | list of tables | Defaults to empty; names must be unique within the capsule. |

Each package override has exactly `name`, `required_roots`, `generated_target_roots`, and `include_paths`. All are required. `required_roots` is non-empty; `generated_target_roots` and `include_paths` may be empty. Unknown capsule or override keys fail registry loading.

For an overridden package, `required_roots` and `generated_target_roots` replace their corresponding defaults; global and override `include_paths` are combined and deduplicated. A package in the resolved closure without an override uses the defaults. Every generated target root is exactly one safe top-level path segment. Nested paths, `.`, and names that overlap a required root fail registry loading.

`secret_allowlist` is an optional repository-level array. Each row has exactly `path`, `blob_oid`, and `detector_code`; all are required. Paths follow the same safe repository-relative rules, object IDs must be 40 or 64 lowercase hexadecimal characters, and duplicate triples fail. An allowlist row applies only to that exact immutable blob and detector finding. It is included in the effective collection policy hash.

Paths cannot be absolute, empty, contain `.` or `..` segments, contain backslashes, or escape the package directory. V1 paths are literal paths, not globs. Exclusions use adapter-owned category classifiers rather than arbitrary registry globs, preventing a repository policy from silently excluding production source.

The effective policy is the adapter version, all versioned defaults, and normalized repository values. It is serialized as compact canonical JSON with sorted object keys and original list order replaced by deterministic sorted order where order has no semantics. Its SHA-256 is the `policy_hash`. TOML formatting and key order do not affect the hash.

The registry continues to contain stable intent only. Resolved paths, SHAs, attempts, collection dates, policy results, and progress remain generated state.

## Standard-Library NPM Workspace Resolution

The adapter uses Python 3.9 standard-library JSON handling plus existing Git commands. JSON is parsed with duplicate-key rejection.

Accepted workspace declarations are:

- a list of non-empty strings; or
- an object with exactly `packages` and optional `nohoist`, where both values are lists of strings.

`nohoist` is validated but does not change package discovery. The repository root `package.json` is also considered a package independently of workspace patterns.

Workspace patterns support only literal path segments and a whole-segment `*`. V1 rejects `**`, braces, character classes, negation, backslashes, absolute paths, and parent traversal. This supports PayPal's `packages/*` and `packages/react-paypal-js-storybook/*`. Expansion is against tracked tree directories at the exact SHA, sorted by POSIX path. Overlapping patterns deduplicate by path. Every discovered package directory must contain one regular tracked UTF-8 `package.json`; duplicate package names fail.

For every focus package, the resolver recursively includes workspace packages named in:

- `dependencies`;
- `optionalDependencies`; and
- `peerDependencies`, including peers marked optional.

`devDependencies` never extend the closure. `dependencies`, `optionalDependencies`, and `peerDependencies` must be objects whose keys and values are strings. `peerDependenciesMeta`, when present, must be an object. Every metadata key must name an existing peer; every value must be an object containing exactly `optional` with a Boolean value. Unsupported or malformed metadata is `needs-policy-review`.

Normalization is exact. A name in `optionalDependencies` suppresses the same name in `dependencies` and emits one `optional-dependency` edge with `optional = true`. A peer always emits a separate `peer-dependency` edge, even when the same name also has a runtime edge; its optional flag is the corresponding `peerDependenciesMeta.optional`, defaulting to false. A remaining dependency emits `dependency` with `optional = false`. Duplicate JSON keys are rejected before this reduction, and duplicate normalized `(from_package, to_name, dependency_kind)` edges are invalid.

If a normalized dependency name matches a workspace package, v1 includes that package regardless of npm range syntax and records the declared specification and local package version. V1 does not claim npm semver-range compatibility.

`workspace:`, `file:`, and `link:` specifications are recorded. A `file:` or `link:` target that resolves inside the repository must identify the same discovered package path and name; otherwise collection fails. External dependency names and specifications are recorded but their source is not collected. Cycles are resolved with a visited set and deterministic package-name ordering.

Malformed manifests, unsupported workspace forms, ambiguous focus packages, duplicate names, and unsafe local dependency targets are deterministic `needs-policy-review` failures.

## Required File Classification

The adapter reads the exact commit tree with `git ls-tree -rz` and reads blobs with `git cat-file blob`. It does not trust or execute working-tree files.

For each included package, classification uses this precedence:

1. Unsafe paths, symlinks, gitlinks, non-blobs, LFS pointers, non-UTF-8 content, NUL-containing content, and oversized files fail if selected by any required rule.
2. `package.json`, literal `include_paths`, tracked `main` or `bin` wrappers, and tracked type declaration targets are required. A configured exclusion cannot remove them.
3. Files recognized by an enabled excluded category are outside capsule scope.
4. Every remaining regular tracked UTF-8 file below a required root is required.
5. Documentation and examples outside required roots remain optional existing snapshot evidence and are not part of capsule completeness.

Category classifiers are fixed in adapter v1:

- `tests`: filenames containing `.test.` or `.spec.`, and path segments `test`, `tests`, `__tests__`, or `bundle-tests`;
- `stories`: filenames containing `.stories.` and path segments `.storybook`, `storybook`, or `stories`; and
- `fixtures`: path segments `fixture`, `fixtures`, `__fixtures__`, or `snapshots`.

Changing these classifiers requires a new adapter version.

The adapter records `exports`, conditional exports, wildcard export values, `main`, `module`, `types`, `typings`, `bin`, and `files` declarations. It recursively walks JSON export values but does not expand wildcard targets.

- A tracked `types` or export `types` target is required. Because declaration files can reference sibling declarations, the complete tracked top-level declaration directory containing that target is required. This captures PayPal's tracked `types/` tree.
- A tracked `main` or `bin` target is required.
- A missing target is `generated-target-not-tracked` only when its normalized first path segment exactly equals a `generated_target_root` declared for that package. The manifest records the matching root.
- A missing target with no matching reviewed generated root is `needs-policy-review`; the adapter never infers generated output from names such as `dist`, `build`, or `lib`.
- Other escaping, symlink, or unsafe declared targets fail.
- Generated targets are not mapped back to source without executing the build or parsing build configuration.

The manifest therefore reports three independent statements:

```text
Tracked source scope completeness: complete
Published artifact correspondence: unverified-generated-targets
Repository completeness: intentionally incomplete
```

`Tracked source scope completeness: complete` is valid only when every required file after category classification is saved and validated. The capsule does not claim that declared generated targets match captured source or that all repository behavior is covered. A generated-root declaration is an operator-reviewed classification, not proof of artifact provenance.

## Capsule Snapshot Manifest

Existing snapshot manifest format 2 remains valid and retains its exact parser. A supplement uses format 3. At the top level, format 3 preserves every format-2 field and adds exactly `capture_purpose`, `canonical_snapshot`, and `capsule`. Its `files` records use the complete format-3 schema below; format-2 file records are not retroactively changed.

`capture_purpose` is `source-capsule`, `policy-upgrade`, or `query-deep-dive`. `canonical_snapshot` is the repository-relative path of the unique canonical capture at the same SHA.

The `capsule` object has exactly:

```json
{
  "adapter": "npm-tracked-source-v1",
  "capsule_id": "react-paypal-js-runtime",
  "policy_hash": "<64-hex>",
  "focus_packages": ["@paypal/react-paypal-js"],
  "included_packages": [],
  "dependency_edges": [],
  "external_dependencies": [],
  "required_roots": [],
  "generated_target_roots": [],
  "include_paths": [],
  "excluded_categories": ["fixtures", "stories", "tests"],
  "declared_targets": [],
  "secret_scan": {
    "detector": "text-secrets-v1",
    "scanned_blob_count": 0
  },
  "tracked_source_scope_completeness": "complete",
  "published_artifact_correspondence": "unverified-generated-targets",
  "repository_completeness": "intentionally-incomplete"
}
```

Nested records have these exact schemas:

- `included_packages`: `{name, path, version, reason}`, where reason is `focus` or `internal-runtime-dependency`;
- `dependency_edges`: `{from_package, to_package, dependency_kind, specification, optional}`, where kind is `dependency`, `optional-dependency`, or `peer-dependency`;
- `external_dependencies`: `{from_package, name, dependency_kind, specification, optional}`;
- `required_roots`: `{package, path, source}`, where source is `default`, `package-override`, or `tracked-declaration-target`;
- `generated_target_roots`: `{package, path, source}`, where source is `default` or `package-override`;
- `include_paths`: `{package, path, source}`, where source is `capsule-policy`, `package-override`, or `declared-target`;
- `declared_targets`: `{package, field, export_key, condition, target, status, generated_root}`, where empty strings represent inapplicable export key, condition, or generated root and status is `tracked-required`, `generated-target-not-tracked`, or `recorded-pattern`; and
- `secret_scan`: exactly `{detector, scanned_blob_count}`. The detector is `text-secrets-v1`; the count is a non-negative integer and is recomputed from selected Git blobs.

These arrays sort by package name and then POSIX path or target; dependency arrays additionally sort by kind and destination name. The design does not permit free-form summary strings in these records.

Every format-3 `files` entry has exactly:

```json
{
  "path": "files/packages/example/src/index.ts",
  "sha256": "<64-lowercase-hex>",
  "size": 123,
  "purpose": "source-capsule",
  "git_blob_oid": "<40-or-64-lowercase-hex>",
  "git_mode": "100644",
  "package": "@scope/example",
  "classification_reason": "required-root"
}
```

`path`, `sha256`, `size`, and `purpose` retain their format-2 meanings. `git_blob_oid` is the exact object ID read by `git cat-file`; `git_mode` is exactly `100644` or `100755`. `package` is the owning resolved npm package for npm capsules and is the empty string for an explicit deep dive. Allowed npm classification reasons are `package-manifest`, `required-root`, `include-path`, `tracked-main-target`, `tracked-bin-target`, `tracked-types-target`, and `tracked-declaration-directory`. A deep-dive file uses `deep-dive-request`. When more than one rule selects a file, the first matching reason in that listed order is recorded. Unknown fields, modes, purposes, or reasons fail validation.

Validators recompute the package closure, required-file set, policy hash, detector identity, completeness fields, object IDs, modes, and file hashes from the exact Git tree before promotion. The immutable source-capsule manifest is scoped only by repository, SHA, adapter, capsule ID, and policy hash. It never contains version applicability. Index adapter, capsule ID, policy hash, focus packages, SHA, canonical path, kind, and revision must match the immutable manifest exactly; `applies_to_version_ids` exists only in the generated index.

Query deep dives use the same format with adapter `explicit-git-blobs-v1`. Their `capsule` object instead has exactly `adapter`, `capsule_id`, `policy_hash`, `request_id`, `request_hash`, `question_hash`, `requested_version_id`, `paths`, `secret_scan`, `tracked_source_scope_completeness`, and `repository_completeness`. `paths` is the sorted exact `{path, reason}` list from the immutable request. `secret_scan` has the same exact schema as above. Completeness must be `complete-for-requested-paths`; repository completeness remains `intentionally-incomplete`. The immutable raw manifest does not duplicate the full question text. Later version applicability is not added to a deep-dive manifest.

## Full-Reading Budget Contract

All limits count raw bytes, not characters or estimated tokens. Every required reading file must decode as strict UTF-8 and contain no NUL byte.

Capsule accounting includes every saved upstream blob but excludes the generated `snapshot.md`. Packet accounting includes:

- `ingest-packet.md`;
- the canonical `snapshot.md` used for provenance;
- every added supplement `snapshot.md`;
- every upstream file and release-note file listed as required reading; and
- no generated `changed-files.txt` or `source-diff.patch` aid.

Paths are deduplicated before file and byte accounting. `max_packet_files` counts the files above, including `ingest-packet.md`. `max_packet_utf8_bytes` is their exact byte sum after the packet Markdown has been rendered.

`ingest-packet.md` renders configured maxima and required paths but not the derived `actual_*` values, so its bytes do not depend on the result being measured. Actual values live in `packet.json` and are validated from disk.

Capsule selection, manifest rendering, packet rendering, and both budget checks occur in transaction staging before any raw snapshot, index, or packet publication. A capsule that passes its own limits but fails packet limits is a failed collection with no promoted evidence.

V1 does not automatically split a capsule. Automatic split identity is intentionally unsupported. An over-budget capsule enters `needs-policy-review`; the operator must approve larger bounded limits or define a separately designed adapter version. This removes ambiguous partial-capsule semantics.

## Version Index V2

Source capsules require an explicit generated index migration. A v2 index has exactly these top-level keys:

```json
{
  "format_version": 2,
  "repo_id": "paypal/paypal-js",
  "capture_order": ["<sha>"],
  "branch_observations": [],
  "captures": [],
  "versions": []
}
```

### Capture Records

Each capture record has exactly:

```json
{
  "capture_id": "<full-sha>:r1",
  "sha": "<full-sha>",
  "capture_kind": "supplement",
  "capture_revision": 1,
  "snapshot_path": "raw/github/paypal/paypal-js/snapshots/<capture>",
  "collection_date": "YYYY-MM-DD",
  "purpose": "source-capsule",
  "adapter": "npm-tracked-source-v1",
  "capsule_id": "react-paypal-js-runtime",
  "policy_hash": "<64-lowercase-hex-or-empty>",
  "focus_packages": ["@paypal/react-paypal-js"],
  "applies_to_version_ids": ["<64-lowercase-hex>"]
}
```

Canonical IDs are `<sha>:c0`; supplement IDs are `<sha>:rN`. Allowed purposes are `release-evidence`, `legacy-supplement`, `release-alias-evidence`, `source-capsule`, `policy-upgrade`, and `query-deep-dive`. Canonical and legacy records use empty `adapter` and `capsule_id` values. Source capsules and policy upgrades use adapter `npm-tracked-source-v1` and the exact registry capsule ID. Query deep dives use adapter `explicit-git-blobs-v1` and the immutable request ID as capsule ID. Canonical records use revision zero, purpose `release-evidence`, an empty policy hash, and empty focus packages. Supplements use a positive revision unique per SHA. Capture records sort by `capture_order`, canonical before supplement, then revision.

Every snapshot path must resolve to an immutable manifest whose repository, SHA, kind, revision, adapter, capsule ID, and policy hash exactly match the capture record. A canonical capture applies to every version identity at its SHA. A supplement applies only to the explicit version IDs listed in the generated capture record and those versions' `evidence_ids`. Applicability is index metadata and is deliberately absent from immutable raw manifests.

Within one repository, `(sha, adapter, capsule_id, policy_hash)` identifies at most one source-capsule capture. `focus_packages` and `applies_to_version_ids` are sorted unique lists. A later release identity sharing the SHA attaches that existing raw capture by changing only the generated index and creating an independent supplement packet. The existing manifest and capture directory remain byte-for-byte unchanged. An A-then-later-B shared-SHA sequence must validate before and after attachment without duplicating or modifying raw evidence.

### Version Records

Each version record has exactly:

```json
{
  "version_id": "<64-lowercase-hex>",
  "ref_kind": "package-version",
  "ref_name": "@paypal/react-paypal-js@10.1.1",
  "version": "10.1.1",
  "sha": "<full-sha>",
  "aliases": [],
  "package": "@paypal/react-paypal-js",
  "evidence_ids": ["<full-sha>:c0", "<full-sha>:r1"],
  "release_notes_paths": [],
  "changelog_paths": []
}
```

`version_id` is SHA-256 over compact JSON with sorted keys containing exactly `package`, `ref_kind`, `ref_name`, `sha`, and `version`. Aliases and evidence do not affect identity. This preserves separate package-release identities sharing one SHA.

`evidence_ids` always begins with that SHA's canonical capture and then lists only applicable supplements in increasing revision order. Release-note and changelog paths must be inside captures named by `evidence_ids`. Version records retain the existing deterministic identity and semantic ordering rules.

The validator requires bidirectional agreement: every capture `applies_to_version_ids` reference must exist and include the capture in `evidence_ids`, and every noncanonical `evidence_ids` item must name a capture listing that version. Cross-SHA and cross-repository attachment is invalid.

### V1 Migration

An index without `format_version` is v1. It remains readable for existing release collection and validation, but capsule collection is blocked until explicit migration.

`migrate-index-v2 --repo <id> --dry-run` performs these deterministic steps:

1. group v1 entries by SHA and require one canonical path per SHA;
2. create one canonical capture record per SHA;
3. create one version record per existing release, branch, tag, or commit identity;
4. preserve aliases, release-note paths, changelog paths, capture order, and branch observations;
5. scan immutable snapshot manifests under the repository snapshot root for same-SHA supplements;
6. map legacy supplements only when their release evidence identifies exact existing version identities;
7. classify a mapped old supplement as `legacy-supplement`; and
8. fail migration on an unreferenced or ambiguous supplement rather than guessing its scope.

Dry-run writes no generated state. Approved migration stages a complete v2 index, validates a save/reload round trip, and publishes exactly one `index-v2-migrate` transaction and `index-migrated-v2` run event through the protocol below. Its immutable artifact set is empty; its before and after index hashes must differ. V1 is never rewritten implicitly. Loading v2 and saving it without semantic changes must be byte-identical.

## Packet Contract V2

Existing packet v1 directories remain valid and immutable. New supplement packets use packet contract v2 with exactly:

```json
{
  "format_version": 2,
  "packet_id": "<deterministic-id>",
  "repo_id": "paypal/paypal-js",
  "packet_type": "supplement",
  "initial_state": "awaiting-review",
  "from": {
    "version_id": "<id>",
    "sha": "<sha>",
    "evidence_ids": ["<sha>:c0"]
  },
  "to": {
    "version_id": "<id>",
    "sha": "<sha>",
    "evidence_ids": ["<sha>:c0", "<sha>:r1"]
  },
  "added_evidence_ids": ["<sha>:r1"],
  "required_reading": [],
  "changed_files": [],
  "reading_budget": {
    "max_files": 160,
    "max_utf8_bytes": 1000000,
    "actual_files": 0,
    "actual_utf8_bytes": 0
  }
}
```

Packet contract v2 permits exactly `packet_type = "supplement"`. Baseline, delta, and comparison remain packet-v1 contracts until a separate design specifies their v2 invariants. For a supplement packet:

- `from` and `to` identify the same version ID and SHA;
- `from.evidence_ids` is a strict prefix of `to.evidence_ids`;
- `added_evidence_ids` is exactly the non-empty suffix;
- every added capture is a supplement applicable to that version;
- `changed_files` is empty; and
- required reading is canonical `snapshot.md`, each added supplement manifest, and every file recorded by the added supplements, in deterministic path order.

Packet IDs hash the normalized semantic contract excluding `packet_id` and the two `actual_*` budget fields, then prepend a bounded readable label. Actual budget values are deterministic derivatives of required reading and are independently validated, so they do not participate in identity. Required-reading paths and evidence IDs do participate, so different evidence sets cannot share an ID.

Packet v1 parsing remains exact for old packets. Packet v2 parsing uses only the v2 schema. A packet directory cannot mix versions.

When validating a v1 packet against index v2, its endpoint tuple of repository, ref kind, ref name, package, version, and SHA must resolve to exactly one v2 `version_id`; zero or multiple matches are errors. Migration never rewrites packet JSON.

The packet state machine remains unchanged:

```text
awaiting-review -> approved | rejected
approved -> ingesting | rejected
ingesting -> ingested | validation-failed
validation-failed -> approved | rejected
ingested and rejected are terminal
```

State-event JSONL retains the existing exact event shapes. There is no `superseded` state and no replacement link. Adding evidence always creates an independent supplement packet, so no existing packet or state history is rewritten.

## Recoverable Publication Protocol

Filesystem operations across raw snapshots, packets, and the index cannot be one atomic rename. The implementation therefore uses a repository-scoped write-ahead journal and deterministic recovery rather than claiming cross-directory atomicity.

Generated transaction state lives at:

```text
tracking/github/repos/<company>/<repo>/transactions/<transaction-id>/
├── events.jsonl
├── before-index.json
├── after-index.json
├── staged-artifacts/     # snapshots and/or packet until publication
├── terminal-event.jsonl  # exact staged run file
└── COMMITTED
```

The transaction ID is a 64-character lowercase SHA-256 over repository ID, operation, exact SHA or empty string, policy hash or empty string, selected version ID or empty string, capsule ID or request ID or empty string, run ID, and attempt ordinal. This makes retries distinct while leaving each interrupted attempt recoverable by its journal.

### Operations And Terminal Events

The protocol supports exactly these operation shapes:

| Operation | Immutable artifacts | Index change | Terminal state |
| --- | --- | --- | --- |
| `index-v2-migrate` | none | complete v1-to-v2 replacement | `index-migrated-v2` |
| `source-capsule-collect` | one new supplement and one packet | add capture and attach it to one version | `source-capsule-collected` |
| `source-capsule-attach` | one packet; existing raw capture is reused | attach existing capture to one additional version | `source-capsule-attached` |
| `source-capsule-check` | none | none; before and after index hashes are equal | `source-capsule-unchanged` |
| `deep-dive-collect` | one new supplement and one packet | add capture and attach it to the requested version | `deep-dive-collected` |

Every transaction reserves a unique run ID and exact run path before preparation:

```text
tracking/github/runs/<run-id>.jsonl
```

`run_id` is the command's pre-existing collection run ID, matching `[0-9]{8}T[0-9]{12}Z-[a-z0-9-]{1,80}-[0-9a-f]{32}` and containing no path separators. Tests inject its UTC timestamp and nonce. A command creates a separate run ID for each event-v2 transaction, so several capsule operations selected by one invocation cannot collide.

The final run file must not exist during preparation. `terminal-event.jsonl` is written with exactly one compact JSON line plus `\n`, file-`fsync`ed, and recorded by device, inode, byte size, and SHA-256 before `prepared`. It is later published with an atomic no-replace hard link into `tracking/github/runs/`; source and destination directories must be on the same device. All event-v2 operations use this exact terminal schema; inapplicable string fields are empty rather than omitted:

```json
{
  "event_version": 2,
  "transaction_id": "<64-hex>",
  "run_id": "<bounded-run-id>",
  "operation_id": "<bounded-stable-operation-id>",
  "dry_run": false,
  "repo_id": "paypal/paypal-js",
  "selector": "<stable-selector-or-index-v2>",
  "operation": "source-capsule-collect",
  "state": "source-capsule-collected",
  "ref_name": "<resolved-ref-or-empty>",
  "sha": "<full-sha-or-empty>",
  "version_id": "<version-id-or-empty>",
  "capture_id": "<capture-id-or-empty>",
  "packet_id": "<packet-id-or-empty>",
  "request_id": "<request-id-or-empty>",
  "index_hash": "<64-hex>"
}
```

The allowed operation/state pairs are exactly those in the table. Migration uses selector and operation ID `index-v2` and empty ref, SHA, version, capture, packet, and request fields. A source-capsule operation ID is `capsule:<capsule-id>:<policy-hash>:<version-id>`. A deep-dive operation ID is `deep-dive:<request-id>`. Collection and attachment require capture and packet IDs; unchanged checks require the existing capture ID and an empty packet ID; deep dive additionally requires its request ID.

Legacy event-v1 run files retain existing reconciliation by `(repo_id, selector)`. Each event-v2 run file validates independently and contains exactly one terminal event for its transaction. Across event-v2 history, `transaction_id` and `run_id` are independently unique, the filename must equal `<run_id>.jsonl`, and the journaled run path must resolve to that file. The event-v2 status reducer keys latest results by `(repo_id, operation_id)` and never assumes one terminal event per selector, so several capsules for one release are representable.

### Locks And Preparation

The repository `.collection.lock` is acquired first and held through recovery or publication. Nested lock order is exactly:

```text
collection lock -> repository snapshot-root promotion lock -> packet lock
```

The snapshot-root promotion lock is the existing stable `.promotion.lock` below that repository's snapshot root. It is acquired once when an operation may create a snapshot. Final `-rN` allocation occurs while this stable lock is held; no final snapshot path is needed to identify the lock. After revision allocation and packet-ID derivation, the exact packet lock is acquired. Index-only migration acquires neither nested lock. Source-capsule attachment acquires only the packet lock because it creates no raw snapshot. No mutating path may acquire these locks in reverse order.

Packet lifecycle transitions also acquire the repository collection lock before the packet lock and recover or block on unfinished journals before reading packet state. This prevents approval of a packet published by an uncommitted transaction.

The transaction coordinator owns these descriptors. Snapshot and packet publication gain internal variants that accept already-open, already-locked parent descriptors; they must not reacquire the same lock through another descriptor. Public single-artifact helpers retain their current lock-owning behavior outside a journal transaction.

Before publication, the collector:

1. recovers every nonterminal transaction for the repository;
2. preflights packet lifecycle and index expectations;
3. acquires the stable repository snapshot-root promotion lock when required;
4. allocates final supplement revisions while that stable lock is held;
5. derives the packet ID, acquires its packet lock when required, and retains all locks through commit or rollback;
6. stages and validates the operation's exact immutable artifact set;
7. writes exact prior and intended index bytes;
8. renders and file-`fsync`s `terminal-event.jsonl`, records its ownership identity, and reserves a non-existing run path;
9. appends and `fsync`s a `prepared` journal event containing all paths and SHA-256 hashes; and
10. `fsync`s the transaction directory.

Publication then:

1. promotes each owned immutable snapshot or packet, `fsync`s its destination parent directory, and journals path, device, inode, and content hash;
2. when the operation table requires an index change, atomically replaces the index, `fsync`s the index file and its parent directory, and journals the resulting hash; otherwise requires equal before/after hashes and emits no `index-published` event;
3. atomically hard-links the staged terminal file to the reserved run path with no replacement, verifies the linked inode and bytes, `fsync`s `tracking/github/runs/`, and journals publication;
4. writes and file-`fsync`s `COMMITTED`, then `fsync`s the transaction directory; and
5. releases locks.

Every journal event is one compact JSON object, appended with one write and file `fsync`. Events have monotonically increasing `sequence`, exact operation names, and no free-form secret content. The prepared journal stores the exact run ID, run path, terminal bytes hash, and intended terminal event. Recovery can therefore locate the event without searching other run files.

A directory content hash is SHA-256 over canonical JSON listing every relative path, Git-style mode, byte size, and file SHA-256 in sorted path order. Ownership journal events store this hash together with device and inode.

Every journal event has required common fields `event_version = 1`, `transaction_id`, `sequence`, and `event`. Event-specific fields are exact:

| Event | Additional fields |
| --- | --- |
| `prepared` | `repo_id`, `operation`, `before_index_hash`, `after_index_hash`, `planned_artifacts`, `run_id`, `run_path`, `run_device`, `run_inode`, `terminal_event`, `terminal_event_hash` |
| `artifact-published` | `artifact_kind`, `path`, `device`, `inode`, `content_hash` |
| `index-published` | `after_index_hash` |
| `terminal-event-published` | `run_path`, `terminal_event_hash` |
| `rolled-back` | `reason_code` |
| `recovery-required` | `reason_code`, `observed_index_hash` |

`planned_artifacts` is the operation table's exact sorted set of records `{artifact_kind, path, staged_device, staged_inode, content_hash}` for snapshots and packets. Promotion must be a same-device rename, so the staged ownership identity remains valid at the final path even if a crash occurs before `artifact-published` is journaled. Index publication is represented by its dedicated hashes. Run publication is represented by `run_id`, `run_path`, `run_device`, `run_inode`, and `terminal_event_hash` in `prepared`. Journal parsing rejects unknown fields, duplicate sequences, sequence gaps, an artifact set inconsistent with the operation, events invalid for the current phase, and hashes or ownership identities that disagree with staged bytes. `COMMITTED` is a zero-byte regular file created with exclusive no-follow semantics and then file- and directory-`fsync`ed.

Recovery under the collection lock follows these rules:

- `source-capsule-check` has no mutable artifact or index phase; recovery either publishes its prepared terminal event or recognizes the matching event and commits;
- before index publication, verify ownership tokens, remove only transaction-owned snapshots and packets, restore no index, and append `rolled-back`;
- after index publication but before terminal-event publication, complete forward when every artifact matches, or atomically restore `before-index.json` and remove only verified owned artifacts when an artifact is missing;
- terminal-event publication is the irreversible forward-only boundary; recovery detects it only at the exact journaled run path and accepts it only when its device, inode, sole-line transaction ID, and byte hash match the staged run identity, even if `terminal-event-published` was not journaled;
- after that boundary, intact artifacts and index complete forward by writing `COMMITTED`, while any mismatch becomes `recovery-required` rather than rollback;
- if an existing artifact's device, inode, or content hash differs from the journal, mark `recovery-required` without deleting or rewriting it;
- if the current index matches neither recorded hash, mark `recovery-required`, block further collection, and require manual review; and
- never delete or rewrite an artifact without matching repository namespace, path, device, inode, and expected hash.

Every recovery rename, index restoration, and verified artifact removal is followed by `fsync` of the affected parent directory before the recovery journal advances. If the run path exists with any other bytes, recovery marks `recovery-required` and never edits or deletes it. If rollback occurs before terminal publication, the still-absent reserved run path requires no cleanup. Read-only validation reports nonterminal or `recovery-required` journals but does not mutate them. Collection and explicit `recover` perform recovery. Crash tests interrupt after every file write, file `fsync`, rename, unlink, parent-directory `fsync`, and journal append.

Packet directory hashes in a committed journal describe publication-time bytes with the initial state event. Later valid packet-state appends intentionally change that directory, so completed-journal validation does not compare the current packet tree to its publication hash. Nonterminal recovery can compare it because the packet lock prevents lifecycle transitions until commit.

## Normal Capsule Collection

For each selected release or branch with capsule policy:

1. resolve the exact version identity and SHA;
2. require or explicitly migrate version index v2;
3. check for an existing capture with the same SHA, capsule ID, adapter, and policy hash;
4. when no matching capture exists, inspect exact Git objects, resolve package scope, and stage a `source-capsule-collect` transaction with one supplement and packet;
5. when a matching capture exists but is not applicable to this version, stage a `source-capsule-attach` transaction with only the updated index and new packet;
6. when a matching capture is already applicable, stage a `source-capsule-check` transaction with identical before/after index bytes and no packet;
7. run the exact snapshot, evidence attachment, detector, UTF-8, and packet-budget validators required by the selected operation;
8. publish through the recoverable journal;
9. leave every newly created packet `awaiting-review`; and
10. emit the operation-specific event-v2 terminal state.

Same SHA, capsule ID, policy hash, and already-attached version ID produces `source-capsule-unchanged`. If the capture exists but is not attached to a newly discovered version identity sharing that SHA, the collector reuses the raw capture byte-for-byte, updates bidirectional index references, and creates a supplement packet for that version. A changed policy hash creates a new `policy-upgrade` supplement; it never edits the earlier capsule. Collection may process multiple refs but obtains one repository lock and transaction at a time. It never approves or ingests packets.

The public CLI additions are:

```text
collect --repo <id> --capsules [--dry-run]
migrate-index-v2 --repo <id> [--dry-run]
deep-dive --repo <id> --request <tracking-json-path> [--dry-run]
recover --repo <id>
retry-due [--repo <id>]
retry-reset --repo <id> --operation <operation> --selector <selector> --unit-id <id> --actor <id> --reason <text>
```

`--now` is accepted only by internal APIs and tests, not the production CLI. Production commands use an injected UTC clock initialized from the system clock once per command.

## Persistent Retry And Quarantine State

Retry state is an append-only event log:

```text
tracking/github/repos/<company>/<repo>/collection-failures.jsonl
```

Each failed-attempt event has exactly:

```json
{
  "event_version": 1,
  "event": "attempt-failed",
  "attempt_id": "<64-hex>",
  "retry_key": "<64-hex>",
  "repo_id": "paypal/paypal-js",
  "operation": "capsule",
  "selector": "<stable-selector>",
  "unit_id": "<capsule-id:policy-hash>",
  "resolved_sha": "<sha-or-empty>",
  "policy_hash": "<hash-or-empty>",
  "phase": "resolve|inspect|stage|publish|recover",
  "category": "transient|deterministic-policy|unknown",
  "code": "<bounded-stable-error-code>",
  "fingerprint": "<64-hex>",
  "epoch": 1,
  "attempt": 1,
  "outcome": "retry-pending|needs-policy-review|quarantined",
  "observed_at": "<UTC-RFC3339>",
  "next_retry_at": "<UTC-RFC3339-or-empty>"
}
```

Retry state is keyed by the exact executable scheduling unit, never by failure phase:

| Operation | Selector | Unit ID |
| --- | --- | --- |
| `capsule` | exact release or branch selector | `<capsule-id>:<policy-hash>` |
| `deep-dive` | selected version's stable selector | request ID |
| `index-migration` | `index-v2` | `index-v2` |
| `recover` | transaction ID | transaction ID |

`retry_key` hashes exactly repository ID, operation, selector, and unit ID. `resolved_sha`, `policy_hash`, and `phase` are failure observations and never create parallel retry keys. A changed capsule policy creates a new unit ID; a changed deep-dive request creates a new request ID. `attempt_id` hashes retry key, epoch, attempt ordinal, and collection run ID. `fingerprint` hashes category, stable code, and phase; volatile paths, timestamps, and remote prose are excluded. Codes are ASCII slugs of at most 100 bytes.

Transient codes are limited to reviewed network and infrastructure classes such as `network-timeout`, `dns-failure`, `github-rate-limit`, `remote-5xx`, and `git-interrupted`. Deterministic-policy codes include `invalid-registry`, `unsupported-workspace`, `ambiguous-package`, `missing-required-root`, `unsafe-required-file`, `capsule-budget-exceeded`, and `packet-budget-exceeded`. Unmapped exceptions use category `unknown` and a bounded exception-class code. A nonterminal publication journal is recovered before its selector can consume another retry attempt.

The reducer processes valid events in file order under the repository collection lock. Epoch starts at one. Within an epoch, attempt ordinals count executions of the retry unit and must increase by exactly one regardless of fingerprint or failing phase. A changed failure does not reset the retry budget. Deterministic-policy failures immediately produce `needs-policy-review`. Transient and unknown failures produce:

| Attempt | Meaning | Outcome | Delay |
| ---: | --- | --- | ---: |
| 1 | initial failure | `retry-pending` | 15 minutes |
| 2 | retry 1 failed | `retry-pending` | 2 hours |
| 3 | retry 2 failed | `retry-pending` | 24 hours |
| 4 | retry 3 failed | `quarantined` | none |

No in-process daemon is added. The only retry scheduler command is `retry-due [--repo <id>]`. It reduces the log, selects each due `retry_key` once, and dispatches the exact operation, selector, and unit ID from that key. A normal scheduled command that encounters the same key applies the same due-state gate. Not-due, quarantined, and policy-review keys are reported and skipped. Work units are deduplicated before dispatch; the repository lock and a second state check after lock acquisition prevent concurrent duplicate attempts.

Successful retry appends exactly:

```json
{
  "event_version": 1,
  "event": "attempt-succeeded",
  "attempt_id": "<64-hex>",
  "retry_key": "<64-hex>",
  "repo_id": "paypal/paypal-js",
  "operation": "capsule",
  "selector": "<stable-selector>",
  "unit_id": "<capsule-id:policy-hash>",
  "resolved_sha": "<sha-or-empty>",
  "policy_hash": "<hash-or-empty>",
  "epoch": 1,
  "attempt": 2,
  "observed_at": "<UTC-RFC3339>"
}
```

Explicit reset appends exactly:

```json
{
  "event_version": 1,
  "event": "retry-reset",
  "reset_id": "<64-hex>",
  "retry_key": "<64-hex>",
  "repo_id": "paypal/paypal-js",
  "operation": "capsule",
  "selector": "<stable-selector>",
  "unit_id": "<capsule-id:policy-hash>",
  "new_epoch": 2,
  "actor": "<bounded-ASCII-identity>",
  "reason": "<bounded-ASCII-reason>",
  "observed_at": "<UTC-RFC3339>"
}
```

An `attempt-succeeded` event is written only when the key is currently `retry-pending`, including reset-ready state. Its epoch must match current epoch and its attempt is the next execution ordinal; it clears the active retry state. A success with no prior retry state needs no retry-log event because the collection terminal event is authoritative.

`retry-reset` is valid only for a known `retry-pending`, `needs-policy-review`, or `quarantined` key. It requires explicit `--actor` and `--reason`; both are at most 200 ASCII bytes. `new_epoch` must equal the prior epoch plus one. Reset projects the key to `retry-pending` with `next_retry_at = observed_at` and the next execution ordinal equal to one. Earlier epochs remain immutable history and do not count toward the new four-attempt bound. `reset_id` hashes retry key, new epoch, actor, reason, and collection run ID.

Failure-log appends use one write plus file `fsync` while the collection lock is held. Duplicate attempt or reset IDs are invalid, and retry commands check for an existing ID before append. Logs never contain credentials or unbounded exception text.

The failure-log parser rejects unknown fields, duplicate JSON keys, invalid timestamps, epoch or attempt gaps, retry-key/hash disagreement, unit IDs inconsistent with their operation, outcomes inconsistent with category or attempt number, success without a currently retryable key, and reset events for unknown keys.

The status reducer projects `retry-pending`, `needs-policy-review`, and `quarantined` once per retry key into generated JSON and Markdown. These states are never reported as unchanged or collected, and they block ingest eligibility only for the affected operation unit and version until resolved.

## Versioned Secret Detector Contract

Every blob selected for an npm capsule or deep dive is scanned by the standard-library suite `text-secrets-v1` after size, strict UTF-8, and NUL validation and before staging. The scanner reads the complete decoded blob without Unicode or newline normalization and applies Python `re` patterns with `re.ASCII`; multiline behavior is enabled only where shown. It does not scan rejected binary or oversized content because those files already fail collection.

The suite contains exactly these detector codes and expressions:

| Detector code | Python regular expression |
| --- | --- |
| `pem-private-key-header-v1` | `(?m)^-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----[ \t]*\r?$` |
| `aws-access-key-id-v1` | `(?<![A-Z0-9])(?:AKIA|ASIA)[A-Z0-9]{16}(?![A-Z0-9])` |
| `github-token-v1` | `(?<![A-Za-z0-9_])(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{36,255}(?![A-Za-z0-9])` |

Changing a pattern, flag, detector set, decoding rule, or maximum supported input requires a new suite name. Unit fixtures construct exact positive vectors from fragments to avoid committing token-shaped strings: `"-----BEGIN " + "PRIVATE KEY-----"`, `"AKIA" + "A" * 16`, and `"ghp_" + "A" * 36`. Exact negative vectors are the corresponding values with the final character removed, each value embedded within an ASCII alphanumeric token, ordinary words `client_secret`, and a public-key header. Tests also cover CRLF, matches at both file boundaries, multiple detector matches, and one allowlisted finding alongside one non-allowlisted finding.

Every finding is `(path, git_blob_oid, detector_code)`. All findings must be allowlisted independently by the exact immutable triple before promotion. Reports contain only that triple, the file SHA-256, and suite name; they never contain the matched text or byte offset. The manifest claim is only `scanned by text-secrets-v1`. The collector and wiki must never describe a scanned file or capsule as `secret-free`, because this bounded detector suite cannot prove absence of credentials.

## Query-Driven Deep Dive Safety

Query handling searches wiki pages and indexed raw evidence first. When saved evidence is insufficient, the operator identifies one exact version ID and SHA and creates a tracking request containing the question, requested paths, and selection reasons.

Requests live under `tracking/github/repos/<company>/<repo>/deep-dive-requests/<request-id>.json` and have exactly:

```json
{
  "format_version": 1,
  "request_id": "<64-hex>",
  "repo_id": "paypal/paypal-js",
  "version_id": "<64-hex>",
  "sha": "<full-sha>",
  "question": "<bounded-UTF-8-question>",
  "paths": [
    {"path": "packages/example/src/file.ts", "reason": "implementation"}
  ],
  "max_file_bytes": 512000,
  "max_packet_files": 160,
  "max_packet_utf8_bytes": 1000000,
  "secret_detector": "text-secrets-v1",
  "created_at": "<UTC-RFC3339>"
}
```

Allowed reasons are `implementation`, `type-definition`, `test-evidence`, and `configuration`. Paths are sorted unique safe repository-relative POSIX paths. The question is at most 2,000 UTF-8 bytes. `secret_detector` is required and must equal `text-secrets-v1`. `request_id` hashes every semantic field except itself and `created_at`. A request becomes immutable once a supplement references its hash; later changes fail validation rather than changing raw provenance.

The deep-dive collector:

- resolves paths only through the exact commit tree;
- accepts only tracked regular Git blobs with mode `100644` or `100755`;
- reads bytes with `git cat-file blob`, never by executing or importing repository files;
- rejects symlink mode `120000`, gitlink mode `160000`, untracked paths, unsafe paths, LFS pointer blobs, non-UTF-8 bytes, NUL bytes, and configured size-limit violations;
- never runs package installation, build, test, generator, hook, or repository script commands; and
- copies accepted bytes exactly without newline normalization.

An LFS pointer is any blob beginning with the exact ASCII line `version https://git-lfs.github.com/spec/v1`. Secret detection follows the versioned contract above. A flagged blob blocks promotion. A false-positive exception requires stable registry allowlisting by repository path, exact Git blob object ID, and detector code; path-only allowlisting is invalid.

A successful deep dive creates a `query-deep-dive` supplement, attaches it only to the selected version ID, creates an independent v2 supplement packet, and leaves it awaiting review. Query-specific paths remain generated tracking input and do not become capsule registry policy.

`rules/query-and-synthesis.md` must be corrected to require this same-SHA supplement flow instead of updating accepted raw evidence.

## PayPal JS Migration

The 15 canonical snapshots and 15 existing release packets remain immutable. Migration does not replace or supersede them.

The rollout is:

1. run v1-to-v2 index migration in dry-run and report exact identity and capture mapping;
2. approve and publish the generated index plus its required `index-migrated-v2` run event as one index-only journal transaction;
3. audit all 15 SHAs with `npm-tracked-source-v1` without promotion;
4. stop if any required scope, generated-target classification, or budget fails;
5. report package closure, roots, files, bytes, exclusions, and artifact-correspondence status for every SHA;
6. use `main` as the isolated first supplement pilot because it has a baseline packet rather than a release-delta dependency;
7. after approval, publish the main capsule supplement and its independent packet;
8. validate index round trip, journal, raw evidence, packet, and retry state;
9. request approval before publishing the remaining 14 supplements and packets; and
10. start no ingest.

Because every capsule is an independent same-SHA packet, publishing later release capsules cannot make an earlier delta packet or capsule packet stale.

Before any PayPal JS packet is approved for ingest, perform a separate backlink and content review of the existing `paypal-js`, `paypal-js-v6`, and `react-paypal-js-v8` source identities. Collection does not decide that wiki consolidation.

## Validation And Testing

Deterministic Python 3.9-compatible tests must cover:

- strict nested TOML parsing with the repository's fallback parser;
- every capsule default, unknown key, path restriction, and policy hash rule;
- workspace list/object forms, supported globs, overlaps, root package, and rejected patterns;
- duplicate package names, malformed manifests, dependency cycles, local protocols, dependency-map precedence, exact `peerDependenciesMeta`, optional peers, and malformed peer metadata;
- tracked declaration roots, `types/`, wrappers, conditional exports, wildcard recording, explicit generated-root matches, unreviewed missing targets, and generated-root overlap failures;
- classification precedence and every allowed excluded category;
- complete format-3 file records, format-2 compatibility, exact Git object IDs and modes, executable blobs, symlinks, gitlinks, LFS pointers, and binary data;
- every `text-secrets-v1` positive and negative vector, boundary and CRLF behavior, multiple findings, exact-blob allowlisting, detector-version policy hashing, and rejection of `secret-free` output;
- raw-byte capsule and packet budget boundaries, including rendered manifests and packet Markdown;
- index-only v1-to-v2 migration publication and recovery, shared-SHA package identities, ambiguous legacy supplements, and byte-stable v2 round trips;
- bidirectional index-only capture/version evidence references, supplement revision ordering, and A-then-later-B shared-SHA attachment with an unchanged manifest hash;
- packet v1 compatibility, exact supplement-only packet-v2 invariants, and rejection of baseline, delta, or comparison packet-v2 values;
- supplement required-reading calculation and packet budget validation;
- unchanged packet state events and rejection of mixed packet versions;
- stable snapshot-root lock ordering, concurrent revision allocation without collision, and journal recovery after every durable file or parent-directory operation;
- exact run-path recovery, operation-specific artifact sets and terminal events, index-only and attachment-only transactions, multiple capsules for one selector, ownership mismatch, index hash mismatch, forward completion, rollback, and manual-recovery projection;
- retry persistence across restarts, one key across changing failure phases, due-key deduplication, injected clocks, lock-time recheck, success, reset epochs, four-attempt quarantine, and exact `retry-due` CLI dispatch;
- deep-dive untracked, traversal, symlink, gitlink, LFS, secret, and size failures;
- correction of the query-rule immutability conflict; and
- the exact PayPal graph of 15 canonical captures, 15 legacy packets, one main pilot supplement, and 14 later supplement packets.

Network-dependent PayPal verification remains outside the default unit suite. Passing existing tests alone does not approve migration; live dry-run evidence and deterministic validation are required.

## Acceptance Criteria

The design is implemented when:

- repository configuration can select `npm-tracked-source-v1` without company-specific code;
- PayPal JS includes complete declared tracked source for `@paypal/react-paypal-js` and internal `@paypal/paypal-js`, including tracked `types/` declarations;
- generated artifact correspondence is explicitly unverified rather than implied;
- no successful capsule silently omits required source or exceeds a full-reading budget;
- index v2 preserves shared-SHA version identities and every applicable supplement across save/reload;
- adding a later shared-SHA version changes only generated index and packet evidence, never the capsule manifest or raw capture;
- packet v2 represents same-SHA evidence additions without modifying existing packets or state history;
- format-3 manifests preserve exact Git object, mode, package, classification, policy, and detector provenance while format 2 remains readable;
- crash recovery converges after every durable publication step using a stable revision lock and exact journaled run path;
- retry and quarantine state persists once per executable scheduling unit across processes and scheduled runs;
- deep dives read only safe exact-SHA Git blobs and execute no repository code;
- deterministic tests and validators pass; and
- no collection, migration, recovery, or retry command starts wiki ingest.
