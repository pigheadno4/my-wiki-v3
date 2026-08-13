---
title: "GitHub changelog: braintree/braintree-ios-drop-in"
type: source
date_ingested: 2026-08-13
original_format: github-repo
raw_files:
  - "github/braintree/braintree-ios-drop-in/snapshots/2026-08-13-d951d10/manifest.json"
tags: [braintree, ios, mobile-sdk, drop-in, changelog, github-repository]
---

## Overview

Chronological release synthesis for `braintree/braintree-ios-drop-in`. Cumulative implementation knowledge belongs in [[source-github-braintree-ios-drop-in]] and the linked immutable snapshots.

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
