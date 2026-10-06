---
title: "Braintree JavaScript v2 PayPal Client Reference"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/client-reference/javascript/v2/paypal"
raw_files:
  - "braintree/docs/reference/client-reference/javascript/v2/paypal-2026-09-16.md"
tags: [braintree, paypal, javascript-v2, client-reference, checkout, vault]
---

## Overview

This 2026-09-16 website snapshot is the Braintree.js JavaScript v2 client reference for PayPal options used by Vault and Checkout with PayPal integrations. It documents browser-side configuration, presentation and callback output; it does not itself establish current SDK support, Sandbox or Production availability, merchant enablement, server-side transaction processing, or successful payment execution.

## Key takeaways

- Custom and Drop-in setups must nest this configuration under a `paypal` object. `singleUse` defaults to `false`; setting it to `true` triggers the Checkout flow. For Checkout, `amount` and `currency` are required, and the `intent` option is documented only for v2.25.0 and later.
- The reference distinguishes an `authorize` intent, which submits a transaction for authorization but not settlement, from `sale`, which submits it for settlement when a transaction is created. A PayPal authentication callback or generated nonce is therefore not by itself proof of authorization, capture or settlement.
- `onSuccess` is deprecated and represents successful PayPal login rather than form submission; it is not fired for Drop-in. `onAuthorizationDismissed` is documented for v2.18.0 and later and is also unavailable in Drop-in.
- Billing-address retrieval requires both `enableBillingAddress` and the PayPal Billing Address Request feature on the merchant's PayPal account; the page says the feature is not available to all merchants. Shipping-address fields and overrides are separate client options.
- With `headless: true`, the integration supplies its own launch UI, Braintree's normal PayPal button and resolution state are not displayed, and the generated nonce must be read from `onPaymentMethodReceived`; this mode does not work with Drop-in. Linked examples and guides are navigation, not captured or executed proof.

## Detail locators

- `Options` lines 17-22: Vault/Checkout scope and custom-or-Drop-in nesting requirement.
- `Options` lines 24-40: button container, nonce input field and display name.
- `Options` lines 41-83: `singleUse`, version-qualified `intent`, authorization-versus-settlement wording and callback boundaries.
- `Options` lines 85-166: returned shipping-address fields and shipping-address override fields/editability.
- `Options` lines 167-204: billing-address feature, merchant-eligibility qualification and returned fields.
- `Options` lines 205-264: Checkout amount/currency requirements and version-qualified locale inventory.
- `Options` lines 265-281: headless/custom-UI behavior, nonce callback requirement, Drop-in exclusion and version-qualified billing-agreement description.

## Related

- Company: [[braintree]]
- Concept: [[braintree-web-sdk]]

## Raw Sources

- [[raw/braintree/docs/reference/client-reference/javascript/v2/paypal-2026-09-16|Braintree JavaScript v2 PayPal client reference snapshot (2026-09-16)]]
