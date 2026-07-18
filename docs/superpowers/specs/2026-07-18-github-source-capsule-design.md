# GitHub Public Source Capsule and Deep-Dive Design

**Status:** Approved
**Date:** 2026-07-18
**Extends:** `2026-07-14-github-repository-collection-design.md` and `2026-07-15-github-release-retention-design.md`

## Problem

The GitHub collector currently preserves repository documentation, package manifests, changelogs, release notes, and selected changed public files. That evidence is suitable for release-level ingest, but source-code coverage is accidental: a TypeScript file is retained only when it is an explicit registry key path or a changed path that matches the public-entrypoint heuristic.

The PayPal JS pilot exposes the gap. Its 15 snapshots contain only sparse TypeScript entrypoints, so a later query about implementation behavior may not be answerable from the retained raw evidence. Saving every repository file for every release would solve that gap at the cost of impractical full-read ingest units and excessive storage.

The collector therefore needs a bounded, deterministic public source capsule for each selected release, plus an immutable query-driven supplement workflow for details outside that capsule.

## Goals

- Preserve enough public implementation source to answer common code-level questions offline.
- Keep every capsule bounded and completely readable as an ingest unit.
- Make completeness claims relative to an explicit capsule scope, never the whole repository.
- Follow required internal monorepo dependencies without collecting unrelated packages.
- Keep repository and package policy in the registry rather than company-specific script branches.
- Preserve canonical snapshots and supplements as first-class immutable evidence.
- Support later same-SHA deep dives without modifying accepted raw files.
- Fail closed when required evidence cannot be captured completely.
- Retry transient failures without creating infinite collection loops.
- Keep collection batchable while preserving user-gated, one-packet-at-a-time ingest.

## Non-Goals

- Mirroring a complete Git repository at every release.
- Claiming that an npm adapter covers Swift, Android, PHP, Ruby, or other ecosystems.
- Parsing TypeScript or JavaScript import graphs in the first adapter.
- Collecting external dependency source.
- Automatically approving or ingesting a capsule or deep-dive packet.
- Relabeling the existing PayPal JS snapshots as source-capsule compliant.

## Selected Architecture

Use two evidence levels:

1. `npm-public-api-v1` creates a standard public source capsule for every selected npm release.
2. A query-driven deep dive creates a later immutable same-SHA supplement containing complete files needed for a specific question.

For a new release, default documentation and the source capsule are promoted together in one canonical snapshot. For an already accepted SHA, a new or upgraded capsule is an immutable `-rN` supplement.

```text
registry policy
    -> exact ref and SHA
    -> temporary checkout
    -> npm workspace and dependency resolution
    -> complete bounded package source directories
    -> immutable canonical snapshot or supplement
    -> first-class evidence index
    -> immutable awaiting-review packet
    -> user approval
    -> one full-read ingest cycle
```

## Registry Contract

The existing repository row may add a nested stable source-capsule policy:

```toml
[repos.source_capsule]
adapter = "npm-public-api-v1"
focus_packages = ["@paypal/react-paypal-js"]
dependency_scope = "internal-runtime-closure"
required_source_roots = ["src"]
include_paths = []
exclude_paths = [
  "**/*.test.*",
  "**/*.spec.*",
  "**/*.stories.*",
  "**/__fixtures__/**",
]
max_file_bytes = 1048576
max_files = 150
max_bytes = 3000000
```

The registry continues to contain stable intent only. It does not contain resolved packages, current SHAs, policy hashes, attempts, collection dates, or progress.

`required_source_roots`, `include_paths`, and `exclude_paths` are POSIX-style paths or glob patterns relative to each included package directory. They cannot be absolute, contain `..`, or escape the resolved workspace package. Repository-level evidence remains governed by the existing repository key-path policy.

The effective policy is the adapter's versioned defaults plus the repository overrides. The collector serializes that effective policy as canonical, sorted JSON and records its SHA-256 policy hash. TOML formatting and key order must not change the hash.

Adding another ecosystem requires a separately named and versioned adapter, for example `swift-public-api-v1` or `gradle-public-api-v1`. An adapter may reuse shared snapshot infrastructure, but it owns its ecosystem-specific discovery and completeness rules.

## NPM Workspace And Dependency Resolution

`npm-public-api-v1` parses structured JSON rather than extracting metadata with regular expressions. It supports npm workspace declarations in accepted array and object forms and discovers workspace package manifests at the exact checked-out SHA.

The resolver:

1. locates every configured focus package by its exact package name;
2. fails if a focus package is missing or ambiguous;
3. builds a deterministic map from package name to workspace path;
4. recursively follows workspace packages named by `dependencies`, `optionalDependencies`, and internal `peerDependencies`;
5. excludes `devDependencies` from the dependency closure;
6. records external dependencies but does not collect their source; and
7. resolves cycles with a visited set while preserving stable package ordering.

`internal-runtime-closure` is the only dependency scope accepted by `npm-public-api-v1`. A different closure rule requires a new adapter version rather than an undocumented interpretation of the same policy.

