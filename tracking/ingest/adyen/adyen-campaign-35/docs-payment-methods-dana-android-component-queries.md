# Retrieval queries — docs-payment-methods-dana-android-component

## Q1 — purpose and limits

**Query:** What does the DANA Android Component guide cover, and what cannot be inferred from it?

**Answer:** It is a DANA-specific add-on for existing Android Components, with distinct Sessions and Advanced redirect flows plus a recurring-token section. It does not independently supply a country/currency eligibility matrix, DANA-provider onboarding procedure, final redirect-return result contract, or proof that any merchant/account has live access or that a payment authorized or settled. IDR amounts and TEST clients are examples in token-payment snippets; live acceptance requires a DANA request in LIVE Customer Area. Raw lines 15–23, 128–165, 368–374, 376–515, 718–724; canonical source stem [[source-adyen-docs-payment-methods-dana-android-component]].

**Forward route:** [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-dana-android-component]] → [[raw/adyen/docs/payment-methods/dana/android-component/2026-09-15]].

## Q2 — prerequisites and recurring boundary

**Query:** What setup and fields are required for base versus recurring DANA Android payments?

**Answer:** Sessions requires an existing Android Components Sessions flow, Checkout API v68+, redirect handling and DANA added in Customer Area; Advanced requires an existing Advanced flow, additional redirect-action handling and Customer Area addition, without restating v68+ there. Both use `InstantPaymentComponent`, with `dana` from `checkoutSession` or `/paymentMethods` respectively, and no DANA-specific extra **base** request/config fields. Recurring differs: `/payments` token creation adds `storePaymentMethod: true` and `shopperReference`; a `recurring.token.created` webhook supplies the token only after initial settlement. Later token payments add stored ID, shopper reference, `ContAuth`, and an interval-specific recurring model. Recurring examples vary in amount and `returnUrl`; do not treat them as a single universal request. Raw lines 25–125, 128–165, 169–363, 376–515 and 519–713; canonical source stem [[source-adyen-docs-payment-methods-dana-android-component]].

**Forward route:** [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-dana-android-component]] → [[raw/adyen/docs/payment-methods/dana/android-component/2026-09-15]].
