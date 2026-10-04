---
title: "Braintree Forward API Adyen Destination Example"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/extend/forward-api/adyen"
raw_files:
  - "braintree/docs/guides/extend/forward-api/adyen-2026-09-16.md"
tags: [braintree, braintree-extend, forward-api, adyen, sandbox]
---

## Overview

This collected Braintree developer guide is a destination example for using Braintree Forward API configurations with two Adyen API routes: Payments through `adyen_payments` and Authorise through `adyen_authorise`. It is a Braintree-hosted forwarding guide, not Adyen-owned API authority, proof of current Adyen capability, or evidence that Adyen authorized a merchant, accepted a request, executed a payment, or settled funds. See [[braintree]] and [[braintree-forward-api]].

The snapshot was collected on 2026-09-16. Its displayed requests target Braintree's sandbox forwarding endpoint and an Adyen test Payments URL. They preserve example request construction and credential placement, not current production availability, account approval, destination configuration, successful forwarding, or payment execution.

## Key takeaways

- The page states that production Forward API use is subject to eligibility and directs readers to an Account Manager or Business Development. Collection of the page, availability of a sandbox endpoint, and the example request do not establish production approval.
- The page names `adyen_payments` for the Adyen Payments API and `adyen_authorise` for the Adyen Authorise API. These are destination-config routes documented by Braintree; current Adyen API behavior and merchant eligibility require separate Adyen authority and account evidence.
- The displayed Payments examples send `POST` requests through `https://forwarding.sandbox.braintreegateway.com/` to `https://checkout-test.adyen.com/v70/payments`. They authenticate the forwarding call with Braintree public/private keys and include a Braintree merchant ID and payment-method nonce. Destination authentication is supplied separately in `sensitive_data`, using either `basic_auth_token` or `api_key`.
- Both displayed requests use `adyen_payments`, a `fake-valid-nonce`, test card data, amount/currency fields and an order-reference placeholder. They are examples only; they do not demonstrate a successful destination response, authorization, capture, settlement, or production credential setup, and they do not provide an `adyen_authorise` request example.
- For additional non-mandatory destination fields, the guide points to the Forward API `override` attribute with a `body` containing a JSON or XML string. It warns that data sent this way appears in Braintree logs and instructs users not to send sensitive data or customer PII through that path.

> [!warning] Production eligibility and destination authority are separate
> Braintree says production Forward API use is eligibility-gated. Confirm Braintree approval, the correct environment and forwarding configuration, and current Adyen API, account and credential requirements before relying on this route. This Braintree-hosted example is not official Adyen authority.

> [!warning] Protect credentials and logged override data
> The examples require Braintree credentials and merchant identity plus a destination Basic-auth token or API key. Keep real credentials, payment data and private identifiers out of source and evidence artifacts. The guide specifically warns that override-body data appears in Braintree logs and should not contain sensitive data or customer PII.

> [!warning] Example requests are not payment proof
> The snapshot contains request examples but no destination response or lifecycle evidence. It does not prove request acceptance, merchant authorization, payment authorization or capture, settlement, funding, or production readiness.

## Detail locators

- Production Forward API eligibility and contact routes: `**AVAILABILITY**`, raw lines 16-17.
- Named Adyen API/config pairings: paragraph below `# Adyen`, raw line 19.
- Basic-auth and API-key authentication support: `## Usage`, raw line 24.
- Basic-auth sandbox request fields, Braintree credentials, `adyen_payments`, Adyen test v70 Payments URL, sample payment data and `basic_auth_token`: first `### bash` example, raw lines 25-50.
- API-key sandbox request and `api_key` placement: second `### bash` example, raw lines 51-77.
- Optional-field `override.body` guidance and JSON/XML string format: paragraph after the second example, raw line 78.
- Logging and sensitive-data/PII warning for the override path: `**NOTE**`, raw lines 79-80.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-forward-api]]

## Related raw API references

- [[raw/braintree/docs/reference/forward-api/overview-2026-09-16|Braintree Forward API overview]] - linked navigation-only route for general Forward API behavior and production eligibility; not read as factual evidence for this source
- [[raw/braintree/docs/reference/forward-api/forward-2026-09-16|Braintree Forward API request reference]] - linked navigation-only route for `override` details; not read as factual evidence for this source
- [[raw/braintree/docs/guides/extend/forward-api/worldpay-2026-09-16|Braintree Forward API Worldpay guide]] - next-page navigation only; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/guides/extend/forward-api/adyen-2026-09-16|Braintree Forward API Adyen destination guide]] - complete collected guide covering eligibility, named destination configs, Basic-auth and API-key sandbox examples, override-body guidance and the logging warning
