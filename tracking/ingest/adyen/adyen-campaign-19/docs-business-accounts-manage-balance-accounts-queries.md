# Fixed retrieval queries: docs-business-accounts-manage-balance-accounts

## Q1 — resource identity, creation and observation

**Question.** In the captured Business Accounts balance-account guide, what does a balance account represent, how is it associated with an account holder, and which API routes inspect it without mistaking an example response for a funded or usable live account?

**Forward route.** `wiki/index.md` → `wiki/adyen-index.md` → `[[adyen-business-accounts]]` → `[[source-adyen-docs-business-accounts-manage-balance-accounts]]` → `[[raw/adyen/docs/business-accounts/manage-balance-accounts/2026-09-15]]`. At worker audit, `wiki/adyen-index.md` lacked the literal `[[adyen-business-accounts]]` edge; coordinator index repair is required to complete this route.

**Expected answer.** It is a Configuration API resource with information about funds held by the user. The guide creates it through `POST /balanceAccounts` using the associated account holder ID and says to retain the returned balance-account ID. The paginated `GET /accountHolders/{id}/balanceAccounts` lists an account holder's accounts, `GET /balanceAccounts/{id}` gives details/balances, and `GET /balanceAccounts/{id}/paymentInstruments` gives associated instruments (called “cards” here). Customer Area views accounts within one selected balance platform. The example `defaultCurrencyCode: EUR`, zero balances, primary-account description and `status: active` are illustrative; they do not establish a particular live account's verification, funding, role authorization or usable Business Account number.

**Raw locators.** Lines 17–21 (resource/process context); 23–27 (create association); 227–253 (response identity/sample currency/status/balances); 256–278 (view paths).

## Q2 — update and permanent closure

**Question.** How does the captured guide update and permanently close a balance account, and what condition prevents immediate closure if funds remain?

**Forward route.** `wiki/index.md` → `wiki/adyen-index.md` → `[[adyen-business-accounts]]` → `[[source-adyen-docs-business-accounts-manage-balance-accounts]]` → `[[raw/adyen/docs/business-accounts/manage-balance-accounts/2026-09-15]]`. The same missing provider-index edge was observed at worker audit.

**Expected answer.** Use `PATCH /balanceAccounts/{id}` to update; the worked example only changes `description`. To close permanently, check for zero balance, move any remaining funds via the separately linked transfer route, then update each balance account with `status: Closed`. Separate permanent account-holder deactivation may apply when the contractual platform relationship ends. These instructions do not prove that a real transfer or closure has occurred.

**Raw locators.** Lines 280–295 (PATCH and description example); 473–482 (zero-balance closure and account-holder deactivation).
