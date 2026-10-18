# Fixed retrieval checks — Business Accounts get started

Q1. What does this captured guide cover, and what is not proven?
- Expected: A 2022-modified, 2026-09-15-captured onboarding overview for offering Business Accounts through Adyen for Platforms. It requires a Platforms integration and balance-platform enablement confirmed with Adyen; it lists an Authentication SDK for PSD2 online-transaction compliance. It does not prove current country/product eligibility, a capability being enabled, Adyen approval, a user consenting, an account being opened, a transfer executing or bank receipt.
- Raw locators: `raw/adyen/docs/business-accounts/get-started/2026-09-15.md:15-29`, `:31-48`.
- Canonical route (the `[[adyen-business-accounts]]` concept and index link are owned by another C19 worker/coordinator and were pending at this audit): `wiki/index.md` → `wiki/adyen-index.md` → `[[adyen-business-accounts]]` → `wiki/sources/adyen/source-adyen-docs-business-accounts-get-started.md` → `[[raw/adyen/docs/business-accounts/get-started/2026-09-15]]`.

Q2. Which stages and test/live boundaries does the guide specify?
- Expected: Complete the underlying platform or marketplace integration, contact Adyen to assess fit, scope compliance/capabilities/onboarding/Terms/account creation/authentication/transfers with Adyen, build with test credentials, test the API integration, and configure live separately. The guide says test setup is not replicated to live, so repeat configuration and testing in live. The linked child guides own actual resource, consent, verification, transfer and account-opening mechanics; the overview is no operational evidence.
- Raw locators: `raw/adyen/docs/business-accounts/get-started/2026-09-15.md:31-59`, `:61-79`.
- Canonical route (subject to coordinator concept/index creation): `wiki/index.md` → `wiki/adyen-index.md` → `[[adyen-business-accounts]]` → `wiki/sources/adyen/source-adyen-docs-business-accounts-get-started.md` → `[[raw/adyen/docs/business-accounts/get-started/2026-09-15]]`.
