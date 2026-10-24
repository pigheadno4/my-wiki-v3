# KakaoPay iOS Component retrieval checks

Q1. What does the iOS Component guide require before adding KakaoPay, and where does recurring differ from the base flow?

Sessions requires existing iOS Components, Checkout API v68+, redirect handling and the Customer Area method addition (raw lines 25–36). Advanced requires existing Components, redirect handling and the method addition, with no separate API minimum stated (lines 322–332). The page says no extra KakaoPay-specific base `/sessions` or `/payments` fields (lines 40–48, 363–365), but recurring token creation explicitly needs `storePaymentMethod: true` and a unique `shopperReference` in `/payments` (lines 81–97, 376–392). Forward route: [[index]] → [[adyen-index]] → [[adyen-ios-sdk]] → [[source-adyen-docs-payment-methods-kakaopay-ios-component]] → [[raw/adyen/docs/payment-methods/kakaopay/ios-component/2026-09-15]].

Q2. When is a recurring token usable, and what test/live ambiguity limits the examples?

The guide says the shopper logs into Kakao and confirms the recurring transaction, then `recurring.token.created` follows settlement and supplies `storedPaymentMethodId` for later `ContAuth` with the same shopper reference and Subscription or UnscheduledCardOnFile model (raw lines 88–111; repeated lines 383–406). The examples use TEST and KRW, but the section mixes the phrase “test successful KakaoPay live payments” with test Customer Area status and a separate live Customer Area request (lines 312–320, 607–615). This is not proof of live eligibility or successful authorization/capture. Forward route: [[index]] → [[adyen-index]] → [[adyen-ios-sdk]] → [[source-adyen-docs-payment-methods-kakaopay-ios-component]] → [[raw/adyen/docs/payment-methods/kakaopay/ios-component/2026-09-15]].
