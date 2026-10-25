# KCP bank-transfer Android Drop-in retrieval checks

## Q1 — Purpose, scope, and non-inferences

`source-adyen-docs-payment-methods-bank-transfer-kcp-android-drop-in` is the 2026-09-15 method-specific Android Drop-in add-on for existing Sessions or Advanced integrations (raw lines 15–25, 54–60). It does not establish a complete standalone integration, current account eligibility, a completed transfer or live readiness; the page says no KCP bank-transfer testing credentials exist because authorization requires a Public Identification Certificate (raw lines 50–52, 76–78). Forward route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-bank-transfer-kcp-android-drop-in]] → [[raw/adyen/docs/payment-methods/bank-transfer-kcp/android-drop-in/2026-09-15]].

## Q2 — Central capability, prerequisites, warnings

Sessions requires an existing Android Sessions Drop-in, Checkout API v68+ and Customer Area method setup, with no extra `/sessions` or method configuration parameters stated (raw lines 29–46). Advanced requires an existing Android Advanced Drop-in, redirect handling and Customer Area setup, with no extra method configuration or `/payments` parameters stated (raw lines 56–74). The v68 requirement is stated for Sessions and the redirect requirement for Advanced; the repeated TEST warning says no KCP bank-transfer test credentials because authorization uses a Public Identification Certificate (raw lines 33–35, 52, 60–62, 78). Forward route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-bank-transfer-kcp-android-drop-in]] → [[raw/adyen/docs/payment-methods/bank-transfer-kcp/android-drop-in/2026-09-15]].
