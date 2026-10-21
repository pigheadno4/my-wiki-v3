# docs-marketplaces-top-up-balance-account-scheduled-top-ups retrieval probes

## Q1 — Who can configure a Marketplace top-up pull sweep, and what does its shown threshold request do?

Answer: The pinned guide requires Adyen for Platforms, Configuration API credentials, three webhook families, user `receiveFromTransferInstrument` capability and Support enablement; account holders need verified bank accounts in the EU, UK or US on the named standard debit rails (raw lines 26–37). POST `/balanceAccounts/{balanceAccountId}/sweeps` creates a pull from the user's linked verified transfer instrument into that user's balance account, with `schedule.type: balance`, `triggerAmount` and `sweepAmount` (lines 39–74). The TEST example triggers below EUR 5,000 and requests EUR 1,000 (lines 76–107).

Route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-top-up-balance-account-scheduled-top-ups]] → [[raw/adyen/docs/marketplaces/top-up-balance-account/scheduled-top-ups/2026-09-15]].

## Q2 — Does an active sweep mean a funded balance, and does the example specify a fixed-time schedule?

Answer: No. A successful response gives a sweep ID and default **active** configuration, followed by a created webhook (raw lines 463–495). Only when the condition is met does Adyen initiate an incoming top-up; transfer and transaction webhooks report authorization, eventual funds-added state or failure (lines 53–59, 496–500). The page mentions fixed timing as an option (lines 19–24), but its concrete request uses only `schedule.type: balance` and a balance threshold (lines 63–107); it does not provide fixed-time scheduling fields. The triggered request is not booked-credit proof.

Route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-top-up-balance-account-scheduled-top-ups]] → [[raw/adyen/docs/marketplaces/top-up-balance-account/scheduled-top-ups/2026-09-15]].
