# Tagged Native GitHub Collection Design

**Date:** 2026-07-30
**Profile:** Tagged native SDK repository
**Validation pilots:** `stripe/stripe-ios` and `stripe/stripe-android`
**Status:** Approved

## Goal

Add one reusable collection profile for a repository that publishes one native SDK under semantic-version tags but does not expose an npm workspace. Validate it against both Stripe native SDK repositories before treating it as reusable.

The initial collection retains:

- `stripe-ios@26.4.1`, the latest stable Stripe iOS release and the exact iOS dependency used by `@stripe/stripe-react-native@0.72.0`; and
- `stripe-android@23.13.1`, the latest stable Stripe Android release and the exact Android dependency used by `@stripe/stripe-react-native@0.72.0`.

Collection creates immutable raw evidence and review packets only. It does not edit wiki knowledge, approve work items, or start ingest.

## Observed Repository Differences

The design is based on the exact release trees at:

| Repository | Release | Commit SHA | Files | Primary source | Test-related files |
| --- | --- | --- | ---: | ---: | ---: |
| `stripe/stripe-ios` | `26.4.1` | `d9252fd0a4a6d369fa45bb06f74c4e818c914f91` | 10,213 | 2,403 Swift | approximately 1,365 |
| `stripe/stripe-android` | `23.13.1` | `dc874ce7c62dd433664ec4e312efeb9300c21795` | 13,339 | 4,840 Kotlin and 19 Java | approximately 4,551 |

Both releases use annotated tags. The iOS tag object is `e61afc0e1677560f6d1238411e74b85e1a54e15f`; the Android tag object is `db6e5112d67f6de4cb2e5048fbecd251d9f23d10`. Immutable snapshots and work items use the peeled commit SHA, while release records retain the upstream tag identity.

Stripe iOS is organized as framework roots such as `StripePaymentSheet`, `StripePayments`, `StripeApplePay`, and `StripeConnect`. Its distribution declarations are `Package.swift`, `modules.yaml`, and module podspecs.

Stripe Android is organized as Gradle modules such as `paymentsheet`, `payments-core`, `connect`, and `crypto-onramp`. Its distribution declarations are `settings.gradle`, root and module build files, and module API signature files.

The release mechanics are shared, but the source layout is not. One adapter therefore owns tag and evidence mechanics while each registry row owns its module paths and limits.

## Profile Contract

A repository can reuse this profile when:

- it publishes one logical SDK release per selected repository tag;
- stable tags resolve deterministically as semantic versions, with or without a leading `v`;
- one configured release identity can own the retained repository paths;
- public API, implementation, examples, and build metadata can be expressed as literal repository-relative files or roots;
- tests, fixtures, generated output, and automation can be excluded without removing the selected public source of truth; and
- the bounded capsule can be read serially during a later approved ingest.

Reuse requires a reviewed registry policy, fixture coverage for any new path convention, a smoke collection, offline validation, and user review of the generated packet. It does not require another repository-specific design document unless the repository violates this contract.

Repositories with multiple independently versioned deliverables, non-semantic release identities, generated-only public APIs, or an evidence set that cannot be bounded require a separate adapter decision.

## Shared Adapter

Add `tagged-tree-v1` beside `npm-tracked-source-v1`.

The adapter owns:

- exact semantic-version tag resolution, including optional leading `v`;
- one package-qualified release identity for the selected tag;
- literal configured root and include selection from the exact Git tree;
- changed-path classification inside the configured policy boundary;
- standard context selection, hashing, secret detection, and hard budgets; and
- the existing snapshot, release-record, comparison, packet, retry, and approval lifecycle.

The adapter does not:

- parse Swift, Kotlin, CocoaPods, Swift Package Manager, or Gradle source;
- execute builds or dependency managers;
- infer module dependencies;
- select a whole repository;
- automatically widen a capsule after a budget failure; or
- contain branches for Stripe or another provider.

To preserve existing downstream contracts, the adapter emits a synthetic single-package workspace:

