---
title: "Braintree Control Panel Important Gateway Credentials"
type: source
date_ingested: 2026-09-27
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/control-panel/important-gateway-credentials"
raw_files:
  - "braintree/articles/control-panel/important-gateway-credentials-2026-09-16.md"
tags: [braintree, control-panel, api-credentials, merchant-account, tokenization-key, sandbox, production]
---

## Overview

This collected Braintree article is a Control Panel retrieval guide for identifiers used in gateway access and integration configuration. It distinguishes the API environment, user-specific public and private keys, gateway-wide merchant ID, merchant-account-specific ID, client tokenization keys, and the legacy Client-Side Encryption key while documenting their Control Panel access paths and material environment, permission, and security boundaries.

## Key takeaways

- Braintree identifies four API credentials: environment, public key, private key, and merchant ID. The environment directs API requests to Sandbox or Production; each environment has different API keys, so an environment switch requires corresponding code changes.
- A user's public and private keys together form that user's API keys. Users can change or rotate their own keys, which can affect an integration. The private key must not be shared outside use in an API call. Public and private keys are reached through the applicable Sandbox or Production Control Panel under **API** and **API Keys**; the private value requires the separate **View** action.
- The merchant ID identifies the entire gateway account, can cover multiple merchant accounts, and differs between Sandbox and Production. It is not the merchant account ID. The article routes merchant-ID lookup through **Business** and also identifies its position after `/merchants/` in the logged-in Control Panel URL.
- A merchant account ID identifies one merchant account inside a gateway. When multiple merchant accounts exist and an API request omits this ID, the request uses the default merchant account. The IDs are under **Business** and **Merchant Accounts**; visibility requires the user's **Add/Edit Processing Options** role permission. Additional merchant accounts can be created manually only in Sandbox; adding one in Production requires contacting Braintree.
- Tokenization keys authorize a client SDK to tokenize payment information for server use and are viewed or generated under **API** and **Tokenization Keys**. The Client-Side Encryption key is described as required for Braintree's older integration method, is gateway-wide rather than user-specific, and is located under **API** and **Client-Side Encryption Keys**.

## Detail locators

- Four API credentials and their integration purpose: `## API credentials`, lines 21-27.
- Sandbox/Production direction, separate keys, user ownership, rotation, and code-change warning: `### Environment` through `### API keys`, lines 30-43.
- Public/private key identity, Control Panel paths, generation/view actions, and private-key confidentiality: `#### Public key` through `#### Private key`, lines 48-76.
- Gateway-wide merchant ID, environment scope, Control Panel path, and URL location: `### Merchant ID`, lines 79-98.
- Merchant account ID scope, default routing, Control Panel path, permission requirement, Sandbox-only manual creation, and distinction from merchant ID: `### Merchant account ID`, lines 106-154.
- Tokenization-key purpose and access path: `### Tokenization keys`, lines 162-174.
- Legacy CSE-key scope and access path: `### Client-Side Encryption key`, lines 177-187.

## Evidence boundary

> [!warning] Credential locations are environment- and access-sensitive
> Use the Control Panel that matches the intended Sandbox or Production environment, and do not expose private keys outside API-call use. This collected page documents credential categories and UI routes; it does not supply credential values, establish that every Control Panel user can view every section, or prove current support for the older Client-Side Encryption integration.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-control-panel]]
- Supporting concept: [[braintree-web-sdk]]

## Raw Sources

- [[raw/braintree/articles/control-panel/important-gateway-credentials-2026-09-16|Braintree Important Gateway Credentials]] - complete collected article covering gateway credential types, Control Panel access paths, and environment, role and security boundaries
