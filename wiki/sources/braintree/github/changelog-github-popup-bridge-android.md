---
title: "GitHub changelog: braintree/popup-bridge-android"
type: source
date_ingested: 2026-08-27
original_format: github-repo
raw_files:
  - "github/braintree/popup-bridge-android/snapshots/2026-08-27-f306541/manifest.json"
tags: [braintree, popup-bridge, android, browser-switch, changelog, github-repository]
---

## Overview

Chronological release synthesis for `braintree/popup-bridge-android`. Cumulative implementation knowledge belongs in [[source-github-popup-bridge-android]] and the linked immutable snapshot.

## `popup-bridge@5.3.0` (2026-07-30)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `popup-bridge` | Initial baseline | `5.3.0` | `f30654168b997ea1dd95ebc61901582ae00bebb0` | Full |

**Exact release change:** Updates Android Gradle Plugin to `8.13.2` and compile/target SDK to API 37.

**Developer or merchant impact:** Applications consuming the stable artifact retain the same PopupBridge protocol and payment boundary. Repository maintainers and source builders need a toolchain compatible with AGP 8.13.2 and API 37. The release does not add a payment method, change merchant eligibility, or alter server-side processing.

**Migration action:** Treat this as the first exact-SHA baseline. Integrators should register an application deep link, construct `PopupBridgeClient` with a `PopupBridgeWebViewClient`, preserve any existing WebViewClient through the wrapper delegate, and forward activity return intents through `handleReturnToApp()`.

**Updated source sections:** Baseline and build requirements; application setup; browser-switch and return flow; activity lifecycle; WebView and JavaScript interface; Venmo detection; analytics; release history; documentation conflicts.

**Evidence boundary:** No prior exact-SHA PopupBridge Android snapshot exists in the wiki, so this baseline has no comparison manifest. Historical changelog and migration entries provide context but are not separately retained version proof.

**Evidence:**

- Release manifest: `raw/github/braintree/popup-bridge-android/releases/popup-bridge/5.3.0/2026-08-27/manifest.json`
- Release notes: `raw/github/braintree/popup-bridge-android/releases/popup-bridge/5.3.0/2026-08-27/release-notes.md`
- Snapshot manifest: `raw/github/braintree/popup-bridge-android/snapshots/2026-08-27-f306541/manifest.json`
- Repository changelog: `raw/github/braintree/popup-bridge-android/snapshots/2026-08-27-f306541/files/CHANGELOG.md`
- Root build: `raw/github/braintree/popup-bridge-android/snapshots/2026-08-27-f306541/files/build.gradle`

## Historical v5 Context

- `5.2.0` updates Browser Switch to `3.5.1` and compile SDK to API 36.
- `5.1.0` fixes the WebViewClient being silently overridden.
- `5.0.0` moves to `ComponentActivity`, removes the public `deliverPopupBridgeResult` method and lifecycle observer, adds Android 13 build support, updates Browser Switch to 3.0.0, and validates Venmo installation.

> [!warning] v5 guide contradiction
> The retained v5 migration guide says result delivery became internal through a lifecycle observer, directly conflicting with the v5 changelog and exact `5.3.0` runtime/demo. Integrations at this baseline must explicitly call `handleReturnToApp()`.

These historical entries guide migration analysis. Version-specific implementation claims for `5.0.0` through `5.2.0` require separate snapshots.