- package name equals the configured focus release identity, such as `stripe-ios`;
- package root is the repository root;
- owned paths are the configured policy paths, not every repository file;
- dependency edges and external dependencies are empty; and
- workspace resolver identity is `single-tagged-tree-v1`.

For `tagged-tree-v1`, `dependency_scope` is `configured-repository-paths`. NPM package-manifest discovery, workspace closure, declared JavaScript targets, and generated NPM target handling do not run.

The effective policy hash includes the adapter name, resolver identity, normalized roots and includes, exclusions, budgets, secret allowlist, and release identity. Historical validation uses the policy embedded in the snapshot.

## Registry And Release Policies

Both repositories remain separate Tier 1 rows and use package-qualified tracks.

Stripe iOS:

```toml
[[repos.version_tracks]]
selector = "package:stripe-ios@26"
backfill = "latest-stable"
future = "all-stable"
include_prerelease = false
pinned_versions = ["26.4.1"]
```

Stripe Android:

```toml
[[repos.version_tracks]]
selector = "package:stripe-android@23"
backfill = "latest-stable"
future = "all-stable"
include_prerelease = false
pinned_versions = ["23.13.1"]
```

The current latest stable release equals the pinned React Native dependency for both repositories, so each initial collection creates one release item. Recollection of the exact tag SHA and release-note hash skips it.

A future major version requires a reviewed new major track and receives a full-ingest recommendation. The current-major track must not silently absorb a major transition.

## Bounded Capsule Policy

Neither full repository is eligible. Initial snapshots target no more than 400 upstream evidence files. The hard limits are:

| Limit | Value |
| --- | ---: |
| Per file | 512,000 bytes |
| Snapshot files | 500 |
| Snapshot UTF-8 content | 5,000,000 bytes |
| Packet files | 550 |
| Packet UTF-8 content | 6,000,000 bytes |

A smoke packet containing more than 450 required-reading files returns to capsule-policy review and is not eligible for ingest approval, even when it remains below the absolute packet limit. Hard-limit violations fail collection before publication.

Both capsules include:

- `README.md`, `CHANGELOG.md`, `MIGRATING.md`, `LICENSE`, and `VERSION`;
- package, module, and build declarations needed to identify the distributed SDK surface;
- public API declarations;
- a bounded implementation cross-section for PaymentSheet, direct payment APIs, the platform wallet, and core result or error behavior; and
- selected source examples that demonstrate supported integration flows.

Both capsules exclude:

- tests, test utilities, fixtures, snapshots, and screenshot assets;
- CI, release automation, lint configuration, and developer tooling;
- generated documentation and generated build output;
- vendored dependencies; and
- unrelated example assets or project metadata.

Stories remain eligible where a future native repository uses them as maintained integration evidence.

### Stripe iOS Policy

The reviewed policy is built from:

- Swift Package Manager, CocoaPods, and module declarations;
- the public PaymentSheet surface;
- Stripe Payments API bindings and payment-handler entrypoints;
- Stripe Apple Pay public source;
- selected core types required to understand those entrypoints; and
- selected PaymentSheet and non-card payment example source.

Specialized frameworks such as Connect, Identity, Financial Connections, Issuing, and crypto onramp retain their public entrypoints and distribution declarations in the baseline. Their complete internal implementations are outside the standard capsule.

The policy must exclude paths such as `Tests/`, module test targets, UI tests, snapshot tests, and `StripePaymentsTestUtils`. At `26.4.1`, `StripePaymentsTestUtils/Resources` alone contains more than 4,000 files and must never enter the capsule through a broad `StripePayments/` root.

### Stripe Android Policy

The reviewed policy is built from:

- root Gradle settings, dependency declarations, and selected module build files;
- public API signature files;
- the public PaymentSheet API and a bounded implementation cross-section;
- direct payments and core result or error entrypoints;
- Google Pay entrypoints; and
- selected `paymentsheet-example` and general example source.

Specialized modules such as Connect, Identity, Financial Connections, card scan, payment-method messaging, and crypto onramp retain their public API signatures, build declarations, and principal entrypoints in the baseline. Their complete internal implementations are outside the standard capsule.

