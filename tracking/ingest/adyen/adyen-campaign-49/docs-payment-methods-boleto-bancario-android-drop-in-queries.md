# Boleto Bancário Android Drop-in retrieval checks

## Q1 — Purpose, scope and payment status

Query: What does the captured Boleto Bancário Android Drop-in page add, and does a voucher response prove payment?

Expected route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-boleto-bancario-android-drop-in.md` → `raw/adyen/docs/payment-methods/boleto-bancario/android-drop-in/2026-09-15.md`. Canonical stem: `/payment-methods/boleto-bancario/android-drop-in`; raw heading `# Boleto Bancário Android Drop-in` at line 15. Expected answer: a 2026-09-15-captured add-on to existing Android Drop-in Sessions/Advanced integrations, with request fields, optional UI configuration and an Advanced voucher action. `PresentToShopper` and voucher issuance do not prove offline payment. The approved `source-adyen-docs-payment-methods-boleto-bancario` method overview explains Boleto de Proposta and shopper payment routes, not this child's implementation. Child raw lines 15–23, 165–181; overview pinned raw lines 23–35. No current live merchant enablement or executed payment is established.

## Q2 — Flow fields, due date, and test/live lifecycle

Query: Which fields and prerequisites differ between Sessions and Advanced, and what do due date and offer status mean?

Expected route: same root/provider/concept/source/raw chain, then the linked approved Boleto overview for its separate status statement. Sessions requires an existing Android Drop-in flow, Checkout API v68+, Customer Area setup, and required shopperName, billingAddress and socialSecurityNumber; optional **deliverAt** is an ISO 8601 UTC due date, with five-day default and next-working-day weekend/holiday qualification (child raw lines 25–49). Advanced requires voucher-action handling and required paymentMethod.type **boletobancario** plus those shopper fields, but calls the optional due-date key **deliveryDate** (child raw lines 106–154). The default payment text says process only after confirmation and no amount mismatch; optional custom shopperStatement should reject higher/lower amounts and post-due payments (child raw lines 49–58, 154–163). The overview says unpaid transactions remain open in Customer Area for 15 days after the due date before Boleto expires and becomes Offer cancelled (overview raw line 39), which does not establish late-payment acceptance. In test, manual offer promotion simulates payment/reconciliation; live use needs a separate live Customer Area request (child raw lines 88–104, 179–197).
