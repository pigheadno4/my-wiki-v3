# Retrieval queries — docs-payment-methods-dana-web-component

## Q1 — purpose and limits

**Query:** What does the DANA Web Component guide cover, and what cannot be inferred from it?

**Answer:** It is a DANA-specific supplement for existing Web Components: Sessions and Advanced redirect routes plus a separate recurring-token section. This page does not itself establish current ID/IDR merchant eligibility, a working account, successful redirect return, authorization or settlement. Its IDR amounts are recurring example values; the DANA overview separately describes ID/IDR and display constraints. The page's live request gate is in LIVE Customer Area, and the phrase “test successful DANA live payments” appears beside TEST Customer Area status guidance; neither is operation proof. Raw lines 15–23, 74–111, 312–320, 322–399 and 600–608; canonical source stem [[source-adyen-docs-payment-methods-dana-web-component]].

**Forward route:** [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-dana-web-component]] → [[raw/adyen/docs/payment-methods/dana/web-component/2026-09-15]].

## Q2 — setup, recurring and snippet warning

**Query:** What are the Sessions/Advanced prerequisites, and why should the Redirect and no-extra-fields examples be qualified?

**Answer:** Sessions requires an existing Web Components Sessions flow, Checkout API v68+, redirect handling and DANA in Customer Area. Advanced requires an existing Advanced flow, redirect handling and Customer Area addition, but its requirement table does not independently restate v68+. Both import `Redirect`; the displayed constructor writes `type:dana` without quotes and defines no `dana` variable, so it cannot be assumed ready to copy. No extra DANA-specific base `/sessions` or `/payments` fields are stated, but recurring `/payments` adds `storePaymentMethod` and `shopperReference`; `recurring.token.created` delivers the stored ID after initial settlement, and later payments use the stored ID, `ContAuth`, and an interval-specific model. Raw lines 25–72, 74–111, 322–399; canonical source stem [[source-adyen-docs-payment-methods-dana-web-component]].

**Forward route:** [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-dana-web-component]] → [[raw/adyen/docs/payment-methods/dana/web-component/2026-09-15]].
