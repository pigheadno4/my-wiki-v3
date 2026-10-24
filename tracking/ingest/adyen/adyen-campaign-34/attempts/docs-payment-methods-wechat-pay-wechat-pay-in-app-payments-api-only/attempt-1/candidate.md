---
title: "WeChat Pay in-app for API only"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/wechat-pay/wechat-pay-in-app-payments/api-only"
raw_files:
  - "adyen/docs/payment-methods/wechat-pay/wechat-pay-in-app-payments/api-only/2026-09-15.md"
tags: [adyen, wechat-pay, in-app-payments, api-only, mobile-sdk]
---

## Overview

This [[adyen]] snapshot, captured 2026-09-15, describes **WeChat Pay in-app payments** through an existing API-only integration and WeChat's iOS or Android mobile SDK, not desktop QR or mini-program checkout. The merchant server creates the Adyen payment, passes returned SDK data to the mobile app, and checks the result after the shopper uses WeChat. See [[adyen-online-payments]] and raw lines 15–19, 47–53, 356–394.

## Key takeaways

- Prerequisites are an existing API-only integration and adding the method in the **test Customer Area**; preparation separately routes merchants to a WeChat Open Platform developer account, mobile-app registration, and WeChat mobile SDK integration. The app should check WeChat availability on the shopper's device before presenting the option. These provider/app steps and Adyen setup are separate; the links contain the detailed onboarding instructions. See raw lines 21–38.
- A `/paymentMethods` request **can** specify a supported country/region and currency; `CN` and `CNY` are examples, not an exhaustive eligibility list. Its response identifies `paymentMethod.type: wechatpaySDK`. When selected, the **server** sends `/payments` with that type. The cURL and library requests show CNY and a `returnUrl` as examples; the cURL endpoint is `checkout-test.adyen.com/v72`, not a stated minimum supported Checkout API version. See raw lines 40–73 and 75–354.
- The illustrated `/payments` response is `Pending` with an `action` of type `sdk` and `sdkData`. Pass the returned `sdkData` to the **WeChat Pay SDK**, which launches WeChat for shopper continuation, then obtain its result. The illustrated `appid`, partner, nonce, prepay and signature values are response examples, not credentials to reuse or proof of payment completion. See raw lines 356–390.
- After the shopper completes the WeChat-app step, the page directs a `/payments/details` request using the SDK `resultCode`. Its prose also specifies encoded `paymentData` and conditions it on `/payments` result codes `AuthenticationNotRequired` or `AuthenticationFinished`; however, the preceding illustrated `/payments` response is `Pending` with no `paymentData`, and all subsequent details examples submit only `details.resultCode`. That prose/example mismatch leaves the exact `paymentData` source for the illustrated SDK path unresolved here; do not treat the snippets as a complete request contract. See raw lines 362–386, 392–413 and 416–628.
- Use the `/payments/details` `resultCode` to display the current shopper result. The table distinguishes `Authorised`, `Error` with `refusalReason`, unresolved `Pending`/`Received`, and `Refused`; for the unresolved states, it explicitly says the final result arrives by **AUTHORISATION webhook**. A WeChat SDK callback, `Pending` API response or shopper-facing display is not itself final authorization, capture or settlement proof. The table's funds-timing statements are historical guidance, not observed receipt. See raw lines 630–641.
- The page says WeChat Pay had **no test platform** at snapshot time; it suggests canceling at verification or making a low-value live payment with a personal WeChat account to test, and separately requires a request in the **live Customer Area** before live acceptance. That is source guidance, not an instruction to execute a provider or financial operation. Its numerous `checkout-test`/`Environment.TEST` code samples therefore do not establish an operational WeChat sandbox. See raw lines 57–73, 87–88, 643–652.

## Detail locators

- API-only and provider/app/SDK preparation, method availability and discovery: raw lines 21–45.
- Server `/payments` request and language-specific TEST examples, including library-version comments and live endpoint-prefix notes: raw lines 47–354. The Go examples label library v10.4.0 but import `/v9/` paths (raw lines 227–234, 534–540); review before copying.
- SDK action/result and `/payments/details` prose/examples mismatch: raw lines 356–628.
- Current display results, asynchronous webhook boundary and test/live guidance: raw lines 630–652.

## Related

- [[adyen-online-payments]]
- [[adyen-android-sdk]]
- [[adyen-ios-sdk]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/wechat-pay/wechat-pay-in-app-payments/api-only/2026-09-15|WeChat Pay in-app API-only guide — captured 2026-09-15]]
