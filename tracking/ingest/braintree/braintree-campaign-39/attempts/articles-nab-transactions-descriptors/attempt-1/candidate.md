---
title: "Braintree NAB Transaction Descriptors"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/nab/transactions/descriptors"
raw_files:
  - "braintree/articles/nab/transactions/descriptors-2026-09-16.md"
tags: [braintree, nab, transactions, descriptors, bank-statements]
---

## Overview

This collected Braintree-hosted article, filed under its NAB documentation path, describes statement descriptors for the addressed account. It distinguishes the account's settled hard descriptor from a custom dynamic descriptor passed per transaction through the API, while stating that the customer's bank ultimately controls the exact statement presentation.

## Key takeaways

- The article says the addressed account supports two descriptor types. A hard descriptor appears after settlement and becomes the permanent charge description after the customer's bank finalizes transaction status; a dynamic descriptor is configured by the merchant and passed with each transaction through the API.
- Merchant name, location, and a phone number or URL for a dynamic descriptor are listed as required descriptor information. The hard descriptor is described as automatically configured from application information, with changes routed through Braintree's contact path. Detailed field and character limits remain in the pinned raw.
- Both hard and dynamic merchant names must match the registered trading name provided to NAB. The article requires an Australian phone number, and a dynamic descriptor can show either the phone number or URL, not both. These are qualifications of this captured account path, not evidence of a general regional or processor policy.
- PayPal-transaction descriptor updates are routed to the PayPal console, while Amex descriptor updates require direct contact with Amex; those routes differ from the article's general Braintree contact route.

> [!warning] Scope and evidence boundaries
> This is a 2026-09-16 snapshot of a Braintree-hosted NAB documentation path. It is not independent NAB, PayPal, Amex, or bank authority and does not establish current account or processor assignment, regional or currency availability, merchant eligibility, exact bank rendering, acceptance of a descriptor change, posting timing, or successful payment execution. Do not transfer its rules to sibling account or processor articles.

## Detail locators

- Descriptor purpose, bank-controlled presentation, and example format: `# Descriptors`, raw lines 14-18.
- Addressed-account hard and dynamic descriptor definitions: `# Descriptors`, raw lines 20-24.
- Required descriptor information, application-derived hard descriptor, and Braintree change route: raw lines 26-35.
- Separate PayPal-console and direct-Amex update routes: note under `# Descriptors`, raw lines 38-39.
- Hard-descriptor merchant-name, location, and Australian-phone requirements: `## Hard descriptor requirements`, raw lines 44-66.
- Dynamic merchant-name, Australian-phone, URL, and either-phone-or-URL requirements: `## Dynamic descriptor requirements`, raw lines 69-94.
- Linked Ruby developer-documentation route for passing dynamic descriptors per transaction: raw line 96; navigation only, not additional behavioral evidence for this entry.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-control-panel]]
- General descriptor route: [[source-braintree-control-panel-descriptors]]

## Raw Sources

- [[raw/braintree/articles/nab/transactions/descriptors-2026-09-16|Braintree NAB Transaction Descriptors]] - complete collected article for the addressed account's descriptor types, statement-display qualification, update routes, and field requirements
