# Fixed retrieval queries: docs-business-accounts-account-structure-resources-platform-account-structure

## Q1 — platform versus user resource map

**Question.** In this captured Business Accounts account-structure example, which resources belong to the platform versus its restaurant users, and which balance accounts have distinct roles?

**Forward route.** `wiki/index.md` → `wiki/adyen-index.md` → `[[adyen-business-accounts]]` → `[[source-adyen-docs-business-accounts-account-structure-resources-platform-account-structure]]` → `[[raw/adyen/docs/business-accounts/account-structure-resources/platform-account-structure/2026-09-15]]`. At worker audit the provider index lacked literal `[[adyen-business-accounts]]`; coordinator index repair is needed.

**Expected answer.** The guide states that the platform needs a balance platform and merchant account in each acquiring/registered processing region, then illustrates company and merchant accounts, regional balance platforms, a platform liable account holder and liable balance account for platform funds, and regional platform legal entities. Per user it illustrates stores, country-level account holders and legal entities/business lines, a balance account holding user funds, a separate account to link Business Account instruments, verified external transfer instruments for payouts, and a Business Account payment instrument per restaurant. The specific FoodDelivery country/region counts are examples. None of these diagram labels establishes bank legal ownership, a verified user, an opened Business Account, live balances, or completed supplier payouts.

**Raw locators.** Lines 21–27 (scope and example); 29–46 (platform resources); 48–70 (user resources and distinct balance-account roles); 72–76 (diagram).

## Q2 — conflicting cardinality and routing boundary

**Question.** Does this account-structure page reliably allow several Business Account numbers on one balance account, and how should it be reconciled with the captured creation guide?

**Forward route.** `wiki/index.md` → `wiki/adyen-index.md` → `[[adyen-business-accounts]]` → `[[source-adyen-docs-business-accounts-account-structure-resources-platform-account-structure]]` → `[[raw/adyen/docs/business-accounts/account-structure-resources/platform-account-structure/2026-09-15]]`; then `[[source-adyen-docs-business-accounts-create-business-accounts]]` → `[[raw/adyen/docs/business-accounts/create-business-accounts/2026-09-15]]` for the conflict. The provider-index concept edge remains a coordinator repair.

**Expected answer.** This structure page says multiple Business Accounts may link to one balance account, while requiring that account to be separate from the one holding the user's funds. However, the captured Create business accounts guide says a balance account has only one Business Account number and an API error for a duplicate; the captured integration checklist likewise says one `bankAccount` payment instrument per balance account. The sources conflict on cardinality. Do not silently treat the diagram sentence as implementable multi-number behavior without current API/product confirmation. The structure page describes resource routing, not proof that any external bank account belongs to a named person or that funds moved.

**Raw locators.** Current page lines 56–70, especially 60; conflict source `raw/adyen/docs/business-accounts/create-business-accounts/2026-09-15.md` line 46; supporting checklist `raw/adyen/docs/business-accounts/integration-checklist/2026-09-15.md` line 48.
