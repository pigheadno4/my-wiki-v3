# Fixed queries — Gift card iOS Drop-in

## Q1 — /sessions and /payments integration scope

**Query:** What does the captured iOS Drop-in gift-card guide require by endpoint, and which prerequisites remain?

**Expected answer:** https://docs.adyen.com/payment-methods/gift-cards/ios-drop-in is a page last modified 2025-08-11 and captured 2026-09-15. It assumes existing iOS Drop-in and intended test variants in Customer Area; it says no extra gift-card request fields, /sessions is the stated default from Drop-in v5.0.0, and /payments is for an additional use case (full pinned raw/adyen/docs/payment-methods/gift-cards/ios-drop-in/2026-09-15.md, ## Requirements and ## API reference lines 23–38). The /sessions tab says no required gift-card-specific iOS Drop-in integration (lines 40–48). The /payments tab uses checkBalance→/paymentMethods/balance, requestOrder→/orders with total transaction amount if balance is short, and cancelOrder→/orders/cancel (lines 50–62); the Swift sample is a placeholder, not full server code (lines 64–81). Base integration and provider onboarding still apply. Route: wiki/index.md → wiki/adyen-index.md → wiki/concepts/adyen-online-payments.md → wiki/sources/adyen/source-adyen-docs-payment-methods-gift-cards-ios-drop-in.md.

## Q2 — result, asynchronous outcome and test/live boundary

**Query:** How should the iOS gift-card result, simulator codes and live prerequisites be interpreted?

**Expected answer:** The page says to show a shopper-facing result using /payments response resultCode and also receive payment outcome asynchronously by webhook. It lists Authorised, Cancelled, Error and Refused; manual capture is an extra step only when that capture mode is used (pinned raw/adyen/docs/payment-methods/gift-cards/ios-drop-in/2026-09-15.md, ## Show the payment result lines 83–94). Provider-dependent test-card/amount-suffix cases simulate outcomes in TEST, with Payment list as the status check; they are not production guarantees (## Test and go live lines 96–117). Before live acceptance, onboard with a provider, add the variant in live Customer Area and contact Support; real-detail small-amount live tests are described afterward, not evidenced by the page (lines 119–125). The method overview is wiki/sources/adyen/source-adyen-docs-payment-methods-gift-cards.md. Route: wiki/index.md → wiki/adyen-index.md → wiki/concepts/adyen-online-payments.md → wiki/sources/adyen/source-adyen-docs-payment-methods-gift-cards-ios-drop-in.md.
