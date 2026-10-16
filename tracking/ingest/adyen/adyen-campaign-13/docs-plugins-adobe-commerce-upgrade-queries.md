# Fixed retrieval checks — Adyen Adobe Commerce plugin upgrade

## Q1 — Purpose, scope, and non-inference

**Question:** What does this page instruct for plugin upgrades, and what should a reader not infer from its v11 example or commands?

**Expected answer:** It gives default and customized upgrade command sequences for `adyen/module-payment`, recommends upgrades at major releases, and states a support cutoff before v9.0.0 in this snapshot. The v11.0.0 command is an example target; the page does not establish that v11 is compatible with a particular Adobe Commerce/PHP installation or that any commands were run successfully. It is separate from the major-version migration guide, which owns target-specific dependency and behavior changes. The raw says last modified 2021-09-20 while its body mentions v11.0.0, so do not infer an exact update date or independent current support policy.

**Raw locators:** Frontmatter line 10; intro lines 14–27; default command/example lines 29–49; customized branch lines 51–75.

**Canonical wiki route:** [[adyen-index]] → [[adyen-magento2]] → [[source-adyen-docs-plugins-adobe-commerce-upgrade]].

## Q2 — Central capability, prerequisites, and warnings

**Question:** What are the default versus customized command steps, and what operational effects or missing protections need attention?

**Expected answer:** In the default branch, move to the Adobe Commerce project root, then run `composer require adyen/module-payment:VERSION_TO_UPGRADE`, `bin/magento setup:upgrade` database migrations, and `bin/magento cache:flush`. In the customized branch, first extract added custom code, then move to that project root and run the same three commands; afterward, check custom-code compatibility with the new version and apply changes if needed. These steps alter dependencies/database/cache and are not read-only validation. The page does not specify a backup or rollback procedure, nor prove custom code, stored tokens, order status, or payments survived. Consult the separate migration guide and exact target release for platform/dependency/webhook/tokenization requirements.

**Raw locators:** Default Integration lines 29–49; Customized Integration lines 51–75; support/release links lines 16–27.

**Canonical wiki route:** [[adyen-index]] → [[adyen-magento2]] → [[source-adyen-docs-plugins-adobe-commerce-upgrade]] → [[raw/adyen/docs/plugins/adobe-commerce/upgrade/2026-09-15|pinned raw snapshot]].
