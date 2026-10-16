---
title: "Adyen Composable Storefront package upgrade"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/salesforce-commerce-cloud/composable-storefront/upgrade"
raw_files:
  - "adyen/docs/plugins/salesforce-commerce-cloud/composable-storefront/upgrade/2026-09-15.md"
tags: [adyen, salesforce-commerce-cloud, composable-storefront, npm, upgrade]
---

## Overview

This 2023-09-29-last-modified, 2026-09-15-captured short guide outlines a package-version change for Adyen's **Salesforce Commerce Cloud Composable Storefront/Retail React** integration using `@adyen/adyen-salesforce-pwa`. It is distinct from the SFRA cartridge upgrade path and gives no evidence of a merchant deployment or version compatibility. See [[adyen-salesforce-commerce-cloud]] and [[adyen]].

## Key takeaways

- **Version choice and scope:** Adyen recommends upgrading on a major release such as v2.x.x and points readers to npm and release notes for the latest version. The guide's `1.0.0` to `2.0.0` dependency change is an example, not a statement that either is current or compatible with a particular app.
- **Stated sequence:** In the Retail React app's `package.json`, change the `@adyen/adyen-salesforce-pwa` dependency version, install the new version, then follow the linked Managed Runtime deployment steps. The page does not enumerate peer dependency, breaking-change, migration, webhook, security or rollback requirements; those must be assessed against the selected release and installation context.
- **Build-command ambiguity:** The raw labels step 4 “Build your app with the new version” but repeats `npm install`, the same command used for step 3. Do not infer that `npm install` performs an app build or substitute an unverified command from this page. Verify the actual project's build process before deployment.
- **Outcome boundary:** Editing a dependency, running the shown command, or following deployment navigation does not establish that a new package was built, deployed, compatible, secure or processing payments successfully.

## Detail locators

- Lines 15–19: Composable Storefront scope, major-release recommendation, npm and release-note lookup.
- Lines 21–32: Retail React `package.json` dependency and example `1.0.0` → `2.0.0` change.
- Lines 33–41: install command, duplicated build-step command and linked MRT deployment route.

## Related

- [[adyen-salesforce-commerce-cloud]] — SFRA versus Composable Storefront architecture and support boundary.
- [[source-adyen-docs-plugins-salesforce-commerce-cloud-composable-storefront-install-and-set-up-the-package]] — package installation and Managed Runtime deployment route.
- [[source-adyen-docs-plugins-salesforce-commerce-cloud-composable-storefront-customization-guide]] — upgrade-safe customization advice.
- [[source-adyen-docs-plugins-salesforce-commerce-cloud-sfra-upgrade]] — separate SFRA cartridge upgrade path.

## Raw Sources

- [[raw/adyen/docs/plugins/salesforce-commerce-cloud/composable-storefront/upgrade/2026-09-15|Composable Storefront package upgrade, captured 2026-09-15]]
