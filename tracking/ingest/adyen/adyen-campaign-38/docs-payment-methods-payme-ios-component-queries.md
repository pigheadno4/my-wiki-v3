# PayMe iOS Component — retrieval checks

Canonical source stem: `source-adyen-docs-payment-methods-payme-ios-component`

## Q1 — What is the page's purpose and scope, and what cannot be inferred?

It is a 2026-09-15-captured guide for adding PayMe to an existing iOS Components integration; the Component presents PayMe and redirects the shopper to the PayMe app, with support stated from iOS Components v4.0.0 (raw lines 15–23). It does not show a current eligible merchant account or a completed live authorization, capture or settlement. Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` (`## Sources`) → `wiki/sources/adyen/source-adyen-docs-payment-methods-payme-ios-component.md` → `raw/adyen/docs/payment-methods/payme/ios-component/2026-09-15.md`.

## Q2 — What are the central capability, prerequisites and warnings?

The page requires an existing Sessions or Advanced iOS Components flow and adding PayMe in Customer Area (raw lines 25–41). `/sessions` is the default for Components v5+; `/payments` is listed for an additional use case, with optional `sku` available only under Checkout API v70+ (raw lines 43–71). v5+ Sessions/Advanced examples use `InstantPaymentComponent` with different delegates; v4.x.x has a separate constructor pattern (raw lines 112–159). The illustrative `/payments` example is JavaScript inside a `swift` fence (raw lines 73–108). Sandbox amount endings simulate Authorised, expiry/cancellation, or creation error without a PayMe app, and the expiry row describes a ten-minute default; simulation does not establish a live result (raw lines 161–171). Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` (`## Sources`) → `wiki/sources/adyen/source-adyen-docs-payment-methods-payme-ios-component.md` → pinned raw above.
