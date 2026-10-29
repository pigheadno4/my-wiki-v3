# Fixed queries — Gift card Web Drop-in

## Q1 — scope, version and partial-payment routes

**Query:** What does the captured gift-card Web Drop-in guide add, and how do /sessions and /payments differ for partial payments?

**Expected answer:** https://docs.adyen.com/payment-methods/gift-cards/web-drop-in is a page last modified 2023-03-10 and captured 2026-09-15 about existing Web Drop-in. It requires intended test variants in Customer Area, gives a v6 import, and says no extra gift-card request fields; /sessions is the default from Drop-in v5.0.0, while /payments is an additional-use-case route (full pinned raw/adyen/docs/payment-methods/gift-cards/web-drop-in/2026-09-15.md, ## Requirements through ## API reference lines 26–48). The /sessions tab says Drop-in handles partial payments automatically (lines 50–58). The /payments tab calls for onBalanceCheck→/paymentMethods/balance, onOrderRequest→/orders with amount, merchantAccount and reference for a short balance, and onOrderCancel→/orders/cancel (lines 60–74). The /payments sample JS is incomplete (lines 80–102), so it is no executable recipe. Base fields and provider onboarding still apply. Route: wiki/index.md → wiki/adyen-index.md → wiki/concepts/adyen-online-payments.md → wiki/sources/adyen/source-adyen-docs-payment-methods-gift-cards-web-drop-in.md.

## Q2 — result, simulator and live prerequisites

**Query:** Which gift-card results and webhook boundaries are documented, and what do test amounts and live steps establish?

**Expected answer:** The guide uses /payments resultCode for shopper-facing status and says the outcome also arrives asynchronously by webhook; listed results are Authorised, Cancelled, Error and Refused. Manual capture is an extra step only for integrations using manual capture (pinned raw/adyen/docs/payment-methods/gift-cards/web-drop-in/2026-09-15.md, ## Show the payment result lines 123–134). Provider-dependent test card numbers and last-three-digit amount suffixes simulate outcomes in TEST, not production guarantees (raw ## Test and go live lines 157–178). Before live acceptance, the page calls for provider onboarding, live Customer Area variant addition and Support setup; real-detail small-amount live testing is then suggested, not shown as having occurred (lines 180–186). The method overview is wiki/sources/adyen/source-adyen-docs-payment-methods-gift-cards.md. Route: wiki/index.md → wiki/adyen-index.md → wiki/concepts/adyen-online-payments.md → wiki/sources/adyen/source-adyen-docs-payment-methods-gift-cards-web-drop-in.md.
