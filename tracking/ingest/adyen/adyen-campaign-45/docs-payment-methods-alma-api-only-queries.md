# Alma API-only retrieval checks

## Q1 — What API-only integration scope does this guide have, and what cannot it establish?

Route `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-alma-api-only]]` → `[[raw/adyen/docs/payment-methods/alma/api-only/2026-09-15]]`. Canonical source stem: `source-adyen-docs-payment-methods-alma-api-only`. Full pinned raw path: `raw/adyen/docs/payment-methods/alma/api-only/2026-09-15.md`. Raw lines 19–42 make this an add-on for an existing Web API-only Advanced integration, merchant-built form, Customer Area setup and redirect handling. FR/EUR discovery and a `RedirectShopper` sample do not prove account enablement, final authorization, capture or live success.

## Q2 — Which discovery, installment and example qualifications matter?

Use the same root/provider/concept/source/raw route. The `/paymentMethods` table specifies FR/EUR (raw 44–51). The `/payments` add-on table lists telephone, email, billing/delivery and optional `alma.installments_count`: 3 or 4, omitted for shopper choice (85–95). The example returns a redirect action (137–150), not a final outcome. Warn that purchased-item prose at line 35 has no matching item field/example (85–135); the Alma `/payments` example omits `paymentMethod` (99–135), uses FR/EUR with en-US locale and four-character postal code (106–129), and both curl snippets omit line continuation before `-d` (60–61/104–105). Test status and live Customer Area request are at 153–157. The page gives no method-specific capture/refund/cancel steps.
