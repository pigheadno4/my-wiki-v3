---
title: "PayPal Magnes (Mobile Risk)"
type: source
date_ingested: 2026-04-15
original_format: webpage
raw_files:
  - "paypal-magnes-overview.md"
  - "paypal-magnes-integrate.md"
  - "paypal-magnes-android.md"
  - "paypal-magnes-ios-objc.md"
  - "paypal-magnes-reference.md"
  - "paypal-magnes-payload-parameters.md"
  - "paypal-magnes-sample-payloads.md"
  - "paypal-magnes-ios-550-release-notes.md"
  - "paypal-magnes-ios-550-xcframework.md"
  - "paypal-magnes-android-551-release-notes.md"
  - "paypal-magnes-android-551-aar.md"
tags: [paypal, magnes, mobile, fraud-detection, risk-management, device-fingerprinting, ios, android, limited-release]
---

## Overview

PayPal Magnes is a mobile SDK (iOS and Android) for device fingerprinting and risk management. It is a limited-release product in the `/limited-release/` namespace. Formerly codenamed "Dyson" — the two names are interchangeable.

Source URL: <https://developer.paypal.com/limited-release/magnes/>

Last updated: 2024-09-23

## Key Takeaways

### Problem Magnes solves

Standard mobile integration sends transactions directly from app → merchant server → PayPal API. In this model, PayPal **cannot access device fingerprinting data** critical for risk management.

### How Magnes works

1. Magnes is integrated within the client app
2. Generates a `PayPal-Client-Metadata-Id` (or accepts one passed in)
3. Collects device payload and sends to PayPal Risk Services
4. During transaction: mobile app passes the metadata ID to merchant server
5. Merchant server includes `PayPal-Client-Metadata-Id` in PayPal Mobile API call
6. PayPal Risk Services uses payload for risk adjudication

> [!info] Magnes does NOT make risk decisions
> Magnes only provides data to PayPal Risk Services — all risk decisions are made by Risk Services, not Magnes.

### Key identifiers

- **`PayPal-Client-Metadata-Id`** — the bridge between Magnes device data and the PayPal API transaction

### Data and privacy

- Collects mobile device data based on permissions granted at app install
- Used for risk analysis and authentication only
- PayPal does not share Magnes data with third parties

### Integration platforms

3 platform-specific integration guides:

- Android (`MagnesSDK` Java/Kotlin singleton)
- iOS Swift (`PPRMagnesSDK`)
- iOS Objective-C (`PPRMOCMagnesSDK`; separate `collect` vs `collectAndSubmit`; `MagnesSource` values numeric: PAYPAL=10, EBAY=11, BRAINTREE=12, DEFAULT=-1)

### Android Integration Detail

- **Central class**: `lib.android.paypal.com.magnessdk.MagnesSDK` (singleton)
- **8 optional permissions** in `AndroidManifest.XML` (location, network, wifi, accounts, internet, phone state, GSF ID)
- **Setup modes**: simple (context only) vs advanced (`appGuid`, `Environment.LIVE`/`SANDBOX`, `MagnesSource`, custom networking factory)
- **`MagnesSource` options**: `PAYPAL`, `EBAY`, `BRAINTREE`, `DEFAULT`
- **`collectAndSubmit()`**: simple or advanced (pass own `paypalClientMetaDataId` + `additionalData` HashMap)
- **`MagnesResult`**: `getPaypalClientMetaDataId()` (32-char) + `getDeviceInfo()` (JSONObject)
- **`PayPal-Client-Metadata-Id`** must be included as header in merchant server's PayPal API call

### Payload Parameters (~60 fields)

| Category | Android-only | iOS-only | Both |
| --- | --- | --- | --- |
| Device IDs | `android_id`, `gsf_id`, `serial_number`, `mac_addrs`, `device_id`, `subscriber_id` | `cloud_identifier`, `local_identifier`, `vendor_identifier` | `app_guid`, `linker_id`, `device_model`, `device_name` |
| Network | `bssid_arr`, `cdma_*`, `cell_id`, `location_area_code`, `network_operator`, `phone_type`, `roaming`, `sim_*`, `base_station_id` | `location_auth_status` | `bssid`, `ssid`, `conn_type`, `ip_addresses`, `ip_addrs`, `proxy_setting`, `VPN_setting` |
| Risk signals | `known_apps`, `device_uptime` | `email_configured`, `pin_lock_last_timestamp` | `is_rooted`, `is_emulator`, `sms_enabled` |
| App/OS | `app_first_install_time`, `app_last_update_time` | — | `app_id`, `app_version`, `os_type`, `os_version`, `PayPal-Client-Metadata_Id` |
| Location | `location` (permission req'd) | `location` (permission req'd) | `locale_country`, `locale_lang`, `ds`, `tz`, `tz_name` |

> [!info] Pages are login-gated
> Both the payload parameters and sample payload pages show "Please log in to view the content" but content is visible anyway. The `conf_url` field reveals internal Dyson config URLs: `dyson_config_android_v3.json` and `dyson_config_ios_v4.json`.
> Undocumented fields in sample payloads not in the parameters table: `pairing_id`, `pm`. `vpn_setting` appears lowercase in samples vs `VPN_setting` in the parameters table — casing inconsistency.
> iOS sample `app_id: "com.paypal.Dyson"` confirms the "Dyson" codename was the iOS bundle ID.

### Android v5.5.1 AAR — Binary Inspection

Key findings from javap decompilation:

