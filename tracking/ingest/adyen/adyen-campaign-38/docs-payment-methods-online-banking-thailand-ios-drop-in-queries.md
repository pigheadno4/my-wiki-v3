# Online banking Thailand iOS Drop-in — retrieval checks

Canonical source stem: `source-adyen-docs-payment-methods-online-banking-thailand-ios-drop-in`

## Q1 — What is the purpose and scope, and what cannot be inferred?

The 2026-09-15-captured page supplies method-specific additions to an existing iOS Drop-in integration, separated by Sessions and Advanced server-side flows (raw lines 15–25, 58–62). It does not establish current merchant eligibility, available issuer IDs, or a successful live payment or settlement. Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` (`## Sources`) → `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-thailand-ios-drop-in.md` → `raw/adyen/docs/payment-methods/online-banking-thailand/ios-drop-in/2026-09-15.md`.

## Q2 — What are the central capability, prerequisites and warnings?

Sessions requires an existing iOS Drop-in flow with Checkout API v68+ and adding Online banking Thailand in Customer Area; no extra `/sessions` parameters or method-specific configuration are stated (raw lines 29–46). Advanced requires an existing iOS Drop-in flow with `action.type: redirect` handling and Customer Area setup; no extra method-specific configuration or `/payments` parameters are stated (raw lines 62–80). Both sections advise TEST payments using an issuer ID available for the corresponding Component and checking TEST Customer Area; live acceptance requires a separate live Customer Area request (raw lines 48–56, 82–90). Redirect and TEST steps do not establish final authorization. Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` (`## Sources`) → `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-thailand-ios-drop-in.md` → pinned raw above.
