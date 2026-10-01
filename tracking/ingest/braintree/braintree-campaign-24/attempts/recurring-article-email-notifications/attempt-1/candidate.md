---
title: "Braintree Recurring Billing Email Notifications"
type: source
date_ingested: 2026-09-30
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/guides/recurring-billing/email-notifications"
raw_files:
  - "braintree/articles/guides/recurring-billing/email-notifications-2026-09-16.md"
tags: [braintree, recurring-billing, email-notifications, subscriptions, past-due]
---

## Overview

This Braintree article documents customer email notifications for recurring-billing charge failures and retries. These Control Panel-configured emails are limited to events that leave a subscription in the `Past Due` state; the article is not an API or webhook notification reference, and it routes successful sale or refund receipts to separate documentation.

## Key takeaways

- Braintree lists four configurable recurring-billing email events: **First Decline** after the first unsuccessful recurring-cycle charge attempt, **First Retry** after an automatic retry following that failure, **Second Retry** after the next attempt when the first retry failed, and **Past Due** a configurable number of days after the first decline.
- Braintree sends these emails only for events that leave the subscription `Past Due`. If retry logic cancels a subscription after the second retry, the article's example says the customer receives only **First Decline** and **First Retry** emails: there is no **Second Retry** email and no automatic cancellation notification.
- The account's authorized signer must contact Support to request feature activation. After Support confirms activation, the article instructs the merchant to enable "email receipts" in the Control Panel and configure the recurring plan and send options under **Subscriptions** > **Email Notifications**.
- The authorized signer is not the same as the Control Panel's Account Admin role and cannot be managed in the Control Panel.
- Emails for every successful sale transaction or refund belong to the separate Email Receipts route, not this recurring-billing notification route.

## Detail locators

- Separate successful-sale and refund Email Receipts route: `# Email Notifications > NOTE`, lines 17-18.
- First Decline, First Retry, Second Retry and Past Due triggers: `# Email Notifications`, lines 22-28.
- `Past Due`-state condition and cancellation example: `# Email Notifications`, line 30.
- Support activation prerequisite and Control Panel setup path: `## Configuring email notifications`, lines 33-43.
- Sender, subject, plain-text body and send-option configuration categories: `### Configuration options`, lines 46-63.
- Authorized-signer identity and Account Admin distinction: `#### Authorized signer`, lines 66-70.

> [!warning] Customer email scope
> This article documents customer emails configured through the Control Panel. It does not establish webhook event kinds, payloads, delivery behavior or API request/response semantics. Keep those routes separate, and do not generalize these emails beyond recurring-billing events that leave the subscription `Past Due`.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-recurring-billing]]
- Recurring-billing status and retry context: [[source-braintree-recurring-billing-overview]]
- Separate subscription webhook reference: [[source-braintree-webhooks-subscription-node]]

## Related raw API references

- [[raw/braintree/articles/guides/recurring-billing/recurring-advanced-settings-2026-09-16|Braintree recurring-billing advanced settings article]] - navigation only for automatic retries and retry logic; not read as factual evidence for this source
- [[raw/braintree/articles/control-panel/transactions/email-receipts-2026-09-16|Braintree Email Receipts article]] - navigation only for successful sale and refund receipts; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/articles/guides/recurring-billing/email-notifications-2026-09-16|Braintree recurring-billing email notifications article]] - complete collected page covering customer-email triggers, the `Past Due` condition, cancellation example, activation prerequisite and Control Panel configuration route
