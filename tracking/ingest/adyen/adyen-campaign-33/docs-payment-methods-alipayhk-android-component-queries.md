# Retrieval checks — Alipay HK Android Component

Q1. What does this page add to an Android Components integration, and what are the flow-specific prerequisites? It adds `alipay_hk` through `InstantPaymentComponent` to an existing Sessions or Advanced integration. Sessions explicitly requires Checkout API v68+, existing redirect handling and Customer Area method addition; Advanced requires its existing integration, additional redirect-action handling and method addition. Neither flow calls for extra method-specific configuration or request parameters. Raw lines 25–42, 67–77, 140–148, 173–183, 236–240.

Q2. What material boundary prevents treating the examples as a live or completed payment? The page gives test credentials and test Customer Area status lookup, while live acceptance needs a separate live Customer Area request. It does not supply final webhook, authorization, capture or settlement proof, and the Sessions v68 requirement should not be silently assigned to Advanced. Raw lines 33–36, 128–138, 144–148, 242–252.

Forward route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-alipayhk-android-component]] → [[raw/adyen/docs/payment-methods/alipayhk/android-component/2026-09-15]].
