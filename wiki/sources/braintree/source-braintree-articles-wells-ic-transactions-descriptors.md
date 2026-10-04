---
title: "Braintree Wells IC Transaction Descriptors"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/wells-ic/transactions/descriptors"
raw_files:
  - "braintree/articles/wells-ic/transactions/descriptors-2026-09-16.md"
tags: [braintree, wells-ic, transactions, descriptors, bank-statements, amex]
---

## Overview

This collected Braintree-owned article, filed under its Wells IC processor path, explains the statement descriptors associated with purchases through a merchant's app or website. It distinguishes soft, hard and per-transaction dynamic descriptors, while leaving the exact customer-statement presentation to the customer's bank. It is not independent current bank policy.

## Key takeaways

- The article says Braintree automatically configured the account's hard and soft descriptors from application information and allows them to be viewed and edited on the Business page in the Control Panel. It requires merchant name, state or province, and customer-service phone information; exact field constraints remain in the pinned raw.
- Dynamic descriptors are custom descriptors passed per transaction through the API. For this captured Wells IC path, the article says they use a name, state, and phone number or URL, while Braintree supplies the state; a refund defaults to the dynamic descriptor passed on the original transaction. This describes descriptor reuse, not refund success, settlement or funding.
- For Braintree's aggregated American Express account, the article gives a Braintree soft descriptor for pending transactions and says the merchant's hard descriptor appears after settlement, with Braintree information retained in an expandable field. It explicitly excludes merchants using their own Amex account from that behavior.
- PayPal-transaction descriptor updates use a separate PayPal-console route rather than the Control Panel path described here.

> [!warning] Processor, account and eligibility boundaries
> This 2026-09-16 Braintree snapshot is scoped to the captured Wells IC path and does not establish current bank policy, regional or account eligibility, or pricing terms. Do not transfer its descriptor, refund or Amex behavior to Wells Flat or another processor/account. A customer's bank controls the final statement rendering, and the page is not proof of successful authorization, settlement, refund or funding.

## Detail locators

- Separate PayPal-console route: note below `# Descriptors`, lines 17-18.
- Descriptor purpose, bank-controlled presentation and example: `# Descriptors`, lines 22-24.
- Soft, hard and dynamic descriptor meanings: `# Descriptors`, lines 26-31.
- Required descriptor information and application-derived Control Panel configuration: `# Descriptors`, lines 33-42.
- Hard and soft merchant-name, state and phone constraints: `## Hard and soft descriptor requirements`, lines 47-68.
- Dynamic name, phone and URL requirements plus API-navigation link: `## Dynamic descriptor requirements`, lines 71-107.
- Refund descriptor default: note below the dynamic-descriptor section, lines 110-111.
- Aggregated-versus-own Amex account behavior and pending-versus-settled display: `## American Express descriptors`, lines 116-124.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-control-panel]]
- General Braintree descriptor route: [[source-braintree-control-panel-descriptors]]

## Raw Sources

- [[raw/braintree/articles/wells-ic/transactions/descriptors-2026-09-16|Braintree Wells IC Transaction Descriptors]] - complete collected Braintree article for Wells IC-scoped descriptor configuration, statement display, refund reuse and Amex account qualifications
