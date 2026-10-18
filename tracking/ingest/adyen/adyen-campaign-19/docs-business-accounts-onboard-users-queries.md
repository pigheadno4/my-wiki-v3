# Business accounts onboarding — retrieval probes

## Q1 — Purpose and outcome boundary

**Query:** If a platform submits Business accounts onboarding information for an existing verified account holder, is the Business account open?

**Expected answer:** No. The dated guide gives an API-only UI and LEM/Configuration data path. Legal-entity type and operating country determine additional information; new account holders first follow Platforms/marketplace onboarding, while already verified holders still supply Business accounts data. Adyen verification begins after submission. This is not approval, an opened account, accepted terms, live balance or transfer proof.

**Raw locators:** lines 15–31 and 147–163. **Canonical discovery route:** [[adyen-index]] → [[adyen-business-accounts]] → [[source-adyen-docs-business-accounts-onboard-users]] → [[raw/adyen/docs/business-accounts/onboard-users/2026-09-15]]. Provider-index Business accounts link is pending coordinator repair.

## Q2 — Source of funds and conditions

**Query:** What does the onboarding-v4 section require for Business accounts funding source and EU/UK organizations, and does the document table require all files from every user?

**Expected answer:** It applies SOF checks to Business accounts and Issuing, using businessLines service banking for Business accounts and issuing for cards. The prose sets sourceOfFunds.adyenProcessedFunds according to origin and, for non-Adyen-processed funds, asks for type and description; Adyen may ask for source-specific proof documents with age conditions. EU organizations provide turnover or balance sheet; UK organizations also provide employee count. The table examples are conditional. Its processed-funds row names businessLines.adyenProcessedFunds instead of the prose's sourceOfFunds path, so confirm the exact field with the applicable API schema. This page does not cover complete ToS consent or prove a verified account.

**Raw locators:** lines 33–52, 53–139 and 141–145. **Canonical discovery route:** [[adyen-index]] → [[adyen-business-accounts]] → [[source-adyen-docs-business-accounts-onboard-users]] → [[raw/adyen/docs/business-accounts/onboard-users/2026-09-15]]. Provider-index Business accounts link is pending coordinator repair.
