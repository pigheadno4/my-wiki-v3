# Multibanco Android chooser retrieval checks

## Q1 — Purpose and proof boundary

Query: What does the Multibanco for Android page provide, and can it answer request-field, voucher action or live-payment questions by itself?

Expected route: `wiki/index.md` line 10 → `wiki/adyen-index.md` line 2663 → `wiki/concepts/adyen-online-payments.md` Sources → `wiki/sources/adyen/source-adyen-docs-payment-methods-multibanco-android.md` Overview/Detail locators → `raw/adyen/docs/payment-methods/multibanco/android/2026-09-15.md` `# Multibanco for Android` lines 15–17, `### How do you want to integrate?` lines 19–27 and `## See also` lines 29–36. Expected answer: a 2026-09-15-captured integration chooser for Android Drop-in/Components and their Sessions/Advanced base guides. It has no request schema, voucher action lifecycle, live enablement proof or completed-payment evidence; follow the selected child guide and method overview.

## Q2 — Routes and voucher context

Query: Which Multibanco Android integration paths are offered, what must be built first, and where are the voucher lifecycle and implementation details?

Expected route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-multibanco-android.md` Key takeaways/Related → `raw/adyen/docs/payment-methods/multibanco/android/2026-09-15.md` lines 19–36; continue to `wiki/sources/adyen/source-adyen-docs-payment-methods-multibanco-android-drop-in.md` and `wiki/sources/adyen/source-adyen-docs-payment-methods-multibanco-android-component.md` for child-specific routes, and `wiki/sources/adyen/source-adyen-docs-payment-methods-multibanco.md` → `raw/adyen/docs/payment-methods/multibanco/2026-09-15.md` lines 23–36 for method-level voucher/PT/EUR context. Expected answer: choose all-in-one Drop-in or Components with InstantPaymentComponent; the page links both Sessions and Advanced base guides and says to create the main integration first. The Components link's “redirect” wording is navigation, not a new action-type assertion; the method overview explains that the shopper later redeems a voucher at an ATM or through online banking.
