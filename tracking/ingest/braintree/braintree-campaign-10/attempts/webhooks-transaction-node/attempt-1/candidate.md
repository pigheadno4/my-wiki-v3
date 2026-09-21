---
title: "Braintree Transaction Webhooks (Node.js)"
type: source
date_ingested: 2026-09-21
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/general/webhooks/transaction/node"
raw_files:
  - "braintree/docs/reference/general/webhooks/transaction/node-2026-09-16.md"
tags: [braintree, node-js, webhooks, transactions, ach, sepa-direct-debit]
---

## Overview

This Braintree Node.js reference documents two transaction webhook notification kinds and limits the stated availability to ACH and SEPA Direct Debit requests. The collected availability sentence and attribute rendering are damaged, so this source retains only the unambiguous payment-method names, event conditions, and payload categories.

## Key takeaways

- The availability line explicitly names ACH and SEPA Direct Debit requests, but it ends with the malformed text `Direct Debitandrequests`. This source does not reconstruct a missing payment method, operation, link, or qualification and does not extend transaction webhooks to all Braintree transactions.
- `webhook_notification.kind` identifies the trigger. The retained table lists `transaction_settlement_declined` when settlement for the transaction was declined and `transaction_settled` when the transaction successfully settled.
- The page says `transaction_settlement_declined` may occur after `transaction_settled` if the customer's bank "returns the refund after it has appeared to settle." That unusual wording is preserved as source-specific text rather than normalized into a broader return, reversal, or finality rule.
- The Attributes section is concatenated and supplies no visible attribute names. It indicates only the categories: notification kind, UTC trigger date/time, and an associated Braintree Transaction object. It does not establish the object's field inventory or universal webhook delivery, ordering, retry, duplication, parsing, or finality behavior.

## Detail locators

- Payment-method availability and damaged trailing prose: `# Transaction > **AVAILABILITY**`, lines 17-18.
- Notification-kind trigger role: `### Notification kinds`, lines 21-25.
- `transaction_settlement_declined`, its qualified post-settled possibility, and `transaction_settled`: notification table, lines 27-39.
- Concatenated payload categories with missing visible attribute names: `### Attributes`, lines 42-44.

## Evidence limitations

> [!warning] Damaged availability and attribute rendering
> The collected page does not support reconstructing the text after `SEPA Direct Debit`, any additional payment method or operation, or the missing attribute labels. The dedicated page adds SEPA Direct Debit to the existing overview's ACH route without contradicting that overview; neither page establishes universal transaction-webhook support.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-webhooks]]

## Raw Sources

- [[raw/braintree/docs/reference/general/webhooks/transaction/node-2026-09-16|Braintree Node.js transaction-webhook reference]] - complete page covering payment-method availability, two settlement notification kinds, their stated trigger conditions, and damaged attribute rendering
