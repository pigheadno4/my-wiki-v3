---
title: "Braintree Sub-merchant Account Webhooks (Node.js)"
type: source
date_ingested: 2026-09-22
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/general/webhooks/sub-merchant-account/node"
raw_files:
  - "braintree/docs/reference/general/webhooks/sub-merchant-account/node-2026-09-16.md"
tags: [braintree, node-js, webhooks, marketplace, sub-merchants]
---

## Overview

This Braintree Node.js reference documents webhook notifications for approved and declined sub-merchant account events in the Braintree Marketplace onboarding context. It identifies each event kind and the broad payload route without treating a notification as an account-creation or activation operation.

## Key takeaways

- Calling `kind` on the notification object identifies what triggered the webhook. The two stated values are `sub_merchant_account_approved` and `sub_merchant_account_declined`.
- `sub_merchant_account_approved` is triggered when a sub-merchant has been approved. The notification reports that event; it does not itself create, submit, approve or activate an account.
- `sub_merchant_account_declined` is triggered when a sub-merchant has been declined. The notification reports the decline and does not perform an account operation.
- The stated payload routes are the notification kind, the UTC date and time at which the webhook was triggered, and a `MerchantAccount` object. The collected page points declined notifications to the Braintree Marketplace sub-merchant onboarding guide for additional attributes.

## Detail locators

- Notification-object `kind` purpose and event-kind scope: `# Sub-merchant Account > ### Notification kinds`, lines 17-21.
- Approved and declined event conditions: notification table, lines 23-26.
- Payload categories and `MerchantAccount` response route: `# Sub-merchant Account > ### Attributes`, lines 29-31.
- Declined-event additional-attribute navigation to Braintree Marketplace onboarding: `# Sub-merchant Account > ### Attributes`, line 33.

## Evidence limitations

> [!warning] Event notification is not an account operation
> This page establishes only that a sub-merchant approval or decline event triggered a webhook. It does not document account creation, submission, activation, funding readiness, transaction eligibility, approval criteria, decline reasons, or the timing of an onboarding decision.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-webhooks]]
- Webhook purpose and delivery setup: [[source-braintree-webhooks-overview]]
- Separate Node.js merchant-account creation reference: [[source-braintree-merchant-account-create-node]]

## Related raw API references

- [[raw/braintree/docs/guides/braintree-marketplace/confirmation/node-2026-09-16|Braintree Marketplace sub-merchant onboarding confirmation guide]] - navigation-only route for additional declined-webhook attributes; not used as factual evidence here

## Raw Sources

- [[raw/braintree/docs/reference/general/webhooks/sub-merchant-account/node-2026-09-16|Braintree Node.js sub-merchant account webhook reference]] - complete collected page covering approval and decline notification kinds plus payload routes
