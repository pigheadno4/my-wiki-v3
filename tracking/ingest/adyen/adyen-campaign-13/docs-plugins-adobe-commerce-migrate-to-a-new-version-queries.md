# Fixed retrieval checks — Adyen Adobe Commerce major-version migration

## Q1 — Purpose, scope, and non-inference

**Question:** What does this migration guide cover, and what does following it not prove?

**Expected answer:** It gives distinct upgrade paths for existing Adobe Commerce plugin integrations moving to major versions 11, 10, or 9, including platform prerequisites, dependency review and breaking changes. It does not prove a deployment was upgraded, custom code remained compatible, webhooks arrived, token references survived in a usable state, or orders/payments succeeded. The v11 page's Commerce 2.4.8-or-later wording conflicts with the retained exact `adyen/module-payment@11.0.0` repository baseline, which says 2.4.8 only; exact-release compatibility must be checked.

**Raw locators:** Introduction lines 15–19; v11 lines 21–47, particularly 25; v10 lines 49–74; v9 lines 76–145. Related exact package baseline: [[source-github-adyen-magento2]].

**Canonical wiki route:** [[adyen-index]] → [[adyen-magento2]] → [[source-adyen-docs-plugins-adobe-commerce-migrate-to-a-new-version]].

## Q2 — Central capability, prerequisites, and warnings

**Question:** What differs across v11, v10 and v9, and which v9 changes need explicit configuration or verification?

**Expected answer:** V11 guide requirements are PHP 8.2+ and Commerce 2.4.8+, with Checkout API v71, Web Components 6.35.0 and PHP API Library v29.0.0; custom and headless integrations need compatibility/breaking-change review. V10 requires PHP 8.2+ and Commerce 2.4.8 and uses Checkout API v71 with Components 6.13.1. V9.0.1 uses Checkout API v70 and Components 5.51.1; later v9 dependencies may change. For manually configured v9 integrations the webhook URL suffix changes from `/process/json` to `/webhook`. V9 also changes method registration/selection and headless request fields, moves gift cards to a native `/orders` flow that needs Adyen-side configuration for existing gift-card setups, and uses Adobe Commerce Vault for tokenization. Tokenized methods and recurring model must be reconfigured; automatic token-reference migration should be verified, not presumed successful. The page points to monitoring/troubleshooting but specifies no rollback procedure.

**Raw locators:** V11 lines 23–47; v10 lines 51–74; v9 dependencies/webhook lines 90–106; method/headless lines 108–129; gift card lines 131–137; Vault lines 139–145; next steps 147–151.

**Canonical wiki route:** [[adyen-index]] → [[adyen-magento2]] → [[source-adyen-docs-plugins-adobe-commerce-migrate-to-a-new-version]] → [[raw/adyen/docs/plugins/adobe-commerce/migrate-to-a-new-version/2026-09-15|pinned raw snapshot]].
