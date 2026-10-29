# Fixed retrieval checks — docs-payment-methods-payto-web

## Q1 — Identify chooser purpose and limits

- Query: What does Adyen's PayTo Web page provide, and does it define PayTo agreement or payment behavior?
- Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-payto-web.md` → `raw/adyen/docs/payment-methods/payto/web/2026-09-15.md`.
- Expected: The 36-line page is a Web chooser with Drop-in and Components links (raw lines 15–27), then base-guide links (29–36). It has no request schema, SDK minimum, agreement lifecycle or webhook outcome. The separate overview `wiki/sources/adyen/source-adyen-docs-payment-methods-payto.md` holds method context.
- Scope: Captured 2026-09-15; navigation does not prove merchant eligibility, agreement approval or executed payment.

## Q2 — Recover exact Web routes and prerequisite order

- Query: Which PayTo Web UI and server-side flow choices are linked, and what should be created first?
- Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-payto-web.md` → pinned raw.
- Expected: Drop-in is labeled all-in-one website UI (raw lines 21–23); Components has a PayTo route without naming a concrete class (25–27). Create the main integration first (31), choosing Web Drop-in or Components with Sessions or Advanced base guides (33–36).
- Scope: Use selected child method guide for PayTo fields, bank agreement and final-status detail; do not import that behavior into this chooser.
