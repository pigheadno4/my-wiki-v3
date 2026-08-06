# Adyen iOS Stable Baseline Collection Design

**Date:** 2026-08-01
**Status:** Approved design; implementation and collection not yet started

## Objective

Enable `Adyen/adyen-ios` in the generic GitHub release collector and collect one immutable, source-rich baseline for the latest stable release. The pilot must support future implementation-level queries without mirroring tests, generated documentation, binary frameworks, or media assets.

Collection ends at `awaiting_approval`. Wiki ingest remains a separate user-approved, serial, full-read operation.

## Release Policy

- Repository identity: `adyen/adyen-ios`.
- Package identity: `adyen-ios`.
- Baseline release: `adyen-ios@5.25.1`.
- Tag: `5.25.1`.
- Exact tag SHA observed during design: `5f6779b31299e3067de3a5279a816f3b8d2fbdf3`.
- Version track: stable major version 5.
- Backfill: latest stable release, pinned to `5.25.1` for this pilot.
- Future collection: every newer stable v5 release.
- Prereleases: excluded. In particular, `6.0.0-alpha.1` is not part of this pilot.
- Stable v6: requires a reviewed v6 version track and a full-ingest major-transition recommendation.

The collector must resolve the tag again during collection and stop for manual review if it no longer resolves to the observed SHA.

## Registry Design

Update the existing inventory row in `tracking/github/repo-registry.toml` rather than creating a second repository entry:

- set `enabled = true`;
- retain weekly frequency, tier 1 priority, mobile SDK type, and semantic-tag strategy;
- add one package-qualified v5 version track; and
- add one `tagged-tree-v1` capsule named `adyen-ios-public-source`.

The capsule uses the existing configured-repository-path behavior. This pilot does not add a new adapter or language parser.

## Evidence Capsule

### Included evidence

At tag `5.25.1`, retain all tracked Swift implementation files from the SDK product modules and Demo application. The inspected tree contains 630 SDK Swift files and 49 Demo Swift files, for 679 Swift files totaling approximately 2.1 MB.

The SDK product scope is:

- `Adyen` core;
- `AdyenActions`;
- `AdyenCard`;
- `AdyenCardScanner`;
- `AdyenCashAppPay`;
- `AdyenComponents`;
- `AdyenDelegatedAuthentication`;
- `AdyenDropIn`;
- `AdyenEncryption`;
- `AdyenSession`;
- `AdyenSwiftUI`;
- `AdyenTwint`; and
- `AdyenWeChatPay`.

The Demo scope includes its Swift configuration helpers, Session and Advanced Flow examples, networking, models, presentation delegates, UIKit screens, and SwiftUI screens. Configuration source files that refer to environment-provided credentials are included because they contain integration behavior but no credential values.

Also retain these repository-level integration and compatibility files when present at the tag:

- `README.md`;
- `MIGRATION.md`;
- `Package.swift`;
- `Adyen.podspec`;
- `Cartfile`;
- `LICENSE`; and
- privacy manifests associated with retained products.

Registry roots must be source-bearing directories rather than broad product roots that also contain binary assets. Current module-root Swift files are explicit includes. The implementation must verify that the selected set contains every expected tracked `.swift` file in scope.

### Excluded evidence

Exclude:

- `Tests/` and `AdyenCardScannerTests/`;
- test fixtures and snapshots;
- generated API documentation under `docs/`;
- `Adyen.docc/` generated or reference documentation;
- screenshots, PNGs, PDFs, localization assets, and Xcode asset catalogs;
- `XCFramework/` and other binary framework artifacts;
- CI, formatting, release-automation, and repository-maintenance files; and
- Demo `.xcconfig` secret templates or local secret files.

No excluded file is silently treated as implementation evidence. If a later query requires one, collect it as an immutable supplement tied to the baseline SHA.

### Change coverage

The registry policy must remain bounded but must not silently miss a newly introduced Swift module or source root. A future changed `.swift` path outside the configured policy must appear as unclassified or as an evidence gap, forcing manual policy review before delta ingest.

## Collection Flow

1. Add and validate the reviewed registry policy.
2. Run targeted collector and registry tests.
3. Run `collect --repo adyen/adyen-ios --mode backfill`.
4. Resolve `adyen-ios@5.25.1`, its exact tag SHA, and release-note evidence.
5. Build the snapshot in temporary storage.
6. Validate source selection, budgets, UTF-8 content, hashes, and secret findings.
7. Publish one immutable exact-SHA snapshot and one package-qualified release record.
8. Generate the canonical ingest packet and status output.
9. Stop at `awaiting_approval`.

Collection must report the selected file count and bytes, excluded categories, evidence gaps, unclassified changes, packet recommendation, and immutable evidence paths. Collection does not edit wiki pages.

## Ingest Design

The first accepted release is a baseline and therefore receives a `full` recommendation. User approval is still required before lifecycle approval or ingest.

After approval, ingest exactly one work item. Read the complete packet, complete snapshot, release record, release notes, and relevant existing Adyen wiki context before editing. The ingest creates or updates:

- `wiki/sources/adyen/github/source-github-adyen-ios.md` for durable repository knowledge;
- `wiki/sources/adyen/github/changelog-github-adyen-ios.md` for package-qualified release history;
- `wiki/adyen-index.md`;
- the Adyen company page; and
- the appropriate company and root operation logs required by current ingest rules.

The cumulative source page must cover package products, Drop-in versus Components, Session and Advanced Flow boundaries, supported payment-method modules, integration requirements, delegated repositories, and explicit evidence gaps. Later stable v5 releases compare against this baseline and may receive delta recommendations when packet evidence allows.

## Failure Handling

Use the existing GitHub collection protections:

- publish no partial snapshot or queue item after failure;
- preserve previously accepted evidence;
- retry transient failures up to three times per run;
- record exhausted failures as `collection_failed`; and
- move repeated or policy-blocking failures to `needs_manual_review`.

A tag mismatch, selected binary file, invalid UTF-8 file, secret finding, missing required source, or capsule budget overflow blocks publication and requires review.

## Verification

Before collection:

- registry parsing and policy tests pass;
- the selected paths cover all 679 expected Swift files at the pinned tag;
- excluded tests, generated docs, images, localization assets, secret configuration files, and binaries are absent; and
- capsule and packet budgets can contain the selected text evidence.

After collection:

- `python3 scripts/validate_github_collection.py` passes;
- status shows exactly one new Adyen iOS work item at `awaiting_approval`;
- snapshot and release manifests resolve to the exact SHA and package-qualified version;
- all manifest hashes match; and
- no wiki file has changed.

## Success Criteria

The pilot succeeds when `adyen-ios@5.25.1` has one validated immutable release record, one validated source-rich snapshot, and one review packet awaiting user approval, with no tests, generated documentation, media, binary frameworks, credential files, or automatic wiki edits included.
