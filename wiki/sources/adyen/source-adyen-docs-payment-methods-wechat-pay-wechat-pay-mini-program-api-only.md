---
title: "Adyen WeChat Pay Mini Program API-only"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/wechat-pay/wechat-pay-mini-program/api-only"
raw_files:
  - "adyen/docs/payment-methods/wechat-pay/wechat-pay-mini-program/api-only/2026-09-15.md"
tags: [adyen, wechat-pay, mini-program, api-only, online-payments]
---

## Overview

This Adyen guide, last modified 2019-09-06 and captured 2026-09-15, describes **WeChat Pay in a WeChat Mini Program** through an **API-only integration**. It separates Mini Program UI calls, the merchant server's Adyen API calls, WeChat's order/prepay step, `/payments/details`, and an asynchronous authorisation webhook. The historical page does not establish present Mini Program or merchant eligibility or successful processing. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Provider and Adyen preparation:** Build the API-only base integration and add **WeChat Pay Mini Program in test Customer Area**. Before accepting payments, create a **WeChat Mini Program account** and give Adyen Support or an Implementation Manager the **Mini Program AppID, entity name and currency**; the page says these details are required so payments are settled to the Adyen account. This is an onboarding instruction, not evidence those details were registered or funds settled. (raw lines 21–40)
- **Client/server boundary:** The Mini Program calls the merchant server using `wx.request`; the server makes all calls to **Adyen**. The sequence diagram routes server `/payments` and `/payments/details` responses back to the Mini Program and separately shows an asynchronous authorisation webhook to the server. The page tells the Mini Program to allow-list a **live** Adyen checkout domain and obtains the shopper's `openid` via `wx.login()` then a WeChat `jscode2session` request using the Mini Program AppID, secret and `jsCode`. Those credential placeholders are not actual keys or permission proof. (raw lines 42–95)
- **Payment request and WeChat handoff:** The Mini Program's merchant-server request shows `paymentMethod.type: wechatpayMiniProgram` and `openid`; the server's `/payments` example adds merchant account, reference, amount and `countryCode: CN`, `currency: CNY` using a **live Checkout v72 URL**. These are example values, not a stated universal country/currency or API-version rule. The prose says Adyen contacts the WeChat server for a `prepay_id`; the response puts it in `redirect.data.package`, and Mini Program `wx.requestPayment()` uses the returned data. A `Pending` sample response and prepay identifier do not show a completed payment. (raw lines 97–203)
- **Result handling:** On the Mini Program payment callback, `res.errMsg` can be `requestPayment:ok`, `requestPayment:fail cancel`, or a failure detail. The Mini Program sends `paymentData` and `details.paymentStatus` to the merchant server, which the prose says calls Adyen `/payments/details`; that response's `resultCode` is shown to the shopper. **Pending/Received** mean an order was received and a final result is expected in an **AUTHORISATION webhook**. `requestPayment:ok`, redirect completion, or the sample `Authorised` response does not prove any real payment, capture or settlement occurred. (raw lines 205–286)
- **Example inconsistency:** The Step 4 heading and prose specify `/payments/details`, but its curl snippet uses a **`/payments` URL** and lacks a comma after `paymentData`; it is not a self-contained executable details request. The sequence diagram's note also calls `wx.requestPayment()` a `/payments/details` request, whereas its arrows and Step 4 prose send that request through the merchant server. Follow the stated client/server boundary and verify details behavior in the linked API reference rather than silently repairing these examples. (raw lines 52–70, 205–255)
- **Environment qualification:** Despite test Customer Area setup and Customer Area status guidance, the page says WeChat Pay **does not have a test platform**. Its examples use live checkout/allow-list domains and it recommends cancelling at verification or making a low-value **live** payment with a personal WeChat account. No provider/account/payment action was performed here; the recommendation and example URLs do not demonstrate current live enablement or a successful charge. (raw lines 25–26, 72–78, 148–169, 288–295)

## Detail locators

- API-only prerequisite, test Customer Area setup and Mini Program account/AppID/entity/currency submission: raw lines 21–40.
- Sequence diagram, server-only Adyen calls, domain allow-list and `openid` retrieval: raw lines 42–95.
- `wechatpayMiniProgram` request, live v72 example, WeChat `prepay_id` and `wx.requestPayment()`: raw lines 97–203.
- Callback values, `/payments/details` prose/snippet mismatch, result table and webhook qualification: raw lines 205–286.
- No-test-platform guidance and live-test advice: raw lines 288–295.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/wechat-pay/wechat-pay-mini-program/api-only/2026-09-15|Adyen WeChat Pay Mini Program API-only guide, 2026-09-15 snapshot]]
