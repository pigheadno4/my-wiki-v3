---
title: "Braintree Control Panel: Clone Transactions"
type: source
date_ingested: 2026-09-23
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/control-panel/transactions/clone"
raw_files:
  - "braintree/articles/control-panel/transactions/clone-2026-09-16.md"
tags: [braintree, control-panel, transactions, cloning, payment-methods, settlement]
---

## Overview

This collected Braintree article documents cloning an existing transaction in the Control Panel. It describes copying transaction information, including the payment method, into a new transaction workflow while identifying payment-method, Vault-origin, status, permission, CVV, and settlement-submission boundaries. This is a Control Panel action, not the server SDK/API clone operation.

## Key takeaways

- The article describes cloning as copying information from an existing transaction, including its payment method. Its opening says the amount is the only information the merchant must provide when the original transaction is compatible, while the later procedure separately instructs the merchant to enter the amount and CVV if applicable; the remaining information is automatically filled in.
- Most transactions are described as cloneable, but an original transaction is ineligible if it was processed through PayPal, Apple Pay, Google Pay, or Venmo; was created from a Vault record; or has `Processor Declined`, `Failed`, `Gateway Rejected`, or `Settling` status. For a Vault-origin transaction, the article routes the merchant to create a new transaction from the Vault record instead.
- The gateway-rejection exclusion has a narrow exception: a transaction rejected for a Fraud or Risk Threshold reason can be cloned when a legitimate transaction was mistakenly rejected as fraudulent. The page does not extend that exception to other gateway-rejection reasons or other excluded statuses.
- In the Control Panel procedure, the merchant enters the new transaction's amount and CVV if applicable. For an authorization, the merchant is instructed to clear `Submit for Settlement`; this separates authorization-only creation from settlement submission and does not establish final settlement or funding.
- If an otherwise eligible transaction does not display the clone option, the article directs the merchant to check that the Control Panel user's role has both **Create Sales** and **Submit Sales for Settlement** permissions.
- When CVV rules are enabled, a merchant who wants a CVV check must enter the CVV under **Payment Information**. If no CVV is included, Braintree says it will not check CVV, regardless of whether CVV rules are enabled.

> [!warning] Collected eligibility and lifecycle boundaries
> This page was fetched on 2026-09-16 and does not prove current payment-method support, role behavior, or merchant eligibility. Preserve the listed exclusions and the narrow fraud/risk gateway-rejection exception, and do not treat transaction creation or settlement submission as proof of final settlement or funding.

## Detail locators

- Copy purpose, included payment method, automatic fill, and amount premise: `# Clone Transactions`, lines 16-18.
- Payment-method, Vault-origin, and transaction-status exclusions: `## Compatibility`, lines 23-28.
- Fraud/Risk Threshold gateway-rejection exception: `## Compatibility`, line 30.
- Control Panel search, clone, amount/CVV entry, authorization-only settlement choice, and creation steps: `## Cloning a transaction`, lines 35-48.
- Required Control Panel role permissions when the clone option is absent: `## Cloning a transaction > NOTE`, lines 51-52.
- CVV-entry and no-CVV/no-check behavior: `## Checking CVV on cloned transactions`, lines 57-59.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-control-panel]]

## Related raw API references

- [[raw/braintree/docs/reference/request/transaction/clone_transaction/node-2026-09-16|Transaction Clone Transaction (Node.js)]] - unread navigation-only route for the distinct server SDK/API operation; not used as factual evidence here
- [[raw/braintree/articles/control-panel/transactions/create-2026-09-16|Control Panel Create Transactions]] - unread navigation-only route for creating a transaction from a Vault record; not used as factual evidence here
- [[raw/braintree/articles/control-panel/transactions/gateway-rejections-2026-09-16|Control Panel Gateway Rejections]] - unread navigation-only route for gateway-rejection reasons; not used as factual evidence here
- [[raw/braintree/articles/control-panel/users-roles/role-permissions-2026-09-16|Control Panel Role Permissions]] - unread navigation-only route for permission details; not used as factual evidence here
- [[raw/braintree/articles/guides/fraud-tools/basic/avs-cvv-rules-2026-09-16|AVS and CVV Rules]] - unread navigation-only route for CVV-rule configuration; not used as factual evidence here

## Raw Sources

- [[raw/braintree/articles/control-panel/transactions/clone-2026-09-16|Braintree Control Panel Clone Transactions article]] - complete collected page covering copied information, compatibility exclusions, the fraud/risk exception, Control Panel steps, role permissions, CVV handling, and the authorization settlement-submission choice
