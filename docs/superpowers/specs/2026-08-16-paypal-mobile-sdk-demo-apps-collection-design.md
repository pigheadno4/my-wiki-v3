# PayPal Mobile SDK Demo Apps Collection Design

**Date:** 2026-08-16
**Status:** Approved design, pending written-spec review

## Goal

Collect checkout-focused baselines for the independent PayPal Android and iOS SDK demo repositories. Preserve implementation evidence for native PayPal and card checkout, Payment Links, application return handling, and merchant-server boundaries without treating sample code as general product documentation.

## Repository identities

| Repository | Platform | Tracking | Priority |
| --- | --- | --- | --- |
| `paypal-examples/paypal-android-sdk-demo-app` | Android / Jetpack Compose | Default branch at exact SHA | Tier 1 |
| `paypal-examples/paypal-ios-sdk-demo-app` | iOS / SwiftUI | Default branch at exact SHA | Tier 1 |

Each repository remains an independent `commit`-tracked source with its own snapshot, packet, work item, cumulative source page, and changelog. No semantic package version will be fabricated for either demo application.

## Approved capsule boundaries

Both repositories use one `commit-tree-v1` capsule. Tests, fixtures, generated output, IDE metadata, signing material, dependency caches, CI, screenshots, and videos are excluded. Text-based stories or runtime resources remain eligible when they document supported application states or integration behavior.

### Android

Retain:

- application implementation and text runtime resources under `app/src/main`;
- the application manifest and app-level Gradle configuration;
- root Gradle settings, dependency catalog, and project properties needed to establish SDK and platform requirements;
- `README.md` and license or notice files when present.

Exclude `.idea`, test source sets, Gradle wrapper binaries, build output, the repository's demo keystore, screenshots, and videos. The keystore must not be copied even though upstream documents it as a demo credential.

### iOS

Retain:

- Swift application implementation and text runtime resources under `PayPalDemo`;
- Xcode project metadata needed to establish targets and SDK dependencies;
- application plist and entitlements needed to understand URL and associated-domain handling;
- `README.md` and license or notice files when present.

Exclude unit and UI tests, user-specific Xcode state, derived data, signing material, binary asset payloads, screenshots, and videos. Asset-catalog metadata may be retained only when it contributes integration-relevant configuration.

## Evidence and claim boundaries

The baselines may establish how these exact demo commits implement:

- PayPal web/native checkout orchestration;
- card checkout orchestration;
- Payment Links launch and application return handling;
- Android App Links and iOS Universal Links integration;
- browser/app lifecycle handoff;
- client-to-merchant-server calls and order completion;
- platform dependency and minimum-version declarations.

The samples do not independently prove merchant eligibility, regional availability, production readiness, security sufficiency, or behavior delegated to PayPal SDK and server repositories. Subscription behavior is included only when retained implementation supports it; README instructions alone remain documentation evidence and must not be presented as an implemented native subscription flow.

## Collection workflow

1. Add reviewed capsule policies to the two existing disabled registry entries and enable them.
2. Validate the registry before network collection.
3. Dry-run each repository independently and review selected paths, exclusions, secrets, and budgets.
4. Collect both default branches at exact full SHAs.
5. Publish two immutable snapshots and two full-review packets.
6. Review the packets together for Android/iOS scope parity while preserving separate repository identities.
7. Stop both work items at `awaiting_approval`. Collection must not approve, ingest, or edit wiki knowledge.

If a capsule omits checkout-critical code, includes signing material, exceeds budget, or reports an evidence gap, revise the policy and recollect before approval. Do not silently truncate the capsule.

## Serial ingest and paired analysis

After explicit packet approval, ingest one repository at a time. Read every required path in full, complete validation, and move the first work item to a terminal state before claiming the second.

Expected source outputs are:

```text
wiki/sources/paypal/github/source-github-paypal-android-sdk-demo-app.md
wiki/sources/paypal/github/changelog-github-paypal-android-sdk-demo-app.md
wiki/sources/paypal/github/source-github-paypal-ios-sdk-demo-app.md
wiki/sources/paypal/github/changelog-github-paypal-ios-sdk-demo-app.md
```

After both ingests, create one concise paired analysis covering checkout paths, state coordination, return-link handling, server responsibilities, SDK boundaries, and platform-specific differences. Every claim must identify its owning repository and exact commit; the analysis must not merge their evidence histories.

## Validation and success criteria

- Registry validation passes with both entries enabled and exactly one valid capsule each.
- Each dry run selects a bounded, nonempty checkout-focused packet with no secret, unsafe-path, or budget errors.
- The Android capsule excludes the demo keystore and both capsules exclude tests and binary media.
- Each real collection stops at `awaiting_approval` with no automatic ingest.
- `scripts/validate_github_collection.py` passes after both collections.
- Later checks compare selected path/hash evidence against the latest accepted snapshot and skip unchanged or excluded-only changes.

## Out of scope

- Historical commit backfill in the initial campaign.
- Building or executing either mobile application.
- Running sandbox payments.
- Treating sample behavior as canonical SDK or API documentation.
- Combining the two repositories into one source page or changelog.
- Automatically approving or batching their ingests.
