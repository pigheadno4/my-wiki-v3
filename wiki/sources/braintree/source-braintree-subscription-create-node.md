---
title: "Braintree Subscription Create (Node.js)"
type: source
date_ingested: 2026-09-21
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/subscription/create/node"
raw_files:
  - "braintree/docs/reference/request/subscription/create/node-2026-09-16.md"
tags: [braintree, node-js, subscriptions, recurring-billing]
---

## Overview

This Braintree Node.js reference documents creating a subscription through `gateway.subscription.create()`. It centers the vaulted-payment-method requirement and the token-versus-conditional-nonce choice, then routes readers to creation-time merchant-account, plan-modification, trial, start-date and descriptor inputs without reproducing the full parameter inventory.

## Key takeaways

- A subscription can use a payment-method token or, under certain conditions, a payment-method nonce. Braintree states that the payment method must be vaulted before it can be associated with the subscription, so the token path is usually simplest.
- Payment-method tokens do not carry 3D Secure data. To apply 3DS to the first transaction of a new subscription, the page requires creation with a 3DS-enriched payment-method nonce.
- A merchant account can be selected at creation; omitting it uses the default merchant account. A selected merchant account must use the subscription plan's currency, otherwise attempted subscription transactions trigger a validation error; using another currency requires a new plan in that currency.
- Creation can add, update or remove plan add-ons and discounts. An add-on or discount can be added to a subscription only once; use `quantity` when the same modification is to be applied several times. Detailed inheritance and override fields remain in the raw page.
- The page offers three ways to override the plan's start date: `first_billing_date`, `billing_day_of_month`, or `start_immediately`. Passing more than one produces a validation error. Trial and dynamic-descriptor examples are also routed to the raw page rather than treated as a complete input schema.

## Detail locators

- Token-versus-conditional-nonce creation and the vault prerequisite: `# Subscription: Create`, lines 15-19.
- Token 3DS limitation and the 3DS-enriched nonce requirement for the first transaction: `# Subscription: Create`, line 39, with the worked call under `## Examples > ### Create with 3D Secure enriched payment method nonce`, lines 72-93.
- Merchant-account selection, default behavior and same-currency qualification: `## Examples > ### Specify merchant account`, lines 43-70.
- Add-on and discount add/update/remove scope, inheritance, override categories and single-add qualification: `## Examples > ### Override plan details`, lines 95-307.
- Trial inputs and qualifications: `## Examples > ### Override trial details`, lines 310-343.
- Three mutually exclusive start-date inputs and examples: `## Examples > ### Set start date`, lines 346-408.
- Dynamic-descriptor examples: `## Examples > ### Dynamic descriptors`, lines 410-449.

## Evidence limitations

> [!warning] Request-detail and outcome boundary
> The examples demonstrate Node.js creation shapes but are not a complete request schema. This page does not establish a minimum SDK version, exhaustive validation behavior, or settlement and later subscription lifecycle outcomes. Use the pinned raw locators and the dedicated response, recurring-billing and validation references for those separate details.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]
- Supporting concept: [[recurring-payments]]

## Related raw API references

- [[raw/braintree/docs/reference/response/subscription/node-2026-09-16|Braintree Node.js Subscription response reference]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/guides/recurring-billing/create/node-2026-09-16|Braintree Node.js recurring-billing creation guide]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/reference/general/validation-errors/all/node-2026-09-16|Braintree Node.js validation-error reference]] - navigation only; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/reference/request/subscription/create/node-2026-09-16|Braintree Node.js subscription-create request reference]] - complete collected page covering payment-method prerequisites, token and 3DS-enriched nonce creation paths, merchant-account currency, plan modifications, trials, start dates and descriptors
