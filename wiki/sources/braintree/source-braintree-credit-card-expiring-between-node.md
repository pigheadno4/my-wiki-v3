---
title: "Braintree Credit Card Expiring Between (Node.js)"
type: source
date_ingested: 2026-09-20
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/credit-card/expiring-between/node"
raw_files:
  - "braintree/docs/reference/request/credit-card/expiring-between/node-2026-09-16.md"
tags: [braintree, node-js, credit-cards, vault, retrieval]
---

## Overview

This Braintree Node.js reference documents `gateway.creditCard.expiringBetween(before, after)` for finding objects that expire between two supplied dates. It shows callback and stream-oriented examples, but the collected purpose sentence does not render the object type and the stream example does not show a complete connection from the gateway call to the displayed stream consumer.

## Key takeaways

- The callback example constructs two JavaScript `Date` values, passes them as `before` and `after`, and receives `err` and an `expiredCards` callback argument. The callback body does not show how the returned collection is processed.
- The stream section creates an object-mode `Writable` named `writableStream`, calls `gateway.creditCard.expiringBetween(before, after)` without assigning or piping its return value, and then registers a `data` listener on the differently spelled `writeableStream`. Treat this as an incomplete collected example rather than reconstructing the intended result flow.
- The page says the objects expire between the specified dates, but it does not state whether either date boundary is inclusive or how timezones are interpreted. The literal dates in the examples do not establish those semantics.
- The collected phrase `collection ofobjects` omits the rendered object name. This source therefore does not identify a response-object type or import a response schema from another page.

> [!warning] Incomplete collected rendering
> The pinned page omits the object name in its purpose sentence and contains an unconnected, inconsistently spelled stream example. Use it to locate the Node.js date-range operation and the displayed callback/stream forms, not to infer a response schema, a working stream-consumption pattern, boundary inclusivity, or timezone behavior.

## Detail locators

- Operation purpose and missing rendered object name: `# Credit Card: Expiring Between`, lines 13-16.
- Callback dates, invocation, and callback arguments: `# Credit Card: Expiring Between > ### Node` under `Using a callback`, lines 17-22.
- Object-mode writable-stream setup: `Using a stream > ### Node`, lines 24-32.
- Stream-section dates, unassigned invocation, and `writeableStream` listener: `Using a stream > ### Node`, lines 34-38.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]

## Raw Sources

- [[raw/braintree/docs/reference/request/credit-card/expiring-between/node-2026-09-16|Braintree Node.js credit-card expiring-between reference]] - complete collected page covering the date-range operation, callback example, incomplete stream example, and evidence limitations
