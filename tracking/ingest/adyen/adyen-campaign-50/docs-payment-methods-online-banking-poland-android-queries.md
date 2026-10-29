# Online banking Poland Android router retrieval checks

## Q1 — What does this captured Android page directly provide?
Expected route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-poland-android.md` → `raw/adyen/docs/payment-methods/online-banking-poland/android/2026-09-15.md`.
Expected answer: a short chooser linking an all-in-one Android Drop-in child and an Android Components child whose label names `OnlineBankingPLComponent` and says it handles redirect. Those are navigation descriptions, not a verified action contract or payment result. Raw locators: lines 15–27. Approved `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-poland.md` supplies P24/PL/PLN bank-redirect method context separately.

## Q2 — Which base integration paths does it link, and what is outside its scope?
Expected route: same root/provider/concept/source/raw chain.
Expected answer: create the main integration first; links Android Drop-in and Components base guides for both Sessions and Advanced flows. The router does not state request fields, version minima, return/details or webhook handling, test/live gates, merchant enablement or payment finality. Read the child guide for implementation claims. Raw locators: lines 29–36.
