---
title: "Adyen plugin release notes (2019–2026 snapshot)"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/release-notes"
raw_files:
  - "adyen/docs/plugins/release-notes/2026-09-15.md"
tags: [adyen, plugins, release-notes, adobe-commerce, salesforce-commerce-cloud, netsuite, shopware-6, cegid-retail-y2]
---

## Overview

Adyen's captured plugin release log records dated, product-specific additions, changes, fixes, removals, breaking changes, prerequisites and known issues from Magento 2 v4.1.0 (2019-05-10) through Cegid Retail Y2 v2.1.33 (2026-09-11). It covers Adobe Commerce and its Express/Hyvä modules, Salesforce Commerce Cloud B2C SFRA and Composable Storefront, Salesforce OMS and B2B, Shopware 6, NetSuite Payments and Reconciliation Bundles, and Cegid Retail Y2. Read the exact product, version and entry heading before applying a change. See [[adyen]], [[adyen-magento2]], [[adyen-salesforce-commerce-cloud]], [[adyen-salesforce-order-management-system]], [[adyen-netsuite]] and [[adyen-cegid-retail-y2]].

## Key takeaways

- The page states that Adobe Commerce minor and patch releases from v9.9.1 onward are documented exclusively on GitHub. It also points SFCC and Shopware readers to GitHub for technical release detail. This pinned page is a snapshot of its own entries, not a current-version or installed-version check.
- Adobe Commerce v11.0.0 (2026-08-24) changes headless fields and response handling: `additional_information.cc_type` is no longer set, `sortAndFilterPaymentMethods()` no longer returns `adyenPaymentMethodsResponse`, and `/payments/details` REST / `adyenPaymentDetails` GraphQL now return structured refusals, cancellations and errors rather than the generic refusal exception. Capture-mode customizations and the Multishipping Billing shopper-data global may also need review. The v11 migration guide is linked in that entry.
- Adobe Commerce v10.0.0 (2025-07-22) requires Adobe Commerce 2.4.8 and PHP 8.2 or later and introduces Web Components v6; its customization, donation, logging, Boleto and `additionalData` changes have separate qualification. The Express Checkout module v3.0.0 (2025-09-30) separately requires the Payments plugin v10.0.0 or later and Adobe Commerce v2.4.8. Do not merge module and core-plugin version requirements.
- Salesforce B2C SFRA v26.1.0 (2026-01-21) moves webhook processing to a new cartridge and calls for an updated cartridge path/endpoints. Earlier SFRA v25.3.0 removes the prebuilt `cartridges/` directory and requires a local build. SFRA v24.2.0 changes the cartridge layout and switches payment-method retrieval from `/sessions` to `/paymentMethods`. These are version-specific migration breaks, not universal SFCC behavior.
- Salesforce Composable Storefront v4.0.0 (2025-11-14) adds a companion `int_adyen_PWA` cartridge and requires its installation for that version's integration. Its v4.4.0 entry adds a Terminal API in-person endless-aisle route with cartridge metadata, environment and component setup. SFRA and Composable Storefront have separate packages and dependencies.
- Salesforce OMS v3.0.0 (2024-08-06) makes HMAC signature verification mandatory for that package's webhooks; Shopware 6 v4.0.0 (2024-07-18) describes its own HMAC verification as optional. These statements belong to different products and releases. OMS v2.1.0 also changes managed-package generation and namespace, with upgrade instructions.
- Cegid Retail Y2 v2.1.12 documents a receipt-log-length failure that can leave an Adyen-processed payment absent from Cegid, with reconciliation risk; v2.1.13 says it fixed that issue. The v2.1.14 TLS 1.3 Open Failed known issue is marked resolved by v2.1.19, whose entry says it reverted the TLS change. Do not treat the old known issues as unqualified present defects.
- NetSuite Reconciliation Bundle releases cover SDR import, CSV parsing, matching and deposit-creation diagnostics; the Payments Bundle has distinct Pay by Link, tokenization, authorization and capture fixes. A release note records a reported software change, not a merchant's payment, reconciliation or bank-credit outcome.

## Detail locators

- Page scope, GitHub handoff and release cadence: raw lines 15–34.
- 2026 Adobe Commerce v11 breaking changes, new cleanup cron (disabled by default), fixes and migration: lines 48–94.
- 2025 Adobe Commerce v10 and Express Checkout v3 migration/dependency changes: lines 432–453 and 509–583.
- Salesforce SFRA 2026 v26.1–v26.3 and Composable v4.0–v4.5: lines 104–149, 169–207, 280–365.
- SFRA 2025 v25.3 build break and older v24.2 flow/layout change: lines 591–620 and 1355–1389.
- Salesforce OMS v3 and v2.1 package/webhook changes: lines 1033–1057 and 1832–1859.
- Shopware 6 v4.0 HMAC/compatibility changes and v3.15 gift-card changes: lines 1128–1158 and 1253–1284.
- Cegid Retail Y2 receipt/TLS issue sequence and installation qualifications: lines 488–500, 714–725, 798–833 and 1299–1305.
- NetSuite Reconciliation Bundle SDR changes and Payments Bundle examples: lines 755–765, 840–851, 585–589 and 638–659.
- Historical Magento 2 and SFCC entries, including version-bound 3DS, payment-method and webhook changes: lines 2008–3482.

## Related

- [[adyen-magento2]]
- [[adyen-salesforce-commerce-cloud]]
- [[adyen-salesforce-order-management-system]]
- [[adyen-netsuite]]
- [[adyen-cegid-retail-y2]]

## Raw Sources

- [[raw/adyen/docs/plugins/release-notes/2026-09-15|Adyen plugin release notes, 2026-09-15 capture]]
