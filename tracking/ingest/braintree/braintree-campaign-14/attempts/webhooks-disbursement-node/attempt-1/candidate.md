---
title: "Braintree Disbursement Webhooks (Node.js)"
type: source
date_ingested: 2026-09-22
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/general/webhooks/disbursement/node"
raw_files:
  - "braintree/docs/reference/general/webhooks/disbursement/node-2026-09-16.md"
tags: [braintree, node-js, webhooks, disbursements, merchant-accounts]
---

## Overview

This Braintree Node.js reference distinguishes two disbursement webhook notification kinds and the conditions that trigger them. Both are limited to merchant accounts whose funding Braintree manages, and the page's bank-departure wording does not establish when a merchant receives funds.

## Key takeaways

- Calling `kind` on the notification object identifies what triggered the webhook. The page documents `disbursement` and the deprecated `transaction_disbursed` kind.
- `disbursement` means Braintree has sent a disbursement to the account, stated as leaving Braintree's bank account that day. It is sent once per merchant account per day rather than once per transaction.
- The deprecated `transaction_disbursed` kind means a transaction has been marked for disbursement, also stated as leaving Braintree's bank account that day.
- Both notification kinds are for Braintree-funded merchant accounts only. The page further says a merchant receives a disbursement webhook only when Braintree manages funding for the selected merchant account; availability of Disbursement Summary reports is the stated indicator.
- The concatenated attributes section identifies payload categories for notification kind and trigger time, disbursement identity, amount, date and debit/credit type, associated transaction IDs, merchant account, and retry/success indicators. The exact attribute presentation remains in the pinned raw.

## Detail locators

- Notification-object `kind` purpose and event-kind scope: `# Disbursement > ### Notification kinds`, lines 17-21.
- `disbursement` event condition and per-account-per-day boundary: notification table, lines 23-30.
- Deprecated `transaction_disbursed` event condition: notification table, lines 31-33.
- Payload categories, Braintree-managed funding qualification, report-availability indicator and retry/success indicator prose: `# Disbursement > ### Attributes`, lines 36-38.

## Evidence limitations

> [!warning] Bank departure is not merchant receipt
> The page says the disbursement or marked transaction will leave Braintree's bank account that day. It does not promise merchant receipt that day, provide arrival timing, establish settlement finality, or guarantee a payout outcome. The collected attributes prose is concatenated, so this source preserves broad payload categories without reconstructing property names or structure.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-webhooks]]
- Webhook purpose and delivery setup: [[source-braintree-webhooks-overview]]
- Node.js parsing and delivery-response behavior: [[source-braintree-webhooks-parse-node]]

## Raw Sources

- [[raw/braintree/docs/reference/general/webhooks/disbursement/node-2026-09-16|Braintree Node.js disbursement webhook reference]] - complete collected page covering notification kinds, trigger conditions, funding qualification and payload categories
