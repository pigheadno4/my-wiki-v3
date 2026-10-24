# Retrieval checks — NaverPay API-only

Q1. What integration and setup does this guide require, and what does its API-only NaverPay flow add?

A1. It assumes an existing API-only Advanced flow with `action.type: redirect` handling and NaverPay added in Customer Area (raw lines 23–29). The form lists NaverPay without extra shopper fields (raw lines 38–44); `/paymentMethods` discovery specifies `countryCode: KR` and `amount.currency: KRW` (raw lines 46–53), with an illustrative `kcp_naverpay` response (raw lines 331–342). The payment example sends amount/reference/returnUrl/merchantAccount and shows `RedirectShopper` plus a redirect action (raw lines 348–367, 624–638). Retrieve via [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-naverpay-api-only]] → [[raw/adyen/docs/payment-methods/naverpay/api-only/2026-09-15]].

Q2. What material conflicts and outcome/test boundaries prevent treating the examples as a finished payment integration?

A2. The flow prose calls for additional item information (raw lines 33–36), but the `/payments` section says no additional parameters are needed (raw lines 344–346); examples lack item data and explicit `paymentMethod` (raw lines 348–367, 389–398, 489–503). TEST v72 Adyen endpoint and redirect examples appear (raw lines 59–74, 352–367, 624–638), yet the page says NaverPay has no test environment (raw lines 640–642). The redirect is intermediate; this page gives no detailed return/webhook or final authorization/capture/settlement proof. Its recommendation to test live was only read, not performed. Retrieve via [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-naverpay-api-only]] → [[raw/adyen/docs/payment-methods/naverpay/api-only/2026-09-15]].
