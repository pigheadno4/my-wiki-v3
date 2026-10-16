---
title: "Adyen Adobe Commerce plugin overview"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/adobe-commerce"
raw_files:
  - "adyen/docs/plugins/adobe-commerce/2026-09-15.md"
tags: [adyen, adobe-commerce, magento2, plugin, checkout]
---

## Overview

This Adyen Docs landing guide presents the Adobe Commerce (formerly Magento 2) payment plugin, its **standard** and **headless** integration choices, feature matrix, version/support table, checkout/webhook overview and setup routes. The plugin is described for Magento 2, Adobe Commerce and Adobe Commerce Cloud. This is a 2026-09-15 documentation snapshot with 2025-04-29 last-modified metadata, not an exact installed package or a merchant's live configuration. The version-qualified implementation baseline is [[adyen-magento2]] and [[source-github-adyen-magento2]]; do not infer payment, order, refund or settlement success from this overview. See [[adyen]].

## Key takeaways

- **Integration shape:** Standard integration uses Adyen Web Components with the default Adobe Commerce Checkout theme. Headless integration lets the merchant build a checkout form for an Adobe Commerce PWA storefront while the plugin supplies a headless back end. The page says the plugin brings payment methods, tokenization and risk management into a synchronized Commerce/Adyen integration, with Commerce transaction summaries and Adyen detailed reporting. Storefront implementation and the precise enabled methods remain configuration- and version-dependent.
- **Feature matrix:** The snapshot marks credit cards, local methods, tokenization, Dynamic 3DS2, risk management, Pay by Link, donations, express methods and in-person payments for both forms. It marks back-end MOTO orders and Multiple Address Shipping for **standard only**, not headless. Those checkmarks are product-documentation claims, not proof a method is enabled, regionally eligible or working for a particular merchant.
- **Version boundary:** The docs table states V9 ↔ Adobe Commerce 2.4.4–2.4.7, V10 ↔ 2.4.8, and V11 ↔ 2.4.8 or later, while saying compatibility depends on plugin version. The separate pinned `adyen/module-payment@11.0.0` GitHub baseline says Magento **2.4.8 only**. The broad major-version docs row must not override that exact release constraint; check the precise package release and current support matrix before installation or upgrade. The raw table also defines Level 1/2/3 support and dated end dates; after Level 3 ends, Adyen says security updates and support stop.
- **Support and customization:** The page warns support may be unavailable without the default Adobe Commerce checkout and discourages plugin customization because upgrades and maintenance become harder. For headless, Adyen describes its support as back-end API request processing, authentication and payment lifecycle; merchant front end, custom back-end logic and third-party dependencies are outside that scope.
- **Checkout and setup:** The overview says the plugin uses Adyen Checkout API during checkout and webhooks to update Commerce order statuses, with order summaries in Commerce and detail in Adyen. It directs merchants to create a test account, set up test Customer Area/API credentials and webhooks, configure the plugin and methods, test, then use the go-live checklist. Those links are routes to separate instructions; authorization, webhook receipt, a Commerce status, and a live financial outcome need their own evidence.

## Detail locators

- Lines 15–30: plugin identity, supported host-platform names and standard/headless architecture.
- `## Features`, lines 32–48: integration-type matrix, including standard-only MOTO and multiple-address shipping.
- `## Supported versions`, lines 50–58: docs compatibility table; compare exact `11.0.0` baseline in [[source-github-adyen-magento2]].
- `### Support levels`, lines 60–87: support levels/dates, default checkout and headless/customization boundary.
- `## How it works`, lines 89–95: Checkout API, webhook/order-status sync and reporting route.
- `## Get started`, lines 97–113, and `## Next steps`, lines 121–133: test-account and separate setup/go-live guide routes.

## Related

- [[adyen-magento2]] — canonical plugin concept and reciprocal source route.
- [[source-github-adyen-magento2]] — exact `adyen/module-payment@11.0.0` repository evidence, not a substitute for this dated docs table.
- [[changelog-github-adyen-magento2]] — release-history and migration boundary.

## Raw Sources

- [[raw/adyen/docs/plugins/adobe-commerce/2026-09-15|Adobe Commerce plugin overview, captured 2026-09-15]]
