---
title: "GitHub changelog: adyen/adyen-wechatpay-ios"
type: source
date_ingested: 2026-08-26
original_format: github-repo
raw_files:
  - "github/adyen/adyen-wechatpay-ios/snapshots/2026-08-26-1127f79/manifest.json"
tags: [adyen, wechat-pay, ios, xcframework, changelog, github-repository]
---

## Overview

Chronological release synthesis for `adyen/adyen-wechatpay-ios`. Cumulative integration knowledge belongs in [[source-github-adyen-wechatpay-ios]] and the linked immutable snapshots.

## `AdyenWeChatPayInternal@2.2.0` (2025-03-26)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `AdyenWeChatPayInternal` | Initial baseline | `2.2.0` | `1127f793854d8624dbe6741d5c42be39dadd4f93` | Full |

**Important findings:** The release updates the embedded Tencent WeChat SDK to `2.0.4` and raises the wrapper deployment target to iOS 12.

**Developer or merchant impact:** Applications must support iOS 12 or newer. The delegated WeChat binary changes independently of Adyen iOS, so native handoff regression testing should accompany the wrapper update.

**Migration action:** Confirm the host application's deployment target, app ID and Universal Link registration, URL return handling, physical-device handoff, and merchant-server payment-status confirmation. No source-level wrapper API migration is documented.

**Updated source sections:** Evidence boundary; distribution and platform requirements; native app handoff; simulator contradiction; `2.2.0` release finding; query guidance.

Broader wrapper installation, native request, and callback behavior is the initial cumulative baseline, not release-specific change evidence.

### Evidence gaps

- The executable implementation is retained only as a binary XCFramework; code-level verification of Tencent SDK behavior is unavailable.
- The outer XCFramework advertises a simulator slice, while the README and umbrella header restrict simulator use. Physical-device behavior remains the reliable test boundary.
- This repository does not establish shopper-facing Adyen Component behavior, merchant eligibility, payment authorization, capture, settlement, or fulfillment.

### Evidence

- `raw/github/adyen/adyen-wechatpay-ios/releases/adyenwechatpayinternal/2.2.0/2026-08-26/manifest.json`
- `raw/github/adyen/adyen-wechatpay-ios/releases/adyenwechatpayinternal/2.2.0/2026-08-26/release-notes.md`
- `raw/github/adyen/adyen-wechatpay-ios/snapshots/2026-08-26-1127f79/manifest.json`
- `raw/github/adyen/adyen-wechatpay-ios/snapshots/2026-08-26-1127f79/files/README.md`
- `raw/github/adyen/adyen-wechatpay-ios/snapshots/2026-08-26-1127f79/files/AdyenWeChatPayInternal.podspec`
- `raw/github/adyen/adyen-wechatpay-ios/snapshots/2026-08-26-1127f79/files/AdyenWeChatPayInternal.xcframework/Info.plist`
- `raw/github/adyen/adyen-wechatpay-ios/snapshots/2026-08-26-1127f79/files/AdyenWeChatPayInternal.xcframework/ios-arm64/AdyenWeChatPayInternal.framework/Headers/`
