# Fixed retrieval checks — docs-payment-methods-online-banking-poland-web-drop-in

## Q1 — Find purpose and Sessions/Advanced additions

- Query: What does Adyen's Poland online banking Web Drop-in page require in Sessions and Advanced, and does it require a separate `OnlineBankingPL` import?
- Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-poland-web-drop-in.md` → `raw/adyen/docs/payment-methods/online-banking-poland/web-drop-in/2026-09-15.md`.
- Expected: Existing Web Drop-in Sessions flow, Checkout API v68+, redirect handling and method added in Customer Area (raw lines 25–36); `shopperEmail` required and at most 50 characters for `/sessions` (40–46). Existing Advanced Web Drop-in flow and redirect handling (290–300); required email at most 50 characters, issuer listed as selected bank ID with no required mark (316–323). Individual `OnlineBankingPL` import is optional tree shaking in both flows (270–280, 302–312). This is a method-specific add-on to the PL/PLN Przelewy24 overview `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-poland.md`.
- Scope: The Checkout API v68 minimum is stated in Sessions only. A redirect action does not establish final payment or current merchant eligibility.

## Q2 — Recover examples, redirect and live readiness warnings

- Query: What do the Poland online banking Web Drop-in TEST requests, redirect response and live guidance establish, and what must be qualified?
- Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-poland-web-drop-in.md` → pinned raw.
- Expected: TEST v71 Sessions PL/PLN example shows mobile-style `adyencheckout://your.package.name` in a Web guide, and some SDK snippets omit constructing the request object (raw lines 48–69, 71–136, 250–268). TEST v72 Advanced examples show `onlineBanking_PL` and issuer `141`, but the issuer row is unmarked, so example presence is not universal requiredness (320–349, 351–655). Both curl commands lack continuation after `-X POST` (57–58, 334–335). Advanced guide link embeds an unresolved platform template (298). `RedirectShopper` with `action.type: redirect` is a redirect step (657–671). Test status is checked in Customer Area payment list; live acceptance requires a request in live Customer Area (282–288, 673–679).
- Scope: These are 2026-09-15 captured instructions and TEST examples, not live payment or account proof.
