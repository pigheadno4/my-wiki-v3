# Retrieval queries — docs-payment-methods-alipay-android-component

## Q1 — purpose and prerequisites

**Query:** How does an existing Android Components integration add Alipay in Sessions versus Advanced flow?

**Answer:** The page is an Alipay-specific add-on for existing Android Components. Sessions requires Checkout API v68+, Alipay added in Customer Area, and handling `action.type: redirect`; no extra Alipay-specific `/sessions` parameters are stated. Advanced likewise requires an existing Advanced integration, Customer Area setup and redirect handling; no extra Alipay-specific `/payments` parameters are stated. The Android client imports `instant` (and `components-compose` for Compose) and launches `InstantPaymentComponent`. The Sessions client gets `alipay` from `checkoutSession`, while Advanced selects it from `/paymentMethods`. The Advanced table does not independently state v68+. Raw lines 23–42, 44–125, 138–175, 179–238.

**Forward route:** [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-alipay-android-component]] → [[raw/adyen/docs/payment-methods/alipay/android-component/2026-09-15]].

## Q2 — live and payment-outcome boundary

**Query:** Does the Alipay Android Component guide establish a region/currency rule or prove a live payment completed after redirect?

**Answer:** No region or currency rule appears in this page. It requires redirect handling in both flows (raw lines 35 and 145), recommends live penny tests, and says a request for Alipay must be submitted in the live Customer Area before accepting live payments (raw lines 128–136 and 240–248). It does not provide a final webhook, authorization, capture, settlement or refund outcome rule. The Component and Customer Area steps alone do not prove live enablement or a completed payment; consult the main integration and lifecycle guides for those states.

**Forward route:** [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-alipay-android-component]] → [[raw/adyen/docs/payment-methods/alipay/android-component/2026-09-15]].
