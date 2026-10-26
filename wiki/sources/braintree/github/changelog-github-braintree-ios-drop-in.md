---
title: "GitHub changelog: braintree/braintree-ios-drop-in"
type: source
date_ingested: 2026-08-13
date_updated: 2026-10-27
original_format: github-repo
raw_files:
  - "github/braintree/braintree-ios-drop-in/snapshots/2026-10-27-ae66bc6/manifest.json"
  - "github/braintree/braintree-ios-drop-in/snapshots/2026-08-13-d951d10/manifest.json"
tags: [braintree, ios, mobile-sdk, drop-in, changelog, github-repository]
---

## Overview

Chronological release synthesis for `braintree/braintree-ios-drop-in`. Cumulative implementation knowledge belongs in [[source-github-braintree-ios-drop-in]] and the linked immutable snapshots.

## `default-branch@ae66bc6` Documentation Delta (ingested 2026-10-27)

Approved serial delta `github-fce4c89c9e41ed166c99`: `d951d104ac960188824bda191be2f57c57351a31` -> `ae66bc646250711940d72834caab3c377d485879`. Upstream commit date 2026-04-23. This is an unreleased documentation ref, not a new package release; all `BraintreeDropIn@9.14.0` history below remains preserved.

- Adds September 1, 2026 deprecation/no-update and September 1, 2027 unsupported milestones, one-year processing-support wording and possible suspension after unsupported status. Directs migration to the modular SDK; no new payment API, dependency or compatibility claim.
- Updates v9 lifecycle table and retrospectively supplies v8's April 2023 unsupported date. Preserves original baseline Active/TBA evidence.
- Flags stale Inactive/active-development prose and September-versus-October dates in the retained iOS website guide. Reciprocal warnings in both sources and the iOS concept; neither snapshot proves current policy or an automatic payment cutoff.
- README is the sole changed retained file; 202 unchanged. All 406 prior/current file sizes/hashes/Git identities verified. Focused reading approved for manifests/shared context; full old/new README, comparisons and cumulative source/changelog reads. No build, payment test, registry change or raw modification.

Updated: existing iOS concept first, cumulative source/changelog, reciprocal website warning, company/catalog and logs. No new source count or cross-provider comparison. Details and located quotes: [[source-github-braintree-ios-drop-in]].

Evidence: [snapshot](raw/github/braintree/braintree-ios-drop-in/snapshots/2026-10-27-ae66bc6/manifest.json), [README](raw/github/braintree/braintree-ios-drop-in/snapshots/2026-10-27-ae66bc6/files/README.md), [comparison](tracking/github/repos/braintree/braintree-ios-drop-in/comparisons/default-branch/d951d10--ae66bc6/comparison.json), [patch](tracking/github/repos/braintree/braintree-ios-drop-in/comparisons/default-branch/d951d10--ae66bc6/diff.patch).

## `BraintreeDropIn@9.14.0` (2025-03-06)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `BraintreeDropIn` | Initial baseline | `9.14.0` | `d951d104ac960188824bda191be2f57c57351a31` | Full |

**Exact release change:** The release requires `braintree_ios` 5.27.0. No new payment method or public Drop-in flow is documented for `9.14.0`.

**Developer or merchant impact:** This package remains on the Braintree iOS 5.27 dependency line and supports iOS 12+, Xcode 15+, and Swift 5.9. Do not infer compatibility with or behavior from the independently retained `braintree-ios@7.9.0` source.

**Migration action:** Treat `9.14.0` as the first exact-SHA Drop-in baseline. Before moving the underlying modular SDK or adopting v7 behavior, verify a compatible Drop-in release or replace the prebuilt UI with a modular integration.

**Updated source sections:** Version and dependency boundary; selection and server handoff; payment methods; 3D Secure; UI boundary; release findings.

**Evidence boundary:** No prior exact-SHA iOS Drop-in snapshot exists in the wiki. Historical repository changelog entries provide context but are not retained source comparisons.

**Evidence:**

- Release manifest: `raw/github/braintree/braintree-ios-drop-in/releases/braintreedropin/9.14.0/2026-08-13/manifest.json`
- Release notes: `raw/github/braintree/braintree-ios-drop-in/releases/braintreedropin/9.14.0/2026-08-13/release-notes.md`
- Snapshot manifest: `raw/github/braintree/braintree-ios-drop-in/snapshots/2026-08-13-d951d10/manifest.json`
- Repository changelog: `raw/github/braintree/braintree-ios-drop-in/snapshots/2026-08-13-d951d10/files/CHANGELOG.md`
- Package manifest: `raw/github/braintree/braintree-ios-drop-in/snapshots/2026-08-13-d951d10/files/Package.swift`
