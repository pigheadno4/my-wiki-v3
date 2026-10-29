# Alma Web Component retrieval checks

## Q1 — Purpose, scope and what not to infer

**Canonical source stem:** `source-adyen-docs-payment-methods-alma-web-component`
**Full pinned raw:** `raw/adyen/docs/payment-methods/alma/web-component/2026-09-15.md`
**Verified locators:** `# Alma Web Component`, lines 15–23; `## Sessions flow Component`, line 25; `## Advanced flow Component`, line 122; redirect response lines 210–224.
**Route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-alma-web-component.md` → pinned raw.
**Answer boundary:** This is an Alma add-on for an existing Web Components integration. FR/EUR TEST examples, redirect response and Customer Area links do not prove live eligibility or completed payment.

## Q2 — Central capability, prerequisites and warnings

**Verified locators:** Sessions requirements/fields lines 29–48; Web Sessions app-scheme return example line 64; Redirect import/init lines 88–114; Advanced requirements and installments field lines 124–169; HTTPS return example line 184 and redirect response 210–224.
**Answer boundary:** Begin with the appropriate Web Components Sessions/Advanced flow and Customer Area setup; Sessions specifies Checkout API v68+. The method tables leave phone, email and addresses unmarked as required. Advanced can set installment count to 3 or 4, or omit it for shopper choice. Import and initialize Redirect; no extra Sessions method configuration is stated. The Sessions Web sample uses Android-style `adyencheckout://your.package.name`, while Advanced uses HTTPS; the guide does not reconcile the examples. Its JS `{ type:alma }` is illustrative, with `alma` unquoted and undefined in the snippet. Redirect action is not final authorization.
