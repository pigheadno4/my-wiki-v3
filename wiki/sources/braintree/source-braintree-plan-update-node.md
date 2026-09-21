---
title: "Braintree Plan Update (Node.js)"
type: source
date_ingested: 2026-09-20
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/plan/update/node"
raw_files:
  - "braintree/docs/reference/request/plan/update/node-2026-09-16.md"
tags: [braintree, node-js, plans, recurring-billing, add-ons, discounts]
---

## Overview

This Braintree Node.js reference documents updating a plan by ID through `gateway.plan.update()` in callback and Promise forms. It covers plan attributes, associated add-on and discount changes, and a trial-period update effect; it does not establish whether plan changes propagate to existing subscriptions.

## Key takeaways

- If the requested plan cannot be found, the page says the operation returns a `notFoundError`.
- When a plan already has add-ons or discounts, the page warns that modification tokens must be passed during an update; otherwise all modifications associated with that plan are removed after the update.
- As an alternative to modification tokens, the update can add, update, and remove associated add-ons or discounts, including multiple changes in one request. The prose uses names such as `add_ons`, `inherited_from_id`, and `existing_id`, while the displayed Node examples use `addOns`, `inheritedFromId`, and `existingId`.
- For added modifications, details are inherited from the referenced add-on or discount; for updated modifications, details are inherited from the existing associated item. The page provides a short, explicit override-field list at the locator below rather than establishing arbitrary override support.
- The page says that passing `trial_period` removes the plan's billing day of month; its Node examples express that input as `trialPeriod`. It does not document units, validation, or effects on existing subscriptions.

## Detail locators

- Plan-ID update invocation, update attributes, and callback form: `# Plan: Update > ### Callback`, lines 16-28.
- Promise form: `# Plan: Update > ### Promise`, lines 30-41.
- Missing-plan error route: `# Plan: Update`, line 42.
- Modification-token approach and destructive omission warning: `### Add-ons and discounts`, lines 43-80.
- Add, update, and remove examples for add-ons and discounts: `### Add-ons and discounts`, lines 82-146.
- Multiple add-on or discount changes in one update: `### Multiple updates`, lines 148-199.
- Inheritance behavior and the allowed override-field list: `### Override details`, lines 201-288.
- Trial-period update effect and callback/Promise examples: `### Update trail period`, lines 290-311.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]

## Raw Sources

- [[raw/braintree/docs/reference/request/plan/update/node-2026-09-16|Braintree Node.js plan-update request reference]] - complete collected page covering plan-ID updates, missing-plan handling, add-on and discount modification paths, override details, and the trial-period update effect
