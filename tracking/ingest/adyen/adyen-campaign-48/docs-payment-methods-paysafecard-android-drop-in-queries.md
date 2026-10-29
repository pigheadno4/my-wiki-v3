# Q1 — Purpose, scope and non-inference

What is the purpose and scope of the 2026-09-15-captured PaySafeCard Android Drop-in guide at https://docs.adyen.com/payment-methods/paysafecard/android-drop-in, and what must not be inferred from it?

Answer: It is a method-specific add-on to an existing Android Drop-in integration, split between Sessions and Advanced server flows (pinned raw/adyen/docs/payment-methods/paysafecard/android-drop-in/2026-09-15.md lines 15–25, 286–294). It is not a full standalone Android integration, current eligibility guarantee, proof of live setup, or successful payment evidence. The source routes through [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-paysafecard-android-drop-in]] → [[raw/adyen/docs/payment-methods/paysafecard/android-drop-in/2026-09-15]].

# Q2 — Central capability, prerequisites and warnings

What must be added for PaySafeCard in Android Drop-in Sessions versus Advanced, and what caveats do the raw examples impose?

Answer: Sessions requires an existing Android Sessions Drop-in, Checkout API v68+, Customer Area addition and a required `shopperReference` in `/sessions` (raw lines 25–44). Advanced requires an existing Android Advanced Drop-in, redirect handling, Customer Area addition and required `shopperReference` in `/payments`; it states no minimum API version (raw lines 286–310). Neither section requires extra PaySafeCard Drop-in configuration (raw lines 268–272, 296–300). The Advanced result is `RedirectShopper` with a redirect action, not a final authorization (raw lines 597–611). Test code and live Support gate are at raw lines 613–621. The request examples are abbreviated: Advanced omits `paymentMethod`, some Sessions SDK examples omit request construction, and both curl examples have a line-break syntax flaw; Sessions and Advanced use differing example return URLs (raw lines 50–265, 316–595). The captured method overview labels payment flow “Direct” while the child guide requires a redirect action; keep that qualification visible. See [[source-adyen-docs-payment-methods-paysafecard]] for method-level capability and country/currency tables, not for proof of current acceptance.

Canonical URL stem: https://docs.adyen.com/payment-methods/paysafecard/android-drop-in
Full pinned raw path: raw/adyen/docs/payment-methods/paysafecard/android-drop-in/2026-09-15.md
