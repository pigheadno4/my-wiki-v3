# docs-marketplaces-custom-payouts-configure-settlement-delay retrieval probes

## Q1 — How can a Marketplace override the settlement delay for one user's balance account?

Answer: The merchant account supplies the default, but the platform can set a specific balance-account override through Configuration API creation (POST `/balanceAccounts`) or update (PATCH `/balanceAccounts/{id}`) using `platformPaymentConfiguration.settlementDelayDays` (raw lines 19, 33–44). Documented values are 1–20 business days or `null` for default (line 44). The credential needs Balance Platform BCL role, Configuration webhook subscriptions and Account Manager enablement (lines 21–31). One-day delay needs prior Adyen approval and an account with a managed payout schedule cannot use this custom delay (line 30).

Route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-custom-payouts-configure-settlement-delay]] → [[raw/adyen/docs/marketplaces/custom-payouts/configure-settlement-delay/2026-09-15]].

## Q2 — What adjacent setting can a delay update reset, and what does success prove?

Answer: A previously configured `salesDayClosingTime` must be included whenever the balance account is updated, or it resets to the default **00:00**; allowed values are hourly **00:00–07:00** (raw lines 40–46). The response and balance-account created/updated webhook show configuration state (lines 268–321). They do not prove that a settlement batch has become available, that a payout was scheduled or executed, or that the bank received funds. The TEST example sets a three-business-day delay (lines 48–64).

Route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-custom-payouts-configure-settlement-delay]] → [[raw/adyen/docs/marketplaces/custom-payouts/configure-settlement-delay/2026-09-15]].
