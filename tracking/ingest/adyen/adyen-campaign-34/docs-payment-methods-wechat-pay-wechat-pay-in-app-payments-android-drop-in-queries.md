# WeChat Pay Android Drop-in v5 retrieval questions

## Q1 — What is this guide for, and what are prerequisites?

It is the method-specific add-on for **Android Drop-in v5.0.0** (released October 2023); earlier versions have a separate guide (raw lines 15–21). Sessions and Advanced each require their existing Android Drop-in integration at minimum 5.0.0 and WeChat Pay added in Customer Area (lines 23–39). The ordinary `/sessions` or `/payments` request and Drop-in configuration require no **additional WeChat Pay-specific** fields/settings, after which the chosen main flow creates the session or launches Drop-in (lines 41–67). Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-wechat-pay-wechat-pay-in-app-payments-android-drop-in]] → [[raw/adyen/docs/payment-methods/wechat-pay/wechat-pay-in-app-payments/android-drop-in/2026-09-15]].

## Q2 — What are the testing and outcome limits?

This snapshot says WeChat Pay has no TEST platform; it describes personal-account cancellation at verification or low-value **live** payment as testing options, without verifying either (raw lines 69–74). Payment status is checked in the live Customer Area and accepting live payments requires submitting a WeChat Pay request there; neither step proves account approval or a completed payment (lines 76–78). The guide supplies no detailed SDK app-switch, action-response or final webhook contract; older-version and API-only result paths remain separate authority (lines 19–21, 80–86). Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-wechat-pay-wechat-pay-in-app-payments-android-drop-in]] → [[raw/adyen/docs/payment-methods/wechat-pay/wechat-pay-in-app-payments/android-drop-in/2026-09-15]].
