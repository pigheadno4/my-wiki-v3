# Vipps overview retrieval checks

## Q1 — Purpose, scope, and inference boundary

The canonical `source-adyen-docs-payment-methods-vipps` is the 2026-09-15 Adyen Vipps online-payment overview: it identifies Vipps and its shopper flow, displays a capability matrix, and routes readers to integration guides (`raw/adyen/docs/payment-methods/vipps/2026-09-15.md:15-31,33-75`). The snapshot does not prove present availability, merchant eligibility, a completed payment, or the child guides' implementation requirements. The route is `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-vipps]]` → its pinned raw.

## Q2 — Central capability, prerequisites, and warnings

The shopper needs the mobile Vipps app and a Visa or Mastercard linked to the Vipps account; their account information is connected to a phone number (`raw/adyen/docs/payment-methods/vipps/2026-09-15.md:23-25`). In-app checkout switches to the Vipps app for authentication; website checkout first redirects to a Vipps-hosted phone-number page and then to authentication in the app (`raw/adyen/docs/payment-methods/vipps/2026-09-15.md:27`). The matrix says Wallets / redirect / NO / NOK and marks refund, capture and chargeback categories positively, while recurring has an x with “See note” but no note appears in this pinned page (`raw/adyen/docs/payment-methods/vipps/2026-09-15.md:29-31`). The Web, iOS, Android, React Native, Flutter, API-only and Pay by Link links are guide routes, not proof of channel-specific prerequisites, authorization or payment outcome (`raw/adyen/docs/payment-methods/vipps/2026-09-15.md:33-75`). Retrieval route: `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-vipps]]`.
