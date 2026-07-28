# Braintree Web Source Capsule

## Status

Approved design; awaiting implementation.

## Goal

Add `braintree/braintree-web` as the next registry-driven GitHub pilot. Retain
enough source to answer deep implementation questions while preserving the
existing approval-gated, serial full-read ingest boundary.

The pilot establishes `braintree-web@3.143.0` as the only historical baseline
and retains every future stable v3 release. It does not backfill v2.

## Repository Findings

`braintree/braintree-web` publishes one root package named `braintree-web`.
Tag `3.143.0` contains the current approved baseline. Unlike the prior
`v3.142.0` baseline tag, upstream omitted the `v` prefix for this release;
exact upstream tag spelling is part of the retained release identity. The
package's public implementation is organized under `src/` and includes:

- client and shared request infrastructure;
- Hosted Fields and card tokenization;
- 3D Secure;
- PayPal, PayPal Checkout, and PayPal Checkout v6;
- Venmo and Fastlane;
- Apple Pay, Google Pay, and Payment Request;
- local payments, SEPA, US bank accounts, and UnionPay;
- data collection and risk integrations; and
- shared frame, redirect, analytics, and error utilities.

Integration stories live under `.storybook/stories/`. The combined `src/` and
story trees contain about 329 tracked files and 2.06 MB of content before
standard repository context and category exclusions.

## Approaches Considered

### 1. Full production source plus stories

Selected. Collect all production source under `src/`, all integration stories
under `.storybook/stories/`, and the repository changelog and component
inventory.

This preserves source-level evidence across every payment module, shared
infrastructure, and intended integration scenarios. It remains within a
reviewed bounded capsule.

### 2. Selected payment modules only

Rejected. A smaller list focused on Hosted Fields, 3DS, PayPal, and Venmo would
omit shared client, frame, analytics, and utility behavior required to explain
those modules correctly. It would also create avoidable evidence gaps for
wallets and bank payments.

### 3. Full repository minus tests

Rejected. Build scripts, CI, publishing automation, and Storybook test
infrastructure add collection and ingest cost without improving payment
knowledge.

## Version Policy

The existing registry row will use:

```toml
[[repos.version_tracks]]
selector = "package:braintree-web@3"
backfill = "latest-stable"
future = "all-stable"
include_prerelease = false
```

The first collection must resolve package-qualified release
`braintree-web@3.143.0` from tag `3.143.0`. Later periodic collection selects
every stable v3 release newer than the highest retained version.

Prereleases and v2 releases remain out of scope. Historical releases below the
retained v3 baseline require a separate explicit request and review.

## Capsule Policy

The repository will use one `npm-tracked-source-v1` capsule:

```toml
[[repos.capsules]]
id = "braintree-web-public-source"
adapter = "npm-tracked-source-v1"
focus_packages = ["braintree-web"]
dependency_scope = "internal-runtime-closure"
changed_path_policy = "policy-bounded"
default_required_roots = ["src", ".storybook/stories"]
default_generated_target_paths = ["dist/"]
include_paths = ["CHANGELOG.md", "components.json"]
excluded_categories = ["tests", "fixtures"]
secret_detector = "text-secrets-v1"
max_file_bytes = 512000
max_capsule_files = 380
max_capsule_utf8_bytes = 3000000
max_packet_files = 420
max_packet_utf8_bytes = 3500000
```

`src/` is the complete production implementation boundary.
`.storybook/stories/` is retained because stories document supported component
states and merchant integration behavior. `.storybook/tests/`, Storybook
helpers, configuration, generated static assets, build scripts, and CI are
outside the required roots.

`CHANGELOG.md` provides repository release history. `components.json` records
the component inventory used by the build and documentation system.

Tests and fixtures remain excluded. The reusable test classifier must also
treat paths under `__mocks__/` as tests; this prevents
`src/lib/__mocks__/` from entering the capsule merely because it is nested
under `src/`. Stories remain eligible and are not classified as tests.

`changed_path_policy = "policy-bounded"` prevents changed files outside the
reviewed roots, exact includes, declared package targets, and internal runtime
closure from silently expanding future snapshots.

The 380-file and 3 MB capsule limits leave bounded headroom above the measured
baseline. Budget overflow must route to manual review rather than
automatically raising a limit.

## Collection Envelopes

