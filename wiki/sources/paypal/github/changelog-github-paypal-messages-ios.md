---
title: "GitHub changelog: paypal/paypal-messages-ios"
type: source
date_ingested: 2026-08-12
date_updated: 2026-10-07
original_format: github-repo
raw_files:
  - "github/paypal/paypal-messages-ios/snapshots/2026-10-07-e3ee08c/manifest.json"
  - "github/paypal/paypal-messages-ios/snapshots/2026-08-13-fdd1868/manifest.json"
  - "github/paypal/paypal-messages-ios/snapshots/2026-08-12-432d6b8/manifest.json"
tags: [paypal, ios, swift, messaging, pay-later, changelog, github-repository]
---

## Overview

Package-qualified release ledger for `paypal/paypal-messages-ios`. Durable integration and architecture guidance belongs in [[source-github-paypal-messages-ios]].

## `paypal-messages-ios@2.0.0` - Change Set `e3ee08c` (2026-09-10)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `paypal-messages-ios` | `1.2.0` | `2.0.0` | `e3ee08c5310096457ea709f49b8b22b6b385a916` | Full, additive |

Collected and ingested October 7, 2026. All 66 assigned retained files were read completely; six changed and 60 are hash-identical. The major upgrade raises the minimum from iOS 14 to iOS 15 in retained SPM and CocoaPods configuration. The README retains Swift 5.8+ and Xcode 14.3+. Apps that must support iOS 14 cannot adopt v2 merely by updating the dependency version.

The release README now includes the Braintree-only disclaimer previously retained at untagged `fdd1868`: a Braintree account and integrated Braintree SDK are required; PPCP SDK integrations are unsupported. This is the first retained managed release containing that policy, not proof of a new runtime account check. The earlier untagged evidence remains below.

SPM's binary URL/checksum, the podspec and `BuildInfo.version` advance to `2.0.0`. Existing message/modal requests and analytics therefore carry the new version value. The `Environment.swift` edit only combines Swift pattern bindings; no endpoint or query change is shown. Configuration, views, delegates, modal, caching, analytics implementation and demos remain unchanged, including the `setConfig` omission of environment and partner identity. No new checkout or messaging API was established.

Migration: raise the app's supported iOS target, verify the Braintree prerequisites and test the exact installed artifact. Carthage metadata, Xcode project files and a test mock are classified exclusions among twelve upstream changes; Xcode-wide target changes remain release-note-backed rather than independently read project evidence. Binary contents and device behavior were not verified.

Updated sections: source Overview, Evidence Boundary, Requirements, new Major Version 2, preserved Major Version 1, Version History and Raw Sources; existing Pay Later/iOS SDK concepts, company/catalog, and a dated addendum to the historical iOS/Android analysis. All prior knowledge and source counts remain preserved.

Evidence:
- `raw/github/paypal/paypal-messages-ios/releases/paypal-messages-ios/2.0.0/2026-10-07/manifest.json`
- `raw/github/paypal/paypal-messages-ios/releases/paypal-messages-ios/2.0.0/2026-10-07/release-notes.md`
- `raw/github/paypal/paypal-messages-ios/snapshots/2026-10-07-e3ee08c/manifest.json`
- `raw/github/paypal/paypal-messages-ios/snapshots/2026-10-07-e3ee08c/files/README.md`
- `raw/github/paypal/paypal-messages-ios/snapshots/2026-10-07-e3ee08c/files/Package.swift`
- `raw/github/paypal/paypal-messages-ios/snapshots/2026-10-07-e3ee08c/files/PayPalMessages.podspec`
- `tracking/github/repos/paypal/paypal-messages-ios/comparisons/paypal-messages-ios/1.2.0--2.0.0/comparison.json`
- `tracking/github/repos/paypal/paypal-messages-ios/comparisons/paypal-messages-ios/1.2.0--2.0.0/diff.patch`

## Untagged `default-branch@fdd1868` (`develop`) - Braintree Policy Boundary (2026-06-01)

| Ref | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `develop` | released `1.2.0` tree | untagged documentation commit | `fdd18681f486a3b2f1c60e3c47f8669f55a73a96` | Delta |

The only changed path is `README.md`. It removes the recommendation to integrate through the PayPal iOS SDK and states that the component is intended for the Braintree SDK only, requiring both a Braintree account and Braintree SDK integration; PPCP SDK integrations are unsupported.

