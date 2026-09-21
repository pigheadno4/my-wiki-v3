---
title: "Braintree Webhooks Overview"
type: source
date_ingested: 2026-09-19
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/webhooks/overview"
raw_files:
  - "braintree/docs/guides/webhooks/overview-2026-09-16.md"
tags: [braintree, webhooks, notifications, gateway-events]
---

## Overview

Braintree webhooks push automated gateway-event notifications to a merchant-controlled server instead of requiring the merchant to poll the API. Notifications are delivered by HTTPS POST for selected triggers and carry a notification kind plus the Braintree object being reported, so merchants can update their systems or start business processes.

## Key takeaways

- The overview routes webhook selection across transaction and subscription status changes, payment-method and account activity, disputes, fraud, local payment methods, OAuth revocation, disbursements, and endpoint tests. The linked trigger and notification-kind references own the detailed event catalog.
- A webhook destination must be a valid HTTPS path. Account users also need webhook permission on their assigned Control Panel role before they can access the Webhooks tab and create a destination.
- Setup spans creating the server destination, selecting at least one notification type in the Control Panel, parsing incoming notifications, and testing the handler.

> [!warning] Delivery volume and timing
> Braintree says it strives to send notifications as quickly as events occur, but this overview gives no delivery-time guarantee. When many subscriptions bill simultaneously, notifications may arrive in a short, high-volume burst, so handler capacity must not assume evenly spaced delivery.

## Detail locators

- Event families: `# Overview`, notification list.
- Delivery shape and chosen triggers: `# Overview`, paragraph beginning "Notifications are delivered via HTTPS POST".
- Setup sequence and HTTPS requirement: `# Overview`, note and configuration checklist.
- Control Panel role requirement: `## User permissions`.
- Burst-volume qualification: `## Volume`.

This overview does not document delivery retries, ordering, duplicate-delivery behavior, signature verification, or parsing details; use the dedicated linked guides and references when those details are required.

## Related

- Company: [[braintree]]
- Concept: [[braintree-webhooks]]

## Raw Sources

- [[raw/braintree/docs/guides/webhooks/overview-2026-09-16|Braintree webhooks overview]] — complete collected overview covering purpose, event families, setup, permissions, and volume
