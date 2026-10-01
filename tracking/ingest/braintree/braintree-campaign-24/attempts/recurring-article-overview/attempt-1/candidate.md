---
title: "Braintree Recurring Billing Overview (Article)"
type: source
date_ingested: 2026-09-30
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/guides/recurring-billing/overview"
raw_files:
  - "braintree/articles/guides/recurring-billing/overview-2026-09-16.md"
tags: [braintree, recurring-billing, subscriptions, plans, vault]
---

## Overview

This collected Braintree article is the article-level orientation to recurring billing: automatic customer charging in monthly increments, the plan and Vault prerequisites, and the roles of plans, customers, and subscriptions. It is distinct from the existing developer-guide overview, which owns availability and subscription-status guidance, and from Node.js guides and API request or response references.

## Key takeaways

- Setting up recurring billing requires a plan created in the Control Panel or through the API and customers stored in the Vault. A subscription then associates a customer's preferred payment method with a plan.
- Plans define the billing-cycle length, billing date, default cost, and number of cycles before expiration, and they can represent different services.
- Customers include a payment method, can include personal details such as address or email, and can be linked to multiple subscriptions.
- A subscription is funded by a specific payment method and can have elements that differ from its original plan.

## Evidence boundaries

> [!warning] Article orientation is not implementation or lifecycle authority
> This article does not define subscription statuses, retries, SDK methods, request schemas, or response objects. Use the existing developer-guide overview and dedicated Node.js sources for those topics. The article also does not discuss Braintree Marketplace compatibility, so it cannot establish support or resolve the existing compatibility conflict.

## Detail locators

- Monthly recurring-billing scope and the plan, Vault, payment-method and subscription setup sequence: `# Overview`, line 16.
- Three required elements: `# Overview`, line 18.
- Plan role and configuration categories: `#### Plans`, lines 21-26.
- Customer role, payment method, optional personal details and multiple-subscription relationship: `#### Customers`, lines 29-34.
- Subscription funding and flexibility relative to the original plan: `#### Subscriptions`, lines 37-41.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-recurring-billing]]
- Generic concept: [[recurring-payments]]
- Separate developer-guide overview and status route: [[source-braintree-recurring-billing-overview]]
- Article-level plan route: [[source-braintree-recurring-article-plans]]
- Article-level subscription-administration route: [[source-braintree-recurring-article-subscriptions]]
- Separate Node.js creation guide: [[source-braintree-recurring-billing-create-node]]

## Related raw API references

- [[raw/braintree/articles/guides/recurring-billing/plans-2026-09-16|Braintree recurring-billing plans article]] - unread navigation-only route for plan setup and constraints
- [[raw/braintree/docs/guides/recurring-billing/plans/node-2026-09-16|Braintree Node.js recurring-billing plans guide]] - unread navigation-only implementation route
- [[raw/braintree/articles/control-panel/vault/create-2026-09-16|Braintree Control Panel Vault customer-creation article]] - unread navigation-only route for storing customers and payment methods
- [[raw/braintree/articles/guides/recurring-billing/subscriptions-2026-09-16|Braintree recurring-billing subscriptions article]] - unread navigation-only route for subscription administration

## Raw Sources

- [[raw/braintree/articles/guides/recurring-billing/overview-2026-09-16|Braintree recurring-billing overview article]] - complete collected article covering monthly scope, plan and Vault prerequisites, and the roles of plans, customers, and subscriptions
