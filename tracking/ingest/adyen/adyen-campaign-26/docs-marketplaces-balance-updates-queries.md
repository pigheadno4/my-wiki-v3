# Retrieval checks — docs-marketplaces-balance-updates

Q1. How can a Marketplace receive Balance webhook notifications, and what scopes are described?

A1. Route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-balance-updates]] → [[raw/adyen/docs/marketplaces/balance-updates/2026-09-15]]. The source marks Balance webhooks pilot/limited availability. Subscribe in Customer Area, obtain the webhook ID, then POST settings to `/balancePlatforms/{id}/webhooks/{id}/settings` with trigger criteria (raw lines 19–20, 34–40). The target may cover every account in the balance platform, all accounts of one account holder, or one balance account (raw lines 26–30, 41–45). More granular settings inherit and override higher-level ones as the source table states (raw lines 49–57).

Q2. Do the captured pages settle multi-condition logic or prove money movement?

A2. Route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-balance-updates]] → [[raw/adyen/docs/marketplaces/balance-updates/2026-09-15]]. This overview says a balance change must meet all conditions before Adyen sends a webhook (raw line 47). The related [[source-adyen-docs-platforms-balance-updates-configure-balance-webhook]] has an active-status row saying any condition triggers and a conditions row saying all must match (its raw lines 88–90), leaving compound logic unresolved. A configured alert or example balance change is not a transfer, payout, refund, settlement or bank-receipt record (this raw lines 24–26, 34–47).
