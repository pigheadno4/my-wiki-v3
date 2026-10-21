# docs-marketplaces-manage-balance-accounts — retrieval checks

Q1. How does a marketplace create and inspect a user's balance account, and how is it related to onboarding?

The page defines the balance account as an API resource for information about funds held by a user, managed through the Balance Platform Configuration API (raw lines 19–21). POST `/balanceAccounts` with the target account-holder ID and retain the returned balance-account `id` (lines 23–27, 227–254). Inspect in Customer Area or use paginated holder-account GET, balance-account detail GET, or associated-payment-instruments GET (lines 256–278). The page says the operations are part of a larger onboarding and verification process (line 21), so a TEST creation example does not prove verification or live payment/payout capability. Route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-manage-balance-accounts]] → [[raw/adyen/docs/marketplaces/manage-balance-accounts/2026-09-15]].

Q2. What boundary must be met before permanent balance-account closure, and is that the same as deactivating the account holder?

Only an empty/zero-balance account can be permanently closed. If funds remain, the guide directs payout or transfer first, then PATCH the balance account to status `Closed` (raw lines 473–480). A separate link addresses permanent account-holder deactivation when the contractual relationship ends (line 482). The guide provides no completed closure or movement response; an instruction to pay out or transfer does not establish funds arrival. Route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-manage-balance-accounts]] → [[raw/adyen/docs/marketplaces/manage-balance-accounts/2026-09-15]].
