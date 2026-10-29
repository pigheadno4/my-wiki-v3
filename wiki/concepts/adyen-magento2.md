---
title: "Adyen Adobe Commerce Plugin"
type: concept
category: technology
tags: [adyen, adobe-commerce, magento2, checkout, webhooks, pos, vault]
---

## Adyen Adobe Commerce Plugin

The Adyen Adobe Commerce Plugin is the `adyen/module-payment` integration for Magento 2. It connects Adobe Commerce checkout, order, invoice, vault, webhook, and point-of-sale lifecycles to Adyen Checkout and Terminal APIs.

## Current baseline

The first retained baseline is `adyen/module-payment@11.0.0` at exact SHA `4206983499d829ef695185ac78af06b9bdfe96c6`. It supports Magento 2.4.8 only, PHP 8.2 through 8.5, Checkout API v71, Adyen Web Components 6.35.0, and `adyen/php-api-library ^29.0.0`.

This is version-qualified repository evidence. Merchant account enablement, payment-method availability, regional eligibility, and current production configuration remain outside the snapshot.

## Checkout architecture

The plugin retrieves payment methods using merchant account, amount, currency, country, locale, channel, and shopper context, then filters and orders the response for Magento checkout. It supports cards and stored cards, wallet and alternative-payment Components, gift-card partial payments, multishipping, Pay by Link, POS Cloud, and Giving donations.

REST and GraphQL surfaces support guest and authenticated carts. They validate masked cart identifiers and ownership before exposing payment methods, submitting additional details, checking payment status, handling gift cards, or deactivating stored tokens.

## Payment lifecycle

The plugin persists `/payments` responses needed for action continuation and returns structured `/payments/details` failures. Capture, refund, and cancel requests use deterministic idempotency keys. Manual-capture orders wait for capture webhook processing before the Magento lifecycle is treated as complete; authorization alone is not fulfillment evidence.

Webhooks are validated, stored, and processed asynchronously through Magento cron. Merchants therefore need the Adyen cron group running on schedule and must retain idempotent order handling. Version 11.0.0 also adds cleanup of stale payment-response rows.

## Vaulting and recurring use

Vault flows support `CardOnFile`, `Subscription`, and `UnscheduledCardOnFile` recurring models. Token removal coordinates Magento vault state with Adyen recurring-detail disablement, while recurring-contract and token-created webhooks reconcile asynchronous changes.

These interfaces establish plugin implementation, not permission to use a stored credential for a particular merchant or transaction. The merchant must still supply the correct shopper reference, consent, recurring model, and account configuration.

## Customization and query boundary

Adyen recommends extending the plugin through documented extension points. Editing the default module can move the integration outside normal plugin support and make upgrades more difficult. Headless support covers core backend processing, authentication, and payment lifecycle; custom storefront rendering, middleware, shopper-data collection, action handling, and third-party dependencies remain merchant-owned.

The standard retained capsule is checkout-focused. For rough questions about other module areas, use the retained manifest first; detailed questions outside the assigned evidence should trigger a focused temporary clone or approved supplement.

## Related

- [[source-adyen-docs-plugins-release-notes]] — 2019–2026 captured cross-plugin release chronology; Adobe Commerce v10/v11 and separate Express/Hyvä entries provide version-specific migration and breaking-change locators, with technical minor/patch details routed to GitHub.


- [[source-adyen-docs-plugins-adobe-commerce-upgrade]] — 2026-09-15-captured default/customized `adyen/module-payment` Composer, database-upgrade and cache-flush procedure with custom-code compatibility checks; target-major prerequisites remain in the separate migration guide.


- [[source-adyen-docs-plugins-adobe-commerce-set-up-the-plugin-in-adobe-commerce-multiple-merchant-accounts]] — 2023-modified, 2026-09-15-captured Adobe Commerce website/store/store-view configuration for multiple merchant accounts; separate store views and scoped payment-method settings are described, not account funds routing.


- [[source-adyen-docs-plugins-adobe-commerce-set-up-tokenization]] — 2023-modified, 2026-09-15-captured Adobe Commerce Vault setup for shopper-selected stored methods, RECURRING_CONTRACT webhooks and recurring model/CVC options; optional risk-rule changes and non-native automatic subscriptions remain qualified.


