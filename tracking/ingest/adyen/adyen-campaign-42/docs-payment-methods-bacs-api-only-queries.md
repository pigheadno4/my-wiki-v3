# Fixed-query evidence — BACS API-only

Canonical source stem: `source-adyen-docs-payment-methods-bacs-api-only`
Retrieval route: `[[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-bacs-api-only]]`

## Q1 — Purpose, scope, and inference boundary

This 2026-09-15 page adds BACS Direct Debit to an **existing Web API-only Advanced-flow** integration, with merchant-built UI, method discovery, bank-detail payment, token and test/live instructions (raw lines 15–47, 343–353, 729–792). It does not establish current merchant enablement, successful UI certification, a valid DDI or cleared/settled funds. The Advanced example's `Received` result is not final success; the page says webhooks track whether payment succeeded (raw lines 714–727, 780). The BACS overview supplies clearing, DDI and chargeback context.

## Q2 — Central capability, prerequisites, and warnings

Adyen strongly recommends Drop-in/Component because BACS must certify the shopper UI; without them the method **may** be disabled and chargebacks may follow (raw line 19). Existing API-only integration and BACS Customer Area setup are prerequisites, with action handling labeled `Direct` (raw lines 25–31). `/paymentMethods` uses GB/GBP; `/payments` requires shopper email, `directdebit_GB`, holder name, account number and bank location ID (raw lines 45–73, 330–353). The high-level purchased-item step has no matching BACS-specific field in the dedicated table (raw lines 33–37, 343–353). Prose states `Direct`, but its adjacent JSON shows `voucher` with a PDF mandate URL and `Received`, so action and outcome must be confirmed elsewhere (raw lines 714–727). Initial token creation uses shopper reference and `storePaymentMethod: true`; conditional `recurring.token.created` supplies the ID for later `ContAuth` debit. Changed collection date/amount requires advance notice under the cited Guarantee, while explicit permission and notice before each debit are strongly recommended on this page (raw lines 729–780). Live acceptance needs a request in the live Customer Area (raw lines 782–792).
