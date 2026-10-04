---
title: "Braintree Forward API Stripe Destination Example"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/extend/forward-api/stripe"
raw_files:
  - "braintree/docs/guides/extend/forward-api/stripe-2026-09-16.md"
tags: [braintree, braintree-extend, forward-api, stripe, sandbox]
---

## Overview

This collected Braintree developer guide is a destination example for using Braintree Forward API configurations with Stripe API routes. It names Braintree configs for Stripe Payment Methods, Tokens and Charges. It is Braintree-hosted forwarding guidance, not Stripe-owned API authority, evidence of current Stripe capability, or proof that Stripe authorized a merchant, accepted a request, created a payment method or token, executed a charge, or completed a payment. See [[braintree]] and [[braintree-forward-api]].

The snapshot was collected on 2026-09-16. Its displayed request targets Braintree's sandbox forwarding endpoint and Stripe's `/v1/payment_methods` route. It documents example request construction, not current production availability, account approval, destination credentials or configuration, successful forwarding, tokenization, authorization, capture, settlement, or funding.

## Key takeaways

- The page states that production Forward API use is subject to eligibility and directs readers to an Account Manager or Business Development. Collection of the page and availability of a sandbox endpoint do not establish production approval or merchant enablement.
- The page associates Stripe Payment Methods, Tokens and Charges routes with the Braintree config names `stripe_create_payment_method`, `stripe_create_token` and `stripe_create_charge`, respectively. Those are Braintree-documented destination config names; current Stripe API contracts, account eligibility and credential requirements require separate Stripe authority and account evidence.
- The one displayed request posts to Braintree's sandbox forwarding endpoint, authenticates that forwarding call with Braintree public/private keys, includes a Braintree merchant ID and `payment_method_nonce`, selects `stripe_create_payment_method`, and targets `https://api.stripe.com/v1/payment_methods`. It is an example only and contains no destination response or lifecycle evidence.
- The example also places illustrative card fields under `data`. The page does not establish that the example is a complete production credential, PCI, tokenization or payment workflow, and it does not show example calls for `stripe_create_token` or `stripe_create_charge`.
- For additional non-mandatory destination fields, the guide points to the Forward API `override` attribute with a `body` containing a JSON or XML string. It warns that data sent through that path appears in Braintree logs and tells users not to send sensitive data or customer PII that way.

> [!warning] Production eligibility and destination authority are separate
> Braintree says production Forward API use is eligibility-gated. Confirm Braintree approval, the correct environment and forwarding configuration, and current Stripe API, account and credential requirements before relying on this route. This Braintree-hosted example is not official Stripe authority.

> [!warning] Protect credentials, payment data and logged overrides
> Keep real Braintree credentials, card data, destination credentials and private identifiers out of source and evidence artifacts. The guide specifically warns that override-body data appears in Braintree logs and should not contain sensitive data or customer PII.

> [!warning] Config names and example requests are not payment proof
> The snapshot names configs and contains a request example but no destination response or lifecycle evidence. It does not prove request acceptance, payment-method or token creation, charge authorization or capture, settlement, funding, or production readiness.

## Detail locators

- Production Forward API eligibility and contact routes: `**AVAILABILITY**`, raw lines 16-17.
- Stripe API route and Braintree config-name associations for Payment Methods, Tokens and Charges: paragraph below `# Stripe`, raw line 19.
- Braintree sandbox forwarding endpoint, Basic-auth environment variables, merchant ID, payment-method nonce, `stripe_create_payment_method`, Stripe destination URL and illustrative card fields: `## Usage` / `### bash`, raw lines 22-45.
- Optional-field `override.body` guidance and JSON/XML string format: paragraph after the example, raw line 46.
- Logging and sensitive-data/PII warning for the override path: `**NOTE**`, raw lines 47-48.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-forward-api]]

## Related raw API references

- [[raw/braintree/docs/reference/forward-api/overview-2026-09-16|Braintree Forward API overview]] - linked navigation-only route for general Forward API behavior and production eligibility; not read as factual evidence for this source
- [[raw/braintree/docs/reference/forward-api/forward-2026-09-16|Braintree Forward API request reference]] - linked navigation-only route for `override` details; not read as factual evidence for this source

## Linked destination references (navigation only)

- [Stripe Payment Methods create reference](https://stripe.com/docs/api/payment_methods/create) - linked by the collected guide; not read as factual evidence here
- [Stripe Tokens reference](https://stripe.com/docs/api/tokens) - linked by the collected guide; not read as factual evidence here
- [Stripe Charges create reference](https://stripe.com/docs/api/charges/create) - linked by the collected guide; not read as factual evidence here

## Raw Sources

- [[raw/braintree/docs/guides/extend/forward-api/stripe-2026-09-16|Braintree Forward API Stripe destination guide]] - complete collected guide covering production eligibility, three named Stripe destination configs, a sandbox Payment Methods request example, override-body guidance and the logging warning