This is a repository documentation-policy change, not a semantic release or code change. At its August ingest, no collected package release carried this evidence. The subsequently retained `2.0.0` README now carries it in a tagged release; runtime account enforcement remains unproven.

Evidence: `raw/github/paypal/paypal-messages-ios/snapshots/2026-08-13-fdd1868/manifest.json` and `tracking/github/repos/paypal/paypal-messages-ios/comparisons/default-branch/432d6b8--fdd1868/comparison.json`.

## `paypal-messages-ios@1.2.0` - Change Set `432d6b8` (2026-03-25)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `paypal-messages-ios` | Managed baseline | `1.2.0` | `432d6b832714b2615106c3f2a748ac61654d8bbd` | Full |

The exact release adds `language_rendered` analytics and bold styling for server message substrings marked with `%bold%`. Merchant impact is primarily analytics fidelity and message presentation; no checkout-payment API was added.

The exact source also exposes a version-qualified configuration risk: `PayPalMessageViewModel.updateConfig()` omits `environment`, `merchantID`, and `partnerAttributionID`. A full config replacement therefore does not replace those fields through `setConfig`; see [[source-github-paypal-messages-ios]] and [[analysis-paypal-messages-ios-vs-android]].

Evidence: `raw/github/paypal/paypal-messages-ios/releases/paypal-messages-ios/1.2.0/2026-08-12/manifest.json`, release notes, and the exact-SHA snapshot manifest.

## `paypal-messages-ios@1.1.0` - Cumulative Context (2026-02-27)

The retained upstream changelog records language/locale parameters, requested-language analytics, an authorization header for logging, and modal/dependency fixes. This is cumulative history inside the `1.2.0` snapshot, not a separately collected managed release.

## `paypal-messages-ios@1.0.0` - Cumulative Context (2024-05-14)

The first stable history includes message/modal accessibility, interaction gating until render, merchant-profile caching by client and merchant ID, richer response errors, integration identity, analytics/schema revisions, privacy-manifest work, and development-environment controls. These facts are historical context from the cumulative changelog; the current API description is grounded in the `1.2.0` source capsule.

## Evidence Boundary

- `1.2.0` and `2.0.0` have managed immutable release records and source capsules.
- Earlier entries summarize the `CHANGELOG.md` retained at the `1.2.0` SHA and are not complete file-level comparisons.
- Package presence and stable tags do not establish merchant eligibility or buyer offer availability.

## Raw Sources

- `raw/github/paypal/paypal-messages-ios/snapshots/2026-10-07-e3ee08c/manifest.json`
- `raw/github/paypal/paypal-messages-ios/releases/paypal-messages-ios/2.0.0/2026-10-07/manifest.json`
- `raw/github/paypal/paypal-messages-ios/releases/paypal-messages-ios/2.0.0/2026-10-07/release-notes.md`
- `tracking/github/repos/paypal/paypal-messages-ios/comparisons/paypal-messages-ios/1.2.0--2.0.0/comparison.json`
- `tracking/github/repos/paypal/paypal-messages-ios/comparisons/paypal-messages-ios/1.2.0--2.0.0/diff.patch`
- `raw/github/paypal/paypal-messages-ios/snapshots/2026-08-13-fdd1868/manifest.json`
- `raw/github/paypal/paypal-messages-ios/snapshots/2026-08-13-fdd1868/files/README.md`
- `tracking/github/repos/paypal/paypal-messages-ios/comparisons/default-branch/432d6b8--fdd1868/comparison.json`
- `tracking/github/repos/paypal/paypal-messages-ios/comparisons/default-branch/432d6b8--fdd1868/diff.patch`
- `raw/github/paypal/paypal-messages-ios/snapshots/2026-08-12-432d6b8/manifest.json`
- `raw/github/paypal/paypal-messages-ios/releases/paypal-messages-ios/1.2.0/2026-08-12/manifest.json`
- `raw/github/paypal/paypal-messages-ios/releases/paypal-messages-ios/1.2.0/2026-08-12/release-notes.md`
- `raw/github/paypal/paypal-messages-ios/snapshots/2026-08-12-432d6b8/files/CHANGELOG.md`
