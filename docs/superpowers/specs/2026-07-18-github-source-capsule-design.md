# GitHub Tracked Source Capsule and Deep-Dive Design

**Status:** Revised after decline review; pending final user review
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
include_paths = []
excluded_categories = ["tests", "stories", "fixtures"]
max_file_bytes = 512000
max_capsule_files = 120
max_capsule_utf8_bytes = 750000
max_packet_files = 160
max_packet_utf8_bytes = 1000000

[[repos.capsules.package_overrides]]
name = "@paypal/paypal-js"
required_roots = ["src", "types"]
include_paths = []

[[repos.secret_allowlist]]
path = "path/to/reviewed-file.ts"
blob_sha = "<40-or-64-lowercase-hex>"
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
| `include_paths` | no | list of paths | Defaults to empty. Applied package-relative to every included package. |
| `excluded_categories` | no | list of enums | Defaults to `tests`, `stories`, and `fixtures`; only those values are accepted in v1. |
| `max_file_bytes` | no | integer | Defaults to 512,000; positive raw-byte limit for one file. |
| `max_capsule_files` | no | integer | Defaults to 120; positive count of saved upstream files. |
| `max_capsule_utf8_bytes` | no | integer | Defaults to 750,000; positive sum of saved upstream file bytes. |
| `max_packet_files` | no | integer | Defaults to 160; positive full-reading file count. |
| `max_packet_utf8_bytes` | no | integer | Defaults to 1,000,000; positive full-reading byte count. |
| `package_overrides` | no | list of tables | Defaults to empty; names must be unique within the capsule. |

Each package override has exactly `name`, `required_roots`, and `include_paths`. All are required. `required_roots` is non-empty. Unknown capsule or override keys fail registry loading.

For an overridden package, `required_roots` replaces `default_required_roots`; global and override `include_paths` are combined and deduplicated. A package in the resolved closure without an override uses the defaults.

`secret_allowlist` is an optional repository-level array. Each row has exactly `path`, `blob_sha`, and `detector_code`; all are required. Paths follow the same safe repository-relative rules, blob hashes must be lowercase Git object IDs, and duplicate triples fail. An allowlist row applies only to that exact immutable blob and detector finding. It is included in the effective collection policy hash.

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

`devDependencies` never extend the closure. Dependency maps must contain string names and string specifications. If a dependency name matches a workspace package, v1 includes that package regardless of npm range syntax and records the declared specification and local package version. V1 does not claim npm semver-range compatibility.

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
- A target under absent generated output such as `dist/` is recorded as `generated-target-not-tracked`.
- Other missing, escaping, symlink, or unsafe declared targets fail.
- Generated targets are not mapped back to source without executing the build or parsing build configuration.

The manifest therefore reports three independent statements:

```text
Tracked source scope completeness: complete
Published artifact correspondence: unverified-generated-targets
Repository completeness: intentionally incomplete
```

`Tracked source scope completeness: complete` is valid only when every required file after category classification is saved and validated. The capsule does not claim that generated `dist` files match captured source or that all repository behavior is covered.

## Capsule Snapshot Manifest

Existing snapshot manifest format 2 remains valid. A capsule supplement uses format 3, preserves all existing repository, ref, SHA, file hash, exclusion, capture-kind, revision, date, and release-evidence fields, and adds exactly `capture_purpose`, `canonical_snapshot`, and `capsule`.

`capture_purpose` is `source-capsule`, `policy-upgrade`, or `query-deep-dive`. `canonical_snapshot` is the repository-relative path of the unique canonical capture at the same SHA.

The `capsule` object has exactly:

