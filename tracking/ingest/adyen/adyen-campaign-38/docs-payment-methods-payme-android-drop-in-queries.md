# PayMe Android Drop-in retrieval checks

## Q1 — Purpose, scope and inference limit

The canonical source [[source-adyen-docs-payment-methods-payme-android-drop-in]] is a 2026-09-15-captured Android Drop-in guide for showing PayMe in a payment form and redirecting the shopper to the PayMe app (raw lines 15–21). It states Android Drop-in 4.0.0 support and an existing Advanced-flow integration with PayMe added in Customer Area (raw lines 21–28). It is a documented integration and sandbox pattern; a redirect, example request or return is not proof of live merchant eligibility, final authorization or settlement (raw lines 166–199). The opening/outcome links use Sessions-flow targets despite the explicit Advanced-flow requirement (raw lines 19, 27, 183–187).

Full retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-payme-android-drop-in]] → [[raw/adyen/docs/payment-methods/payme/android-drop-in/2026-09-15]].

## Q2 — Capability, prerequisites and warnings

The guide says `/paymentMethods` uses HK `countryCode` and HKD `amount.currency` to show availability (raw lines 80–85); the client passes Drop-in's `paymentComponentData.paymentMethod` to the server for `/payments`, and returns the `action` to the client for PayMe-app redirect (raw lines 87–96, 166–187). It says the return URL comes from `RedirectComponent.getReturnUrl(context)`, but prose spells `returnURL` and examples `returnUrl` (raw lines 95–96, 115, 152). The request examples conflict on `channel`: `Android`, `Web`, and `Web/iOS/Android` (raw lines 67, 116, 153). The additional-use-case table leaves Required cells blank (raw lines 30–41), and the early `kotlin` fence contains JS syntax (raw lines 43–54). Sandbox amount endings simulate Authorised, OfferCancelled after ten-minute default expiry, or Error; no PayMe app is needed there (raw lines 189–199). These are dated examples, not observed production outcomes.

Full retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-payme-android-drop-in]] → [[raw/adyen/docs/payment-methods/payme/android-drop-in/2026-09-15]].
