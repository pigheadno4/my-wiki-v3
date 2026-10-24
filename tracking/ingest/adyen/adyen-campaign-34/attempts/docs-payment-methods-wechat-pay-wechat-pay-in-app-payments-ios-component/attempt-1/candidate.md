---
title: "WeChat Pay iOS Component"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/wechat-pay/wechat-pay-in-app-payments/ios-component"
raw_files:
  - "adyen/docs/payment-methods/wechat-pay/wechat-pay-in-app-payments/ios-component/2026-09-15.md"
tags: [adyen, wechat-pay, ios, components, in-app]
---

## Overview

This 2025-modified, 2026-09-15-captured [[adyen]] guide adds **in-app WeChat Pay** to an existing **iOS Components** integration through [[adyen-online-payments]]. The Component renders WeChat Pay on the payment form and initiates an app switch from the merchant's app to the shopper's WeChat app. It is distinct from desktop QR and Mini Program flows; app switch, component creation and Customer Area configuration do not establish a finished payment.

## Key takeaways

- Choose the existing server-side **Sessions** or **Advanced** iOS Components flow and add WeChat Pay in Adyen Customer Area. The page calls `/sessions` the default from **Components v5.0.0**, and `/payments` the route for an additional use case. It says no additional WeChat Pay-specific API fields are required; the linked main integration owns baseline server requests and subsequent action/result handling.
- Before integration, the merchant is directed to create a **WeChat Open Platform developer account**, **register the mobile app with WeChat**, and configure Xcode URL scheme with its registered WeChatPay app ID under identifier `weixin`. The page also lists `weixin`, `weixinULAPI` and `weixinURLParamsAPI` in `LSApplicationQueriesSchemes`, and installing the Adyen WeChat Pay iOS module through CocoaPods or Carthage. These are app/provider and client packaging responsibilities; the page does not show a credential issuance, live permission grant or actual SDK callback.
- For **iOS Components v5.0.0+**, the sample gets a `wechatpaySDKComponentPaymentMethod` and builds a `wechatpaySDKComponent.Configuration` with optional localization. It then says there is no required WeChat Pay-specific Components integration. The **v4.x.x** tab likewise says no required WeChat Pay-specific integration. These statements do not waive the base iOS Components flow or provider app-registration work.
- The page says WeChat Pay has **no test platform** in this snapshot. For someone with a personal WeChat account it suggests canceling when asked to verify (**recommended**) or making a low-value **live** payment; neither is an observed test result. It directs checking live Customer Area Payment list and says a **live Customer Area request** for WeChat Pay is required before accepting live payments. No final `/payments/details` sequence, webhook event/status interpretation, authorization/capture/settlement result, or currency/region rule is supplied here; the linked main iOS integration and webhook references remain separate authority.

## Detail locators

- [[raw/adyen/docs/payment-methods/wechat-pay/wechat-pay-in-app-payments/ios-component/2026-09-15|Pinned raw]], lines 15–39: iOS in-app component, app-switch role and Sessions/Advanced prerequisites.
- Same raw, lines 41–71: WeChat developer/app registration, iOS URL schemes and CocoaPods/Carthage packaging.
- Same raw, lines 73–99: no extra API fields, versioned Sessions/Payments route and v5/v4 component configuration wording.
- Same raw, lines 101–118: no-test-platform statement, suggested personal-account live checks, live Customer Area request and navigation to iOS/Webhooks references.

## Related

- [[source-adyen-docs-payment-methods-wechat-pay-wechat-pay-in-app-payments-api-only]] — separate API-only in-app route.
- [[source-adyen-docs-payment-methods-wechat-pay]] — method overview.

## Raw Sources

- [[raw/adyen/docs/payment-methods/wechat-pay/wechat-pay-in-app-payments/ios-component/2026-09-15|WeChat Pay iOS Component]]
