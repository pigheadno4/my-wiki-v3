---
title: "GitHub: braintree/popup-bridge-android"
type: source
date_ingested: 2026-08-27
original_format: github-repo
raw_files:
  - "github/braintree/popup-bridge-android/snapshots/2026-08-27-f306541/manifest.json"
tags: [braintree, popup-bridge, android, webview, paypal, venmo, browser-switch, github-repository]
---

## Overview

`popup-bridge@5.3.0` is the first retained exact-SHA baseline for Braintree's Android WebView popup bridge. It exposes a native JavaScript interface to an embedded checkout, opens popup URLs through Braintree Browser Switch, and returns deep-link data to the parent page.

PopupBridge is a transport layer for an existing web integration. It does not create a PayPal or Braintree payment session, produce a payment-method nonce, grant payment-method eligibility, or process the resulting transaction.

## Baseline and Build Requirements

The retained Maven package resolves to SHA `f30654168b997ea1dd95ebc61901582ae00bebb0` and was released on 2026-07-30. It is published as `com.braintreepayments.api:popup-bridge:5.3.0`.

The exact Gradle build sets minimum Android API 23 and compile/target API 37. Library source targets Java and Kotlin JVM 11, uses Kotlin `2.1.10`, and depends on Braintree Browser Switch `3.5.1`, AndroidX AppCompat and Lifecycle Runtime, and DataStore Preferences.

## Application Setup

The merchant application owns the deep-link destination activity and URL scheme. Its manifest must register a browsable, exported activity with a matching scheme; the README requires lowercase scheme characters because Android scheme matching is case-sensitive.

The application constructs `PopupBridgeClient` with:

- a `ComponentActivity` containing the checkout WebView;
- the WebView;
- the registered return URL scheme; and
- a `PopupBridgeWebViewClient`, optionally wrapping the application's existing `WebViewClient`.

Construction enables JavaScript, adds a JavaScript interface named `popupBridge`, and sets the supplied wrapper as the WebView's client. The application should retain both the bridge client and wrapper for the activity lifetime.

## Browser-Switch and Return Flow

The exact flow is:

1. JavaScript calls `window.popupBridge.open(url)`.
2. `PopupBridgeClient` creates Browser Switch options with request code 1, the popup URL, and the merchant return scheme.
3. A successful start returns a serialized pending request, which the bridge persists in Android DataStore.
4. The external browser or wallet deep-links back to the merchant activity.
5. The activity passes the return intent to `handleReturnToApp()`.
6. Browser Switch completes the persisted request as success, failure, or no result.
7. PopupBridge calls `window.popupBridge.onComplete(error, payload)`, or the optional `onCancel()` callback for cancellation.

The success payload contains the callback path, query parameters, and fragment. Native completion accepts only a return URI whose host is `popupbridgev1`; Browser Switch owns the pending-request and return-scheme matching around that result.

The bridge clears the pending request before dispatching the result. A volatile guard suppresses concurrent duplicate handling when both activity lifecycle methods forward the same return.

## Required Activity Lifecycle Handling

The exact demo calls `handleReturnToApp(getIntent())` from `onResume` and calls `handleReturnToApp(newIntent)` from `onNewIntent`. The source comment says both calls are required for `singleTop`, `singleTask`, or `singleInstance` activities so cancellation and new-intent returns are covered.

> [!warning] Lifecycle documentation contradiction
> `v5_MIGRATION.md` says v5 internally delivers results through a lifecycle observer and removes the need for an `onResume` call. The v5 changelog says the lifecycle observer was removed, `PopupBridgeClient` has no observer, and the exact `5.3.0` demo explicitly forwards both lifecycle callbacks. The README quick start only updates the activity intent and also omits the required `handleReturnToApp` call. Follow the exact source and demo for `5.3.0`.

## WebView Client and JavaScript Interface

`PopupBridgeClient` assigns its supplied `PopupBridgeWebViewClient` to the WebView. Applications with an existing client must pass it as the wrapper's delegate so navigation, loading, certificate, authentication, interception, history, and error callbacks continue to run. Release `5.1.0` fixed a prior issue where the WebViewClient was silently overridden.

The native JavaScript interface exposes:

- `getReturnUrlPrefix()` as `<merchant-scheme>://popupbridgev1/`;
- `open(url)` to start Browser Switch; and
- `sendMessage(name[, data])` to the application's `PopupBridgeMessageListener`.

Unlike the retained iOS `3.1.0` implementation, Android `5.3.0` dispatches the message field to a public listener. Navigation and startup failures are separately available through navigation and error listeners.

## Venmo Detection and Payment Boundary

The library manifest declares a package query for `com.venmo`. On each page-finished callback, `PopupBridgeWebViewClient` checks package installation and sets `window.popupBridge.isVenmoInstalled` in the page. Version 5 first added this validation.

The demo includes launch targets for PayPal through Braintree, historical PayPal Checkout.js, Venmo, Local Payment Methods, and a generic popup. The README explains PayPal WebView usage with Braintree Web or Checkout.js. These are transport use cases, not proof of current SDK compatibility or merchant availability.

The bridge returns web callback data rather than a native payment nonce. The embedded Braintree Web or compatible PayPal web integration still owns session creation and tokenization, and merchant configuration, buyer context, server-side sale or vault operations, and settlement remain external.

## Analytics Behavior

