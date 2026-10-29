# Zip overview retrieval checks

## Q1 — What is Zip's scope here, and what cannot be inferred?

Route `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-zip]]` → `[[raw/adyen/docs/payment-methods/zip/2026-09-15]]`. Canonical source stem: `source-adyen-docs-payment-methods-zip`. Full pinned raw path: `raw/adyen/docs/payment-methods/zip/2026-09-15.md`. Raw lines 11 and 22–34 show a 2024-modified, 2026-captured Zip BNPL overview naming Australian Zip Pay/Zip Money, AU/US and AUD/USD in a redirect matrix. It does not prove current merchant eligibility, country/currency pairing, a successful payment or availability of a particular Zip product.

## Q2 — What shopper flow and feature qualifications matter?

Use the same root/provider/concept/source/raw route. Raw lines 24–30 describe merchant-to-Zip redirect, Zip sign-in, SMS OTP authentication and return; return is not a final payment outcome. Lines 32–34 mark recurring, refund, capture and chargeback capabilities, but the separate-capture cell says “See note” with no note present in this captured page. Treat those marks as overview indications, not account entitlement or API instructions. Raw lines 36–66 route Web, iOS, Android, API-only and Pay by Link implementation guides.
