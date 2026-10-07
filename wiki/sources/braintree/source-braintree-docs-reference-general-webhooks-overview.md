---
title: "Braintree Generic Webhook Reference Overview"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/general/webhooks/overview"
raw_files:
  - "braintree/docs/reference/general/webhooks/overview-2026-09-16.md"
tags: [braintree, webhooks, notification-kinds, reference]
---

## Overview

This unversioned Braintree reference is the generic index for webhook notification kinds. It explains how a notification identifies its trigger, routes readers to the category-specific trigger references, states the common notification attributes, and identifies invalid-signature failure during parsing.

## Key takeaways

- Calling `kind` on the notification object reveals what triggered the webhook. The exact trigger condition depends on that notification kind, so the linked category references remain authoritative for event-specific conditions.
- Every webhook notification has a `kind`, a `timestamp`, and one additional attribute specific to its notification type. The category list spans account, merchant/platform, payment, subscription, dispute, transaction, fraud, OAuth, local-payment, disbursement, and test references; the list is navigation rather than one universal payload contract.
- Attempting to parse a webhook notification with an invalid signature raises an invalid-signature exception. This overview routes to an exception reference but does not specify a language SDK method or the signature inputs and verification procedure.

## Scope boundary

This is a generic webhook reference snapshot, not a PayPal Commerce Channel API message contract or a product- and SDK-specific integration guide. Category presence does not establish product enablement, merchant eligibility, or that an event occurred; its invalid-signature statement is a parsing-security boundary, while environment-specific handling, acknowledgement, retry, and delivery-time rules remain with their dedicated authorities and must not be transferred into this page.

## Detail locators

- Guide route for creating or parsing webhooks: `# Overview`, line 16.
- Notification-kind meaning, category routes, and kind-specific trigger condition: `## Notification kinds`, lines 19-41.
- Common and type-specific notification attributes: `## Attributes`, lines 44-46.
- Trigger-condition routing: `## Triggers`, lines 49-51.
- Invalid-signature parsing failure and exception route: `## Exceptions`, lines 54-56.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-webhooks]]
- Related guide: [[source-braintree-webhooks-overview]]

## Raw Sources

- [[raw/braintree/docs/reference/general/webhooks/overview-2026-09-16|Braintree generic webhook reference overview]] - complete collected page covering notification-kind routing, common attributes, trigger routing, and invalid-signature parsing failure