The runtime sends started, succeeded, failed, and canceled event names to `https://api.paypal.com/v1/tracking/batch/events`. Metadata includes application ID and name, app version, SDK version, Android API level, manufacturer and model, emulator state, platform, tenant, and a per-client session ID.

The analytics client launches requests in the activity lifecycle scope. Its network executor supports HTTPS only, uses 10-second connect and read timeouts, and throws for non-2xx responses. `AnalyticsClient` does not catch those exceptions, and the retained public API exposes neither an analytics opt-out nor a merchant error callback for analytics delivery.

## Exact `5.3.0` Change and Historical Context

Exact release `5.3.0` updates Android Gradle Plugin to `8.13.2` and compile/target SDK to 37. It does not change the bridge protocol or add a payment method.

Historical changelog context records Browser Switch `3.5.1` and API 36 in `5.2.0`, the WebViewClient override fix in `5.1.0`, and the v5 move to `ComponentActivity`, removal of the public result-delivery method and lifecycle observer, Android 13 build support, and Venmo installation validation.

## Retained Documentation Conflicts

> [!warning] Stale README and data-collector guidance
> The README says Android SDK 21 although the exact build requires API 23, announces a v4 beta despite the retained v5 release, and shows `5.2.1-SNAPSHOT` next to stable `5.3.0`. The PayPal data-collector guide imports the removed pre-v4 `com.braintreepayments.popupbridge.PopupBridge` API and an older PayPal data collector. These snippets are historical evidence and cannot be applied directly to `5.3.0`.

The v4 migration guide also predates the current `handleReturnToApp` API. Integration guidance should therefore be assembled from the exact `5.3.0` runtime and demo, with the older guides used only to understand prior breaking changes.

## Evidence Boundaries

The 41-file capsule includes the complete retained public runtime, demo integration, build and dependency metadata, README, changelog, migration guides, security policy, and historical PayPal data-collector guide. Tests, fixtures, CI, and publishing implementation details outside the selected manifests are excluded.

The capsule proves exact-SHA implementation behavior. It does not prove production browser selection, Android platform compatibility across devices, merchant enablement, buyer eligibility, payment tokenization, or settlement. No earlier exact-SHA PopupBridge Android snapshot is retained, so historical changelog entries are not byte-level version comparisons.

## Related

- [[changelog-github-popup-bridge-android]] - package-qualified Android release ledger
- [[braintree-popup-bridge]] - shared transport concept and platform parity
- [[paypal-braintree-integration]] - Braintree web-session, nonce, and server boundary
- [[paypal-checkout]] - PayPal browser checkout architecture
- [[braintree-android-sdk]] - independently versioned native Braintree Android SDK
- [[source-github-popup-bridge-ios]] - independently versioned iOS PopupBridge baseline
- [[braintree]] - company and knowledge-status page

## Raw Sources

- Snapshot manifest: `raw/github/braintree/popup-bridge-android/snapshots/2026-08-27-f306541/manifest.json`
- Release manifest: `raw/github/braintree/popup-bridge-android/releases/popup-bridge/5.3.0/2026-08-27/manifest.json`
- Release notes: `raw/github/braintree/popup-bridge-android/releases/popup-bridge/5.3.0/2026-08-27/release-notes.md`
- README: `raw/github/braintree/popup-bridge-android/snapshots/2026-08-27-f306541/files/README.md`
- Repository changelog: `raw/github/braintree/popup-bridge-android/snapshots/2026-08-27-f306541/files/CHANGELOG.md`
- Runtime client: `raw/github/braintree/popup-bridge-android/snapshots/2026-08-27-f306541/files/PopupBridge/src/main/java/com/braintreepayments/api/PopupBridgeClient.kt`
- WebView client: `raw/github/braintree/popup-bridge-android/snapshots/2026-08-27-f306541/files/PopupBridge/src/main/java/com/braintreepayments/api/PopupBridgeWebViewClient.kt`
- JavaScript interface: `raw/github/braintree/popup-bridge-android/snapshots/2026-08-27-f306541/files/PopupBridge/src/main/java/com/braintreepayments/api/internal/PopupBridgeJavascriptInterface.kt`
- Pending-request repository: `raw/github/braintree/popup-bridge-android/snapshots/2026-08-27-f306541/files/PopupBridge/src/main/java/com/braintreepayments/api/internal/PendingRequestRepository.kt`
- Demo activity: `raw/github/braintree/popup-bridge-android/snapshots/2026-08-27-f306541/files/Demo/src/main/java/com/braintreepayments/popupbridge/demo/PopupActivity.java`
- Library build: `raw/github/braintree/popup-bridge-android/snapshots/2026-08-27-f306541/files/PopupBridge/build.gradle`
- Root build: `raw/github/braintree/popup-bridge-android/snapshots/2026-08-27-f306541/files/build.gradle`
- Dependency catalog: `raw/github/braintree/popup-bridge-android/snapshots/2026-08-27-f306541/files/gradle/libs.versions.toml`
- v4 migration guide: `raw/github/braintree/popup-bridge-android/snapshots/2026-08-27-f306541/files/v4_MIGRATION.md`
- v5 migration guide: `raw/github/braintree/popup-bridge-android/snapshots/2026-08-27-f306541/files/v5_MIGRATION.md`
- PayPal data-collector guide: `raw/github/braintree/popup-bridge-android/snapshots/2026-08-27-f306541/files/popupbridge-paypaldatacollector-android.md`
