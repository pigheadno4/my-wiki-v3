---
title: "Braintree Webhook Parsing (Node.js)"
type: source
date_ingested: 2026-09-19
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/webhooks/parse/node"
raw_files:
  - "braintree/docs/guides/webhooks/parse/node-2026-09-16.md"
tags: [braintree, webhooks, node-js, signature-verification, retries]
---

## Overview

This guide shows how a Node.js webhook handler passes Braintree's signed `bt_signature` and `bt_payload` POST parameters to `gateway.webhookNotification.parse()`. It also identifies the parsed notification shape, invalid-signature failure, non-sequential arrival warning, and the response condition that controls Braintree's documented retries.

## Key takeaways

- Braintree sends the webhook to the configured destination URL as a POST whose `application/x-www-form-urlencoded` body contains `bt_signature` and `bt_payload`. The signed payload is intended to show that the message came from Braintree and was not modified in transit.
- The Node examples pass both parameters to `gateway.webhookNotification.parse()` using either a callback or a Promise. The result is a `WebhookNotification` with a UTC timestamp, a kind mapped to webhook triggers, and a Braintree object determined by the notification type.
- Parsing a notification with an invalid signature raises an invalid-signature exception. Use the dedicated exception reference linked from the raw page for exception details.

> [!warning] Ordering and retry scope
> Notifications may not be delivered sequentially, so handlers should use the event timestamp rather than assuming arrival order. If a webhook takes longer than 30 seconds to respond, Braintree treats it as a timeout and retries hourly for up to 3 hours in sandbox or 24 hours in production, stopping when it receives a successful HTTPS `2xx` response within 30 seconds. These conditions describe retry behavior; they do not establish a general delivery-time or sequential-delivery guarantee.

## Detail locators

- Signed inputs and notification contents: `# Parse`, paragraphs and list before `### Callback`.
- Callback handler: `### Callback`.
- Promise handler: `### Promise`.
- Invalid-signature failure: `### Exceptions`.
- Timeout, cadence, environment windows, and successful-response condition: `### Retries`.

## Related

- Company: [[braintree]]
- Concept: [[braintree-webhooks]]
- Related source: [[source-braintree-webhooks-overview]]

## Raw Sources

- [[raw/braintree/docs/guides/webhooks/parse/node-2026-09-16|Braintree webhook parsing for Node.js]] — complete collected guide covering signed inputs, callback and Promise parsing, invalid signatures, ordering, and retries
