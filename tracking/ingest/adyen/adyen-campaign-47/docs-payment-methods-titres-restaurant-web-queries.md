# Fixed retrieval queries — Titres-restaurant Web chooser

## Q1 — Purpose and scope

**Query:** What does Adyen's captured Titres-restaurant for Web page establish, and what does it leave to child guides?

**Expected:** The page at `https://docs.adyen.com/payment-methods/titres-restaurant/web`, last modified 2022-12-12 and captured 2026-09-15, says it accepts Titres-restaurant on a website and acts as a Drop-in/Components choice (raw lines 6–29). It contains no issuer eligibility, API fields, balance, capture, or transaction result procedure; use the selected child and method overview for details. Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-titres-restaurant-web.md` → `raw/adyen/docs/payment-methods/titres-restaurant/web/2026-09-15.md`. Canonical stem: `https://docs.adyen.com/payment-methods/titres-restaurant/web`.

## Q2 — Method-specific and general routes

**Query:** Which routes should a website implementer use for Titres-restaurant Drop-in versus Components?

**Expected:** The method-specific all-in-one Drop-in child is `/payment-methods/titres-restaurant/web-drop-in` (raw lines 21–23). The prebuilt Components child is `/payment-methods/titres-restaurant/web-component` (lines 25–27). The final line separately links the **general** Web Drop-in and Components guides at `/online-payments/drop-in-web` and `/online-payments/components-web` (line 29). These are navigation links and do not imply identical child requirements or payment success. Route: root index → provider index → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-titres-restaurant-web.md` → full pinned raw `raw/adyen/docs/payment-methods/titres-restaurant/web/2026-09-15.md`.
