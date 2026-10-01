---
title: "Braintree Recurring Billing: Subscriptions Article"
type: source
date_ingested: 2026-09-30
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/guides/recurring-billing/subscriptions"
raw_files:
  - "braintree/articles/guides/recurring-billing/subscriptions-2026-09-16.md"
tags: [braintree, recurring-billing, subscriptions, control-panel, refunds, cancellation]
---

## Overview

This collected Braintree article is the Control Panel-oriented retrieval route for creating, updating, retrying, refunding, canceling and searching subscriptions. It describes subscriptions as automatic monthly charges and preserves prerequisites and action-specific boundaries; it is distinct from the existing Node.js recurring-billing guides, dedicated request references and Subscription response reference.

## Key takeaways

- A plan must exist before a subscription can be created. The article routes creation through a customer's vaulted payment method and separately warns readers to review trial-period risks and requirements before including a trial. It says a payment method can have an unlimited number of subscriptions and that duplicate subscriptions are not covered by duplicate-transaction checking, creating an accidental-overbilling risk.
- Subscription status constrains updates. The article lists broader update categories for Pending and Active subscriptions, limits Past Due updates to subscription ID, payment method, merchant account and descriptor, and says Expired or Canceled subscriptions cannot be updated and require a new subscription instead. Exact field lists remain in the raw locators.
- For merchants operating in the EU, the article requires four weeks' notice before changing a recurring-plan price and before billing a customer after six or more months without a payment. It repeats the dormant-customer notice for a Past Due retry and links separate declined-recurring-transaction retry rules.
- Adding a new payment method to a customer's Vault record does not automatically change the customer's subscriptions. The subscription's payment method token must be updated; the article says the new card is then charged on the next billing date. A plan-price change affects future subscriptions only, so an existing subscription's price must be edited directly.
- A Past Due subscription can be retried from the Control Panel. Refunds operate on the subscription's associated sale transaction only when that transaction is `Settled` or `Settling`, and the article permits a partial refund amount.
- Canceling an Active subscription does not delete it from the Control Panel, preserving historical subscription data. Subscription search results can be downloaded as CSV, but they omit the cancellation date; the article directs merchants needing that value to enable the Subscription Canceled webhook and store its data locally.

## Detail locators

- Monthly subscription purpose: `# Subscriptions`, line 16.
- Plan prerequisite, Control Panel creation route, billing-date/cycle, add-on/discount and trial categories: `## Creating a subscription`, lines 22-41.
- Trial prerequisite and duplicate-subscription overbilling risk: `## Creating a subscription`, lines 44-49.
- EU price-change and dormant-customer notice plus status-dependent update boundary: `## Updating a subscription`, lines 55-60.
- Pending/Active, Past Due and Expired/Canceled update categories: `## Updating a subscription`, lines 63-90.
- Vault payment-method non-propagation, subscription-token update route and next-billing-date effect: `### Subscription payment method`, lines 93-111.
- Existing-subscription price non-propagation and direct-edit boundary: `### Subscription price`, lines 114-129.
- Past Due retry notice, declined-transaction route and Control Panel action: `## Retrying a Past Due subscription`, lines 132-148.
- Settled/Settling transaction and partial-refund boundary: `## Refunding a subscription`, lines 151-167.
- Active-subscription cancellation route and retained historical record: `## Canceling an Active subscription`, lines 170-184.
- Subscription CSV routes and missing cancellation-date webhook/local-storage instruction: `## Searching for subscriptions`, lines 189-197.

## Evidence limitations

> [!warning] Article, snapshot and compatibility boundary
> This article supplies Control Panel-oriented subscription actions and links to separate API and lifecycle authorities; it is not a Node.js method, request-schema or Subscription response-object specification. The collected page does not discuss Braintree Marketplace compatibility, so it does not resolve the existing conflict between recurring-billing incompatibility statements and Marketplace production guidance. Collection also does not establish current account eligibility, enablement or successful payment outcomes.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-recurring-billing]]
- Generic context: [[recurring-payments]]
- Product and status orientation: [[source-braintree-recurring-billing-overview]]
- Node.js creation and management guides: [[source-braintree-recurring-billing-create-node]], [[source-braintree-recurring-billing-manage-node]]
- Dedicated Node.js operations: [[source-braintree-subscription-create-node]], [[source-braintree-subscription-update-node]], [[source-braintree-subscription-retry-charge-node]], [[source-braintree-subscription-cancel-node]], [[source-braintree-subscription-search-node]]
- Unresolved Marketplace boundary: [[braintree-marketplace]]

## Related raw API references

- [[raw/braintree/articles/guides/recurring-billing/plans-2026-09-16|Braintree recurring-billing plans article]] - unread navigation-only route linked for the creation prerequisite
- [[raw/braintree/articles/guides/recurring-billing/billing-cycles-2026-09-16|Braintree recurring-billing cycles article]] - unread navigation-only route for billing-date and cycle details
- [[raw/braintree/articles/guides/recurring-billing/trial-periods-2026-09-16|Braintree recurring-billing trial-periods article]] - unread navigation-only route for trial risks and requirements
- [[raw/braintree/articles/guides/recurring-billing/add-ons-discounts-2026-09-16|Braintree recurring-billing add-ons and discounts article]] - unread navigation-only route for add-on and discount behavior

## Raw Sources

- [[raw/braintree/articles/guides/recurring-billing/subscriptions-2026-09-16|Braintree recurring-billing subscriptions article]] - complete collected article covering Control Panel subscription creation, status-qualified updates, payment-method and price changes, retries, refunds, cancellation and search
