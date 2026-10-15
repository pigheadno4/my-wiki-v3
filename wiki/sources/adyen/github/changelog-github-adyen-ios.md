---
title: "GitHub changelog: Adyen/adyen-ios"
type: source
date_ingested: 2026-10-15
original_format: github-repo
raw_files:
  - "github/adyen/adyen-ios/snapshots/2026-10-14-da34749/manifest.json"
  - "github/adyen/adyen-ios/snapshots/2026-08-01-5f6779b/manifest.json"
tags: [adyen, ios, swift, mobile-sdk, changelog, github-repository]
---

## Overview

Chronological release synthesis for `Adyen/adyen-ios`. Cumulative implementation knowledge belongs in [[source-github-adyen-ios]] and the linked immutable snapshots.

## `adyen-ios@5.26.0` (2026-10-07)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `adyen-ios` | `5.25.1` | `5.26.0` | `da347498d07b843e5af3f9eb871376514ffdf38c` | Additive full, approved focused reading |

Collected 2026-10-14; ingested 2026-10-15. All older release findings and baseline implementation knowledge are preserved.

**Payment and value changes:**

- Apple Pay in Drop-in forwards the partial-payment order from `PreApplePayComponent` to its inner Apple Pay Component. Existing submission includes the order with payment details, fixing the missing-order remaining-amount flow described after gift-card use. This is not a new payment method or proof of payment success.
- CVC formatting now limits the sanitized field value, not only the display. Single-character over-limit edits are rejected; multi-character replacements pass through sanitization. Amex uses four digits, other/unknown brands three. Brand-bound validators use the helper, while the default standalone validator retains its three-to-four-digit range.
- Source-derived finding, absent from the release highlights: amount conversions now use an uppercase currency-code table with system fallback rather than locale-dependent fraction digits. Conversion signatures retain the now-unused locale parameter; localized display remains. Existing arithmetic/round-toward-zero behavior is not a new rounding guarantee.

**Presentation and demo changes:** Safe-area toolbar constraints, form content/frame guides, explicit margins, and keyboard clipping/0.15-second shorter-frame settling accompany the release's iPhone Duo support announcement. Inactive title/underline defaults become light `#757575` and dark `#8E8E93`, without replacing custom colors or changing generic label/separator defaults. SwiftUI demo scene URLs now cover initial connection and subsequent callbacks, including conditional Cash App Pay notification forwarding. The UIKit AppDelegate adds scene configuration, but the new UIKit SceneDelegate and plist changes are excluded; complete UIKit return wiring is not established.

**Distribution:** Release notes announce `5.26.0` as the final CocoaPods release, with SPM/Carthage afterward. Same-tag README installation text and the podspec still include CocoaPods. The discrepancy is retained in [[source-github-adyen-ios]] and [[adyen-ios-sdk]]; it does not prove this release is unavailable through CocoaPods or establish a global CocoaPods shutdown date. Minimum requirements remain iOS 12, Xcode 15 and Swift 5.7.

**Migration and checks:** Plan future distribution upgrades; regression-test gift-card remainder-to-Apple-Pay order propagation, Amex/non-Amex CVC typing/paste/value alignment, currency conversion versus display locale, adaptive layouts/keyboard changes, custom colors and scene-return integration. No build, device, accessibility or payment tests were run here.

**Updated source sections:** `5.26.0` reading/evidence boundary; Apple Pay order propagation; card security-code handling; currency conversion; adaptive presentation/app returns; distribution discrepancy. Older `5.25.1` sections remain intact.

**Reading/validation:** Approved full mode with focused reading of all 23 changed retained files and affected prior code/dependencies. Verified all 1,375 current/prior file hashes and sizes; 666 files unchanged. Large manifest/comparison inventories checked mechanically. Every upstream path has a disposition (23 retained, 7,920 policy exclusions); no packet evidence gaps or unclassified changes. The generated security-review heuristic is not an advisory finding.

**Evidence:**

- Release record: `raw/github/adyen/adyen-ios/releases/adyen-ios/5.26.0/2026-10-14/manifest.json`
- Release notes: `raw/github/adyen/adyen-ios/releases/adyen-ios/5.26.0/2026-10-14/release-notes.md`
- Snapshot: `raw/github/adyen/adyen-ios/snapshots/2026-10-14-da34749/manifest.json`
- Comparison and retained-code diff: `tracking/github/repos/adyen/adyen-ios/comparisons/adyen-ios/5.25.1--5.26.0/comparison.json` and `tracking/github/repos/adyen/adyen-ios/comparisons/adyen-ios/5.25.1--5.26.0/diff.patch`
- Apple Pay forwarding: `raw/github/adyen/adyen-ios/snapshots/2026-10-14-da34749/files/AdyenDropIn/Components/PreApplePayComponent.swift`
- CVC sanitizer: `raw/github/adyen/adyen-ios/snapshots/2026-10-14-da34749/files/AdyenCard/Formatters/CardSecurityCodeFormatter.swift`
- Currency conversion: `raw/github/adyen/adyen-ios/snapshots/2026-10-14-da34749/files/Adyen/Formatters/AmountFormatter.swift`
- Exact additional implementation links and four grounding excerpts: [[source-github-adyen-ios]].

## `adyen-ios@5.25.1` (2026-06-04)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `adyen-ios` | Initial baseline | `5.25.1` | `5f6779b31299e3067de3a5279a816f3b8d2fbdf3` | Full |

**Important finding:** The release fixes a layout issue that could affect Component form rendering when Adyen iOS is embedded through a cross-platform SDK.

**Developer or merchant impact:** React Native or Flutter wrapper integrations may receive corrected native form sizing or presentation. The release note does not identify a specific form or source file, so narrower claims are not supported by this baseline.

**Migration action:** No API migration or breaking change is documented. Wrapper integrations should regression-test their native Component forms after updating.

**Updated source sections:** platform and distribution; context and integration modes; Session and advanced flow; cards and storage; Apple Pay and actions; native app handoffs; analytics, privacy, and cross-platform wrappers.

**Evidence boundary:** This is the first retained Adyen iOS baseline, so no prior exact-SHA comparison exists. The layout fix comes from the upstream release note; broader SDK architecture comes from the complete retained source capsule at the same SHA.

**Evidence:**

- Release manifest: `raw/github/adyen/adyen-ios/releases/adyen-ios/5.25.1/2026-08-01/manifest.json`
- Release notes: `raw/github/adyen/adyen-ios/releases/adyen-ios/5.25.1/2026-08-01/release-notes.md`
- Snapshot manifest: `raw/github/adyen/adyen-ios/snapshots/2026-08-01-5f6779b/manifest.json`
- Cross-platform identity: `raw/github/adyen/adyen-ios/snapshots/2026-08-01-5f6779b/files/Adyen/Helpers/CheckoutPlatformParams.swift`
- Form infrastructure: `raw/github/adyen/adyen-ios/snapshots/2026-08-01-5f6779b/files/Adyen/UI/Form/`
