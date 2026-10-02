---
title: "Braintree Auth Overview"
type: source
date_ingested: 2026-10-02
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/braintree-auth/overview"
raw_files:
  - "braintree/docs/guides/braintree-auth/overview-2026-09-16.md"
tags: [braintree, braintree-auth, connected-merchants, platforms, oauth, beta]
---

## Overview

This collected overview presents Braintree Auth as a way for ecommerce platforms and merchant service providers to connect with Braintree merchants and take authorized actions on their behalf. It is a product-orientation and retrieval entry: the linked configuration, Connect, payment-method, Shared Vault and Grant API authorities own their implementation details and qualifications.

The snapshot labels Braintree Auth closed beta. Collection of this page does not establish current availability, platform or merchant eligibility, completed merchant authorization, payment-method enablement, transaction approval, or live payment acceptance.

## Key takeaways

- The intended integrator is an ecommerce platform or merchant service provider, while the connected party is a Braintree merchant. The overview frames the resulting relationship as allowing the integrator to take authorized actions on the merchant's behalf; it does not define the exact OAuth scopes or connection sequence.
- One stated use case is connecting merchants' Braintree and PayPal accounts to a platform for invoicing, accounting or analytics services, with access to the merchants' customer and transaction data.
- The overview says a single onboarding flow can support credit cards, debit cards, PayPal and Apple Pay on the web for merchants. The dedicated payment-method guides remain the authority for method-specific setup, eligibility and runtime behavior.
- The page routes transactions made on behalf of merchants with payment methods stored in the platform's vault to Shared Vault transactions. It separately routes sharing saved payment methods with other connected Braintree merchants to the Grant API; this overview does not supply either API's setup or lifecycle details.

> [!warning] Closed beta and orientation boundary
> This 2026-09-16 snapshot says Braintree Auth is in closed beta and directs interested parties to contact Braintree. Its product-level use cases do not prove present access, merchant consent, granted OAuth scope, payment-method availability, transaction success, or safe implementation of the linked capabilities.

## Detail locators

- Closed-beta availability and interest route: `# Overview > AVAILABILITY`, lines 16-17.
- Intended integrators, connected-merchant role and authorized-action purpose: `# Overview`, line 19.
- Braintree/PayPal account connection, service examples and customer/transaction-data access: `# Overview`, line 22.
- Single-onboarding payment-method orientation: `# Overview`, line 23.
- Stored-method merchant transactions and Shared Vault route: `# Overview`, line 24.
- Saved-payment-method sharing and Grant API route: `# Overview`, line 25.
- Ruby/Sinatra sample-application scope: `## Sample application`, lines 28-30.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-auth]]
- Product orientation: [[braintree-payment-platform]]

## Related raw API references

- [[raw/braintree/docs/guides/braintree-auth/configuration-2026-09-16|Braintree Auth configuration guide]] - navigation-only route for platform OAuth application setup; not read or used as factual evidence here
- [[raw/braintree/docs/guides/braintree-auth/connect-2026-09-16|Braintree Auth Connect guide]] - navigation-only route for the merchant-facing connection flow; not read or used as factual evidence here
- [[raw/braintree/docs/guides/braintree-auth/merchant-api/node-2026-09-16|Braintree Auth Merchant API guide (Node.js)]] - navigation-only route for connected-merchant actions through an access-token-initialized gateway; not read or used as factual evidence here
- [[raw/braintree/docs/guides/extend/oauth/shared-vault/node-2026-09-16|Shared Vault transactions guide (Node.js)]] - navigation-only concrete Node.js route related to the overview's Shared Vault link; it is not evidence for an unqualified parent or another SDK variant

## Raw Sources

- [[raw/braintree/docs/guides/braintree-auth/overview-2026-09-16|Braintree Auth overview]] - complete collected overview covering closed-beta availability, intended platform and merchant-service-provider roles, connected-merchant use cases, payment orientation, Shared Vault and Grant API routes
