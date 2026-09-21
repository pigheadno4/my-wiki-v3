---
title: "Braintree Subscription Cancel (Node.js)"
type: source
date_ingested: 2026-09-20
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/subscription/cancel/node"
raw_files:
  - "braintree/docs/reference/request/subscription/cancel/node-2026-09-16.md"
tags: [braintree, node-js, subscriptions, recurring-billing, cancellation]
---

## Overview

This Braintree Node.js reference documents `gateway.subscription.cancel()` for canceling a subscription by ID. The page presents cancellation as the way to stop billing a credit card for that subscription and provides callback and Promise invocation forms.

## Key takeaways

- Call `gateway.subscription.cancel()` with the subscription ID, using either the callback or Promise form.
- If the subscription cannot be found, the API returns Braintree's Node.js `notFoundError`.
- A canceled subscription cannot be edited or reactivated; the page directs merchants to create a new subscription instead.

> [!warning] Cancellation boundary
> This page states that cancellation stops billing a credit card and that the canceled subscription cannot be edited or reactivated. It does not state when cancellation takes effect or define refunds, proration, paid-term forfeiture, customer deletion, or payment-method deletion.

## Detail locators

- Billing effect: `# Subscription: Cancel`, line 15.
- Callback and Promise invocation forms: `# Subscription: Cancel > ### Callback` and `### Promise`, lines 16-25.
- Missing-subscription error and the edit/reactivation limit: `# Subscription: Cancel`, lines 27-29.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]

## Raw Sources

- [[raw/braintree/docs/reference/request/subscription/cancel/node-2026-09-16|Braintree Node.js subscription-cancel reference]] - complete page covering the billing effect, callback and Promise forms, missing-subscription error, and edit/reactivation limit
