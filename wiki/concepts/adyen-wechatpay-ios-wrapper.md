---
title: "Adyen WeChat Pay iOS Wrapper"
type: concept
category: technology
tags: [adyen, wechat-pay, ios, xcframework, mobile-sdk, wallet]
---

## Adyen WeChat Pay iOS Wrapper

The Adyen WeChat Pay iOS wrapper packages Tencent's static WeChat SDK as the `AdyenWeChatPayInternal` XCFramework. Its purpose is distribution and integration convenience for Swift Package Manager, CocoaPods, Carthage, and direct Xcode embedding; it is not Adyen's shopper-facing checkout Component.

## Current baseline

The first retained baseline is `AdyenWeChatPayInternal@2.2.0` at exact SHA `1127f793854d8624dbe6741d5c42be39dadd4f93`. It embeds WeChat SDK `2.0.4`, requires iOS 12, and documents Xcode 11 for direct framework embedding and Xcode 12 for Swift Package Manager.

The separately versioned `AdyenWeChatPay` module in [[adyen-ios-sdk]] integrates this dependency into Adyen's payment flow. Questions about payment-method presentation, Adyen actions, `/payments`, or final status belong to that SDK and merchant-server evidence rather than this wrapper alone.

## Native handoff contract

The public headers expose application registration with an app ID and Universal Link, URL and Universal Link return handling, installation and API-availability checks, request submission, and asynchronous delegate callbacks.

For payments, `PayReq` carries partner ID, prepay ID, nonce, timestamp, package, and signature. `PayResp` carries the SDK response error fields and a return key. These callbacks report the native WeChat handoff result; they do not establish Adyen authorization, capture, settlement, or fulfillment.

## Distribution and runtime boundary

The podspec publishes a vendored XCFramework with an iOS 12 deployment target. A manually dispatched GitHub workflow pushes the podspec to CocoaPods using a repository secret. The retained source includes public headers and package metadata, while the executable implementation remains an opaque binary whose behavior is delegated to Tencent's SDK.

> [!warning] Contradiction
> The XCFramework manifest lists an `ios-arm64_x86_64-simulator` slice, but the README says the static WeChat library does not support arm64 simulators and the umbrella header suppresses the WeChat headers whenever `TARGET_IPHONE_SIMULATOR` is set. Use a physical device for dependable integration testing.

## Query boundary

- Use this page for package identity, embedded WeChat SDK version, public native request/response interfaces, platform requirements, and distribution.
- Use [[adyen-ios-sdk]] for Adyen Component configuration, checkout orchestration, actions, and merchant-server handoffs.
- Use official Adyen and WeChat product documentation for merchant eligibility, app registration, regional availability, and current production requirements.
- Treat app return callbacks as intermediate client evidence until the merchant backend confirms the payment lifecycle.

## Related

- [[source-github-adyen-wechatpay-ios]] - cumulative exact-SHA wrapper evidence
- [[changelog-github-adyen-wechatpay-ios]] - package-qualified release history
- [[adyen-ios-sdk]] - independently versioned Adyen checkout Component owner
- [[source-github-adyen-ios]] - exact Adyen iOS repository evidence
- [[adyen]] - company and knowledge-status page
