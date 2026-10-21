# C26 Pay by Link components retrieval checks

## Q1 — Purpose and prerequisites

**Query:** What can Marketplace Pay by Link components do in a platform portal, and what must be configured before users create links?

**Answer:** The Overview and Details components let platform users create, monitor, filter, share/copy and expire payment links in a portal (raw lines 27–35, 69–95, 158–178). The guide requires an Adyen for Platforms integration, a Balance Platform API key with action-appropriate component roles, an account holder with a store linked to a business line using `payByLink` or `eCommerce`, and a scoped server-created session token (raw lines 45–65, 253–308). Before the first link, the user supplies a shopper terms URL and confirms compliance; created link details cannot be changed (raw lines 182–196). Route: [[index]] → [[adyen-index]] → [[adyen-platform-components]] → [[source-adyen-docs-marketplaces-components-overview-after-payment-pay-by-link-component]] → [[raw/adyen/docs/marketplaces/components-overview/after-payment/pay-by-link-component/2026-09-15]].

## Q2 — Lifecycle and split boundary

**Query:** Does a completed link prove payout, and does the component itself decide the split or automatically email shoppers?

**Answer:** No. The guide defines Completed as successful processing of the link's required payment, while Payment pending means the transaction is unconfirmed (raw lines 129–135); neither establishes settlement, payout or bank receipt. Store split configuration controls shopper-payment distribution, and without one the guide says all funds go to the liable balance account; the component does not alter split logic (raw line 61). The component does not automatically email shoppers (raw line 58). Links are searchable for up to 90 days; user-set expiry can reach 70 days, otherwise expiry is 24 hours after creation (raw lines 56–57). Route: [[index]] → [[adyen-index]] → [[adyen-platform-components]] → [[source-adyen-docs-marketplaces-components-overview-after-payment-pay-by-link-component]] → [[raw/adyen/docs/marketplaces/components-overview/after-payment/pay-by-link-component/2026-09-15]].
