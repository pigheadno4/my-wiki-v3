# Atome iOS Drop-in retrieval checks

## Q1 — What is this page's scope and what cannot be inferred?

Route `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-atome-ios-drop-in]]` → `[[raw/adyen/docs/payment-methods/atome/ios-drop-in/2026-09-15]]`. Canonical source stem: `source-adyen-docs-payment-methods-atome-ios-drop-in`. Full pinned raw path: `raw/adyen/docs/payment-methods/atome/ios-drop-in/2026-09-15.md`. Raw lines 15–33 and 768–777 identify Atome additions for existing iOS Drop-in Sessions or Advanced integrations. This captured guide does not prove current merchant eligibility, final payment success or live enablement.

## Q2 — What are the flow-specific fields, lifecycle and warnings?

Use the same root/provider/concept/source/raw route. Sessions requires Checkout API v68+, while both flow request tables require shopper/contact/billing/line-item/country fields and MY/MYR or SG/SGD; delivery address is optional when identical to billing (raw lines 29–50, 772–801). Both sections say no Atome-specific Drop-in configuration (lines 730–734, 780–784). Advanced requires redirect handling; its “successful payment” example is actually `RedirectShopper`, not final authorization (lines 772–777, 1518–1530). Partial-refund amount, sandbox account conditions and live Support setup are at lines 736–766 and 1532–1562. The Sessions curl sample repeats countryCode and lacks a shell continuation before `-d` (lines 52–76).
