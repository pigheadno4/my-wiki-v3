---
title: "Stripe Terminal: Apps on Devices"
type: concept
category: technology
tags: [stripe, stripe-terminal, apps-on-devices, android, smartpos, pos, connect]
---

## Definition

Apps on Devices lets merchants deploy a custom Android POS app directly onto Stripe smart readers, running alongside the Stripe Reader app. It enables all-in-one POS hardware or a paired consumer-facing display architecture.

**Availability**: Not available to all users. Included at no extra cost on standard card-present pricing. Contact sales for eligibility assessment.

**SDKs**: Android and React Native only.

## Integration Modes

### 1. POS app on a Stripe smart reader

Both the merchant's POS app and the Stripe Reader app run on the same smart reader.

- On payment initiation, the Stripe Reader app takes the foreground. It returns control to the POS after success, failure, or customer cancellation and continues running in the background.
- On a DevKit, the deployment route determines the kiosk destination. After a completed transaction, a directly installed app returns to the default Stripe Reader app. A Dashboard deploy group can select the preferred kiosk app, which launches at boot and after each transaction. See [[source-stripe-terminal-apps-on-devices-build]].

### 2. POS app paired with consumer-facing app on reader

The merchant's POS runs on a separate device; a custom consumer-facing Android app runs on the Stripe smart reader.

- POS app ↔ consumer-facing app communicate over **TCP/IP**
- Reader handles payment collection; POS drives the transaction flow

## App Requirements

| Constraint | Limit |
| --- | --- |
| APK upload size | 200 MB for standard Stripe API uploads. November 2026 adds a private preview for up to 300 MB. The email request form does not activate access immediately. |
| Device storage used | ≤ 8 GB |

The May 2026 S700/S710 table lists Qualcomm Snapdragon 665, 4 GB RAM, 64 GB storage, Android 10, 1080×1920 px and 420 dpi (xxhdpi). The November overview links device-specific specifications. The T600’s lack of a main battery raises the risk of partial writes, and each T600 DevKit includes the required T-bridge for power and data. See [[source-stripe-terminal-apps-on-devices]].

## Differences from Standard Android

Stripe SmartPOS OS is AOSP-based (no consumer Android extras):

- **No Google Play Services** — Firebase, Google Maps may partially fail; verify before shipping
- **No notifications** — POS app or Stripe Reader app is always primary; no home screen
- **USB disabled in production** — no adb, no USB debugging
- The November overview requires a DevKit to develop and test. With only a production reader, use server-driven payments or standalone mode on a supported reader.

## Android Permissions

Permissions are **auto-granted at install** — no runtime prompts. Apps requesting permissions outside the allowlist are rejected. Notable allowed permissions include: location (coarse + fine), Bluetooth (all variants), camera, NFC, internet, audio, storage, biometric.

**Experimental** (not fully tested): camera, Bluetooth, location APIs.

**NFC scope.** The Apps on Devices overview limits its NFC functionality to payments. See the separate [[source-stripe-terminal-collect-nfc-data]] source for Terminal’s tapped-data preview.

## App Lifecycle

1. **Build and test** — using DevKit device
2. **App review** — prepare for Stripe's review process
3. **Submit** — upload the APK in the Dashboard and submit it to Stripe for review. Standard Stripe API uploads have a 200 MB limit. See the separate private-preview size limit above.
4. **Deploy** — after approval, deploy to selected devices. The May overview links the Deploy API. November links [[source-stripe-terminal-apps-on-devices-deploy-dashboard|Dashboard deployment]], and the separate [[source-stripe-terminal-apps-on-devices-deploy-api|API guide]] documents private-preview access.
5. **Monitor** — track deployment status

Sample app: `github.com/stripe-samples/terminal-apps-on-devices`

## SDK Setup

Use `com.stripe:stripeterminal-core` and `com.stripe:stripeterminal-appsondevices` without the top-level `com.stripe:stripeterminal` dependency. The 2026-05-01 guide illustrates `5.4.1`; the 2026-11-07 guide illustrates `6.0.0`. The documented Terminal Android SDK minimum remains `2.22.0`.

For Terminal Android SDK 6.0.0 or later, use `compileSdk` 35 or higher. The guide separately advises `targetSdkVersion` 24 or higher for Android 15 device support. See [[source-stripe-terminal-apps-on-devices-build]].

Call `TerminalApplicationDelegate.onCreate(this)` in `Application.onCreate()`.

**React Native**: use `AppsOnDevicesConnectionTokenProvider` for serverless initialization — no backend connection token server required.

**Discovery**: `AppsOnDevicesDiscoveryConfiguration` (Android) / `discoveryMethod: 'appsOnDevices'` (React Native). Discovered list contains exactly one reader.

## Transition Animations

