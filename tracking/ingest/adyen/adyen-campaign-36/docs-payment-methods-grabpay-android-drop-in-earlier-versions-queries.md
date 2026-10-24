# Retrieval queries — docs-payment-methods-grabpay-android-drop-in-earlier-versions

## Q1 — purpose and limits

**Query:** What does this earlier-version GrabPay Android Drop-in guide cover, and what cannot be inferred?

**Answer:** It is titled v4.x.x and gives an existing **Advanced-flow Android Drop-in** Wallet/PayLater procedure. Its country/currency table has MY/MYR, SG/SGD and PH/PHP, but the footnote excludes **PayLater in the Philippines**. The guide does not prove current merchant or variant enablement, working Android return, successful authorization/capture/settlement or funds receipt. The title and language-specific API/library TEST examples are historical scopes; the introduction and See also Sessions links conflict with its Advanced requirement. Raw lines 15–42, 74–125, 968–981; canonical source stem [[source-adyen-docs-payment-methods-grabpay-android-drop-in-earlier-versions]].

**Forward route:** [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-grabpay-android-drop-in-earlier-versions]] → [[raw/adyen/docs/payment-methods/grabpay/android-drop-in/earlier-versions/2026-09-15]].

## Q2 — Wallet, PayLater and final outcome

**Query:** Which fields differ for Wallet and PayLater, and what confirms a pending payment?

**Answer:** The client passes Drop-in's `paymentComponentData.paymentMethod` to the server for `/payments`. Both paths list a component-derived `returnUrl`, bounded reference and amount. **PayLater** additionally needs delivery address and line items; early collection for Wallet is a recommendation, not its requirement. A `RedirectShopper` action starts the redirect, after which the server posts returned `actionComponentData.details` to `/payments/details`. Pending/Received is not final: the AUTHORISATION webhook gives the final result; if the shopper never returns, the guide says to wait for AUTHORISATION or OFFER_CLOSED webhook outcomes. The generic HTTPS URLs in snippets do not demonstrate a working `RedirectComponent.getReturnUrl(context)` return route. Raw lines 44–70, 373–404 and 877–966; canonical source stem [[source-adyen-docs-payment-methods-grabpay-android-drop-in-earlier-versions]].

**Forward route:** [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-grabpay-android-drop-in-earlier-versions]] → [[raw/adyen/docs/payment-methods/grabpay/android-drop-in/earlier-versions/2026-09-15]].
