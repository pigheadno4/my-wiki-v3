---
title: "Adyen POS manage payment methods"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/what-we-support/payment-methods/manage-payment-methods"
raw_files:
  - "adyen/docs/point-of-sale/what-we-support/payment-methods/manage-payment-methods/2026-09-15.md"
tags: [adyen, point-of-sale, payment-methods, customer-area, merchant-account]
---

## Overview

This Adyen website page, captured on 2026-09-15, describes **merchant-account payment-method management in Customer Area** for an Adyen point-of-sale integration: view configured methods and details, activate or deactivate them, and change their country/region setting. It is a Customer Area procedure linked from the POS payment-method catalog, not a Management API contract or proof that a method is allowed or available for a particular merchant or terminal. See [[adyen-terminal-api]].

## Key takeaways

- The prerequisite is an Adyen POS integration and the Customer Area **Change payment methods** role. The page directs the user to switch to a merchant account, then open **Payments > Payment methods**. It calls for subscribing to the **Payment method webhook**. These are Customer Area and merchant-account instructions; this page does not specify company/store/terminal inheritance or Management API permission and mutation semantics.
- The overview table lists methods configured for that merchant account. The user can filter the table, choose columns, and open a method's details. Listing or viewing a configured method does not independently establish current method eligibility, currency support, or successful payment acceptance.
- The user selects methods and chooses **More actions > Activate** or **Deactivate**. **Inactive methods unused for 90 days are automatically deleted**. Treat deactivation and continued inactivity as a consequential status change, not merely a display filter.
- **Edit > Country/Region** changes where selected methods are available. Selecting **ANY** removes country/region restrictions in that setting. The page does not say this overrides payment-method, account or regional eligibility requirements.
- External factors may delay availability after a payment-method request; the snapshot says methods **typically appear within a day** and recommends requesting them at least one day before opening. This is timing guidance, not a guaranteed activation deadline. Currency defaults depend on method type; the page directs merchants to Adyen Support for a different currency.

## Detail locators

- Page purpose and available actions: raw lines 15-26.
- POS integration, Customer Area role, Payment method webhook, availability timing and currency qualification: raw `## Requirements`, lines 28-38.
- Merchant-account table and details: raw `## View payment methods`, lines 41-48.
- Activation/deactivation path and 90-day inactive-plus-unused deletion: raw `## Activate or deactivate payment methods`, lines 50-57.
- Country/region edit path and `ANY` unrestricted setting: raw `## Change payment method country/region settings`, lines 59-70.
- Separate supported-method and add-method navigation: raw `## See also`, lines 72-75. Those linked targets are navigation, not behavior established by this page.

## Related

- Company: [[adyen]]
- Main concept: [[adyen-terminal-api]]
- POS method catalog: [[source-adyen-docs-point-of-sale-what-we-support-payment-methods]]
- Terminal feature-settings context: [[source-adyen-docs-point-of-sale-design-your-integration-determine-account-structure-configure-features]] (separate scope)

## Raw Sources

- [[raw/adyen/docs/point-of-sale/what-we-support/payment-methods/manage-payment-methods/2026-09-15|Adyen POS manage payment methods]] — complete captured Customer Area procedure
