---
title: "Adyen Marketplaces: Manage payment methods through API"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/payment-methods/manage-payment-methods/api"
raw_files:
  - "adyen/docs/marketplaces/payment-methods/manage-payment-methods/api/2026-09-15.md"
tags: [adyen, marketplaces, platforms, payment-methods, management-api]
---

## Overview

This 2026-09-15-captured [[adyen]] Marketplaces guide uses the **Management API at merchant-account level** to list configured payment methods, read one method's details, and update an existing method's enabled state, country/region or currency settings. It is configuration guidance, not proof that a method is approved, available to shoppers, or used in a successful payment. [[adyen-platforms]]

## Requirements and API route

- The guide requires an **online payments integration with checkout UI** and a Management API credential with **Management API—Payment methods read and write** role. Only methods supported for the merchant's currency and integration may be configured. The source warns that external factors can delay availability; methods **typically** appear within a day and it recommends requesting them at least one day before opening. This timing is advice, not an activation SLA. See [[raw/adyen/docs/marketplaces/payment-methods/manage-payment-methods/api/2026-09-15|raw lines 26–35]].
- At merchant level, GET `/merchants/{merchantId}/paymentMethodSettings` lists configured methods; GET `/merchants/{merchantId}/paymentMethodSettings/{paymentMethodId}` retrieves one. PATCH on the latter path updates its settings. The examples use the **TEST** `management-test.adyen.com/v3` endpoint and dated library snippets, not an account-specific operation. See [[raw/adyen/docs/marketplaces/payment-methods/manage-payment-methods/api/2026-09-15|raw lines 37–56, 203–216, 351–376]].
- The PATCH field table lists optional `countries`, `currencies` and `enabled`. An **empty** country or currency list means all countries/currencies **supported by that payment method**, not unrestricted global coverage. `enabled=false` disables it; the page states that **disabled payment methods are automatically deleted after 90 days**, a material lifecycle effect. The test Visa sample sends `countries=[NL, US]` and `currencies=[EUR, USD]`; it does not send `enabled`, while the sample response reports `enabled=true`. These samples illustrate settings, not method activation or transaction success. See [[raw/adyen/docs/marketplaces/payment-methods/manage-payment-methods/api/2026-09-15|raw lines 351–390, 575–593]].

## Detail locators

- Scope, prerequisites, supported-method limitation and availability caveat: [[raw/adyen/docs/marketplaces/payment-methods/manage-payment-methods/api/2026-09-15|raw lines 15–35]].
- Merchant-level list and detail reads, TEST API and language-library examples: [[raw/adyen/docs/marketplaces/payment-methods/manage-payment-methods/api/2026-09-15|raw lines 37–350]].
- PATCH fields, empty-array semantics, 90-day disabled deletion, Visa example and illustrative response: [[raw/adyen/docs/marketplaces/payment-methods/manage-payment-methods/api/2026-09-15|raw lines 351–593]].

## Related

- [[adyen-platforms]] — modern Platforms/Marketplace concept.
- [[source-adyen-docs-platforms-payment-methods-api]] — related Platforms store-level Management API guide; keep merchant-versus-store scope distinct.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/marketplaces/payment-methods/manage-payment-methods/api/2026-09-15|Marketplace Management API payment-method settings (captured 2026-09-15)]]
