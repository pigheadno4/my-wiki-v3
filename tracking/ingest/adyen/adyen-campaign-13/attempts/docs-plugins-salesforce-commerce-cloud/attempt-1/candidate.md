---
title: "Adyen Salesforce Commerce Cloud B2C Commerce integrations"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/salesforce-commerce-cloud"
raw_files:
  - "adyen/docs/plugins/salesforce-commerce-cloud/2026-09-15.md"
tags: [adyen, salesforce-commerce-cloud, sfra, composable-storefront, plugin]
---

## Overview

This Adyen Docs hub (captured 2026-09-15; metadata last modified 2025-02-05) compares two B2C Salesforce Commerce Cloud storefront integrations: an **SFRA payments cartridge** and a **Composable Storefront/PWA Kit npm package**. It advertises online, in-app and in-store processor use but supplies storefront integration choices and a feature/support table, not a live merchant integration record or proof of payment, order, refund, or settlement. The bounded provider concept [[adyen-salesforce-commerce-cloud]] routes this storefront family; see [[adyen]] for provider context.

## Key takeaways

- **SFRA** uses Adyen's payments cartridge and Adyen Web **Components** to display methods. **Composable Storefront (Headless)** uses `@adyen/adyen-salesforce-pwa` for Salesforce PWA Kit and Adyen Web **Drop-in**. These are different storefront packages and UI integrations; the page is not a versioned source-code audit of either one. [Raw lines 23–28]
- The feature table is explicitly not parity: both list cards/local methods, 3DS2 and risk checks, but SFRA lists Apple Pay, PayPal and Google Pay express methods while Composable lists Apple Pay and PayPal; SFRA lists multiple gift-card payments versus a generic gift-card check for Composable. It marks payment modifications absent for both, and marks endless aisle, case management, donations and Salesforce **Order Management package compatibility** on SFRA but not Composable. Recurring is “one-off and non-fixed schedule” for SFRA versus “one-off” for Composable. These are table claims from this dated hub, not proof of behavior in a particular installed release. [Raw lines 30–50]
- Adyen says no new SiteGenesis cartridge features are developed; the table says Level 3 support ended May 2025 and v22.2.3 is the latest SiteGenesis-compatible release. The support model distinguishes full support (Level 1), high-priority bug/security updates (Level 2), and security updates only (Level 3), with dated version tables for SFRA and Composable. Check the applicable installed major version and current support source before upgrade decisions. [Raw lines 34, 52–84]
- The raw frontmatter's 2025-02-05 last-modified timestamp predates table entries for **Composable V4 (November 2025)** and **SFRA V26 (January 2026)**. Preserve that metadata/table inconsistency rather than infer an exact table publication date. [Raw lines 10–11, 64–78]
- The separate Salesforce Order Management package is mentioned only as a compatibility feature row; this page does not define OMS operations, order-state behavior, credentials, webhook setup, or payment-modification implementation. Follow the linked storefront-specific setup guides for those details. [Raw lines 50, 86–96]

## Detail locators

- Storefront/package choice: raw lines 23–28. Feature comparison: raw lines 30–50. Support levels and version schedules, including SiteGenesis limit: raw lines 52–84. Integration navigation: raw lines 86–101.
- The links to cartridge, npm package, Sessions-flow Components/Drop-in, SFRA/Composable setup, and OMS at raw lines 23–28 and 50/86–96 are navigation; their target contents are not behavioral evidence in this entry.

## Related

- [[adyen-salesforce-commerce-cloud]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/plugins/salesforce-commerce-cloud/2026-09-15|Adyen Salesforce Commerce Cloud B2C Commerce hub, 2026-09-15 snapshot]]
