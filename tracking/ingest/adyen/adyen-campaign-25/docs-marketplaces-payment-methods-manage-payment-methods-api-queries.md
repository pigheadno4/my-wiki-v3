# Q1 — purpose and prerequisites

**Question:** What does the Marketplace Management API guide manage, at what scope, and what prerequisites apply?

**Answer:** It lists merchant-account-configured payment methods, reads an individual method, and PATCHes an existing method's enabled, country or currency settings (raw lines 19–24, 37–39, 203–205, 351–361). It requires an online payments integration with checkout UI and a Management API credential carrying the Payment methods read and write role; only methods supported for the currency and integration can be configured (lines 26–35). Forward route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-payment-methods-manage-payment-methods-api]] → [[raw/adyen/docs/marketplaces/payment-methods/manage-payment-methods/api/2026-09-15]].

# Q2 — destructive and availability boundaries

**Question:** What happens when a method is disabled or country/currency lists are empty, and does a sample response prove shopper availability?

**Answer:** The PATCH table says `enabled=false` disables a method and the page says disabled methods are automatically deleted after **90 days** (raw lines 351–363). Empty `countries` or `currencies` mean all values **supported by that payment method**, constrained by the integration/currency support requirement (lines 34, 359–360). External factors can delay availability; appearance within a day is typical, not guaranteed (line 35). The TEST Visa PATCH sample changes NL/US and EUR/USD and its sample response lists settings and `enabled=true`, but this is illustrative configuration rather than live method approval, shopper presentation or payment success (lines 365–390, 575–593). Forward route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-payment-methods-manage-payment-methods-api]] → [[raw/adyen/docs/marketplaces/payment-methods/manage-payment-methods/api/2026-09-15]].
