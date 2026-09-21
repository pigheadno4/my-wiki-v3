---
title: "Braintree Plan Create (Node.js)"
type: source
date_ingested: 2026-09-20
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/plan/create/node"
raw_files:
  - "braintree/docs/reference/request/plan/create/node-2026-09-16.md"
tags: [braintree, node-js, plans, recurring-billing, add-ons, discounts]
---

## Overview

This Braintree Node.js reference documents creating a plan with `gateway.plan.create()` in callback and Promise forms. It preserves the merchant recurring-billing prerequisite and routes readers to the page's required-input and add-on/discount examples without replacing the raw reference with a field inventory.

## Key takeaways

- Before creating a plan, the merchant must have the recurring billing feature enabled. This page does not establish how enablement is performed.
- The page identifies `name`, `price`, `billing_frequency`, and `currency_iso_code` as required parameters, while the displayed Node examples use `name`, `price`, `billingFrequency`, and `currencyIsoCode`. Use the complete raw examples as the authority for the displayed Node spelling.
- The page documents two ways to include add-ons or discounts during plan creation: pass modification tokens, or use the displayed add/update/remove structures for `addOns` and `discounts`.
- For the displayed add/update structures, details are inherited from the referenced add-on or discount and the page identifies a limited set of values that can be overridden; the complete examples and override list remain in raw.
- This creation reference does not say that creating a plan creates a subscription or changes existing subscriptions. The linked Plan response and recurring-billing guide are navigation routes, not additional factual evidence for this source.

## Detail locators

- Merchant recurring-billing prerequisite: `# Plan: Create`, line 17.
- Required-input prose plus callback and Promise creation examples: `# Plan: Create`, lines 19-40.
- Modification-token approach: `### Add add_ons/discounts when creating a plan`, lines 42-71.
- Displayed add/update/remove structures for `addOns` and `discounts`: same section, lines 72-177.
- Inheritance and supported override list: same section, lines 178-184; expanded callback and Promise examples continue through line 284.
- External Plan response-object route: `# Plan: Create`, line 15.
- Recurring-billing plans navigation route: `## See Also`, lines 287-290.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]

## Related raw API references

- [[raw/braintree/docs/guides/recurring-billing/plans/node-2026-09-16|Braintree Node.js recurring-billing plans guide]] - navigation-only destination from See Also; not used as factual evidence here

## Raw Sources

- [[raw/braintree/docs/reference/request/plan/create/node-2026-09-16|Braintree Node.js plan-create request reference]] - complete collected page covering the merchant prerequisite, required-input examples, and add-on/discount creation approaches
