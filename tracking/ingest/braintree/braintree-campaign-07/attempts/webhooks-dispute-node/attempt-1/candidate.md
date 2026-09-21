---
title: "Braintree Dispute Webhooks (Node.js)"
type: source
date_ingested: 2026-09-20
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/general/webhooks/dispute/node"
raw_files:
  - "braintree/docs/reference/general/webhooks/dispute/node-2026-09-16.md"
tags: [braintree, node-js, webhooks, disputes]
---

## Overview

This Braintree Node.js reference catalogs dispute webhook notification kinds, the conditions represented by those kinds, and the page's notification-attribute routes. It is an event reference, not a guarantee of webhook delivery or a complete dispute lifecycle specification.

## Key takeaways

- The notification object's `kind` identifies what triggered the webhook. The page lists accepted, automatically accepted, disputed, expired, lost, opened, under-review, and won dispute notification kinds.
- The `dispute_under_review` kind is specifically described as a dispute being under internal review with PayPal. The other rows state the named dispute condition without adding timing, transition, or outcome guarantees.
- The collected **Attributes** section identifies notification kind and UTC trigger time, then gives a deprecation direction to use `transaction` on the Dispute object. Because the collected rendering omits the affected attribute's label, this source does not identify which attribute is deprecated or reconstruct the complete notification payload.

## Detail locators

- Notification-kind purpose and event-trigger catalog: `# Dispute` > `### Notification kinds`, lines 17-46.
- PayPal-qualified internal-review trigger: row `dispute_under_review`, lines 41-43.
- Notification attributes and the unresolved deprecated-attribute direction: `# Dispute` > `### Attributes`, lines 49-51.

> [!warning] Event-reference scope
> The notification-kind rows name conditions that trigger dispute webhooks. They do not establish webhook delivery timing, ordering, retries, duplicate handling, or a universal sequence between dispute states; use the dedicated webhook and dispute authorities for those separate questions.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-webhooks]]
- Cross-cutting concept: [[disputes]]
- Related source: [[source-braintree-webhooks-overview]]

## Raw Sources

- [[raw/braintree/docs/reference/general/webhooks/dispute/node-2026-09-16|Braintree Node.js dispute-webhook reference]] - complete page covering dispute notification kinds, event conditions, and the collected attribute/deprecation route