```json
{
  "adapter": "npm-tracked-source-v1",
  "capsule_id": "react-paypal-js-runtime",
  "policy_hash": "<64-hex>",
  "version_ids": ["<64-hex>"],
  "focus_packages": ["@paypal/react-paypal-js"],
  "included_packages": [],
  "dependency_edges": [],
  "external_dependencies": [],
  "required_roots": [],
  "include_paths": [],
  "excluded_categories": ["fixtures", "stories", "tests"],
  "declared_targets": [],
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
- `include_paths`: `{package, path, source}`, where source is `capsule-policy`, `package-override`, or `declared-target`;
- `declared_targets`: `{package, field, export_key, condition, target, status}`, where empty strings represent inapplicable export key or condition and status is `tracked-required`, `generated-target-not-tracked`, or `recorded-pattern`.

These arrays sort by package name and then POSIX path or target; dependency arrays additionally sort by kind and destination name. The design does not permit free-form summary strings in these records. Every manifest `files` entry names its package and classification reason. Validators recompute the package closure, required-file set, policy hash, completeness fields, and file hashes from the exact Git tree before promotion. Index adapter, capsule ID, policy hash, focus packages, version IDs, SHA, canonical path, kind, and revision must match the immutable manifest exactly.

Query deep dives use the same format with adapter `explicit-git-blobs-v1`. Their `capsule` object instead has exactly `adapter`, `capsule_id`, `policy_hash`, `version_ids`, `request_id`, `request_hash`, `question_hash`, `paths`, `tracked_source_scope_completeness`, and `repository_completeness`. `paths` is the sorted exact `{path, reason}` list from the request. Completeness must be `complete-for-requested-paths`; repository completeness remains `intentionally-incomplete`. The immutable raw manifest does not duplicate the full question text.

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

Every snapshot path must resolve to an immutable manifest whose repository, SHA, kind, and revision exactly match the capture record. A canonical capture applies to every version identity at its SHA. A supplement applies only to the explicit version IDs listed in both the capture record and those versions' `evidence_ids`.

Within one repository, `(sha, adapter, capsule_id, policy_hash)` identifies at most one source-capsule capture. `focus_packages` and `applies_to_version_ids` are sorted unique lists. A later release identity sharing the SHA may attach that existing capture through a new index transaction and independent supplement packet; it does not create duplicate raw evidence.

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

Dry-run writes no generated state. Approved migration stages a complete v2 index, validates a save/reload round trip, and publishes it through the recoverable transaction protocol below. V1 is never rewritten implicitly. Loading v2 and saving it without semantic changes must be byte-identical.

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

V2 permits `baseline`, `delta`, `comparison`, and `supplement`, although this feature initially produces only supplement packets. For a supplement packet:

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
├── staged-packet/        # present until packet publication
└── COMMITTED
```

The transaction ID is a 64-character lowercase SHA-256 over repository ID, operation, exact SHA or empty string, policy hash or empty string, selected version ID or empty string, capsule ID or empty string, collection run ID, and attempt ordinal. This makes retries distinct while leaving each interrupted attempt recoverable by its journal. The repository `.collection.lock` is acquired first and held through recovery or publication. Nested lock order is always:

```text
collection lock -> snapshot promotion locks sorted by final path -> packet lock
```

No mutating code path may acquire these locks in reverse order. Packet lifecycle transitions also acquire the repository collection lock before the packet lock and recover or block on any unfinished journal before reading packet state. This prevents approval of a packet published by an uncommitted transaction.

The transaction coordinator owns these descriptors. Snapshot and packet publication gain internal variants that accept already-open, already-locked parent descriptors; they must not reacquire the same lock through another descriptor. Public single-artifact helpers retain their current lock-owning behavior outside a journal transaction.

Before publication, the collector:

1. recovers every nonterminal transaction for the repository;
2. preflights packet lifecycle and index expectations;
3. acquires required snapshot promotion locks in sorted final-path order and the packet lock, retaining them through commit or rollback;
4. allocates final supplement revisions while those locks are held;
5. stages and validates all raw manifests and files;
6. stages the exact packet directory and both budget calculations;
7. writes exact prior and intended index bytes;
8. appends and `fsync`s a `prepared` journal event containing paths and SHA-256 hashes; and
9. `fsync`s the transaction directory.

Publication then:

1. promotes each owned immutable snapshot and journals its path, device, inode, and content hash;
2. publishes each owned packet directory and journals the same ownership data;
3. atomically replaces the index with `after-index.json` and journals the resulting hash;
4. appends and `fsync`s the intended terminal collection event, keyed by transaction ID;
5. writes and `fsync`s `COMMITTED`; and
6. releases locks.

