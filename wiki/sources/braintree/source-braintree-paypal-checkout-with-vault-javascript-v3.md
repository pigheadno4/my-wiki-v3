---
title: "Braintree PayPal Checkout with Vault - JavaScript v3"
type: source
date_ingested: 2026-09-29
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/paypal/checkout-with-vault/javascript/v3"
raw_files:
  - "braintree/docs/guides/paypal/checkout-with-vault/javascript/v3-2026-09-16.md"
tags: [braintree, paypal, checkout-with-vault, javascript-v3, billing-agreements]
---

## Overview

This Braintree guide is the JavaScript v3 route for Checkout with Vault: a one-time PayPal Checkout experience that also creates a Billing Agreement and stores the customer's PayPal account in the Braintree Vault for possible future charges. It distinguishes the initial checkout-and-vault flow from returning-customer payment-method selection and from ordinary one-time PayPal Checkout; it is not evidence for another SDK version or a direct PayPal Orders API integration.

## Key takeaways

- The initial JavaScript v3 flow combines a one-time checkout with customer authorization to store the PayPal wallet. The guide describes the value as reduced friction on a repeat purchase, while the initial and future-payment credentials remain distinct.
- The initial `createPayment` request uses `flow: checkout`, `requestBillingAgreement: true`, amount and currency. Currency must match the value passed to `loadPayPalSDK`; if intent is used, it must also match between `loadPayPalSDK` and `createPayment`.
- After customer consent, successful client-side tokenization returns a single-use payment-method token. The merchant sends that token to its server for `Transaction.sale`; the result contains a PayPal details object with an `implicitlyVaultedPaymentMethodToken` property, which the merchant can then associate with its Braintree customer for future transactions. Tokenization alone is not a completed transaction or the customer association step.
- For returning customers who already have a vaulted PayPal Billing Agreement, the guide directs merchants to use the One-time Payments flow rather than Checkout with Vault, initialize with a client token generated for that customer ID, and enable `autoSetDataUserIdToken`.
- When integrating Pay Later, the guide makes the returning-customer step mandatory so a buyer can choose a Pay Later offer, requires a separate Pay Later button in addition to the PayPal button, and directs merchants to obtain enablement through their PayPal account manager or Braintree contact route.

## Evidence boundaries

> [!warning] One-time token versus vaulted token
> The payment-method token returned by client-side approval is single-use and is sent to `Transaction.sale`. The distinct `implicitlyVaultedPaymentMethodToken` comes from the sale result and can then be associated with the customer; do not describe approval tokenization alone as completing that server-side association.

> [!warning] Initial versus returning-customer flow
> The initial Checkout with Vault request creates the one-time checkout plus vault consent. The returning-customer section instead says to use the One-time Payments flow with a customer-scoped client token for an existing vaulted Billing Agreement. Preserve that switch rather than repeatedly invoking Checkout with Vault.

> [!warning] Version and linked-reference scope
> These instructions are explicitly JavaScript v3. Treat the page's linked references as navigation routes, not proof of another SDK version's current behavior.

## Detail locators

- Checkout-with-vault identity, stored-wallet purpose and named capabilities: `# Checkout with Vault`, lines 14-35.
- Initial request settings and currency/intent matching conditions: `## Invoking the Checkout with Vault flow`, line 40.
- Shipping-change handling and `updatePayment` replacement for `actions.order.patch`: `## Invoking the Checkout with Vault flow`, line 51.
- Client approval tokenization and the returned single-use token: `## Invoking the Checkout with Vault flow`, line 54.
- Server `Transaction.sale`, `implicitlyVaultedPaymentMethodToken` and customer association: `## Invoking the Checkout with Vault flow`, line 57.
- Pay Later returning-customer requirement, separate button and enablement route: `## Returning customer`, lines 62-68.
- Returning-buyer funding-instrument choice and exact initialization steps: `## Returning customer`, lines 72-82.
- Merchant/customer country statement and the page's locale-reference route: `## Country support`, lines 85-87.
- Presentment and server-side currency navigation: `## Currency presentment`, lines 90-94.

## Related

- Company: [[braintree]]
- Main integration concept: [[paypal-braintree-integration]]
- SDK concept: [[braintree-web-sdk]]
- Vault concept: [[paypal-vault]]

## Related raw API references

- [[raw/braintree/docs/guides/paypal/checkout-with-paypal/javascript/v3-2026-09-16|Braintree PayPal One-time Payments - JavaScript v3]] - unread navigation-only route named by the returning-customer instructions; no sibling behavior is inferred here
- [[raw/braintree/docs/guides/paypal/pay-later-offers/javascript/v3-2026-09-16|Braintree PayPal Pay Later Offers - JavaScript v3]] - unread navigation-only route for the separate Pay Later integration; no offer terms or setup behavior are inferred here

## Raw Sources

- [[raw/braintree/docs/guides/paypal/checkout-with-vault/javascript/v3-2026-09-16|Braintree PayPal Checkout with Vault - JavaScript v3]] - complete collected guide covering the initial checkout-and-vault request, client/server token handoff and returning-customer path
