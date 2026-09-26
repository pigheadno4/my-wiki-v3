---
title: "Braintree Control Panel Transaction Issues"
type: source
date_ingested: 2026-09-23
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/control-panel/transactions/transaction-issues"
raw_files:
  - "braintree/articles/control-panel/transactions/transaction-issues-2026-09-16.md"
tags: [braintree, control-panel, transactions, transaction-issues, notifications, webhooks]
---

## Overview

This collected Braintree Control Panel article defines transaction issues as rare, unexpected processing problems outside standard processor declines and gateway rejections, and says they are generally more complex than a normal decline or rejection. It documents notification delivery and recipient routes, but it does not document an investigation workflow or the underlying causes and remediation of an issue.

## Key takeaways

- The article distinguishes transaction issues from standard processor declines and gateway rejections: they are additional unexpected issues that can prevent smooth processing and are described as rare and generally more complex. The linked decline and gateway-rejection articles are navigation only below and were not used as factual evidence for this source.
- Transaction issue notifications can optionally be delivered by webhook alongside emails. Before webhook creation, the article routes readers to separate instructions for user permissions and destination preparation, then gives a Control Panel path through **API** and the **Webhooks** tab to provide a destination URL and make notification selections. This page does not document the webhook payload, notification kind, delivery timing, ordering, retries, duplicate handling, signature verification, or investigation outcome.
- The article provides two notification-recipient options. A **User Recipient** is an existing Control Panel user and receives notifications only for transactions accessible to that user's role.
- An **Email Recipient** can be any email address, including an internal distribution list. That address receives all transaction issue notifications even when it also belongs to a Control Panel user with limited permissions.

> [!warning] Notification is not investigation or resolution evidence
> This page documents the category distinction and notification configuration/recipient scope only. It does not identify transaction-issue causes, status or reason values, a Control Panel investigation view, remediation steps, resolution timing, or proof that a notified issue was resolved.

## Detail locators

- Transaction issues versus processor declines and gateway rejections: `# Transaction Issues`, line 16.
- Optional webhook delivery alongside emails and linked setup authorities: `## Notifications`, line 21.
- Control Panel webhook-creation navigation: `## Notifications`, lines 24-30.
- Two recipient-designation options: `## Notifications`, line 32.
- User-recipient role-access scope: `## Notifications`, line 34.
- Email-recipient all-notification scope and limited-user qualification: `## Notifications`, line 36.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-control-panel]]
- Supporting concept: [[braintree-webhooks]]

## Related raw API references

- [[raw/braintree/articles/control-panel/transactions/declines-2026-09-16|Braintree Control Panel transaction declines article]] - navigation-only destination linked for the separate processor-decline category; not read or used as factual evidence here
- [[raw/braintree/articles/control-panel/transactions/gateway-rejections-2026-09-16|Braintree Control Panel gateway-rejections article]] - navigation-only destination linked for the separate gateway-rejection category; not read or used as factual evidence here
- [[raw/braintree/docs/reference/general/webhooks/overview-2026-09-16|Braintree webhook overview reference]] - navigation-only destination linked for webhook preparation; not read or used as factual evidence here
- [[raw/braintree/articles/control-panel/users-roles/managing-users-roles-2026-09-16|Braintree Control Panel user-role management article]] - navigation-only destination linked from the User Recipient scope; not read or used as factual evidence here

## Raw Sources

- [[raw/braintree/articles/control-panel/transactions/transaction-issues-2026-09-16|Braintree Control Panel transaction-issues article]] - complete collected page covering the issue-category distinction, optional webhook delivery, Control Panel webhook route, and user/email recipient scope
