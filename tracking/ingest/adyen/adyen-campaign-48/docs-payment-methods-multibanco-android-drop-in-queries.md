# Multibanco Android Drop-in retrieval checks

## Q1 — Purpose and voucher boundary

Query: What does the Multibanco Android Drop-in guide add, and does checkout/voucher creation prove a paid Multibanco transaction?

Expected route: `wiki/index.md` line 10 → `wiki/adyen-index.md` line 2663 → `wiki/concepts/adyen-online-payments.md` Sources → `wiki/sources/adyen/source-adyen-docs-payment-methods-multibanco-android-drop-in.md` Overview/Detail locators → `raw/adyen/docs/payment-methods/multibanco/android-drop-in/2026-09-15.md` `# Multibanco Android Drop-in` lines 15–23 and Sessions/Advanced headings lines 25–46, 67–87. For redemption meaning, follow `wiki/sources/adyen/source-adyen-docs-payment-methods-multibanco.md` → `raw/adyen/docs/payment-methods/multibanco/2026-09-15.md` lines 23–36. Expected answer: a 2026-09-15-captured add-on to an existing Android Drop-in Sessions or Advanced integration; no method-specific extra request/configuration fields, but Advanced voucher-action handling. The shopper must later redeem the voucher at an ATM or via online banking; a created voucher or simulated test sale does not prove real payment completion or current live enablement.

## Q2 — Prerequisites, voucher action and test lifecycle

Query: What are the flow prerequisites and action type for Multibanco Android Drop-in, and how are test offers promoted versus live setup?

Expected route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-multibanco-android-drop-in.md` Key takeaways/Detail locators → `raw/adyen/docs/payment-methods/multibanco/android-drop-in/2026-09-15.md` `## Sessions flow Drop-in` lines 25–65 and `## Advanced flow Drop-in` lines 67–104; method-level voucher/expiry/PT/EUR context at `wiki/sources/adyen/source-adyen-docs-payment-methods-multibanco.md` → `raw/adyen/docs/payment-methods/multibanco/2026-09-15.md` lines 23–36. Expected answer: Sessions requires existing Drop-in, Checkout API v68+, Customer Area setup; Advanced requires existing Drop-in, `action.type: voucher` handling and setup. No **extra Multibanco-specific** /sessions, /payments or configuration parameters are stated; base request requirements still apply. Testing requires a test Customer Area request, then manual promotion of a pending offer to sale under Payments > Offers and reconciliation test. Live acceptance requires a separate live Customer Area request. The overview says voucher reference/entity/amount/expiry and later shopper redemption, so do not equate pending offer with paid status.
