# docs-payment-methods-gift-cards-android-drop-in-earlier-versions retrieval checks

## Q1 — Version and scope

Query: What version and flow does this gift-card Android Drop-in guide cover, and which request values determine gift-card availability?

Expected: The 2023-modified, 2026-09-15-captured guide is titled v4.x.x and requires an existing Advanced Android Drop-in integration plus Customer Area setup (raw lines 15–26). /paymentMethods countryCode and amount.currency filter available methods; NL/EUR are examples, not universal gift-card coverage (lines 28–33). The opening link points to a Sessions base guide (line 19), inconsistent with the Advanced requirement, so do not generalize this v4.x.x callback recipe to Sessions or newer SDKs. Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-gift-cards-android-drop-in-earlier-versions]] → [[raw/adyen/docs/payment-methods/gift-cards/android-drop-in/earlier-versions/2026-09-15]]. Full pinned raw: `raw/adyen/docs/payment-methods/gift-cards/android-drop-in/earlier-versions/2026-09-15.md`.

## Q2 — Partial payments and test/live boundary

Query: How does v4.x.x Drop-in handle a low-balance gift card, and what do its test results and live steps establish?

Expected: The Advanced DropInService must implement checkBalance to call /paymentMethods/balance, createOrder to call /orders with the full transaction amount when balance is low, and cancelOrder to call /orders/cancel on shopper cancellation; partial payments follow order creation (raw lines 35–47). The sample updates payment methods after manual gift-card removal and cancels an in-progress order when Drop-in closes (lines 79–96). Provider-dependent test cards and amount suffixes simulate Authorised/Refused/Error, with 100 mapping to Authorised in the simulator only (lines 99–120). The live checklist is provider onboarding, variant addition and Support contact, with possible small-amount real-card end-to-end testing (lines 122–128); none is evidence of actual live execution. Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-gift-cards-android-drop-in-earlier-versions]] → [[raw/adyen/docs/payment-methods/gift-cards/android-drop-in/earlier-versions/2026-09-15]]. Full pinned raw: `raw/adyen/docs/payment-methods/gift-cards/android-drop-in/earlier-versions/2026-09-15.md`.
