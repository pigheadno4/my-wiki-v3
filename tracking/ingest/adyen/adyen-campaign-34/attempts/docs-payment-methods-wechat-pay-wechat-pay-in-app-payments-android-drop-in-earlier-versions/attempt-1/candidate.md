---
title: "Adyen WeChat Pay Android Drop-in earlier versions"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/wechat-pay/wechat-pay-in-app-payments/android-drop-in/earlier-versions"
raw_files:
  - "adyen/docs/payment-methods/wechat-pay/wechat-pay-in-app-payments/android-drop-in/earlier-versions/2026-09-15.md"
tags: [adyen, wechat-pay, android, drop-in, in-app]
---

## Overview

This 2019-modified, 2026-09-15-captured [[adyen]] guide is titled **WeChat Pay Drop-in v4.x.x integration** and documents an **existing Advanced-flow Android Drop-in** in-app payment route. It separately says WeChat Pay is supported from Android Drop-in **3.5.0 and later**; the title is not a new universal minimum. Drop-in displays the method and switches from the merchant app to the shopper's WeChat app. This is distinct from desktop QR/H5 and Mini Program journeys. [[adyen-online-payments]]

## Key takeaways

- **Preparation and method display:** The requirement table says to use an existing **Advanced** Android Drop-in integration and add WeChat Pay in Customer Area. Preparation links to creating a WeChat Open Platform developer account and registering the merchant mobile app with WeChat. The app must be available on the shopper device for WeChat Pay to appear. `/paymentMethods` uses `countryCode` and `amount.currency`; CN and CNY are examples of supported country/region and currency, not exhaustive eligibility rules. See raw lines 19–46.
- **Client/server handoff:** Drop-in gives the Android client `paymentComponentData.paymentMethod`, which the client sends to its server. The server makes `/payments` with that method; examples use `paymentMethod.type: wechatpaySDK`, CNY, a merchant account and a generic `returnUrl`. The sample URL and app ID in the sample action are placeholders, not registered app credentials or a verified Android return/deep link. The response may include `resultCode: Pending` and an `action` with `type: sdk` and `sdkData`; the server passes the action to the client for Drop-in to launch WeChat. The displayed `/v72/payments` and API-library versions belong to examples, not a stated minimum for this older Drop-in guide. See raw lines 48–56, 58–357 and 359–389.
- **Return and outcome:** After the WeChat app step and redirect back to the merchant app, the guide calls for `/payments/details`. Its result code is used for shopper display: `Authorised`, `Error`, `Pending`/`Received`, or `Refused`. For **Pending/Received**, the guide says the payment order was received and the **final result arrives in an AUTHORISATION webhook**; neither the initial Pending response nor an app return is final success. Its historical statements about expected fund-arrival days do not prove settlement or bank receipt for a particular transaction. See raw lines 359–408.
- **Testing and live gate:** The page says WeChat Pay has **no test platform** in this snapshot; with a personal WeChat account, it suggests canceling at verification (recommended) or making a low-value live payment. It directs payment-status checks to live Customer Area and says to submit a WeChat Pay request there before accepting live payments. These are historical setup/test suggestions, not proof of live account enablement or a completed payment. See raw lines 410–419.

> [!warning] Contradiction
> The page's **requirement table says Advanced flow** (raw line 29), while its introductory Android Drop-in link and closing “See also” link point to **Sessions-flow** guides (raw lines 23 and 425). Follow the explicit Advanced requirement and its `/payments` → action → `/payments/details` instructions for this page; treat the Sessions links as mismatched navigation rather than changing the required flow.

## Detail locators

- Historical title/version, app-switch description, Advanced requirement and WeChat registration links: raw lines 15–35.
- Method discovery and conditional display: raw lines 37–46.
- `/payments` inputs, language-specific TEST examples and response action: raw lines 48–389.
- Return/details/result-code table and webhook-final Pending/Received state: raw lines 391–408.
- No-test-platform guidance and live Customer Area gate: raw lines 410–419.

## Related

- [[adyen-online-payments]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/wechat-pay/wechat-pay-in-app-payments/android-drop-in/earlier-versions/2026-09-15|WeChat Pay Android Drop-in earlier-versions snapshot]]
