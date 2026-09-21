---
title: "Braintree Client Authorization Overview"
type: source
date_ingested: 2026-09-19
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/authorization/overview"
raw_files:
  - "braintree/docs/guides/authorization/overview-2026-09-16.md"
tags: [braintree, client-sdk, client-authorization, client-token, tokenization-key, 3d-secure]
---

## Overview

This Braintree guide compares the two credentials used to authorize Client SDK access: tokenization keys and client tokens. It is a client-authorization selection guide; it does not establish that a payment transaction has been authorized.

## Key takeaways

- A tokenization key is a lightweight reusable client-authorization value for payment-method tokenization. It can ship with an app, and the Control Panel provides its deactivation route.
- A client token is generated with a server-side library and must be sent from the merchant server to the client. The guide calls it short-lived and reusable for up to 24 hours, while noting that Braintree may deactivate it before its JWT expiration.
- Client tokens authorize payment-method tokenization, payment-method retrieval, and client-side vaulting. Direct client-side vaulting and listing saved payment methods require a customer ID; a tokenization-key flow can instead send a single-use payment-method token to the server for vaulting.
- The capability table gives client tokens configuration-supply and 3D Secure capabilities that tokenization keys do not have. Both forms cover payment-method tokenization and the listed card and wallet categories; those rows describe client-authorization capabilities, not payment authorization, merchant enablement, or buyer eligibility.
- For collecting payment information and handing it to a server, especially when 3D Secure is not required, the guide recommends a tokenization key. It recommends a client token for the full range of Drop-in functionality, direct client-side saving, or presenting returning customers with saved methods. It also says client tokens can reduce tokenization latency, particularly outside the US.
- An app that supports both guest and registered-user purchases may use both forms by instantiating a new Braintree instance with the chosen authentication method.

## Detail locators

- Client authorization purpose and the two credential definitions: `# Overview`, line 16; `## Types of authorization`, lines 21-25.
- Creation, delivery, deactivation, reuse, vaulting, retrieval, configuration, payment-method, wallet, and 3D Secure differences: `## Types of authorization` > `### Capabilities`, lines 30-44.
- Tokenization-key selection guidance: `## When to use tokenization keys`, lines 49-51.
- Client-token selection and latency guidance: `## When to use client tokens`, lines 56-58.
- Guest and registered-user combination guidance: `## Using both`, line 63.

## Related

- Company: [[braintree]]
- Concept: [[braintree-web-sdk]]

## Raw Sources

- [[raw/braintree/docs/guides/authorization/overview-2026-09-16|Braintree client authorization overview]] - complete guide comparing tokenization keys and client tokens, their qualified capabilities, and selection guidance