- [[source-adyen-docs-plugins-adobe-commerce-manage-orders]] — 2023-modified, 2026-09-15-captured Commerce order capture, cancellation, refund, expiry and case-management guide distinguishing order/invoice/credit-memo status from Adyen payment and financial outcomes; cancellation webhook label differs from the setup guide.


- [[source-adyen-docs-plugins-adobe-commerce-set-up-in-person-payments]] — 2024-modified, 2026-09-15-captured Adobe Commerce Terminal API POS setup guide for separate merchant account, API/POS roles, capture delay and partial-capture remainder cancellation, terminal toggles, store/key/order timing and optional tokenization; configuration is not terminal-payment proof.


- [[source-adyen-docs-plugins-adobe-commerce-set-up-adyen-customer-area]] — 2024-modified Adobe Commerce Customer Area setup guide captured 2026-09-15: v8.4+ automated versus manual setup, credential/webhook/HMAC and capture-delay instructions, with reconfiguration-loss and v8/v9 endpoint qualifications.


- [[source-adyen-docs-plugins-adobe-commerce-customize]] — 2024-modified, 2026-09-15-captured separate-module customization guide for DI overrides, method plugins and checkout UI, with support/major-upgrade and staging-test boundaries.


- [[source-adyen-docs-plugins-adobe-commerce-go-live-checklist]] — 2023-modified, 2026-09-15-captured Adobe Commerce live-setup and real-payment test checklist, including live credentials, webhook/cron and conditional capture checks; completion and outcomes require independent evidence.


- [[source-adyen-docs-plugins-adobe-commerce-migrate-to-a-new-version]] — 2024-modified, 2026-09-15-captured v9/v10/v11 migration guide for platform/dependency, manual webhook, method/gift-card and Vault changes; v11 Commerce support wording conflicts with exact package evidence.


- [[source-adyen-docs-plugins-adobe-commerce-troubleshooting]] — Adyen Docs Adobe Commerce plugin troubleshooting guide (2023-modified, 2026-09-15 capture) for cache, logs, webhook/cron order-status diagnostics, and selected checkout errors; diagnostic guidance does not prove a fix or a payment outcome.


- [[source-adyen-docs-plugins-adobe-commerce-set-up-the-plugin-in-adobe-commerce]] — 2024-modified, 2026-09-15-captured Adobe Commerce plugin install/configuration guide for Composer/module setup, cron or queue processing, automated/manual credentials, destructive reconfiguration, capture and webhook order-status settings; no installed-package or live-outcome proof.


- [[source-adyen-docs-plugins-adobe-commerce-supported-payment-methods]] — 2024-modified, 2026-09-15-captured Adobe Commerce Standard/Headless method-country support matrix and merchant-account request route, with Trustly country and express-module qualifications; no exact package version or merchant eligibility proof.


- [[source-adyen-docs-plugins-adobe-commerce-set-up-the-payment-methods-in-adobe-commerce]] — 2025-modified, 2026-09-15-captured Adobe Commerce payment-method configuration guide for Customer Area prerequisite, card/alternative/headless/express settings, admin-order roles and Giving; configuration is not payment or capture proof.


- [[source-adyen-docs-plugins-adobe-commerce-headless-integration]] — Adyen Adobe Commerce headless PWA guide captured 2026-09-15 (metadata last modified 2024), covering REST and plugin-v8.2.0+ GraphQL checkout, shopper actions, conditional gift-card/token flows, and version-specific field/security cautions; examples do not prove a live payment.


- [[source-adyen-docs-plugins-adobe-commerce-headless-integration-express-checkout]] — 2024-modified, 2026-09-15-captured headless Adobe Commerce express-module guide for Apple Pay, Google Pay and PayPal quote/shipping/order flows, GraphQL v8.2.0+ requirement and cart-state warnings; separate from the versioned `adyen/module-payment` repository baseline.


- [[source-adyen-docs-plugins-adobe-commerce]] — 2026-09-15 Adyen Docs overview of standard versus PWA headless Adobe Commerce plugin integrations, feature/version/support tables, Checkout API/webhook flow and setup routes; major-version guidance must be checked against exact package releases.


- [[source-github-adyen-magento2]] - cumulative exact-SHA plugin evidence
- [[changelog-github-adyen-magento2]] - package-qualified release history
- [[adyen-php-api-library]] - independently versioned server dependency
- [[adyen-terminal-api]] - Terminal API and in-person payment boundary
- [[recurring-payments]] - cross-provider recurring and stored-credential concepts
- [[adyen]] - company and knowledge-status page
