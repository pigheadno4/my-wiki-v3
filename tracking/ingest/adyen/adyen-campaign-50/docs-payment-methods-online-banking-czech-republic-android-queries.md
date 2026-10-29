# Online banking Czech Republic Android router retrieval checks

## Q1 — What does this captured Android page directly cover?
Expected route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-czech-republic-android.md` → `raw/adyen/docs/payment-methods/online-banking-czech-republic/android/2026-09-15.md`.
Expected answer: a short chooser linking an all-in-one Android Drop-in child and an Android Components child whose link text names `OnlineBankingCZComponent` and says it handles redirect. These are routes, not a verified child implementation or transaction outcome. Raw locators: lines 15–27. The approved `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-czech-republic.md` separately supports CZ/CZK and bank-redirect method facts.

## Q2 — Which base integration paths does it link, and what remains outside its scope?
Expected route: same root/provider/concept/source/raw chain.
Expected answer: build the main integration first; links Android Drop-in and Components base guides for both Sessions and Advanced flows. The page does not state required request fields, minimum versions, redirect return/details behavior, test/live setup, account eligibility or payment finality. Route those to fully read child guides. Raw locators: lines 29–36.
