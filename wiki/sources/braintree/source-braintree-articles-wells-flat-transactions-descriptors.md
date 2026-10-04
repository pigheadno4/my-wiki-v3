---
title: "Braintree Wells Flat Transaction Descriptors"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/wells-flat/transactions/descriptors"
raw_files:
  - "braintree/articles/wells-flat/transactions/descriptors-2026-09-16.md"
tags: [braintree, wells-flat, transactions, descriptors, bank-statements, amex]
---

## Overview

This collected Braintree-owned article, filed under its Wells Flat documentation path, explains statement descriptors for purchases made through a merchant's mobile app or website. It distinguishes soft, hard and per-transaction dynamic descriptors, documents application-derived configuration and Control Panel editing, and leaves the exact statement presentation to the customer's bank.

## Key takeaways

- A soft descriptor appears after authorization while the charge is pending; a hard descriptor appears after settlement and remains once the customer's bank finalizes the transaction status. A dynamic descriptor is custom information configured and passed with each transaction through the API.
- Merchant name, merchant state or province, and a customer-service phone number are required descriptor information. The article says Braintree automatically configured the hard and soft descriptors from application information and routes viewing and editing to the Business page in the Control Panel.
- Dynamic descriptors use a name, state, and phone number or URL, but the merchant need not supply the state because Braintree says it will retrieve that information. The pinned raw owns the detailed length, character, capitalization and formatting requirements.
- A refund defaults to the dynamic descriptor passed on the original transaction. This describes descriptor reuse only; it does not establish refund success, settlement or funding. PayPal-transaction descriptor updates use a separate PayPal-console route.
- The American Express section applies to Braintree's aggregated Amex account and expressly excludes merchants using their own Amex account. Under the aggregated-account path, the article documents Braintree information as the pending soft descriptor and merchant-specific hard-descriptor information after settlement.

> [!warning] Scope, account and evidence boundaries
> This is a 2026-09-16 snapshot of Braintree's Wells Flat documentation path, not independent or current Wells Fargo policy. The page does not establish present account eligibility, pricing-model assignment or regional applicability. Do not transfer its rules to a Wells IC path, another processor, account or region. A customer's bank controls the final statement rendering, and this page does not prove successful authorization, settlement, refund or funding.

## Detail locators

- Separate PayPal-console route: note below `# Descriptors`, lines 17-18.
- Descriptor purpose, bank-controlled rendering and statement example: `# Descriptors`, lines 22-24.
- Soft, hard and dynamic descriptor definitions: `# Descriptors`, lines 26-31.
- Required descriptor information and application-derived Control Panel configuration: `# Descriptors`, lines 33-40.
- Hard and soft merchant-name, state and phone constraints: `## Hard and soft descriptor requirements`, lines 43-64.
- Dynamic state handling and detailed name, phone and URL constraints: `## Dynamic descriptor requirements`, lines 67-103.
- Refund descriptor default: note below `## Dynamic descriptor requirements`, lines 106-107.
- Aggregated-versus-own American Express account boundary and pending/settled statement behavior: `## American Express descriptors`, lines 112-120.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-control-panel]]
- API/SDK concept: [[braintree-server-sdk]]
- General Braintree descriptor route: [[source-braintree-control-panel-descriptors]]

## Raw Sources

- [[raw/braintree/articles/wells-flat/transactions/descriptors-2026-09-16|Braintree Wells Flat Transaction Descriptors]] - complete collected article covering statement-descriptor types, configuration, field requirements, refund reuse and account-qualified American Express behavior
