# Braintree Mobile Drop-in Baselines Design

**Date:** 2026-08-13

## Goal

Collect and ingest current stable baselines for the independent Braintree iOS and Android Drop-in repositories, then produce a cross-platform analysis that supports detailed integration and version-aware queries without merging their histories with the parent Braintree mobile SDKs.

## Repository and release identities

| Repository | Package identity | Initial baseline | Priority |
| --- | --- | --- | --- |
| `braintree/braintree-ios-drop-in` | `BraintreeDropIn` | `BraintreeDropIn@9.14.0` | Tier 1 |
| `braintree/braintree-android-drop-in` | `drop-in` | `drop-in@6.17.0` | Tier 1 |

Both repositories use `semver-tags`, weekly collection, and `tagged-tree-v1`. Their release histories remain independent from `braintree/braintree_ios` and `braintree/braintree_android`.

## Capsule policy

Use a public-source capsule for each repository.

### iOS retained evidence

- Complete implementation under `Sources/BraintreeDropIn`.
- Public headers and runtime resources under that source root.
- Integration demo code under `Demo/Application`, excluding UI tests and binary assets.
- `README.md`, `CHANGELOG.md`, `DEVELOPMENT.md`, and `LICENSE`.
- `Package.swift`, `BraintreeDropIn.podspec`, and relevant Xcode project metadata.

Exclude unit/UI tests, generated documentation, screenshots and image catalogs, MockVenmo test support, sample packaging smoke tests, CI, release automation, resolved dependency lockfiles, and unrelated development tooling.

### Android retained evidence

- Complete implementation and runtime resources under `Drop-In/src/main`.
- Useful integration demo code and manifest under `Demo/src/main`.
- `README.md`, `CHANGELOG.md`, `DEVELOPMENT.md`, `CONTRIBUTING.md`, `ACKNOWLEDGEMENTS.md`, `LICENSE`, and `v6_MIGRATION_GUIDE.md`.
- Root and module Gradle metadata, `gradle.properties`, and `settings.gradle`.

Exclude tests, generated API HTML, screenshots, vendored APKs and binaries, CI, release automation, signing material, Gradle wrapper binaries, and unrelated tooling.

Stories or demo states that document supported integration behavior remain eligible. Test fixtures do not become evidence merely because they resemble examples.

## Collection workflow

1. Add reviewed version tracks and capsule policies to the two existing disabled registry entries, then enable them.
2. Validate the registry before network collection.
3. Dry-run each baseline independently.
4. Collect both baselines and publish immutable exact-SHA snapshots, release records, comparison metadata where applicable, and approval packets.
5. Review both packets together for scope consistency, hashes, exclusions, evidence gaps, and parent-SDK dependency boundaries.
6. Stop with both work items at `awaiting_approval`. Collection must not approve, ingest, or edit wiki knowledge.

If either capsule exceeds its reviewed budget or excludes a checkout-critical public file, revise the registry policy and recollect before approval. Do not silently truncate.

## Serial ingest workflow

After explicit packet approval:

1. Ingest iOS as one complete SHA work item.
2. Complete validation and mark iOS terminal before claiming Android.
3. Ingest Android as one complete SHA work item.
4. Preserve one cumulative source page and one changelog per repository.
5. Update existing Braintree concepts, company page, provider index, and logs only when supported by the complete retained evidence.

The initial baselines use full ingest. Later contained releases may use delta ingest after packet review.

## Wiki outputs

Create or update:

```text
wiki/sources/braintree/github/source-github-braintree-ios-drop-in.md
wiki/sources/braintree/github/changelog-github-braintree-ios-drop-in.md
wiki/sources/braintree/github/source-github-braintree-android-drop-in.md
wiki/sources/braintree/github/changelog-github-braintree-android-drop-in.md
wiki/analyses/analysis-braintree-drop-in-ios-vs-android.md
```

The repository source pages own implementation and integration behavior. The changelogs own package-qualified release history. The paired analysis is created only after both serial ingests complete.

## Paired analysis scope

Compare:

- UI launch and result-handling models;
- client-token and tokenization-key authorization;
- payment-method nonce return and server handoff;
- cards, PayPal, Venmo, Apple Pay or Google Pay, and 3D Secure surfaces;
- vaulted payment-method display and management;
- parent Braintree SDK compatibility;
- migration, deprecation, browser/app-switch, and platform lifecycle risks;
- customization and accessibility boundaries.

The analysis must distinguish Drop-in orchestration from payment processing. It may cite parent SDK sources for delegated behavior, but it must identify the owning repository and must not merge package versions or evidence histories.

## Validation and success criteria

- Registry validation succeeds with both entries enabled.
- Each dry run reports a bounded, nonempty capsule with no secret or path errors.
- Each real collection stops at `awaiting_approval` with no evidence gaps or unclassified retained changes.
- Snapshots exclude tests, generated docs, images, and binaries while retaining complete public implementation and useful demos.
- Serial ingest reads every assigned path in full and passes focused wiki validation.
- `scripts/validate_github_collection.py` passes after collection and after each ingest.
- The final analysis links both independent source pages and changelogs and states all version and parent-SDK boundaries explicitly.

## Out of scope

- Collecting every historical major version in this first baseline campaign.
- Executing mobile builds or payment transactions.
- Treating demo presence as merchant eligibility or payment-method availability.
- Automatically approving or batching the two ingests.
- Combining Drop-in and parent SDK repositories into one source page or changelog.
