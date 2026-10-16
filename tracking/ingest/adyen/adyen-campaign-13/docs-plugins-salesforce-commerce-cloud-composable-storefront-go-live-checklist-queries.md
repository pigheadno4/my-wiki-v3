# Fixed retrieval checks — Composable Storefront go-live checklist

Q1. What is this checklist's scope, and what does it not prove?
- Expected: A Salesforce Commerce Cloud Composable Storefront/PWA checklist for fresh live configuration because test settings are not copied to live. It covers account/finance/risk, API/MRT, webhooks, region and conditional wallets, followed by real-detail tests. It is distinct from SFRA, does not pin the deployed package version and does not prove a merchant completed the checklist, deployed successfully, passed a payment, refunded, settled or received funds.
- Raw locators: `raw/adyen/docs/plugins/salesforce-commerce-cloud/composable-storefront/go-live-checklist/2026-09-15.md:15-30`, `:150-174`.
- Canonical route: `wiki/sources/adyen/source-adyen-docs-plugins-salesforce-commerce-cloud-composable-storefront-go-live-checklist.md` → `[[adyen-salesforce-commerce-cloud]]`.

Q2. Which live credentials, security, webhook and test conditions carry the main warnings?
- Expected: Live team roles/account access, methods and payout/reconciliation setup; Visa/Mastercard 3DS enrollment may take seven days; Retail React App CSP script-src and PCI SAQ A assessment. Live API credentials need three listed permissions; MRT gets live key, endpoint-region value and live URL prefix, with optional site-specific variables. Live webhooks need event coverage/acceptance, MRT user/password/HMAC, and scheduled processing; an HTTP 200 test response does not prove downstream order processing. Wallet steps are conditional. Real-detail payment/refusal/FRAUD/refund/partial-refund/3DS tests incur fees and are not documented as already successful.
- Raw locators: `raw/adyen/docs/plugins/salesforce-commerce-cloud/composable-storefront/go-live-checklist/2026-09-15.md:38-105`, `:107-148`, `:150-170`.
- Canonical route: `wiki/sources/adyen/source-adyen-docs-plugins-salesforce-commerce-cloud-composable-storefront-go-live-checklist.md` → `[[adyen-salesforce-commerce-cloud]]`.
