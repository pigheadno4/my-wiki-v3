---
title: "Adyen Salesforce Commerce Cloud"
type: concept
category: technology
tags: [adyen, salesforce-commerce-cloud, sfra, composable-storefront, plugin]
---

## Definition

Adyen's Salesforce Commerce Cloud B2C documentation overview describes two storefront integrations: an SFRA payments cartridge using Adyen Web Components, and a Composable Storefront/PWA Kit npm package using Adyen Web Drop-in. Its dated feature matrix is not at parity, and its support table distinguishes separate major-version timelines. The page says SiteGenesis receives no new cartridge features.

## Evidence boundary

This overview is a captured documentation page, not a versioned implementation audit or a merchant deployment record. Its 2025-02-05 last-modified metadata predates release rows for November 2025 and January 2026, so version support must be checked against the applicable current release. The Salesforce Order Management package is mentioned only as a feature-compatibility row; this overview does not define OMS operations, configuration, payment outcomes, or settlement.

## Sources

- [[source-adyen-docs-plugins-release-notes]] — 2019–2026 captured SFCC SFRA and Composable Storefront release chronology, including separate v26.1 SFRA webhook-cartridge and v4.0 Composable companion-cartridge migration locators.


- [[source-adyen-docs-plugins-salesforce-commerce-cloud-composable-storefront-upgrade]] — 2023-modified, 2026-09-15-captured Retail React `@adyen/adyen-salesforce-pwa` dependency-upgrade outline with major-release recommendation and MRT deployment link; build step repeats `npm install`, so verify the actual build and selected-release compatibility.


- [[source-adyen-docs-plugins-salesforce-commerce-cloud-sfra]] — 2024-modified, 2026-09-15-captured SFRA cartridge/Web Components landing guide with dated SFRA/Node support, default-checkout customization caveat and linked setup/test/go-live route; no exact release or payment-outcome proof.


- [[source-adyen-docs-plugins-salesforce-commerce-cloud-composable-storefront-troubleshooting]] — 2024-modified, 2026-09-15-captured Composable Storefront diagnostic route through logs, package version, release notes, GitHub issues and Support; cache/custom-cartridge isolation belongs to separate SFRA guidance, and no fix or payment result is verified.


- [[source-adyen-docs-plugins-salesforce-commerce-cloud-composable-storefront]] — 2024-modified, 2026-09-15-captured PWA Kit/Adyen Web Drop-in package landing page with test-account and child setup/go-live/migration routes; navigation is not deployment or payment proof.


- [[source-adyen-docs-plugins-salesforce-commerce-cloud-sfra-install-the-cartridge-and-import-the-metadata]] — 2023-modified, 2026-09-15-captured SFRA cartridge WebDAV/build and site-metadata import guide, with conditional ES5 transpilation, Business Manager service changes and endpoint-version warning; setup procedure is not deployment or payment proof.


- [[source-adyen-docs-plugins-salesforce-commerce-cloud-composable-storefront-customization-guide]] — 2024-modified, 2026-09-15-captured Composable Storefront/PWA package guide for front-end, server-controller and webhook overrides, with post-deployment/testing advice, package-edit prohibition and no pre-built Salesforce OMS integration.


- [[source-adyen-docs-plugins-salesforce-commerce-cloud-sfra-upgrade]] — 2024-modified, 2026-09-15-captured SFRA cartridge default/custom upgrade paths, v23.3.2-to-v24.1.0 path split and intervening breaking-change review; no merchant deployment or compatibility proof.


- [[source-adyen-docs-plugins-salesforce-commerce-cloud-sfra-troubleshooting]] — 2020-modified, 2026-09-15-captured SFRA cartridge diagnostic guide for cache/customization/log isolation, method/configuration errors and exact OriginKey/PayPal symptoms; remedies are conditional, not verified fixes.


- [[source-adyen-docs-plugins-salesforce-commerce-cloud-sfra-customization-guide]] — 2026-09-15 SFRA cartridge customization guide for v23.2.1+ separate-cartridge overrides, method configuration and v25.4.0+ pre-authorization hook; default-cartridge edit instructions conflict with its support/upgrade warning.


- [[source-adyen-docs-plugins-salesforce-commerce-cloud-composable-storefront-go-live-checklist]] — 2023-modified, 2026-09-15-captured Composable Storefront live-preparation checklist for separate live account/API/MRT/webhook/region setup, conditional wallets, 3DS/CSP and fee-incurring real-detail tests; a checklist or webhook HTTP 200 is not proof of payment completion.


- [[source-adyen-docs-plugins-salesforce-commerce-cloud-supported-payment-methods]] — 2026-09-15-captured SFRA/Composable method-and-version matrix and merchant-account request route; raw 2025-08-04 metadata conflicts with SFRA V26 rows, and country/feature eligibility requires separate lookup.


- [[source-adyen-docs-plugins-salesforce-commerce-cloud-composable-storefront-set-up-payment-methods]] — 2026-09-15 Adyen Composable Storefront guide for Business Manager method activation and version-qualified Apple Pay, Click to Pay, installments, PayPal express and Google Pay setup; distinct from SFRA and live-payment proof.


- [[source-adyen-docs-plugins-salesforce-commerce-cloud-composable-storefront-install-and-set-up-the-package]] — 2026-09-15 Adyen Composable Storefront setup guide for the PWA npm package and SFCC cartridge, site/credential/webhook/MRT configuration, optional version-gated features and migration/testing boundaries.


- [[source-adyen-docs-plugins-salesforce-commerce-cloud-sfra-go-live-checklist]] — 2026-09-15 SFRA live-preparation checklist for separate live account/credentials/webhooks, real-payment testing, versioned Business Manager settings and older shared-prefix limit; checklist completion is not outcome proof.


- [[source-adyen-docs-plugins-salesforce-commerce-cloud-sfra-set-up-payment-methods]] — 2023-modified, 2026-09-15-captured SFRA cartridge guide to merchant-account method prerequisites, Business Manager processor/display settings and conditional Apple Pay, Amazon Pay, Klarna, installments, gift-card, Google Pay and PayPal setup; configuration is not live outcome proof.


- [[source-adyen-docs-plugins-salesforce-commerce-cloud-sfra-set-up-the-cartridge]] — 2026-09-15 Adyen SFRA cartridge setup guide for test/live keys, storefront and Business Manager configuration, webhook security and scheduled order-status processing, plus optional features and pending CSC payment-link orders.


- [[source-adyen-docs-plugins-salesforce-commerce-cloud]] — 2026-09-15 SFCC B2C storefront overview for SFRA cartridge/Components versus Composable PWA package/Drop-in, dated feature and support comparison, and SiteGenesis limit.

## Related

- [[adyen]]
