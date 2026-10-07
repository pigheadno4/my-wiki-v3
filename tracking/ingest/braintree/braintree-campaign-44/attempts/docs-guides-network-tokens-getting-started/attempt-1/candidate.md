---
title: "Braintree Getting Started with Network Tokens"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/network-tokens/getting-started"
raw_files:
  - "braintree/docs/guides/network-tokens/getting-started-2026-09-16.md"
tags: [braintree, network-tokens, vault, cards, eligibility]
---

## Overview

This 2026-09-16 collected, unversioned Braintree website snapshot is a getting-started retrieval route for Braintree-managed network tokens. It limits stated availability to merchants processing full stack with Braintree in the United States and select regions, directs merchants to contact Braintree to determine account eligibility, and says enabled merchants need no integration change. Once enabled, network tokens begin to be used for transactions; Braintree says it enrolls existing Vault cards as promptly as possible and attempts enrollment for newly added cards. The page separately routes cards tokenized by another payment service provider to Bring Your Own Tokens, distinguishes a payment method having a network token from a particular transaction having used one, warns that a token may not always be used, and assigns token expiry, update and cancellation lifecycle management to Braintree. This snapshot does not prove current regional or merchant eligibility, account enablement, token enrollment or availability, Sandbox or Production behavior, exact SDK/API-version behavior, or successful network-token payment processing. See [[braintree]] and [[braintree-payment-methods]].

## Key takeaways

- Availability and activation are conditional: the page names US and select North American, South American and European regions, requires full-stack Braintree processing, and directs merchants to confirm merchant-account eligibility with Braintree.
- The stated no-integration-change path applies after Braintree enablement; cards tokenized elsewhere are routed to the separate Bring Your Own Tokens path.
- Existing Vault cards are to be enrolled as promptly as possible, while new Vault cards are only described as enrollment attempts with card networks; neither statement guarantees that a network token will be generated or used.
- The transaction response fields answer different questions: `is_network_tokenized?` indicates whether a network token exists for the payment method, while `processed_with_network_token?` indicates whether one was used for that transaction. The page explicitly says a token may not always be used.
- Braintree says it manages network-token expiration, update and cancellation lifecycle and applies card-network updates as they become available.

## Detail locators

- Regional, merchant and full-stack availability qualification: raw line 16.
- Eligibility contact, no-integration-change statement and Bring Your Own Tokens route: raw line 18.
- Existing-card enrollment timing, enabled-use statement and attempted enrollment of newly vaulted cards: raw line 20.
- Transaction response-field distinction and non-guaranteed token use: raw lines 22-24.
- Expiration, update, cancellation and Braintree-managed lifecycle statement: raw line 26.

## Related

- [[braintree-payment-methods]]
- [[source-braintree-docs-guides-network-tokens-how-it-works]] - separate explanation of provisioning, transaction routing and lifecycle updates
- [[source-braintree-docs-guides-network-tokens-bring-your-own-token-node]] - separate route for network tokens obtained outside Braintree

## Raw Sources

- [[raw/braintree/docs/guides/network-tokens/getting-started-2026-09-16|Braintree Getting Started with Network Tokens (2026-09-16)]]
