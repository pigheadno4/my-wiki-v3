---
title: "Braintree Recurring Billing Plans (Node.js)"
type: source
date_ingested: 2026-09-22
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/recurring-billing/plans/node"
raw_files:
  - "braintree/docs/guides/recurring-billing/plans/node-2026-09-16.md"
tags: [braintree, node-js, recurring-billing, plans, add-ons, discounts]
---

## Overview

This Braintree Node.js guide describes plans as templates that must exist before subscriptions are created. It explains how plan settings and associated add-ons or discounts flow into new subscriptions, while keeping detailed Node request shapes with the pinned raw and dedicated API references.

## Key takeaways

- A plan must be created before a subscription. The plan supplies the plan name and description, trial and billing schedule, amount and currency; subscription creation then identifies the plan with `plan_id`.
- The guide displays callback and Promise forms of Node.js plan creation, but the request inventory remains in the raw and the dedicated plan-create reference.
- Merchants operating in the European Union must give customers four weeks' notice before changing a recurring plan's price and also before billing when at least six months have passed since the customer's last payment. The guide says these notices are not required outside the EU, while calling them good practice.
- Add-ons and discounts are created in the Control Panel; the guide explicitly says they cannot be created or updated through the API. They can be applied case by case or associated with a plan so new subscriptions inherit them automatically.
- Inherited add-on or discount details can be overridden when the subscription is created or updated. The guide does not say that later plan association or modification automatically changes existing subscriptions.

## Detail locators

- Plan prerequisite, template role and populated attribute categories: `# Plans`, lines 14-26.
- Node.js callback and Promise creation examples: `# Plans > ### Callbacks` and `### Promises`, lines 28-46.
- Subscription `plan_id` requirement and EU notice qualification: `# Plans`, lines 47-49.
- Control Panel creation and API create/update boundary for add-ons and discounts: `## Add-ons and discounts`, lines 52-54.
- Case-by-case application, plan association, automatic inheritance by new subscriptions and subscription-time override route: `## Add-ons and discounts`, line 58.
- Add-on and discount field examples plus active-subscription response-array routes: `## Add-ons and discounts`, lines 60-73.
- Separate response references: `## See also`, lines 76-82.

## Evidence limitations

> [!warning] Plan and modification boundaries
> Automatic inheritance is stated for new subscriptions created from an associated plan. This guide does not establish that changing a plan or its associations changes existing subscriptions, and its API prohibition applies specifically to creating or updating add-ons and discounts rather than to plan creation itself.

## Related

- Company: [[braintree]]
- Main concept: [[recurring-payments]]
- Supporting concept: [[braintree-server-sdk]]
- Node.js plan creation details: [[source-braintree-plan-create-node]]
- Node.js plan modification details: [[source-braintree-plan-update-node]]
- Node.js add-on retrieval: [[source-braintree-add-on-all-node]]
- Node.js discount retrieval: [[source-braintree-discount-all-node]]

## Raw Sources

- [[raw/braintree/docs/guides/recurring-billing/plans/node-2026-09-16|Braintree Node.js recurring-billing plans guide]] - complete collected page covering plan templates, EU notice requirements, add-on and discount creation boundaries, inheritance and subscription-time overrides
