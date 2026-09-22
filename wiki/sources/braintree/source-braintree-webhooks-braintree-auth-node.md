---
title: "Braintree Auth Webhooks (Node.js)"
type: source
date_ingested: 2026-09-22
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/general/webhooks/braintree-auth/node"
raw_files:
  - "braintree/docs/reference/general/webhooks/braintree-auth/node-2026-09-16.md"
tags: [braintree, node-js, webhooks, braintree-auth, beta, connected-merchants]
---

## Overview

This Braintree Node.js reference documents closed-beta Braintree Auth webhook notifications for connected-merchant underwriting or application activity and PayPal account linking changes. It provides event conditions and broad payload categories without importing the separate OAuth access-revocation or Grant API payment-instrument semantics.

## Key takeaways

- Braintree Auth is identified as closed beta, with interested users directed to the Business Development team. This page does not state a separate sandbox-versus-production availability rule.
- `connected_merchant_status_transitioned` is triggered when a connected merchant's underwriting status changes or the merchant submits an application. The notification reports either stated event; it does not perform underwriting or submit the application.
- `connected_merchant_paypal_status_changed` is triggered when a connected merchant's PayPal account has been successfully linked or unlinked to their Braintree gateway. It does not establish how linking or unlinking is initiated.
- The documented payload categories are notification kind, UTC trigger date and time, connected merchant ID, and OAuth application client ID. The page routes kind-specific additional attributes to the separate Braintree Auth webhooks guide.

## Detail locators

- Closed-beta availability and interest route: `# Braintree Auth > AVAILABILITY`, lines 17-18.
- Notification-object `kind` purpose and Braintree Auth scope: `# Braintree Auth > ### Notification kinds`, lines 23-25.
- Underwriting-status or application-submission condition: notification table, line 29.
- Successful PayPal account link or unlink condition: notification table, line 30.
- Payload categories and kind-specific guide route: `# Braintree Auth > ### Attributes`, lines 33-35.

## Evidence limitations

> [!warning] Braintree Auth scope is distinct
> This page states closed-beta Braintree Auth scope but no separate environment split. Its events concern connected-merchant underwriting/application activity and PayPal account linking status; they are not OAuth access-revocation events or Grant API payment-instrument update/revocation events. A webhook reports the stated event and does not itself perform the underlying operation.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-webhooks]]
- Distinct OAuth access-revocation notifications: [[source-braintree-webhooks-oauth-node]]
- Distinct Grant API payment-instrument notifications: [[source-braintree-webhooks-grant-api-node]]

## Related raw API references

- [[raw/braintree/docs/guides/braintree-auth/webhooks/node-2026-09-16|Braintree Auth webhooks guide for Node.js]] - navigation-only route for kind-specific additional attributes; not used as factual evidence here

## Raw Sources

- [[raw/braintree/docs/reference/general/webhooks/braintree-auth/node-2026-09-16|Braintree Auth webhook reference for Node.js]] - complete collected page covering closed-beta availability, connected-merchant notification conditions and payload categories
