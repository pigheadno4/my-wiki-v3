---
title: "Adyen Shopify"
type: concept
category: technology
tags: [adyen, shopify, plugin, ecommerce]
---

## Definition

Adyen's Shopify route uses separate Credit Cards and Alternative Payments apps. The 2025-modified installation guide, captured 2026-09-15, requires Shopify Checkout Extensibility and a Credit Cards app setup before Alternative Payments. It provides configuration and test/live transition steps, not evidence of merchant enablement or a completed payment. [[source-adyen-docs-plugins-shopify]]

## Integration boundary

The Shopify-specific guide owns account connection, one-merchant-account-per-region selection, method setup/sync, test mode and live-account transition. Supported methods depend on the separately linked list and merchant-account setup; the guide does not define a universal country/currency matrix, package version, capture flow, or order-outcome guarantee.

## Sources

- [[source-adyen-docs-plugins-shopify-supported-payment-methods]] — 2024-modified, 2026-09-15-captured Shopify plugin method/region table for an unnumbered “latest version,” with qualified Trustly coverage and no currency, merchant-enablement or payment-outcome proof.


- [[source-adyen-docs-plugins-shopify]] — 2025-modified, 2026-09-15-captured Shopify app installation, method setup, testing and live-account transition guide.

## Related

- [[adyen-online-payments]]
- [[adyen]]
