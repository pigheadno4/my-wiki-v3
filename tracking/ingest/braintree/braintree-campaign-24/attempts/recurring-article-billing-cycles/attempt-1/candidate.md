---
title: "Braintree Billing Cycles (Recurring Billing Article)"
type: source
date_ingested: 2026-09-30
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/guides/recurring-billing/billing-cycles"
raw_files:
  - "braintree/articles/guides/recurring-billing/billing-cycles-2026-09-16.md"
tags: [braintree, recurring-billing, billing-cycles, subscriptions]
---

## Overview

This collected Braintree article is the article-level route for recurring-billing cycle length, billing dates, and finite or indefinite subscription duration. It also documents chosen-date processing timing and billing-date lifecycle constraints; it is distinct from existing Node.js recurring-billing guides and dedicated subscription API references.

## Key takeaways

- Braintree recurring billing lets a plan or subscription specify cycle length, billing date, and number of cycles. Cycle length is measured in monthly increments and is the same for each subscription within a plan.
- On a subscription billing date, Braintree says it begins charging payment methods at 9am UTC. Because the recurring-billing system runs a couple of times each day, subscriptions may not all be processed simultaneously.
- The article says recurring-billing transactions are submitted for settlement on the chosen billing date and funds are collected immediately regardless of weekends or holidays. For a declined payment method, retry logic can be configured in the Control Panel.
- A new plan can begin billing immediately or on a future date. Immediate billing anchors the cycle to the signup calendar date rather than a number of elapsed days; starts on the 29th, 30th, or 31st default to the last day of the first month in a billing cycle, so the article recommends choosing a future date present in every month for consistency.
- On a subscription's final cycle, the Control Panel's `Next Bill Date` is the subscription's final date. A new subscription can override its plan's billing date, but that date cannot be changed after creation; the article recommends canceling and creating a new subscription when a change is needed.
- The number of billing cycles determines when a plan or subscription expires. `Never expires` provides an indefinite option, and a new subscription can override the plan's cycle count at creation.

## Consequential qualifications

> [!warning] Billing-date processing is not simultaneous
> The 9am UTC statement marks when charging begins, not when every subscription finishes processing. The article says recurring billing runs a couple of times each day, so subscriptions may be processed at different times.

> [!warning] An existing subscription's billing date is immutable
> The article does not provide an in-place billing-date change after subscription creation; it recommends canceling the subscription and creating a new one.

## Detail locators

- Configurable cycle dimensions, charging start time, multiple daily runs, chosen-date settlement, weekends and holidays, and retry-logic route: `# Billing Cycles`, lines 16-20.
- Monthly cycle increments and plan-wide consistency: `## How it works > ### Billing cycle length`, line 35.
- Immediate or future start, calendar-date anchoring, and 29th-31st end-of-month handling: `## How it works > ### Billing date`, lines 40-44.
- Final-cycle `Next Bill Date` meaning: `## How it works > ### Billing date > #### Identifying the next billing date`, lines 49-60.
- Creation-time billing-date override and post-creation immutability: `## How it works > ### Billing date > #### Changing the billing date`, lines 67-69.
- Finite cycle count, `Never expires`, and creation-time cycle-count override: `## How it works > ### Number of billing cycles`, lines 74-76.

## Evidence boundaries

> [!warning] Article and implementation scopes are separate
> This article establishes its stated billing-cycle timing and lifecycle guidance. Use the separate Node.js guides and dedicated subscription request or response references for SDK operations, field schemas, and API-specific behavior. The article does not address Braintree Marketplace compatibility and therefore does not resolve the existing compatibility conflict.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-recurring-billing]]
- Generic concept: [[recurring-payments]]
- Article-level plan setup and lifecycle: [[source-braintree-recurring-article-plans]]
- Node.js recurring-billing creation guide: [[source-braintree-recurring-billing-create-node]]
- Node.js subscription creation reference: [[source-braintree-subscription-create-node]]

## Raw Sources

- [[raw/braintree/articles/guides/recurring-billing/billing-cycles-2026-09-16|Braintree recurring-billing billing-cycles article]] - complete collected article covering cycle length, billing-date processing and anchoring, next-date interpretation, post-creation date immutability, and finite or indefinite duration