Every journal event is one compact JSON object, appended with one write and `fsync`. Events have monotonically increasing `sequence`, exact operation names, and no free-form secret content. The prepared journal stores the exact intended terminal collection event. Run-event validation permits exactly one terminal event per transaction ID, so recovery can append a missing event without duplication.

A directory content hash is SHA-256 over canonical JSON listing every relative path, Git-style mode, byte size, and file SHA-256 in sorted path order. Ownership journal events store this hash together with device and inode.

Successful capsule publication uses this exact terminal run event:

```json
{
  "event_version": 2,
  "transaction_id": "<64-hex>",
  "dry_run": false,
  "repo_id": "paypal/paypal-js",
  "selector": "<stable-selector>",
  "state": "collected-supplement",
  "ref_name": "<resolved-ref>",
  "sha": "<full-sha>",
  "version": "<resolved-version>",
  "packet_id": "<packet-id>"
}
```

`collected-supplement` is added to collection terminal states. Existing event schemas remain accepted for existing runs. Event-v2 validation rejects unknown keys and requires `transaction_id` uniqueness within the repository run history.

Every journal event has required common fields `event_version = 1`, `transaction_id`, `sequence`, and `event`. Event-specific fields are exact:

| Event | Additional fields |
| --- | --- |
| `prepared` | `repo_id`, `operation`, `before_index_hash`, `after_index_hash`, `planned_artifacts`, `terminal_event`, `terminal_event_hash` |
| `artifact-published` | `artifact_kind`, `path`, `device`, `inode`, `content_hash` |
| `index-published` | `after_index_hash` |
| `terminal-event-published` | `run_path`, `terminal_event_hash` |
| `rolled-back` | `reason_code` |
| `recovery-required` | `reason_code`, `observed_index_hash` |

`planned_artifacts` is a sorted list of exact repository-relative final paths, artifact kinds, and expected content hashes. Journal parsing rejects unknown fields, duplicate sequences, sequence gaps, events invalid for the current phase, and hashes that disagree with staged bytes. `COMMITTED` is a zero-byte regular file created with exclusive no-follow semantics and then directory-`fsync`ed.

Recovery under the collection lock follows these rules:

- before index publication, verify ownership tokens, remove only transaction-owned snapshots and packets, restore no index, and append `rolled-back`;
- after index publication but before terminal-event publication, complete forward when every artifact matches, or atomically restore `before-index.json` and remove only verified owned artifacts when an artifact is missing;
- terminal-event publication is the irreversible forward-only boundary; recovery detects it by transaction ID even if the corresponding journal event was not appended before the crash;
- after that boundary, intact artifacts and index complete forward by writing `COMMITTED`, while any mismatch becomes `recovery-required` rather than rollback;
- if an existing artifact's device, inode, or content hash differs from the journal, mark `recovery-required` without deleting or rewriting it;
- if the current index matches neither recorded hash, mark `recovery-required`, block further collection, and require manual review; and
- never delete or rewrite an artifact without matching repository namespace, path, device, inode, and expected hash.

Read-only validation reports nonterminal or `recovery-required` journals but does not mutate them. Collection and explicit `recover` perform recovery. Crash tests interrupt after every durable write.

Packet directory hashes in a committed journal describe publication-time bytes with the initial state event. Later valid packet-state appends intentionally change that directory, so completed-journal validation does not compare the current packet tree to its publication hash. Nonterminal recovery can compare it because the packet lock prevents lifecycle transitions until commit.

## Normal Capsule Collection

For each selected release or branch with capsule policy:

1. resolve the exact version identity and SHA;
2. require or explicitly migrate version index v2;
3. check for an existing capture with the same SHA, capsule ID, adapter, and policy hash;
4. inspect exact Git objects and resolve package scope;
5. stage a `source-capsule` supplement using adapter `npm-tracked-source-v1` and a v2 supplement packet;
6. run snapshot, evidence attachment, UTF-8, and packet-budget validation;
7. publish through the recoverable journal;
8. leave the supplement packet `awaiting-review`; and
9. emit one reconciled terminal collection event.