The PayPal JS capsule therefore focuses on `@paypal/react-paypal-js` and includes `@paypal/paypal-js` because it is an internal runtime dependency. Storybook, release automation, and other unrelated workspace packages remain outside the capsule.

## File Selection

The first npm adapter captures complete bounded source directories instead of attempting a TypeScript import graph.

For every included package, required evidence is:

- its `package.json`;
- every tracked public wrapper path named by adapter conventions or explicit `include_paths`;
- every regular tracked file under each configured required source root; and
- package-level source metadata required to interpret those files.

Configured exclusions remove tests, stories, fixtures, generated output, vendored dependencies, and build caches. An exclusion that removes a file otherwise classified as required is an error, not an optional omission.

The adapter records `exports`, conditional exports, wildcard exports, `main`, `module`, `types`, and `bin` declarations. A declared target is classified as:

- tracked and captured;
- tracked but outside the declared capsule, which fails review unless explicitly allowed;
- generated build output not present in Git, which is recorded as such; or
- missing or unsafe, which fails when the target should be tracked source evidence.

The adapter does not claim that source paths are byte-identical to the published npm artifact. Its claim is limited to complete tracked source coverage for the declared package scope at the selected Git SHA.

Optional documentation or examples may be omitted within policy, but every omission and reason is recorded. Required files never truncate silently. If required files exceed `max_files`, `max_bytes`, or an individual-file safety limit, collection fails and requests a reviewed policy override or explicit package/module split.

## Completeness And Manifest Provenance

Every capsule manifest records:

- adapter name and version;
- normalized effective policy and policy hash;
- focus package names and resolved workspace paths;
- included internal package names, paths, dependency edges, and reasons;
- external dependencies that were not collected;
- required and optional file classifications;
- export and entrypoint resolution results;
- exclusions and omissions with reasons;
- exact file hashes and sizes;
- canonical snapshot path and exact SHA when the capture is a supplement; and
- capsule and repository completeness statements.

The manifest uses explicit language:

```text
Capsule completeness: complete
Repository completeness: intentionally incomplete
```

`Capsule completeness: complete` is valid only when every required file in the declared scope is present and validated. Optional omissions do not invalidate the capsule, but they prevent broader claims.

The 15 existing PayPal JS canonical snapshots remain legacy evidence. Their manifests are not rewritten and they are never described as compliant capsules.

## First-Class Evidence Index

A version must retain one canonical snapshot and an ordered supplement inventory rather than a single replaceable evidence path:

```json
{
  "canonical_snapshot": "raw/github/paypal/paypal-js/snapshots/2026-07-18-10.1.1-3d72ac9",
  "supplements": [
    {
      "snapshot": "raw/github/paypal/paypal-js/snapshots/2026-07-20-10.1.1-3d72ac9-r1",
      "capture_revision": 1,
      "purpose": "npm-public-api-capsule",
      "policy_hash": "<sha256>"
    }
  ]
}
```

Supplement attachment never replaces canonical provenance. Index save, reload, reporting, packet generation, and validation must retain every attached supplement and its purpose. Existing version-index fields may remain readable during migration, but new writes must use one normalized evidence-set model.

## Packet Contract And Lifecycle

Packets are immutable after publication. Their deterministic identity includes the complete indexed evidence set used to generate required reading.

Every saved capsule file is required reading when that capsule is ingested. If the resulting packet exceeds its reading budget, packet creation fails and requests an explicit package/module split. The tool does not create a packet that cannot satisfy the project's full-read rule.

When an evidence set changes:

- an `awaiting-review` packet is replaced by a new packet ID and transitions to `superseded` with a replacement link;
- an `approved` or `ingesting` packet blocks evidence replacement until its state is resolved;
- an `ingested` packet remains permanent history and later evidence receives a separate supplement packet; and
- a `rejected` or `superseded` packet remains queryable history and cannot re-enter ingest.

The packet state event schema must represent the replacement packet ID without rewriting prior events. Replacement publication, evidence-index mutation, supplement promotion, and the superseding event form one rollback-safe transaction.

Baseline, delta, and comparison packets may include capsule evidence from their canonical snapshots. A later supplement packet records a purpose such as `npm-public-api-capsule`, `policy-upgrade`, or `query-deep-dive`.

## Normal Collection Flow

For a newly selected release, the collector:

1. resolves the ref to an exact SHA;
2. checks out that SHA in a temporary directory;
3. resolves the configured capsule policy and package closure;
4. stages default evidence and the complete capsule;
5. validates provenance, required files, hashes, safety, and budgets;
6. promotes one canonical immutable snapshot;
7. records its evidence set in the version index;
8. creates an immutable `awaiting-review` packet; and
9. emits one reconciled terminal collection event.

For a known SHA:

- the same evidence and policy hash produce `unchanged`;
- new release notes or aliases use the existing immutable supplement rules;
- a new capsule policy produces a `policy-upgrade` supplement; and
- no accepted raw snapshot is modified.

Collection may batch selected refs. It never approves or ingests a packet.

## Query-Driven Deep Dive

Query handling searches wiki pages and indexed raw evidence first. If no saved file covers the question, the workflow:

