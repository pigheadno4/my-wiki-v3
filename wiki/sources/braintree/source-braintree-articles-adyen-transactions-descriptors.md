---
title: "Braintree Adyen Transaction Descriptors"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/adyen/transactions/descriptors"
raw_files:
  - "braintree/articles/adyen/transactions/descriptors-2026-09-16.md"
tags: [braintree, adyen, descriptors, transactions, bank-statements, amex]
---

## Overview

This collected Braintree-owned article, filed under its Adyen processor documentation, describes statement descriptors for the Braintree account in scope. It distinguishes the post-settlement hard descriptor from a per-transaction dynamic descriptor while leaving the exact customer-statement presentation to the customer's bank. This is not independent Adyen API or PayPal Orchestration documentation.

## Key takeaways

- The hard descriptor appears after a transaction settles and remains as the charge description once the customer's bank finalizes the transaction status. A dynamic descriptor is custom information passed with each transaction through the API.
- Merchant name and merchant city are required descriptor parameters. The article says Braintree automatically configured the account's hard descriptor from application information; changing it requires the account's authorized signer to contact Braintree with the fields and desired values. The authorized signer is distinct from an Account Admin role and cannot be managed in the Control Panel.
- For a dynamic descriptor, Braintree obtains the location from the application information rather than requiring it on the transaction. The raw section lists the permitted descriptor-name contents and character rules and warns that many banks truncate names at 22 characters.
- For American Express transactions using Adyen's aggregated Amex account, the article says dynamic descriptors are unsupported and the hard descriptor is passed by default when dynamic descriptors are enabled. Merchants processing through their own Amex account are instead directed to configure dynamic descriptors with Amex.

> [!warning] Scope and presentation boundaries
> This Braintree snapshot gives no general regional or pricing-model eligibility statement; the illustrated currency is not eligibility evidence. A customer's bank controls the final statement display, and the captured page is not proof of current support for a particular account. Do not transfer these descriptor rules or Amex account conditions to another processor.

## Detail locators

- Descriptor purpose, bank-controlled presentation and example: `# Descriptors`, lines 16-18.
- Hard and dynamic descriptor definitions: `# Descriptors`, lines 20-26.
- Required merchant-name/city fields and hard-descriptor change route: `## Configuring descriptors`, lines 29-37.
- Authorized-signer identity, Account Admin distinction and identity-confirmation note: `### Authorized signer`, lines 40-48.
- Hard-descriptor merchant-name and merchant-city constraints: `## Hard descriptor requirements`, lines 53-69.
- Dynamic location handling, name-field constraints, bank truncation warning and linked developer-doc route: `## Dynamic descriptor requirements`, lines 72-88.
- Aggregated-account versus own-account American Express behavior: `### Special note on Amex`, lines 91-95.

## Related

- Company: [[braintree]]
- Account administration concept: [[braintree-control-panel]]
- Transaction API/SDK concept: [[braintree-server-sdk]]

## Raw Sources

- [[raw/braintree/articles/adyen/transactions/descriptors-2026-09-16|Braintree Adyen Transaction Descriptors]] - complete collected article covering account descriptor configuration, statement presentation and Amex account qualifications
