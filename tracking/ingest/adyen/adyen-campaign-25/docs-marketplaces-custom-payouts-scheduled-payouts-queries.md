# C25 query checks — docs-marketplaces-custom-payouts-scheduled-payouts

## Q1 — Purpose and prerequisites
Q: How does a Marketplace platform configure a custom scheduled payout to a user's verified bank account?
A: The schedule belongs to a source balance account and targets a transfer instrument linked to the same legal entity as the account holder. The guide requires Adyen for Platforms, Transfers API initiate role, two Customer Area roles and the user's sendToTransferInstrument capability. Configuration uses Customer Area or Configuration API POST /balanceAccounts/{balanceAccountId}/sweeps with destination, currency, cron schedule in the balance account time zone and push direction. See raw/adyen/docs/marketplaces/custom-payouts/scheduled-payouts/2026-09-15.md:19-38, :53-99, :120-140. A configured sweep is not a payout outcome.
Forward route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-custom-payouts-scheduled-payouts]] → [[raw/adyen/docs/marketplaces/custom-payouts/scheduled-payouts/2026-09-15]].

## Q2 — Conditions, examples and outcome boundary
Q: Does active schedule status or a transfer-created event prove bank arrival, and what constraints can prevent or reroute a payout?
A: No. The default active sweep is configuration. A scheduled run triggers a transfer request only when its conditions hold: available balance, optional trigger/target/fixed amounts, and a valid bank route for the selected priority and transfer amount. All configured priorities must be valid routes; regional cutoffs affect expected arrival. Sweep-execution, transfer-state and transaction-debit webhooks are distinct and none alone proves beneficiary receipt. The TEST examples mix USD/EUR creation currencies and differing priority-update fields, so they are not a single exact request recipe. See raw/adyen/docs/marketplaces/custom-payouts/scheduled-payouts/2026-09-15.md:21, :40-51, :425-429, :470-482, :839-847, :849-1100, :1130-1153.
Forward route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-custom-payouts-scheduled-payouts]] → [[raw/adyen/docs/marketplaces/custom-payouts/scheduled-payouts/2026-09-15]].
