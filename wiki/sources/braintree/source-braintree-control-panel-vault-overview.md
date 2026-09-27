---
title: "Braintree Control Panel Vault Overview"
type: source
date_ingested: 2026-09-27
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/control-panel/vault/overview"
raw_files:
  - "braintree/articles/control-panel/vault/overview-2026-09-16.md"
tags: [braintree, control-panel, vault, customers, payment-methods, tokenization]
---

## Overview

This collected Braintree article introduces the Vault as storage for customer and payment-method information used for recurring or non-recurring transactions. It describes encrypted payment-method storage, token-based transaction creation, high-level customer-record administration, Control Panel exports and a statement-label caveat; it is not a procedural guide for creating or updating customers or for card verification.

## Key takeaways

- Braintree presents the Vault as a way to keep customers and their payment-method information on file. The page says Vault records can support recurring billing and non-recurring transactions without requiring customers to re-enter their information for each purchase.
- When a payment method is stored, the gateway encrypts its information and associates it with a unique payment-method token that can be used to create transactions. The page also says a stored customer Vault record can be updated, deleted or searched, but it does not document those procedures, their permissions or their outcomes.
- Braintree says it never stores a customer's CVV in the Vault because card associations prohibit that storage. The token and PCI wording on this collected page must not be broadened into a general compliance guarantee.
- From the Control Panel's **Reports** area, the article routes exports for customers, customers with payment-method tokens, and customers with addresses. Vault exports are limited to 40,000 rows, and the page warns that opening the download in Excel or another spreadsheet program can omit rows because of that program's limitations.
- A transaction created from a Vault record may sometimes be passed with a recurring ecommerce indicator because CVV cannot accompany that transaction. The article says a bank may display that indicator on a customer statement, but it does not necessarily mean the customer was enrolled in future recurring payments.

> [!warning] Overview and collected-snapshot boundary
> This article establishes overview-level Vault purpose, tokenization, export and statement-label facts only. It does not establish the steps, prerequisites, supported payment methods or outcomes for the separately documented Create New Customers, Update Customer Information or Card Verification actions. Treat the 2026-09-16 snapshot as collected evidence, not confirmation of current product support, permissions or behavior.

## Detail locators

- Vault purpose and recurring versus non-recurring use: `# Overview`, lines 16-18.
- Encryption, unique payment-method token, transaction creation and high-level update/delete/search scope: `## How it works`, lines 23-25.
- Never-store-CVV warning: note under `## How it works`, lines 28-29.
- Exported record categories and Control Panel Reports route: `## Exporting Vault records`, lines 36-51.
- Export row limit and spreadsheet omission warning: note under `## Exporting Vault records`, lines 54-55.
- Recurring ECI statement display and no-future-enrollment clarification: `## Charge shows as recurring on customer statement`, lines 60-62.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-control-panel]]
- Related concept: [[recurring-payments]]

## Related raw API references

- [[raw/braintree/articles/control-panel/vault/create-2026-09-16|Braintree Control Panel Create New Customers article]] - unread navigation-only route for customer-record creation; not used as factual evidence here
- [[raw/braintree/articles/control-panel/vault/update-2026-09-16|Braintree Control Panel Update Customer Information article]] - unread navigation-only route for customer, payment-method and address update details; not used as factual evidence here
- [[raw/braintree/articles/control-panel/vault/card-verification-2026-09-16|Braintree Control Panel Card Verification article]] - unread navigation-only route for verification purpose, access and outcomes; not used as factual evidence here
- [[raw/braintree/articles/guides/recurring-billing/overview-2026-09-16|Braintree Recurring Billing overview]] - unread navigation-only route linked by the article; not used as factual evidence here
- [[raw/braintree/articles/risk-and-security/compliance/pci-compliance-2026-09-16|Braintree PCI Compliance article]] - unread navigation-only route linked by the article; not used as factual evidence here

## Raw Sources

- [[raw/braintree/articles/control-panel/vault/overview-2026-09-16|Braintree Control Panel Vault Overview article]] - complete collected page covering Vault purpose, encrypted tokenized storage, high-level record administration, exports, CVV non-retention and the recurring-indicator statement caveat
