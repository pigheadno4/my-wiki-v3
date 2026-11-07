# Adyen React Native Collection Review - 2026-11-07

## Approval Boundary and Identity

User approved the recheck and findings before ingestion. Existing future-stable collection completed without registry, capsule or budget changes. No approve/claim/ingest command, wiki edit, build, device/payment test, commit or push. Unrelated Stripe/index/log changes are preserved.

- Latest stable discovered: @adyen/react-native@2.14.0, published 2026-11-02T15:20:39Z.
- Exact SHA: 08e15ac5e38d925780895093844edc7ca4cdb811.
- Work item: github-01b194e7c644e7ff1f60, awaiting_approval, approved_mode null.
- Snapshot: raw/github/adyen/adyen-react-native/snapshots/2026-11-07-08e15ac/manifest.json.
- Release: raw/github/adyen/adyen-react-native/releases/react-native/2.14.0/2026-11-07/manifest.json and release-notes.md in that directory.
- Comparison: tracking/github/repos/adyen/adyen-react-native/comparisons/react-native/2.13.0--2.14.0/comparison.json, comparison.md and diff.patch.
- Packet: tracking/github/repos/adyen/adyen-react-native/ingest-packets/github-01b194e7c644e7ff1f60/packet.json and packet.md.
- Source/changelog unchanged; last ingested remains 2.13.0 on 2026-10-21.

## Findings Before Ingestion

### Native Dependencies

android/dependencies.gradle raises Adyen Android 5.20.0 -> 5.22.0; the wrapper podspec raises Adyen iOS 5.26.0 -> 5.27.0. Those exact native versions already have independent wiki histories from the preceding approved ingests. A wrapper pin does not duplicate native implementation evidence, verify downloaded artifacts or automatically upgrade a merchant application.

### Android Compatibility and Migration

The release notes and retained docs/Compatibility.md announce Android support from React Native 0.79 and Expo 54, with app compile/target API 36 and AGP 8.9.1 or newer. Bare React Native guidance uses Kotlin 2.3.0. Expo 54 requires the documented 2.2.20 exception; Expo 55-57 uses 2.3.0. The guide says not to lower Expo 58+'s existing compile SDK 37 to 36. RN 0.79 needs explicit app-level AGP 8.9.1 guidance; later template defaults are described separately.

The Kotlin plugin classpath must actually use the configured version; raising an unused kotlinVersion alone is insufficient according to the retained guide. These are version-qualified upstream compatibility claims, not independent build/AAR inspection. Native Android repository catalog/compiler settings, wrapper defaults and consumer minimums remain distinct.

Important qualifications to preserve in an ingest:

- The tag's package.json still declares react-native >=0.76.0 and optional expo >=52, while README/compatibility guidance raises Android support to 0.79/54. Do not treat peer-range satisfaction as proof of supported Android compatibility. The tag uses the known 2.0.0-local.1 release placeholder; the published npm manifest/generation script was not independently inspected, so do not claim published npm metadata is definitively wrong.
- android/build.gradle still contains its existing AGP 8.7.3 buildscript declaration, below the newly documented consuming-app minimum. It does not enforce the minimum solely by changing that literal; preserve the documented app configuration and resolution boundary instead of claiming the wrapper automatically raises every app's AGP.
- The compatibility guide retains legacy unsupported RN 0.73/0.72 notes below the new requirements. Those are not supported configurations for this release. Upstream claims of a tested RN/Expo matrix are not tests executed by this collection.
- The native iOS distribution notice does not establish wrapper Swift Package Manager support; its retained integration still uses a podspec/CocoaPods. Native and wrapper distribution histories remain separate.

### AGP 9 and Expo Plugin Wiring

android/build.gradle applies kotlin-android only when no kotlin extension is already registered, addressing the AGP-9 built-in-Kotlin collision path. This is a bounded configuration guard, not verification of every AGP/React Native combination.

New src/plugin/setKotlinGradlePlugin.ts rewrites a matching unversioned Kotlin plugin classpath to follow android.kotlinVersion. withAdyenAndroid.ts hooks it through withProjectBuildGradle only for Groovy. Versioned/parameterized declarations are left unchanged by the regex; Kotlin DSL and arbitrarily formatted Gradle declarations are not established automatic-fix coverage. Excluded upstream test text is visible in the comparison, but those tests were not collected as retained source or executed here.

### iOS Embedded Card Styling

CardComponentViewProxy now assigns cardConfig.style from AdyenAppearanceLoader.findStyle()?.formComponent through its internal appearance provider, falling back to FormComponentStyle(). Retained Customization.md explicitly extends the existing AdyenAppearance formComponent style to embedded CardView. This is a native appearance-provider fix, not a new React style prop or claim that arbitrary React CSS-like styling customizes native card fields.

The CardView.tsx change extracts its existing width into StyleSheet and keeps the dynamic native-reported height. ApplePayModule.swift and ApplePayConfiguration.ts changes are formatting-only; no new Apple Pay callback, funding feature or return-buyer API is established by those hunks.

## Evidence and Validation

- Prior snapshot: 305 files / 667,888 bytes. Current: 306 files / 677,072 bytes. One added, 12 modified, 293 unchanged, none removed. All 611 retained file sizes, SHA-256 and Git blob identities pass.
- All 36 upstream dispositions reconcile: 13 retained, 23 intentional exclusions; no packet gaps/unclassified changes. Registry policy excludes tests/CI/lockfiles and generated reports; no silent scope expansion.
- Collection-time required reading: 22 paths / 339,068 bytes. Pure full-mode preflight validates 315 paths / 958,275 bytes without approving or claiming the item.
- Review covered complete packet Markdown and retained diff, parsed JSON metadata/inventories, full compatibility/build/dependency/podspec/package metadata, complete plugin and card-proxy/CardView implementations, customization guide and release notes. This is not a full pre-ingest read of every assigned/current/prior source file or the whole upstream repository.
- Seeded 305 verified prior raw blobs only into the collector's temporary Git object store to avoid redundant lazy fetches; no accepted evidence or collector code was changed. Collector and helper completed, no background process remains.
- Offline GitHub validation retains exactly 13 unrelated historical errors, none for this item; one pending work item. No global all-green claim. Canonical wrapper source/changelog and registry remain byte-identical to HEAD.

## Recommendation

The script recommends delta/high from a contained-minor/payment heuristic. Recommend a user-approved full additive override because this release changes supported Android baselines and the consumer toolchain migration, while updating both native SDK pins. Preserve all 2.12.0/2.13.0 knowledge, document the compatibility/metadata qualifications and keep repositories independent.

Recommend focused reading for that full ingest: fully read all 13 added/changed retained files, affected prior/dependency code, release/comparison evidence and cumulative wiki history; mechanically verify unchanged files, generated manifests and duplicated diff content. Full mode remains full. Next action requires separate ingest approval; no commit/push is authorized.
