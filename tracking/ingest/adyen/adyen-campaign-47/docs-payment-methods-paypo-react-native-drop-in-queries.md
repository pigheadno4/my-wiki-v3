# PayPo React Native Drop-in retrieval checks

## Q1 — What is this guide's scope, and what cannot be inferred?

Route `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-paypo-react-native-drop-in]]` → `[[raw/adyen/docs/payment-methods/paypo/react-native-drop-in/2026-09-15]]`. Canonical source stem: `source-adyen-docs-payment-methods-paypo-react-native-drop-in`. Full pinned raw path: `raw/adyen/docs/payment-methods/paypo/react-native-drop-in/2026-09-15.md`. Raw lines 15–48 and 443–473 identify React Native Drop-in Sessions/Advanced PayPo additions, with PL/PLN examples. This captured page does not prove current merchant eligibility, live activation or completed payment.

## Q2 — Which requirements, redirect and capture limits matter?

Use the same root/provider/concept/source/raw route. Sessions needs Checkout API v68+, shopper name/email; Advanced adds method type `paypo` and redirect handling, with name/email required and billing/delivery unmarked in both tables (raw lines 25–48, 443–473). RedirectShopper is an intermediate action (lines 845–859). The offer lasts up to 72 hours before authorization, the shopper's 30-day term starts at authorization, and merchant capture is full-only; funding follows capture (lines 391–421, 861–891). No PayPo-specific Drop-in configuration is required (lines 423–427, 455–459). The Sessions requirement links to advanced-flow while its create-session link uses sessions-flow, and the returnUrl samples differ (lines 33, 41, 66, 494). Test/live setup is at lines 429–441 and 893–905.
