---
title: "Stripe Terminal: Set Up Your Integration (All SDK Platforms)"
type: source
date_ingested: 2026-04-24
original_format: webpage
raw_files:
  - "stripe-terminal-setup-integration-2025.md"
tags: [stripe, terminal, in-person, integration, sdk, ios, android, javascript, react-native, server-driven, connection-token]
---

## Stripe Terminal: Set Up Your Integration (All SDK Platforms)

Setup guide for all 5 Terminal integration platforms: Server-driven, JavaScript, iOS, Android, and React Native.

## Key Takeaways

### Server-driven limitations

Server-driven integration does **not** support:
- Stripe Terminal mobile readers (M2, WisePad 3)
- Offline payment collection

Advantages: works with any backend language/middleware, internet connection (not LAN), supports .NET and cloud infrastructure.

### SDK versions (as of 2026-04-24)

| SDK | Current version | Package |
| --- | --- | --- |
| iOS | StripeTerminal ~5.0 | CocoaPods / Swift Package Manager |
| Android | stripeterminal:5.4.1 | Gradle |
| Android (coroutines) | stripeterminal-ktx:5.4.1 | Optional |
| React Native | @stripe/stripe-terminal-react-native | npm/yarn/expo (public preview) |

### Platform requirements

| Platform | Minimum | Key requirements |
| --- | --- | --- |
| iOS | iOS 13+ | AndroidX not applicable; location + BT plist entries; initialize once in AppDelegate |
| Android | AndroidX required (no support libs) | Java 8 target; ACCESS_FINE_LOCATION + BT permissions; lifecycle-aware |
| React Native | — | Public preview; pod install for iOS; requestNeededAndroidPermissions helper |
| JavaScript | Modern browsers | Same-network + local DNS; Chrome 142+ needs explicit local network permission |

### iOS Info.plist requirements (all 4 required)

1. `NSLocationWhenInUseUsageDescription` — location required; payments disabled without it
2. `UIBackgroundModes: bluetooth-central` — keeps reader connected in background
3. `NSBluetoothAlwaysUsageDescription` — required even if not using BT readers
4. `NSBluetoothPeripheralUsageDescription` — removed requirement in SDK 3.4.0+ but include for App Store validation

### Android permissions required

```xml
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.BLUETOOTH_CONNECT" />
<uses-permission android:name="android.permission.BLUETOOTH_SCAN" />
```

Location services required — payments disabled without it.

### Android initialization (lifecycle-aware)

```kotlin
class StripeTerminalApplication : Application() {
    override fun onCreate() {
        super.onCreate()
        TerminalApplicationDelegate.onCreate(this)  // required for lifecycle
    }
}
```

`Terminal.init()` called once; `Terminal.getInstance()` anywhere after.

### iOS initialization

```swift
// In AppDelegate.application:didFinishLaunchingWithOptions
Terminal.initWithTokenProvider(APIClient.shared)
```

### Chrome 142+ JavaScript SDK note

Chrome 142 (October 28, 2025) and later require explicit permission before websites can access local network devices. Affects Terminal JavaScript SDK. See Stripe Support for setup steps.

### Certificate pinning

Do not configure certificate pinning in Terminal applications unless required. It can break Terminal reader connectivity.

### React Native Android 12+ requirement

Add `android:exported="true"` to your MainActivity in AndroidManifest.xml.

## Relevant Wiki Pages

- [[stripe]] — Stripe company overview
- [[stripe-terminal]] — Stripe Terminal concept page

## Raw Sources

- [[stripe-terminal-setup-integration-2025]] — verbatim SDK setup guide (all 5 platforms + Apps on Devices stub)
