---
title: "Braintree Account Updater Webhook (Node.js)"
type: source
date_ingested: 2026-09-21
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/general/webhooks/account-updater/node"
raw_files:
  - "braintree/docs/reference/general/webhooks/account-updater/node-2026-09-16.md"
tags: [braintree, node-js, webhooks, account-updater, vault]
---

## Overview

This Braintree Node.js reference documents the Account Updater daily-report webhook. The webhook is available only to merchants using Braintree's Account Updater feature, and its single listed notification kind is suppressed when there were no updates.

## Key takeaways

- This webhook is available only to merchants using the Account Updater feature. The page does not establish that every Braintree merchant has the feature or describe feature enrollment, configuration, pricing, or regional availability.
- `webhook_notification.kind` identifies what triggered the webhook. The only listed kind is `account_updater_daily_report`.
- That notification represents a daily report containing all vaulted payment methods updated during the prior 24 hours. If there are no updates, the webhook is not triggered. This page does not establish when individual updates occur or promise a webhook for each updated payment method.
- The Attributes section is concatenated and supplies no visible attribute names. It identifies the payload categories as notification kind, UTC trigger time, report-generation date, and an assigned report-download URL that expires after one week. It does not document the report's file format, download authentication, delivery guarantees, retries, ordering, or duplicate handling.

## Detail locators

- Account Updater merchant-availability restriction: `# Account Updater > **AVAILABILITY**`, lines 17-18.
- Notification-kind trigger role: `### Notification kinds`, lines 23-27.
- Daily-report contents and no-updates suppression condition: notification table, lines 29-31.
- Concatenated payload categories and one-week link expiry: `### Attributes`, lines 34-36.

## Evidence limitations

> [!warning] Feature-specific webhook
> The page does not support universalizing Account Updater availability or reconstructing missing attribute identifiers. It documents a report-level notification for feature users, not per-payment-method delivery or proof that a Vault update occurred successfully in every case.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-webhooks]]

## Raw Sources

- [[raw/braintree/docs/reference/general/webhooks/account-updater/node-2026-09-16|Braintree Node.js Account Updater webhook reference]] - complete page covering feature-specific merchant availability, the daily-report trigger, no-update suppression, payload categories, and report-link expiry