Same SHA, capsule ID, policy hash, and already-attached version ID is `unchanged`. If the capture exists but is not attached to a newly discovered version identity sharing that SHA, the collector reuses the raw capture, updates bidirectional index references, and creates a supplement packet for that version. A changed policy hash creates a new `policy-upgrade` supplement; it never edits the earlier capsule. Collection may process multiple refs but obtains one repository lock and transaction at a time. It never approves or ingests packets.

The public CLI additions are:

```text
collect --repo <id> --capsules [--dry-run]
migrate-index-v2 --repo <id> [--dry-run]
deep-dive --repo <id> --request <tracking-json-path> [--dry-run]
recover --repo <id>
retry-due [--repo <id>]
retry-reset --repo <id> --selector <selector> --actor <id> --reason <text>
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
  "attempt_key": "<64-hex>",
  "repo_id": "paypal/paypal-js",
  "selector": "<stable-selector>",
  "resolved_sha": "<sha-or-empty>",
  "policy_hash": "<hash-or-empty>",
  "phase": "resolve|inspect|stage|publish|recover",
  "category": "transient|deterministic-policy|unknown",
  "code": "<bounded-stable-error-code>",
  "fingerprint": "<64-hex>",
  "attempt": 1,
  "outcome": "retry-pending|needs-policy-review|quarantined",
  "observed_at": "<UTC-RFC3339>",
  "next_retry_at": "<UTC-RFC3339-or-empty>"
}
```

`attempt_key` hashes repository ID, selector, resolved SHA or empty string, policy hash or empty string, and phase. `attempt_id` hashes attempt key, attempt number, and collection run ID. `fingerprint` hashes category, stable code, and phase; volatile paths, timestamps, and remote prose are excluded. Codes are ASCII slugs of at most 100 bytes.

Transient codes are limited to reviewed network and infrastructure classes such as `network-timeout`, `dns-failure`, `github-rate-limit`, `remote-5xx`, and `git-interrupted`. Deterministic-policy codes include `invalid-registry`, `unsupported-workspace`, `ambiguous-package`, `missing-required-root`, `unsafe-required-file`, `capsule-budget-exceeded`, and `packet-budget-exceeded`. Unmapped exceptions use category `unknown` and a bounded exception-class code. A nonterminal publication journal is recovered before its selector can consume another retry attempt.

The reducer processes valid events in file order under the repository collection lock. Attempt numbers must equal the prior consecutive same-fingerprint count plus one. A changed fingerprint begins at one. Deterministic-policy failures immediately produce `needs-policy-review`. Transient and unknown failures produce:

| Attempt | Meaning | Outcome | Delay |
| ---: | --- | --- | ---: |
| 1 | initial failure | `retry-pending` | 15 minutes |
| 2 | retry 1 failed | `retry-pending` | 2 hours |
| 3 | retry 2 failed | `retry-pending` | 24 hours |
| 4 | retry 3 failed | `quarantined` | none |

No in-process daemon is added. An external scheduler invokes `collect --retry-due`; normal scheduled collection may invoke the same selector. The command selects only keys whose `next_retry_at` is due according to its injected clock. Not-due, quarantined, and policy-review keys are reported and skipped. The repository lock prevents concurrent duplicate attempts.

Successful retry appends exactly:

```json
{
  "event_version": 1,
  "event": "attempt-succeeded",
  "attempt_id": "<64-hex>",
  "attempt_key": "<64-hex>",
  "repo_id": "paypal/paypal-js",
  "selector": "<stable-selector>",
  "resolved_sha": "<sha-or-empty>",
  "policy_hash": "<hash-or-empty>",
  "phase": "resolve|inspect|stage|publish|recover",
  "fingerprint": "<64-hex>",
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
  "attempt_key": "<64-hex>",
  "repo_id": "paypal/paypal-js",
  "selector": "<stable-selector>",
  "actor": "<bounded-ASCII-identity>",
  "reason": "<bounded-ASCII-reason>",
  "observed_at": "<UTC-RFC3339>"
}
```

