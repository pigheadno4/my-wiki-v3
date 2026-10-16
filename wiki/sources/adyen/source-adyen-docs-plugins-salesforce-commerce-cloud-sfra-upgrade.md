---
title: "Upgrade the Salesforce Commerce Cloud SFRA cartridge"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/salesforce-commerce-cloud/sfra/upgrade"
raw_files:
  - "adyen/docs/plugins/salesforce-commerce-cloud/sfra/upgrade/2026-09-15.md"
tags: [adyen, salesforce-commerce-cloud, sfra, upgrade]
---

## Overview

Adyen's SFRA payments-cartridge upgrade guide (page metadata last modified 2024-01-04; captured 2026-09-15) recommends upgrading at major releases or from an unmaintained version and separates default from customized integration steps. It describes changing SFRA and cartridge versions, site metadata and cartridge paths; it does not certify compatibility, merchant readiness, completed deployment or payment outcomes. Route through [[adyen-salesforce-commerce-cloud]] for the SFRA-versus-Composable distinction.

## Key takeaways

- Upgrade effort depends on cartridge customization. Before either path, check the SFRA version required by the target cartridge and migrate SFRA if needed; the guide recommends the latest SFRA. Select a cartridge release from GitHub rather than assuming all versions are interchangeable (raw lines 16–33, 65–75).
- For the default integration, re-upload metadata with customizations included, replace the RefArch `yourSiteId` and `jobs.xml` `site-id` values with the Business Manager site ID, import the zipped `site_import` through Business Manager, run `npm run build`, and update the SFRA cartridge path (raw lines 35–59). These are site-configuration changes, not evidence that the import/build worked.
- The path table distinguishes **v23.3.2 or earlier** (`int_adyen_SFRA:int_adyen_overlay:app_storefront_base`) from **v24.1.0 or later** (`app_adyen_SFRA:int_adyen_SFRA:app_storefront_base`). Use the path for the target version; the raw table is at lines 61–63 (and 113–115 for customized integration).
- For a customized integration, first examine breaking changes, extract custom code from the Adyen cartridge into a separate cartridge, then check/migrate SFRA, download the target release, re-upload site metadata, build both the unmodified Adyen and custom cartridges, assess compatibility of custom code, set the custom cartridge ahead of the target Adyen path, and re-enable the Business Manager configuration page (raw lines 65–117). The raw page points to the customization guide for extraction details; they are not established by this page alone.
- Breaking changes must be considered across **all intervening releases** between the installed and target versions, not just the destination release; the page gives v21.2.0 → v23.1.0 as an example (raw lines 123–127). It does not prescribe a backup/rollback procedure, test matrix, credential or token migration, or merchant-specific compatibility result; those require separate evidence and operational planning.

## Detail locators

- Upgrade recommendation, support schedule and customization fork: raw lines 16–27.
- Default integration's SFRA check, metadata import, build and path: raw lines 29–63.
- Customized integration's extraction, separate cartridge, two builds and Business Manager re-enable: raw lines 65–117.
- Breaking-change review across intervening versions: raw lines 123–127.

## Related

- [[adyen-salesforce-commerce-cloud]] — SFCC integration concept, distinct SFRA and Composable routes.
- [[adyen]] — Adyen provider page.

## Raw Sources

- [[raw/adyen/docs/plugins/salesforce-commerce-cloud/sfra/upgrade/2026-09-15|SFRA cartridge upgrade, captured 2026-09-15]]
