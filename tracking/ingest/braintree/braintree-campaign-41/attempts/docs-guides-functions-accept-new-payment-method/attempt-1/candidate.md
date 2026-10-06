---
title: "Braintree Functions: Accept a New Payment Method"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/functions/accept-new-payment-method"
raw_files:
  - "braintree/docs/guides/functions/accept-new-payment-method-2026-09-16.md"
tags: [braintree, functions, payment-methods, transactions, integration-guide]
---

## Overview

This collected Braintree website page is a documentation preview for building a Braintree Function that connects a new payment-method service to Braintree transaction handling. It illustrates initialization, authorization-handler responsibilities, local testing, configuration and deployment, then a transaction sale that selects the function by name. The preview is not evidence that Functions are currently available to a particular merchant, that an example is production-ready or secure for a real provider, that a function was deployed, or that a payment succeeded. As website guidance, it also does not establish GitHub implementation state, an exact CLI/package version, or current package availability. [[braintree]] [[braintree-payment-platform]]

## Key takeaways

- The `paymentMethod` template creates an authorization handler and, by default, files for capture, void, refund and vault operations. The authorization handler is merchant-authored JavaScript: it receives transaction details, constructs the payment-method service request, performs the outbound API call, and maps the response back into Braintree's expected response shape.
- The shown payload, endpoint, response mapping and `Authorized` status are examples. The page does not establish a complete provider API contract, authentication or secret-management design, input validation, error and timeout behavior, idempotency, PCI scope, or production security posture. Those responsibilities must be resolved for the actual payment-method service and runtime rather than inferred from the snippet.
- The documented workflow includes local `btfns test`, optional mock-data generation, a YAML trigger map, and `btfns deploy`. Deployment defaults to sandbox; production is an explicit prompt selection or `--production` command. Local tests, generated sample data, configuration text and a deploy command do not prove deployed runtime behavior.
- A sale example passes `functionName`; the page says configured triggers are then invoked automatically and later calls for that transaction route back to the function without repeating the function name. Data unavailable through the Transaction API may be passed through Custom Fields. This is page-scoped example behavior, not evidence of present account eligibility, a successful authorization, capture, refund, void, vault action, settlement or funding.

## Detail locators

- Availability and preview status: lines 17-18.
- Template initialization and generated lifecycle files: lines 21-29.
- Authorization handler's transaction-data, payment-service request and Braintree-response responsibilities: lines 30-62; illustrative JavaScript: lines 36-119.
- Local testing and generated mock data: lines 121-138.
- Trigger configuration and sandbox-versus-production deployment: lines 139-158.
- Sale selection, trigger routing, subsequent refund/void routing and Custom Fields: lines 159-193.

## Related

- [[braintree]]
- [[braintree-payment-platform]]

## Raw Sources

- [[raw/braintree/docs/guides/functions/accept-new-payment-method-2026-09-16|Braintree Functions — Accept a New Payment Method (collected 2026-09-16)]]
