# Swish React Native Drop-in retrieval check

## Q1 — Purpose, scope, and limits

The 2026-09-15 page is a Swish-specific add-on to existing React Native Drop-in integrations, split between Sessions and Advanced server-side flows (raw lines 15–25, 57–67). It gives prerequisites and TEST/LIVE setup rather than a full QR display, shopper-return or final outcome procedure; no current enablement or executed transaction follows from the dated text (raw lines 39–55, 69–87). Route: `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-swish-react-native-drop-in]]`.

## Q2 — Central capability, prerequisites, and warnings

Sessions requires an existing React Native Drop-in integration, Checkout API v68+ and Swish in Customer Area; it states no Swish-specific `/sessions` fields or configuration (raw lines 29–47). Advanced requires an existing Advanced Drop-in integration, `action.type: qr` handling and Swish in Customer Area, with no extra method-specific configuration or `/payments` fields (raw lines 61–79). Both flow sections describe a 15-second TEST authorization, simulator refusal codes in `shopperStatement`, TEST status inspection and a separate live Customer Area request (raw lines 49–55, 81–87). The Sessions prerequisite URL points to Advanced flow, and the Advanced QR-action link points to a `#handle-the-redirect` anchor; these are navigation conflicts, not proof that the action is redirect or that the flow is Advanced (raw lines 33, 41, 65–66). Route: `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-swish-react-native-drop-in]]`.
