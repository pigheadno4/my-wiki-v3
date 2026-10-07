---
title: "Braintree Masterpass Testing and Go Live"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/masterpass/testing-go-live"
raw_files:
  - "braintree/docs/guides/masterpass/testing-go-live-2026-09-16.md"
tags: [braintree, masterpass, testing, sandbox, secure-remote-commerce]
---

## Overview

This 2026-09-16 [[braintree|Braintree]] website snapshot is a narrow server-side testing reference for the replaced Masterpass product: it explains Sandbox card-number validation and supplies static nonces that simulate cards originating from Masterpass. It also directs former Masterpass users to Secure Remote Commerce (SRC). Use [[braintree-payment-methods]] for the provider-wide method route.

## Key takeaways

- In Sandbox, the page says only Braintree test credit-card numbers are accepted; vaulting or transacting with any other card number produces a validation error.
- For testing server-side code, the page provides static Masterpass-originating nonces representing American Express, Discover, Mastercard and Visa cards. These are simulation fixtures, not a client checkout, a real card, or a successful transaction result.
- The availability notice says Masterpass was replaced by Visa SRC and directs prior users to integrate with SRC. It describes SRC as a limited release for eligible merchants, warns that its API is subject to change, says it was introduced in Android v2, iOS v4 and JavaScript v3 Client SDKs, and directs merchants to request access.

## Scope and evidence boundary

The page is unversioned except for the SDK-family versions named in its SRC notice, and its body contains no Production configuration, activation, validation or go-live procedure despite the title. Its current-tense SRC wording is snapshot evidence rather than current availability or merchant eligibility: the separately retained [[source-braintree-payment-methods-secure-remote-commerce|SRC authority]] says Click to Pay/SRC would no longer be supported effective January 20, 2026 while also describing a limited release, leaving present support and a safe migration path unresolved. The fixtures establish only documented Sandbox simulation behavior for server-side testing, not exact SDK runtime behavior or payment execution.

## Detail locators

- Masterpass replacement, SRC limited-release eligibility, API-change warning, Client SDK families and access route: opening `**AVAILABILITY**`, raw lines 17-18.
- Sandbox-only test-card rule and validation-error condition: `## Testing`, raw lines 21-23.
- Static-nonce purpose and the four simulated card brands: `### Nonces`, raw lines 24-32.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Support-status authority: [[source-braintree-payment-methods-secure-remote-commerce]]

## Raw Sources

- [[raw/braintree/docs/guides/masterpass/testing-go-live-2026-09-16|Braintree Masterpass Testing and Go Live (captured 2026-09-16)]] - complete captured page containing the availability notice, Sandbox validation rule and static Masterpass nonce fixtures
