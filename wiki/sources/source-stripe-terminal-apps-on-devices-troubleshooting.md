---
title: "Stripe Terminal: Apps on Devices — Troubleshooting"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-terminal-apps-on-devices-troubleshooting-2025.md"
tags: [stripe, stripe-terminal, apps-on-devices, troubleshooting, android]
---

## Summary

Known issues and resolutions for Apps on Devices deployments.

## Key Issues

**APK upload timeout**: Stripe enforces 45s timeout on uploads. Fix: upload from EC2/VPS with faster internet, then push to Stripe.

**Sandbox → live mode**: sandbox approval doesn't carry over. Must resubmit; upload exact same APK for automatic approval.

**Admin settings access**: swipe-from-left doesn't work when a third-party app is the default launcher. Use `stripe://settings/` deep link. Android Settings app is **blocked on production** devices entirely.

**Multiple apps on S700/S710**: supported but no built-in launcher — must build switching in-app. Configure `default_kiosk_application` via API (not available in Dashboard).

**Web apps**: package via Cordova → APK; needs JS bridge to Android Terminal SDK. Alternative: use server-driven integration (no bridge needed).

**Crash loops**: if app crashes during initialization on production, device enters crash loop. On DevKit, Stripe payment app restarts instead.

**IPC limit**: Android OS limits inter-process data to 500 KB when saving activity state. Large numbers of line items can cause crashes. Fix: store data in DB, not in memory.

**No production logs**: Stripe doesn't expose logs on production readers. Use Sentry or similar third-party library.

**Sideloaded DevKit app won't restart after payment**: preferred kiosk app is only set when device is in a deploy group. Fix: upload app targeting DevKit device types → deploy to a DevKit deploy group.

## Raw Sources

- [[stripe-terminal-apps-on-devices-troubleshooting-2025]] — verbatim webpage content
