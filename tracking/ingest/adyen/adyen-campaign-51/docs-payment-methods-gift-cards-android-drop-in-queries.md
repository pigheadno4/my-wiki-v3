# Fixed retrieval queries — docs-payment-methods-gift-cards-android-drop-in

## Q1 — Scope and integration route

Query: What does the Android gift-card Drop-in guide add, and which SDK/version and server-side flows does it cover?

Expected route: `wiki/index.md` line 10 → `wiki/adyen-index.md` line 2822 → `wiki/concepts/adyen-online-payments.md` Sources → `wiki/sources/adyen/source-adyen-docs-payment-methods-gift-cards-android-drop-in.md` Overview/Key takeaways → `raw/adyen/docs/payment-methods/gift-cards/android-drop-in/2026-09-15.md` lines 15–67. Expected answer: a 2026-09-15-captured gift-card add-on to an existing Android Drop-in integration, scoped to v5.0.0 or later; earlier versions have a separate guide. Sessions and Advanced each require their respective base Android integration and Customer Area gift-card setup. This add-on requires no *additional* gift-card fields for Sessions `/sessions` or Advanced `/payments`, and no additional Drop-in configuration, while the base flow still applies. Sessions then routes to checkout-session creation; Advanced routes to launch/show.

## Q2 — Partial payments, testing and live qualifications

Query: Does the Android add-on describe gift-card balance/order/callback handling, and what should be inferred from its simulator and live instructions?

Expected route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-gift-cards-android-drop-in.md` Payment-flow boundary/Testing versus live/Detail locators → `raw/adyen/docs/payment-methods/gift-cards/android-drop-in/2026-09-15.md` lines 23–98. For method-level partial-payment context, follow `wiki/sources/adyen/source-adyen-docs-payment-methods-gift-cards.md` → `raw/adyen/docs/payment-methods/gift-cards/2026-09-15.md` lines 19–27. Expected answer: this short Android page does not specify balance checks, `/orders` routing, callbacks or webhook behavior. The overview says insufficient gift-card balance can be combined with another method and added steps vary by integration; base Android and partial-payment guides are the next implementation routes. Test numbers depend on provider; the amount-ending table is simulator-only, and `Invalid Pin`/`Pin tries exceeded` are refusal labels, not supplied credential fields. Live setup calls for provider onboarding, the live variant and Support; no test result establishes live account eligibility or completed payment.
