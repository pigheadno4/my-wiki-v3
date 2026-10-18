# Fixed retrieval checks — Business accounts account structure

Q1. What is this source's purpose and scope, and what must not be inferred?
- Expected: A 2021-modified, 2026-09-15-captured Adyen Business accounts resource map for a Platforms integration, not proof of an opened bank account, legal ownership, verified capability, available balance, completed transfer or bank receipt. It says merchant accounts connect to a balance platform and separate platforms are needed for acquiring regions. Linked onboarding/authentication/send/receive guides own implementation and eligibility details.
- Raw locators: `raw/adyen/docs/business-accounts/account-structure-resources/2026-09-15.md:15-31`, `:33-42`.
- Canonical URL: `https://docs.adyen.com/business-accounts/account-structure-resources`.
- Forward route (after the new concept and provider-index link are promoted): `wiki/index.md` → `wiki/adyen-index.md` → `[[adyen-business-accounts]]` → `wiki/sources/adyen/source-adyen-docs-business-accounts-account-structure-resources.md` → `[[raw/adyen/docs/business-accounts/account-structure-resources/2026-09-15]]`.

Q2. How do account holder, main legal entity, balance accounts, payout transfer instrument and business-account payment instrument differ, and what conflict remains?
- Expected: Account holder links a user's main legal entity and balance account and governs capabilities; a verified transfer instrument is the payout bank-account destination. Balance accounts hold user funds and support financial activity. The Business accounts `paymentInstrument` is an externally facing Adyen-issued `bankAccount` resource associated with a balance account; its creation is described as generating an account number, with one bankAccount instrument per balance account. The page's prose says a Business accounts user needs two balance accounts (funds and instrument), yet Example 1 shows one balance account linked to a bankAccount instrument. Preserve that unresolved structural tension, rather than treating the illustration as implementation authorization.
- Raw locators: `raw/adyen/docs/business-accounts/account-structure-resources/2026-09-15.md:33-49`.
- Canonical URL: `https://docs.adyen.com/business-accounts/account-structure-resources`.
- Forward route (after the new concept and provider-index link are promoted): `wiki/index.md` → `wiki/adyen-index.md` → `[[adyen-business-accounts]]` → `wiki/sources/adyen/source-adyen-docs-business-accounts-account-structure-resources.md` → `[[raw/adyen/docs/business-accounts/account-structure-resources/2026-09-15]]`.
