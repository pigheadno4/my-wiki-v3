---
title: "Braintree Subscription Webhooks (Node.js)"
type: source
date_ingested: 2026-09-20
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/general/webhooks/subscription/node"
raw_files:
  - "braintree/docs/reference/general/webhooks/subscription/node-2026-09-16.md"
tags: [braintree, node-js, webhooks, subscriptions, recurring-billing]
---

## Overview

This Braintree Node.js reference catalogs subscription webhook notification kinds, the conditions that trigger them, and the subscription data exposed through the notification attributes. It is an event reference, not a general webhook-delivery or subscription-billing guarantee.

## Key takeaways

- The notification object's `kind` identifies the trigger. The table covers billing skipped, cancellation, successful and unsuccessful charging, expiration, trial end, activation, and transition to past due.
- A successful-charge notification also occurs when proration on an upgrade creates a new transaction mid-cycle. An unsuccessful-charge notification requires an existing subscription that fails to create a successful charge; the page excludes manual retries and subscription-creation attempts that fail because of an unsuccessful transaction.
- The active notification is triggered by creation of the first authorized transaction or by a successful transaction moving a subscription from Past Due to Active. A trial-to-first-billing-cycle transition does not trigger it.
- The past-due notification is limited to a decline of the initial transaction in a billing cycle and is not triggered again in that billing cycle after the status has moved to past due. A skipped-billing notification has its own condition: a negative or zero balance that covers the subscription cost.
- The attributes route identifies the notification kind, UTC trigger time, and a `Subscription` object. That subscription object contains only the 20 most recent associated transactions.

## Detail locators

- Notification-kind meaning and trigger catalog: `# Subscription` > `### Notification kinds`, lines 17-32.
- Skipped-billing balance condition: notification row `subscription_billing_skipped`, line 25.
- Successful- and unsuccessful-charge qualifications: rows `subscription_charged_successfully` and `subscription_charged_unsuccessfully`, lines 27-28.
- Active and past-due transition qualifications and exceptions: rows `subscription_went_active` and `subscription_went_past_due`, lines 31-32.
- Notification attributes and 20-most-recent-transactions limit: `# Subscription` > `### Attributes`, lines 35-37.

## Collected evidence limitation

> [!warning] Event-reference scope
> These rows state when the named subscription notification kinds are triggered and what the documented payload route contains. They do not establish universal webhook delivery, ordering, retry, duplicate-handling, billing-success, or payment-finality guarantees; use the dedicated webhook and subscription authorities for those separate questions.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-webhooks]]
- Related source: [[source-braintree-webhooks-overview]]

## Raw Sources

- [[raw/braintree/docs/reference/general/webhooks/subscription/node-2026-09-16|Braintree Node.js subscription-webhook reference]] - complete page covering subscription notification kinds, event-specific trigger conditions, and payload-attribute limits
