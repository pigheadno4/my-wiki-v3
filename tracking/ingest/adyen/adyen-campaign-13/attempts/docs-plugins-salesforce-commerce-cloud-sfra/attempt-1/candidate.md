---
title: "Adyen Salesforce Commerce Cloud SFRA cartridge overview"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/salesforce-commerce-cloud/sfra"
raw_files:
  - "adyen/docs/plugins/salesforce-commerce-cloud/sfra/2026-09-15.md"
tags: [adyen, salesforce-commerce-cloud, sfra, cartridge, web-components]
---

## Overview

This 2024-01-10-last-modified, 2026-09-15-captured landing guide introduces Adyen's **Salesforce Commerce Cloud SFRA payments cartridge**, built with Adyen Web Components, and routes merchants through test-account preparation, installation/metadata import, cartridge and payment-method setup, optional customization, test payments and go-live checks. It describes the SFRA cartridge, not the separate Composable Storefront/PWA npm package. See [[adyen-salesforce-commerce-cloud]] and [[adyen]].

## Key takeaways

- **Architecture and dated support:** The page calls the cartridge an SFRA payment solution based on Adyen Web Components. Its snapshot support list is SFRA versions 5, 6 and 7 and Node v14 or later; it does not pin a cartridge release. Check the applicable current package/version and method matrix before treating the landing-page claim about access to Adyen platform features as method or account eligibility.
- **Customization caveat:** The page says support may be unavailable outside the default checkout and discourages plugin customization because of upgrade/maintenance cost. If customizing, it recommends tracking custom code and following its separate customization guide.
- **Integration route:** It points to an Adyen test account while live credentials are pending, then installation and metadata import, cartridge setup, payment-method setup, optional customization, test cards and a go-live checklist. These links locate the child procedures; this overview does not provide their detailed configuration, security or payment-lifecycle behavior, nor demonstrate that installation, a test transaction or live payment succeeded.
- **Navigation issue:** The final troubleshooting link points to `/plugins/salesforce-commerce-cloud/composable-storefront/`, not the SFRA troubleshooting path. Use the SFRA-specific guide for SFRA diagnostics rather than inferring that the linked Composable page describes SFRA behavior.

## Detail locators

- Lines 15–23: SFRA identity, broad platform pitch and Web Components architecture.
- `## Supported versions`, lines 25–39: unpinned latest-version route, snapshot SFRA/Node list and customization/support caveat.
- `## Get started`, lines 41–58: account prerequisite and linked test-to-live integration sequence; line 58 contains the mismatched troubleshooting link.
- `## Next steps`, lines 60–66: installation/metadata-import navigation.

## Related

- [[adyen-salesforce-commerce-cloud]] — SFRA versus Composable Storefront and version boundary.
- [[source-adyen-docs-plugins-salesforce-commerce-cloud-sfra-install-the-cartridge-and-import-the-metadata]] — SFRA build and metadata-import procedure.
- [[source-adyen-docs-plugins-salesforce-commerce-cloud-sfra-set-up-the-cartridge]] — subsequent credential, webhook and Business Manager setup.
- [[source-adyen-docs-plugins-salesforce-commerce-cloud-sfra-set-up-payment-methods]] — conditional payment-method setup.
- [[source-adyen-docs-plugins-salesforce-commerce-cloud-sfra-go-live-checklist]] — separate go-live preparation.
- [[source-adyen-docs-plugins-salesforce-commerce-cloud-sfra-troubleshooting]] — SFRA-specific diagnostics.

## Raw Sources

- [[raw/adyen/docs/plugins/salesforce-commerce-cloud/sfra/2026-09-15|SFRA cartridge overview, captured 2026-09-15]]
