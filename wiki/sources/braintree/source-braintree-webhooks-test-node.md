---
title: "Braintree Test Webhook (Node.js)"
type: source
date_ingested: 2026-09-22
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/general/webhooks/test/node"
raw_files:
  - "braintree/docs/reference/general/webhooks/test/node-2026-09-16.md"
tags: [braintree, node-js, webhooks, testing, control-panel]
---

## Overview

This Braintree Node.js reference identifies the notification kind used for a Control Panel-triggered test webhook. It documents only notification metadata and does not present the test as a real payment or other production gateway event.

## Key takeaways

- Calling `kind` on the notification object identifies what triggered the webhook. The only notification kind listed for Test webhooks is `check`.
- The `check` kind is triggered by a test notification in the Control Panel. This trigger does not establish that a transaction, payment, subscription or other production event occurred.
- The Attributes section lists only the webhook notification kind and the UTC time at which the webhook was triggered. It does not document a transaction, payment, customer or other event-object payload for this test notification.

## Detail locators

- Notification-object `kind` purpose and Test webhook scope: `# Test > ### Notification kinds`, lines 17-21.
- `check` kind and Control Panel test trigger: notification table, lines 23-27.
- Kind and UTC trigger-time attributes: `# Test > ### Attributes`, lines 30-32.

## Evidence limitations

> [!warning] Test notification is not a real event
> This reference establishes a Control Panel-triggered `check` notification with only kind and UTC trigger time documented. It does not prove production delivery, successful payment processing, a real gateway event, or the presence of any business-object payload.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-webhooks]]
- Sample-payload and Control Panel testing workflows: [[source-braintree-webhooks-testing-go-live-node]]
- Webhook purpose and delivery setup: [[source-braintree-webhooks-overview]]

## Raw Sources

- [[raw/braintree/docs/reference/general/webhooks/test/node-2026-09-16|Braintree Node.js test webhook reference]] - complete collected page covering the `check` notification kind, Control Panel trigger and documented metadata-only attributes
