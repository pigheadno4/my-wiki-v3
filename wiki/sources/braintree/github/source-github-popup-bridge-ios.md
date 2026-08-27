---
title: "GitHub: braintree/popup-bridge-ios"
type: source
date_ingested: 2026-08-27
original_format: github-repo
raw_files:
  - "github/braintree/popup-bridge-ios/snapshots/2026-08-27-00256b4/manifest.json"
tags: [braintree, popup-bridge, ios, webview, paypal, venmo, app-switch, github-repository]
---

## Overview

`PopupBridge@3.1.0` is the first retained exact-SHA baseline for Braintree's iOS WebView popup bridge. It lets JavaScript running in a `WKWebView` open an authentication popup through `ASWebAuthenticationSession` and receive the return URL data in the parent page.

PopupBridge is a transport adapter around an existing web checkout. It does not create PayPal or Braintree orders, tokenize a payment, grant merchant eligibility, or process the resulting transaction.

## Baseline and Installation

The retained package resolves to SHA `00256b4b8c58367287fe35a442a33cd7c010a94f` and was released on 2026-06-24. It requires iOS 16+, Xcode 16.2+, and Swift 5.10+ or Objective-C.

The repository supports Swift Package Manager, CocoaPods, and Carthage. Its public product and module are named `PopupBridge`; the framework metadata and podspec both report version `3.1.0`.

## WebView-to-Browser Flow

Constructing `POPPopupBridge` performs the bridge setup:

1. It enables a `WKScriptMessageHandler` named `POPPopupBridge` through a weak proxy.
2. It injects `window.popupBridge` at document start into the main frame and child frames.
3. JavaScript calls `window.popupBridge.open(url)`, which sends the URL to native code.
4. Native code opens the URL in `ASWebAuthenticationSession` with an ephemeral browser session requested by default.
5. A valid return URL is reduced to its path, query parameters, and fragment and delivered through `window.popupBridge.onComplete(null, payload)`.

The return URL must use the active callback scheme and the exact host `popupbridgev1`. A mismatched scheme or host is ignored. Cancellation invokes `window.popupBridge.onCancel()` when that callback exists and otherwise calls `onComplete(null, null)`.

The injected script also exposes `window.popupBridge.sendMessage(message, data)`, and `WebViewMessage` can decode that shape. The exact `3.1.0` `POPPopupBridge.userContentController` implementation handles only the decoded URL field and does not dispatch the decoded message field to a public listener. The retained data-collector guide's message callback therefore describes an older API rather than a working `3.1.0` path.

## Venmo App Switch in `3.1.0`

Exact release `3.1.0` adds `init(webView:returnURLScheme:prefersEphemeralWebBrowserSession:)`. When the Venmo app is installed, PopupBridge uses the merchant-provided scheme consistently for the JavaScript return prefix, the `ASWebAuthenticationSession` callback scheme, and native return validation. JavaScript receives the full prefix through `window.popupBridge.getReturnUrlPrefix()`.

The merchant must:

- register the same scheme under `CFBundleURLTypes`;
- allowlist `com.venmo.touch.v2` under `LSApplicationQueriesSchemes`; and
- pass the scheme to the PopupBridge initializer.

When Venmo is not installed, the bridge advertises and validates its internal `sdk.ios.popup-bridge://popupbridgev1/` prefix. The injected interface separately reports `window.popupBridge.isVenmoInstalled`.

This plumbing does not make Venmo available to a merchant. The embedded Braintree Web integration owns Venmo creation and tokenization, and remote configuration, account enablement, buyer context, and server processing remain outside this repository.

## PayPal and Braintree Web Boundary

The retained README lists three supported payment integrations:

- PayPal SDK v5, with v6 and later explicitly unsupported;
- PayPal through Braintree; and
- Venmo through Braintree.

The PayPal example loads Braintree Web client and PayPal Checkout components, creates a Braintree client from merchant authorization, loads the PayPal SDK, and leaves button rendering and transaction handling to that web integration. PopupBridge only replaces the unavailable WebView popup transport.

The retained Venmo example similarly loads Braintree Web and uses `window.popupBridge.getReturnUrlPrefix()` as `deepLinkReturnUrl`. It sets `paymentMethodUsage: 'multi_use'`, but that example alone does not prove that a merchant has vaulting permission or that a returned nonce was stored and charged successfully.

## Browser, WebView, and Lifecycle Characteristics

- `prefersEphemeralWebBrowserSession` defaults to `true`, requesting isolation from the user's normal browser cookies and browsing data.
- The injected user script runs in all frames, preserving popup support from an iframe.
- The bridge's deinitializer calls `removeAllScriptMessageHandlers()` on the shared user-content controller rather than removing only its own named handler.
- The demo loads `https://braintree.github.io/popup-bridge-example/` and registers `com.braintreepayments.Demo` as its return scheme. It is demonstration evidence rather than a merchant integration contract.