- **minSdkVersion**: 16
- **`MagnesSource`**: DEFAULT, PAYPAL, EBAY, BRAINTREE, SIMILITY, VENMO (SIMILITY+VENMO undocumented, matches iOS)
- **`setHasUserLocationConsent(boolean)`** confirmed present (defaults false per release notes)
- **`disableBeacon(boolean)`** undocumented Builder method (same as iOS)
- **Telemetry APIs**: `collectTelemetryData`, `setTelemetryFocusChanged`, `collectTouchData` — undocumented (matches iOS)
- **`getPaypalClientMetaDataId()`** — lowercase 'p' in 'paypal' (exact casing matters)
- Internal classes obfuscated (a/b/c/...); public API classes unobfuscated

Detail directory: `raw/magnes-android-551/` — AndroidManifest, aar-metadata, javap output for all 7 public classes

### Android v5.5.1 Release Notes

- **Trigger**: Google Play Store rejecting apps for location data collection without explicit consent
- **New API**: `setHasUserLocationConsent(boolean)` on `MagnesSettings.Builder` — **defaults to `false`**
- **10 location-gated fields** (only collected if consent = true): latitude, longitude, location_area_code, cell_id, base_station_id, cdma_network_id, cdma_system_id, bssid, ssid, bssid_array
- **Policy already enforced** — file Play Store appeal immediately requesting extension
- **Upgrade**: replace `.aar` in project workspace

### iOS v5.5.0 XCFramework — Binary Inspection

Key discrepancies found between docs and binary:

- `MagnesSource.DEFAULT` = `19` in binary (docs say `-1`)
- Undocumented sources: `SIMILITY = 17`, `VENMO = 18`
- `setUp` has undocumented `disableBeacon: Bool` parameter
- Minimum iOS target is **12.0** per swiftinterface (README says 11.0)
- Undocumented telemetry APIs: `registerTelemetry`, `collectTouchData`, `collectTelemetryData`
- Privacy Manifest declares: UserDefaults (CA92.1), CoarseLocation, PreciseLocation, PerformanceData

Detail directory: `raw/magnes-ios-550/` — headers, swiftinterface, PrivacyInfo.xcprivacy, ABI JSON

### iOS v5.5.0 Release Notes

- **Required for**: Apple Privacy Manifest enforcement (May 1, 2024) — missing = App Store Connect rejection risk
- **Deprecated fields**: Device Total Space, Device Available Free Space, System Uptime
- **No update needed** if using JavaScript SDK (not binary framework)
- **Upgrade**: replace `PPRiskMagnes.xcframework` / `PPRiskMagnes.framework` in project

### Non-mobile equivalent

**FraudNet** — for non-mobile (web) risk solutions. See `/limited-release/fraudnet`.

## Raw Sources

- [[paypal-magnes-overview]] — overview: problem statement, Magnes vs standard payment flow diagrams, 7-step Magnes payment flow, data privacy policy
- [[paypal-magnes-integrate]] — integration index: 3 platforms (Android, iOS Swift, iOS Objective-C)
- [[paypal-magnes-android]] — Android: MagnesSDK singleton, 8 optional permissions, simple/advanced setup, MagnesSource enum, collectAndSubmit, MagnesResult (paypalClientMetaDataId + deviceInfo)
- [[paypal-magnes-ios-objc]] — iOS Obj-C: PPRMOCMagnesSDK singleton, libPPRiskMagnesOC.a, 8 required frameworks (not mandatory from Xcode 14), separate collect vs collectAndSubmit, numeric MagnesSource values, `setEnviroment` typo in source
- [[paypal-magnes-reference]] — reference index: Magnes Payload Parameters (alphabetical) + Sample Payloads (Android/iOS)
- [[paypal-magnes-payload-parameters]] — ~60 parameters with Android/iOS availability; page is login-gated but table visible; conf_url reveals internal dyson_config JSON URLs
- [[paypal-magnes-sample-payloads]] — Android (Pixel XL, source_app:0) + iOS (com.paypal.Dyson, source_app:10, Simulator) sample JSONs; undocumented fields: `pairing_id`, `pm`; `vpn_setting` casing inconsistency
- [[paypal-magnes-ios-550-release-notes]] — v5.5.0 required for Apple Privacy Manifest (May 1, 2024); 3 deprecated fields; download password + SHA-512 checksum; no update needed for JS SDK integrations
- [[paypal-magnes-ios-550-xcframework]] — stub for binary XCFramework inspection; detail in `raw/magnes-ios-550/`; key findings: SIMILITY=17/VENMO=18 undocumented sources; disableBeacon param; iOS 12 min (not 11); telemetry APIs; Privacy Manifest declares UserDefaults+location+perf
- [[paypal-magnes-android-551-release-notes]] — Google Play compliance; `setHasUserLocationConsent(boolean)` defaults false; 10 location-gated fields; policy already enforced (file appeal); "Magnet" typo in source
- [[paypal-magnes-android-551-aar]] — stub for .aar binary inspection; detail in `raw/magnes-android-551/`; minSdkVersion 16; SIMILITY+VENMO undocumented; disableBeacon; telemetry APIs; `getPaypalClientMetaDataId` exact casing

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-fraud-risk]] — Full PayPal fraud & risk stack concept page (FraudNet + Magnes + FP/FPA/Chargeback Protection)
- [[source-paypal-expanded-checkout-fraud-protection]] — FraudNet and Fraud Protection Advanced (web equivalents)
