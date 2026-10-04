---
title: "Braintree dLocal Payment Orchestration Integration Guide"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/orchestration/dlocal"
raw_files:
  - "braintree/docs/guides/orchestration/dlocal-2026-09-16.md"
tags: [braintree, dlocal, payment-orchestration, cards, transactions]
---

## Overview

This Braintree-hosted guide documents how merchants with an existing Braintree integration can use PayPal Payment Orchestration to process card transactions through dLocal. Transaction operations remain on Braintree; the guide warns that operating directly with dLocal can create discrepancies and synchronization errors. It is not independent dLocal API authority or proof of merchant availability, payment execution, settlement, or funding.

## Key takeaways

- Setup spans both providers: the merchant needs currency-specific Braintree merchant accounts and a dLocal account, and works with a Braintree AM or TAM to share the dLocal API and integration keys securely with Braintree. dLocal issues separate sandbox and production keys.
- After setup, create and manage transactions through the Braintree SDK or GraphQL API. Customer creation is mandatory for this integration, including first name, last name, and email; the raw guide locates the complete transaction-field mapping and country-specific requirements for card brands, 3DS, tax identifiers, decimal handling, and installments.
- Lifecycle state is consequential: a standalone authorization must be captured within seven days. For capture or refund HTTP errors, Braintree can keep a transaction in `SETTLING` while it reconciles with dLocal; do not ship or provide service until the status is `SETTLED`. A charge with no inline response can be `FAILED`, then later become `SETTLED` during reconciliation with an automatic refund initiated.
- Feature, operation, response-code, network-token, sandbox-card, and country matrices are snapshot-specific details in the pinned raw. Conditional enablement and market rules should be checked there rather than generalized from an example.

## Detail locators

- Identity and Braintree-owned transaction-operation boundary: lines 14-25 and 124-138.
- Feature and lifecycle-operation matrices: lines 26-103 and 192-210.
- Dual-provider setup and market-specific prerequisites: lines 106-121.
- Required transaction and customer data: lines 136-180.
- Status mapping, reconciliation, and retry cautions: lines 214-263.
- Network tokens, response-code lookup, and sandbox mapping qualification: lines 266-290.
- Country-specific requirements and go-live route: lines 328-367.

## Related

- [[braintree]]
- [[braintree-payment-platform]]

## Raw Sources

- [[raw/braintree/docs/guides/orchestration/dlocal-2026-09-16|Braintree dLocal Integration Guide (2026-09-16 snapshot)]]
