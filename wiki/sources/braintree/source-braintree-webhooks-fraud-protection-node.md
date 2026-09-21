---
title: "Braintree Fraud Protection Webhook (Node.js)"
type: source
date_ingested: 2026-09-21
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/general/webhooks/fraud-protection/node"
raw_files:
  - "braintree/docs/reference/general/webhooks/fraud-protection/node-2026-09-16.md"
tags: [braintree, node-js, webhooks, fraud-protection, transaction-review]
---

## Overview

This Braintree Node.js reference documents the `transaction_reviewed` Fraud Protection webhook. It covers the event condition for a dashboard-reviewed transaction and the categories of review data reported by the notification.

## Key takeaways

- `webhook_notification.kind` identifies what triggered the webhook. The only notification kind listed on this page is `transaction_reviewed`.
- The event applies when a transaction cited for Review in the Fraud Protection Dashboard has been accepted or rejected. The page does not establish that every transaction, fraud decision, product, payment method, or merchant is covered by this webhook.
- If the reviewed transaction was rejected, the page says a void or refund of the transaction amount **has been requested**. It does not state that the void or refund completed, succeeded, settled, or became final.
- The Attributes section is concatenated and supplies no visible attribute names. It identifies the payload categories as notification kind, reviewed transaction identifier, resulting risk decision, reviewer email, reviewer notes, UTC review time, and UTC webhook-trigger time, then routes further detail to the Fraud Protection guide.

## Detail locators

- Notification-kind trigger role: `### Notification kinds`, lines 17-21.
- `transaction_reviewed` acceptance/rejection condition and requested void/refund qualification: notification table, lines 23-25.
- Concatenated review payload categories and further-guide route: `### Attributes`, lines 28-30.

## Evidence limitations

> [!warning] Event-specific scope
> This page documents one Fraud Protection Dashboard review event. It does not establish universal fraud screening or notification coverage, merchant or payment-method eligibility, review automation, delivery guarantees, or completion of a requested void or refund; it also does not expose visible payload field names.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-webhooks]]

## Raw Sources

- [[raw/braintree/docs/reference/general/webhooks/fraud-protection/node-2026-09-16|Braintree Node.js Fraud Protection webhook reference]] - complete page covering the reviewed-transaction trigger, requested void/refund qualification, payload categories, and further-guide route
