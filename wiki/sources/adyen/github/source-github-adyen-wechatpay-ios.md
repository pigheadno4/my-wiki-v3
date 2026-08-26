---
title: "GitHub: adyen/adyen-wechatpay-ios"
type: source
date_ingested: 2026-08-26
original_format: github-repo
raw_files:
  - "github/adyen/adyen-wechatpay-ios/snapshots/2026-08-26-1127f79/manifest.json"
tags: [adyen, wechat-pay, ios, xcframework, mobile-sdk, github-repository]
---

## Overview

`adyen/adyen-wechatpay-ios` packages Tencent's static WeChat SDK as the `AdyenWeChatPayInternal` XCFramework. This cumulative page begins with package-qualified release `AdyenWeChatPayInternal@2.2.0` at exact SHA `1127f793854d8624dbe6741d5c42be39dadd4f93`.

Repository: <https://github.com/Adyen/adyen-wechatpay-ios>

## Evidence boundary

- This repository is a distribution wrapper around Tencent's SDK, not Adyen's shopper-facing WeChat Pay checkout Component. That Component belongs to the independently versioned `adyen/adyen-ios` repository.
- The snapshot retains public Objective-C headers, package metadata, workflow metadata, and the XCFramework inventory. The executable implementation is binary and cannot be independently inspected.
- Native request submission and callbacks prove an app-handoff contract. They do not prove Adyen payment authorization, capture, settlement, merchant eligibility, or fulfillment status.
- The capsule retains one iOS-arm64 public-header surface. The outer XCFramework inventory describes an additional simulator slice, but the retained executable slices are not source-level evidence.

## Grounding excerpts

> "This repository provides an XCFramework around the static library for more convenient importing of the WeChat Pay SDK."
>
> `raw/github/adyen/adyen-wechatpay-ios/snapshots/2026-08-26-1127f79/files/README.md:3`

> "Embeded WeChat SDK versions: 2.0.4"
>
> `raw/github/adyen/adyen-wechatpay-ios/snapshots/2026-08-26-1127f79/files/README.md:5`

> "AdyenWeChatPayInternal is just a wrapper around the original WeChat Pay SDK"
>
> `raw/github/adyen/adyen-wechatpay-ios/snapshots/2026-08-26-1127f79/files/README.md:48`

> "Update deployment target to iOS 12"
>
> `raw/github/adyen/adyen-wechatpay-ios/releases/adyenwechatpayinternal/2.2.0/2026-08-26/release-notes.md:4`

## Distribution and platform requirements

The wrapper supports direct XCFramework embedding, Swift Package Manager, CocoaPods, and Carthage. The README requires Xcode 11 or newer for direct embedding, Xcode 12 or newer for Swift Package Manager, and iOS 12 or newer. The podspec publishes the prebuilt XCFramework as a vendored framework with deployment target `12.0`.

The wrapper imports dependent system frameworks and libraries and removes the documented need to add `-Objc` and `-all_load` linker flags. A manually dispatched GitHub workflow publishes the podspec to CocoaPods trunk using a repository secret; that workflow is release-mechanism evidence, not proof that a particular binary was accepted or deployed.

## Native app handoff

`WXApi` registers the application with a WeChat app ID and Universal Link. It exposes handlers for URL and Universal Link returns, checks for WeChat installation and OpenAPI support, opens the WeChat app, and submits requests through `sendReq`. Responses arrive asynchronously through `WXApiDelegate.onResp`; iOS 16 and later can additionally ask the host app for permission before the SDK reads callback data from the pasteboard.

For payments, `PayReq` carries `partnerId`, `prepayId`, `nonceStr`, `timeStamp`, `package`, and `sign`. `PayResp` extends the shared response fields with `returnKey`. A successful `sendReq` completion reports that the request was handed off, and a native response reports the SDK callback result. The merchant server must still use Adyen's payment lifecycle as the authority for authorization and subsequent payment state.

## Simulator contradiction

The outer XCFramework manifest advertises an `ios-arm64_x86_64-simulator` library, including both arm64 and x86_64 simulator architectures. The README nevertheless says the static WeChat library does not support the arm64 simulator, and the umbrella header suppresses all WeChat public-header imports whenever `TARGET_IPHONE_SIMULATOR` is set.

Treat physical-device testing as the dependable integration boundary. The presence of a simulator slice does not establish that the payment API is callable or behaviorally testable on every simulator architecture.

## `2.2.0` release finding

Release `2.2.0` updates the embedded WeChat binary to `2.0.4` and raises the deployment target to iOS 12. No wrapper API migration or breaking change is documented. Broader registration, handoff, request, callback, and installation behavior is the initial cumulative baseline, not change evidence introduced solely by `2.2.0`.

## Query guidance

- Use this source for exact package identity, embedded WeChat SDK version, public native interfaces, platform requirements, and wrapper distribution.
- Use [[source-github-adyen-ios]] for Adyen Component configuration, checkout actions, Sessions or advanced flow, and merchant-server handoffs.
- Use official Adyen and WeChat documentation for current eligibility, app registration, regional availability, and production configuration.
- Recollect this repository or Tencent's delegated SDK evidence when a query requires binary behavior not represented in the retained public headers.

## Related

- [[changelog-github-adyen-wechatpay-ios]] - package-qualified release ledger
- [[adyen-wechatpay-ios-wrapper]] - durable wrapper and query-boundary concept
- [[source-github-adyen-ios]] - parent shopper-facing Adyen iOS checkout SDK
- [[adyen-ios-sdk]] - Adyen iOS integration concept
- [[adyen]] - company and knowledge-status page

## Raw sources

- Snapshot manifest: `raw/github/adyen/adyen-wechatpay-ios/snapshots/2026-08-26-1127f79/manifest.json`
- Release manifest: `raw/github/adyen/adyen-wechatpay-ios/releases/adyenwechatpayinternal/2.2.0/2026-08-26/manifest.json`
- Release notes: `raw/github/adyen/adyen-wechatpay-ios/releases/adyenwechatpayinternal/2.2.0/2026-08-26/release-notes.md`
- README: `raw/github/adyen/adyen-wechatpay-ios/snapshots/2026-08-26-1127f79/files/README.md`
- Podspec: `raw/github/adyen/adyen-wechatpay-ios/snapshots/2026-08-26-1127f79/files/AdyenWeChatPayInternal.podspec`
- XCFramework inventory: `raw/github/adyen/adyen-wechatpay-ios/snapshots/2026-08-26-1127f79/files/AdyenWeChatPayInternal.xcframework/Info.plist`
- Public headers: `raw/github/adyen/adyen-wechatpay-ios/snapshots/2026-08-26-1127f79/files/AdyenWeChatPayInternal.xcframework/ios-arm64/AdyenWeChatPayInternal.framework/Headers/`
