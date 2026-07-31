# Braintree Android Collection Design

**Date:** 2026-07-31
**Repository:** `braintree/braintree_android`
**Initial release:** `braintree-android@5.30.0`
**Status:** Revised design; pending written-spec review

## Goal

Add `braintree/braintree_android` as the next registry-driven GitHub collection. The initial baseline retains the latest stable v5 release, `braintree-android@5.30.0`, and future periodic collection retains every later stable v5 release.

The collection must preserve enough production source to answer detailed SDK integration and implementation questions without mirroring the full repository. It creates immutable raw evidence, comparisons, a review packet, and an approval-gated work item. It does not edit wiki knowledge or start ingest.

## Repository Findings

The official `5.30.0` tag resolves to commit `51f183a48557d0fd00eefa541712df0c4f21ee28`. The release is a single native Android SDK version rather than an independently versioned package workspace, so it fits the existing `tagged-tree-v1` profile.

The production SDK is divided into 14 Gradle modules:

- `AmericanExpress`
- `BraintreeCore`
- `Card`
- `DataCollector`
- `GooglePay`
- `LocalPayment`
- `PayPal`
- `PayPalMessaging`
- `SEPADirectDebit`
- `ShopperInsights`
- `SharedUtils`
- `ThreeDSecure`
- `UIComponents`
- `Venmo`

The reviewed production capsule is 388 readable files and 1,171,992 UTF-8 bytes. `UIComponents` is the largest module because its maintained Kotlin and XML resources define required PayPal, Venmo, and card-field UI behavior. Its `card_fields_cc_discover.png` file is 773,661 bytes and cannot enter the text-evidence capsule because it exceeds the 512,000-byte per-file limit and is not UTF-8. The repository has no dedicated public API signature files analogous to the Stripe Android `.api` files, so production `src/main` content is the primary implementation evidence.

Release `5.30.0` removes the Visa Checkout module, deprecates related configuration fields, adds public suspend APIs across multiple payment modules, updates Android build and SDK levels, and changes UI component button sizing. These changes make it a useful complete v5 baseline.

## Approaches Considered

### 1. Complete production capsule

Selected. Collect every readable production source and resource, each module's build and runtime configuration, and bounded root documentation and build context. Use split `UIComponents` roots to omit its single unsupported binary asset without weakening shared collector safety checks.

This preserves cross-module behavior and public implementation evidence while excluding tests, generated documentation, demos, and repository tooling. The measured capsule remains below the existing serial-read review threshold.

### 2. Selected payment modules only

Rejected. Restricting the capsule to PayPal, Venmo, cards, and 3D Secure would omit shared client, browser-switch, analytics, data-collection, UI, and result behavior needed to explain those integrations correctly.

### 3. Full repository minus tests

Rejected. Demo code, generated Dokka output, build automation, and development tooling would materially increase collection and ingest cost without becoming authoritative SDK production evidence.

## Version Policy

The registry row will remain Tier 1 and use one package-qualified major track:

```toml
[[repos.version_tracks]]
selector = "package:braintree-android@5"
backfill = "latest-stable"
future = "all-stable"
include_prerelease = false
pinned_versions = ["5.30.0"]
```

The initial backfill must select only `braintree-android@5.30.0`. Future collection selects every stable v5 release newer than the highest retained version. Recollection of an unchanged tag SHA and release-note hash is skipped.

Prereleases and v4 history are outside this pilot. A future v6 release requires a reviewed major-version track and receives a full-ingest recommendation; the v5 track must not absorb it automatically.

## Capsule Policy

The repository will use one `tagged-tree-v1` capsule with:

- focus package `braintree-android`;
- dependency scope `configured-repository-paths`;
- changed-path policy `policy-bounded`;
- 13 complete production module `src/main` roots;
- split Kotlin and XML roots plus the manifest for `UIComponents`;
- all 14 module `build.gradle` files and the three production `proguard.pro` files; and
- exact root documentation, migration, dependency, license, settings, and build files.

The exact root context is:

- `README.md`
- `CHANGELOG.md`
- `v5_MIGRATION_GUIDE.md`
- `v4_MIGRATION_GUIDE.md`
- `v4.9.0+_MIGRATION_GUIDE.md`
- `APP_LINK_SETUP.md`
- `DEPENDENCIES.md`
- `LICENSE`
- `settings.gradle`
- `build.gradle`
- `gradle.properties`

The split `UIComponents` policy uses these required roots:

- `UIComponents/src/main/java`
- `UIComponents/src/main/res/drawable`
- `UIComponents/src/main/res/layout`
- `UIComponents/src/main/res/values`

It includes `UIComponents/src/main/AndroidManifest.xml` as an exact file. This retains every maintained text source and resource in the module while keeping the unsupported PNG outside the selected evidence set.

The capsule excludes:

- `Demo` and `TestUtils` modules;
- all `src/test` and `src/androidTest` trees;
- generated Dokka content under `docs/` and the `DokkaRestrictToPlugin` build plugin;
- `UIComponents/src/main/res/drawable-xxhdpi/card_fields_cc_discover.png`, which is a binary presentation asset rather than readable implementation evidence;
- fixtures, snapshots, generated build output, and vendored dependencies;
- CI, release automation, and development tooling; and
- binaries and other non-text assets unless a reviewed production resource is required to understand SDK behavior.

Stories remain eligible in the reusable policy when a repository maintains them as integration evidence. This repository does not require a separate story root for the initial capsule.

## Budgets And Review Threshold

The capsule uses the shared tagged-native hard limits:

