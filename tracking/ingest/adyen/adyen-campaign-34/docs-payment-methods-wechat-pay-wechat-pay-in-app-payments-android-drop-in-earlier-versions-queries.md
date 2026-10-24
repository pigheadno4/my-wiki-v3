# Retrieval queries — docs-payment-methods-wechat-pay-wechat-pay-in-app-payments-android-drop-in-earlier-versions

## Q1 — earlier-version Android in-app flow

**Query:** What does the older WeChat Pay Android Drop-in guide require, and how does the app-switch payment start?

**Answer:** The page is titled v4.x.x but states WeChat Pay support from Android Drop-in 3.5.0 onward. Its requirements specify an existing **Advanced-flow** Android Drop-in integration, Customer Area addition, a WeChat Open Platform developer account and mobile-app registration. `/paymentMethods` uses supported `countryCode` and `amount.currency`; CN/CNY are examples, and the WeChat app must be on the shopper device for display. Drop-in returns `paymentComponentData.paymentMethod`; the client passes it to the server for `/payments`, and the server returns the SDK action to the client for the WeChat app switch. The introductory and closing Sessions links conflict with the explicit Advanced requirement. Raw lines 15–56, 359–393 and 425.

**Forward route:** [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-wechat-pay-wechat-pay-in-app-payments-android-drop-in-earlier-versions]] → [[raw/adyen/docs/payment-methods/wechat-pay/wechat-pay-in-app-payments/android-drop-in/earlier-versions/2026-09-15]].

## Q2 — final result and test/live boundary

**Query:** Is a Pending SDK action or WeChat app return a completed payment, and can the page's TEST examples be run on a WeChat test platform?

**Answer:** No. After return to the merchant app, the guide requires `/payments/details`. Its `Pending`/`Received` status means the order was received, with a **final AUTHORISATION webhook** to follow; `Error` and `Refused` have separate shopper actions. The page says WeChat Pay has **no test platform**; it instead suggests canceling at verification or making a low-value live payment with a personal account. It directs status checks and the prerequisite request for live acceptance to live Customer Area. TEST API-client examples and a generic return URL do not prove a usable WeChat test environment, deep-link return, authorization or settlement. Raw lines 359–419.

**Forward route:** [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-wechat-pay-wechat-pay-in-app-payments-android-drop-in-earlier-versions]] → [[raw/adyen/docs/payment-methods/wechat-pay/wechat-pay-in-app-payments/android-drop-in/earlier-versions/2026-09-15]].
