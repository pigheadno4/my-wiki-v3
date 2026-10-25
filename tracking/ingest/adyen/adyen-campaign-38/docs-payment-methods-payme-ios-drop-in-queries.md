# PayMe iOS Drop-in retrieval checks

## Q1 — Purpose, scope, and non-inferences

`source-adyen-docs-payment-methods-payme-ios-drop-in` is the 2026-09-15 method add-on for an existing iOS Drop-in Sessions or Advanced integration; Drop-in displays PayMe and redirects to its app, with support stated from iOS Drop-in v4.0.0 (raw lines 15–41). It does not supply a standalone iOS integration, live approval, direct outcome procedure or proof of real payment; the amount-ending outcomes are sandbox simulations and the outcome instructions are delegated to the base guide (raw lines 110–126). Forward route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-payme-ios-drop-in]] → [[raw/adyen/docs/payment-methods/payme/ios-drop-in/2026-09-15]].

## Q2 — Central capability, prerequisites, warnings

Both flows need their corresponding built iOS Drop-in and Customer Area PayMe setup; `/sessions` is described as the default from Drop-in v5.0.0, while the broader support statement starts at v4.0.0 (raw lines 19–49). Optional `channel` and `lineItems` fields are listed for `/sessions` and `/payments`; `lineItems.sku` is specifically available with Checkout API v70+ (raw lines 51–71). The HK/HKD example sends `payme` and `channel: iOS`, but a Swift-labeled fence contains JavaScript; the sandbox uses no PayMe app and amount endings simulate Authorised, OfferCancelled/ten-minute expiry, or Error (raw lines 73–108, 116–126). Forward route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-payme-ios-drop-in]] → [[raw/adyen/docs/payment-methods/payme/ios-drop-in/2026-09-15]].
