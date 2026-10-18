# General verification errors — retrieval probes

## Q1 — Purpose and product scope

**Query:** Is this Business accounts path a Business-accounts-only error list, and does seeing a code prove that a user's account was opened or rejected?

**Expected answer:** No. The 2023-modified reference is under Business accounts KYC, but explicitly addresses readers with Adyen for Platforms or Issuing integrations. It broadly classifies verificationErrors on legal entities and often links suberrors. It is a dated code catalog, not a specific user's account, capability, onboarding or verification result.

**Raw locators:** lines 14–35 and 309–338. **Canonical discovery route:** [[adyen-index]] → [[adyen-business-accounts]] → [[source-adyen-docs-business-accounts-kyc-verification-codes-general-verification-errors]] → [[raw/adyen/docs/business-accounts/kyc-verification-codes/general-verification-errors/2026-09-15]]. Provider-index Business accounts link is pending coordinator repair.

## Q2 — Error versus suberror versus remediation

**Query:** How should a support or integration reader interpret a general verification code such as 1_15, 2_8203 or 3_10, and does its action link prove remediation?

**Expected answer:** General codes identify a broad check family; 1_15 says a capability is not allowed due to the legal entity's or associated individual's country, 2_8203 says organization.economicSector is missing and links a remediating-action code, and 3_10 says data review is required. Look at the actual verificationErrors object and any subErrors/remediatingActions for the specific entity; linked catalogs provide further detail. A code or action mapping does not prove resolution, current capability allowance or account opening.

**Raw locators:** lines 22–47, 136–139, 241, 295–307 and 309–338. **Canonical discovery route:** [[adyen-index]] → [[adyen-business-accounts]] → [[source-adyen-docs-business-accounts-kyc-verification-codes-general-verification-errors]] → [[raw/adyen/docs/business-accounts/kyc-verification-codes/general-verification-errors/2026-09-15]]. Provider-index Business accounts link is pending coordinator repair.
