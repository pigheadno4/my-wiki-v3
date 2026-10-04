---
title: "Braintree AIB AF Transaction Descriptors"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/aib-af/transactions/descriptors"
raw_files:
  - "braintree/articles/aib-af/transactions/descriptors-2026-09-16.md"
tags: [braintree, aib-af, transactions, descriptors, bank-statements]
---

## Overview

This collected Braintree-owned article, filed under its AIB AF documentation path, explains the statement descriptors associated with purchases through a merchant's mobile app or website. It distinguishes soft, hard and per-transaction dynamic descriptors while leaving the exact customer-statement presentation to the customer's bank.

## Key takeaways

- A soft descriptor appears after authorization while a charge is pending; a hard descriptor appears after settlement and remains as the charge description once the customer's bank finalizes the transaction status. A dynamic descriptor is custom information configured and passed with each transaction through the API.
- Merchant name (trading name) and clearing city or phone number are required descriptor information. The article says Braintree automatically configured the account's hard and soft descriptors from application information and routes changes through a Braintree contact path; exact field constraints remain in the pinned raw.
- PayPal-transaction descriptor updates use the PayPal console, while Amex descriptor updates require contacting Amex directly. These are separate update routes, not evidence that their requirements match this AIB AF article.
- Dynamic descriptors ordinarily use a name and phone number or URL. The article says the merchant need not supply a location because Braintree obtains it from the application information, and a refund defaults to the dynamic descriptor passed on the original transaction. This describes descriptor reuse, not refund success, settlement or funding.

> [!warning] Scope and evidence boundaries
> This is a 2026-09-16 snapshot of Braintree's exact AIB AF documentation path, not AIB BF evidence or independent current bank policy. The page gives no general regional, account-eligibility or pricing statement, and the customer's bank controls final statement rendering. Its linked developer-doc route is navigation, not evidence of the API request shape or agreement with this snapshot. The page does not prove successful authorization, settlement, refund or funding.

## Detail locators

- Descriptor purpose, bank-controlled presentation and statement example: `# Descriptors`, lines 14-18.
- Soft, hard and dynamic descriptor definitions: `# Descriptors`, lines 20-25.
- Required descriptor fields and application-derived hard/soft configuration: `# Descriptors`, lines 27-33.
- Separate PayPal-console and Amex-contact update routes: note below `# Descriptors`, lines 36-37.
- Hard and soft merchant-name and clearing-city/phone constraints: `## Hard and soft descriptor requirements`, lines 42-57.
- Refund descriptor default and application-derived location: `## Dynamic descriptor requirements`, lines 60-68.
- Dynamic name, phone and URL constraints: `## Dynamic descriptor requirements`, lines 71-99.
- Linked developer-doc route for per-transaction dynamic descriptors: line 101; navigation only, not additional factual evidence for this entry.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-control-panel]]
- General Braintree descriptor route: [[source-braintree-control-panel-descriptors]]

## Raw Sources

- [[raw/braintree/articles/aib-af/transactions/descriptors-2026-09-16|Braintree AIB AF Transaction Descriptors]] - complete collected Braintree article for AIB AF-scoped descriptor meanings, configuration, update routes, field requirements and refund reuse
