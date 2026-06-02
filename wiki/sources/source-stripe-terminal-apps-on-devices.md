---
title: "Stripe Terminal: Apps on Devices"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-terminal-apps-on-devices-2025.md"
tags: [stripe, stripe-terminal, apps-on-devices, android, smartpos, aosp, connect]
---

## Summary

Apps on Devices allows merchants to deploy custom Android POS apps directly onto Stripe smart readers. Included at no extra cost on standard card-present pricing; contact sales for eligibility. Android and React Native SDKs only.

## Key Details

**Two integration modes**:
1. **POS on reader**: merchant POS app + Stripe Reader app share one device; POS is the default launcher; Stripe Reader app takes over during payment, then returns control
2. **POS + consumer-facing app**: POS on separate device communicates with a custom consumer-facing app on the reader via TCP/IP

**App limits**: 200MB APK size, 8GB max device storage.

**S700/S710 specs**: Qualcomm 665, 4GB RAM, 64GB, Android 10, 1080×1920, 420dpi.

**AOSP differences**: no Google Play Services (Firebase/Maps may fail), no notifications, no home screen, USB disabled on production devices. Use DevKit for development.

**Permissions**: auto-granted at install, no runtime prompts, allowlist enforced. Camera/BT/location = experimental. NFC = payments only.

**App lifecycle**: Build → App review → Submit (APK via API) → Deploy (via Deploy API) → Monitor.

**Connect**: requires `controller.is_controller = true` on connected account (single-platform control).

## Raw Sources

- [[stripe-terminal-apps-on-devices-2025]] — verbatim webpage content
