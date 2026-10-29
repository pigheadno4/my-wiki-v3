# Fixed retrieval checks: Bancontact card overview

Canonical source stem: `source-adyen-docs-payment-methods-bancontact-bancontact-card`
Pinned raw: `raw/adyen/docs/payment-methods/bancontact/bancontact-card/2026-09-15.md` (SHA-256 `f4dc699849f25f23318d96fcea5083ea2ca8f382b1d3ee2fbc41142c1ae0a182`)
Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-bancontact-bancontact-card.md`

## Q1 — What is this page for, and what should a reader not infer?

It is the Bancontact **card** method overview for Belgium, captured 2026-09-15 with 2023-04-11 last-modified metadata (`raw/adyen/docs/payment-methods/bancontact/bancontact-card/2026-09-15.md:5-17`). It gives card differences from regular cards (`:25-31`), a BE/EUR capability table (`:35-39`), and route links to Web, iOS, Android, API-only and in-person guides (`:41-71`). It does not specify an end-to-end checkout or establish current merchant eligibility, live bank/card coverage, successful authorization or settlement. Its separate Bancontact app link (`:33`) is a different mobile route, not card-entry behavior.

## Q2 — What capabilities, prerequisites and warnings matter most?

The card path has no CVC, though a co-badged card may still show the CVC field; 3D Secure authentication is mandatory, separate captures are unsupported, and the integration must satisfy European co-badged card regulations (`:25-31`). The historical table labels Debit Card, Redirect, Belgium and EUR; it marks refunds and partial refunds available and separate/partial capture and chargebacks unavailable (`:35-37`). Its recurring mark is limited by the Bancontact Wallet Initiated Program (WIP) footnote (`:37-39`), so it is not an unconditional saved-card or merchant-eligibility claim. Use the linked platform/API-only child guides for implementation steps (`:41-65`) and keep in-person as a separate route (`:67-71`).
