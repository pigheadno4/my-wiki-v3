# Zip Web Drop-in retrieval checks

## Q1 — What does this page cover, and what does it not establish?

Route `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-zip-web-drop-in]]` → `[[raw/adyen/docs/payment-methods/zip/web-drop-in/2026-09-15]]`. Canonical source stem: `source-adyen-docs-payment-methods-zip-web-drop-in`. Full pinned raw path: `raw/adyen/docs/payment-methods/zip/web-drop-in/2026-09-15.md`. Raw lines 15–34 show a Zip addition to an existing Web Drop-in integration, with Zip added in test Customer Area and `/sessions` default for Drop-in v5.0.0+. The historical guide does not prove current merchant eligibility, live setup, or completed payment.

## Q2 — What are the endpoint, redirect, token and setup qualifications?

Use the same root/provider/concept/source/raw route. Raw lines 28–44 and 681–694 separate Sessions from additional-use-case Payments; `clickAndCollect=true` means pickup. `RedirectShopper` with a redirect action is an intermediate response, and the page says no Zip-specific Drop-in configuration (lines 1375–1393). Tokenization uses `storePaymentMethod` and `shopperReference`, then `recurring.token.created` after settlement; the server must receive Recurring tokens life cycle events webhooks to obtain `storedPaymentMethodId` before the listed ContAuth/processing-model reuse (lines 1395–1428). Zip test credentials and a separate live Customer Area request are at lines 1628–1634. The `/payments` curl example has literal hint markup inside JSON (lines 697–718).
