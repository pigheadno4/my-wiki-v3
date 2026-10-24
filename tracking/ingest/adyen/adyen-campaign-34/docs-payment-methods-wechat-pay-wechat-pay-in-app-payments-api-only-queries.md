# Retrieval checks — WeChat Pay in-app API-only

Q1. What does this guide implement, and who handles each step? For an existing API-only integration, Adyen Customer Area setup and separate WeChat developer/app/SDK preparation precede a merchant-server `/payments` call with `wechatpaySDK`. The returned `sdkData` goes to the WeChat mobile SDK for shopper continuation, then the SDK result is checked through `/payments/details`. Raw lines 15–32, 47–53, 356–394.

Q2. Why do the examples not establish a complete test or final payment path? The guide says WeChat Pay has no test platform although the API examples use TEST. Its `/payments/details` prose describes conditional `paymentData` while the illustrated `Pending` `/payments` response lacks it; the cURL details sample includes a top-level `paymentData` placeholder with literal `{hint:...}` markup in its keys, whereas later language-library examples show only `details.resultCode`. `Pending`/`Received` await the AUTHORISATION webhook, and live acceptance separately requires a live Customer Area request. Raw lines 57–73, 362–386, 392–413, 416–628, 638–652.

Forward route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-wechat-pay-wechat-pay-in-app-payments-api-only]] → [[raw/adyen/docs/payment-methods/wechat-pay/wechat-pay-in-app-payments/api-only/2026-09-15]].
