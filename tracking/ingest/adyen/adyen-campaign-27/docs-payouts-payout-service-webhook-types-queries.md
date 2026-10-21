# Retrieval checks

Q1. Which Payout Service webhook types does the captured guide list, and how is their payload structured?

Answer: Follow [[index]] → [[adyen-index]] → [[adyen-webhooks]] → [[source-adyen-docs-payouts-payout-service-webhook-types]] → [[raw/adyen/docs/payouts/payout-service/webhook-types/2026-09-15]]. The general envelope has `data`, `environment`, and `type`; `data` varies by type, and some types have `data.status` (raw lines 26–36, 70–78). Configuration types cover account-holder, balance-account, and sweep create/update/delete entries; Transfer types are `balancePlatform.transfer.created` and `.updated` (raw lines 80–101).

Q2. Can a `transfer.created` event or bank classification prove payout completion or bank receipt, and how does the guide distinguish internal from bank transfer?

Answer: Follow [[index]] → [[adyen-index]] → [[adyen-webhooks]] → [[source-adyen-docs-payouts-payout-service-webhook-types]] → [[raw/adyen/docs/payouts/payout-service/webhook-types/2026-09-15]]. `transfer.created` reports creation of a credit/deduction request and `transfer.updated` a request status change, so these labels alone do not prove movement or bank receipt (raw lines 94–101). The classification table says internal = `internal`/`internalTransfer`/`balanceAccountId`; third-party bank payout = `bank`/`bankTransfer`/`bankAccount` (raw lines 103–109).
