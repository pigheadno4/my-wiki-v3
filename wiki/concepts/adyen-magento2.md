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

- [[source-github-adyen-magento2]] - cumulative exact-SHA plugin evidence
- [[changelog-github-adyen-magento2]] - package-qualified release history
- [[adyen-php-api-library]] - independently versioned server dependency
- [[adyen-terminal-api]] - Terminal API and in-person payment boundary
- [[recurring-payments]] - cross-provider recurring and stored-credential concepts
- [[adyen]] - company and knowledge-status page
