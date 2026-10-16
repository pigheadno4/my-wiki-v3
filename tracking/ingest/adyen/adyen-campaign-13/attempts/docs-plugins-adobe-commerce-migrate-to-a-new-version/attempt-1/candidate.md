---
title: "Adyen Adobe Commerce major-version migration"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/adobe-commerce/migrate-to-a-new-version"
raw_files:
  - "adyen/docs/plugins/adobe-commerce/migrate-to-a-new-version/2026-09-15.md"
tags: [adyen, adobe-commerce, magento2, migration]
---

## Overview

This Adyen webpage snapshot gives separate **major-version migration paths to plugin v11, v10, and v9** for an existing Adobe Commerce integration. It describes prerequisites and changes to review; it does not show that a merchant's deployment, webhook delivery, stored tokens, checkout, or payments survived an upgrade. See [[adyen]] and [[adyen-magento2]].

## Key takeaways

- **To v11:** the guide states PHP **8.2+** and Adobe Commerce **2.4.8+**; from v10 it says no platform upgrade is needed, while from v9 it directs the platform/PHP upgrade first. V11 uses Checkout API **v71**, Web Components **6.35.0**, and Adyen PHP API Library **v29.0.0**. Custom plugin logic, Components, headless flows, and API-object handling need compatibility review, followed by v11 breaking-change release notes (raw lines 21–47). Its “no action” sentence applies to default checkout/payment logic in the dependency-review step, not to skipping the plugin upgrade or all checks.
- **To v10:** the guide says PHP **8.2+** and Adobe Commerce **2.4.8**, with no support for 2.4.7 or earlier. It lists Checkout API **v71** and Web Components **6.13.1**, plus custom/headless compatibility and breaking-change review (raw lines 49–74).
- **To v9:** the page anchors dependencies to **v9.0.1**: Checkout API **v70** and Components **5.51.1**. It says later v9 releases may change these and must be checked in release notes. It also notes PHP **8.1+** when using Adobe Commerce 2.4.4 (raw lines 76–94). For **manually configured** integrations, the webhook server URL must change from `/process/json` to `/webhook` to continue receiving webhooks (lines 96–106).
- V9 separates payment-method registration, changes default shopper-method selection by **billing-address country/region** with an ISO Country Code override, and changes headless method names and the `shippingAddress` requirement for `/paymentMethods` (raw lines 108–129). The gift-card route changes from an Adyen-hosted page to a native Checkout `/orders` flow, but previously configured gift cards need **additional Adyen-side configuration** to use it (lines 131–137).
- V9 uses **Adobe Commerce Vault** for tokenization. Merchants using tokenization must reconfigure selected methods and a recurring processing model. The guide says previously Adyen-stored token references migrate to the Vault automatically and recommends manually verifying the references (raw lines 139–145). This is migration guidance, not proof that any particular stored credential remains usable.
- **Compatibility conflict to retain:** this guide says v11 requires Adobe Commerce **2.4.8 or later** (raw line 25), whereas the retained exact `adyen/module-payment@11.0.0` repository summary says **2.4.8 only** ([[source-github-adyen-magento2]]). Check the exact target package/release before treating a later Commerce version as supported. The page gives a troubleshooting/monitoring route (lines 147–151), but no rollback procedure.

## Detail locators

- `Migrate to version 11`, raw lines 21–47: platform requirements, dependencies and custom-code/breaking-change review.
- `Migrate to version 10`, raw lines 49–74: platform/dependency requirements and review.
- `Migrate to version 9`, raw lines 76–145: specific v9.0.1 dependency baseline, manual webhook URL change, payment-method/gift-card/tokenization changes.

## Related

- [[adyen-magento2]] — plugin architecture and exact package baseline.
- [[source-github-adyen-magento2]] — exact v11.0.0 repository evidence and compatibility qualification.

## Raw Sources

- [[raw/adyen/docs/plugins/adobe-commerce/migrate-to-a-new-version/2026-09-15|Migrate to a new version, fetched 2026-09-15]]