| Limit | Value |
| --- | ---: |
| Per file | 512,000 bytes |
| Snapshot files | 500 |
| Snapshot UTF-8 content | 5,000,000 bytes |
| Packet files | 550 |
| Packet UTF-8 content | 6,000,000 bytes |

The measured 388-file readable baseline stays below the 450-file required-reading review threshold. A smoke packet with more than 450 required-reading files returns to capsule-policy review and is not eligible for approval, even if it remains under the absolute packet limit. Hard-limit failures must not be solved by silent truncation or automatic budget increases.

## Collection Flow

1. Extend the existing inventory row with the approved v5 version track and capsule configuration, then enable it.
2. Add focused fixtures and tests for Braintree's Gradle module layout, required roots, retained XML resources, the excluded binary PNG path, tag resolution, and policy-bounded changed paths.
3. Run focused tests, the complete offline GitHub test suite, registry validation, and `scripts/validate_github_collection.py`.
4. Run a backfill dry run in isolated temporary state.
5. Require the dry run to select only `braintree-android@5.30.0`, resolve the exact commit, include all required production roots, and remain within the reviewed budgets.
6. Review the dry-run inventory and exclusions before real collection.
7. Publish one immutable exact-SHA snapshot, one package release record, generated status evidence, and one review packet. Generate a comparison only when a prior retained release exists.
8. Stop the work item in `awaiting_approval`.

Collection does not approve the work item, call `next-ingest`, or edit the wiki.

## Ingest Boundary And Wiki Targets

The initial baseline receives a `full` recommendation. A separate user approval is required before serial ingest. The ingest must read the complete accepted snapshot and packet evidence one file at a time and preserve all later historical findings in the same cumulative repository source page.

Expected stable targets are:

- `wiki/sources/braintree/github/source-github-braintree-android.md`
- `wiki/sources/braintree/github/changelog-github-braintree-android.md`

The source page owns durable architecture, module responsibilities, public integration behavior, compatibility, migration findings, and evidence gaps. The changelog owns the package-qualified chronological release history. Later stable v5 releases append their history and update affected durable knowledge; they do not replace older validated findings.

Possible shared updates after ingest include `wiki/companies/braintree.md`, an appropriate Braintree Android concept page, `wiki/braintree-index.md`, and `wiki/braintree-log.md`. Those edits are determined by the ingest concept audit, not by collection.

## Later Release Decisions

Future stable v5 releases compare against the preceding retained release. A contained patch or minor change may receive a delta recommendation only when every changed production path is classified, required evidence is present, and no full-ingest signal applies.

A baseline, major-version transition, incompatible public API change, capsule-policy change, missing prior snapshot, or unbounded security impact receives a full recommendation. Full ingest adds the new release knowledge to the cumulative source; it does not rewrite the page as latest-only. The user remains the final authority on full or delta mode.

## Evidence Gaps And Supplements

The eventual source page must identify the evidence as a bounded production capsule rather than a complete repository mirror. If a future query requires an excluded source path:

1. identify the exact retained release SHA;
2. collect the missing file or bounded directory as an immutable supplement;
3. validate and review the supplement;
4. read it in full; and
5. update the same cumulative source page with the grounded finding.

A supplement does not modify the accepted snapshot and does not merge evidence from another repository into Braintree Android's history.

## Failure Handling

- Missing or ambiguous tags, invalid release identity, missing required roots, unsafe paths, secret findings, or budget overflow route to manual review.
- Transient Git, network, and filesystem-read failures use the existing bounded retry policy.
- A failed attempt publishes no partial snapshot or release record and does not alter accepted wiki knowledge.
- After three consecutive failed runs, automatic retry stops in `needs_manual_review` until the cause is corrected and an explicit retry is requested.
- Existing valid immutable evidence remains reusable after a later failure.

## Validation

Implementation must prove:

- exact tag `5.30.0` resolves to package-qualified release `braintree-android@5.30.0` and the expected peeled commit;
- all 14 production modules are represented by readable source, resource, build, and manifest evidence, and required root context is retained;
- Demo, TestUtils, tests, generated docs, CI, and tooling remain excluded;
- required production XML and UI resources remain eligible;
- the oversized non-UTF-8 Discover card PNG remains outside the selected evidence set without weakening shared safety checks;
- changed paths inside and outside the configured policy receive deterministic dispositions;
- missing roots, unsafe paths, secrets, and hard-budget violations fail closed;
- existing tagged and NPM repository behavior remains unchanged; and
- snapshot, release, comparison, packet, status, and work-item validation passes.

The final collection report must state the exact release identity, tag, commit SHA, file count, UTF-8 byte count, module coverage, excluded-category counts, required-reading count, unclassified-change count, evidence-gap count, and final queue state.

## Acceptance Criteria

- `braintree/braintree_android` is enabled with exactly one supported capsule and one package-qualified v5 track.
- Backfill discovery selects only `braintree-android@5.30.0` at commit `51f183a48557d0fd00eefa541712df0c4f21ee28`.
- The immutable snapshot includes readable evidence for all 14 production modules and required root context while excluding the unsupported binary PNG, tests, demos, generated documentation, CI, and tooling.
- The snapshot and packet remain within hard budgets and at or below 450 required-reading files.
- No changed retained production path is unclassified and no blocking evidence gap remains.
- Offline GitHub validation passes.
- The generated work item stops in `awaiting_approval`.
- No wiki file changes before separate explicit ingest approval.

## Out Of Scope

- Braintree Android v4 and earlier release history;
- prerelease versions;
- `braintree/braintree-android-drop-in` and other Braintree repositories;
- full repository mirroring;
- automatic work-item approval or wiki ingest; and
- changing the shared `tagged-tree-v1` contract beyond fixture coverage required for Braintree's path conventions.
