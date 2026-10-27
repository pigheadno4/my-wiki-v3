# docs-payment-methods-revolutpay retrieval checks

Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-revolutpay]].

## Q1 — What is this source for, and what cannot be inferred?

The 2026-09-15 Adyen page is a Revolut Pay wallet overview, describing shopper paths, capability marks, a closed-beta access request and an API-only child route (pinned raw lines 15–46). It explicitly calls the method pilot phase and closed beta; it does not prove current availability, merchant eligibility, approval or a successful payment (lines 23, 36–38). Its table's “International” and “Multiple” labels do not identify a specific supported country/currency pair (lines 32–34). Canonical source stem: `source-adyen-docs-payment-methods-revolutpay`.

## Q2 — What is the central flow and what warnings matter?

The source says shoppers pay from a Revolut account; mobile redirects to the app with browser fallback, while desktop opens a tab offering QR/email/SMS/passkey sign-in and app/browser payment channels (pinned raw lines 25–30). The table labels the flow Direct and marks recurring x, several refund/capture capabilities check, multiple partial refund/capture x and chargebacks check; “See note” appears on the multiple-partial x marks without an explanatory note in the page (lines 32–34). Closed-beta access is conditional on eligibility, and the only integration child shown is API-only for website/iOS/Android UI (lines 36–46). Neither authentication nor route selection proves authorization or settlement. Canonical source stem: `source-adyen-docs-payment-methods-revolutpay`.
