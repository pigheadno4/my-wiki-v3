---
title: "Stripe Terminal: Apps on Devices — Build and Test"
type: source
date_ingested: 2026-05-01
date_updated: 2026-11-24
original_format: webpage
canonical_url: "https://docs.stripe.com/terminal/features/apps-on-devices/build"
raw_files:
  - "stripe-terminal-features-apps-on-devices-build-2026-11-07.md"
  - "stripe-terminal-apps-on-devices-build-2025.md"
tags: [stripe, stripe-terminal, apps-on-devices, android, devkit, adb, react-native]
---

## Summary

Guide to building and testing a custom Android POS app on Stripe smart readers with Apps on Devices. Connect the SmartPOS DevKit to a network, register it to your Stripe account and install all available updates. The DevKit runs only in sandboxes, ships with adb and developer options enabled, and displays a test watermark. Stripe documents ordering up to five per user. For users with only a production reader, the 2026-11-07 guide points to server-driven payment acceptance or standalone mode on supported hardware.

## Key Details

**Android dependencies.** Use the `com.stripe:stripeterminal-core` and `com.stripe:stripeterminal-appsondevices` artifacts without the top-level `com.stripe:stripeterminal` dependency. The 2026-05-01 guide uses `5.4.1` in its example. The 2026-11-07 guide uses `6.0.0` and retains Terminal Android SDK `2.22.0` as the Apps on Devices minimum. Terminal Android SDK 6.0.0 or later requires `compileSdk` 35 or higher. The guide separately advises `targetSdkVersion` 24 or higher to support Android 15 devices.

**App initialization.** Call `TerminalApplicationDelegate.onCreate(this)` in `Application.onCreate()` and declare the Application subclass in the manifest. React Native can use `AppsOnDevicesConnectionTokenProvider` to initialize without a backend issuing connection tokens.

**Discovery and connection.** Run the app on the registered reader and use `AppsOnDevicesDiscoveryConfiguration` on Android or `discoveryMethod: 'appsOnDevices'` on React Native before connecting. The Android example selects the single discovered reader. The guide documents `easyConnect` as an option to combine the steps, from Android SDK 5.0.0 and in React Native SDK 0.0.1-beta.29.

**Payment handoff.** After the app connects in Apps on Devices mode, the Stripe Reader app handles payment operations and foregrounds full screen to guide the customer. It returns control on success, failure or customer cancellation and continues running in the background. Apps on Devices supports offline payment collection. For the DevKit kiosk destination, see Test routes below.

**Payment transition animations.** Custom animations require reader software 2.42 or later per the November guide. Android supports a preset, custom `res/anim/` resources, or disabling animations via `AppTransitionAnimation.Custom.NO_ANIMATION`. React Native documents preset, custom, disabled and system-default choices. Invalid animation resource IDs throw during connection in debug builds and fall back to the system default in release builds. Settings screens are opened by a separate Android activity transition that can be customized with `ActivityOptions`.

**Admin settings.** The root deep link is `stripe://settings/`. The November guide documents destination-specific links. All settings, network, advanced, and registration code always require the admin PIN. Appearance, language and bug report prompt by default and can be configured to omit that prompt. See the November raw under **Available deep links** for the destination table.

**Device behavior.** Stripe Android devices omit the back button and status bar. Docking and undocking trigger an Android configuration change. Use `android:configChanges="uiMode"` to suppress automatic activity recreation for that change. For T600 landscape orientation, the November guide specifies `android:screenOrientation="nosensor"`.

## Test routes

- **Direct adb installation.** The guide shows `adb install myapp.apk` and launching the app with `adb shell am start com.example.myapp/.MainActivity`. It also covers adb on the same Wi-Fi network for a UX700 DevKit. A directly installed app cannot be set as the preferred kiosk, and the DevKit returns to the default Stripe Reader app after a completed transaction.
- **Dashboard testing.** Use a sandbox deploy group to choose the preferred DevKit kiosk app. The reader launches it at boot and after each transaction. Uninstall a sideloaded app before redeploying it through the Dashboard.
- **Test payments.** Use a Stripe physical test card in the sandbox. Decimal amounts can select test outcomes.

## Dated Verifone support

The 2026-05-01 guide describes US and Canada public preview and selected model-specific private previews. The 2026-11-07 guide lists P630 and UX700 as generally available in the US and V660p and M425 in US and Canada public preview. Further model and country combinations are listed in the November **Verifone reader support** notice, which requires contacting Sales to order a Verifone reader or join a preview.

## Related

- [[stripe]]
- [[stripe-terminal-apps-on-devices]]

## Raw Sources

- [[raw/stripe-terminal-features-apps-on-devices-build-2026-11-07|2026-11-07 Apps on Devices build and test guide]]
- [[stripe-terminal-apps-on-devices-build-2025]] — 2026-05-01 build and test guide, including the historical dependency example and Verifone preview notice
