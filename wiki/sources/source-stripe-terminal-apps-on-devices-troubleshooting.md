---
title: "Stripe Terminal: Apps on Devices — Troubleshooting"
type: source
date_ingested: 2026-05-01
date_updated: 2026-11-24
original_format: webpage
canonical_url: "https://docs.stripe.com/terminal/features/apps-on-devices/troubleshooting"
raw_files:
  - "stripe-terminal-features-apps-on-devices-troubleshooting-2026-11-07.md"
  - "stripe-terminal-apps-on-devices-troubleshooting-2025.md"
tags: [stripe, stripe-terminal, apps-on-devices, troubleshooting, android]
---

## Summary

The May and November 2026 [[stripe]] troubleshooting guides cover uploading, deploying, and operating [[stripe-terminal-apps-on-devices|Apps on Devices]] apps.

## Upload and Approval

- **Files API upload timeout.** Stripe's server cutoff is 45 seconds for this APK upload path. For a timeout with a large APK or slow uplink, the guide suggests uploading to Stripe from a server with a faster connection. The separate [[source-stripe-terminal-apps-on-devices|Apps on Devices overview]] describes a larger-upload private preview with no timeout specified in the capture.
- **Sandbox to live.** Submit the app again for live approval after sandbox approval. The guide says to upload the exact same APK for automatic approval.

## Settings Access

When a third-party app is the default launch app, the usual left-edge swipe to **Settings** is unavailable. The app can use `stripe://settings/` to open Stripe admin's **All settings** screen. The November [[source-stripe-terminal-apps-on-devices-build|Build guide]] says this root destination always requires the admin PIN.

The Android Settings app is a separate screen. Stripe blocks it on production devices. On a DevKit, the guide describes opening Android Settings via `adb` to change the device language, because the DevKit reader app cannot change it.

## Multiple Apps and Kiosk Selection

The May 1 guide names Stripe Reader S700/S710. The November 7 guide describes running multiple apps on Apps on Devices-compatible Terminal readers. Stripe provides no app launcher, so developers implement switching in their apps. During deployment, they can specify `default_kiosk_application`, which launches at update checks and after payments. The November wording identifies the compatible-reader class and gives no exhaustive device list or rollout evidence.

The troubleshooting guides say the Dashboard cannot configure multiple apps on a device. The November Build guide separately documents choosing a preferred kiosk app when deploying to a DevKit deploy group in the sandbox Dashboard. A direct sideload does not set the DevKit's preferred kiosk app.

To configure that preferred app on a DevKit, include the device in a deploy group. Upload the app selecting only DevKit device types to skip app review, then deploy the version to the group targeting that DevKit.

## Web App Packaging

A framework such as Cordova can package a web app as an Android APK. The app needs a JavaScript bridge to issue local Terminal SDK commands. With a server-driven integration, Stripe handles payment collection commands and device communication without the JavaScript bridge or Terminal handoff client.

## Crashes and Production Logs

- **Restarts.** A production reader restarts the merchant app after a crash when that app is configured as the default. An initialization failure can cause a crash loop. On a DevKit configured to use the Stripe payment app as default, a crash of the merchant app restarts Stripe's app instead.
- **Many line items.** The guide identifies memory as a possible cause and cites a 500 KB Android IPC limit when saving activity state. Storing data outside activity state, such as in a database, can help.
- **Production fixes and observability.** Upload and deploy a corrected version to fix a deployed app. Stripe does not expose production reader logs and points to Sentry for observability.

## Raw Sources

- [[raw/stripe-terminal-features-apps-on-devices-troubleshooting-2026-11-07|2026-11-07 Apps on Devices troubleshooting guide]]
- [[raw/stripe-terminal-apps-on-devices-troubleshooting-2025|2026-05-01 Apps on Devices troubleshooting guide]]
