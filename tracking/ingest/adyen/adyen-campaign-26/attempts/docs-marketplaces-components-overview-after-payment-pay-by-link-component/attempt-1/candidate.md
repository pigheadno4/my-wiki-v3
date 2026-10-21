---
title: "Adyen Marketplace Platform Experience Pay by Link components"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/components-overview/after-payment/pay-by-link-component"
raw_files:
  - "adyen/docs/marketplaces/components-overview/after-payment/pay-by-link-component/2026-09-15.md"
tags: [adyen, marketplaces, platform-components, pay-by-link]
---

## Overview

This 2026-09-15 Marketplace-path [[adyen]] guide covers Platform Experience Pay by Link components embedded in a platform user portal: an Overview for creating, monitoring, filtering and sharing links, and Details for inspecting, copying or expiring a link. It is a component integration and link-management guide, not evidence of payment settlement or beneficiary receipt. The page requires an Adyen for Platforms integration and warns that features vary by library version. See [[adyen-platform-components]].

## Key takeaways

- **Access and scope:** A Balance Platform API key needs the applicable Pay By Link Component roles assigned by Adyen: View for link visibility, View PII for shopper information, Manage Links for creation/deactivation, and Manage Settings for themes/settings. The server creates a Session authentication token using an allowed origin, account-holder resource, role policy and `product: platform`; the client supplies a session create/refresh callback. Live origins require HTTPS. The account holder must have a store linked to a business line whose sales channels include `payByLink` or `eCommerce`. See raw lines 45–65 and 251–319.
- **Link setup and lifecycle:** A store is selected for link creation (automatically if there is only one). The user must provide a shopper terms-and-conditions URL and confirm compliance before the first link; the created link's details cannot be changed. Links remain searchable in the component list for up to 90 days. User-set expiry is at most 70 days; without one, the page states expiry after 24 hours. The component does not automatically email shoppers. Overview groups Active/Payment pending and Completed/Expired links; Payment pending is not a confirmed payment. A single-use link expires after its first successful payment, while an Open link can take multiple payments until deactivated/canceled. See raw lines 56–60, 69–160 and 182–196.
- **Money-flow boundary:** A shopper payment through a component-created link follows the store split configuration; if the store has no split configuration, the page says all funds go to the platform liable balance account by default. The component does not alter existing split logic. A link marked Completed is a link/payment-processing state, not independent proof of settlement or payout. See raw lines 61, 71 and 125–144.
- **Per-store settings and form validation:** Component terms and theme are configured per store and do not carry to links created through the API or Customer Area. Optional `fieldsConfig` can prefill, lock or hide creation fields, but hidden required fields still validate and need valid `data`; individual address subfields cannot be hidden. The field table labels `value` as a string while its examples use numbers, so check the versioned API/component contract before relying on that type. See raw lines 220–235 and 647–840.
- **Integration details:** The page shows npm or script/stylesheet setup, version-specific SRI for the latter, component initialization and callbacks, localization and CSS customization. It marks `availableTranslations` deprecated and states `environment` defaults to test. These examples describe UI wiring, not a successful live payment. See raw lines 321–645 and 843–863.

## Detail locators

- Component purpose, requirements, roles, expiry, split fallback and store prerequisites: pinned raw lines 15–65.
- Overview status meanings, filters and time-zone rule; Details actions: pinned raw lines 69–178.
- Creation and per-store terms/theme: pinned raw lines 182–235.
- Server session policy, origin, role and account-holder scope: pinned raw lines 237–319.
- Installation, initialization, callbacks, version and localization: pinned raw lines 321–645.
- `fieldsConfig`, visibility, validation, examples and supported languages: pinned raw lines 647–863.

## Related

- [[adyen-platform-components]] — reciprocal Platform Experience component concept.
- [[source-adyen-docs-platforms-components-overview-after-payment-pay-by-link-component]] — same dated guide under the Platforms path.

## Raw Sources

- [[raw/adyen/docs/marketplaces/components-overview/after-payment/pay-by-link-component/2026-09-15|Marketplace Pay by Link components, captured 2026-09-15]]
