---
title: "Braintree Local Payment Method Webhooks (Node.js)"
type: source
date_ingested: 2026-09-21
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/general/webhooks/local-payment-methods/node"
raw_files:
  - "braintree/docs/reference/general/webhooks/local-payment-methods/node-2026-09-16.md"
tags: [braintree, node-js, webhooks, local-payment-methods]
---

## Overview

This Braintree Node.js reference distinguishes webhook events for instant and non-instant local payments. For the instant-payment completion event, transaction creation is a separate follow-on `Transaction: Sale` call using the supplied payment-method nonce; the webhook does not itself establish that a transaction was created.

## Key takeaways

- `local_payment_completed` means the customer approved an instant local payment and the purchase amount was withdrawn. The page says a transaction can then be created by calling `Transaction: Sale` with the `payment_method_nonce`; it does not state that the webhook automatically creates that transaction.
- `local_payment_reversed` reports that an instant local payment was reversed and the purchase amount refunded to the customer's account.
- Non-instant methods use `local_payment_funded` when the buyer has completed the payment and `local_payment_expired` when it has expired. These event descriptions do not import the instant flow's separate nonce-based transaction-creation action.
- The attributes section routes payment/order correlation, payment-context, nonce, payer/bank and transaction categories, with several values explicitly limited to `local_payment_completed`. Because the collected rendering concatenates field descriptions and leaves the field owning the displayed `Authorized` and `Settled` values unnamed, use the raw locator rather than reconstructing a payload schema.

## Detail locators

- Notification-kind purpose: `# Local Payment Methods > ### Notification kinds`, lines 17-21.
- Instant completion, separate sale call and nonce guidance: `# Local Payment Methods > ### Notification kinds`, line 25.
- Instant reversal condition: `# Local Payment Methods > ### Notification kinds`, line 26.
- Non-instant funded and expired conditions: `# Local Payment Methods > ### Notification kinds`, lines 27-28.
- Payload categories, completion-only qualifications and unreconstructed trailing values: `# Local Payment Methods > ### Attributes`, lines 31-36.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-webhooks]]

## Related raw API references

- [[raw/braintree/docs/guides/webhooks/parse/node-2026-09-16|Braintree Node.js webhook parsing guide]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/reference/request/transaction/sale/node-2026-09-16|Braintree Node.js Transaction Sale request reference]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/guides/local-payment-methods/overview-2026-09-16|Braintree local payment methods overview]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/articles/guides/payment-methods/local-payment-methods-2026-09-16|Braintree local payment methods and payment-context article]] - navigation only; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/reference/general/webhooks/local-payment-methods/node-2026-09-16|Braintree Node.js local-payment-method webhook reference]] - complete collected page covering instant completion and reversal, non-instant funding and expiry, separate transaction creation, and payload categories
