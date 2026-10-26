# Vipps React Native Component retrieval check

## Q1 — Purpose, scope, and limits

The 2026-09-15 page adds Vipps to an existing React Native Components integration, and explicitly says React Native Components do not support Sessions flow here (raw lines 15–29). It covers Advanced-flow method additions, not the full base integration, current enablement or executed payment. The live Customer Area still requires a separate Vipps request before live acceptance, followed by webhook and payment-list status checks for low-amount tests (raw lines 31–41, 121–129). Route: `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-vipps-react-native-component]]`.

## Q2 — Central capability, prerequisites, and warnings

The Advanced path requires an existing React Native Components integration, redirect handling and Vipps in Customer Area; it adds no Vipps-specific configuration (raw lines 35–47). The `/payments` table describes phone prefill, `shopperStatement` fallback to `reference`, a relevant channel and the 100-minor-unit/1.00-NOK minimum; its Required cells are blank (raw lines 51–60). A sample `RedirectShopper`/redirect action is an intermediate handoff, while the live procedure points to `AUTHORISATION` webhook status (raw lines 87–101, 121–129). TEST uses a Vipps test app and test merchant setup; LIVE requires a separate request (raw lines 103–129). The Components prerequisite links to a Drop-in URL, the request sample's `React-native` channel differs from listed channel examples, and curl lacks continuation after `-X POST` (raw lines 39, 59, 64–85). Route: `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-vipps-react-native-component]]`.
