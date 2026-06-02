---
title: "Stripe Terminal: Apps on Devices — Submit Your App"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-terminal-apps-on-devices-submit-2025.md"
tags: [stripe, stripe-terminal, apps-on-devices, app-review, dashboard, webhooks]
---

## Summary

How to upload an Apps on Devices APK to Stripe via the Dashboard and monitor review status.

## Upload Flow (Dashboard)

Terminal → Software → Create app → enter name + package name → Upload APK window:
1. Choose compatible device types
2. Upload APK file
3. Add reviewer instructions (if review required)
4. Enter notification email address(es)
5. Click **Submit for review**

## Monitor Status

| Channel | What it provides |
| --- | --- |
| Email | App review result notification |
| Dashboard | App review status on app details page |
| Webhook | `terminal.device_asset_version.app_review_approved` or `terminal.device_asset_version.app_review_rejected` |

## Raw Sources

- [[stripe-terminal-apps-on-devices-submit-2025]] — verbatim webpage content
