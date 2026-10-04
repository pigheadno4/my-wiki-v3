---
title: "Braintree Moneris Transaction Descriptors"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/moneris/transactions/descriptors"
raw_files:
  - "braintree/articles/moneris/transactions/descriptors-2026-09-16.md"
tags: [braintree, moneris, transactions, descriptors, bank-statements]
---

## Overview

This Braintree-hosted, Moneris-routed snapshot explains the identifying information customers may see on bank statements for purchases made through a merchant's mobile app or website. For the account addressed by the article, it distinguishes an automatically configured hard descriptor from an API-supplied dynamic descriptor; the customer's bank ultimately determines the exact rendering. This is account-route documentation from [[braintree]], not independent Moneris API documentation or PayPal Orchestration authority.

## Key takeaways

- The article says the account supports hard and dynamic descriptors. A hard descriptor is displayed after settlement once the customer's bank finalizes the transaction status, while a dynamic descriptor is custom information passed with each transaction through the API.
- Hard descriptor information requires merchant name (DBA), location and phone number. The phone number is not shown in the hard descriptor by default, and the article routes assistance and descriptor changes through Braintree's contact path.
- The merchant name/DBA is limited to 22 characters and to letters, numbers, periods and dashes. The article says Braintree automatically configured the hard descriptor from application information.
- Depending on the card issuer, a statement will typically append the dynamic descriptor name to the DBA with a forward slash. The DBA, slash and dynamic name share a 22-character limit; exceeding it can cause truncation or reversion to the hard descriptor. Dynamic names cannot contain spaces or special characters.
- The linked per-transaction developer-doc route supports only the `name` field in this snapshot; phone and URL are not supported there. PayPal descriptor updates use the PayPal console, while Amex descriptor updates require direct contact with American Express.

> [!warning] Scope and statement-rendering boundaries
> This is a 2026-09-16 snapshot of a Braintree article under its Moneris account route. It does not establish current availability, a merchant's account or regional eligibility, independent Moneris requirements, API request shape, Orchestration behavior, or successful payment processing. Do not transfer its rules to sibling account, processor, region or payment-method routes. The issuing bank controls exact statement rendering, and the article uses qualified language for the typical dynamic format and the possible truncation-or-reversion outcome.

## Detail locators

- Descriptor purpose, mobile-app or website context, bank-controlled rendering and example: `# Descriptors`, raw lines 14-18.
- Hard and dynamic descriptor definitions: `# Descriptors`, raw lines 20-24.
- Required hard-descriptor parameters, default phone-number visibility and merchant-name restrictions: `# Descriptors`, raw lines 26-37.
- Application-derived hard configuration, Braintree change route and separate PayPal/Amex routes: `# Descriptors`, raw lines 41-47.
- Dynamic descriptor composition, issuer-qualified typical rendering and shared 22-character limit: `## Dynamic descriptors`, raw lines 52-67.
- Dynamic-name character restrictions and identification guidance: `### Dynamic descriptor name`, raw lines 72-81.
- Overlength truncation-or-reversion possibility and the per-transaction developer-doc field boundary: `### Dynamic descriptor name`, raw lines 84-89.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-control-panel]]
- General Braintree descriptor route: [[source-braintree-control-panel-descriptors]]

## Raw Sources

- [[raw/braintree/articles/moneris/transactions/descriptors-2026-09-16|Braintree Moneris Transaction Descriptors]] - complete collected Braintree article for the Moneris-routed hard and dynamic descriptor snapshot
