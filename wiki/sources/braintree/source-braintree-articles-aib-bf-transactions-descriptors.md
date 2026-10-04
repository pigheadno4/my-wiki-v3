---
title: "Braintree AIB BF Transaction Descriptors"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/aib-bf/transactions/descriptors"
raw_files:
  - "braintree/articles/aib-bf/transactions/descriptors-2026-09-16.md"
tags: [braintree, aib-bf, transactions, descriptors, bank-statements]
---

## Overview

This collected Braintree-hosted article, filed under the AIB BF path, explains the identifying information customers may see on statements for purchases made through a merchant's app or website. It distinguishes soft, hard and per-transaction dynamic descriptors, while stating that the customer's bank ultimately determines the exact statement presentation.

The snapshot is not independent current bank policy and does not establish present account or regional eligibility, pricing, or payment success. Its AIB BF scope must not be transferred to AIB AF or another processor/account arrangement.

## Key takeaways

- A soft descriptor is displayed while an authorized charge is pending. A hard descriptor is displayed after settlement and becomes the permanent charge description once the customer's bank finalizes transaction status. A dynamic descriptor is custom information configured and passed with each transaction through the API.
- Merchant name (trading name) and clearing city or phone number are required descriptor parameters. The article says hard and soft descriptors were automatically configured from application information and directs change requests to Braintree with the fields and desired values. PayPal-transaction descriptor changes instead use the PayPal console.
- For dynamic descriptors, the article says a refund defaults to the dynamic descriptor passed on the original transaction. It also says a location need not be supplied because Braintree obtains it from the application location. These are descriptor-selection statements, not evidence that a refund, authorization, settlement or funding event succeeded.
- Detailed merchant-name, clearing-city/phone, dynamic-name, phone and URL constraints, examples, and the linked developer-reference route remain in the raw locators rather than being generalized as current or cross-processor requirements.

> [!warning] Bank-controlled presentation
> The customer's bank determines exactly how the business descriptor appears. The example format and configured values do not guarantee the customer's final statement rendering.

> [!warning] Captured AIB BF scope
> Keep these definitions, configuration routes and field constraints within this captured AIB BF article. Do not treat them as AIB AF rules, independent current bank policy, current regional/account eligibility, pricing terms, or proof of transaction or refund success. The linked developer documentation is a navigation route, not evidence that its request behavior agrees with this snapshot.

## Detail locators

- Descriptor purpose, bank-controlled presentation and example: `# Descriptors`, raw lines 14-18.
- Soft, hard and dynamic descriptor meanings: `# Descriptors`, raw lines 20-25.
- Required parameters, application-derived configuration, Braintree change route and separate PayPal-console route: raw lines 27-37.
- Hard and soft merchant-name and clearing-city/phone requirements: `## Hard and soft descriptor requirements`, raw lines 42-57.
- Refund descriptor default and application-derived location: `## Dynamic descriptor requirements`, raw lines 60-68.
- Dynamic name, phone and URL constraints, examples, recommendation and developer-doc navigation: raw lines 71-103.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-control-panel]]
- General descriptor route: [[source-braintree-control-panel-descriptors]]

## Raw Sources

- [[raw/braintree/articles/aib-bf/transactions/descriptors-2026-09-16|Braintree AIB BF Transaction Descriptors]] - complete collected snapshot covering descriptor meanings, application-derived configuration, statement-presentation qualification, dynamic/refund behavior and field constraints
