# Fixed retrieval queries: docs-business-accounts-create-business-accounts

## Q1 — purpose and boundary

**Question.** What does Adyen's captured Create business accounts guide say is created for a user's Business Account, how is it related to the balance account, and what should not be inferred from the guide's API examples?

**Forward route.** `wiki/index.md` → `wiki/adyen-index.md` → `[[adyen-business-accounts]]` → `[[source-adyen-docs-business-accounts-create-business-accounts]]` → `[[raw/adyen/docs/business-accounts/create-business-accounts/2026-09-15]]`. At worker audit, the provider index had no literal `[[adyen-business-accounts]]` link; coordinator index repair is required for a complete forward route.

**Expected answer.** The described action generates a business account number linked to the user's balance account by creating a `bankAccount` payment instrument. Financial transactions remain processed in the balance account. The NL/US TEST response examples show payment-instrument IDs and bank details, but they do not prove a particular account was approved, opened, usable, funded, or received a transfer.

**Raw locators.** Lines 17–19 (purpose/link to balance account); 32–40 (payment-instrument action and resource identity); 268–282 and 505–521 (example responses); 524–526 (lookup by balance account).

## Q2 — prerequisites, constrained creation and lookup

**Question.** Which prerequisites and limits gate a Business Account number in this captured guide, what is sent to the creation endpoint, and how can an existing number be located?

**Forward route.** `wiki/index.md` → `wiki/adyen-index.md` → `[[adyen-business-accounts]]` → `[[source-adyen-docs-business-accounts-create-business-accounts]]` → `[[raw/adyen/docs/business-accounts/create-business-accounts/2026-09-15]]`. The same missing provider-index edge was observed at worker audit.

**Expected answer.** The page calls for Business Accounts requirements; legal entities for the user and associated entities; two business lines; an account holder and balance account; completed verification checks; and `issueBankAccount` allowed and enabled. Then `POST /paymentInstruments` specifies `balanceAccountId`, `issuingCountryCode`, and `type=bankAccount`; `description` and `reference` are optional. The captured guide lists NL and US and requires the issuing country's currency to match the balance account currency. It says only one business account number per balance account and an API error for an existing number. `GET /balanceAccounts/{id}/paymentInstruments` is its lookup route. These are dated guide conditions, not confirmation of current country availability or a live account.

**Raw locators.** Lines 21–30 (prerequisites and capability); 32–46 (operation, fields, country/currency and cardinality); 524–526 (lookup).