The policy must exclude `src/test`, `src/androidTest`, test-support modules, screenshot trees, and generated documentation. At `23.13.1`, `paymentsheet/src/test/snapshots` alone contains more than 2,200 files and must never enter the capsule.

## Evidence Gaps And Supplements

The source page produced by a later ingest must describe this as a bounded public API and implementation capsule, not a complete repository mirror.

When a future query requires an implementation file outside the accepted capsule:

1. identify the exact source SHA already linked to the relevant release;
2. collect the missing file or bounded directory as an immutable supplement;
3. validate and review the supplement;
4. read the supplement in full; and
5. update the same cumulative source page with the newly grounded finding.

A supplement does not rewrite the original snapshot or merge another repository's evidence history into the source page.

## Collection And Failure Flow

The implementation and pilot sequence is:

1. add adapter parsing, selection, and validation coverage;
2. add Swift-framework and Gradle-module fixtures;
3. configure and enable both repository rows;
4. run all focused and full offline tests;
5. collect `stripe/stripe-ios` first;
6. validate and review its packet size, exclusions, unclassified paths, and evidence gaps;
7. collect `stripe/stripe-android` only after the iOS collection is structurally valid;
8. validate and compare both packets; and
9. stop with both work items in `awaiting_approval`.

Collection fails before publishing queue state when:

- the selected tag is missing, ambiguous, or does not resolve to the expected release identity;
- a configured required path is absent;
- a selected blob is unsafe, non-text where text is required, oversized, or secret-blocked;
- the snapshot or packet exceeds a hard budget;
- a changed production path inside a configured module boundary is unclassified; or
- packet or immutable-evidence validation fails.

No failure may silently truncate evidence, approve a work item, or edit wiki pages. Existing retry and terminal-failure rules remain unchanged.

## Testing

Focused tests must prove:

- plain and `v`-prefixed semantic tags map to the configured release identity;
- the synthetic single-package workspace is deterministic;
- configured roots and exact includes select only tracked blobs;
- test and fixture exclusions work for both Xcode-style and Gradle-style paths;
- missing roots, unsafe paths, secret findings, and hard budgets fail closed;
- changed paths inside and outside policy boundaries receive deterministic dispositions;
- policy hashes change when adapter-relevant configuration changes;
- existing NPM repositories retain byte-compatible behavior; and
- snapshot, release, comparison, work-item, packet, and status validation accepts both pilots.

Run the existing GitHub unit suite, the focused new adapter tests, registry validation, and `scripts/validate_github_collection.py`. Actual collection is a network smoke test; all published artifact validation remains offline and deterministic.

## Expected Wiki Targets

No wiki files change during collection. After separate explicit approvals, serial ingest updates:

Stripe iOS:

- `wiki/sources/stripe/github/source-github-stripe-ios.md`
- `wiki/sources/stripe/github/changelog-github-stripe-ios.md`

Stripe Android:

- `wiki/sources/stripe/github/source-github-stripe-android.md`
- `wiki/sources/stripe/github/changelog-github-stripe-android.md`

Each source page remains independent and cumulative. Shared updates may also affect `wiki/companies/stripe.md`, the corresponding native SDK concept, `wiki/stripe-index.md`, and `wiki/log.md`. The Stripe React Native source links to the native repositories as delegated evidence; it does not absorb their release histories.

## Success Criteria

The profile is ready for reuse when:

- both exact releases resolve from their real tag forms;
- the NPM adapter and its existing repositories remain unchanged in behavior;
- each native release creates one immutable bounded snapshot and one release record;
- each packet stays within hard limits, has at most 450 required-reading files, and contains no unclassified changes or blocking evidence gaps;
- test, fixture, snapshot, and generated-documentation trees remain excluded;
- offline GitHub validation passes;
- both work items stop in `awaiting_approval`; and
- no wiki file changes before explicit ingest approval.

If either real repository cannot fit the bounded policy without losing its selected public contract, collection stops for policy review. The implementation must not solve that failure by mirroring the repository or weakening serial full-read ingest.
