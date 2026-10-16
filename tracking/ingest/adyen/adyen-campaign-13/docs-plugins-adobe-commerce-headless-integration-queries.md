# Fixed queries — docs-plugins-adobe-commerce-headless-integration

## Q1 — Purpose, scope, and what must not be inferred

**Answer:** This Adyen webpage guides a merchant-built PWA checkout on a headless Adobe Commerce back end with the Adyen plugin installed and configured. REST and plugin-v8.2.0-or-later GraphQL routes pass data from storefront to Adobe Commerce to Adyen and back. It is an unversioned website snapshot with version-specific notes, separate from the exact-SHA `adyen/module-payment@11.0.0` repository baseline. The examples and status presentation do not prove current merchant method eligibility, successful live payment, capture, settlement, order fulfillment, or bank receipt.

**Raw locators:** lines 15–32 (identity, platform and version floor); 34–68 (checkout sequence and prerequisites); 503–611 (status and action semantics); 812–825 (match plugin, PHP library and API versions).

**Canonical route:** [[adyen-index]] → [[adyen-magento2]] → [[source-adyen-docs-plugins-adobe-commerce-headless-integration]] → [[raw/adyen/docs/plugins/adobe-commerce/headless-integration/2026-09-15]].

## Q2 — Central capability, prerequisites, and warnings

**Answer:** Configure Adyen Customer Area, plugin, payment methods and headless settings first. Logged-in shopper requests use a Bearer customer token; the guide says guests use a masked `card_id` without a token, using the page's field spelling and front-end integration tokens are no longer required. Retrieve session-filtered methods through Adobe Commerce REST or GraphQL, render and collect selected method data, place the Commerce order, query plugin payment status, and handle nonempty actions or additional details. GraphQL requires v8.2.0+. REST separate `state-data` support begins at v7.2.0 and persists payment data with a PCI-scope warning. The v11.0.0 `ccType` storage change and v9-only `brand_code` are conditional. PayPal uses `handleAction`; GraphQL gift cards require extra balance/state/redemption steps. Vault tokenization requires setup and method-specific enablement; token deactivation is server-side. Select API Explorer versions matching the installed plugin and PHP library.

**Raw locators:** lines 51–68 (configuration and authentication); 70–160 and 189–194 (method routes and parsing); 280–356 (order payload/version conditions); 435–448 (separate state and PCI warning); 503–611 (status/actions); 613–777 (GraphQL gift cards); 779–825 (Vault, token removal and version matching).

**Canonical route:** [[adyen-index]] → [[adyen-magento2]] → [[source-adyen-docs-plugins-adobe-commerce-headless-integration]]; detailed payloads and method conditions at [[raw/adyen/docs/plugins/adobe-commerce/headless-integration/2026-09-15]].
