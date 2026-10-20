# C22 balance types retrieval checks

## Q1 — What are the Issuing-path balance types, and how does a platform inspect them?

For each currency in a balance-platform balance account, the guide lists current (settled) balance, available, pending, pending available and reserved (raw lines 19–30). Its multiple-currency section lists GET `/balanceAccounts/{id}`, the `balancePlatform.balanceAccount.balance.updated` webhook and Customer Area **Balance accounts > Balances** as inspection routes (raw lines 34–40). The prerequisite is an existing balance account; the page does not establish particular account or API access. Forward route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-balance-types]] → [[raw/adyen/docs/issuing/balance-types/2026-09-15]].

## Q2 — What calculation or availability boundary could mislead a reader?

The snapshot's printed available and pending-available formulas (raw lines 24–28) conflict with Example 2: its EUR 50 current, EUR -70 pending and EUR 0 reserved produce printed available EUR -20 and pending available EUR -70 (raw lines 72–86), whereas literal substitution into the printed formulas gives EUR 50 and EUR -90 respectively. The example explicitly says future refund changes can make available negative while current remains positive (raw line 86). Do not rely on this page alone as a calculation rule or as evidence that pending funds settle or a transfer succeeds. Forward route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-balance-types]] → [[raw/adyen/docs/issuing/balance-types/2026-09-15]].
