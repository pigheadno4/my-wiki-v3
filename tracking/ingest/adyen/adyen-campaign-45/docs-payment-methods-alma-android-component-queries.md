# Alma Android Component retrieval checks

## Q1 — Purpose, scope and what not to infer

**Canonical source stem:** `source-adyen-docs-payment-methods-alma-android-component`
**Full pinned raw:** `raw/adyen/docs/payment-methods/alma/android-component/2026-09-15.md`
**Verified locators:** `# Alma Android Component`, lines 15–23; `## Sessions flow Component`, line 25; `## Advanced flow Component`, line 176; `## Test and go live`, lines 342–346.
**Route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-alma-android-component.md` → pinned raw.
**Answer boundary:** This is an Alma Android Components add-on, not a standalone method outcome guide. FR/EUR TEST examples do not prove current eligibility, completed redirect or live payment.

## Q2 — Central capability, prerequisites and warnings

**Verified locators:** Sessions prerequisites and optional fields lines 29–48; app-scheme return example line 64; InstantPaymentComponent lines 88–168; Advanced requirements and optional installments count lines 178–285; HTTPS return example line 300 and redirect response 326–340.
**Answer boundary:** Start with the matching Android Components Sessions/Advanced flow and Customer Area setup; Sessions specifies Checkout API v68+. Import the instant module, plus Compose module when applicable, and create an InstantPaymentComponent. Optional request fields remain optional in the method table; Advanced installments count may be 3 or 4, or omitted for shopper choice. Sessions uses `adyencheckout://your.package.name` as a return URL placeholder while Advanced shows HTTPS; the guide does not reconcile the two or demonstrate a completed app return. Advanced response is a redirect action, not final authorization. Both TEST curl examples put `-X POST` and `-d` on separate lines without shell continuation (raw lines 52–58 and 288–294), so they are illustrative rather than verified copy-ready commands. Live use requires a Customer Area request.
