# Fixed retrieval checks — docs-plugins-salesforce-commerce-cloud-sfra-upgrade

## Q1 — Purpose, scope, and what not to infer

**Query:** What is this Salesforce Commerce Cloud upgrade page for, and what does it not establish?

**Answer:** It guides upgrades of Adyen's **SFRA cartridge**, with separate default and customized integration routes, target SFRA-version checks, metadata import, builds and cartridge-path changes. It is not a Composable Storefront/PWA Kit upgrade guide, a verified compatibility matrix, a merchant deployment record or proof of payments after an upgrade. Page metadata says 2024-01-04 last modified; snapshot captured 2026-09-15. It has no backup/rollback, credential/token migration or test matrix instructions. Evidence: raw lines 10, 14–27, 29–127. Canonical route: [[adyen-index]] → [[adyen-salesforce-commerce-cloud]] → ## Sources → [[source-adyen-docs-plugins-salesforce-commerce-cloud-sfra-upgrade]] → [[raw/adyen/docs/plugins/salesforce-commerce-cloud/sfra/upgrade/2026-09-15]].

## Q2 — Central capability, prerequisites, and warnings

**Query:** How do the default and customized SFRA cartridge upgrade paths differ, and which version and change warnings matter?

**Answer:** Both require checking the SFRA version needed by the target cartridge, migrating SFRA if necessary, downloading the chosen release, re-uploading site metadata with the correct Business Manager site ID, building and setting the cartridge path. The default path builds the Adyen cartridge. The customized path first checks breaking changes and extracts modifications into a separate cartridge; it builds both the unmodified Adyen and custom cartridges, verifies custom-code compatibility, places the custom cartridge ahead of the target Adyen path and re-enables the Business Manager configuration page. The raw path table splits v23.3.2-or-earlier from v24.1.0-or-later. Review breaking changes across every intervening release, not just the destination. Site import and path adjustments change configuration; the page does not prove those operations succeeded or supply a backup/rollback or deployment test plan. Evidence: raw lines 31–63, 65–127. Canonical route: [[adyen-index]] → [[adyen-salesforce-commerce-cloud]] → ## Sources → [[source-adyen-docs-plugins-salesforce-commerce-cloud-sfra-upgrade]] → [[raw/adyen/docs/plugins/salesforce-commerce-cloud/sfra/upgrade/2026-09-15]].
