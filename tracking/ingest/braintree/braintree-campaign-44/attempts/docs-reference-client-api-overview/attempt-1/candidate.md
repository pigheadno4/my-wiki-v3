---
title: "Braintree Client API Overview"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/client-api/overview"
raw_files:
  - "braintree/docs/reference/client-api/overview-2026-09-16.md"
tags: [braintree, client-api, payment-method-nonces, client-sdk, tokenization]
---

## Overview

This unversioned [[braintree]] website-reference snapshot describes the Client API as an HTTP API that accepts multiple payment-method detail types through a unified interface and returns transactable payment-method nonces. It says the Braintree iOS, Android and JavaScript SDKs use this API to tokenize, vault and retrieve supported payment methods.

## Key takeaways

- Client API requests use an authorization fingerprint that the page characterizes as limited authorization suitable for an untrusted client. The request method depends on the endpoint: GET parameters should be URL-encoded, while POST bodies must be JSON with `Content-Type: application/json`; requests should also send `Accept: application/json`.
- Responses are JSON, except that the page also allows a JavaScript function invocation for JSONP. Errors are represented through HTTP status codes and error objects; validation and authorization errors include developer-facing information, and `fieldErrors` can form a nested field-level structure.
- The displayed credit-card POST and response illustrate the request and response shapes, including the authorization fingerprint and returned nonce; routine example fields remain in the raw locator.

## Scope and boundaries

This snapshot documents the Client API layer, not package-qualified SDK behavior, the server-side gateway lifecycle or a distinct product-eligibility statement. It uses an authorization fingerprint but does not explain fingerprint issuance or a client-token flow, and its example gateway URL does not identify an environment-selection rule. The examples and captured responses are not evidence of current availability, merchant enablement, nonce lifetime, vault persistence or payment execution.

## Detail locators

- Client API identity, unified payment-method input and transactable nonce output: `# Client API`, lines 14-18.
- iOS, Android and JavaScript SDK use for tokenization, vaulting and retrieval: `# Client API`, lines 17-18.
- Authorization-fingerprint scope and request-method/header/encoding conditions: `## Requests`, lines 21-24.
- Example credit-card POST with an authorization fingerprint: `### bash`, lines 25-37.
- JSON-versus-JSONP response boundary and example nonce response: `## Responses`, lines 39-59.
- HTTP status/error-object behavior and nested field-error shape: malformed captured Errors heading at lines 60-93.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]
- SDK contexts: [[braintree-web-sdk]], [[braintree-ios-sdk]], [[braintree-android-sdk]]
- Payment-method lifecycle context: [[braintree-payment-methods]]

## Raw Sources

- [[raw/braintree/docs/reference/client-api/overview-2026-09-16|Braintree Client API overview (2026-09-16)]] - fully read pinned webpage snapshot for Client API purpose, SDK relationship, authorization, requests, responses and errors
