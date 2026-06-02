---
title: "Stripe Terminal: Apps on Devices — Build and Test"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-terminal-apps-on-devices-build-2025.md"
tags: [stripe, stripe-terminal, apps-on-devices, android, devkit, adb, react-native]
---

## Summary

Step-by-step guide for building, testing, and running custom Android POS apps on Stripe smart readers using the Apps on Devices DevKit.

## Key Details

**DevKit**: Sandbox-only, up to 5 per user. Adb + developer options enabled by default. Shows on-screen watermark during testing.

**Android dependencies** (use these, not `com.stripe:stripeterminal`):
```
com.stripe:stripeterminal-core:5.4.1
com.stripe:stripeterminal-appsondevices:5.4.1
```
Min SDK version: `2.22.0`. Set `targetSdkVersion ≥ 24` for Android 15 support.

**`TerminalApplicationDelegate.onCreate(this)`** must be called in `Application.onCreate()`.

**React Native serverless init**: use `AppsOnDevicesConnectionTokenProvider` — no backend connection token server needed.

**Discovery**: `AppsOnDevicesDiscoveryConfiguration` (Android) / `discoveryMethod: 'appsOnDevices'` (React Native). Discovery list contains a single reader.

**Transition animations** (when Stripe Reader app takes foreground):
- Preset: `AppTransitionAnimation.Preset(AppTransitionPreset.SLIDE_FROM_BOTTOM)`
- Custom: `AppTransitionAnimation.Custom(enterAnim, exitAnim)` using `res/anim/` resources
- Disabled: `AppTransitionAnimation.Custom.NO_ANIMATION`

**Admin settings**: accessible via `stripe://settings/` deep link from any app.

**Dock config change**: connecting/disconnecting from dock triggers Android config change; suppress activity recreation with `android:configChanges="uiMode"`.

**No system UI**: no back button or status bar on production devices.

**adb testing**: `adb install myapp.apk` → `adb shell am start com.example.myapp/.MainActivity`. Sideloaded apps must be uninstalled before Dashboard deployment.

**Test payments**: physical test card required (order via Dashboard); sandbox only; decimal amounts control outcome.

## Raw Sources

- [[stripe-terminal-apps-on-devices-build-2025]] — verbatim webpage content
