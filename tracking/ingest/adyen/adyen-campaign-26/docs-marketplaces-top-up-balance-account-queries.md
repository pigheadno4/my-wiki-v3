# Retrieval checks — docs-marketplaces-top-up-balance-account

Q1. What is a Marketplace balance-account top-up, for whom, and by which routes? Answer: It is an incoming external-source transfer increasing a user's balance account; the marketplace can also top up its liable account. Suggested uses include covering refund/chargeback negative balances and funding a planned transfer. Scheduled top-ups follow timing/amount; on-demand top-ups are initiated manually, with child pages for process and webhooks. Raw lines 17–37, 39–51.

Q2. What scope and outcome boundary matters? Answer: The title/description and lead emphasize a pull sweep/verified instrument, but the body includes scheduled and on-demand paths; their method-specific eligibility and status rules belong to child guides. Initiation triggers an incoming external transfer but does not prove source debit finality, booked balance-account credit, availability, negative-balance cure or outgoing bank receipt. Raw lines 6–7, 17, 19–21, 30–51.

Forward route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-top-up-balance-account]] → [[raw/adyen/docs/marketplaces/top-up-balance-account/2026-09-15]].
