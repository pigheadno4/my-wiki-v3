---
title: "Adyen Docs: Secure webhooks"
type: source
date_ingested: 2026-10-10
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/webhooks/secure-webhooks"
raw_files:
  - "adyen/docs/development-resources/webhooks/secure-webhooks/2026-09-15.md"
tags: [adyen, webhooks, security, oauth, basic-authentication, hmac]
---

## Overview

This [[adyen]] documentation page is a 2026-09-15 snapshot of recommendations for securing webhook endpoint access, checking message origin and integrity, rotating credentials and HMAC keys, and allowing Adyen network traffic. It describes OAuth 2.0, basic authentication over HTTPS, HMAC signatures, and domain or DNS-based firewall allowlisting.

## Key takeaways

- Adyen recommends an authentication mechanism for webhook endpoint access. OAuth 2.0 is strongly recommended but documented here as supported only for Standard webhooks and all Balance Platform webhook types; basic authentication is listed as supported for all Adyen webhook types.
- In the documented OAuth flow, Adyen obtains an access token from the merchant-designated identity provider and sends it in each webhook event header. Configuration requires a client ID, protected client secret, authorization-server URL, an access-token TTL of at least one hour (3599 seconds), and a scope; the page recommends least-privilege scopes and periodic credential rotation.
- Basic authentication must be used over HTTPS because otherwise its credentials can be compromised. The page explicitly limits its assurance to identifying Adyen as the sender and says it does not establish that the event was unmodified in transit.
- Adyen strongly recommends HMAC signature verification for protection against unauthorized webhooks and describes successful verification as confirming Adyen origin and lack of in-transit modification. This is a message-authentication claim, not proof of endpoint security generally, delivery, processing, account eligibility, or any payment or resource outcome.
- After generating a replacement HMAC key, propagation can take time, so the receiver should temporarily continue accepting events signed by the previous key.
- Adyen does not provide a stable IP-address list. For firewall rules, the page points to domain allowlisting of `out.adyen.com` or systematic DNS resolution, recommends an hourly lookup, and warns that hardcoded resolved addresses can still disrupt delivery when addresses change.

> [!warning] Recommendation conflict and evidence boundary
> The authentication section says OAuth 2.0 is supported for Standard and Balance Platform webhooks, but its basic-authentication subsection also recommends basic authentication for all webhook types other than Standard. The snapshot does not reconcile how that latter recommendation applies to Balance Platform webhooks, so preserve the stated support scopes and verify the current configuration path rather than inferring a single universal choice. This documentation snapshot also does not prove current availability, successful configuration, delivery, processing, replay protection, or a business outcome.

## Detail locators

- Security purpose: `# Secure webhooks`, lines 15-19.
- Authentication choices and support scope: `## Authentication / Authorization`, lines 27-40.
- OAuth token flow, configuration inputs, secret handling, minimum token TTL, least-privilege scope, and credential rotation: `### Open Authorization (OAuth 2.0)`, lines 36-53.
- Basic-authentication scope, HTTPS requirement, and origin-versus-integrity limitation: `### Basic authentication over HTTPS`, lines 55-63.
- HMAC recommendation and stated origin-and-integrity purpose: `## Hash-based message authentication code (HMAC) signatures`, lines 65-67. Detailed signature formats and verification procedures are delegated to the linked verification guide.
- Replacement-key propagation and previous-key overlap: `### Changing your HMAC key`, lines 69-73.
- Firewall guidance, unavailable stable IP list, domain allowlisting, DNS lookup interval, and hardcoded-address disruption risk: `## Domain and IP addresses`, lines 75-84.

## Related

- Company: [[adyen]]
- Concept: [[adyen-webhooks]]
- Detailed HMAC verification guide: [[source-adyen-docs-development-resources-webhooks-secure-webhooks-verify-hmac-signatures]]

## Raw Sources

- [[raw/adyen/docs/development-resources/webhooks/secure-webhooks/2026-09-15|Adyen Docs — Secure webhooks (2026-09-15)]]
