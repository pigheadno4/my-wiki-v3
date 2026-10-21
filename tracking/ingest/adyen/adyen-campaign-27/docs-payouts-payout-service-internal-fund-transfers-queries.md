# Query proposal — docs-payouts-payout-service-internal-fund-transfers

Q1. What movement does this Payout Service overview cover, and what initiation routes does it name?
Answer: It describes transferring funds from one balance account to another inside a balance platform, with settlement-account funding and sweeps as context (raw lines 15-19). The two routes are scheduled transfers triggered by timing/amount and on-demand transfers when needed (lines 21-24). Route: [[index]] → [[adyen-index]] → [[adyen-platform-internal-transfers]] → [[source-adyen-docs-payouts-payout-service-internal-fund-transfers]] → [[raw/adyen/docs/payouts/payout-service/internal-fund-transfers/2026-09-15]].

Q2. Does the overview establish transfer completion or an external bank payout?
Answer: No. It is an overview directing readers to the scheduled/on-demand guides, internal-transfer webhooks and transfer-details view (raw lines 21-44). It does not give a booked event, role/capability gates or bank destination. The movement named here is balance-account to balance-account (line 19), so a configured sweep or request cannot be treated as bank receipt or completed movement. Route: [[index]] → [[adyen-index]] → [[adyen-platform-internal-transfers]] → [[source-adyen-docs-payouts-payout-service-internal-fund-transfers]] → [[raw/adyen/docs/payouts/payout-service/internal-fund-transfers/2026-09-15]].
