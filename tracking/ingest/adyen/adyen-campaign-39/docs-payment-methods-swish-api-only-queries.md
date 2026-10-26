# Swish API-only retrieval check

## Q1 — Purpose, scope, and limits

The 2026-09-15 page adds Swish to an existing Adyen Web Advanced API-only integration and links back to the main flow; it is method-specific, not a complete implementation guide (raw lines 15–29). It documents SE/SEK method discovery and a QR or app redirect path (raw lines 55–62, 100–165). It does not establish current eligibility, live setup or an executed payment: a live Swish request is still required in live Customer Area (raw line 233). Route: `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-swish-api-only]]`.

## Q2 — Central capability, prerequisites, and warnings

An existing API-only integration must handle the additional action and add Swish in Customer Area; method discovery specifies `countryCode: SE` and `amount.currency: SEK` (raw lines 23–29, 55–62). The desktop path renders `action.qrCodeData`, the mobile path redirects to `action.url`, and tablet may show either or both; completion is limited to three minutes after initiation (raw lines 39–43, 100–157). Mobile return uses URL-decoded `redirectResult` in `/payments/details`, while the `AUTHORISATION` webhook reports payment outcome; `Pending` and `Received` precede the final webhook (raw lines 181–225). TEST simulator scenarios and a separate live request are documented (raw lines 227–233). The source conflicts on item data versus no extra `/payments` fields and on required `action.type: qr` versus sample `qrCode`; its `/paymentMethods` curl example also lacks a continuation after `-X POST` (raw lines 28, 37, 67–81, 96–98, 139–155). Route: `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-swish-api-only]]`.
