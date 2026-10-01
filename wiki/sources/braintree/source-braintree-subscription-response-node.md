---
title: "Braintree Subscription Response History (Node.js)"
type: source
date_ingested: 2026-09-30
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/response/subscription/node"
raw_files:
  - "braintree/docs/reference/response/subscription/node-2026-09-16.md"
tags: [braintree, node-js, subscriptions, recurring-billing, response-objects]
---

## Overview

This Braintree Node.js response reference documents the history objects returned on a subscription. It is a narrow response-object route for locating recorded balance, price, status and event-source detail; it is distinct from recurring-billing articles, Node.js subscription guides and request references, and it does not define the broader subscription lifecycle.

## Key takeaways

- Each subscription history object returned on a subscription includes balance, price, status and subscription-event source information. The exact field inventory remains at the raw locator below.
- The history object's documented status values are `Active`, `Canceled`, `Expired`, `PastDue` and `Pending`. This page names those states but does not define their transitions, billing consequences or lifecycle semantics.
- The documented `subscription_source` values are `api`, `control_panel` and `recurring`, described as where the subscription event was created. The page does not further define those origins or state that they identify the original subscription-creation channel.
- The callback and Promise examples retrieve a subscription with `gateway.subscription.find()` and access the first history entry's balance through `subscription.statusHistory[0].balance`. They illustrate reading returned history, not creating or updating a subscription and not guaranteeing that every returned subscription has a first history entry.
- The page states that results are limited according to the linked PayPal Data Protection Addendum for Card Processing Products policy. Because that external policy is not part of this source, this entry preserves the limitation notice without interpreting which results or fields are limited.

## Detail locators

- Results-limitation notice: `# Subscription`, lines 17-18.
- Subscription-history object scope and exact field table: `## Subscription history`, lines 21-36.
- Documented history status values: `## Subscription history > status`, lines 27-32.
- Documented event-source values: `## Subscription history > subscription_source`, lines 33-36.
- Callback and Promise access examples: `## Subscription history > ### Callbacks`, lines 38-46, and `### Promises`, lines 48-55.

## Evidence boundaries

> [!warning] History values are not lifecycle definitions
> This response reference lists history status and event-source values but does not explain status transitions, billing effects, retry behavior, cancellation timing or other lifecycle meaning. Use the separate recurring-billing articles and guides for those topics, and do not treat this page as a request schema or subscription action guide.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-recurring-billing]]
- Node.js SDK context: [[braintree-server-sdk]]
- Distinct article-level subscription administration: [[source-braintree-recurring-article-subscriptions]]
- Distinct single-subscription lookup request: [[source-braintree-subscription-find-node]]
- Distinct subscription-search request: [[source-braintree-subscription-search-node]]

## Raw Sources

- [[raw/braintree/docs/reference/response/subscription/node-2026-09-16|Braintree Subscription response reference - Node.js]] - complete collected page covering subscription-history field categories, documented status and event-source values, callback and Promise history access examples, and the results-limitation notice
