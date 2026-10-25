# Online banking Thailand Android Drop-in — retrieval checks

Canonical source stem: `source-adyen-docs-payment-methods-online-banking-thailand-android-drop-in`

## Q1 — What is the purpose and scope, and what cannot be inferred?

The 2026-09-15-captured page gives method-specific additions for an existing Android Drop-in integration, split by Sessions and Advanced flows (raw lines 15–25, 74–76). It does not itself establish current merchant enablement, a list of available issuers, or a completed live payment. Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` (`## Sources`) → `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-thailand-android-drop-in.md` → `raw/adyen/docs/payment-methods/online-banking-thailand/android-drop-in/2026-09-15.md`.

## Q2 — What are the central capability, prerequisites and warnings?

Sessions requires an existing Android Sessions Drop-in integration, Checkout API v68+, and adding the method in Customer Area; it calls for no extra `/sessions` parameters (raw lines 29–40). Advanced requires an existing Android Advanced Drop-in integration with `action.type: redirect` handling and Customer Area setup, and no extra `/payments` parameters (raw lines 76–82, 106–110). Both sections offer optional `setSubmitButtonVisible` with `true` default, but their Kotlin examples contain malformed placeholder braces (raw lines 42–62, 84–104). TEST instructions refer to available Component issuer IDs without listing them; live acceptance requires a separate request in the live Customer Area (raw lines 64–72, 112–118). Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` (`## Sources`) → `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-thailand-android-drop-in.md` → pinned raw above.
