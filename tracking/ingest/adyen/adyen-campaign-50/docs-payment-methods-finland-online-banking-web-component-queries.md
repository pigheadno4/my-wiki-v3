# Fixed retrieval checks — docs-payment-methods-finland-online-banking-web-component

## Q1 — Locate the Web Components integration and its required additions

- Query: For Finland online banking in Adyen Web Components, what must the Sessions and Advanced integrations add?
- Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-finland-online-banking-web-component.md` → `raw/adyen/docs/payment-methods/finland-online-banking/web-component/2026-09-15.md`.
- Expected: Existing Web Components Sessions flow, Checkout API v68+, redirect handling and method enablement (raw lines 25–36); `shopperEmail` in `/sessions` (40–46); `Redirect` import, no extra method config, initialize (342–370). Advanced existing flow and redirect setup (378–410); `paymentMethod.type: ebanking_FI` and `shopperEmail` required, `issuer` required only in Issuer redirect flow, return URL description (412–423); sample redirect action (710–724).
- Scope: The v68 floor is explicitly in Sessions requirements only. The guide is a method add-on. `Redirect` snippets show unquoted `ebanking_FI` and Advanced examples omit the required `paymentMethod`; do not present the snippets as executable as written.

## Q2 — Recover sample and test limitations

- Query: Which Finland online banking Web Component examples and Paytrail testing claims need qualification?
- Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-finland-online-banking-web-component.md` → pinned raw, then separate method overview `wiki/sources/adyen/source-adyen-docs-payment-methods-finland-online-banking.md`.
- Expected: Sessions TEST v71 FI/EUR sample has an app-scheme `returnUrl` in the Web guide, malformed `s.hopper@@example.com`, and missing curl continuation after `-X POST` (raw lines 48–69); both `Redirect` examples contain unquoted `type:ebanking_FI` (369, 409); Advanced TEST v72 curl sample omits required `paymentMethod`, repeats malformed email and missing continuation (418–445). Test with Paytrail test environment/sample data; multiple partial refunds currently cannot be tested (372–376, 726–730). Separate method overview marks multiple partial refunds available, so this captured guide establishes a test limitation, not a demonstrated successful refund test.
- Scope: `RedirectShopper` / `action.type: redirect` is a redirect step, not final payment status (710–724). Raw was captured 2026-09-15; do not infer current live configuration.
