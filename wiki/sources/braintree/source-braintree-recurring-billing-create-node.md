---
title: "Braintree Recurring Billing Create (Node.js)"
type: source
date_ingested: 2026-09-22
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/recurring-billing/create/node"
raw_files:
  - "braintree/docs/guides/recurring-billing/create/node-2026-09-16.md"
tags: [braintree, node-js, recurring-billing, subscriptions]
---

## Overview

This Braintree Node.js guide explains how subscription creation combines a stored payment method with a plan, and how the plan supplies pricing, trial, billing, add-on and discount details unless selected details are overridden. It also distinguishes creation and initial-charge behavior for subscriptions that bill immediately, begin on a future billing date, or include a trial.

## Key takeaways

- The basic inputs are a stored `payment_method_token` and a `plan_id`; the subscription inherits the plan's price, trial duration, billing details, add-ons and discounts. A payment-method nonce is available only under the guide's linked conditions, and the payment method must already be vaulted before association with the subscription.
- Payment-method tokens carry no 3D Secure data. When 3DS must apply to the first transaction, the guide requires creating the subscription with a 3DS-enriched payment-method nonce.
- With multiple merchant accounts, creation can select an account or use the default. The selected account must use the plan's currency; otherwise attempted subscription transactions trigger a validation error, and a different currency requires a new plan.
- Selected plan details can be overridden during creation; the exact override categories and examples remain in the pinned raw under `## Overriding plan details`.
- Without a trial, immediate billing attempts the charge and submits the transaction for settlement right away; the subscription is created as `Active` only after a successful attempt, while a failed attempt creates no subscription. A future-billing subscription is created immediately as `Pending`, then becomes `Active` or `Past Due` according to the first billing-date charge attempt. A trial subscription is created as `Active`, with the charge attempted at trial end and failure changing it to `Past Due`.
- Subscription days run midnight to midnight in the gateway account's time zone, regardless of creation time. Braintree separately directs merchants to read its trial-period risks and requirements before configuring trials.

## Detail locators

- Stored token and plan prerequisites, inherited plan details, conditional nonce route and vault prerequisite: `# Create Subscriptions`, lines 14-20.
- First-transaction 3DS requirement: `# Create Subscriptions`, line 40.
- Merchant-account selection, defaulting and plan-currency warning: `## Specifying merchant account`, lines 41-47.
- Plan-detail override categories and worked examples: `## Overriding plan details`, lines 72-84.
- Immediate, future-date and trial transaction flows: `## Transaction flow`, lines 87-121.
- Trial risk route and full status-flow diagram route: `## Transaction flow`, lines 124-127.
- Gateway-time-zone definition of a subscription day: `## Subscription days`, lines 128-130.
- Optional recurring-billing email setup and enablement route: `## Email notifications`, lines 131-133.

## Evidence limitations

> [!warning] Settlement submission is not settlement completion
> For immediate billing, the guide says Braintree attempts the charge and submits the transaction for settlement right away. It does not say that settlement completes immediately. Detailed request fields, validation behavior, status definitions, trial requirements and later lifecycle behavior remain with the linked references or the pinned raw.

## Related

- Company: [[braintree]]
- Main concept: [[recurring-payments]]
- Supporting concept: [[braintree-server-sdk]]
- Dedicated Node.js request reference: [[source-braintree-subscription-create-node]]

## Raw Sources

- [[raw/braintree/docs/guides/recurring-billing/create/node-2026-09-16|Braintree Node.js recurring-billing creation guide]] - complete collected page covering prerequisites, inherited and overridden plan details, merchant-account currency, initial transaction flows, subscription-day timing and optional notifications
