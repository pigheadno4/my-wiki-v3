---
title: "Braintree Control Panel Webhooks"
type: source
date_ingested: 2026-09-26
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/control-panel/webhooks"
raw_files:
  - "braintree/articles/control-panel/webhooks-2026-09-16.md"
tags: [braintree, control-panel, webhooks, notifications, permissions]
---

## Overview

This collected Braintree Control Panel article explains how a permitted user creates and tests gateway webhooks. It frames webhooks as push notifications to a designated destination and separates Control Panel configuration from the server-side parsing required after creation. The 2026-09-16 snapshot is collected evidence, not confirmation of current behavior or availability.

## Key takeaways

- The page describes webhooks as automated gateway-event notifications pushed to a designated destination instead of information that the merchant must pull through the API. It lists subscription-status, disbursement, transaction-dispute, Braintree Marketplace sub-merchant-account-status, and Grant API payment-method-status event families.
- Configuring a webhook requires the Control Panel user's role to include the exact **Manage Webhooks** permission. The documented creation flow uses the Control Panel's **API** area and **Webhooks** tab, then asks for a destination URL and notification selections.
- Creating the Control Panel configuration does not complete the integration: the merchant must separately configure its server to parse received webhooks. The linked parsing guide owns those implementation details and is navigation-only evidence for this source.
- The **Check URL** action can send a test webhook for an existing configuration. The article warns that testing in production can cause unexpected behavior when handling code does not inspect the webhook kind it receives; the linked testing guide owns notification details.
- This article does not state transport security requirements, delivery timing, ordering, retry, duplicate-delivery, signing, acknowledgement, replay, or failure-recovery semantics. It also does not identify Audit Webhook event kinds or establish that these general Control Panel steps apply to the separate select-partner Audit Webhooks feature.

## Detail locators

- Push-versus-pull purpose and merchant response workflow: introductory paragraphs, lines 16-18.
- Supported notification families: `## Types of webhooks`, lines 21-30.
- Required Control Panel role permission: `## Creating webhooks`, line 35.
- Control Panel destination and notification selection plus separate server parsing: `## Creating webhooks`, lines 37-48.
- Test action and production-handler warning: `## Testing webhooks`, lines 51-66.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-webhooks]]
- Supporting concept: [[braintree-control-panel]]

## Related raw API references

- [[raw/braintree/articles/control-panel/users-roles/role-permissions-2026-09-16|Braintree Control Panel role permissions]] - navigation-only route for the linked Manage Webhooks permission detail
- [[raw/braintree/docs/guides/webhooks/create/node-2026-09-16|Braintree Node.js webhook creation guide]] - navigation-only route for destination and notification-selection details
- [[raw/braintree/docs/guides/webhooks/parse/node-2026-09-16|Braintree Node.js webhook parsing guide]] - navigation-only route for server-side parsing behavior
- [[raw/braintree/docs/guides/webhooks/testing-go-live/node-2026-09-16|Braintree Node.js webhook testing and go-live guide]] - navigation-only route for test-notification details

## Raw Sources

- [[raw/braintree/articles/control-panel/webhooks-2026-09-16|Braintree Control Panel Webhooks]] - complete collected article covering webhook purpose, event families, configuration permission, creation flow and testing warning
