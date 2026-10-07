---
title: "Braintree Fastlane Server-side Integration (Node.js)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/fastlane/server-side/node"
raw_files:
  - "braintree/docs/guides/fastlane/server-side/node-2026-09-16.md"
tags: [braintree, paypal, fastlane, server-side, nodejs, graphql, shipping]
---

## Overview

This collected [[braintree]] webpage is an unversioned Node-routed server-side guide for [[paypal-fastlane]]. It covers generating a Fastlane client token with root-domain input and, when processing a payment, including the customer's shipping address so it is saved to the Fastlane profile. Its Braintree SDK and GraphQL blocks are examples, not proof of current availability, merchant or buyer eligibility, direct PayPal Orders API behavior, Vault success, or an executed payment.

## Key takeaways

- The guide says the client-token request must include the root domain; omission prevents Fastlane from working. It rejects domain entries that contain a subdomain, wildcard, or HTTP/HTTPS protocol.
- When processing a payment after generating a Fastlane token, the page directs the merchant to include the customer's shipping address in the request so it is saved to the customer's Fastlane profile for future use.
- The Node.js sale example passes a client-supplied payment-method nonce and device data along with customer, billing, and shipping data. The GraphQL charge example instead passes a payment-method ID, `riskData.deviceData`, shipping, email, and billing-address input; these are example request shapes, not evidence of a successful transaction.
- The GraphQL example requests `vaultPaymentMethodAfterTransacting` with `when: 'ON_SUCCESSFUL_TRANSACTION'`. This is a success-conditioned example input and does not establish that vaulting occurred or will succeed.

## Detail locators

- **Snapshot identity:** raw lines 1-10 record the canonical URL, fetch date, page title, route slug, and source create/update timestamps.
- **Client-token action and root-domain requirement:** `Step 1: Generate client token`, raw lines 17-24.
- **Braintree Node.js client-token example:** raw lines 28-52 show Sandbox gateway construction, `clientToken.generate`, the `domains` array, error branch, and response-token extraction.
- **GraphQL client-token example:** raw lines 53-74 show the `CreateClientTokenInput` mutation and its nested domain input.
- **Domain input restrictions and error condition:** raw lines 76-82 exclude subdomains, wildcards, and protocols and state that those inputs produce an error.
- **Payment-time shipping action and purpose:** `Step 2: Update Fastlane with Consumer's shipping address`, raw lines 85-91.
- **Node.js sale material inputs and routine fields:** raw lines 96-143 show the amount, payment-method nonce, device data, customer, billing, shipping, and result-handling example.
- **GraphQL charge material inputs and conditional vault option:** raw lines 144-185 show `ChargeCreditCardInput`, payment-method ID, risk/device data, shipping, email, success-conditioned vaulting, and billing-address inputs.

## Related

- [[braintree]]
- [[paypal-fastlane]]
- [[source-braintree-docs-guides-fastlane-client-side-node|Braintree Fastlane Client-side Integration (Node route)]]
- [[source-braintree-docs-guides-fastlane-advanced-option|Braintree Fastlane Advanced Options]]

## Raw Sources

- [[raw/braintree/docs/guides/fastlane/server-side/node-2026-09-16|Braintree Fastlane Server-side Integration — Node.js route (2026-09-16 snapshot)]]