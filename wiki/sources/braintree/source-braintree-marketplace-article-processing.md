---
title: "Braintree Marketplace Processing"
type: source
date_ingested: 2026-09-30
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/guides/braintree-marketplace/processing"
raw_files:
  - "braintree/articles/guides/braintree-marketplace/processing-2026-09-16.md"
tags: [braintree, marketplace, processing, service-fees, escrow, refunds, disputes]
---

## Overview

This collected Braintree Marketplace article describes Marketplace-specific transaction handling: allocating service fees between a master merchant and sub-merchant, holding and releasing whole transactions in escrow, and assigning refund and dispute costs. It is not a generic Braintree processing guide, and the collected snapshot does not prove current Marketplace availability or merchant eligibility.

## Key takeaways

- A service fee routes part of a sub-merchant transaction's revenue to the master merchant account, with the remainder disbursed to the sub-merchant. If the Braintree transaction fee exceeds the service fee, Braintree says it first uses settled funds in the master merchant account and then debits the master merchant's bank account for any remainder.
- The master merchant must request an escrow hold through the API either when creating the transaction or before submitting it for settlement. Escrow holds the transaction until an API release, and the entire transaction, including its service fee, must be held and released together; partial disbursements require separate transactions. Braintree recommends not holding funds in escrow for longer than 30 days.
- While funds are in escrow, a refund pulls the full transaction amount from escrow and partial refunds are unavailable until release. Outside escrow, full and partial refunds are available, but the article says the refund is deducted from the master merchant bank account rather than the sub-merchant funding source.
- Chargebacks or retrievals against sub-merchant transactions, including associated fees, are likewise deducted from the master merchant bank account. The article routes recoupment approaches to its final section; those suggestions do not change who Braintree says it debits.

> [!warning] Availability and scope boundary
> New merchants seeking a marketplace solution are directed to Braintree Sales. This collected article documents Marketplace-specific allocation, escrow, refund, and dispute behavior; it does not establish current support, eligibility, settlement of a particular transaction, or a generic Braintree processing model.

## Detail locators

- New-merchant Marketplace Sales route: opening `AVAILABILITY`, lines 17-18.
- Service-fee purpose, transaction-creation routes, worked allocation example, and fee-shortfall funding order: `## Service fees`, lines 23-31.
- Escrow purpose, hold and release timing, whole-transaction rule, partial-disbursement workaround, funding-timeline route, and 30-day recommendation: `## Escrow`, lines 36-46.
- Escrow-sensitive full and partial refund behavior and master-merchant debit responsibility: `## Refunds`, lines 51-55.
- Chargeback/retrieval notification and debit responsibility: `## Disputes`, lines 58-60.
- Suggested recoupment approaches, including integration logic and Vault storage: `## Collecting funds from your sub-merchants`, lines 63-70.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-marketplace]]

## Related raw API references

- [[raw/braintree/docs/guides/braintree-marketplace/create/node-2026-09-16|Braintree Marketplace transaction creation guide - Node.js]] - unread navigation-only route for API creation details; no Node-specific behavior is imported here
- [[raw/braintree/docs/reference/request/transaction/release-from-escrow/node-2026-09-16|Braintree release-from-escrow reference - Node.js]] - unread navigation-only operation reference; no additional release behavior is imported here
- [[raw/braintree/articles/risk-and-security/chargebacks-retrievals/overview-2026-09-16|Braintree chargebacks and retrievals overview]] - unread navigation-only risk reference; no broader dispute behavior is imported here

## Raw Sources

- [[raw/braintree/articles/guides/braintree-marketplace/processing-2026-09-16|Braintree Marketplace processing article]] - complete collected article covering service fees, escrow, refunds, disputes, and master-merchant recoupment suggestions
