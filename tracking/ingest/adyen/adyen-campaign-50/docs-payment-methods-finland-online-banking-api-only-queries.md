# Online banking Finland API-only retrieval checks

## Q1 — identity, flow and proof boundary

Query: What does the captured Online banking Finland API-only guide cover, and can it prove current issuer availability or a completed payment?

Expected route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` Sources → `wiki/sources/adyen/source-adyen-docs-payment-methods-finland-online-banking-api-only.md` → `raw/adyen/docs/payment-methods/finland-online-banking/api-only/2026-09-15.md` `# Online banking Finland for API only` lines 15–29, `## Build your payment form` lines 38–70, and `## Get Online banking Finland as an available payment method` lines 72–80. Canonical stem: `/payment-methods/finland-online-banking/api-only`.

Expected answer: This is a 2026-09-15-captured add-on to an existing Web API-only Advanced integration with redirect handling and Customer Area setup. FI/EUR discovery and an issuer table are documented, but the default route uses Paytrail bank selection and an alternate merchant-selected issuer route. The captured list is not current availability, and examples or redirect initiation do not prove payment completion. The separate method overview raw is `raw/adyen/docs/payment-methods/finland-online-banking/2026-09-15.md`, not this source's raw_files.

## Q2 — conditional issuer, result and conflicting limits

Query: When is issuer required, what finishes a redirected payment, and how should the examples and refund-testing note be read?

Expected route: same root/provider/concept/source/raw chain; verify pinned child raw `## Add additional parameters to your /payments request` lines 446–455, examples 457–480 and 798–823, `## Handle the redirect` lines 1148–1207, outcome/webhook tables 1209–1225, and `## Test and go live` lines 1227–1231. Canonical stem: `/payment-methods/finland-online-banking/api-only`.

Expected answer: `paymentMethod.type: ebanking_FI` and `shopperEmail` are marked required; `paymentMethod.issuer` is required only for merchant-side issuer selection, while default Paytrail selection omits it. Use returned `action.url`, then URL-decoded `redirectResult` in `/payments/details`. Pending/Received is nonfinal; AUTHORISATION webhooks determine success/failure and OFFER_CLOSED true means timeout/no completion. The page's three-day funds statement is a historical provider claim. Its item-information prose lacks a corresponding named table/example field, and discovery/payment examples contain malformed email and shell syntax. The child says multiple-partial-refund testing is unavailable, while the separately captured overview matrix marks that capability; test coverage is distinct from method support.