`retry-reset` requires explicit `--actor` and `--reason`; both are at most 200 ASCII bytes. `reset_id` hashes attempt key, actor, reason, and collection run ID. Failure-log appends use one write plus file `fsync` while the collection lock is held. Duplicate attempt or reset IDs are invalid, and retry commands check for an existing ID before append. A changed SHA or policy hash naturally creates a new attempt key. Logs never contain credentials or unbounded exception text.

The failure-log parser rejects unknown fields, duplicate JSON keys, invalid timestamps, attempt gaps, outcomes inconsistent with category or attempt number, success without a currently retryable key, and reset events for unknown keys.

The status reducer projects `retry-pending`, `needs-policy-review`, and `quarantined` into generated JSON and Markdown. These states are never reported as unchanged or collected, and they block capsule ingest eligibility for the affected version until resolved.

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
  "created_at": "<UTC-RFC3339>"
}
```

Allowed reasons are `implementation`, `type-definition`, `test-evidence`, and `configuration`. Paths are sorted unique safe repository-relative POSIX paths. The question is at most 2,000 UTF-8 bytes. `request_id` hashes every semantic field except itself and `created_at`. A request becomes immutable once a supplement references its hash; later changes fail validation rather than changing raw provenance.

The deep-dive collector:

- resolves paths only through the exact commit tree;
- accepts only tracked regular Git blobs with mode `100644` or `100755`;
- reads bytes with `git cat-file blob`, never by executing or importing repository files;
- rejects symlink mode `120000`, gitlink mode `160000`, untracked paths, unsafe paths, LFS pointer blobs, non-UTF-8 bytes, NUL bytes, and configured size-limit violations;
- never runs package installation, build, test, generator, hook, or repository script commands; and
- copies accepted bytes exactly without newline normalization.

An LFS pointer is any blob beginning with the exact ASCII line `version https://git-lfs.github.com/spec/v1`. Secret detection runs before staging. A flagged blob blocks promotion and reports only path, blob ID, detector code, and hashes. It never prints or silently redacts the suspected value. A false-positive exception requires stable registry allowlisting by repository path, exact blob SHA, and detector code; path-only allowlisting is invalid.

A successful deep dive creates a `query-deep-dive` supplement, attaches it only to the selected version ID, creates an independent v2 supplement packet, and leaves it awaiting review. Query-specific paths remain generated tracking input and do not become capsule registry policy.

`rules/query-and-synthesis.md` must be corrected to require this same-SHA supplement flow instead of updating accepted raw evidence.

## PayPal JS Migration

The 15 canonical snapshots and 15 existing release packets remain immutable. Migration does not replace or supersede them.

The rollout is:

1. run v1-to-v2 index migration in dry-run and report exact identity and capture mapping;
2. approve and publish only the generated index migration;
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
- duplicate package names, malformed manifests, dependency cycles, optional peers, and local protocols;
- tracked declaration roots, `types/`, wrappers, conditional exports, wildcard recording, and generated targets;
- classification precedence and every allowed excluded category;
- exact Git blob reading, executable blobs, symlinks, gitlinks, LFS pointers, binary data, and secrets;
- raw-byte capsule and packet budget boundaries, including rendered manifests and packet Markdown;
- v1-to-v2 migration, shared-SHA package identities, ambiguous legacy supplements, and byte-stable v2 round trips;
- bidirectional capture/version evidence references and supplement revision ordering;
- packet v1 compatibility and exact packet v2 same-SHA invariants;
- supplement required-reading calculation and packet budget validation;
- unchanged packet state events and rejection of mixed packet versions;
- lock ordering and journal recovery after every durable write;
- ownership mismatch, index hash mismatch, forward completion, rollback, and manual-recovery projection;
- retry persistence across restarts, due-time selection, injected clocks, concurrency, success, reset, and quarantine;
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
- packet v2 represents same-SHA evidence additions without modifying existing packets or state history;
- crash recovery converges after every durable publication step;
- retry and quarantine state persists across processes and scheduled runs;
- deep dives read only safe exact-SHA Git blobs and execute no repository code;
- deterministic tests and validators pass; and
- no collection, migration, recovery, or retry command starts wiki ingest.
