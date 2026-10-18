# Worker retrieval checks

Q1. What is this guide's central purpose and what preparations does it name?

A1. The Business Accounts third-party transfer page explains Transfer webhooks for the balance account involved in an incoming or outgoing third-party bank request: `transfer.created` announces the request and `transfer.updated` reports changes (raw lines 15–28). Its requirements name a payout service integration, a server that can receive and accept webhooks, and Transfer plus Transaction webhook subscriptions (raw lines 30–40). Route: [[index]] → [[adyen-index]] → [[adyen-business-accounts]] → [[source-adyen-docs-business-accounts-third-party-transfer-webhooks]] → [[raw/adyen/docs/business-accounts/third-party-transfer-webhooks/2026-09-15]].

Q2. What consequential failure or evidence boundary must a payout-status answer preserve?

A2. Outgoing `booked` records deduction from the user's balance account and explicitly is not final; the transfer can still fail after external-bank rejection (raw lines 1534–1543). Internal review and instant credit examples place pending/failed/credited in `tracking` while top-level transfer `status` remains `booked` (raw lines 1657–1666, 1790–1800, 1815–1823, 1920–1966, 2425–2554). ETA is an estimate for the stated local regular/fast/wire scope and can deviate from actual arrival (raw lines 2115–2127). Permanent return reasons may block the transfer instrument and make a later request fail with 422, even though some reason-table rows suggest retrying (raw lines 2699–2705, 2882–2898). Route: [[index]] → [[adyen-index]] → [[adyen-business-accounts]] → [[source-adyen-docs-business-accounts-third-party-transfer-webhooks]] → [[raw/adyen/docs/business-accounts/third-party-transfer-webhooks/2026-09-15]].