When a payment starts, the Stripe Reader app takes the foreground. Custom transition animations require reader software 2.42 or later per the 2026-11-07 guide. On Android, configure the transition via `appTransitionAnimation` in `AppsOnDevicesConnectionConfiguration`.

- **Preset**: `AppTransitionAnimation.Preset(AppTransitionPreset.SLIDE_FROM_BOTTOM)`
- **Custom**: `AppTransitionAnimation.Custom(enterAnim, exitAnim)` using `res/anim/` resources
- **Disabled**: pass `AppTransitionAnimation.Custom.NO_ANIMATION`

## DevKit

- Sandbox only; up to 5 per user; order from Dashboard
- Adb + developer options enabled by default; shows on-screen watermark
- Test via `adb install myapp.apk` or Dashboard deploy flow
- Sideloaded apps must be uninstalled before Dashboard deployment

## Device Notes

- Admin settings: `stripe://settings/` deep link
- No system UI (no back button, no status bar)
- Dock connect/disconnect = Android config change; suppress recreation with `android:configChanges="uiMode"`

## Connect Compatibility

Apps on Devices deploys only to connected accounts controlled by a **single platform**:

- `controller.is_controller` must be `true` on the connected account
- Prevents multiple platforms from deploying to the same account

## App Review

Stripe documents three cases that qualify for automated approval before deployment.

- Apps used on Stripe readers without P2PE, such as the S700/S710
- Apps intended only for development and testing on a DevKit
- Reuploads of APKs that Stripe previously reviewed and approved

Stripe requires manual review before deployment for apps from users of its P2PE solution and all apps intended for Verifone devices. From submission, Stripe typically reviews apps within two working days and reviews most within five. Exceptional cases can take longer, and incomplete information can delay review or cause a submission to fail. These estimates create no obligation for Stripe or its affiliates.

**Guidelines** (all apps):

- Use the Terminal reader running the app to collect sensitive card and PIN information. Omit UI for manual entry of PINs, authentication values, or payment information.
- Use a DevKit to accept sandbox payments during development and testing so Stripe can use a physical Terminal test card. If live payments are necessary, accept a minimal charge such as 1 USD or its equivalent in another currency.
- Fix defects before submitting (app must install, not crash, connect to reader)
- The November 7, 2026 review guide instructs developers to allowlist `65.87.144.8/32–65.87.144.11/32` for the app.
- Provide self-contained instructions with applicable login information, a fixed authentication code valid indefinitely if applicable, the route to the payment UI, and a test walkthrough. Reviewer credentials must prevent access to sensitive information and functionality with side effects.

See [[source-stripe-terminal-apps-on-devices-app-review]] for full guidelines.

**Submit via Dashboard**. In Terminal → Software, create the app, choose compatible devices, upload the APK, add reviewer instructions if review is required, enter notification email addresses and submit for review. Monitor by email, Dashboard or webhook. `terminal.device_asset_version.app_review_approved` permits deployment. `terminal.device_asset_version.app_review_rejected` requires fixing the issue and resubmitting. See [[source-stripe-terminal-apps-on-devices-submit]].

**Deploy via Dashboard**: after approval, deploy from deploy group page, Software tab, or app details page. Device reboots immediately to install; auto-reboots every 24h. Cannot downgrade versions. Failed installs after 3 attempts → user can postpone. Progressive deployments supported (staged % rollout, manual advance required). Alpha → Beta → General group best practice. See [[source-stripe-terminal-apps-on-devices-deploy-dashboard]].

## Sources

- [[source-stripe-terminal-apps-on-devices]] — May and November 2026 overview of Android POS integrations, APK upload scopes, DevKit and T600 requirements, permissions, deployment and Connect.
- [[source-stripe-terminal-apps-on-devices-build]] — build/test: DevKit setup, SDK deps, serverless init, discovery, transition animations, adb testing
- [[source-stripe-terminal-apps-on-devices-app-review]] — app review: automated vs manual, timeline, guidelines
- [[source-stripe-terminal-apps-on-devices-submit]] — submit: Dashboard upload flow, status monitoring (email/Dashboard/webhook)
- [[source-stripe-terminal-apps-on-devices-deploy-dashboard]] — deploy: deploy groups, three entry points, progressive rollout, Alpha/Beta/General best practice
- [[source-stripe-terminal-apps-on-devices-deploy-api]] — deploy via API (private preview): same behavior as Dashboard, device deploy groups + locations
- [[source-stripe-terminal-apps-on-devices-monitor]] — Dashboard deployment monitoring. The May 2026 guide lists per-release reader counts by status (Pending, Served, Installed, and Failed). Served means the app reached the device and installation will be attempted on its next reboot.
- [[source-stripe-terminal-apps-on-devices-troubleshooting]] — May and November 2026 troubleshooting for Files API uploads, app approval, settings, multiple apps on compatible readers, kiosk selection, and restarts.
