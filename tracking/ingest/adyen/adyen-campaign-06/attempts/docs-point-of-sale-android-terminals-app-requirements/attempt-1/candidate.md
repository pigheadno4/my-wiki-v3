---
title: "Adyen Android payment-terminal app requirements"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/android-terminals/app-requirements"
raw_files:
  - "adyen/docs/point-of-sale/android-terminals/app-requirements/2026-09-15.md"
tags: [adyen, point-of-sale, android-terminals, app-requirements, apk, security]
---

## Overview

Adyen's Android-terminal app requirements page describes upload checks, device compatibility, allowed permissions, runtime restrictions, WebView versions, and a test path for apps installed on Adyen Android **payment terminals** in Terminal API or standalone solutions. It concerns apps on those devices, not a merchant-phone Mobile SDK or the separately versioned Android online-checkout SDK. The 2026-09-15 snapshot does not establish current regional model availability, app approval or successful deployment. [[adyen]] [[adyen-android-terminals]]

## Key takeaways

- The APK maximum is 200 MB in live and 700 MB in test. Its manifest must include `minSdkVersion`; the app must run on the terminal's Android version. The raw model/region/OS/API-level/`Build.MODEL`/CPU table is a dated compatibility snapshot, and Adyen calls the regional rollout work in progress. Check live Customer Area for regional terminal availability. Unique `versionCode` values are required for each Customer Area release, and native-code libraries must match the terminal's ARMv7 or ARM64 ABI. See `## App specifications`.
- The page advises against merchant apps on P630 due to limited storage. In this snapshot P630 and M450 support app installation, but certificate installation is unsupported. See `## Requirements`.
- Only the listed Android app permissions are allowed; an APK with an unlisted permission is marked invalid at upload. Terminal apps cannot use a `CATEGORY_HOME` launcher, manifest `testOnly`, a custom accessibility service, or `android.permission.BIND_DEVICE_ADMIN`. The terminals lack debug mode, an installed browser, and Google Play services. An installed app cannot be downgraded; the page allows upgrade or uninstall. See `## Allowed permissions` and `## Restrictions`.
- A WebView app must be compatible with the version for its terminal software and Android OS; the table differentiates Android 13, 10 and 9, including no Android 13 WebView entry at software 1.108 or earlier. Read the current device value at **Settings > Device info**; Support is the route for requesting a specific WebView version. See `## WebView versions`.
- USB ADB debugging cannot be enabled on Adyen payment terminals for security reasons. Adyen routes debugging to a regular Android device, then upload/install and Terminal API integration tests on a test terminal, then final integration testing with a live Customer Area and live terminal. Those steps are testing guidance, not evidence that an app or payment passed them. See `## Debug and test`.

## Detail locators

- `## App specifications`: exact per-model regional rows and Android/API-level/CPU/`Build.MODEL` values; the AMS1 `minSdkVersion` example and ABI names `armeabi-v7a`, `armeabi`, `arm64-v8a`. The table labels both S1E4Pro and S1F4Pro with similar `Build.MODEL` strings; keep those row identities as printed and verify device identity separately.
- `## Allowed permissions`: full allowlist, including location, camera, network, storage and biometric entries; listed permission availability is not proof of a particular terminal's hardware capability or granted runtime permission.
- `## WebView versions`: terminal-software-to-Android-WebView version matrix. This is distinct from a general browser, which the Restrictions section says is absent.
- `## Debug and test`: regular-device adb debug, test-terminal local/cloud Terminal API integration checks, support log route, and later live-terminal testing.

## Related

- [[adyen-android-terminals]] — Android payment terminal app and deployment routes.
- [[adyen-terminal-api]] — integration-message boundary for the described terminal tests.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/android-terminals/app-requirements/2026-09-15|Adyen Android app requirements, fetched 2026-09-15]]
