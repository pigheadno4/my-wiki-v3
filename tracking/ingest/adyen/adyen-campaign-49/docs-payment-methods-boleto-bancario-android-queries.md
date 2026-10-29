# Boleto Bancário Android router retrieval checks

## Q1 — What does this captured Android page directly offer?
Expected route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-boleto-bancario-android.md` → `raw/adyen/docs/payment-methods/boleto-bancario/android/2026-09-15.md`.
Expected answer: a short Android router to Boleto Bancário Drop-in and Components child guides. Drop-in is described as all-in-one UI; the Components link names `BoletoComponent` and says “handle the redirect to Boleto Bancário.” That is link text, not proof of a redirect action type or payment outcome. Raw locators: lines 15–27. The approved `wiki/sources/adyen/source-adyen-docs-payment-methods-boleto-bancario.md` separately supports the BR/BRL voucher and offline payment journey.

## Q2 — Which base guides are linked, and what remains unanswered here?
Expected route: same root/provider/concept/source/raw chain.
Expected answer: the page says to create the main integration first and links Android Drop-in and Components for both Sessions and Advanced flows. It does not specify request fields, SDK/API versions, actual action type, voucher expiry, paid status or test/live requirements. Route those to fully read child guides and attribute any method overview facts to the approved overview. Raw locators: lines 29–36.
