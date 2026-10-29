# Fixed queries — Multibanco Web chooser

## Q1 — purpose and limits

**Query:** What does the captured Multibanco Web page provide, and what does it leave to other guides?

**Expected answer:** The page at `https://docs.adyen.com/payment-methods/multibanco/web` is a 2026-09-15-captured chooser for website Drop-in/Components child guides and main Web Sessions/Advanced integrations. It contains navigation, not voucher handling, request fields, merchant enablement or proof of a paid voucher (full pinned `raw/adyen/docs/payment-methods/multibanco/web/2026-09-15.md`, `# Multibanco for Web` lines 15–17 and chooser/See also lines 19–36). The separate Multibanco overview `wiki/sources/adyen/source-adyen-docs-payment-methods-multibanco.md`, pinned `raw/adyen/docs/payment-methods/multibanco/2026-09-15.md` lines 23–36, explains voucher redemption after checkout. Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-multibanco-web.md`.

## Q2 — UI and flow routes

**Query:** Which Multibanco Web UI and base-flow paths does the chooser link?

**Expected answer:** Drop-in is the all-in-one website UI route `/payment-methods/multibanco/web-drop-in`; Components routes to `/payment-methods/multibanco/web-component` without specifying a concrete Component class or setup recipe (pinned `raw/adyen/docs/payment-methods/multibanco/web/2026-09-15.md`, `### How do you want to integrate?` lines 19–27). The page says to create the main integration first and links Web Drop-in/Components for both Sessions and Advanced flows (`## See also` lines 29–36). These routes do not prove payment completion; use the chosen child and base guides for actual voucher handling. Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-multibanco-web.md`.
