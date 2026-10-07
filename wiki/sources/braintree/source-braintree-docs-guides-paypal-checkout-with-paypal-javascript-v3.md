---
title: "Braintree PayPal One-time Payments - JavaScript v3"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/paypal/checkout-with-paypal/javascript/v3"
raw_files:
  - "braintree/docs/guides/paypal/checkout-with-paypal/javascript/v3-2026-09-16.md"
tags: [braintree, paypal, one-time-payments, checkout, javascript-v3]
---

## Overview

This collected [[braintree]] guide is the JavaScript v3 website route for a one-time PayPal Checkout flow through Braintree. It covers creating the client-side payment resource, tokenizing buyer approval into a Braintree payment-method nonce, and handing that nonce to a merchant server for `Transaction.sale`. It is not a vaulted-payment flow, a direct PayPal Orders API integration, or evidence that approval, tokenization or a sale request produced a successful payment outcome.

The page is a 2026-09-16 snapshot. Its JavaScript SDK minimum, country, currency, customization and environment statements are page-scoped evidence, not proof of current support, merchant enablement, buyer eligibility or production availability. Exact implementation behavior for separately retained package versions remains independent.

## Key takeaways

- The guide defines One-time Payments as a checkout flow that does not store the customer's PayPal account in the Braintree Vault. It names cart/product-page checkout and checkout-page replacement as typical uses, and records address/funding-instrument selection plus country-qualified two-factor-authentication support.
- The examples require Braintree JavaScript SDK `3.90.0` or higher. The page separately directs integrations using that SDK with the deprecated PayPal `checkout.js` library to its migration guide; this collected route does not itself prove current SDK lifecycle status or the behavior of PayPal Web SDK v6.
- To request the payment resource, the guide sets `flow` to `checkout` and supplies amount and currency to `createPayment`. Currency must match `loadPayPalSDK`, and intent, when used, must match in both calls. The callback and Promise blocks are alternative examples rather than additional required flows.
- After buyer consent, `tokenizePayment` returns a payment-method nonce on successful tokenization. The merchant sends that nonce to its server and uses a Braintree server SDK to call `Transaction.sale`. Approval, a nonce and the server request are distinct stages; none alone proves authorization, capture, settlement or funding.
- The page also routes optional contact, shipping, line-item, buyer-identifier and Pay Now/Continue behaviors. The Contact Module is stated to be US-only. Server-side shipping callbacks require callback-domain registration in both Sandbox and Production. `COMMIT` maps to Pay Now on the PayPal review page, whereas `CONTINUE` returns the payer to the merchant site to complete the transaction. Keep the detailed settings, examples and domain rules in the raw locators.

> [!warning] Client approval is not a payment outcome
> A successful consent and tokenization step yields a Braintree payment-method nonce for server submission. It does not itself establish that `Transaction.sale` was accepted or that a payment was authorized, captured, submitted for settlement, settled or funded.

> [!warning] Preserve flow and version boundaries
> This is a JavaScript v3 Braintree website guide for the non-vault one-time flow. Do not transfer its examples to Checkout with Vault, the separate PayPal Checkout v6 adapter, a direct PayPal Orders API flow, another SDK version or a current production-support claim.

## Detail locators

- One-time-payment identity, non-vault distinction, named support and typical placements: `# One-time Payments`, raw lines 14-33.
- JavaScript SDK minimum and deprecated `checkout.js` migration notice: `## Invoking the One-time Payments flow`, raw lines 36-42.
- `flow`, amount, currency and intent matching conditions: `## Invoking the One-time Payments flow`, raw lines 48-52; callback example at raw lines 55-107 and Promise example at raw lines 109-166.
- Approval tokenization, returned nonce and server-side `Transaction.sale` handoff: raw lines 167-171.
- Contact preferences, field behavior, example and US-only statement: `### Integrating Contact Module`, raw lines 186-231.
- Shipping callbacks, buyer changes, callback-domain registration in both environments and exact domain-name rules: `### Integrating Shipping Module`, raw lines 234-347.
- Line-item display locations and example field constraints: `### Integrating Pass Line-item Details`, raw lines 352-380.
- Buyer-identifier example: `### Integrating Pass Buyer Identifier`, raw lines 382-392.
- Pay Now/Continue semantics and `COMMIT`/`CONTINUE` values: `### Integrating Pay Now or Continue`, raw lines 395-433.
- Conditional shipping-address collection and server-side sale-call route: `## Shipping address`, raw lines 438-440.
- Snapshot country and currency statements plus linked support routes: `## Country support` through `## Currency presentment`, raw lines 443-452.

## Related

- Company: [[braintree]]
- Main integration concept: [[paypal-braintree-integration]]
- Browser SDK concept: [[braintree-web-sdk]]
- Distinct vault route: [[source-braintree-paypal-checkout-with-vault-javascript-v3]]

## Related raw API references

- [[raw/braintree/docs/guides/paypal/paypal-sdk-migration-guide/javascript/v3-2026-09-16|Braintree PayPal SDK migration guide - JavaScript v3]] - navigation-only route named for deprecated `checkout.js` integrations; not read as behavioral or current-support evidence here
- [[raw/braintree/docs/guides/paypal/server-side/node-2026-09-16|Braintree PayPal server-side guide - Node.js]] - navigation-only route for server processing and currency details; no transaction outcome is inferred here

## Raw Sources

- [[raw/braintree/docs/guides/paypal/checkout-with-paypal/javascript/v3-2026-09-16|Braintree PayPal One-time Payments - JavaScript v3]] - complete collected guide covering the client payment-resource request, approval tokenization, nonce-to-server handoff and optional checkout modules
