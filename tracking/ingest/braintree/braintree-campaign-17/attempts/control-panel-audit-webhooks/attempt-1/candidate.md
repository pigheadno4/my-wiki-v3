---
title: "Braintree Control Panel Audit Webhooks"
type: source
date_ingested: 2026-09-26
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/control-panel/audit-webhooks"
raw_files:
  - "braintree/articles/control-panel/audit-webhooks-2026-09-16.md"
tags: [braintree, control-panel, audit-webhooks, authentication, security-events]
---

## Overview

This collected Braintree Control Panel article describes Audit Webhooks as automated notifications that an authentication event occurred in the gateway. It catalogs administrative and authentication event families and two shared attributes, while limiting availability to select partners. The 2026-09-16 snapshot is evidence of the collected article, not confirmation of current availability.

## Key takeaways

- The article marks Audit Webhooks as available only to select partners. It describes them as a specialized notification system that pushes information to a designated destination when an authentication event occurs instead of requiring API polling.
- The event catalog is organized into five families: **API** changes to IP restrictions, tokenization keys, API keys, and two-factor authentication; **Login** password-reset and Control Panel login events; **AuthZ** role creation/change/assignment/unassignment and user-suspension changes; **OAuth** access grants and application creation/change; and **Fraud Protection** AVS, CVV, risk-threshold, and premium-fraud-protection changes. These are gateway administration and authentication events, not evidence that Audit Webhooks are transaction webhooks or that they report transaction lifecycle events.
- The page's Shared Attributes table documents only a notification `kind` and the UTC `timestamp` at which the webhook was triggered. It does not document a payload object, authentication/signature fields, delivery identifier, or event-specific schema.
- This article does not state which Control Panel permission is required or provide a setup procedure. It links to the separate **Create webhooks** article for general webhook information; that unread page remains a navigation route rather than factual support here.
- Beyond saying notifications are pushed to a designated destination, the article does not specify transport or endpoint requirements, timing, ordering, retries, duplicate handling, signature verification, acknowledgement responses, replay, or failure recovery.

> [!warning] Login catalog mismatch
> Under **Login**, the rendered notification-kind list includes `UserLoginFailed`, while the descriptive table instead contains `user_locked_out` and has no `user_login_failed` row. This source preserves the mismatch and does not infer that the two names are equivalent.

## Detail locators

- Select-partner availability: `**AVAILABILITY**`, line 15.
- Authentication-event purpose, push-versus-pull description, and separate general-webhook route: introductory text, lines 19-23.
- API notification kinds and trigger descriptions: `## API > ### Notifications`, lines 29-42.
- Login notification-kind list and trigger table, including the mismatch: `## Login > ### Notifications`, lines 48-59.
- Authorization event kinds and trigger descriptions: `## AuthZ > ### Notifications`, lines 65-77.
- OAuth event kinds and trigger descriptions: `## OAuth > ### Notifications`, lines 83-93.
- Fraud Protection event kinds and trigger descriptions: `## Fraud Protection > ### Notifications`, lines 99-112.
- Shared `kind` and UTC `timestamp` attributes: `## Shared Attributes`, lines 115-120.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-webhooks]]
- Supporting concept: [[braintree-control-panel]]

## Related raw API references

- [[raw/braintree/articles/control-panel/webhooks-2026-09-16|Braintree Control Panel Create webhooks article]] - navigation-only general-webhook route linked by the Audit Webhooks article; not read or used as factual evidence here

## Raw Sources

- [[raw/braintree/articles/control-panel/audit-webhooks-2026-09-16|Braintree Control Panel Audit Webhooks]] - complete collected article covering select-partner availability, administrative and authentication event families, and shared notification attributes
