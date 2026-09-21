---
title: "Braintree Webhook Creation (Node.js Guide)"
type: source
date_ingested: 2026-09-19
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/webhooks/create/node"
raw_files:
  - "braintree/docs/guides/webhooks/create/node-2026-09-16.md"
tags: [braintree, webhooks, control-panel, notifications]
---

## Overview

This page in Braintree's Node.js webhook guide documents how to register a webhook destination in the Control Panel. Its scope is account-side destination configuration and notification selection, not implementation of a Node.js server handler or notification parsing.

## Key takeaways

- Webhooks are configured in the Control Panel, and the Control Panel user's role must have the **Manage Webhooks** permission.
- The creation flow asks for a destination URL and notification selections before the user creates the webhook. At least one notification kind must be selected.
- The destination URL must use a valid HTTPS path and be publicly accessible on the merchant's site. Braintree sends webhook notifications to that URL as POST requests.
- Multiple webhook destination URLs can be created to route particular webhook notifications to specific endpoints.

## Detail locators

- `# Create`, note and checklist: Control Panel location, **Manage Webhooks** role permission, creation navigation, destination entry, and notification selection.
- `## Destination URL`: HTTPS and public-access requirements, POST delivery, and multiple-destination routing.
- `## Notification kinds`: minimum selection required to create a webhook.

## Related

- Company: [[braintree]]
- Concept: [[braintree-webhooks]]

## Raw Sources

- [[raw/braintree/docs/guides/webhooks/create/node-2026-09-16]] — fully read Braintree Node.js-guide page for Control Panel webhook creation
