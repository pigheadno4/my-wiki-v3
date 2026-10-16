---
title: "Adyen Adobe Commerce plugin upgrade steps"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/adobe-commerce/upgrade"
raw_files:
  - "adyen/docs/plugins/adobe-commerce/upgrade/2026-09-15.md"
tags: [adyen, adobe-commerce, magento2, upgrade]
---

## Overview

This Adyen webpage snapshot gives command-level upgrade steps for the Adobe Commerce `adyen/module-payment` plugin, branching between a **default** and a **customized** integration. It recommends upgrading for major releases and states that plugin versions earlier than **9.0.0** are unsupported (raw lines 14–27). The page is an instruction set, not evidence that a merchant ran the commands, completed database migration, preserved custom code, or processed a payment. See [[adyen]] and [[adyen-magento2]].

## Key takeaways

- In the default branch, go to the Adobe Commerce project root, run `composer require adyen/module-payment:VERSION_TO_UPGRADE`, then `bin/magento setup:upgrade` to run database migration scripts, then `bin/magento cache:flush` (raw lines 29–49). The v11.0.0 command is an **example target**, not an instruction that every installation should select that version.
- In the customized branch, **extract custom code first**, then run the same dependency, database-upgrade, and cache-flush steps; afterward, check compatibility of that custom code with the selected new version and adjust it as needed (raw lines 51–75). The guide does not define a backup or rollback procedure, so extracting custom code should not be read as a complete recovery plan.
- The page says upgrade effort depends on customizations and links to GitHub releases for fixes/features (raw lines 20–27). Use the separate [[source-adyen-docs-plugins-adobe-commerce-migrate-to-a-new-version]] guide for target-major platform prerequisites, dependency and webhook/tokenization changes. The commands here do not establish compatibility for a specific Commerce/PHP version or merchant configuration.
- Raw metadata says last modified **2021-09-20**, while the captured body mentions a **v11.0.0** example (raw lines 10, 16, 39, 63). Treat both as snapshot evidence; do not infer an exact later update date or current support policy from that metadata alone.

## Detail locators

- Intro, raw lines 14–27: recommendation, support cutoff and default/customized branch selection.
- `Default Integration`, raw lines 29–49: Composer requirement, database migration and cache flush.
- `Customized Integration`, raw lines 51–75: extract custom code before upgrade and check compatibility after.

## Related

- [[adyen-magento2]] — versioned plugin architecture and package baseline.
- [[source-adyen-docs-plugins-adobe-commerce-migrate-to-a-new-version]] — major-version-specific platform and behavior changes.

## Raw Sources

- [[raw/adyen/docs/plugins/adobe-commerce/upgrade/2026-09-15|Upgrade the plugin, fetched 2026-09-15]]
