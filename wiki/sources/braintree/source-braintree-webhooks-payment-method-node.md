---
title: "Braintree Payment Method Webhooks (Node.js)"
type: source
date_ingested: 2026-09-20
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/general/webhooks/payment-method/node"
raw_files:
  - "braintree/docs/reference/general/webhooks/payment-method/node-2026-09-16.md"
tags: [braintree, node-js, webhooks, payment-methods, paypal, venmo]
---

## Overview

This Braintree Node.js reference documents payment-method webhook notification kinds and routes to their payload attributes. Its currently documented triggers are specific to PayPal billing-agreement cancellation and named Venmo revocation or customer-data events; it does not establish notification coverage for every stored payment method.

## Key takeaways

- The notification object's `kind` identifies what triggered a payment-method webhook. This page lists `payment_method_revoked_by_customer` and `payment_method_customer_data_updated`.
- `payment_method_revoked_by_customer` concerns a previously enabled payment instrument revoked by the customer or by Venmo. The page says this webhook is currently sent only when a customer cancels a PayPal billing agreement, removes a Venmo connection, or Venmo suspends the account because of suspicious activity on the customer's Venmo account.
- `payment_method_customer_data_updated` reports updated customer data on a payment method. The only trigger currently stated is a customer updating Enriched Customer Data in Venmo, provided the merchant has enabled that feature.

> [!warning] Current payment-method scope
> Both trigger descriptions are explicitly qualified as current and are PayPal- or Venmo-specific. Do not generalize this reference into webhook coverage for all payment instruments or all customer-data changes.

## Detail locators

- Notification-kind meaning and trigger table: `# Payment Method` > `### Notification kinds`, lines 17-24.
- Revocation triggers and current PayPal/Venmo scope: notification table row `payment_method_revoked_by_customer`, line 23.
- Customer-data update trigger and merchant-enablement condition: notification table row `payment_method_customer_data_updated`, line 24.
- Payload routes, including kind and trigger time, Vault payment-method/customer references, the revoked `PaymentMethod`, and updated-customer-data structures: `# Payment Method` > `### Attributes`, lines 27-29.

## Related

- Company: [[braintree]]
- Concept: [[braintree-webhooks]]
- Related source: [[source-braintree-webhooks-overview]]

## Raw Sources

- [[raw/braintree/docs/reference/general/webhooks/payment-method/node-2026-09-16|Braintree Node.js payment-method webhook reference]] - complete page covering notification kinds, currently documented PayPal/Venmo triggers, and payload-attribute routes
