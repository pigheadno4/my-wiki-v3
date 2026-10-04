---
title: "Braintree Extend Forwarding Braintree API Payment Tokens"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/extend/forward-api/braintree-api-forwarding"
raw_files:
  - "braintree/docs/guides/extend/forward-api/braintree-api-forwarding-2026-09-16.md"
tags: [braintree, braintree-extend, forward-api, payment-method-nonce, payment-method-token, sandbox]
---

## Overview

This collected Braintree Extend guide describes two ways to construct a Forward API request from payment data returned by the alternate Braintree API: pass a returned token as `payment_method_nonce`, or pass a stored payment-method token backed by a payment method in that API as `payment_method_token`. The page illustrates both routes with server-authenticated calls to Braintree's sandbox forwarding endpoint and an `httpbin.org` destination. It is configuration guidance, not evidence that a destination accepted a request or that a payment was executed, authorized, captured, settled, reconciled, or funded. See [[braintree]] and [[braintree-forward-api]].

## Key takeaways

- Production Forward API use is subject to eligibility. The page directs readers to an Account Manager or Business Development, so this snapshot does not establish current availability, merchant eligibility, production enablement, or account readiness.
- For a token returned from the alternate Braintree API, the first example uses the `payment_method_nonce` request field. For a payment-method token backed by a payment method in that API, the second example uses `payment_method_token`. These are distinct request-object choices; the page does not say that one proves the other exists or remains usable.
- Both examples call `https://forwarding.sandbox.braintreegateway.com/`, authenticate with Braintree public/private keys, identify a `merchant_id`, request `POST`, and target `https://httpbin.org/post`. Their inline configs constrain the method and destination URL, specify URL-encoded body formatting and `CreditCard` type, and transform `$number` into `/body/card[number]`. These are example values and options, not a general destination-support, credential-storage, permission, or production-config contract.
- The page does not document a Control Panel role, destination-side authorization, or a returned destination/payment result. Forwarding configuration must therefore remain separate from proof that the merchant may act at the destination or that any transaction was created or completed.

> [!warning] Eligibility and permission boundary
> The immutable 2026-09-16 snapshot gates production Forward API use on eligibility but does not establish a merchant's present eligibility, required Control Panel role, destination authority, or production configuration approval. The Basic-auth credentials in the curl examples identify how those sandbox requests are formed; they do not establish broader permissions.

> [!warning] Forwarding is not payment outcome evidence
> The examples construct requests to `httpbin.org` through the Braintree sandbox forwarding endpoint. They do not show a retained response or prove destination acceptance, payment execution, authorization, capture, settlement, reconciliation, or funding.

## Detail locators

- Production eligibility and Account Manager or Business Development inquiry route: `# Forwarding Braintree API Payment Tokens > AVAILABILITY`, lines 17-18.
- Returned alternate-Braintree-API token and `payment_method_nonce` route: `# Forwarding Braintree API Payment Tokens`, lines 20-21.
- Nonce example's sandbox endpoint, Basic authentication, merchant, method, destination, config restrictions, type, and card-number transformation: first `### bash` block, lines 23-45.
- Backed payment-method token and `payment_method_token` route: `# Forwarding Braintree API Payment Tokens`, lines 46-48.
- Stored-token example's sandbox endpoint, Basic authentication, merchant, method, destination, config restrictions, type, and card-number transformation: second `### bash` block, lines 50-72.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-forward-api]]

## Related raw API references

- [[raw/braintree/docs/reference/forward-api/overview-2026-09-16|Forward API overview]] - navigation-only route linked by the availability notice; not used as factual evidence here

## Raw Sources

- [[raw/braintree/docs/guides/extend/forward-api/braintree-api-forwarding-2026-09-16|Braintree guide to forwarding Braintree API payment tokens]] - complete collected guide for the two alternate-Braintree-API token input routes, sandbox request examples, and production-eligibility qualification
