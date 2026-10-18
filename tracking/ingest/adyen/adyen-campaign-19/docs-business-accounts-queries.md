# Business Accounts overview retrieval checks

Q1. What does the dated Adyen Business Accounts overview say users can do, and what integration paths are named?
Expected forward route: [[adyen-index]] → [[adyen-business-accounts]] → ## Sources → [[source-adyen-docs-business-accounts]] → [[raw/adyen/docs/business-accounts/2026-09-15]]. Inspect raw lines 19–30 for the development warning, API/Hosted Onboarding paths, business-related incoming/outgoing transfers and direct Adyen-account payouts. The page does not prove an account exists for any user.

Q2. Which user and geographic qualifications appear in the captured overview, and can they establish current eligibility?
Expected forward route: [[adyen-index]] → [[adyen-business-accounts]] → ## Sources → [[source-adyen-docs-business-accounts]] → [[raw/adyen/docs/business-accounts/2026-09-15]]. Inspect raw lines 32–42 for entity type, UBO/individual tax-residence and additional-information prerequisites; lines 44–80 for dated Eurozone/mainland UK/US details, Channel Islands exclusion and US state reporting note. Compare exact tax-resident versus reside wording; this 2023-modified development snapshot cannot alone establish current regional or account eligibility.
