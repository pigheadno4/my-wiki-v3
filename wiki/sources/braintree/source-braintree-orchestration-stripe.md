---
title: "Braintree PayPal Orchestration Stripe Integration"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/orchestration/stripe"
raw_files:
  - "braintree/docs/guides/orchestration/stripe-2026-09-16.md"
tags: [braintree, orchestration, stripe, card-payments, transaction-lifecycle]
---

## Overview

This Braintree-hosted Stripe integration guide describes a US-only route for using an existing Braintree integration to process card transactions through PayPal Orchestration with Stripe as the destination. Merchants perform transaction operations through Braintree, while the guide says settlement, chargebacks, reporting, and reconciliation are handled through the Stripe portal. This collected page is Braintree documentation for that destination integration, not independent current Stripe authority, proof of account eligibility, or execution evidence.

## Key takeaways

- Use Braintree for transaction operations; operating directly in Stripe can create discrepancies and synchronization errors. The documented core route supports single-step charge, separate authorization and capture, full capture, voids, and refunds, subject to the operation matrix and status rules in the raw source; within this Braintree-managed integration, a standalone authorization must be captured within seven days before it expires. It does not support partial capture, capture above the authorized amount, Adjust Authorization, or the listed escrow/partial-settlement operations.
- Setup requires a US-based merchant, currency-specific Braintree merchant accounts arranged with a Braintree AM or TAM, a Stripe connection configured in the Braintree Control Panel, and the correct distinct Stripe key for each sandbox or production environment. The guide directs merchants to confirm setup with a sandbox test transaction.
- Stripe transactions require `cardholderName` during payment-method tokenization. Refunds require sufficient Stripe-account funds; an insufficient-funds refund can remain `PENDING` at Stripe and `SETTLING` in Braintree until Braintree receives a final webhook update. Merchants are not required to implement the Stripe refund webhooks described by this guide because Braintree registers them.
- Treat `SETTLING` as non-final: do not ship goods or provide services until the Braintree transaction is `SETTLED`. The generic reconciliation paragraph says Braintree queries Stripe for capture, refund, and charge, but the more specific `FAILED`-charge section says charge errors are not automatically reconciled. Because the source does not resolve that conflict, query by the internal transaction reference with Find/Search before attempting another create.
- The feature tables, required-field mappings, response-code mappings, test-card mappings, and SDK/GraphQL navigation are snapshot-specific detail routes. They do not establish current Stripe behavior outside this Braintree-managed integration or prove settlement or funding.

## Detail locators

- **Supported feature matrices:** `## Features` (lines 21-108), including core lifecycle, void/refund, payment instruments, fraud data, and verification support.
- **Account, environment, credential, field, and webhook prerequisites:** `## Before you begin` and `## Transactions` (lines 111-188).
- **Supported Braintree transaction operations:** `### Transaction object support` (lines 191-222).
- **Status mapping, reconciliation, fulfillment, and retry behavior:** `## Transaction status mapping` through `## Retries` (lines 223-283).
- **Network-token enablement and response mappings:** `## Network tokens` and `## Response codes` (lines 286-403).
- **Sandbox card mapping and production distinction:** `## Test cards` (lines 406-439).

## Related

- [[braintree]]
- [[braintree-payment-platform]]

## Raw Sources

- [[raw/braintree/docs/guides/orchestration/stripe-2026-09-16|Braintree Stripe Integration Guide (fetched 2026-09-16)]]
