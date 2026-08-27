---
title: "Braintree PopupBridge"
type: concept
category: technology
tags: [braintree, paypal, venmo, webview, ios, android, mobile, app-switch]
---

## Braintree PopupBridge

Braintree PopupBridge adapts a web checkout running inside a native mobile WebView so JavaScript popup flows can open in a browser context and return structured data to the parent page. It is a transport bridge for an existing web integration, not a payment SDK, order API, or merchant-enablement mechanism.

## iOS Baseline

The first retained iOS baseline is `PopupBridge@3.1.0` at exact SHA `00256b4b8c58367287fe35a442a33cd7c010a94f`. It requires iOS 16+, Xcode 16.2+, and Swift 5.10+, and supports Swift Package Manager, CocoaPods, and Carthage.

`POPPopupBridge` injects `window.popupBridge` into a `WKWebView`, opens requested URLs with `ASWebAuthenticationSession`, and returns the callback path, query parameters, and fragment to `window.popupBridge.onComplete`. The return is accepted only when its URL scheme matches the active return scheme and its host is `popupbridgev1`.

## Android Baseline

The first retained Android baseline is `popup-bridge@5.3.0` at exact SHA `f30654168b997ea1dd95ebc61901582ae00bebb0`. The build requires Android API 23+, compiles and targets API 37, uses Java/Kotlin JVM 11, and depends on Braintree Browser Switch `3.5.1`.

`PopupBridgeClient` enables JavaScript, installs a `popupBridge` JavaScript interface, opens requested URLs through Browser Switch, persists the pending request in Android DataStore, and returns the deep-link payload to `window.popupBridge.onComplete`. The host activity must forward return intents through `handleReturnToApp()`; single-task-style activities should call it from both `onResume` and `onNewIntent`, with the client suppressing duplicate handling.

## Platform Parity

| Concern | iOS `3.1.0` | Android `5.3.0` |
| --- | --- | --- |
| Embedded surface | `WKWebView` user script | `WebView` JavaScript interface |
| External browser | `ASWebAuthenticationSession` | Braintree Browser Switch |
| Return mechanism | callback scheme and host validation | application deep link plus persisted pending request |
| Venmo signal | injected at setup | injected after page load |
| Host integration | retain `POPPopupBridge` | retain client, wrap `WebViewClient`, forward return intents |
| Payment output | callback payload only | callback payload only |

Neither platform creates a payment-method nonce. The embedded web SDK and merchant server remain responsible for payment behavior and processing.

## PayPal and Venmo Boundary

The retained README lists PayPal SDK v5, PayPal through Braintree, and Venmo through Braintree as supported web payment integrations. PayPal SDK v6 and later are explicitly listed as unsupported at this baseline.

For Venmo app switch, `3.1.0` adds a public initializer accepting the merchant's registered return URL scheme. PopupBridge advertises that scheme through `window.popupBridge.getReturnUrlPrefix()` only when the Venmo app is installed; otherwise it retains the internal `sdk.ios.popup-bridge` callback scheme. The merchant must register the same scheme under `CFBundleURLTypes` and allowlist `com.venmo.touch.v2` for installation checks.

This bridge does not grant Venmo or PayPal eligibility. The embedded Braintree Web or compatible PayPal web integration still owns payment-session creation and tokenization, while merchant configuration, buyer context, and server processing remain external requirements.

## Integration Characteristics

- The injected JavaScript runs in the main frame and child frames because `forMainFrameOnly` is false.
- Cancellation invokes `window.popupBridge.onCancel()` when present and otherwise calls `onComplete(null, null)`.
- The SDK emits started, succeeded, failed, and canceled analytics events to PayPal's batch tracking endpoint with application, SDK, OS, device, package-manager, and session metadata.
- Deinitialization removes all script message handlers from the WebView's user-content controller, so applications sharing that controller should account for the cleanup behavior.

> [!warning] Retained documentation conflicts
> The `3.1.0` podspec still describes an `SFSafariViewController` implementation although the current runtime uses `ASWebAuthenticationSession`. The PayPal data-collector guide uses the removed `POPPopupBridgeDelegate` API from v1, and the privacy manifest contains blank data-type and purpose values while analytics source sends application and device metadata. Treat these files as stale or incomplete guidance rather than current integration instructions.

> [!warning] Android integration conflicts
> The Android README says API 21 while the exact build sets `minSdkVersion` 23, advertises a v4 beta despite the retained v5 release, and references an older snapshot version. More importantly, `v5_MIGRATION.md` says return delivery is internal through a lifecycle observer, while the v5 changelog says that observer was removed and the exact `5.3.0` demo explicitly calls `handleReturnToApp()` from `onResume` and `onNewIntent`. Follow the exact runtime and demo for this version.

## Version Boundary

Version 3 moved the minimum platform to iOS 16 and added ephemeral browser-session control plus Venmo installation detection. Exact release `3.1.0` adds the merchant return-scheme initializer required for the retained Venmo app-switch path. Historical changelog statements provide migration context; no earlier exact-SHA PopupBridge iOS snapshot is retained yet.

Android v5 removes the old result-delivery method and lifecycle observer, moves from `FragmentActivity` to `ComponentActivity`, and adds Venmo installation validation. Exact release `5.3.0` updates Android Gradle Plugin to 8.13.2 and compile/target SDK to 37; it does not change the popup protocol or payment-method surface. No earlier exact-SHA PopupBridge Android snapshot is retained.

## Related

- [[source-github-popup-bridge-ios]] - exact-SHA iOS implementation baseline
- [[changelog-github-popup-bridge-ios]] - package-qualified release ledger
- [[source-github-popup-bridge-android]] - exact-SHA Android implementation baseline
- [[changelog-github-popup-bridge-android]] - package-qualified Android release ledger
- [[paypal-braintree-integration]] - Braintree web-session and nonce-processing boundary
- [[paypal-checkout]] - PayPal browser checkout architecture
- [[braintree-ios-sdk]] - independently versioned native Braintree iOS SDK
- [[braintree-android-sdk]] - independently versioned native Braintree Android SDK
- [[braintree]] - company page
