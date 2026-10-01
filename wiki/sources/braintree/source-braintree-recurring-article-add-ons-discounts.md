---
title: "Braintree Recurring Billing Add-ons and Discounts"
type: source
date_ingested: 2026-09-30
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/guides/recurring-billing/add-ons-discounts"
raw_files:
  - "braintree/articles/guides/recurring-billing/add-ons-discounts-2026-09-16.md"
tags: [braintree, recurring-billing, subscriptions, add-ons, discounts, control-panel]
---

## Overview

This Braintree article explains how add-ons and discounts change a specific customer's subscription price without changing the base plan price. It is an article-level behavior and administration route, distinct from the Node.js recurring-billing guides and the dedicated Plan or Subscription API references.

## Key takeaways

- Add-ons charge for additional features or services, while discounts reduce a subscription price for a promotion or price break; both modify a specific customer's price without changing the base plan.
- They can be applied manually to individual subscriptions or associated with a plan so that they apply automatically to new subscriptions.
- Add-ons and discounts must be created and deleted in the Control Panel. The API can view existing items and add them to a subscription, either unchanged or with modifications.
- When an add-on or discount is added to a new or existing subscription, its billing-cycle count, amount, and quantity can be overridden. An item associated with a subscription cannot be deleted from the Control Panel.

## Evidence boundaries

> [!warning] Control Panel and API responsibilities
> An add-on or discount must be created in the Control Panel before it can be associated with a subscription or plan. The article limits the API to viewing existing items and applying them to subscriptions, and it says an item associated with a subscription cannot be deleted from the Control Panel.

> [!info] Documentation scope
> This article establishes product behavior and administration boundaries. Use the separate Node.js guides and API references for implementation methods, request fields, and response shapes.

## Detail locators

- Add-on and discount purpose, specific-customer price effect, and manual versus plan-associated application: `# Add-ons and Discounts`, lines 14-18.
- Control Panel creation/deletion and API view/application boundary: `## Creating an add-on or discount`, lines 21-29.
- Control Panel navigation and creation steps: `## Creating an add-on or discount`, lines 32-37.
- Overridable billing cycles, amount and quantity, plus the associated-subscription deletion restriction: `## Creating an add-on or discount`, lines 39-48.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-recurring-billing]]
- Cross-provider context: [[recurring-payments]]

## Raw Sources

- [[raw/braintree/articles/guides/recurring-billing/add-ons-discounts-2026-09-16|Braintree Add-ons and Discounts]] - complete collected article covering subscription-price modifiers, application choices, administration boundaries and deletion limits
