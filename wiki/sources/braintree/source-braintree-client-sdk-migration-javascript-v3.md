---
title: "Braintree JavaScript SDK v2-to-v3 Migration"
type: source
date_ingested: 2026-10-02
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/client-sdk/migration/javascript/v3"
raw_files:
  - "braintree/docs/guides/client-sdk/migration/javascript/v3-2026-09-16.md"
tags: [braintree, javascript, client-sdk, migration, hosted-fields]
---

## Overview

This collected [[braintree]] website snapshot documents the historical migration from the Braintree JavaScript SDK v2 to v3. It describes a major-version API change requiring integration-code changes and a move toward a lower-level, modular client/component model. It is migration evidence for [[braintree-web-sdk]], not proof of current SDK support, merchant eligibility, or the behavior of any separately retained GitHub version.

## Key takeaways

- The guide characterizes v3 as a new major-version API and says upgrading from v2.x requires integration-code changes.
- Instead of one v2.x file containing every client-side integration tool, v3 uses modular components so an integration can include only the payment methods it needs.
- A custom UI begins by creating an API client with a tokenization key or client token, then instantiating components with that client.
- Hosted Fields moves tokenization away from an SDK-controlled form-submission flow: the merchant integration calls `tokenize` when it chooses and sends the returned nonce to its server.
- A Kount Custom integration with its own Kount merchant ID carries a consequential pre-migration condition: the guide says to contact Braintree before migrating so the ID is hard-coded into the gateway. This statement is specific to the collected snapshot and does not establish current Kount or migration policy.

## Detail locators

- **Migrating from v2 to v3 / Why upgrade to v3** — breaking-change framing, lower-level control, form-submission independence, Hosted Fields formatting, modular size, error messaging, and Drop-in changes.
- **Getting v3** — historical package and script-loading routes plus the modular component example.
- **Accepting payments / Custom UI** — client creation with a tokenization key or client token and callback/Promise examples.
- **Credit cards with Hosted Fields** — iframe boundary, formatting changes, explicit tokenization, and nonce handoff examples.
- **PayPal** — a version-qualified `3.63.0+` component route and examples. The collected callback example contains a malformed `fuAction` token, so use this section as snapshot navigation rather than implementation-ready code.
- **Using multiple components** — sharing one client across component instances.
- **Using Premium Fraud Management Tools** — gateway-derived environment/Kount configuration and the Kount Custom pre-migration warning.

## Related

- [[braintree-web-sdk]] — provider concept for the modular browser SDK, nonce handoff, and exact-version evidence boundaries.
- [[braintree-web-drop-in]] — separately versioned prebuilt UI and migration boundary.

## Raw Sources

- [[raw/braintree/docs/guides/client-sdk/migration/javascript/v3-2026-09-16|Braintree JavaScript v3 client-SDK migration guide snapshot]]
