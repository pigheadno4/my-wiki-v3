---
title: "Braintree Transaction Lifecycle"
type: source
date_ingested: 2026-09-23
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/get-started/transaction-lifecycle"
raw_files:
  - "braintree/articles/get-started/transaction-lifecycle-2026-09-16.md"
tags: [braintree, transactions, authorization, settlement, transaction-statuses]
---

## Overview

This collected Braintree article explains the status sequence it documents for a successful transaction as money travels from the customer toward the merchant's bank account. It distinguishes authorization, settlement submission, processor settlement work, and settled status so those stages are not collapsed into one event.

## Key takeaways

- `Authorized` means the customer's bank approved the initial payment-method and sufficient-funds check. The authorization places a hold on the customer's funds but does not remove them.
- `Submitted for Settlement` means the process of removing money from the customer's account has been initiated. The article says authorization eventually expires, submission is needed to collect funds, and submission happens by default for transactions created through the Control Panel; it also calls this status "captured or capturing" in payments-industry usage. Submission is still a distinct stage from `Settling` and `Settled`.
- `Settling` begins when Braintree starts communicating with the processor about the settlement request. Time in this state depends on the processing bank.
- `Settled` is displayed once the article says the money has moved from the customer's bank through the merchant account and hit the merchant account; the funds are then routed to the merchant's bank account. The page does not document the timing of arrival in that bank account, so `Settled` should not be presented as proof of completed bank funding.
- Unsuccessful or interrupted transactions can have other statuses. This article does not enumerate them; it routes readers to the separate transaction-status reference.

> [!warning] Keep lifecycle stages distinct
> An authorization is a hold rather than removal of funds. Submission initiates settlement processing, `Settling` identifies processor communication, and `Settled` identifies the later merchant-account stage described by this page. The 2026-09-16 collected snapshot does not prove current timing, support, or funding behavior beyond the article's statements.

## Detail locators

- Successful-transaction sequence and status purpose: `# Transaction Lifecycle`, lines 16-20.
- Bank approval, sufficient-funds check, authorization status, and hold-without-removal boundary: `## Authorized`, lines 23-25.
- Authorization expiry, collection requirement, Control Panel default, and initiation of funds removal: `## Submitted for Settlement`, lines 28-32.
- Processor communication and processing-bank-dependent duration: `## Settling`, lines 35-37.
- Merchant-account movement, settled display, and routing toward the bank account: `## Settled`, lines 40-42.
- Unsuccessful or interrupted transaction route to the full status reference: `## Other statuses`, lines 45-47.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]

## Related raw API references

- [[raw/braintree/docs/reference/general/statuses-2026-09-16|Braintree transaction-status reference]] - unread navigation-only destination for the article's complete-status link; not used as factual evidence here
- [[raw/braintree/articles/control-panel/transactions/managing-authorizations-2026-09-16|Braintree Managing Authorizations article]] - unread navigation-only destination for authorization timing and delayed-submission guidance; not used as factual evidence here

## Raw Sources

- [[raw/braintree/articles/get-started/transaction-lifecycle-2026-09-16|Braintree Transaction Lifecycle article]] - complete collected page covering Authorized, Submitted for Settlement, Settling, Settled, and the route to other statuses
