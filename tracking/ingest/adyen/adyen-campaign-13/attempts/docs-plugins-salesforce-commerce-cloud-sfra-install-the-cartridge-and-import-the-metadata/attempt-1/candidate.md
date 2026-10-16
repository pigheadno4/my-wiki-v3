---
title: "Adyen SFRA cartridge installation and metadata import"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/salesforce-commerce-cloud/sfra/install-the-cartridge-and-import-the-metadata"
raw_files:
  - "adyen/docs/plugins/salesforce-commerce-cloud/sfra/install-the-cartridge-and-import-the-metadata/2026-09-15.md"
tags: [adyen, salesforce-commerce-cloud, sfra, cartridge, metadata]
---

## Overview

This 2023-06-15-last-modified, 2026-09-15-captured guide lays out preparatory steps to build Adyen's **Salesforce Commerce Cloud SFRA cartridge** and import its site metadata into Business Manager. Its scope is the SFRA cartridge, not the Composable Storefront/PWA npm package. It does not establish that a specific merchant has installed, activated or tested the cartridge. See [[adyen-salesforce-commerce-cloud]] and [[adyen]].

## Key takeaways

- **Prerequisites and version condition:** The guide calls for Salesforce Sandbox access, the SFRA repository with developer access, and a downloaded Adyen cartridge. It says cartridge v25.3.0 or later uses ES6+ and requires transpilation when the Salesforce environment needs ES5; the page's 2023 last-modified metadata is older than that version reference, so confirm release-specific requirements before relying on it.
- **Connection/build steps:** It instructs creating a cartridge-root `dw.json` with sandbox hostname, username, WebDAV access key and target code version, then running `npm install` and `npm run build`. The build description says the command transpiles/compiles source from `/src` and writes deployable output to `/cartridges`. The page does not document cartridge-path activation or a completed upload; the next linked setup guide carries subsequent configuration. Treat the `dw.json` fields as deployment credentials and avoid exposing their values.
- **Metadata import changes configuration:** It directs merchants to customize the metadata, replace `yourSiteId` and `jobs.xml` `site-id` with the actual Business Manager site ID, zip `site_import`, then import it through **Site Import & Export**. The guide says this adds Adyen attributes for site preferences, orders and custom objects, plus named services including `AdyenPayment`, `AdyenRecurring` and `AdyenCheckoutPaymentMethods`. Import is a state-changing Business Manager action; this page does not specify overwrite behavior for an existing site configuration, so inspect the actual package and target before import.
- **Endpoint/version and outcome boundary:** It warns against changing the imported services' endpoint version numbers because doing so can cause integration errors. The next step is separate cartridge setup in Adyen Customer Area and Business Manager. Commands, metadata examples and an import procedure are instructions, not evidence of actual installation, payment authorization, webhook processing or settlement.

## Detail locators

- `## Prerequisites`, lines 16–23: sandbox/SFRA/cartridge access and conditional v25.3.0+ ES6-to-ES5 rule.
- `## Step 1: Set your credentials and version`, lines 25–36: `dw.json` WebDAV credentials and target code version.
- `## Step 2: Install Node modules` and `## Step 3: Build the code`, lines 38–58: package install, build and `/cartridges` output.
- `## Step 4: Import the metadata`, lines 60–88: site ID substitutions, Business Manager import path, attributes/services and endpoint-version warning.
- `## Next steps`, lines 94–100: subsequent cartridge configuration route.

## Related

- [[adyen-salesforce-commerce-cloud]] — SFRA versus Composable Storefront and version boundary.
- [[source-adyen-docs-plugins-salesforce-commerce-cloud-sfra-set-up-the-cartridge]] — subsequent Adyen Customer Area and Business Manager setup.
- [[source-adyen-docs-plugins-salesforce-commerce-cloud-sfra-upgrade]] — version-specific upgrade path.

## Raw Sources

- [[raw/adyen/docs/plugins/salesforce-commerce-cloud/sfra/install-the-cartridge-and-import-the-metadata/2026-09-15|SFRA cartridge install and metadata import, captured 2026-09-15]]
