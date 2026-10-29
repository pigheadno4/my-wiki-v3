# Pix Flutter Component retrieval checks

## Q1 — identity, flow and payment proof

Query: What does the captured Pix Flutter Component add to Sessions and Advanced, and does a Pending QR response prove payment success?

Expected route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` Sources → `wiki/sources/adyen/source-adyen-docs-payment-methods-pix-flutter-component.md` → `raw/adyen/docs/payment-methods/pix/flutter-component/2026-09-15.md`. Canonical stem: `/payment-methods/pix/flutter-component`.

Expected answer: This dated method add-on assumes existing Flutter Components; Sessions states Checkout API v68+, Customer Area setup and an amount field (raw `## Sessions flow Component` lines 25–48). Advanced names `action.type: qrCode`, requires front-end paymentMethod and amount in its method-specific table, and returns a Pending response with qrCodeData (raw `## Advanced flow Component` lines 530–565 and response lines 1053–1073). Pending/QR display is not final paid status, and these examples do not establish current merchant eligibility or a live payment. Both integration-type links point to Flutter Drop-in base guides despite Components labels (lines 31 and 538); use the correct flow-specific Components route.

## Q2 — field limits, expiration, refunds and test boundary

Query: Which Pix Flutter Component request limits and test/live qualifications matter, and which sample or base-guide conflicts must be preserved?

Expected route: same root/provider/concept/source/raw chain, with pinned raw lines 37–48, 50–90, 505–528, 530–565 and 1053–1092; canonical stem `/payment-methods/pix/flutter-component`.

Expected answer: Sessions marks amount required, leaves shopperName/CPF-or-CNPJ and lineItems unmarked, and gives shopperStatement a 140-character maximum. Advanced marks paymentMethod and amount required, advises shopperName plus socialSecurityNumber, and says a supplied shopperStatement stays under 60 characters. Advanced sessionValidity defaults to one hour on Checkout API v71 or earlier or 24 hours on v72 or later (raw lines 560–563); fixed 2021/2025 example dates are historical. The page says refunds within 90 days through Customer Area/API, while test simulation promotes pending offers to sale and live acceptance needs a live Customer Area request (lines 511–528, 1075–1092). Sessions examples differ on paymentMethod/sessionValidity, and both prerequisite links misroute Components to Drop-in; the Advanced action link uses a redirect anchor although the action type is qrCode. The Pix table calls required `/payments.paymentMethod` `state.data.paymentMethod` (Pix raw line 556), whereas the Flutter Components Advanced base guide describes `onSubmit` returning `data` and `/payments.paymentMethod` as the complete event `payload` (base raw `raw/adyen/docs/online-payments/build-your-integration/advanced-flow/2026-09-15.md`, lines 22256–22269 and 22332–22341). The web-style property path is not a verified Flutter Components field. No actual refund, reconciliation, approval or final payment is demonstrated.
