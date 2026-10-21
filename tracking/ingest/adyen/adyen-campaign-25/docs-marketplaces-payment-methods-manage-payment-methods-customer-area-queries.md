# Q1 — purpose and prerequisites

**Question:** What can a Marketplace operator manage on the Customer Area Payment methods page, and what setup does this source state?

**Answer:** At merchant-account scope the page lists configured methods, opens one method's details, activates/deactivates selected methods, and changes country/region restrictions (raw lines 19–24, 40–69). It states online checkout integration, the Change payment methods Customer Area role and Payment method webhook subscription; method support depends on currency/integration, and availability may lag despite a typical within-a-day appearance (lines 26–37). Forward route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-payment-methods-manage-payment-methods-customer-area]] → [[raw/adyen/docs/marketplaces/payment-methods/manage-payment-methods/customer-area/2026-09-15]].

# Q2 — currency, ANY and deletion limits

**Question:** Does this page show self-service currency editing or unlimited country availability, and when does automatic deletion apply?

**Answer:** No currency-edit UI steps are shown: the intro mentions currency, but the requirements direct a nondefault currency change to Support, while the worked edit covers only **Country/Region** (raw lines 24, 35–37, 58–69). Choosing **ANY** removes that UI country/region restriction, subject to method support for currency and integration (lines 35, 66–69). The page says automatic deletion applies to methods that are **Inactive and unused for 90 days**; it does not say every deactivation immediately deletes a method (line 56). UI settings do not prove method approval, shopper availability or payment success. Forward route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-payment-methods-manage-payment-methods-customer-area]] → [[raw/adyen/docs/marketplaces/payment-methods/manage-payment-methods/customer-area/2026-09-15]].
