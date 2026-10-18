# Account statement guideline retrieval checks

## Q1 — What does Adyen's page require of a platform statement template, and how do the product/region sections differ?

**Answer:** The page instructs platforms offering business accounts or issuing cards to provide statements, preserve Adyen API data unchanged, and obtain Adyen approval for the template. EU/US Adyen Bank Accounts, UK Business Accounts and Issuing have distinct institution/account/disclosure sections. The platform supplies bold-marked contact information. EU/US bank-account disclosures and interest-bearing-only APYE items differ from UK e-money-account wording. For Issuing, a sample goes to Adyen before cards are issued; EU can use the UI without a downloadable statement if it displays all listed information, while UK needs a durable download. These are Adyen's dated compliance guidelines, not legal advice.

**Evidence:** `raw/adyen/docs/business-accounts/compliance-guidelines/account-statements/2026-09-15.md:19-27,25-94,96-152,172-211,299-301`. **Forward route:** `[[index]]` → `[[adyen-index]]` → `[[adyen-business-accounts]]` → `[[source-adyen-docs-business-accounts-compliance-guidelines-account-statements]]` → `[[raw/adyen/docs/business-accounts/compliance-guidelines/account-statements/2026-09-15]]`. Issuing route: `[[index]]` → `[[adyen-index]]` → `[[adyen-issuing]]` → same source → same raw (after concept placement).

## Q2 — Can a single branch name or deposit-protection statement be copied across EU, US and UK templates?

**Answer:** No. The prose supplies different EU/US bank and UK PSP identities and region-specific disclosure wording. The later table differs from the UK prose by naming the London branch and marks an Adyen N.V. institution row for all three regions alongside separate US and UK branch rows. A template needs Adyen review/approval, and the source says it is not legal advice. Its EU DGS, US FDIC and UK FSCS statements are dated guideline text, not independently verified current protection for a user's funds.

**Evidence:** `raw/adyen/docs/business-accounts/compliance-guidelines/account-statements/2026-09-15.md:19-23,25-43,86-105,144-146,213-239,295-301`. **Forward route:** `[[index]]` → `[[adyen-index]]` → `[[adyen-business-accounts]]` → `[[source-adyen-docs-business-accounts-compliance-guidelines-account-statements]]` → `[[raw/adyen/docs/business-accounts/compliance-guidelines/account-statements/2026-09-15]]`.
