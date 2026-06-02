---
title: "Stripe Terminal: Apps on Devices — Prepare for App Review"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-terminal-apps-on-devices-app-review-2025.md"
tags: [stripe, stripe-terminal, apps-on-devices, app-review, p2pe, verifone]
---

## Summary

Stripe's app review process for Apps on Devices varies by use case. Manual review is required for P2PE apps and all Verifone deployments. Most non-P2PE Stripe reader apps qualify for automated approval.

## Automated Approval (no manual review)

- Non-P2PE apps on Stripe readers (S700/S710 etc.) — limit compatible device types to Stripe only
- DevKit-only apps — limit compatible device types to DevKit types
- Re-uploading a previously reviewed and approved APK

## Manual Review Process

Stripe downloads and installs the app on a Terminal smart reader and interacts with the payment collection UI using the submitted instructions.

**Timeline**: typically 2 working days; up to 5 working days. May be longer in exceptional periods (e.g. late December). No SLA obligation created.

**Rejection reasons**: unable to follow instructions, features that risk payment data, technical defects preventing full review.

## App Review Guidelines (apply to all apps)

- **Multi-tenant**: platforms should build one app serving all merchants with business-specific config — avoids per-business submissions
- **No keyed card/PIN input**: no UI elements that allow manual entry of PINs, authentication values, or card numbers — always use the Terminal reader for payment collection
- **Sandbox payments**: default to sandbox + DevKit; if live payments required, minimum charge of 1 USD (or equivalent)
- **Fix defects first**: app must install, not crash, and successfully discover/connect to the reader before submission
- **Self-contained instructions**: include login credentials (valid indefinitely), path to payment UI, and full walkthrough — no side-effecting actions (e.g. no real food orders)

## Raw Sources

- [[stripe-terminal-apps-on-devices-app-review-2025]] — verbatim webpage content