## Analytics and Privacy Evidence

The runtime sends `popup-bridge:started`, `succeeded`, `failed`, and `canceled` events to `https://api.paypal.com/v1/tracking/batch/events`. Its batch metadata includes the application identifier and name, application version, PopupBridge version, OS version, device manufacturer and model, simulator state, package manager, platform, and a per-instance session ID.

Analytics failures are logged and do not fail the popup flow. The retained source does not expose an opt-out control.

> [!warning] Privacy-manifest mismatch
> `PrivacyInfo.xcprivacy` contains blank data-type and purpose values while the exact runtime sends application and device metadata to PayPal's analytics endpoint. The snapshot does not establish whether this blank declaration satisfies current App Store privacy requirements.

## Migration History and Documentation Conflicts

Version 2 replaced `SFSafariViewController` with `ASWebAuthenticationSession`, converted the library to Swift, removed the global return-scheme and open methods, removed `POPPopupBridgeDelegate`, and initially made URL-type registration unnecessary. Version 3 raised the platform floor to iOS 16 and added private-session control plus Venmo installation detection. Version `3.1.0` reintroduces merchant URL-scheme registration for the specific Venmo app-switch path.

> [!warning] Stale integration guidance
> The `3.1.0` podspec still describes an `SFSafariViewController` implementation even though the exact runtime and v2 migration use `ASWebAuthenticationSession`. The retained PayPal data-collector guide calls the removed `POPPopupBridgeDelegate` methods and uses pre-v2 integration types, so its snippets cannot be applied directly to `3.1.0`.

The README's version table marks 3.x active, 2.x inactive and unsupported after April 2026, and 1.x inactive and unsupported after October 2025. These dated status statements should be rechecked before current support recommendations.

## Evidence Boundaries

The 35-file capsule includes public runtime source, demo code, package and project metadata, migration guides, changelog, README, security policy, and the legacy PayPal data-collector guide. Tests and fixtures are excluded. The capsule proves behavior at the exact retained SHA; it does not prove production browser behavior, App Store acceptance, merchant enablement, payment-method eligibility, or server-side settlement.

No earlier exact-SHA PopupBridge iOS snapshot is retained. Historical changelog entries are useful migration context but are not equivalent to separately collected version comparisons.

## Related

- [[changelog-github-popup-bridge-ios]] - package-qualified release ledger
- [[braintree-popup-bridge]] - WebView transport concept and platform boundary
- [[paypal-braintree-integration]] - Braintree payment-session, nonce, and server boundary
- [[paypal-checkout]] - PayPal browser checkout architecture
- [[braintree-ios-sdk]] - independently versioned native Braintree iOS SDK
- [[braintree]] - company and knowledge-status page

## Raw Sources

- Snapshot manifest: `raw/github/braintree/popup-bridge-ios/snapshots/2026-08-27-00256b4/manifest.json`
- Release manifest: `raw/github/braintree/popup-bridge-ios/releases/popupbridge/3.1.0/2026-08-27/manifest.json`
- Release notes: `raw/github/braintree/popup-bridge-ios/releases/popupbridge/3.1.0/2026-08-27/release-notes.md`
- README: `raw/github/braintree/popup-bridge-ios/snapshots/2026-08-27-00256b4/files/README.md`
- Repository changelog: `raw/github/braintree/popup-bridge-ios/snapshots/2026-08-27-00256b4/files/CHANGELOG.md`
- Runtime bridge: `raw/github/braintree/popup-bridge-ios/snapshots/2026-08-27-00256b4/files/Sources/PopupBridge/POPPopupBridge.swift`
- Injected JavaScript: `raw/github/braintree/popup-bridge-ios/snapshots/2026-08-27-00256b4/files/Sources/PopupBridge/PopupBridgeUserScript.swift`
- Browser session wrapper: `raw/github/braintree/popup-bridge-ios/snapshots/2026-08-27-00256b4/files/Sources/PopupBridge/WebAuthenticationSession.swift`
- Analytics payload and service: `raw/github/braintree/popup-bridge-ios/snapshots/2026-08-27-00256b4/files/Sources/PopupBridge/Analytics/`
- Privacy manifest: `raw/github/braintree/popup-bridge-ios/snapshots/2026-08-27-00256b4/files/Sources/PopupBridge/PrivacyInfo.xcprivacy`
- v2 migration guide: `raw/github/braintree/popup-bridge-ios/snapshots/2026-08-27-00256b4/files/V2_MIGRATION.md`
- v3 migration guide: `raw/github/braintree/popup-bridge-ios/snapshots/2026-08-27-00256b4/files/V3_MIGRATION.md`
- PayPal data-collector guide: `raw/github/braintree/popup-bridge-ios/snapshots/2026-08-27-00256b4/files/popupbridge-paypaldatacollector-ios.md`
