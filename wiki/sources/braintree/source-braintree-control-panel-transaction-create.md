---
title: "Braintree Control Panel: Create Transactions"
type: source
date_ingested: 2026-09-23
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/control-panel/transactions/create"
raw_files:
  - "braintree/articles/control-panel/transactions/create-2026-09-16.md"
tags: [braintree, control-panel, transactions, vault, authorization, settlement]
---

## Overview

This collected Braintree article explains when a merchant can manually create a transaction in the Control Panel, while recommending the API as the normal creation route. It distinguishes new-card and vaulted-payment-method eligibility and identifies authorization and settlement-submission controls without establishing final settlement or funding.

## Key takeaways

- Braintree recommends creating transactions through the API, but the article permits manual creation in the Control Panel when necessary. This page documents the Control Panel workflow, not an API or SDK transaction-creation operation.
- Credit- and debit-card transactions can use either a new card or one already stored in the Vault. Other payment types, with PayPal and Apple Pay given as examples, must already be stored in the Vault before a merchant can use them to create a Control Panel transaction.
- The collected page warns that a transaction cannot be settled for more than its authorized amount unless the merchant's industry and processor support settlement adjustment; it directs merchants to Braintree for more information rather than establishing general adjustment eligibility.
- For an existing Vault customer, the merchant can charge the default payment method or select another stored payment-method token. Exact Control Panel steps and fields remain at the raw locators.
- To create an authorization from an existing Vault record, the article instructs the merchant to clear `Submit for Settlement`. Selecting submission is a request to enter the settlement flow; this page does not say that transaction creation, submission, or a checked control proves final settlement or merchant funding.

> [!warning] Collected eligibility and lifecycle boundaries
> The page was fetched on 2026-09-16 and does not prove current payment-method support, merchant eligibility, or processor capabilities. Confirm current availability with Braintree, preserve the industry-and-processor qualification for settlement adjustment, and keep authorization, settlement submission, final settlement, and funding distinct.

## Detail locators

- API recommendation and manual Control Panel alternative: `# Create Transactions`, line 16.
- New-card versus Vault eligibility and the stored-method prerequisite for other payment types: `# Create Transactions`, line 18.
- Authorized-amount ceiling and industry/processor-qualified settlement-adjustment exception: `# Create Transactions > NOTE`, lines 21-22.
- New-card Control Panel creation and optional Vault-storage steps: `## On a new credit card`, lines 27-39.
- Existing-customer default-method and alternate-token selection: `## On an existing Vault record`, lines 42-52.
- Authorization-only Control Panel choice, transaction creation, and alternate Vault navigation: `## On an existing Vault record`, lines 55-61.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-control-panel]]
- API/SDK context: [[braintree-server-sdk]]

## Related raw API references

- [[raw/braintree/docs/guides/transactions/node-2026-09-16|Braintree Transactions guide for Node.js]] - unread navigation-only route for the recommended API/SDK transaction lifecycle; not used as factual evidence here
- [[raw/braintree/docs/reference/request/transaction/sale/node-2026-09-16|Transaction Sale (Node.js)]] - unread navigation-only transaction-creation request reference; not used as factual evidence here
- [[raw/braintree/docs/reference/request/transaction/submit-for-settlement/node-2026-09-16|Transaction Submit for Settlement (Node.js)]] - unread navigation-only settlement-submission request reference; not used as factual evidence here

## Raw Sources

- [[raw/braintree/articles/control-panel/transactions/create-2026-09-16|Braintree Control Panel Create Transactions article]] - complete collected page covering manual transaction creation, payment-method eligibility, Vault selection, authorization-only creation, and the settlement-adjustment boundary
