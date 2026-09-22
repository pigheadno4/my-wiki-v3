---
title: "Braintree Recurring Billing Overview"
type: source
date_ingested: 2026-09-22
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/recurring-billing/overview"
raw_files:
  - "braintree/docs/guides/recurring-billing/overview-2026-09-16.md"
tags: [braintree, recurring-billing, subscriptions, vault]
---

## Overview

This Braintree guide introduces recurring billing as automatic customer charging in monthly increments and routes the setup sequence from plans and vaulted customer payment methods to subscription creation and management. It also defines the main subscription statuses and their billing significance.

## Key takeaways

- Braintree explicitly states that its recurring billing is not compatible with Braintree Marketplace. The guide does not document an alternative Marketplace subscription flow.
- Setup requires a plan created through the API or Control Panel and a customer with a payment method stored in the Vault. Subscription creation then associates the customer's preferred payment method with the plan; the guide's integration sequence is create plans, create subscriptions, and manage subscriptions.
- `Pending` means the subscription has not started, such as when its specified billing date is in the future. `Active` subscriptions are charged on the next billing date, and subscriptions in a trial period are `Active`.
- `Past Due` most commonly follows a failed subscription payment, but can also result from a balance too high to process or merchant-account setup that prevents transaction creation. For payment failures, the guide routes manual retry and Control Panel automatic-retry setup; it also describes a qualified automatic retry after the associated payment method is updated when proration is enabled. A successful retry before the final billing date returns the subscription to `Active`. After unsuccessful retries, the balance continues to increase and Braintree continues retrying each billing cycle either indefinitely or until the subscription's specified number of cycles is reached; the status remains `Past Due` until that cycle count changes it to `Expired` or the subscription is canceled.
- `Expired` means the subscription reached its specified number of billing cycles. Canceling makes the status `Canceled` and stops further billing.

## Detail locators

- Braintree Marketplace incompatibility: `# Overview > AVAILABILITY`, lines 16-17.
- Monthly recurring-billing purpose, plan and Vault prerequisites, and payment-method-to-plan association: `# Overview`, line 19.
- Required Vault preparation and the three-step integration route: `## Integration steps`, lines 22-29.
- `Pending` and `Active` meanings, including future billing dates and trial status: `## Subscription statuses > ### Pending` and `### Active`, lines 37-44.
- `Past Due` causes, manual and automatic retry routes, payment-method-update/proration condition, recovery and balance-growth behavior: `## Subscription statuses > ### Past Due`, lines 47-52.
- `Expired` and `Canceled` meanings: `## Subscription statuses > ### Expired` and `### Canceled`, lines 55-62.

## Evidence limitations

> [!warning] Availability and lifecycle boundary
> This page makes Braintree recurring billing unavailable with Braintree Marketplace and describes monthly-increment billing. It does not establish a Marketplace substitute, a complete request schema, exact retry configuration, transaction settlement finality, or behavior beyond the stated subscription-status transitions.

## Related

- Company: [[braintree]]
- Main concept: [[recurring-payments]]
- Node.js subscription creation details: [[source-braintree-subscription-create-node]]
- Node.js manual past-due retry details: [[source-braintree-subscription-retry-charge-node]]
- Node.js cancellation details: [[source-braintree-subscription-cancel-node]]

## Raw Sources

- [[raw/braintree/docs/guides/recurring-billing/overview-2026-09-16|Braintree recurring-billing overview]] - complete collected page covering availability, setup sequence and subscription-status meanings
