---
title: "Braintree PayPal checkout.js to PayPal JS SDK Migration - JavaScript v3"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/paypal/paypal-sdk-migration-guide/javascript/v3"
raw_files:
  - "braintree/docs/guides/paypal/paypal-sdk-migration-guide/javascript/v3-2026-09-16.md"
tags: [braintree, paypal, javascript-v3, migration, checkout-js]
---

## Overview

This collected [[braintree]] website guide documents the migration of a JavaScript v3 custom PayPal integration from PayPal `checkout.js` (identified by the page as PayPal JavaScript SDK version 4) to the PayPal JS SDK (identified as version 5). The older integration is described as still supported in this snapshot; the page is an old-to-new integration map, not a deprecation notice or proof of current support.

The route applies only to Braintree JavaScript v3 custom PayPal integrations. It explicitly excludes Drop-in UI, JavaScript v2, Android, iOS and new PayPal web integrations. It does not establish behavior for direct PayPal integrations, PayPal Web SDK v6, current hosted runtime behavior, merchant eligibility, or any separately retained package version.

## Key takeaways

- The loader changes from a separately included `checkout.js` script to either `paypalCheckoutInstance.loadPayPalSDK()` or a directly loaded PayPal JS SDK script. When loading the script directly, the page says the PayPal client ID comes from the Braintree Control Panel and differs between Sandbox and Production; configuration and query-parameter examples remain in the raw locators.
- Button rendering changes from `paypal.Button.render(config, selector)` to `paypal.Buttons(config).render(selector)`. To request only a PayPal button, the new configuration uses `fundingSource: paypal.FUNDING.PAYPAL`; otherwise the guide says the integration tries to render all eligible payment methods.
- The old `payment` callback maps to `createOrder` for Checkout or `createBillingAgreement` for Vault, while the Braintree adapter continues to call `createPayment` inside those callbacks. The old `onAuthorize` callback is renamed `onApprove`, which still calls `tokenizePayment`; `onCancel` and `onError` are described as unchanged.
- The environment no longer needs to be passed in button configuration because it is derived from the PayPal client ID. This is a page-scoped migration statement, not evidence that any supplied client ID, account or environment is valid.
- Checkout versus Vault can no longer be chosen dynamically at payment time in the migrated pattern: the guide says the choice must be made while setting up the SDK. Checkout uses `createOrder`; Vault passes `vault: true` to `loadPayPalSDK` and uses `createBillingAgreement`.

> [!warning] Preserve the old/new version boundary
> This snapshot maps PayPal `checkout.js` v4 to PayPal JS SDK v5 inside a Braintree JavaScript v3 custom integration. Do not reinterpret it as a migration to PayPal Web SDK v6, a Braintree JavaScript v2 migration, a Drop-in procedure, a native SDK guide, a direct PayPal Orders API integration, or current package-support evidence.

> [!warning] Setup-time flow selection is consequential
> In the migrated pattern, Checkout and Vault use different SDK setup and callback names. Preserve the `vault: true` plus `createBillingAgreement` condition for Vault and the `createOrder` mapping for Checkout; do not combine the two example flows.

## Detail locators

- Scope and explicit exclusions: availability notice and list at raw lines 17-26.
- `checkout.js` v4 versus PayPal JS SDK v5 identity and the statement that the older integration remained supported: raw lines 30-32.
- Separate-script old pattern, `loadPayPalSDK` new pattern, callback/Promise alternatives and configuration-object examples: `## Script tag`, raw lines 35-120.
- Direct script-loading alternative, Braintree Control Panel client-ID route, Sandbox/Production distinction and query-parameter navigation: raw lines 122-138.
- `paypal.Button.render` to `paypal.Buttons(...).render(...)` mapping: `### How to initialize the PayPal SDK`, raw lines 144-163.
- PayPal-only funding-source setting, default eligible-method rendering statement and style example: `### How to render a PayPal button`, raw lines 165-197.
- `payment` to `createOrder` or `createBillingAgreement` mappings and separate Checkout/Vault examples: `### Creating a payment resource`, raw lines 199-243.
- `onAuthorize` to `onApprove` mapping and tokenization examples: `### Tokenizing the PayPal account`, raw lines 245-302.
- Unchanged cancellation/error callbacks and removal of explicit `env`: `### Other considerations`, raw lines 304-308.
- Setup-time Checkout/Vault selection, `vault: true` condition and callback names: `## Checkout flow vs Vault flow`, raw lines 311-315.
- End-to-end old and new Checkout examples, including the example-only currency/intent matching comments: `### Checkout flow`, raw lines 318-464.
- Vault requirement and callback/Promise examples: `### Vault flow`, raw lines 466-537.

## Related

- Company: [[braintree]]
- Main integration concept: [[paypal-braintree-integration]]
- Browser SDK concept: [[braintree-web-sdk]]
- Distinct one-time checkout route: [[source-braintree-docs-guides-paypal-checkout-with-paypal-javascript-v3]]
- Distinct Checkout-with-Vault route: [[source-braintree-paypal-checkout-with-vault-javascript-v3]]
- Distinct Braintree JavaScript v2-to-v3 migration: [[source-braintree-client-sdk-migration-javascript-v3]]

## Raw Sources

- [[raw/braintree/docs/guides/paypal/paypal-sdk-migration-guide/javascript/v3-2026-09-16|Braintree PayPal checkout.js to PayPal JS SDK migration - JavaScript v3]] - complete collected old/new migration guide for Braintree custom PayPal integrations
