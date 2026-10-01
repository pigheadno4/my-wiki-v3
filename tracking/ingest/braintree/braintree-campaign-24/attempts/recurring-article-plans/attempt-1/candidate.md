---
title: "Braintree Recurring Billing Plans (Article)"
type: source
date_ingested: 2026-09-30
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/guides/recurring-billing/plans"
raw_files:
  - "braintree/articles/guides/recurring-billing/plans-2026-09-16.md"
tags: [braintree, recurring-billing, plans, subscriptions, control-panel]
---

## Overview

This collected Braintree article is the article-level route for creating, updating, and deleting recurring-billing plans in the Control Panel. It defines a plan as a subscription template that populates information such as amount, currency, and billing cycle when a new subscription is created; it is distinct from the existing Node.js plan guide and dedicated Plan API references.

## Key takeaways

- A plan must be created before subscriptions. The article's Control Panel setup route includes billing date, number of billing cycles, add-ons or discounts, and trial periods; it explicitly directs merchants adding a trial period to read the linked risks and requirements first.
- The billing cycle cannot be modified on an existing plan, although the article says other plan elements can be changed through its Control Panel update flow.
- Changes to a plan apply only to new subscriptions. Existing subscriptions are not updated automatically.
- For merchants operating in the European Union, the article requires four weeks' customer notice before changing a recurring plan's price and also before billing when at least six months have elapsed since the customer's last payment. It says those notices are not required outside the EU, while calling them good practice.
- A plan can be deleted only in the Control Panel, and deletion is unavailable when any former or current subscription is associated with the plan.

## Evidence boundaries

> [!warning] Article and implementation scopes are separate
> This article documents the Control Panel-oriented plan lifecycle and its stated constraints. Use the separate Node.js guide and dedicated Plan API references for SDK operations, request fields, response objects, and API-specific behavior; this article does not replace them.

> [!warning] Marketplace compatibility remains unresolved elsewhere
> This plans article does not state whether Braintree recurring billing is compatible with Braintree Marketplace, so it cannot resolve the conflict already routed through [[source-braintree-recurring-billing-overview]] and [[source-braintree-marketplace-guide-testing-go-live-node]]. Do not infer Marketplace compatibility from the existence of the plan workflow.

## Detail locators

- Plan prerequisite, template role, and populated information categories: `# Plans`, line 16.
- Control Panel creation steps and setup categories: `## Creating a plan`, lines 21-38.
- Trial-period risks-and-requirements warning: `## Creating a plan > **IMPORTANT**`, lines 41-42.
- Existing-plan billing-cycle restriction and Control Panel update route: `## Updating a plan`, lines 47-57.
- New-subscription-only effect and no automatic update to existing subscriptions: `## Updating a plan`, line 59.
- EU price-change and six-month-dormancy notice conditions: `## Updating a plan > **IMPORTANT**`, lines 62-63.
- Control-Panel-only deletion and former-or-current-subscription restriction: `## Deleting a plan`, lines 68-77.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-recurring-billing]]
- Generic concept: [[recurring-payments]]
- Node.js recurring-billing plan guide: [[source-braintree-recurring-billing-plans-node]]
- Node.js plan creation reference: [[source-braintree-plan-create-node]]
- Node.js plan update reference: [[source-braintree-plan-update-node]]
- Node.js plan collection reference: [[source-braintree-plan-all-node]]
- Node.js single-plan lookup reference: [[source-braintree-plan-find-node]]

## Related raw API references

- [[raw/braintree/docs/guides/recurring-billing/plans/node-2026-09-16|Braintree Node.js recurring-billing plans guide]] - unread navigation-only implementation guide; no SDK behavior is imported here
- [[raw/braintree/docs/reference/request/plan/create/node-2026-09-16|Braintree Node.js Plan Create reference]] - unread navigation-only API reference; no request or response behavior is imported here
- [[raw/braintree/docs/reference/request/plan/update/node-2026-09-16|Braintree Node.js Plan Update reference]] - unread navigation-only API reference; no request or response behavior is imported here

## Raw Sources

- [[raw/braintree/articles/guides/recurring-billing/plans-2026-09-16|Braintree recurring-billing plans article]] - complete collected article covering Control Panel plan creation, update and deletion constraints, subscription propagation, trial-risk routing, and EU notice conditions
