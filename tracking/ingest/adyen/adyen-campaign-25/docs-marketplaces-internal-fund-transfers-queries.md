# Retrieval checks — docs-marketplaces-internal-fund-transfers

Q1. What is an internal Marketplace transfer and what paths does the overview cover? Answer: It moves funds between balance accounts: marketplace liable to user, two accounts of the same user, or accounts of different users. The page routes to scheduled transfers triggered by timing/amount and on-demand initiation, plus return and webhook detail. Raw lines 19–26, 38–54.

Q2. What is the key boundary? Answer: An external payout moves funds from a balance account to a user's verified-bank transfer instrument, while this page describes internal balance-account movement. Its bonus/fee/user-movement examples and process links do not establish a particular booked transfer, return, payout or bank receipt, nor detail currency, role, timing or failure rules. Raw lines 19–21, 28–36, 38–54.

Forward route: [[index]] → [[adyen-index]] → [[adyen-platform-internal-transfers]] → [[source-adyen-docs-marketplaces-internal-fund-transfers]] → [[raw/adyen/docs/marketplaces/internal-fund-transfers/2026-09-15]].
