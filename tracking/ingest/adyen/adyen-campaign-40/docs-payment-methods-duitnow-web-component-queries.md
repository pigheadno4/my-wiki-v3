# DuitNow Web Component retrieval check

## Q1 — Purpose, scope, and limits

The canonical stem `source-adyen-docs-payment-methods-duitnow-web-component` is a 2026-09-15 capture of a 2019-modified DuitNow add-on to existing Web Components integrations, with Sessions and Advanced prerequisites (raw lines 6–19, 21–37). It covers Component construction and Customer Area setup, but gives no QR, return, webhook or final outcome procedure and does not establish current merchant eligibility or execution (raw lines 39–98). Route: `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-duitnow-web-component]]`.

## Q2 — Central capability, prerequisites, and warnings

The chosen flow needs an existing Web Components integration and Support-assisted Customer Area addition; no Checkout API minimum is stated (raw lines 21–37). The page says no additional DuitNow-specific fields; `/sessions` is described as default with Components v5.0.0 or later, while `/payments` is linked for an additional use case (raw lines 47–52). Web Components v6 imports `DuitNow` and uses its constructor; v5.x.x or earlier uses `checkout.create('duitnow')` (raw lines 39–45, 64–84). The v6 import link points to Drop-in despite the Components scope (raw line 41). The page calls for real-detail, low-amount test payments and status inspection, and Support must add DuitNow in live Customer Area before live acceptance (raw lines 86–92). Those instructions do not prove an executed payment. Route: `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-duitnow-web-component]]`.
