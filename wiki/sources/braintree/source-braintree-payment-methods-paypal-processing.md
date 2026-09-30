---
title: "Braintree PayPal Processing"
type: source
date_ingested: 2026-09-29
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/guides/payment-methods/paypal/processing"
raw_files:
  - "braintree/articles/guides/payment-methods/paypal/processing-2026-09-16.md"
tags: [braintree, paypal, payment-processing, authorization, capture, settlement, refunds, vaulting]
---

## Overview

This collected Braintree article is the PayPal-specific processing and transaction-lifecycle route for One-Time Payments, Vaulted Payments and Recurring Payments. It explains PayPal authorization and capture, settlement, multiple partial settlements, refunds and voids, dispute navigation, Seller Protection qualifications and the article's legacy Vault flow; it does not establish the same behavior for cards, every Braintree payment method or every PayPal integration.

## Key takeaways

- The article supports either authorizing and submitting for settlement together or separating authorization from capture. It permits a capture attempt for up to 29 days after successful authorization, but says to capture sooner because PayPal does not ensure that all authorized funds remain available throughout that period; capture can also be blocked if the customer's account is restricted or locked, or if the merchant's account has a high restriction level.
- PayPal transactions in this article are not batch-settled: funds are captured after each transaction is submitted for settlement. On successful settlement, the processor response is `Settling`, and the article says those transactions transition to `Settled` within two hours; other cases can produce declined or pending responses, with the outcome also depending on whether multiple partial settlements are used.
- Multiple partial settlements are stated as available for PayPal and Venmo transactions and allow multiple amounts to be settled against a single authorization. For delayed fulfillment or multiple shipments, the article presents a full-order parent authorization with separate per-portion child transactions as an available model, not a requirement for every multiple partial settlement.
- The article allows voids and full or partial refunds for PayPal transactions and recommends the Braintree Control Panel or API so status remains accurate in both PayPal and Braintree. It states that PayPal refunds must be issued within 180 days of the initial sale.
- The described Vault flow is explicitly labeled a legacy integration. Its agreement is tied to the PayPal Business Account credentials configured in the Braintree Control Panel, so changing that account requires customers to authenticate again and accept a new agreement; the article also says some integrations may need additional per-transaction information for vaulted PayPal payments.

## Evidence boundaries

> [!warning] PayPal-specific lifecycle
> Keep the authorization, settlement, refund and Vault statements scoped to PayPal transactions and to this collected article. The partial-settlement paragraph separately names PayPal and Venmo; it does not establish the same capability for cards or all Braintree methods.

> [!warning] Authorization and settlement qualifications
> A 29-day capture-attempt window is not a guarantee that the full authorized amount remains available. Capture can also be blocked if the customer's account is restricted or locked, or if the merchant's account has a high restriction level; settlement above the authorization is conditional on industry and processor support for settlement adjustment.

> [!warning] Legacy Vault flow
> The article itself labels its described Vault flow legacy. Do not use it as current cross-SDK setup authority; follow the linked Vaulted Payments route for implementation details and preserve the PayPal Business Account change consequence.

## Detail locators

- Pay with PayPal scope across one-time, vaulted and recurring payments: `# Processing`, line 16.
- Combined versus separate authorization/capture, 29-day attempt window, availability warning, restriction conditions and settlement-adjustment qualification: `### Authorization`, lines 24-42.
- Immediate per-transaction capture, `Settling` to `Settled` timing and declined-or-pending outcomes: `### Settlement`, lines 45-49.
- Multiple amounts against one authorization and the article's available full-order parent/per-portion child example for PayPal and Venmo partial settlements: `#### Multiple partial settlements`, lines 52-54.
- PayPal void, full/partial-refund and 180-day refund guidance: `## Refunds and voids`, lines 57-61.
- Dispute-management route: `## Disputes`, lines 64-66.
- Seller Protection scope and shipping-address/PayPal-requirement qualifications: `### Seller Protection`, lines 69-75.
- Legacy Vault label, agreement behavior, account-change consequence and possible per-transaction additional information: `## Storing in the Vault`, lines 78-92.

## Related

- Company: [[braintree]]
- Main payment-method route: [[braintree-payment-methods]]
- Braintree-to-PayPal processing boundary: [[paypal-braintree-integration]]
- Dispute context: [[disputes]]
- Recurring-payment context: [[recurring-payments]]

## Related raw API references

- [[raw/braintree/articles/get-started/transaction-lifecycle-2026-09-16|Braintree transaction lifecycle]] - unread navigation-only general lifecycle route; not used to generalize this article's PayPal-specific statements
- [[raw/braintree/docs/reference/request/transaction/submit-for-partial-settlement/node-2026-09-16|Submit for partial settlement - Node.js]] - unread navigation-only implementation route; no SDK behavior is inferred here
- [[raw/braintree/articles/guides/payment-methods/paypal/disputes-2026-09-16|Braintree PayPal Disputes article]] - unread navigation-only dispute route; no dispute lifecycle detail is inferred here

## Raw Sources

- [[raw/braintree/articles/guides/payment-methods/paypal/processing-2026-09-16|Braintree PayPal Processing article]] - complete collected article covering PayPal-specific authorization, capture, settlement, refund and legacy Vault boundaries
