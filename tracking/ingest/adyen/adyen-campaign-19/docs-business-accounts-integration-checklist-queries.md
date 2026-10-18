# Fixed retrieval queries: docs-business-accounts-integration-checklist

## Q1 — prerequisite scope and account structure

**Question.** What does the captured Business Accounts integration checklist require before and during implementation, and what do its named resources and credentials actually establish?

**Forward route.** `wiki/index.md` → `wiki/adyen-index.md` → `[[adyen-business-accounts]]` → `[[source-adyen-docs-business-accounts-integration-checklist]]` → `[[raw/adyen/docs/business-accounts/integration-checklist/2026-09-15]]`. At worker audit, `wiki/adyen-index.md` lacked the literal `[[adyen-business-accounts]]` link; coordinator index repair is needed.

**Expected answer.** The guide says to design with an Adyen implementation manager, understand the separate company/merchant/balance-platform/account-holder/balance-account/legal-entity/transfer-instrument/business-line/payment-instrument roles, and finish the marketplace or platform Adyen for Platforms integration checklist first. It describes Balance Platform and company-scoped LEM credentials, webhook endpoints/acknowledgment/configuration/HMAC, and additional Business Accounts verification checks. Authentication SDK and Open Banking are optional. The checklist does not specify current country eligibility or a complete live permission matrix, and naming a resource or credential is not evidence of a verified or opened account.

**Raw locators.** Lines 23–50 (design/resource roles); 52–65 (base integration and credentials); 67–83 (webhooks, verification and optional features).

## Q2 — test/live boundary and operational proof

**Question.** Does completing the test integration automatically take Business Accounts live, and which live checks does this captured checklist ask for?

**Forward route.** `wiki/index.md` → `wiki/adyen-index.md` → `[[adyen-business-accounts]]` → `[[source-adyen-docs-business-accounts-integration-checklist]]` → `[[raw/adyen/docs/business-accounts/integration-checklist/2026-09-15]]`. The same missing provider-index edge was observed at worker audit.

**Expected answer.** No. The page says test setup is not automatically replicated in the live account. It calls for replicating live setup, updating code, switching to live credentials and endpoints, then live end-to-end checks of API access, Business Account creation with `issueBankAccount`, third-party send/receive using `sendToThirdParty`/`receiveFromThirdParty`, and webhook receipt/acceptance. These are instructions to test, not proof that a particular live account was opened or that funds moved or reached a bank. Terms acceptance and product/country eligibility require their own supporting sources.

**Raw locators.** Lines 85–106 (go-live sequence and checks); lines 75–83 (verification and separate feature routes).
