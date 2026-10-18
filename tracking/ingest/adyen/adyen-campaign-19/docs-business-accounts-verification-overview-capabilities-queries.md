# Fixed retrieval queries: docs-business-accounts-verification-overview-capabilities

## Q1 — Business Account capability set and request boundary

**Question.** Which account-holder capabilities does this captured Business Accounts guide associate with a bank account and third-party transfers, and does an automatic or additional capability request establish usable access or an opened account?

**Forward route.** `wiki/index.md` → `wiki/adyen-index.md` → `[[adyen-business-accounts]]` → `[[source-adyen-docs-business-accounts-verification-overview-capabilities]]` → `[[raw/adyen/docs/business-accounts/verification-overview/capabilities/2026-09-15]]`. At worker audit the provider index lacked literal `[[adyen-business-accounts]]`; coordinator index repair is needed for a complete forward route.

**Expected answer.** The guide lists `issueBankAccount`, `receiveFromThirdParty` and `sendToThirdParty` for Business Accounts. It says the two third-party capabilities are enabled by default when the user has `issueBankAccount`. Default capabilities are configured for the business during design and automatically requested on new account holders in most cases; a non-default one needs a separate request and may prompt more KYC checks. Requested or default-enabled wording alone does not establish Adyen allowance, both access flags true, verified KYC, current product/country eligibility, or a live opened account.

**Raw locators.** Lines 19–23 (default and additional requests/KYC); 25–37 (Business Account and general capability sets); 62–66 (requested/allowed/enabled distinctions).

## Q2 — verification state and permission exception

**Question.** How should `pending`, `valid`, `invalid`, `rejected`, `requested`, `allowed`, and `enabled` be interpreted, especially after data changes and during a verification deadline?

**Forward route.** `wiki/index.md` → `wiki/adyen-index.md` → `[[adyen-business-accounts]]` → `[[source-adyen-docs-business-accounts-verification-overview-capabilities]]` → `[[raw/adyen/docs/business-accounts/verification-overview/capabilities/2026-09-15]]`. The same missing provider-index edge was observed at worker audit.

**Expected answer.** First-time `pending` is requested but not allowed; a previously allowed capability can stay `allowed=true` while changed data is rechecked. `valid` indicates passed capability verification; `rejected` is final in this guide. `invalid` usually blocks use and provides problems/errors/actions, but changed or missing data after prior success can produce `invalid` with `allowed=true` during a specified remediation deadline. `requested` is request state, `allowed` Adyen permission, and `enabled` separately managed access; use requires both allowed and enabled. Observe actual state through account-holder webhooks or `GET /accountHolders/{id}`, without treating this historical guide as evidence of one user's KYC approval or actual account opening.

**Raw locators.** Lines 39–45 (observation); 46–53 (verification-state matrix and exceptions); 55–66 (setting matrix and allowed-plus-enabled rule).
