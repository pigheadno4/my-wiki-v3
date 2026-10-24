# Retrieval checks — docs-payment-methods-gcash

Q1. What is this GCash page's purpose and scope, and what cannot be inferred from it?
Answer: It is an online-payments method overview whose matrix labels GCash a PH/PHP redirect wallet (raw lines 15–17, 58–60), with links to Web, native, cross-platform, API-only and Pay by Link guides (raw lines 62–104). The matrix and navigation do not establish a merchant's current enablement or SDK/API implementation. Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-gcash]] → [[raw/adyen/docs/payment-methods/gcash/2026-09-15]].

Q2. How do one-time and recurring shopper journeys differ, and what expiry/outcome boundary matters?
Answer: The one-time website/app sketch redirects to GCash login, SMS OTP/MPIN and confirmation before returning (raw lines 25–37). For recurring, website selection uses a QR scan while mobile-app selection follows GCash login/OTP/MPIN (raw lines 39–54). Redirect validity defaults to 30 minutes, with Support contact for changes (raw line 56). Return/SMS does not by itself show final payment status, and recurring mechanics are not specified here. Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-gcash]] → [[raw/adyen/docs/payment-methods/gcash/2026-09-15]].
