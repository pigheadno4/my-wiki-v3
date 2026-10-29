# Oney worker retrieval queries

## Q1 — Purpose and scope

**Query:** What does the Oney overview document, and what does its shopper-facing acceptance message establish?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-oney.md` → `raw/adyen/docs/payment-methods/oney/2026-09-15.md`.

**Evidence locator:** Canonical stem `https://docs.adyen.com/payment-methods/oney`; full pinned raw `raw/adyen/docs/payment-methods/oney/2026-09-15.md`, heading `# Oney`, lines 15–31. It describes an Oney installment redirect and an accepted **installment request**; it does not prove final authorization, capture, settlement or merchant eligibility.

## Q2 — Central capability, prerequisites and warning

**Query:** What regional/method and modification scope does the captured Oney table state, and what conditions matter for capture?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-oney.md` → `raw/adyen/docs/payment-methods/oney/2026-09-15.md`.

**Evidence locator:** Same canonical stem; full pinned raw `raw/adyen/docs/payment-methods/oney/2026-09-15.md`, lines 23–25, 33–41 under `# Oney`, and `## How do you want to integrate?` lines 43–61. The page states a European-country/region entity for compliance checks and purchase-time shopper risk checks. The matrix lists FR/ES/IT, EUR, redirects and specific refund/capture marks; the country table says capture after more than six days requires reauthorization. These snapshot entries do not establish current enablement, a credit decision, or transaction outcomes.
