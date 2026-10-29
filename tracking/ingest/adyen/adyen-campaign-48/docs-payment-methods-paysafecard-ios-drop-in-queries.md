# Fixed queries — PaySafeCard iOS Drop-in

## Q1 — purpose and limits

**Query:** What does the captured PaySafeCard iOS Drop-in page add, and what does it leave to the base guide?

**Expected answer:** The page at `https://docs.adyen.com/payment-methods/paysafecard/ios-drop-in` is a 2026-09-15-captured, method-specific add-on for existing iOS Drop-in Sessions and Advanced flows. It gives shopperReference, configuration, redirect and test/live details; it does not establish current account eligibility, a complete request implementation, or successful payment (full pinned `raw/adyen/docs/payment-methods/paysafecard/ios-drop-in/2026-09-15.md`, `# PaySafeCard iOS Drop-in` lines 15–23, Sessions lines 25–44, Advanced lines 286–312). Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-paysafecard-ios-drop-in.md`.

## Q2 — flow-specific fields and warnings

**Query:** Which PaySafeCard iOS Drop-in Sessions/Advanced prerequisites and method fields are stated, and which source/example tensions matter?

**Expected answer:** Sessions requires existing iOS Sessions Drop-in, Checkout API v68+, PaySafeCard Customer Area setup, and `shopperReference` in `/sessions`; no extra PaySafeCard Drop-in configuration is specified (child `raw/adyen/docs/payment-methods/paysafecard/ios-drop-in/2026-09-15.md`, lines 25–44, 268–272). Advanced requires existing iOS Advanced Drop-in, redirect handling for `action.type: redirect`, Customer Area setup, and `shopperReference` in `/payments`; example response is `RedirectShopper` with redirect action (child lines 286–312, 599–613). Test code is test-only and Support must add PaySafeCard in live Customer Area before acceptance (child lines 274–284, 615–625). **Cross-page warning:** the PaySafeCard overview `wiki/sources/adyen/source-adyen-docs-payment-methods-paysafecard.md`, pinned `raw/adyen/docs/payment-methods/paysafecard/2026-09-15.md` lines 25–27, labels the flow Direct; do not silently override the child redirect requirement. **Example warnings:** Advanced requests omit paymentMethod, Advanced examples use website returnUrl while Sessions uses an app URL, and both curl snippets miss a continuation before `-d` (child lines 55–62, 314–597). The examples are not complete copy-ready requests. Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-paysafecard-ios-drop-in.md`.
