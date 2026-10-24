---
title: "Adyen WeChat Pay in-app Android Component, earlier versions"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/wechat-pay/wechat-pay-in-app-payments/android-component/earlier-versions"
raw_files:
  - "adyen/docs/payment-methods/wechat-pay/wechat-pay-in-app-payments/android-component/earlier-versions/2026-09-15.md"
tags: [adyen, wechat-pay, android, components, in-app, earlier-versions, online-payments]
---

## Overview

This Adyen earlier-version guide, captured 2026-09-15 with a 2019-07-04 last-modified value, adds **WeChat Pay in-app** to an existing **Advanced-flow Android Components** integration. The title says **Component v4.x.x**, while the body says WeChat Pay is supported from Android Components **3.5.0 and later**; neither statement establishes today's SDK support or merchant eligibility. The Component handles an app switch to the shopper's WeChat app. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Setup and discovery:** The guide requires an existing Advanced Android Components integration and adding the method in Adyen Customer Area. Preparation also points to a **WeChat Open Platform developer account** and registration of the merchant's mobile app with WeChat. For `/paymentMethods`, `countryCode` and `amount.currency` must be supported values; **CN** and **CNY** are examples, not exclusive eligibility limits. Select returned method type `wechatpaySDK`, add the Android WeChat Pay module, and check availability on the device before offering it. The code explicitly says `WeChatPayProvider` only checks availability and is not an actual payment provider. (raw lines 19–70)
- **Server and client roles:** If the shopper chooses the method, the server sends `/payments` with `wechatpaySDK`, an amount, merchant account, reference and return URL. The sample uses Checkout **v72 TEST** and language-library versions as examples, not as a stated API minimum. The `/payments` response carries an `action` for the client; its sample `Pending` and `sdkData.appid` are response examples, not a merchant app-ID configuration or final success. The client passes the action to `WeChatPayActionComponent` to switch apps. (raw lines 70–93, 96–128, 217–244, 377–421)
- **Return and result:** The returning Android `Intent` is passed to the Action Component (via `onCreate` or `onNewIntent` depending on launch mode); observed `actionComponentData` goes to the server's `/payments/details`. Its `resultCode` is used for shopper presentation. **Pending/Received** mean the order was received and the final result will arrive through an **AUTHORISATION webhook**; they are not payment success. The table separately describes Authorised, Error and Refused. An app switch or Intent alone proves neither authorization nor settlement. (raw lines 409–464)
- **Environment and live gate:** Despite TEST endpoints/environment in request and Component snippets, the page says WeChat Pay had **no test platform**. It recommends cancelling at verification using a personal WeChat account, or a low-value **live** payment; neither was performed for this ingest. It also says a WeChat Pay request must be submitted in **live Customer Area** before accepting live payments. A request or Customer Area status check is not evidence of approval or successful processing. (raw lines 79–80, 108–109, 414–416, 466–475)
- **Guide-link mismatch:** Requirements link to the **Advanced** Android Components base guide (raw line 29), but the final 'Android Components integration guide' See also link points to a **Sessions** URL (raw line 481). Preserve the selected flow when following a base guide; this page does not explain the mismatch. (raw lines 25–30, 477–483)

## Detail locators

- Historical version, Advanced prerequisite, Adyen and WeChat setup: raw lines 15–35.
- Discovery, module and availability-only provider: raw lines 37–70.
- Server payment examples and `sdk` action response: raw lines 72–407.
- Android app switch, Intent, `/payments/details` and result-code table: raw lines 409–464.
- No-test-platform guidance, live request and conflicting See also base link: raw lines 466–483.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-android-sdk]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/wechat-pay/wechat-pay-in-app-payments/android-component/earlier-versions/2026-09-15|Adyen WeChat Pay Android Component earlier-version guide, 2026-09-15 snapshot]]
