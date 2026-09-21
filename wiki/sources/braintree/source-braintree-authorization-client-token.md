---
title: "Braintree Client Token Authorization"
type: source
date_ingested: 2026-09-19
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/authorization/client-token"
raw_files:
  - "braintree/docs/guides/authorization/client-token-2026-09-16.md"
tags: [braintree, client-token, client-sdk, authorization, jwt]
---

## Overview

This Braintree guide explains the client token used to configure and authorize a Braintree client SDK. It assigns token generation to the merchant server and token retrieval plus SDK initialization to the client; this is client-SDK application authorization, not evidence of transaction authorization or payment success.

## Key takeaways

- A client token is a signed JWT containing the configuration and authorization information required by the Braintree client SDK.
- The server generates the client token and provides it to the client, which obtains the token and uses it to initialize the client SDK. The guide says this authenticates the application to communicate directly with Braintree.
- Client tokens are valid for up to 24 hours, not a guaranteed full 24-hour lifetime. If a token includes a customer ID and creates an excessive number of payment methods, Braintree says it will be invalidated; the page gives no numeric threshold.
- The page does not document a fixed use count or broader reuse guarantee.

## Detail locators

- Token format, contents, and client-SDK purpose: `# Client Token`, line 16.
- Server generation, server-to-client delivery, and application-communication scope: `# Client Token`, lines 18-20.
- Validity and customer-ID/excessive-payment-method invalidation: `# Client Token`, line 22.

## Related

- Company: [[braintree]]
- Concept: [[braintree-web-sdk]]
- Related concept: [[braintree-server-sdk]]

## Raw Sources

- [[raw/braintree/docs/guides/authorization/client-token-2026-09-16|Braintree client-token authorization guide]] - complete guide covering token purpose, server/client roles, validity, and stated invalidation
