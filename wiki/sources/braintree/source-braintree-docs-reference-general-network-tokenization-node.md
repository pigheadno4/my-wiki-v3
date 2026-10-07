---
title: "Braintree Network Tokenization Fields (Node.js)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/general/network-tokenization/node"
raw_files:
  - "braintree/docs/reference/general/network-tokenization/node-2026-09-16.md"
tags: [braintree, nodejs, network-tokens, credit-cards, response-fields]
---

## Overview

This 2026-09-16 collected Braintree website page is a Node-routed server-side response-field reference for Braintree-managed network tokenization of vaulted credit cards. It says a transaction qualifies to be processed with a network token when the vaulted card has been tokenized, limits the page's stated support to Visa and Mastercard vaulted credit cards, and directs merchants to Customer Success to determine merchant-account eligibility. It distinguishes the card-level `is_network_tokenized?` response from the transaction-level `processed_with_network_token?` response and names a `network_token` details map. The route does not establish an exact Node SDK package or version, a Sandbox or Production environment, present-day account enablement, token availability, or successful token use; it is also distinct from Apple Pay or another product-specific response object and from the separate Bring Your Own Token request path. See [[braintree]] and [[braintree-payment-methods]].

## Key takeaways

- Subject, condition and action: for a vaulted Visa or Mastercard credit card that has been network-tokenized, the page says a transaction qualifies to be processed with that network token; merchant-account eligibility must be confirmed with Braintree Customer Success.
- `is_network_tokenized?` answers whether the card has been network-tokenized and describes the TPAN as replacing the underlying source-card credential; `processed_with_network_token?` separately answers whether the particular transaction was processed with a network token.
- The page names `network_token` as a map for token details used in the transaction, but the captured explanation is malformed; use the raw locator without inferring map keys, presence rules or a token-response schema.

## Detail locators

- Processing qualification, vaulted-card condition and Visa/Mastercard scope: raw lines 16-18.
- Merchant-account eligibility contact: raw line 20.
- Server-side response-object purpose: raw lines 23-26.
- Card-level `is_network_tokenized?` boolean and TPAN explanation: raw lines 28-32.
- Transaction-level `processed_with_network_token?` boolean: raw lines 34-38.
- `network_token` map row and damaged captured explanation: raw lines 39-41.

## Related

- [[braintree-payment-methods]]
- [[source-braintree-docs-guides-network-tokens-getting-started]] - separate Braintree-managed network-token eligibility, enablement and lifecycle route
- [[source-braintree-docs-guides-network-tokens-bring-your-own-token-node]] - separate Node-routed request path for externally supplied or self-vaulted network tokens
- [[source-braintree-docs-reference-response-apple-pay-card-node]] - separate Apple Pay Card response reference

## Raw Sources

- [[raw/braintree/docs/reference/general/network-tokenization/node-2026-09-16|Braintree Network Tokenization Fields Node reference (2026-09-16)]]
