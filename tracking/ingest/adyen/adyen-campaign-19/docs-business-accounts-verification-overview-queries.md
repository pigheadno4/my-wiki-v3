# Retrieval probes — Business Accounts verification overview

Q1. When does Adyen verify a Business Accounts user, and does a requested capability or pending check mean the user is approved?

Forward route: [[adyen-index]] → [[adyen-business-accounts]] → `## Sources` → [[source-adyen-docs-business-accounts-verification-overview]] → [[raw/adyen/docs/business-accounts/verification-overview/2026-09-15]].

Expected answer: Checks occur when configured capabilities are requested during onboarding, when a separately requested capability is added, after user-data changes, and in periodic/proactive reviews covering legal entity and associated persons. Verification is asynchronous: errors may coexist with pending overall status; rejected is not allowed. Inspect the actual per-capability settings/status and verification updates. Account-holder creation or requested=true is no proof of KYC approval or opened Business Account. The page does not supply a country eligibility list. Raw locators: lines 19–23, 30–64, 143–159, 161–194; `## When does Adyen verify users`, `## How the verification process works`.

Q2. How do verification deadlines affect already allowed capabilities, and are 30 or 60 days guaranteed?

Forward route: [[adyen-index]] → [[adyen-business-accounts]] → `## Sources` → [[source-adyen-docs-business-accounts-verification-overview]] → [[raw/adyen/docs/business-accounts/verification-overview/2026-09-15]].

Expected answer: Deadlines exist in LEM API v3/v4 and may preserve already allowed capability use during re-verification/data review. Required information/documents must be submitted and verified by Adyen by the final date; a review finalizes only after confirmation plus resolution of errors. The page's dated standard table is 30 days for issueBankAccount/sendToThirdParty and 60 days for receiveFromThirdParty, but Adyen can shorten or remove them. Missed deadlines or failed KYC disallow capabilities. Inspect real account-holder deadline data; the mixed allowed=true/invalid/1_14 sample is not a universal rule. Raw locators: lines 46–52, 60–84, 89–137, 181–194; `### Verification deadlines`.
