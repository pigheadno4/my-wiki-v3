# Cash App Pay Android chooser retrieval checks

## Q1 — Purpose and proof boundary

Query: What does the Cash App Pay Android page provide, and can it prove flow requirements, payment success or current merchant eligibility?

Expected route: `wiki/index.md` line 10 → `wiki/adyen-index.md` line 2716 → `wiki/concepts/adyen-online-payments.md` Sources → `wiki/sources/adyen/source-adyen-docs-payment-methods-cash-app-pay-android.md` Overview/Detail locators → `raw/adyen/docs/payment-methods/cash-app-pay/android/2026-09-15.md` `# Cash App Pay for Android` lines 15–17 and `## How do you want to integrate?` lines 19–29. Expected answer: a dated Android chooser linking Cash App Pay Drop-in/Components and Sessions base guides. It does not itself define request fields, result finality, version minima or account/payment proof; it concerns Cash App Pay, not Cash App Afterpay.

## Q2 — Integration routes and scope cautions

Query: Which Cash App Pay Android integration routes does the chooser offer, does its Sessions-only base navigation rule out Advanced, and where are result/US-wallet conditions documented?

Expected route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-cash-app-pay-android.md` Key takeaways/Related → `raw/adyen/docs/payment-methods/cash-app-pay/android/2026-09-15.md` lines 19–29; continue to `wiki/sources/adyen/source-adyen-docs-payment-methods-cash-app-pay-android-drop-in.md` or `wiki/sources/adyen/source-adyen-docs-payment-methods-cash-app-pay-android-component.md` for flow/version/result detail, and `wiki/sources/adyen/source-adyen-docs-payment-methods-cash-app-pay.md` → `raw/adyen/docs/payment-methods/cash-app-pay/2026-09-15.md` lines 23–44 for US/USD wallet and conditional adjustment/chargeback context. Expected answer: choose all-in-one Drop-in or prebuilt Components; chooser lists Sessions base routes only, but approved child guides also cover Advanced, so no exclusion follows. Payment result and tokenization rules belong to child guides; the chooser provides no finality or live-success evidence.
