---
title: "Braintree Subscription Find (Node.js)"
type: source
date_ingested: 2026-09-20
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/subscription/find/node"
raw_files:
  - "braintree/docs/reference/request/subscription/find/node-2026-09-16.md"
tags: [braintree, node-js, subscriptions, lookup]
---

## Overview

This Braintree Node.js reference documents lookup of a single subscription by its ID. Its code examples invoke `gateway.subscription.find()` in callback and Promise forms; this page is about retrieving an existing subscription, not creating or cancelling one.

## Key takeaways

- The callback example passes a subscription ID to `gateway.subscription.find()` and receives a `result` argument; the Promise example passes the same kind of ID and resolves to `result`. The surrounding prose omits the method name, so this invocation claim comes from the displayed code rather than a reconstruction of the incomplete sentence.
- If the subscription cannot be found, the page routes the outcome to Braintree's Node.js `notFoundError` reference. The page also links to the Subscription response-object reference for result details; this source does not reconstruct that unread response schema.
- The page states that results are limited according to the linked PayPal Data Protection Addendum for Card Processing Products policy. Because that external policy was not part of this source, this entry preserves the limitation notice without inferring which results or fields are limited, or why.
- The trailing `Otherwise, use.` prose is incomplete. It does not establish an alternative method, creation behavior, cancellation behavior, or any other subscription lifecycle action.

## Detail locators

- Results-limitation notice and Subscription response-object route: `# Subscription: Find`, lines 16-19.
- Single-subscription lookup purpose and omitted prose method name: `# Subscription: Find`, line 21.
- Callback and Promise invocation forms: `# Subscription: Find > ### Callback`, lines 22-26, and `### Promise`, lines 28-32.
- Incomplete alternative prose and missing-subscription error route: `# Subscription: Find`, lines 33-35.

## Related

- Company: [[braintree]]
- Concept: [[braintree-server-sdk]]

## Raw Sources

- [[raw/braintree/docs/reference/request/subscription/find/node-2026-09-16|Braintree Node.js subscription find reference]] - complete page covering single-subscription ID lookup, callback and Promise examples, the results-limitation notice, incomplete surrounding prose, and the missing-subscription error route