1. identifies the exact relevant version and recorded SHA;
2. checks out that SHA temporarily;
3. traces the relevant implementation, supporting files, and tests;
4. records a generated deep-dive request under `tracking/github/repos/<company>/<repo>/`;
5. creates an immutable same-SHA `query-deep-dive` `-rN` supplement;
6. attaches it to the version's evidence inventory;
7. creates an `awaiting-review` supplement packet; and
8. waits for user approval before full-read ingest or filed analysis.

The generated request records the question, repository, version, SHA, selected paths, selection reasons, policy or operator inputs, and resulting supplement. Query-specific paths do not become stable registry configuration.

`rules/query-and-synthesis.md` must be corrected to require an immutable same-SHA supplement. It must not instruct an agent to update an accepted raw stub or directory.

## Failure Protection, Retry, And Quarantine

Every failed attempt is rollback-safe: it leaves no promoted snapshot, evidence-index mutation, partial packet, misleading success event, or dirty reusable checkout. Retry state belongs in append-only generated tracking, not the registry.

Failures are classified as follows:

### Transient

Network timeouts, GitHub rate limits, temporary DNS failures, interrupted clones, and equivalent recoverable infrastructure failures receive the initial attempt plus at most three scheduled retries. Suggested delays are 15 minutes, two hours, and the next scheduled collection window.

### Deterministic Policy Or Evidence Failure

Missing required source roots, ambiguous packages, invalid registry policy, unsafe required paths, and exceeded required-evidence budgets enter `needs-policy-review` immediately. Identical inputs are not retried automatically because retrying cannot change the result.

### Unknown

An unclassified failure receives at most three retries. If its normalized fingerprint remains unchanged, the circuit breaker opens.

After the initial attempt and three unsuccessful retries, the specific repository/ref/SHA/policy combination enters `quarantined`:

```text
automatic retries: stopped
ingest eligibility: blocked
raw/index mutation: none
manual review: required
```

Other repositories and refs continue collecting. A quarantined item is never reported as unchanged or successful.

Append-only failure events live at:

```text
tracking/github/repos/<company>/<repo>/collection-failures.jsonl
```

Each event records repository, ref, resolved SHA when available, policy hash, failure category, normalized failure fingerprint, attempt number, timestamp, next action, and next retry time when applicable. Fingerprints exclude volatile text such as temporary paths and timestamps.

Quarantine resets only when the upstream SHA changes, the effective policy hash changes, meaningful registry configuration changes, or a user explicitly requests a reviewed retry.

## PayPal JS Legacy Migration

Migration of the 15 collected PayPal JS SHAs is a collection-only operation:

1. audit every SHA with `npm-public-api-v1` without promoting raw evidence;
2. stop the batch if any required capsule fails;
3. report included packages, file counts, byte totals, entrypoint results, and omissions;
4. after approval, promote one audited `-r1` capsule supplement for a single pilot SHA;
5. validate its first-class evidence index and replacement packet;
6. request approval before promoting the remaining 14 supplements;
7. supersede the original unapproved packets with capsule-aware replacements; and
8. leave every replacement in `awaiting-review`.

No migration step rewrites the canonical snapshots, approves a packet, updates wiki content, or begins ingest.

## Validation And Testing

Deterministic Python 3.9-compatible tests must cover:

- npm workspace array and accepted object forms;
- missing and duplicate focus package names;
- recursive internal dependencies and dependency cycles;
- internal dependencies, optional dependencies, and peer dependencies;
- exclusion of external and development dependencies;
- conditional and wildcard exports;
- `main`, `module`, `types`, `bin`, tracked wrappers, and generated targets;
- complete required source-directory selection;
- test, story, fixture, generated, vendor, and build exclusions;
- unsafe paths, symlinks, binary files, and individual-file limits;
- required versus optional omissions;
- deterministic file ordering and policy hashing;
- total file and byte budget failures;
- complete transaction rollback after every publication stage;
- first-class supplement persistence through index save and reload;
- packet required reading across canonical and supplemental evidence;
- replacement packet IDs and `superseded` transitions;
- blocking evidence replacement for approved or ingesting packets;
- query-driven supplements after an ingested packet;
- failure classification, retry counters, stable fingerprints, and quarantine reset;
- legacy canonical plus `-r1` validation; and
- correction of the query workflow's immutability conflict.

Network-dependent verification remains outside the default unit suite. Live rollout proceeds through unit tests and deterministic validators, one dry-run PayPal JS version, one approved pilot supplement, validation of that supplement and packet, and a separate approval before the remaining 14 versions.

## Acceptance Criteria

The design is implemented when:

- a registry row can select `npm-public-api-v1` without company-specific code;
- PayPal JS resolution includes `@paypal/react-paypal-js` and its required internal `@paypal/paypal-js` package while excluding unrelated workspaces;
- no successful capsule silently omits required source;
- manifests make scope, completeness, adapter version, and policy hash explicit;
- version indexes retain canonical and all supplemental evidence;
- immutable packets always enumerate their complete required-reading evidence;
- transient failures retry within bounds and repeated failures quarantine visibly;
- deterministic validation passes; and
- no collection or migration command starts wiki ingest.
