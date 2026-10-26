# Swish iOS Drop-in retrieval checks

Route: `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-swish-ios-drop-in]]`.

## Q1. What is its purpose and scope, and what cannot be inferred?

The canonical stem `source-adyen-docs-payment-methods-swish-ios-drop-in` is a 2026-09-15 Swish-specific add-on for an existing iOS Drop-in integration with separate Sessions and Advanced server-side flows (`raw/adyen/docs/payment-methods/swish/ios-drop-in/2026-09-15.md:15-25,58-68`). It does not establish current merchant enablement, a completed live payment, capture or settlement: its simulator and status instructions are scoped to TEST and live acceptance requires a separate Customer Area request (`:48-56,82-90`).

## Q2. What are the central capability, prerequisites, and warnings?

Sessions needs existing iOS Drop-in Sessions, Checkout API v68+ and Swish added in Customer Area; no additional `/sessions` parameters or Swish configuration are stated (`raw/adyen/docs/payment-methods/swish/ios-drop-in/2026-09-15.md:29-46`). Advanced needs existing iOS Drop-in Advanced, `action.type: qr` handling and Customer Area setup; no additional `/payments` parameters or Swish configuration are stated (`:62-80`). Its action-handling link targets `handle-the-redirect` while the row says `qr`, so do not recast the action type from the link (`:67`). In TEST, the page claims authorization within 15 seconds and allows refusal simulation via `shopperStatement` code such as `FF08`, with TEST Customer Area status checks (`:50-54,84-88`). A separate live Customer Area request is needed for LIVE acceptance (`:56,90`); the TEST timing statement does not establish a live outcome.
