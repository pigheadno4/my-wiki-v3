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

- Device boots into the merchant POS app (replaces Stripe Reader app as default launcher)
- When a payment is initiated, Stripe Reader app takes the foreground
- After transaction completes, Stripe Reader app exits and the POS app becomes primary again

### 2. POS app paired with consumer-facing app on reader

The merchant's POS runs on a separate device; a custom consumer-facing Android app runs on the Stripe smart reader.

- POS app ↔ consumer-facing app communicate over **TCP/IP**
- Reader handles payment collection; POS drives the transaction flow

## App Requirements

| Constraint | Limit |
| --- | --- |
| APK upload size | 200 MB |
| Device storage used | ≤ 8 GB |

**S700/S710 hardware**: Qualcomm Snapdragon 665, 4GB RAM, 64GB storage, Android 10, 1080×1920 px, 420dpi (xxhdpi).

## Differences from Standard Android

Stripe SmartPOS OS is AOSP-based (no consumer Android extras):

- **No Google Play Services** — Firebase, Google Maps may partially fail; verify before shipping
- **No notifications** — POS app or Stripe Reader app is always primary; no home screen
- **USB disabled in production** — no adb, no USB debugging
- Use a DevKit device for development

## Android Permissions

Permissions are **auto-granted at install** — no runtime prompts. Apps requesting permissions outside the allowlist are rejected. Notable allowed permissions include: location (coarse + fine), Bluetooth (all variants), camera, NFC, internet, audio, storage, biometric.

**Experimental** (not fully tested): camera, Bluetooth, location APIs.

**NFC restriction**: device NFC is payments-only — cannot be used for non-payment features.

## App Lifecycle

1. **Build and test** — using DevKit device
2. **App review** — prepare for Stripe's review process
3. **Submit** — upload APK via Stripe API (200MB limit)
4. **Deploy** — push to selected devices via Deploy API
5. **Monitor** — track deployment status

Sample app: `github.com/stripe-samples/terminal-apps-on-devices`

## SDK Setup

**Android Gradle dependencies** (do NOT use `com.stripe:stripeterminal`):

```groovy
com.stripe:stripeterminal-core:5.4.1
com.stripe:stripeterminal-appsondevices:5.4.1
```

Min SDK version: `2.22.0`. Set `targetSdkVersion ≥ 24` for Android 15 support.

Call `TerminalApplicationDelegate.onCreate(this)` in `Application.onCreate()`.

**React Native**: use `AppsOnDevicesConnectionTokenProvider` for serverless initialization — no backend connection token server required.

**Discovery**: `AppsOnDevicesDiscoveryConfiguration` (Android) / `discoveryMethod: 'appsOnDevices'` (React Native). Discovered list contains exactly one reader.

## Transition Animations

When a payment starts, Stripe Reader app takes the foreground. Customize the transition via `appTransitionAnimation` in `AppsOnDevicesConnectionConfiguration`:

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

Stripe reviews apps before deployment. Review is automated (no manual review) for:

- Non-P2PE apps on Stripe readers (S700/S710)
- DevKit-only apps
- Re-uploads of previously approved APKs

Manual review required for: P2PE apps, all Verifone deployments. Timeline: typically 2 working days, up to 5.

**Guidelines** (all apps):

- No keyed card/PIN input fields — always use Terminal reader for payment collection
- Support sandbox payments (DevKit); if live required, minimum 1 USD charge
- Fix defects before submitting (app must install, not crash, connect to reader)
- Instructions must be self-contained; credentials must be valid indefinitely; no side-effecting actions

See [[source-stripe-terminal-apps-on-devices-app-review]] for full guidelines.

**Submit via Dashboard**: Terminal → Software → Create app → upload APK → choose device types, add reviewer instructions, enter notification email(s) → Submit for review. Status via email, Dashboard, or webhooks (`terminal.device_asset_version.app_review_approved` / `app_review_rejected`). See [[source-stripe-terminal-apps-on-devices-submit]].

**Deploy via Dashboard**: after approval, deploy from deploy group page, Software tab, or app details page. Device reboots immediately to install; auto-reboots every 24h. Cannot downgrade versions. Failed installs after 3 attempts → user can postpone. Progressive deployments supported (staged % rollout, manual advance required). Alpha → Beta → General group best practice. See [[source-stripe-terminal-apps-on-devices-deploy-dashboard]].

## Sources

- [[source-stripe-terminal-apps-on-devices]] — primary source: integration modes, requirements, AOSP differences, permissions, Connect compatibility
- [[source-stripe-terminal-apps-on-devices-build]] — build/test: DevKit setup, SDK deps, serverless init, discovery, transition animations, adb testing
- [[source-stripe-terminal-apps-on-devices-app-review]] — app review: automated vs manual, timeline, guidelines
- [[source-stripe-terminal-apps-on-devices-submit]] — submit: Dashboard upload flow, status monitoring (email/Dashboard/webhook)
- [[source-stripe-terminal-apps-on-devices-deploy-dashboard]] — deploy: deploy groups, three entry points, progressive rollout, Alpha/Beta/General best practice
- [[source-stripe-terminal-apps-on-devices-deploy-api]] — deploy via API (private preview): same behavior as Dashboard, device deploy groups + locations
- [[source-stripe-terminal-apps-on-devices-monitor]] — monitor: Dashboard status per release version (Pending/Served/Installed/Failed)
- [[source-stripe-terminal-apps-on-devices-troubleshooting]] — troubleshooting: upload timeout, sandbox/live resubmit, admin settings deep link, IPC limit, crash loops, no production logs
