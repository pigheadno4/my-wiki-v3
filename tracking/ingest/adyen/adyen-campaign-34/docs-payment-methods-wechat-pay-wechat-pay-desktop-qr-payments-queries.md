# WeChat Pay desktop QR and H5 retrieval check

Q1. Which shopper device paths and setup does this overview distinguish?

For a website desktop browser it describes showing a QR to scan with WeChat Pay and says to add WeChat Pay in Adyen Customer Area; for a mobile browser it describes an H5 redirect to the WeChat Pay app and back, with Adyen Support enrolment using the web shop URL. A merchant mobile-app shopper is routed to the separate in-app flow. The page then links Drop-in, Components and API-only child guides (raw lines 15–27, 33–53). Forward route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-wechat-pay-wechat-pay-desktop-qr-payments]] → [[raw/adyen/docs/payment-methods/wechat-pay/wechat-pay-desktop-qr-payments/2026-09-15]].

Q2. Does this page specify QR expiry, live eligibility or a final result, and does its API-only card override the in-app boundary?

No. Its historical table lists International and ten currencies plus capability symbols, but the overview gives no QR lifetime, API version, callback/webhook or completed payment state (raw lines 29–31). The API-only navigation card mentions website/iOS/Android app, while the body explicitly routes merchant mobile-app shoppers to the separate in-app flow (raw lines 27, 49–51). Neither the table nor child-link copy proves present eligibility or that QR scan, H5 return, authorization or settlement succeeded. Forward route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-wechat-pay-wechat-pay-desktop-qr-payments]] → [[raw/adyen/docs/payment-methods/wechat-pay/wechat-pay-desktop-qr-payments/2026-09-15]].