The policy resolver and the published immutable snapshot are distinct,
approved evidence envelopes. The resolver capsule is the policy-audit result:
**327 files** and **2,149,720 UTF-8 bytes** at
`bae582d791026c143abb91c3bdcada92b8c060f6`. The published snapshot is the
immutable source record: **329 files** and **2,162,444 UTF-8 bytes** at the
same SHA. It includes the resolver capsule plus standard repository context
`LICENSE` (1,086 bytes) and `README.md` (11,638 bytes).

The published snapshot must preserve every resolver-selected record and may
add only the collector's standard root repository context. Published snapshot
counts are therefore not required to equal resolver capsule counts. Both
envelopes remain subject to the approved 380-file / 3,000,000-byte capsule
budget; this clarification does not expand policy roots, change exclusions, or
alter packet budgets.

## Collection Flow

1. Update the existing Braintree Web registry row with the approved version
   track and capsule policy, then set `enabled = true`.
2. Add focused tests for registry readiness, version selection, required
   source and story roots, `__mocks__` exclusion, and policy-bounded changed
   paths.
3. Run the offline GitHub validator and complete test suite.
4. Run a backfill dry run in isolated temporary state.
5. Require the dry run to discover only `braintree-web@3.143.0` and to remain
   within the reviewed file and byte budgets.
6. Run real backfill collection only after the dry-run evidence is reviewed.
7. Publish the immutable exact-SHA snapshot, release record, generated status,
   and one approval-gated work item.
8. Stop at `awaiting_approval`. Collection must not approve or ingest the
   work item.

## Ingest Design

The initial baseline receives a `full` recommendation. After user approval,
the ingest process must claim exactly one work item and read the complete
snapshot, release notes, repository changelog context, and relevant existing
wiki pages before editing.

The stable wiki authorities will be:

```text
wiki/sources/braintree/github/source-github-braintree-web.md
wiki/sources/braintree/github/changelog-github-braintree-web.md
wiki/companies/braintree.md
wiki/braintree-index.md
wiki/braintree-log.md
```

The cumulative source page owns durable architecture and implementation
knowledge. The changelog owns package-qualified chronological release history.
The first source increments Braintree's company `source_count` once; the
changelog does not create a second cumulative source count.

Braintree-owned adapters for PayPal, PayPal Checkout v6, Venmo, and Fastlane
remain in the Braintree source history. Delegated PayPal loader or runtime
claims must cross-link independently collected PayPal repository evidence.
The histories must not be merged.

Future stable v3 releases compare against the preceding retained release.
Contained changes may receive a delta recommendation. Public export,
initialization, security, payment behavior, or broad-change signals require a
full recommendation. The user remains the final authority on ingest mode.

## Failure Handling

- Invalid package identity, tag mismatch, missing required roots, unsafe paths,
  secret findings, or budget overflow route directly to manual review.
- Transient Git and network failures use the existing bounded retry policy.
- A failed collection publishes no partial snapshot or release record and does
  not alter accepted wiki knowledge.
- A dry run executes in isolated temporary state because the current CLI can
  record failure state even when `--dry-run` is supplied.
- No wiki page is created before a collected work item is explicitly approved
  for serial ingest.

## Validation

Implementation must pass:

- focused capsule policy, selection, registry, release, and work-item tests;
- the complete repository test suite;
- `python3 scripts/validate_github_collection.py`;
- targeted wiki validation after ingest; and
- `git diff --check`.

The collection report must state the selected file count, UTF-8 byte count,
retained story count, excluded test and fixture count, exact SHA, release
identity, and final queue state.

## Acceptance Criteria

- `braintree/braintree-web` is enabled with exactly one supported capsule and
  one package-qualified v3 version track.
- Backfill discovery selects only `braintree-web@3.143.0`.
- The snapshot contains full production source and Storybook stories while
  excluding tests, fixtures, `__mocks__`, and Storybook test infrastructure.
- The 327-file / 2,149,720-byte resolver capsule and the 329-file /
  2,162,444-byte published snapshot both stay at or below 380 files and
  3,000,000 UTF-8 bytes; their counts need not match because the latter
  includes standard repository context.
- The work item is package-qualified, exact-SHA-bound, and ends in
  `awaiting_approval`.
- No Braintree wiki ingest occurs without a separate user approval.
- Future stable v3 releases can generate deterministic comparisons and
  full/delta recommendations without expanding beyond the reviewed capsule
  policy.

## Out of Scope

- Braintree Web v2 history;
- `braintree/braintree-web-drop-in`, mobile SDKs, server SDKs, or utility
  repositories;
- automated or parallel wiki ingest;
- generated distribution bundles; and
- changes to existing immutable snapshots.
