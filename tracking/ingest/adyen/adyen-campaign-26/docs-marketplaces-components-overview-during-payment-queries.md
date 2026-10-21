# C26 Q1–Q2: Marketplace during-payment components

**Q1. What is this page for, and what setup does it specify?**
Follow [[index]] → [[adyen-index]] → [[adyen-platform-components]] → [[source-adyen-docs-marketplaces-components-overview-during-payment]] → [[raw/adyen/docs/marketplaces/components-overview/during-payment/2026-09-15]]. This short page points to Checkout components as the during-payment UI route: they add a checkout page and link to the dedicated guide for user ecommerce-payment acceptance, detail collection and transaction-result display (raw lines 15-25). It also links the component-libraries overview (raw lines 27-29). The page itself specifies no credentials, session parameters, API requests or integration steps; follow the linked Checkout guide for those requirements.

**Q2. What availability and outcome limits should a reader keep?**
At the same route, the page's “various payment methods” wording links a filtered catalog; it does not establish that a particular method is configured or available to a specific platform, country, user or payment (raw line 19). Its Checkout result description is a navigation label, not proof of authorization, capture, split booking, settlement, payout or bank receipt (raw lines 23-25). Those states require the child guide and transaction-specific evidence.
