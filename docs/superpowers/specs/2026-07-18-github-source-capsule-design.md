# GitHub Tracked Source Capsule and Deep-Dive Design

**Status:** Revised after third decline review; pending final user review
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

## Generic Capsule Evidence Contract

This section is normative for every registered repository supported by an adapter. Company and repository names appear only as examples or conformance fixtures. Implementations derive behavior from adapter contracts and `tracking/github/repo-registry.toml`; they must not branch on PayPal, Stripe, Adyen, or any other company or repository ID.

### Normative Registry Schema

`capsules` becomes an optional array on a repository row. Unknown keys remain errors.

```toml
[[repos.capsules]]
id = "react-paypal-js-runtime"
adapter = "npm-tracked-source-v1"
focus_packages = ["@paypal/react-paypal-js"]
dependency_scope = "internal-runtime-closure"
default_required_roots = ["src"]
default_generated_target_paths = ["dist/", "index.js"]
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
generated_target_paths = ["dist/", "index.js"]
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
| `focus_packages` | yes | list of strings | Non-empty, unique package names accepted by the capsule package-name grammar below. |
| `dependency_scope` | no | string | Defaults to and may only equal `internal-runtime-closure`. |
| `default_required_roots` | no | list of paths | Defaults to `["src"]`. Package-relative POSIX paths. |
| `default_generated_target_paths` | no | list of paths | Defaults to empty. Explicit package-relative generated files or directory prefixes. |
| `include_paths` | no | list of paths | Defaults to empty. Applied package-relative to every included package. |
| `excluded_categories` | no | list of enums | Defaults to `tests`, `stories`, and `fixtures`; only those values are accepted in v1. |
| `secret_detector` | no | string | Defaults to and may only equal `text-secrets-v1`. |
| `max_file_bytes` | no | integer | Defaults to 512,000; positive raw-byte limit for one file. |
| `max_capsule_files` | no | integer | Defaults to 120; positive count of saved upstream files. |
| `max_capsule_utf8_bytes` | no | integer | Defaults to 750,000; positive sum of saved upstream file bytes. |
| `max_packet_files` | no | integer | Defaults to 160; positive full-reading file count. |
| `max_packet_utf8_bytes` | no | integer | Defaults to 1,000,000; positive full-reading byte count. |
| `package_overrides` | no | list of tables | Defaults to empty; names must be unique within the capsule. |

Each package override has exactly `name`, `required_roots`, `generated_target_paths`, and `include_paths`. All are required. `required_roots` is non-empty; `generated_target_paths` and `include_paths` may be empty. Unknown capsule or override keys fail registry loading.

For an overridden package, `required_roots` and `generated_target_paths` replace their corresponding defaults; global and override `include_paths` are combined and deduplicated. A package in the resolved closure without an override uses the defaults. A generated target ending in exactly one `/` is a directory prefix; that marker is stripped before safe-path validation. Every other value is one exact file. Empty directory values and repeated trailing slashes fail. Values otherwise use the same safe package-relative path rules, and a generated file or directory may not overlap a required root or include path. Matching is literal, case-sensitive, and segment-aware; no generated-target value is a glob.

The capsule package-name grammar is deliberately separate from release-tag parsing and is named `npm-package-name-v1`. A name is lowercase ASCII, URL-safe, and at most 214 bytes. An unscoped name matches `[a-z0-9][a-z0-9._~-]*`. A scoped name has exactly one `/`; its scope matches `@[a-z0-9][a-z0-9._~-]*`, while its package component matches `[a-z0-9._~-]+`. The scoped package component may therefore begin with `.` or `_`, as npm permits, but the scope and an unscoped package may not. Empty components, uppercase letters, percent escapes, whitespace, additional slashes, and release suffixes such as `@1.2.3` fail registry loading. Both scoped and unscoped names are supported. Fixtures include `@scope/.pkg`, `@scope/_pkg`, rejected `@.scope/pkg`, rejected `@_scope/pkg`, and rejected unscoped `.pkg` and `_pkg`.

`secret_allowlist` is an optional repository-level array. Each row has exactly `path`, `blob_oid`, and `detector_code`; all are required. Paths follow the same safe repository-relative rules, object IDs must be 40 or 64 lowercase hexadecimal characters, and duplicate triples fail. An allowlist row applies only to that exact immutable blob and detector finding. It is included in the effective collection policy hash.

All policy paths reject absolute paths, empty values, `.` or `..` segments, and backslashes. Capsule roots, includes, overrides, and generated targets are package-relative and cannot escape their owning package directory. Secret allowlist paths are repository-relative and cannot escape the repository. V1 policy paths are literal paths, not globs. Exclusions use adapter-owned category classifiers rather than arbitrary registry globs, preventing a repository policy from silently excluding production source.

The effective policy is the adapter version, all versioned defaults, and normalized repository values. Only allowlist rows whose `(path, blob_oid)` identify a selected candidate blob and whose `detector_code` belongs to the selected detector suite are applicable and participate; unrelated allowlist rows do not change a capture's policy. It is serialized as compact canonical JSON with sorted object keys. The exact array canonicalization rules are:

| Array | Canonical order |
| --- | --- |
| `focus_packages`, `default_required_roots`, `default_generated_target_paths`, `include_paths`, `excluded_categories` | unique Unicode-code-point lexical order |
| `package_overrides` | package name; each nested path array uses lexical order |
| applicable `secret_allowlist` | `(path, blob_oid, detector_code)` |
| resolved `included_packages` | `(name, path, version, reason)` |
| `dependency_edges` | `(from_package, to_package, dependency_kind, specification, optional)` |
| `external_dependencies` | `(from_package, name, dependency_kind, specification, optional)` |
| resolved roots, generated targets, and includes | every field in schema order |
| `declared_targets` | `(package, field, json_pointer, condition_chain, array_indices, target)`; the two nested arrays retain traversal order |
| every `matched_paths` | unique POSIX lexical order |
| request `paths` | `(path, reason)` |
| capture `applies_to_version_ids` | unique lowercase-hex lexical order |
| detector findings | `(path, git_blob_oid, detector_code)` |
| format-3 `files` and `excluded` | `(path)` and `(path, reason)` respectively |
| aliases | unique lexical order |
| `planned_artifacts` | `(artifact_kind, path, staged_device, staged_inode, content_hash)` |
| packet `from.evidence_ids`, `to.evidence_ids`, `added_evidence_ids`, and `required_reading` | preserve the semantic orders defined by packet contract v2; never resort lexically |

No other array may be hashed until this specification assigns it either a sort key or an explicit order-preserving semantic. Duplicate rows are rejected after normalization unless the field explicitly says it deduplicates. Compact serialization uses UTF-8, separators `,` and `:`, `ensure_ascii = false`, no insignificant whitespace, and no trailing newline. Its SHA-256 is the `policy_hash`. TOML formatting and key order do not affect the hash.

The registry continues to contain stable intent only. Resolved paths, SHAs, attempts, collection dates, policy results, and progress remain generated state.

### Standard-Library NPM Workspace Resolution

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

### Required File Classification

The adapter reads the exact commit tree with `git ls-tree -rz` and reads blobs with `git cat-file blob`. It does not trust or execute working-tree files.

For each included package, classification uses this precedence:

1. Unsafe paths, symlinks, gitlinks, non-blobs, LFS pointers, non-UTF-8 content, NUL-containing content, and oversized files fail if selected by any required rule.
2. `package.json`, literal `include_paths`, every tracked declared entrypoint selected below, and tracked type declaration targets are required. A configured exclusion cannot remove them.
3. Files recognized by an enabled excluded category are outside capsule scope.
4. Every remaining regular tracked UTF-8 file below a required root is required.
5. Documentation and examples outside required roots remain optional existing snapshot evidence and are not part of capsule completeness.

Category classifiers are fixed in adapter v1:

- `tests`: filenames containing `.test.` or `.spec.`, and path segments `test`, `tests`, `__tests__`, or `bundle-tests`;
- `stories`: filenames containing `.stories.` and path segments `.storybook`, `storybook`, or `stories`; and
- `fixtures`: path segments `fixture`, `fixtures`, `__fixtures__`, or `snapshots`.

Changing these classifiers requires a new adapter version.

The adapter records `exports`, conditional exports, wildcard export values, `main`, `module`, `types`, `typings`, `bin`, and `files` declarations. `main`, `module`, `types`, and `typings` must be strings when present. `bin` may be one string or an object with string keys and values. `files` is recorded but does not reduce required source. Package-relative `main`, `module`, `types`, `typings`, and `bin` targets may have one leading `./`, which is stripped before safe-path validation. Every `exports` target string must begin with exactly `./`; targets beginning `../`, `/`, or a package name fail. After that prefix is removed, no target may contain an empty, `.`, `..`, or `node_modules` segment.

`exports` is traversed without resolving for one runtime condition set: its purpose is to retain every statically enumerable public target. It recursively accepts strings, `null`, arrays, subpath-key objects, and condition-key objects. Root string, `null`, array, or condition-object sugar is treated as export key `.`. A subpath key is exactly `.` or begins `./`; after that prefix, it must be non-empty, use `/` separators, not end in `/`, and contain no empty, `.`, `..`, `node_modules`, backslash, percent-encoded slash, or percent-encoded backslash segment. It is either literal with no `*` or a supported pattern with exactly one `*`. A condition key is a non-empty string that does not begin `.`. Mixed subpath and condition keys at one object level, unsafe subpath keys, duplicate subpaths after normalization, and numeric or empty keys are invalid. Duplicate JSON keys fail, but object insertion order is retained because condition order is semantic. Arrays retain fallback order. Every visited node records an RFC 6901 JSON Pointer with `~` escaped as `~0` and `/` as `~1`, the ordered condition-key chain, and the ordered array-index chain. A `null` leaf is a deliberate blocked export, records status `blocked-export`, and selects no file. Unsupported scalar leaves and structurally invalid forms are `needs-policy-review`.

- A tracked `types` or export `types` target is required. Because declaration files can reference sibling declarations, the complete tracked top-level declaration directory containing that target is required. This captures PayPal's tracked `types/` tree.
- Every tracked literal target reached through `main`, `module`, `bin`, or any recursively visited `exports` string is required. This includes runtime and type conditions; the adapter does not discard an unfamiliar condition name.
- A declared export pattern contains exactly one `*` in its subpath key and exactly one `*` in its target. In Node's direct-replacement semantics the substitution may contain `/`. The adapter statically enumerates it without executing Node: it matches the target as a recursive path pattern against the complete sorted set of regular tracked package blobs, derives each substitution, substitutes that same text into the export key, and requires every remaining target match. Node's most-specific subpath-pattern precedence is applied before condition traversal. A `null` at a subpath-map leaf blocks that concrete subpath across descendant conditions; a `null` inside a condition or array blocks only that recorded condition and fallback chain, so another public branch can still select its file. `**`, braces, character classes, multiple stars, and patterns that cannot be enumerated by this rule are `needs-policy-review`.
- A missing literal target is `generated-target-not-tracked` only when it exactly equals a reviewed generated file or is below a reviewed generated directory. A wildcard with no tracked match is `generated-pattern-not-tracked` only when its fixed path prefix is below a reviewed generated directory. The manifest records the matching generated-target policy value.
- A missing target or unmatched pattern with no exact reviewed generated policy is `needs-policy-review`; the adapter never infers generated output from names such as `dist`, `build`, `lib`, or `index.js`.
- Other escaping, symlink, or unsafe declared targets fail.
- Generated targets are not mapped back to source without executing the build or parsing build configuration.

The manifest therefore reports three independent statements:

```text
Tracked source scope completeness: complete
Published artifact correspondence: unverified-generated-targets
Repository completeness: intentionally incomplete
```

`Tracked source scope completeness: complete` is valid only when every required file after category classification is saved and validated. The capsule does not claim that declared generated targets match captured source or that all repository behavior is covered. A generated-target declaration is an operator-reviewed classification, not proof of artifact provenance.

### Capsule Snapshot Manifest

Existing snapshot manifest formats 1 and 2 remain valid and retain their exact parsers. A supplement uses format 3. Its exact top-level key set is `format_version`, `repository`, `ref`, `capture_kind`, `capture_revision`, `collection_date`, `prior_snapshot`, `files`, `excluded`, `release_notes`, `release_evidence`, `capture_purpose`, `canonical_snapshot`, `effective_policy`, and `capsule`. Only `repository` retains its exact format-2 schema. Format 3 deliberately does not inherit format-2 release identity fields. Unknown or missing keys fail. Format-1 and format-2 records are not retroactively changed.

The format-3 `ref` object is commit-only and has exactly:

```json
{
  "kind": "commit",
  "name": "commit:<full-sha>",
  "sha": "<full-sha>",
  "version": "",
  "aliases": [],
  "upstream_commit_time": "<UTC-RFC3339>",
  "release_published_at": null
}
```

`capture_kind` is `supplement`, `capture_revision` is a positive integer unique at the SHA, and both `prior_snapshot` and `canonical_snapshot` are exactly the version-neutral canonical capture ID `<sha>:c0`, never a filesystem path. The generated index resolves that ID to `snapshot_path`; immutable format-3 bytes do not copy a potentially release-named canonical path. `release_notes` is `null`, `release_evidence` is `[]`, and no initiating tag, package version, branch, version ID, alias, or release-derived path appears anywhere in immutable format-3 bytes. For an npm capsule, each `excluded` row has exactly `{path, reason}`, where `reason` is `excluded-category:<category>` and category is one enabled adapter category; rows sort by `(path, reason)`. For a deep dive, `excluded` is `[]`. `capture_purpose` is exactly `source-capsule`, `policy-upgrade`, or `query-deep-dive`.

A format-3 capture directory name is also version-neutral. An npm capture is `<collection-date>-source-capsule-<sha12>-<capsule-slug>-<policy12>-rN`; a deep dive is `<collection-date>-query-deep-dive-<sha12>-<request12>-rN`. `sha12`, `policy12`, and `request12` are the first 12 lowercase hexadecimal characters. `capsule-slug` lowercases ASCII, replaces each maximal run outside `[a-z0-9._-]` with `-`, trims leading and trailing `-`, falls back to `capsule`, and truncates to 40 bytes. The revision is allocated under the stable snapshot-root lock. No release label participates in path allocation or immutable capture identity.

`effective_policy` is the complete normalized policy object used for that capture. For `npm-tracked-source-v1`, it has exactly the registry capsule fields listed above plus normalized `package_overrides`, the applicable repository `secret_allowlist`, `category_classifier = "excluded-categories-v1"`, and `workspace_resolver = "npm-workspaces-v1"`. Defaults are materialized and every override and allowlist row uses its exact normative schema. For `explicit-git-blobs-v1`, it has exactly `adapter`, `max_file_bytes`, `max_packet_files`, `max_packet_utf8_bytes`, `secret_detector`, and the applicable normalized `secret_allowlist`. Canonicalization and hashing use the global table above. Historical validation uses this embedded object, not the current registry. A current-policy difference is reported as `current-policy-drift` work and never invalidates or recaptures committed historical evidence automatically.

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
  "generated_target_paths": [],
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

- `included_packages`: `{name, path, version, reason}`, where reason is `focus`, `internal-dependency`, `internal-optional-dependency`, or `internal-peer-dependency`;
- `dependency_edges`: `{from_package, to_package, dependency_kind, specification, optional}`, where kind is `dependency`, `optional-dependency`, or `peer-dependency`;
- `external_dependencies`: `{from_package, name, dependency_kind, specification, optional}`;
- `required_roots`: `{package, path, source}`, where source is `default`, `package-override`, or `tracked-declaration-target`;
- `generated_target_paths`: `{package, path, path_kind, source}`, where `path_kind` is `file` or `directory` and source is `default` or `package-override`;
- `include_paths`: `{package, path, source}`, where source is `capsule-policy`, `package-override`, or `declared-target`;
- `declared_targets`: `{package, field, json_pointer, condition_chain, array_indices, target, status, generated_policy_path, matched_paths}`, where `condition_chain` is the ordered list of condition keys, `array_indices` is the ordered list of fallback positions, empty arrays or strings represent inapplicable values, `matched_paths` is sorted unique, and status is `tracked-required`, `tracked-pattern-required`, `generated-target-not-tracked`, `generated-pattern-not-tracked`, or `blocked-export`; and
- `secret_scan`: exactly `{detector, scanned_blob_count}`. The detector is `text-secrets-v1`; the count is a non-negative integer and is recomputed from selected Git blobs.

These arrays use the exact canonical ordering table above. Export condition chains and fallback indices retain traversal order even though the enclosing declared-target records sort by their full semantic tuple. The design does not permit free-form summary strings in these records.

If more than one closure path reaches a package, its recorded reason uses precedence `focus`, `internal-dependency`, `internal-optional-dependency`, then `internal-peer-dependency`; all normalized dependency edges remain recorded. The name `internal-runtime-closure` is retained as a registry compatibility value, but it means the explicitly defined dependency, optional-dependency, and peer-dependency closure above rather than claiming every peer is installed runtime code.

Every format-3 `files` entry has exactly:

```json
{
  "path": "packages/example/src/index.ts",
  "sha256": "<64-lowercase-hex>",
  "size": 123,
  "purpose": "source-capsule",
  "git_blob_oid": "<40-or-64-lowercase-hex>",
  "git_mode": "100644",
  "package": "@scope/example",
  "classification_reason": "required-root"
}
```

The `files` array sorts uniquely by upstream POSIX `path`.

`path` is always the safe upstream repository-relative path, exactly as in format 2; evidence resolution prepends the snapshot's `files/` directory once. `sha256` is SHA-256 of the exact copied bytes, and `size` is their byte length. `purpose` is exactly `source-capsule` for the npm adapter or `query-deep-dive` for the explicit adapter. `git_blob_oid` is the exact object ID read by `git cat-file`; `git_mode` is exactly `100644` or `100755`. `package` is the owning resolved npm package for npm capsules and is the empty string for an explicit deep dive. Allowed npm classification reasons are `package-manifest`, `required-root`, `include-path`, `tracked-main-target`, `tracked-module-target`, `tracked-bin-target`, `tracked-export-target`, `tracked-export-pattern`, `tracked-types-target`, and `tracked-declaration-directory`. A deep-dive file uses `deep-dive-request`. When more than one rule selects a file, the first matching reason in that listed order is recorded. Unknown fields, modes, purposes, or reasons fail validation.

Before promotion, validators recompute the package closure, required-file set, embedded policy bytes and hash, detector identity, completeness fields, object IDs, modes, and file hashes from the exact Git tree. Offline historical validation verifies the embedded policy hash, copied-byte hashes and sizes, internal schema consistency, index projection, and raw immutability without consulting the mutable registry or executing Git network access. The immutable source-capsule manifest is scoped only by repository, SHA, adapter, capsule ID, and policy hash. It never contains version applicability. Index adapter, capsule ID, policy hash, focus packages, SHA, canonical path, kind, and revision must match the immutable format-3 manifest exactly; `applies_to_version_ids` exists only in the generated index.

Query deep dives use the same format with adapter `explicit-git-blobs-v1`. Their `capsule` object instead has exactly `adapter`, `capsule_id`, `policy_hash`, `request_id`, `question_hash`, `paths`, `secret_scan`, `tracked_source_scope_completeness`, and `repository_completeness`. `paths` is the sorted exact `{path, reason}` list from the immutable request. `request_id` is SHA-256 of the request's compact canonical JSON after removing `request_id` and `created_at`, using the same serialization rules as policy hashing. `question_hash` is SHA-256 of the question's exact UTF-8 bytes without normalization. `capsule_id` equals `request_id`. `secret_scan` has the same exact schema as above. Completeness must be `complete-for-requested-paths`; repository completeness remains `intentionally-incomplete`. The immutable raw manifest does not duplicate the full question text or requested version identity; request-to-version applicability lives only in the generated index.

### Full-Reading Budget Contract

All limits count raw bytes, not characters or estimated tokens. Every required reading file must decode as strict UTF-8 and contain no NUL byte.

Capsule accounting includes every saved upstream blob but excludes the generated `snapshot.md`. Packet accounting includes:

- `ingest-packet.md`;
- the canonical `snapshot.md` used for provenance;
- every added supplement `snapshot.md`;
- every upstream file and release-note file listed as required reading; and
- no generated `changed-files.txt` or `source-diff.patch` aid.

Required reading order is exact: canonical `snapshot.md` first; then, for each `added_evidence_id` in packet order, that supplement's `snapshot.md` followed by its recorded upstream files sorted by POSIX `path`; finally `ingest-packet.md`. A path encountered again is omitted at its later occurrence. Release-note files are included at their owning evidence position using the same POSIX ordering. `required_reading` records this order exactly. `max_packet_files` counts these files, including `ingest-packet.md`. `max_packet_utf8_bytes` is their exact byte sum after the packet Markdown has been rendered.

`ingest-packet.md` renders configured maxima and required paths but not the derived `actual_*` values, so its bytes do not depend on the result being measured. Actual values live in `packet.json` and are validated from disk.

Capsule selection, manifest rendering, packet rendering, and both budget checks occur in transaction staging before any raw snapshot, index, or packet publication. A capsule that passes its own limits but fails packet limits is a failed collection with no promoted evidence.

V1 does not automatically split a capsule. Automatic split identity is intentionally unsupported. An over-budget capsule enters `needs-policy-review`; the operator must approve larger bounded limits or define a separately designed adapter version. This removes ambiguous partial-capsule semantics.

### Version Index V2

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

#### Capture Records

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

Canonical IDs are `<sha>:c0`; supplement IDs are `<sha>:rN`. Allowed purposes are `release-evidence`, `legacy-supplement`, `source-capsule`, `policy-upgrade`, and `query-deep-dive`. Source capsules and policy upgrades use adapter `npm-tracked-source-v1` and the exact embedded capsule ID. Query deep dives use adapter `explicit-git-blobs-v1` and the immutable request ID as capsule ID. Supplements use a positive revision unique per SHA. Capture records sort by `capture_order`, canonical before supplement, then revision.

Legacy projection is exact. A format-1 or format-2 canonical snapshot projects as revision zero, purpose `release-evidence`, empty `adapter`, `capsule_id`, `policy_hash`, and `focus_packages`, and applies to every version record at its SHA. Every format-1 or format-2 supplement projects as `legacy-supplement`, with the same four empty capsule fields and applicability derived only from exact identities in immutable `release_evidence`. No legacy metadata is reinterpreted as a new purpose. Missing or ambiguous legacy applicability fails migration. Validators compare legacy records only to fields those immutable formats contain: repository, SHA, capture kind, revision, path, release evidence, and copied-file hashes. They never require format-3 adapter or policy fields from a legacy manifest.

Every snapshot path must resolve to an immutable manifest and match according to its format-specific projection above. A canonical capture applies to every version identity at its SHA. A supplement applies only to the explicit version IDs listed in the generated capture record and those versions' `evidence_ids`. Applicability is index metadata and is deliberately absent from immutable raw manifests.

Within one repository, `(sha, adapter, capsule_id, policy_hash)` identifies at most one source-capsule capture. `focus_packages` and `applies_to_version_ids` are sorted unique lists. A later release identity sharing the SHA attaches that existing raw capture by changing only the generated index and creating an independent supplement packet. The existing manifest and capture directory remain byte-for-byte unchanged. An A-then-later-B shared-SHA sequence must validate before and after attachment without duplicating or modifying raw evidence.

Source-capsule applicability is package-aware:

- a `package-version` record is eligible only when its non-empty `package` is in the capture's `focus_packages`;
- a `tag` record is eligible only when its non-empty `package` is in `focus_packages`;
- a `branch` or `commit` record is eligible only with an empty `package`; it represents repository-state evidence and may receive the capsule after the resolver confirms every focus package at that SHA; and
- a release identity for an internal dependency that is not also a focus package is never eligible merely because it shares the SHA or appears in `included_packages`.

Before any migration or future collection hashes a new version record, one shared `bind_version_package_v1` routine binds plain-semver tags. It uses, in precedence order, exact immutable release evidence, an explicit package-scoped registry track, or exactly one package among all configured capsule focus packages whose package manifest at that SHA has the tag's version. Zero or multiple candidates are `needs-policy-review`. In a repository with any capsule policy, no plain-semver tag may be hashed with an empty package. Once hashed, package binding is immutable; later collection may add evidence but never mutate identity fields. The validator recomputes eligibility before every attachment and on index load. Tests cover migration and newly discovered tags, two package releases sharing one SHA, allowed focus-package attachment, rejected sibling-package attachment, unambiguous resolution, ambiguous tags, and branch/commit attachment.

#### Version Records

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

#### V1 Migration

An index without `format_version` is v1. It remains readable for existing release collection and validation, but capsule collection is blocked until explicit migration.

`migrate-index-v2 --repo <id> --dry-run` performs these deterministic steps:

1. group v1 entries by SHA and require one canonical path per SHA;
2. create one canonical capture record per SHA;
3. create one version record per existing release, branch, tag, or commit identity, calling `bind_version_package_v1` before hashing `version_id`;
4. preserve aliases, release-note paths, changelog paths, capture order, and branch observations;
5. scan immutable snapshot manifests under the repository snapshot root for same-SHA supplements;
6. map legacy supplements only when their release evidence identifies exact existing version identities;
7. classify a mapped old supplement as `legacy-supplement`; and
8. fail migration on an unreferenced or ambiguous supplement rather than guessing its scope.

Dry-run writes no generated state. Approved migration stages a complete v2 index, validates a save/reload round trip, and publishes exactly one `index-v2-migrate` transaction and `index-migrated-v2` run event through the protocol below. Its immutable artifact set is empty; its before and after index hashes must differ. V1 is never rewritten implicitly. Loading v2 and saving it without semantic changes must be byte-identical.

### Packet Contract V2

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
- the set of `from.evidence_ids` is a proper subset of the set of `to.evidence_ids`; no evidence is removed;
- both endpoint lists independently use canonical-first, increasing-revision order;
- `added_evidence_ids` is exactly the non-empty set difference `to - from`, ordered as those IDs appear in `to`; it need not be a suffix;
- every added capture is a supplement applicable to that version;
- `changed_files` is empty; and
- `required_reading` is the exact ordered projection defined by the full-reading budget contract, including first-occurrence deduplication.

Packet ID canonicalization serializes the exact packet object after removing `packet_id`, `reading_budget.actual_files`, and `reading_budget.actual_utf8_bytes`, using sorted object keys and preserving every array in its already normative order. SHA-256 of those bytes is the 64-hex semantic digest. The readable label is derived from the index version record named by `to.version_id`: use its `ref_name` when non-empty, otherwise `to.sha`; lowercase ASCII, replace each maximal run outside `[a-z0-9._-]` with `-`, trim `-`, fall back to `ref`, and truncate to 40 bytes. The ID is `supplement-<label>-<sha12>-<digest16>`. Actual budget values are deterministic derivatives and do not participate. Exact ordered before/after evidence lists, ordered set difference, and required-reading paths do participate, so insertion of an older revision such as `r1` into an endpoint already containing `r2` cannot collide with another transition.

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

Existing `state-events.jsonl` files retain their exact parser but become read-only legacy prefixes. No new protocol appends JSONL. There is no `superseded` state and no replacement link. Adding evidence always creates an independent supplement packet, so no existing packet or completed state event is rewritten.

#### Immutable Event Publication And Packet Lifecycle

All new transaction, lifecycle, retry, and command-report histories use one immutable-event-file primitive. A chained-history event object includes `event_format = 2`, positive `sequence`, `previous_event_hash`, and `event_hash`. `event_hash` is SHA-256 of the compact canonical event bytes after removing only `event_hash`; `previous_event_hash` is 64 zeroes for the first event unless the history-specific schema says otherwise. Its final filename is `<sequence-as-6-decimal-digits>-<event_hash>.json`. Readers reject unknown fields, duplicate JSON keys, filename disagreement, gaps, non-increasing sequence, previous-hash disagreement, or a non-final filename. Standalone run events use the same canonical bytes and publication mechanics but their schema-owned filename is `<run-id>.json` and their content hash is recorded by the owning transaction.

Each history has a sibling staging namespace named `<history-directory-name>-staging/`, which readers never treat as committed history. Publication writes `<sequence>-<event-hash>.json.staged` there as a regular no-follow file, file-`fsync`s it, and directory-`fsync`s its staging parent. It then creates the final name with an atomic same-filesystem no-replace hard link, verifies same inode and exact bytes, and directory-`fsync`s the destination parent. That destination-parent `fsync` is the event commit boundary. Only then may it unlink the staged name and directory-`fsync` the source parent. Recovery under the history's owning lock publishes a valid staged-only event, removes a staged link whose exact final event is durable, accepts an exact hash-valid final event when staging cleanup already completed, or reports any other destination/staging combination as `recovery-required`.

Before first use, every missing generated namespace component is created one at a time with exclusive no-follow directory semantics and its immediate parent is directory-`fsync`ed before the next component is created. This bootstrap applies to staging and final artifact parents as well as `transactions/`, every event-history and sibling staging directory, packet lifecycle, retry, command-run, and run-event namespaces. A missing namespace is never assumed durable merely because a child was later `fsync`ed.

Lifecycle transitions use lock order `repository collection lock -> packet lock`. Existing packet histories are not rewritten. Their future events live at:

```text
tracking/github/repos/<company>/<repo>/packets/<packet-id>/state-events-v2/
└── <sequence>-<event-hash>.json
tracking/github/repos/<company>/<repo>/packets/<packet-id>/state-events-v2-staging/
└── <sequence>-<event-hash>.json.staged
```

Each lifecycle event has exactly `event_format`, `event_hash`, `sequence`, `previous_event_hash`, `legacy_history_hash`, `repo_id`, `packet_id`, `event`, `from_state`, `to_state`, `actor`, and `observed_at`. `legacy_history_hash` is SHA-256 of the exact legacy `state-events.jsonl` bytes, or SHA-256 of empty bytes when no legacy file exists, and is identical in every v2 event. The first v2 event uses 64 zeroes for `previous_event_hash`; later events name the preceding v2 event hash. `event` is `state-initialized` only for a new packet's sequence one, with empty `from_state` and `to_state = "awaiting-review"`; otherwise it is `state-transition` and the state pair must be one exact allowed transition above. Actor is bounded ASCII and timestamps are UTC RFC3339.

The coordinator validates the complete legacy prefix once, verifies its immutable hash, reduces all v2 events, and publishes one next event through the generic primitive. Initial `awaiting-review` is event sequence one for a newly published packet and is included in the packet's artifact tree before promotion. For a packet with legacy history, the first v2 transition starts after the legacy terminal state. A changed legacy file after a v2 event exists is corruption.

Because no shared file is appended or truncated, recovery either publishes the staged next event, recognizes an already published matching event, or reports an unexpected destination as `recovery-required`. Crash tests interrupt after every namespace `mkdir`, file write, file `fsync`, hard link, staged unlink, and source- or destination-parent directory `fsync`.

## Generic Collection Operations And Durability Contract

This section is normative for collection, attachment, migration, retry, lifecycle transition, and deep-dive operations across every repository. The same journal, retry, and safety behavior applies regardless of provider.

### Recoverable Publication Protocol

Filesystem operations across raw snapshots, packets, and the index cannot be one atomic rename. The implementation therefore uses a repository-scoped write-ahead journal and deterministic recovery rather than claiming cross-directory atomicity.

Generated transaction state lives at:

```text
tracking/github/repos/<company>/<repo>/transactions/<transaction-id>/
├── events/
│   └── <sequence>-<event-hash>.json
├── events-staging/       # transient event hard-link source
├── before-index.json
├── after-index.json
├── staged-artifacts/     # snapshots and/or packet until publication
├── terminal-event.json   # exact staged run file
└── COMMITTED
```

The transaction ID is a 64-character lowercase SHA-256 over repository ID, operation, exact SHA or empty string, policy hash or empty string, selected version ID or empty string, capsule ID or request ID or empty string, run ID, and attempt ordinal. This makes retries distinct while leaving each interrupted attempt recoverable by its journal.

#### Operations And Terminal Events

The protocol supports exactly these operation shapes:

| Operation | Immutable artifacts | Index change | Terminal state |
| --- | --- | --- | --- |
| `index-v2-migrate` | none | complete v1-to-v2 replacement | `index-migrated-v2` |
| `source-capsule-collect` | one new supplement and one packet | add capture and attach it to one version | `source-capsule-collected` |
| `source-capsule-attach` | one packet; existing raw capture is reused | attach existing capture to one additional version | `source-capsule-attached` |
| `source-capsule-check` | none | none; before and after index hashes are equal | `source-capsule-unchanged` |
| `deep-dive-collect` | one new supplement and one packet | add capture and attach it to the requested version | `deep-dive-collected` |
| `deep-dive-check` | none | none; before and after index hashes are equal | `deep-dive-unchanged` |

Every transaction reserves a unique run ID and exact run path before preparation:

```text
tracking/github/runs-v2/<run-id>.json
```

`run_id` is the command's pre-existing collection run ID, matching `[0-9]{8}T[0-9]{12}Z-[a-z0-9-]{1,80}-[0-9a-f]{32}` and containing no path separators. Tests inject its UTC timestamp and nonce. A command creates a separate run ID for each event-v2 transaction, so several capsule operations selected by one invocation cannot collide.

Existing `tracking/github/runs/*.jsonl` files remain read-only event-v1 history. The final v2 run file must not exist during preparation. `terminal-event.json` is written as compact canonical JSON with no trailing newline, file-`fsync`ed, and recorded by device, inode, byte size, and SHA-256 before `prepared`. It is later published with the immutable-event hard-link mechanics into `tracking/github/runs-v2/`; source and destination directories must be on the same device, and this transaction-owned source link is retained until `COMMITTED` rather than cleaned immediately. All event-v2 operations use this exact terminal schema; inapplicable string fields are empty rather than omitted:

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

The allowed operation/state pairs are exactly those in the table. Migration uses selector and operation ID `index-v2` and empty ref, SHA, version, capture, packet, and request fields. A source-capsule operation ID is `capsule:<capsule-id>:<policy-hash>:<version-id>`. A deep-dive operation ID is `deep-dive:<request-id>`. Collection and attachment require capture and packet IDs; unchanged checks require the existing capture ID and an empty packet ID; deep dive additionally requires its request ID. Within a repository, `(sha, request_id)` identifies at most one deep-dive capture, and its index applicability may name only the request's `version_id`.

Legacy event-v1 run files retain existing reconciliation by `(repo_id, selector)`. Each event-v2 run file validates independently and contains exactly one terminal event for its transaction. Across event-v2 history, `transaction_id` and `run_id` are independently unique, the filename must equal `<run_id>.json`, and the journaled run path must resolve to that file. The event-v2 status reducer keys latest results by `(repo_id, operation_id)` and never assumes one terminal event per selector, so several capsules for one release are representable.

#### Locks And Preparation

The repository `.collection.lock` is acquired first and held through recovery or publication. Nested lock order is exactly:

```text
collection lock -> repository snapshot-root promotion lock -> packet lock
```

The snapshot-root promotion lock is the existing stable `.promotion.lock` below that repository's snapshot root. It is acquired once when an operation may create a snapshot. Final `-rN` allocation occurs while this stable lock is held; no final snapshot path is needed to identify the lock. After revision allocation and packet-ID derivation, the exact packet lock is acquired. Index-only migration acquires neither nested lock. Source-capsule attachment acquires only the packet lock because it creates no raw snapshot. No mutating path may acquire these locks in reverse order.

Packet lifecycle transitions also acquire the repository collection lock before the packet lock and recover or block on unfinished journals before reading packet state. This prevents approval of a packet published by an uncommitted transaction.

The transaction coordinator owns these descriptors. Snapshot and packet publication gain internal variants that accept already-open, already-locked parent descriptors; they must not reacquire the same lock through another descriptor. Public single-artifact helpers retain their current lock-owning behavior outside a journal transaction.

Before publication, the collector:

1. recovers every nonterminal transaction for the repository;
2. bootstraps `transactions/`, creates the transaction directory plus `events/` and `events-staging/` with no-follow, exclusive semantics, and immediately `fsync`s each affected parent;
3. preflights packet lifecycle and index expectations;
4. acquires the stable repository snapshot-root promotion lock when required;
5. allocates final supplement revisions while that stable lock is held;
6. derives the packet ID, acquires its packet lock when required, and retains all locks through commit or rollback;
7. stages and validates the operation's exact immutable artifact set;
8. writes `before-index.json` and `after-index.json`, then file-`fsync`s both even when their bytes are equal;
9. renders and file-`fsync`s `terminal-event.json`, records its ownership identity, bootstraps `runs-v2/`, and reserves a non-existing run path;
10. file-`fsync`s every regular file in every staged snapshot and packet, then directory-`fsync`s every staging directory bottom-up through `staged-artifacts/`;
11. directory-`fsync`s the transaction directory after all staged names and ownership identities are final;
12. publishes a `prepared` immutable journal event containing all paths, ownership identities, and SHA-256 hashes; and
13. directory-`fsync`s the transaction directory again before publication begins.

No `prepared` event may exist until every recovery input and every byte intended for promotion is durable. Staging and each destination must be on the same filesystem used by its same-device rename or hard link. Failure to establish that topology is a deterministic preflight failure with no publication.

Publication then:

1. promotes each owned immutable snapshot or packet by same-device rename, directory-`fsync`s both its staged source parent and final destination parent, and publishes a journal event with path, device, inode, and content hash;
2. when the operation table requires an index change, atomically replaces the index from its staged source, file-`fsync`s the final index, directory-`fsync`s both source and destination parents, and publishes the resulting hash; otherwise requires equal before/after hashes and emits no `index-published` event;
3. atomically hard-links the staged terminal file to the reserved run path with no replacement, verifies linked inode and bytes, directory-`fsync`s `tracking/github/runs-v2/`, and publishes the journal event;
4. writes and file-`fsync`s `COMMITTED`, then `fsync`s the transaction directory, removes the staged terminal hard link, and `fsync`s the transaction directory again; and
5. releases locks.

Every journal event uses the immutable-event primitive in the transaction's `events/` directory. Its sequence and previous hash form the transaction chain; events have exact operation names and no free-form secret content. The prepared event stores the exact run ID, run path, terminal bytes hash, and intended terminal event. Recovery can therefore locate the event without searching other run files.

A directory content hash is SHA-256 over canonical JSON listing every relative path, Git-style mode, byte size, and file SHA-256 in sorted path order. Ownership journal events store this hash together with device and inode.

Every journal event has required common fields `event_format = 2`, `event_hash`, `previous_event_hash`, `transaction_id`, `sequence`, and `event`. Event-specific fields are exact:

| Event | Additional fields |
| --- | --- |
| `prepared` | `repo_id`, `operation`, `before_index_hash`, `after_index_hash`, `planned_artifacts`, `run_id`, `run_path`, `run_device`, `run_inode`, `terminal_event`, `terminal_event_hash` |
| `artifact-published` | `artifact_kind`, `path`, `device`, `inode`, `content_hash` |
| `index-published` | `after_index_hash` |
| `terminal-event-published` | `run_path`, `terminal_event_hash` |
| `rolled-back` | `reason_code` |
| `recovery-required` | `reason_code`, `observed_index_hash` |

`planned_artifacts` is the operation table's exact sorted set of records `{artifact_kind, path, staged_device, staged_inode, content_hash}` for snapshots and packets. Promotion must be a same-device rename, so the staged ownership identity remains valid at the final path even if a crash occurs before `artifact-published` is journaled. Index publication is represented by its dedicated hashes. Run publication is represented by `run_id`, `run_path`, `run_device`, `run_inode`, and `terminal_event_hash` in `prepared`. Journal parsing rejects unknown fields, sequence gaps, an artifact set inconsistent with the operation, events invalid for the current phase, and hashes or ownership identities that disagree with staged bytes. `COMMITTED` is a zero-byte regular file created with exclusive no-follow semantics, file-`fsync`ed, and followed by transaction-directory `fsync`. The staged terminal-event hard link is removed only after commit and that unlink is followed by transaction-directory `fsync`; per-event staging links follow the generic event commit rule above.

Recovery under the collection lock follows these rules:

- `source-capsule-check` and `deep-dive-check` have no mutable artifact or index phase; recovery either publishes the prepared terminal event or recognizes the matching event and commits;
- before index publication, verify ownership tokens, remove only transaction-owned snapshots and packets, restore no index, and publish `rolled-back`;
- after index publication but before terminal-event publication, complete forward when every artifact matches, or atomically restore `before-index.json` and remove only verified owned artifacts when an artifact is missing;
- terminal-event publication is the irreversible forward-only boundary; recovery detects it only at the exact journaled run path and accepts it only when its device, inode, parsed transaction ID, and byte hash match the staged run identity, even if `terminal-event-published` was not journaled;
- after that boundary, intact artifacts and index complete forward by writing `COMMITTED`, while any mismatch becomes `recovery-required` rather than rollback;
- if an existing artifact's device, inode, or content hash differs from the journal, mark `recovery-required` without deleting or rewriting it;
- if the current index matches neither recorded hash, mark `recovery-required`, block further collection, and require manual review; and
- never delete or rewrite an artifact without matching repository namespace, path, device, inode, and expected hash.

Every recovery rename or index restoration is followed by directory-`fsync` of both source and destination parents before the recovery journal advances. Every verified removal is followed by source-parent `fsync`. If the run path exists with any other bytes, recovery marks `recovery-required` and never edits or deletes it. If rollback occurs before terminal publication, the still-absent reserved run path requires no cleanup. Read-only validation reports nonterminal or `recovery-required` journals but does not mutate them. Collection and explicit `recover` perform recovery. Crash tests interrupt after every namespace creation, file write, file `fsync`, rename, hard link, unlink, source-parent `fsync`, destination-parent `fsync`, immutable event publication, and commit marker.

Packet directory hashes in a committed journal describe publication-time bytes with the initial state event. Later valid immutable lifecycle events intentionally change that directory, so completed-journal validation checks the publication-time subtree separately from `state-events-v2/` rather than comparing one current whole-tree hash. Nonterminal recovery can compare the whole staged artifact because the packet lock prevents lifecycle transitions until commit.

### Normal Capsule Collection

For each selected release or branch with capsule policy:

1. resolve the exact ref and SHA, then call `bind_version_package_v1` before creating or looking up its version ID;
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

### Persistent Retry And Quarantine State

Existing `collection-failures.jsonl`, if present, is a validated read-only legacy prefix. New retry state is an immutable chained history:

```text
tracking/github/repos/<company>/<repo>/collection-failures/events/
└── <sequence>-<event-hash>.json
```

If a legacy file exists, the first v2 event's `previous_event_hash` is SHA-256 of its exact validated bytes; otherwise it is 64 zeroes. Later events name the preceding v2 event hash. Once the first v2 event exists, any change to the legacy prefix is corruption.

Each failed-attempt event has exactly:

```json
{
  "event_format": 2,
  "event_hash": "<64-hex>",
  "sequence": 1,
  "previous_event_hash": "<64-hex-or-zeroes>",
  "event": "attempt-failed",
  "attempt_id": "<64-hex>",
  "run_id": "<bounded-run-id>",
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

`retry_key` hashes exactly repository ID, operation, selector, and unit ID. `resolved_sha`, `policy_hash`, and `phase` are failure observations and never create parallel retry keys. A changed capsule policy creates a new unit ID; a changed deep-dive request creates a new request ID. `run_id` uses the exact run-ID grammar above and is generated before an attempt executes. `attempt_id` hashes retry key, epoch, attempt ordinal, and that stored `run_id`. `fingerprint` hashes category, stable code, and phase; volatile paths, timestamps, and remote prose are excluded. Codes are ASCII slugs of at most 100 bytes.

Transient codes are limited to reviewed network and infrastructure classes such as `network-timeout`, `dns-failure`, `github-rate-limit`, `remote-5xx`, and `git-interrupted`. Deterministic-policy codes include `unsupported-workspace`, `ambiguous-package`, `missing-required-root`, `unsafe-required-file`, `capsule-budget-exceeded`, and `packet-budget-exceeded`. Unmapped post-selection exceptions use category `unknown` and a bounded exception-class code. A nonterminal publication journal is recovered before its selector can consume another retry attempt.

The command creates its `run_id` before loading the registry. Registry parsing occurs before trustworthy repository scheduling units exist, so `invalid-registry` is never written to a repository retry history. It is published at `tracking/github/command-runs/<run-id>/events/000001-<event-hash>.json` through the same immutable-event primitive. The event has exactly the four common chain fields plus `event = "command-failed"`, `run_id`, `command`, `args_hash`, `code = "invalid-registry"`, `registry_path`, `registry_sha256`, and `observed_at`. `args_hash` hashes compact canonical JSON of semantic CLI arguments after removing credentials, environment values, and presentation-only flags. `registry_path` is the normalized repository-relative configured path; `registry_sha256` is the exact file hash or an empty string when no regular readable file exists. This command-level record has no repository, selector, retry, transaction, or packet fields. The status monitor consumes it separately and the command stops before repository selection.

The reducer processes valid events in sequence order under the repository collection lock. Epoch starts at one. Within an epoch, attempt ordinals count executions of the retry unit and must increase by exactly one regardless of fingerprint or failing phase. A changed failure does not reset the retry budget. Deterministic-policy failures immediately produce `needs-policy-review`. Transient and unknown failures produce:

| Attempt | Meaning | Outcome | Delay |
| ---: | --- | --- | ---: |
| 1 | initial failure | `retry-pending` | 15 minutes |
| 2 | retry 1 failed | `retry-pending` | 2 hours |
| 3 | retry 2 failed | `retry-pending` | 24 hours |
| 4 | retry 3 failed | `quarantined` | none |

No in-process daemon is added. The only retry scheduler command is `retry-due [--repo <id>]`. It reduces the history, selects each due `retry_key` once, and dispatches the exact operation, selector, and unit ID from that key. A normal scheduled command that encounters the same key applies the same due-state gate. Not-due, quarantined, and policy-review keys are reported and skipped. Work units are deduplicated before dispatch; the repository lock and a second state check after lock acquisition prevent concurrent duplicate attempts.

Successful retry publishes exactly:

```json
{
  "event_format": 2,
  "event_hash": "<64-hex>",
  "sequence": 2,
  "previous_event_hash": "<64-hex>",
  "event": "attempt-succeeded",
  "attempt_id": "<64-hex>",
  "run_id": "<bounded-run-id>",
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

Explicit reset publishes exactly:

```json
{
  "event_format": 2,
  "event_hash": "<64-hex>",
  "sequence": 3,
  "previous_event_hash": "<64-hex>",
  "event": "retry-reset",
  "reset_id": "<64-hex>",
  "run_id": "<bounded-run-id>",
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

Committed transaction history is authoritative over retry history. Before dispatching a due key, the reducer searches for a committed event-v2 transaction with the same operation ID and successful semantic result. If found, it publishes the missing `attempt-succeeded` event under the collection lock without republishing evidence. For deep dives this check uses the unique `(repo_id, sha, request_id)` capture; for capsules it uses the operation ID and exact index applicability. A crash after transaction commit but before retry success therefore converges to success rather than creating another snapshot or packet.

`retry-reset` is valid only for a known `retry-pending`, `needs-policy-review`, or `quarantined` key. It requires explicit `--actor` and `--reason`; both are at most 200 ASCII bytes. `new_epoch` must equal the prior epoch plus one. Reset projects the key to `retry-pending` with `next_retry_at = observed_at` and the next execution ordinal equal to one. Earlier epochs remain immutable history and do not count toward the new four-attempt bound. `reset_id` hashes retry key, new epoch, actor, reason, and the stored `run_id`.

Retry events publish through the immutable-event primitive while the collection lock is held. Duplicate attempt, reset, run, or event IDs are invalid, and retry commands recheck for an existing semantic ID under lock before publication. Histories never contain credentials or unbounded exception text.

The retry-history parser validates any frozen legacy prefix and then the v2 hash chain. It rejects unknown fields, duplicate JSON keys, filename or hash disagreement, invalid timestamps, epoch or attempt gaps, retry-key, attempt-ID, reset-ID, or run-ID disagreement, unit IDs inconsistent with their operation, outcomes inconsistent with category or attempt number, success without a currently retryable key, and reset events for unknown keys.

The status reducer projects `retry-pending`, `needs-policy-review`, and `quarantined` once per retry key into generated JSON and Markdown. These states are never reported as unchanged or collected, and they block ingest eligibility only for the affected operation unit and version until resolved.

### Versioned Secret Detector Contract

Every blob selected for an npm capsule or deep dive is scanned by the standard-library suite `text-secrets-v1` after size, strict UTF-8, and NUL validation and before staging. The scanner reads the complete decoded blob without Unicode or newline normalization and applies Python `re` patterns with `re.ASCII`; multiline behavior is enabled only where shown. It does not scan rejected binary or oversized content because those files already fail collection.

The suite contains exactly these detector codes and expressions:

| Detector code | Python regular expression |
| --- | --- |
| `pem-private-key-header-v1` | `(?m)^-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----[ \t]*\r?$` |
| `aws-access-key-id-v1` | `(?<![A-Z0-9])(?:AKIA|ASIA)[A-Z0-9]{16}(?![A-Z0-9])` |
| `github-token-v1` | `(?<![A-Za-z0-9_])(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{36,255}(?![A-Za-z0-9])` |

Changing a pattern, flag, detector set, decoding rule, or maximum supported input requires a new suite name. Unit fixtures construct exact positive vectors from fragments to avoid committing token-shaped strings: `"-----BEGIN " + "PRIVATE KEY-----"`, `"AKIA" + "A" * 16`, and `"ghp_" + "A" * 36`. Exact negative vectors are the corresponding values with the final character removed, each value embedded within an ASCII alphanumeric token, ordinary words `client_secret`, and a public-key header. Tests also cover CRLF, matches at both file boundaries, multiple detector matches, and one allowlisted finding alongside one non-allowlisted finding.

Every finding is `(path, git_blob_oid, detector_code)`. All findings must be allowlisted independently by the exact immutable triple before promotion. Reports contain only that triple, the file SHA-256, and suite name; they never contain the matched text or byte offset. The manifest claim is only `scanned by text-secrets-v1`. The collector and wiki must never describe a scanned file or capsule as `secret-free`, because this bounded detector suite cannot prove absence of credentials.

### Query-Driven Deep Dive Safety

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
  "policy_revision": 1,
  "created_at": "<UTC-RFC3339>"
}
```

Allowed reasons are `implementation`, `type-definition`, `test-evidence`, and `configuration`. Paths are sorted unique safe repository-relative POSIX paths. The question is at most 2,000 UTF-8 bytes. `secret_detector` is required and must equal `text-secrets-v1`. `policy_revision` is a positive integer selected by the operator and begins at one. `request_id` hashes every semantic field except itself and `created_at`. An operator who deliberately wants a new capture under changed policy increments `policy_revision`, producing a new request ID; automatic drift detection never does so. A request becomes immutable once a supplement references its hash; later changes fail validation rather than changing raw provenance.

The deep-dive collector:

- resolves paths only through the exact commit tree;
- accepts only tracked regular Git blobs with mode `100644` or `100755`;
- reads bytes with `git cat-file blob`, never by executing or importing repository files;
- rejects symlink mode `120000`, gitlink mode `160000`, untracked paths, unsafe paths, LFS pointer blobs, non-UTF-8 bytes, NUL bytes, and configured size-limit violations;
- never runs package installation, build, test, generator, hook, or repository script commands; and
- copies accepted bytes exactly without newline normalization.

An LFS pointer is any blob beginning with the exact ASCII line `version https://git-lfs.github.com/spec/v1`. Secret detection follows the versioned contract above. A flagged blob blocks promotion. A false-positive exception requires stable registry allowlisting by repository path, exact Git blob object ID, and detector code; path-only allowlisting is invalid.

Before collection, the deep-dive resolver checks committed index and transaction history for `(repo_id, sha, request_id)`. If absent, it creates one `query-deep-dive` supplement, attaches it only to the selected version ID, creates an independent v2 supplement packet, and leaves it awaiting review. If the exact request and capture are already committed and applicable, it validates against the embedded historical policy and emits `deep-dive-check`/`deep-dive-unchanged` with no duplicate snapshot or packet. Difference from the current registry is reported separately as `current-policy-drift`; it is ordinary maintenance, not corruption or `recovery-required`. A conflicting immutable request, SHA, requested version, question hash, path list, or capture bytes is `recovery-required`, never a second capture. A deliberate policy recapture requires a new request ID through `policy_revision`. Query-specific paths remain generated tracking input and do not become capsule registry policy.

`rules/query-and-synthesis.md` must be corrected to require this same-SHA supplement flow instead of updating accepted raw evidence.

## PayPal JS Conformance Appendix

This appendix is a rollout fixture, not a standalone rule or adapter. It introduces no PayPal-specific branches. Every observed requirement, including exact generated `index.js`, shared-SHA identities, historical versions, and package closure, must be expressible through the generic schemas above. A failure that requires repository-name logic rejects the generic design.

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
- every capsule default, unknown key, complete `npm-package-name-v1` grammar including scoped leading-dot/underscore package components, exact generated file/directory path, path restriction, applicable-allowlist filtering, canonical array order, and policy hash rule;
- workspace list/object forms, supported globs, overlaps, root package, and rejected patterns;
- duplicate package names, malformed manifests, dependency cycles, local protocols, dependency-map precedence, exact `peerDependenciesMeta`, optional peers, and malformed peer metadata;
- tracked declaration roots, `types/`, wrappers, `main`, `module`, `bin`, root export sugar, exact subpath-key grammar, unsafe and mixed-key rejection, exports arrays, ordered condition chains, JSON Pointers, `null` exclusions, literal targets, slash-containing wildcard substitutions, deterministic static enumeration, exact generated file/directory matches, unreviewed missing targets, and generated-policy overlap failures;
- classification precedence and every allowed excluded category;
- complete version-neutral format-3 top-level and nested schemas, commit-only refs, canonical capture-ID locators rather than release-derived paths, purpose-specific empty release fields, version-neutral directory names, upstream-relative paths, exact purposes and deep-dive hashes, format-1/2 `legacy-supplement` projection compatibility, embedded historical policy validation, exact Git object IDs and modes, executable blobs, symlinks, gitlinks, LFS pointers, and binary data;
- every `text-secrets-v1` positive and negative vector, boundary and CRLF behavior, multiple findings, exact-blob allowlisting, detector-version policy hashing, and rejection of `secret-free` output;
- raw-byte capsule and packet budget boundaries, including rendered manifests and packet Markdown;
- index-only v1-to-v2 migration publication and recovery, shared `bind_version_package_v1` behavior for migrated and newly discovered plain tags, shared-SHA package identities, ambiguous legacy supplements, and byte-stable v2 round trips;
- bidirectional index-only capture/version evidence references, package-aware eligibility, rejected sibling-package attachment, supplement revision ordering, and A-then-later-B shared-SHA attachment with an unchanged manifest hash;
- packet v1 compatibility, exact supplement-only packet-v2 set-difference invariants including older-revision insertion, exact required-reading order and deduplication, readable-label normalization, packet canonical bytes, and rejection of baseline, delta, or comparison packet-v2 values;
- supplement required-reading calculation and packet budget validation;
- unchanged packet state events and rejection of mixed packet versions;
- stable snapshot-root lock ordering, concurrent revision allocation without collision, first-use namespace bootstrap, file-`fsync` of every staged artifact and index copy, bottom-up staging directory `fsync`, transaction-parent durability, both-parent `fsync` after every rename, source-parent `fsync` after cleanup, and immutable journal recovery after every durable operation;
- exact run-path recovery, operation-specific artifact sets and terminal events, index-only and attachment-only transactions, multiple capsules for one selector, ownership mismatch, index hash mismatch, forward completion, rollback, and manual-recovery projection;
- retry persistence across restarts, frozen legacy-prefix binding, immutable event hash chains, stored run-ID participation in attempt/reset IDs, one key across changing failure phases, exact command-level invalid-registry schema before repository selection, due-key deduplication, committed-transaction success reconciliation, injected clocks, lock-time recheck, reset epochs, four-attempt quarantine, and exact `retry-due` CLI dispatch;
- deep-dive uniqueness, unchanged replay under embedded historical policy after commit/retry interruption, current-policy-drift reporting, explicit policy-revision recapture, conflicting request rejection, untracked, traversal, symlink, gitlink, LFS, secret, and size failures;
- frozen legacy lifecycle-prefix validation and immutable v2 lifecycle recovery at every namespace, write, link, unlink, and directory-`fsync` boundary;
- correction of the query-rule immutability conflict; and
- the exact PayPal graph of 15 canonical captures, 15 legacy packets, one main pilot supplement, and 14 later supplement packets.

Network-dependent PayPal verification remains outside the default unit suite. Passing existing tests alone does not approve migration; live dry-run evidence and deterministic validation are required.

## Acceptance Criteria

The design is implemented when:

- repository configuration can select `npm-tracked-source-v1` without company-specific code;
- the PayPal JS conformance fixture uses only registry policy and generic adapters while including complete declared tracked source for `@paypal/react-paypal-js` and internal `@paypal/paypal-js`, including tracked `types/`, runtime entrypoints, and reviewed generated targets;
- generated artifact correspondence is explicitly unverified rather than implied;
- no successful capsule silently omits required source or exceeds a full-reading budget;
- index v2 preserves shared-SHA version identities and every applicable supplement across save/reload;
- adding a later shared-SHA version changes only generated index and packet evidence, never the capsule manifest or raw capture;
- packet v2 represents same-SHA evidence additions without modifying existing packets or state history;
- format-3 manifests preserve exact Git object, mode, package, classification, policy, and detector provenance while format 2 remains readable;
- format-3 raw bytes and path derivation contain no initiating release identity; with the same SHA, effective policy, collection date, and revision allocation, choosing a different same-SHA version produces byte-identical capture output;
- no new transaction, lifecycle, retry, run, or command history appends JSONL;
- crash recovery converges after every durable staging, publication, and packet-lifecycle step using stable locks, immutable event files, exact journaled paths, and source- plus destination-parent durability;
- retry and quarantine state persists once per executable scheduling unit across processes and scheduled runs;
- deep dives read only safe exact-SHA Git blobs and execute no repository code;
- deterministic tests and validators pass; and
- no collection, migration, recovery, or retry command starts wiki ingest.
