---
title: "WeChat Pay in-app iOS Drop-in integration"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/wechat-pay/wechat-pay-in-app-payments/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/wechat-pay/wechat-pay-in-app-payments/ios-drop-in/2026-09-15.md"
tags: [adyen, wechat-pay, ios, drop-in, in-app]
---

## Overview

This 2026-09-15 snapshot of Adyen's iOS **in-app WeChat Pay Drop-in** guide describes adding the method to an existing iOS Drop-in integration. It distinguishes Sessions and Advanced prerequisites, native app setup, method-specific request/configuration scope, and historical TEST/LIVE limitations. It does not itself specify a full server/client payment sequence or demonstrate payment completion. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Existing flow and merchant setup:** choose the server-side flow already implemented. Sessions requires an existing Sessions-flow iOS Drop-in; Advanced requires an existing Advanced-flow iOS Drop-in. Both requirement tabs say to add WeChat Pay in Customer Area first. The page does not state a Checkout API minimum for either tab. (raw lines 21–37)
- **WeChat and iOS preparation:** the guide calls for a WeChat Open Platform developer account and registered mobile app, with details delegated to the linked enablement guide. In Xcode it says to register the WeChatPay app ID as a URL scheme with identifier `weixin`, add `weixin`, `weixinULAPI`, and `weixinURLParamsAPI` to `LSApplicationQueriesSchemes`, and add Adyen's WeChat Pay dependency via CocoaPods or Carthage. These are setup instructions, not evidence that an app, merchant, or native credential is approved or configured. (raw lines 39–69)
- **Adyen request and Drop-in scope:** the page says no additional WeChat Pay-specific fields are needed; optional fields are directed to the relevant `/sessions` or `/payments` API reference. It describes `/sessions` as the default with iOS Drop-in **v5.0.0 or later** and `/payments` for an additional use case. Its separate v5.0.0-or-later and v4.x.x tabs both say there is no required WeChat Pay-specific Drop-in integration. This is a method-specific add-on statement, not a waiver of the chosen base integration or an API-version guarantee. (raw lines 71–86)
- **Historical TEST/LIVE boundary:** the page states WeChat Pay has no test platform and suggests, for a personal WeChat account, cancelling at payment verification or making a low-value live payment as testing paths. Those are the page's historical suggestions, not an instruction to run a payment here or proof of a TEST environment. It points to Customer Area's payment list for status and says a request in **live Customer Area** is needed before accepting live WeChat Pay. It reports no observed authorization, webhook, capture, settlement, or refund outcome. (raw lines 88–97)

## Detail locators

- Flow-specific Sessions and Advanced requirements: raw lines 21–37.
- WeChat account/app registration links, Xcode URL schemes and dependency options: raw lines 39–69.
- API-reference routing and version-qualified Drop-in statements: raw lines 71–86.
- No-test-platform statement, historical test suggestions, status lookup and live request: raw lines 88–97.
- Further iOS, tokenization and API references are navigation only: raw lines 99–104.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-wechat-pay]]
- [[source-adyen-docs-payment-methods-wechat-pay-wechat-pay-in-app-payments-api-only]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/wechat-pay/wechat-pay-in-app-payments/ios-drop-in/2026-09-15|Adyen WeChat Pay iOS Drop-in, 2026-09-15 snapshot]]
