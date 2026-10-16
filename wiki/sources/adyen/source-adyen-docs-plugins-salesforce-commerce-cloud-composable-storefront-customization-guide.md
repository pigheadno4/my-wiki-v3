---
title: "Adyen Composable Storefront customization guide"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/salesforce-commerce-cloud/composable-storefront/customization-guide"
raw_files:
  - "adyen/docs/plugins/salesforce-commerce-cloud/composable-storefront/customization-guide/2026-09-15.md"
tags: [adyen, salesforce-commerce-cloud, composable-storefront, customization, webhooks]
---

## Overview

This 2024-09-11-last-modified, 2026-09-15-captured guide describes extension points for Adyen's Salesforce Commerce Cloud **Composable Storefront/PWA** npm-package integration. It recommends starting after Managed Runtime deployment and integration testing, then overriding package functions for checkout UI, server controllers and webhook handling. It is separate from the SFRA cartridge route. See [[adyen-salesforce-commerce-cloud]] and [[adyen]].

## Key takeaways

- **Upgrade-safe extension boundary:** Create documented, modular overrides; the guide says not to modify Adyen npm package code. These are recommended practices for future upgrades and troubleshooting, not evidence that a deployed customization is compatible with any particular package version.
- **Front end:** Pass checkout customizations to `AdyenCheckoutProvider`. The listed options include checkout styling, payment-method appearance through `paymentMethodsConfiguration`, localization, Drop-in `beforeSubmit`/`onSubmit` callbacks and an added CSS import. Linked GitHub implementations and Web Drop-in 5.63.0 references are examples, not a support or payment-success guarantee.
- **Server and webhook controllers:** The guide describes adding/replacing controllers through an override array in `overrides/app/ssr.js`, with custom payment functions such as pre-authorization risk checks as examples. Its introductory path is misspelled `ovverrides/app/ssr.js` while its webhook section uses `overrides/app/ssr.js`; verify the installed package/path rather than copying the typo. The webhook example retains `authenticate`, `validateHmac`, and `parseNotification` before a custom handler; preserving those security steps matters when adapting the example.
- **Order handling boundary:** After webhook setup, `AUTHORISATION` handling is described as enabled by default. Other event/order flows need a custom webhook controller; the guide points to B2C Commerce Orders API for order, payment and export statuses. The package has no pre-built integration with Adyen's Salesforce OMS package, so OMS compatibility requires custom webhook handling for ready-for-export synchronization. A registered controller, webhook receipt or updated Commerce status is not proof of a successful payment, export or settlement.

## Detail locators

- Lines 15–26: identity, recommended MRT deployment/testing prerequisite, modular overrides and do-not-modify-package guidance.
- `## Front end customizations`, lines 28–46: provider, styling, translations, callbacks, CSS and linked examples.
- `## Back-end customizations`, lines 48–59: controller override arrays, payment-controller example and misspelled introductory path.
- `## Webhook controller customizations`, lines 61–92: configured webhooks, default AUTHORISATION handler, security-function chain, Orders API status route and absence of pre-built OMS integration.

## Related

- [[adyen-salesforce-commerce-cloud]] — SFRA versus Composable Storefront route and dated support boundary.
- [[source-adyen-docs-plugins-salesforce-commerce-cloud-composable-storefront-install-and-set-up-the-package]] — deployment, test and webhook setup prerequisites.
- [[source-adyen-docs-plugins-salesforce-commerce-cloud-composable-storefront-go-live-checklist]] — live-preparation and outcome-check boundary.

## Raw Sources

- [[raw/adyen/docs/plugins/salesforce-commerce-cloud/composable-storefront/customization-guide/2026-09-15|Composable Storefront customization guide, captured 2026-09-15]]
