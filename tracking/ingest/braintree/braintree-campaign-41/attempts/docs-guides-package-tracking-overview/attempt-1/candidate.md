---
title: "Braintree Package Tracking Overview"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/package-tracking/overview"
raw_files:
  - "braintree/docs/guides/package-tracking/overview-2026-09-16.md"
tags: [braintree, package-tracking, paypal, physical-goods, shipping, transactions]
---

## Overview

This collected Braintree developer-guide overview describes adding item details when an order is created and then adding carrier tracking to a PayPal transaction after it settles and the tangible goods ship. It routes the required transaction, tracking-number and carrier inputs, the returned package trackers, eligibility and SDK prerequisites, and provider-stated customer-experience, dispute and hold-release benefits.

This is a 2026-09-16 unversioned website snapshot. It is not current availability or exact package-version evidence, and it does not prove that a merchant or transaction qualifies, that an item shipped or was delivered, that PayPal displayed tracking updates, that a dispute was resolved, that a hold was released, or that a payment was authorized, captured, settled or funded.

## Key takeaways

- The page addresses sellers of tangible goods and tells them to send tracking for PayPal transactions when items ship. Its availability section separately directs the merchant to ask a Braintree Account Manager whether the integration qualifies and lists captured client- and server-SDK minimums. Those minimums belong to this website snapshot; they are not evidence of currently supported GitHub package versions or account enablement.
- The eligibility section is narrower than a provider-wide package-tracking claim: it lists online physical-goods merchants accepting branded PayPal payments and payments from consumers in the US, UK, Germany, France, Spain, Italy, Australia and Canada, while excluding in-store merchants and sellers of digital goods or services. The snapshot specifically limits automatic dispute resolution and PayPal App tracking updates to PayPal-branded transactions.
- The documented sequence first adds line items when the order is created, then adds tracking details after the transaction settles. For a partially settled transaction, the request table says to use the child transaction ID. The tracking number and carrier are required; payer notification and request line items are optional, and `notify_payer` defaults to false. Exact field limits, formats, paired UPC conditions and examples remain in the raw tables.
- The response is a transaction object whose `packages` field lists trackers created for that transaction. The page warns that `paypal_tracker_id` might not be available immediately and says it should appear momentarily in a later transaction lookup; this timing statement is snapshot guidance, not a delivery-time guarantee.
- The page describes automatic resolution of Item Not Received PayPal disputes and says tracking can qualify payment and dispute holds for early release and can enable live PayPal App updates. These are provider-stated, condition-sensitive benefits, not evidence that submitting a tracker establishes shipment or delivery, creates seller-protection coverage, resolves a particular dispute, releases money, or changes the underlying payment lifecycle.

> [!warning] Tracking submission is not fulfillment or payment proof
> A tracking request and its returned tracker record show only the documented metadata operation. They do not prove carrier acceptance, shipment, delivery, buyer receipt, payment-method or seller-protection coverage, dispute resolution, hold release, authorization, capture, settlement or funding.

> [!warning] Preserve transaction and PayPal conditions
> Apply the post-settlement sequence, child-transaction rule for partial settlements, branded-PayPal limitation for automatic dispute resolution and PayPal App updates, merchant/integration qualification, physical-goods scope and captured country conditions exactly as stated. Do not generalize them to every Braintree transaction, payment method, platform, merchant, country or fulfillment event.

## Detail locators

- Tangible-goods and ship-event framing plus provider-stated benefits: `## Overview`, raw lines 16-23.
- Account-manager qualification and captured client/server SDK versions: `### Availability`, raw lines 26-44; repeated version table under `### SDK Version requirements`, raw lines 128-146.
- Merchant, payment-method and consumer-country eligibility plus in-store and digital-goods exclusions: `### Eligibility`, raw lines 51-59. The collected rendering merges the country bullet with the exclusion label at raw line 57.
- Order-creation line items, optional/paired fields, formats and examples: `### API Specification`, raw lines 70-84.
- Post-settlement event and tracking-request fields, including the partial-settlement child-ID rule, required fields and default notification behavior: raw lines 86-112 under `#### Request`.
- Returned transaction/package tracker fields and delayed PayPal tracker identifier: `#### Response`, raw lines 115-125.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]
- Generic dispute context: [[disputes]]

## Related raw API references

- [[raw/braintree/docs/guides/package-tracking/client-side-2026-09-16|Braintree package-tracking client-side guide]] - next-step navigation present in the collected overview; not read as behavioral evidence for this source
- [[raw/braintree/docs/guides/package-tracking/server-side/node-2026-09-16|Braintree package-tracking server-side Node.js guide]] - related implementation route; not read as behavioral evidence for this source

## Raw Sources

- [[raw/braintree/docs/guides/package-tracking/overview-2026-09-16|Braintree Package Tracking overview]] - complete collected snapshot covering the post-settlement tracking sequence, eligibility and SDK qualifications, request/response field routes and provider-stated benefits
