---
title: "Braintree Marketplace: Creating Transactions with Service Fees (Node.js)"
type: source
date_ingested: 2026-09-30
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/braintree-marketplace/create/node"
raw_files:
  - "braintree/docs/guides/braintree-marketplace/create/node-2026-09-16.md"
tags: [braintree, marketplace, node-js, transactions, service-fees, sub-merchants, escrow]
---

## Overview

This collected Braintree Marketplace guide documents the Node.js route for a master merchant to create a transaction attributed to a successfully onboarded sub-merchant and collect a service fee through `gateway.transaction.sale()`. It preserves the account-attribution, device-data, fee, escrow, refund, verification and charge-responsibility conditions needed to use the route safely; the snapshot does not establish current Marketplace availability or merchant eligibility.

## Key takeaways

- The guide places transaction creation after successful sub-merchant onboarding. For each transaction, it calls correct `merchantAccountId` selection critical because that value determines the sub-merchant to which the transaction is attributed; it also instructs the merchant to collect client device data and include it in the transaction.
- The Node.js example submits `merchantAccountId`, amount, payment-method nonce, device data and `serviceFeeAmount` through `gateway.transaction.sale()`. The page says the service fee is required, cannot be empty, and may range from zero through the total transaction amount.
- The service fee is deducted from the final amount disbursed to the sub-merchant and sent to the master merchant. This is a fee-allocation statement, not evidence that the transaction succeeded, settled or was disbursed.
- Although the guide says Braintree does not escrow funds, it describes an optional Marketplace hold on a sub-merchant's transaction funds until a separate release call, available at or after transaction creation. A full refund while funds are held pulls the full amount from the hold and returns it to the customer; partial refunds are unsupported until release.
- Credit-card verification must use the master merchant account or a merchant-of-record account; using a sub-merchant account as `verification_merchant_account_id` produces a validation error. The guide also assigns transaction processing fees, chargebacks, chargeback fees and, unless funds are being held, refunds to the master merchant account.

## Evidence boundaries

> [!warning] Availability and onboarding boundary
> New merchants seeking a marketplace solution are directed to Braintree Sales. Collection of this guide does not prove current Marketplace availability, eligibility or enablement, and the transaction route applies only after the sub-merchant has been successfully onboarded.

> [!warning] Attribution and device-data prerequisites
> Preserve the page's sub-merchant account attribution and client device-data instructions. Do not generalize the example into a transaction for the master account or treat the displayed callback as proof of authorization, settlement or disbursement.

> [!warning] Held-funds and refund limitation
> The guide's own terminology says Braintree does not escrow funds while describing a Marketplace hold until a separate release call. Do not omit the full-refund effect or imply that partial refunds are supported before release.

## Detail locators

- New-merchant Sales route and successful-onboarding prerequisite: opening `**AVAILABILITY**` and introductory feature list, lines 17-24.
- Correct sub-merchant account attribution and client device-data instructions: `## Creating transactions without escrow`, lines 27-30.
- Node.js `gateway.transaction.sale()` example and displayed request categories: `## Creating transactions without escrow > ### Node`, lines 31-42.
- Required, nonempty service-fee range, disbursement allocation and dynamic-descriptor route: `## Creating transactions without escrow`, lines 43-45.
- Optional hold, separate release call, hold timing and processing-article route: `## Holding funds in escrow`, lines 46-51.
- Full-refund effect and no partial refunds before release: `## Holding funds in escrow > ### Refunds`, lines 52-56.
- Master-or-merchant-of-record verification account requirement and sub-merchant validation error: `## Verifications`, lines 57-60.
- Charges and fees deducted from the master merchant account: `## Other charges and fees`, lines 61-69.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-marketplace]]
- Node gateway context: [[braintree-server-sdk]]
- Separate hold operation: [[source-braintree-transaction-hold-in-escrow-node]]
- Separate release operation: [[source-braintree-transaction-release-from-escrow-node]]

## Related raw API references

- [[raw/braintree/docs/reference/request/transaction/sale/node-2026-09-16|Braintree Transaction Sale reference - Node.js]] - unread navigation-only route for the dedicated sale request and Marketplace options; no additional behavior is imported here
- [[raw/braintree/docs/reference/request/transaction/hold-in-escrow/node-2026-09-16|Braintree Hold in Escrow reference - Node.js]] - unread navigation-only route for the separate post-creation hold call; no additional behavior is imported here
- [[raw/braintree/docs/reference/request/transaction/release-from-escrow/node-2026-09-16|Braintree Release from Escrow reference - Node.js]] - unread navigation-only route for the separate release call; no additional behavior is imported here
- [[raw/braintree/articles/guides/braintree-marketplace/processing-2026-09-16|Braintree Marketplace processing article]] - unread navigation-only article route; no processing or funding behavior is imported here

## Raw Sources

- [[raw/braintree/docs/guides/braintree-marketplace/create/node-2026-09-16|Braintree Marketplace create guide - Node.js]] - complete collected guide covering sub-merchant transaction attribution, service-fee allocation, device-data instructions, held-funds and refund constraints, verification-account scope, and master-merchant charges
