# Retrieval checks — WeChat Pay in-app payments

## Q1. What does this page say an in-app WeChat Pay integration does, and which implementation routes does it identify?

It describes payments initiated from a merchant mobile app. It names an existing Android Drop-in or Component integration and a merchant-built WeChat mobile-SDK route (raw line 19). The shopper switches to the WeChat app for verification and returns to the merchant app, where the merchant may present a result (raw line 21). The iOS, Android and API-only entries are child-guide navigation (raw lines 29–47), not on-page registration, SDK-version or device-compatibility instructions. Forward route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-wechat-pay-wechat-pay-in-app-payments]] → [[raw/adyen/docs/payment-methods/wechat-pay/wechat-pay-in-app-payments/2026-09-15]].

## Q2. What capability and outcome limits should be kept with this overview?

Its historical matrix calls this a wallet with `Redirect (App switch)` flow, `International` country/region label, ten enumerated currencies, refunds and partial refunds marked available, and recurring/chargebacks marked unavailable (raw lines 25–27). These marks do not establish current merchant eligibility, registration, platform/device support or a refund procedure. The app return and displayable result described at raw line 21 are not independent authorization, capture or settlement evidence; final-result mechanics belong to child guides. Forward route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-wechat-pay-wechat-pay-in-app-payments]] → [[raw/adyen/docs/payment-methods/wechat-pay/wechat-pay-in-app-payments/2026-09-15]].
