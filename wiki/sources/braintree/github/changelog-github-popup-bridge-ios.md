---
title: "GitHub changelog: braintree/popup-bridge-ios"
type: source
date_ingested: 2026-08-27
original_format: github-repo
raw_files:
  - "github/braintree/popup-bridge-ios/snapshots/2026-08-27-00256b4/manifest.json"
tags: [braintree, popup-bridge, ios, venmo, changelog, github-repository]
---

## Overview

Chronological release synthesis for `braintree/popup-bridge-ios`. Cumulative implementation knowledge belongs in [[source-github-popup-bridge-ios]] and the linked immutable snapshot.

## `PopupBridge@3.1.0` (2026-06-24)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `PopupBridge` | Initial baseline | `3.1.0` | `00256b4b8c58367287fe35a442a33cd7c010a94f` | Full |

**Exact release change:** Adds `init(webView:returnURLScheme:prefersEphemeralWebBrowserSession:)` for Venmo app switch. When the Venmo app is installed, the provided merchant scheme becomes the return prefix exposed to the web SDK and the native callback scheme.

**Developer or merchant impact:** A WebView-based Braintree Venmo integration can deep-link from the Venmo app back to the native merchant application. The merchant must register and consistently use the custom return scheme and allowlist the Venmo application scheme. This release does not enable Venmo for an account or change server-side payment processing.

**Migration action:** Existing browser-only PopupBridge usage can keep `POPPopupBridge(webView:)`. Venmo app-switch integrations should register an application-owned URL scheme, pass it to the new initializer, allowlist `com.venmo.touch.v2`, and ensure the web integration uses `window.popupBridge.getReturnUrlPrefix()`.

**Updated source sections:** Baseline and installation; WebView-to-browser flow; Venmo app switch; PayPal and Braintree Web boundary; analytics and privacy; migration history and documentation conflicts.

**Evidence boundary:** This is the first retained exact-SHA PopupBridge iOS baseline, so there is no comparison manifest. Historical changelog entries establish migration context but do not provide byte-level evidence for earlier releases.

**Evidence:**

- Release manifest: `raw/github/braintree/popup-bridge-ios/releases/popupbridge/3.1.0/2026-08-27/manifest.json`
- Release notes: `raw/github/braintree/popup-bridge-ios/releases/popupbridge/3.1.0/2026-08-27/release-notes.md`
- Snapshot manifest: `raw/github/braintree/popup-bridge-ios/snapshots/2026-08-27-00256b4/manifest.json`
- Repository changelog: `raw/github/braintree/popup-bridge-ios/snapshots/2026-08-27-00256b4/files/CHANGELOG.md`
- Runtime implementation: `raw/github/braintree/popup-bridge-ios/snapshots/2026-08-27-00256b4/files/Sources/PopupBridge/POPPopupBridge.swift`

## Historical Major-Version Context

- `3.0.0` raises the minimum to iOS 16, Xcode 16.2, and Swift 5.10; adds ephemeral browser-session control; and exposes Venmo installation state.
- `2.1.0` injects bridge JavaScript into every frame and adds the retained blank privacy manifest.
- `2.0.0-beta1` converts the library to Swift, replaces `SFSafariViewController` with `ASWebAuthenticationSession`, removes `POPPopupBridgeDelegate`, and removes the global return-scheme and open methods.

These entries are retained changelog context. Version-specific implementation claims for those releases require separate snapshots.
