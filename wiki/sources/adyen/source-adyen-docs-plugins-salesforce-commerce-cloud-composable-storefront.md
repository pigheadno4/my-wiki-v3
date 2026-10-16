---
title: "Adyen Composable Storefront package for Salesforce B2C Commerce"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/salesforce-commerce-cloud/composable-storefront"
raw_files:
  - "adyen/docs/plugins/salesforce-commerce-cloud/composable-storefront/2026-09-15.md"
tags: [adyen, salesforce-commerce-cloud, composable-storefront, pwa-kit]
---

## Overview

This Adyen Composable Storefront landing page (metadata last modified 2024-01-25; captured 2026-09-15) identifies a headless payments package for Salesforce B2C Commerce stores built with PWA Kit. It says the package includes front-end and back-end components for Adyen Web Drop-in, and routes readers to installation, payment-method setup, customization, testing, go-live and migration guidance. This is an integration overview and navigation entry, not a versioned implementation audit or proof of merchant enablement, deployment or payment outcome. [[adyen-salesforce-commerce-cloud]] distinguishes this PWA package from the SFRA cartridge.

## Key takeaways

- The package targets a Salesforce PWA Kit storefront, whether based on the default Retail React App or a custom Retail React App. The page describes Salesforce Managed Runtime as the route to deploy, host and monitor a built storefront; it does not show that a particular storefront is deployed (raw lines 23–35).
- Before integration, the page routes merchants to Adyen's get-started guide for live-payment preparation and test-account creation. It says integration can begin with a test account while waiting for live credentials, and points to npm to find the latest package version; it supplies no exact installed package version or compatibility proof (raw lines 37–45).
- The remaining steps are links to install/setup, payment methods, customization, test cards, go-live checklist and troubleshooting. These are navigation to separate instructions, not evidence that the linked configuration, payment tests or go-live steps occurred (raw lines 45–57).
- For an existing Adyen SFRA or SiteGenesis integration, the page says migration to Composable Storefront requires the standard installation/setup guide plus its store-page migration step, and recommends migrating in test first. This does not establish a completed migration or token/order continuity (raw lines 59–63).

## Detail locators

- PWA Kit / Drop-in integration identity and Managed Runtime: raw lines 15–27.
- Retail React App choice and test-account preparation: raw lines 29–44.
- Child setup, test, go-live and troubleshooting routes: raw lines 45–57, 65–77.
- SFRA/SiteGenesis migration route and test-first recommendation: raw lines 59–63.

## Related

- [[adyen-salesforce-commerce-cloud]] — SFCC concept and SFRA-versus-Composable boundary.
- [[source-adyen-docs-plugins-salesforce-commerce-cloud-composable-storefront-install-and-set-up-the-package]] — child installation and migration guide.
- [[source-adyen-docs-plugins-salesforce-commerce-cloud-composable-storefront-set-up-payment-methods]] — child payment-method configuration guide.
- [[source-adyen-docs-plugins-salesforce-commerce-cloud-composable-storefront-go-live-checklist]] — child live-preparation checklist.
- [[adyen]] — provider page.

## Raw Sources

- [[raw/adyen/docs/plugins/salesforce-commerce-cloud/composable-storefront/2026-09-15|Composable Storefront landing page, captured 2026-09-15]]
