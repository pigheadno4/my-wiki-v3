# C24 query checks — docs-marketplaces-account-holder-status

## Q1 — Status purpose and transitions
Q: What do Marketplace account-holder active, suspended and closed statuses mean, and who can reverse an Adyen suspension?
A: Active is the table's initial account-holder/balance-account status; suspended temporarily disables the resource and blocks payouts, while closed permanently disables it and all capabilities. The platform can change active to suspended/closed and suspended to active/closed, but only Adyen can reverse an Adyen-initiated suspension. See raw/adyen/docs/marketplaces/account-holder-status/2026-09-15.md:19-38, :40-49.
Forward route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-account-holder-status]] → [[raw/adyen/docs/marketplaces/account-holder-status/2026-09-15]].

## Q2 — Inheritance and money-flow boundary
Q: Where does a post-settlement split go for a suspended or closed holder, and is the reason table universal?
A: Adyen suspension propagates to related balance accounts and closure also closes payment instruments; reason-specific effects may extend to same-legal-entity holders, with case-by-case differences. A suspended holder with pay-ins not blocked receives its split in its balance account. If pay-ins are blocked, or the holder is closed, the split routes to the liable holder's Reserved Incorrect Splits Account. This is documented routing after settlement, not proof a particular payment settled or a payout occurred. See raw/adyen/docs/marketplaces/account-holder-status/2026-09-15.md:51-69, :73-93.
Forward route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-account-holder-status]] → [[raw/adyen/docs/marketplaces/account-holder-status/2026-09-15]].
