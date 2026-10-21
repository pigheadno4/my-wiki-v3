---
title: "Adyen Marketplaces: Manage payment methods in Customer Area"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/payment-methods/manage-payment-methods/customer-area"
raw_files:
  - "adyen/docs/marketplaces/payment-methods/manage-payment-methods/customer-area/2026-09-15.md"
tags: [adyen, marketplaces, platforms, payment-methods, customer-area]
---

## Overview

This 2026-09-15-captured [[adyen]] Marketplaces guide describes the **merchant-account** Payment methods overview in Customer Area: view configured methods and their details, activate/deactivate them, and edit country/region settings. Its introduction also mentions currency updates, but the detailed UI procedure does not provide a currency-edit path. This is configuration guidance, not evidence that a method is available to shoppers or has processed a payment. [[adyen-platforms]]

## Requirements and UI route

- The page calls for an Adyen **online payments integration with checkout UI**, Customer Area **Change payment methods** role, and **Payment method webhook** subscription. Methods must be supported for the relevant currency and integration; external factors can delay availability, and appearing within a day is stated as typical rather than guaranteed. Currency defaults depend on the method type; for a different currency, the page directs the reader to **Support**. See [[raw/adyen/docs/marketplaces/payment-methods/manage-payment-methods/customer-area/2026-09-15|raw lines 26–37]].
- Switch to the merchant account, open **Payments > Payment methods**, use filters/table columns for the configured-method list, and select a method for its details panel. To change status, select method checkboxes and choose **More actions > Activate** or **Deactivate**. These are UI actions; the source does not show a particular request, approval, webhook outcome or shopper-facing method selection. See [[raw/adyen/docs/marketplaces/payment-methods/manage-payment-methods/customer-area/2026-09-15|raw lines 40–55]].
- The page says payment methods set to **Inactive and unused for 90 days** are automatically deleted. Both conditions appear in this Customer Area wording; do not replace them with the related API page's different “disabled after 90 days” phrasing. For countries/regions, select **Edit > Country/Region**; **ANY** removes the country/region restriction in that UI choice, but supported-method and currency/integration limits still apply. See [[raw/adyen/docs/marketplaces/payment-methods/manage-payment-methods/customer-area/2026-09-15|raw lines 35–37, 49–69]].
- The introductory list says country/region **and currency** can be updated. Its only worked edit steps cover **Country/Region**, while the requirement says to contact Support for a nondefault currency. The page does not establish a self-service currency edit. See [[raw/adyen/docs/marketplaces/payment-methods/manage-payment-methods/customer-area/2026-09-15|raw lines 19–24, 35–37, 58–69]].

## Detail locators

- Merchant-account scope, role/webhook requirement and support/availability qualifications: [[raw/adyen/docs/marketplaces/payment-methods/manage-payment-methods/customer-area/2026-09-15|raw lines 15–37]].
- Configured-method list, details panel, activation/deactivation, conditional 90-day deletion and country/region ANY choice: [[raw/adyen/docs/marketplaces/payment-methods/manage-payment-methods/customer-area/2026-09-15|raw lines 40–69]].

## Related

- [[adyen-platforms]] — modern Platforms/Marketplace concept.
- [[source-adyen-docs-marketplaces-payment-methods-manage-payment-methods-api]] — merchant-level Management API route with its own deletion wording.
- [[source-adyen-docs-platforms-payment-methods-customer-area]] — broader Platforms store-level guide; do not import its store/capability steps into this page.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/marketplaces/payment-methods/manage-payment-methods/customer-area/2026-09-15|Marketplace Customer Area payment-method settings (captured 2026-09-15)]]
