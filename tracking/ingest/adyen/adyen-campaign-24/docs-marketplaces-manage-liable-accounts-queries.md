# docs-marketplaces-manage-liable-accounts — attempt 1 retrieval checks

## Q1. Which liable balance accounts belong to the marketplace, and what does each do?

The page names three marketplace-owned accounts (raw lines 19–23). The **main** receives commissions and can pay user fees/correct balances (raw lines 25–27); the **reserved incorrect splits** account receives funds when a target is missing or cannot receive, pending a possible internal correction transfer (raw lines 29–37); the **reserved compensation** account is debited for qualifying persistent refund/chargeback negatives (raw lines 39–45). Route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-manage-liable-accounts]] → [[raw/adyen/docs/marketplaces/manage-liable-accounts/2026-09-15]].

## Q2. When does a bad split or negative balance trigger these accounts, and does that prove user receipt?

A split to a nonexistent target, closed/suspended balance or holder, or holder lacking receive capability is booked to the **incorrect splits** reserve (raw lines 31–37), so the intended user has not been shown to receive it. Refund/chargeback negatives may persist up to 30 days; if over 30 days, the source says the **compensation** reserve is debited on the **first day of the following month**, then any negative reserve needs top-up or internal transfer (raw lines 41–45). These are source rules, not a transaction ledger or bank-receipt record. Route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-manage-liable-accounts]] → [[raw/adyen/docs/marketplaces/manage-liable-accounts/2026-09-15]].
